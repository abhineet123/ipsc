import shutil
import os
import sys

swin_det_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f'swin_det_dir: {swin_det_dir}')
sys.path.append(swin_det_dir)

home_path = os.path.expanduser('~')
deep_mdp_path = os.path.join(home_path, 'isl_labeling_tool', 'deep_mdp')
sys.path.append(deep_mdp_path)

from tqdm import tqdm
import time
import copy
import cv2
from datetime import datetime

import torch
from mmcv import Config
from mmcv.cnn import fuse_conv_bn
from mmcv.runner import init_dist, load_checkpoint, wrap_fp16_model

from mmdet.datasets import replace_ImageToTensor

from mmdet.models import build_detector

from input import Input
from objects import Annotations
from data import Data
from utilities import CustomLogger, linux_path

import numpy as np

import paramparse

flatten = torch.nn.Flatten()
avg_pool_8 = torch.nn.AdaptiveAvgPool2d(output_size=(8, 8))
avg_pool_4 = torch.nn.AdaptiveAvgPool2d(output_size=(4, 4))
avg_pool_2 = torch.nn.AdaptiveAvgPool2d(output_size=(2, 2))


class Params:
    class SlidingWindow:
        sample = 0
        size = 0
        stride = 0
        num = 0

    def __init__(self):
        self.cfg = ('',)

        self.set = ''
        self.seq = ()
        self.start_seq = 0
        self.end_seq = -1

        self.config = ''
        self.ckpt = ''
        self.ckpt_dir = ''
        self.ckpt_name = ''
        self.cfg_options = None
        # self.eval = ["bbox", "segm"]
        self.eval = []
        self.eval_options = {
            "classwise": True
        }
        self.format_only = False
        self.fuse_conv_bn = False
        self.gpu_collect = False
        self.launcher = 'none'
        self.local_rank = 0
        self.multi_run = 0
        self.options = None
        self.out = None
        self.show = 0
        self.batch_size = 1
        self.out_dir = ''
        self.out_name = ''
        self.out_suffix = ''
        self.tmpdir = ''
        self.n_proc = 1
        self.test_name = 'val'
        self.feat_name = 'neck'
        self.reduce = 'f3'

        self.slide = Params.SlidingWindow()

        self.input = Input.Params(source_type=-1, batch_mode=False)
        self.data = Data.Params()
        self.ann = Annotations.Params()


def run(seq_info,
        model,
        params,
        ):
    """
    :param seq_info:
    :param model:
    :param Params params:
    :return:
    """
    model.eval()

    seq_id, start_id, end_id = seq_info

    _logger = CustomLogger.setup(__name__)

    _data = Data(params.data, _logger)

    if not _data.initialize(params.set, seq_id, 0, _logger, silent=1):
        _logger.error('Data module could not be initialized')
        return None

    subset = "training" if _data.split == 'train' else "validation"

    input_params = copy.deepcopy(params.input)  # type: Input.Params

    """end_id is exclusive but Input expects inclusive"""
    input_params.frame_ids = (start_id, end_id - 1)

    _input = Input(input_params, _logger)
    seq_name = _data.seq_name

    print(f'\nseq {seq_id + 1}: {seq_name}\n')

    if not _input.initialize(_data):
        _logger.error('Input pipeline could not be initialized')
        return False

    # read detections and annotations
    if not _input.read_annotations():
        _logger.error('Annotations could not be read')
        return False

    # if not _input.read_detections():
    #     _logger.error('Detections could not be read')
    #     return False

    _frame_size = _input.frame_size
    _n_frames = _input.n_frames

    _annotations = _input.annotations  # type: Annotations

    n_images = _input.n_frames
    n_batches = int(n_images / params.batch_size)

    _input._read_all_frames()

    frame_iter = _input.read_iter(length=params.batch_size)

    feat_name = params.feat_name

    out_name = f'{seq_name}--{start_id}_{end_id}.npy'

    out_path = linux_path(params.out_dir, out_name)

    pbar = tqdm(frame_iter, total=n_batches)
    reduced_feat_list = []
    for batch_id, img_list in enumerate(pbar):
        img = np.stack(img_list, axis=0)
        """bring channel to front"""
        img_reshaped = img.transpose([0, 3, 1, 2])
        img_tensor = torch.tensor(img_reshaped, dtype=torch.float32).cuda()

        with torch.no_grad():
            final_feat = model.extract_feat(img_tensor)
            feat_list = model.features[feat_name]
            if params.reduce == 'f3':
                reduced_feat = f3(feat_list)
            elif params.reduce == 'f3_8':
                reduced_feat = f3_8(feat_list)
            elif params.reduce == 'avg_all':
                reduced_feat = avg_all(feat_list)
            else:
                raise AssertionError(f'invalid reduce type: {params.reduce}')

            reduced_feat_np = reduced_feat.cpu().numpy()

            reduced_feat_list.append(reduced_feat_np)

    reduced_feat_all = np.concatenate(reduced_feat_list, axis=0)

    np.save(out_path, reduced_feat_all)


def avg_all(feat_list):
    avg_pool_feats = []
    for feat in feat_list:
        avg_pool_feat = avg_pool_2(feat, (2, 2))
        avg_pool_feat_flat = torch.flatten(avg_pool_feat)
        avg_pool_feats.append(avg_pool_feat_flat)
    print()
    return avg_pool_feats


def f3_8(feat_list):
    flatten = torch.nn.Flatten()
    feat = feat_list[3]
    feat_pooled = avg_pool_8(feat)
    feat_flat = flatten(feat_pooled)
    return feat_flat


def f3(feat_list):
    # avg_pool = torch.nn.AdaptiveAvgPool2d(output_size=(8, 8))
    feat = feat_list[3]
    # feat_pooled = avg_pool(feat)
    feat_flat = flatten(feat)
    return feat_flat


def main():
    params = Params()
    paramparse.process(params)

    if 'LOCAL_RANK' not in os.environ:
        os.environ['LOCAL_RANK'] = str(params.local_rank)

    config_name = os.path.splitext(os.path.basename(params.config))[0]

    if not params.ckpt:
        if not params.ckpt_dir:
            params.ckpt_dir = linux_path('work_dirs', config_name)
        if not params.ckpt_name:
            params.ckpt_name = 'latest.pth'

        params.ckpt = linux_path(params.ckpt_dir, params.ckpt_name)

    checkpoint_dir = os.path.dirname(params.ckpt)
    checkpoint_name = os.path.splitext(os.path.basename(params.ckpt))[0]
    if not params.out_name:
        params.out_name = 'features'

    if params.out_suffix:
        params.out_name = f'{params.out_name}_{params.out_suffix}'

    if not params.out_dir:
        params.out_dir = linux_path(checkpoint_dir, f'{checkpoint_name}_on_{params.test_name}')

    params.out_dir = linux_path(params.out_dir, params.out_name)

    print(f'writing features to {params.out_dir}')

    exit()

    os.makedirs(params.out_dir, exist_ok=1)

    if True:
        cfg = Config.fromfile(params.config)
        if params.cfg_options is not None:
            cfg.merge_from_dict(params.cfg_options)
        # import modules from string list.
        if cfg.get('custom_imports', None):
            from mmcv.utils import import_modules_from_strings
            import_modules_from_strings(**cfg['custom_imports'])
        # set cudnn_benchmark
        if cfg.get('cudnn_benchmark', False):
            torch.backends.cudnn.benchmark = True
        cfg.model.pretrained = None
        if cfg.model.get('neck'):
            if isinstance(cfg.model.neck, list):
                for neck_cfg in cfg.model.neck:
                    if neck_cfg.get('rfp_backbone'):
                        if neck_cfg.rfp_backbone.get('pretrained'):
                            neck_cfg.rfp_backbone.pretrained = None
            elif cfg.model.neck.get('rfp_backbone'):
                if cfg.model.neck.rfp_backbone.get('pretrained'):
                    cfg.model.neck.rfp_backbone.pretrained = None

        # in case the test dataset is concatenated
        samples_per_gpu = params.batch_size
        test_data_cfg = cfg.data[params.test_name]
        if isinstance(test_data_cfg, dict):
            test_data_cfg.test_mode = True
            samples_per_gpu = test_data_cfg.pop('samples_per_gpu', 1)
            if samples_per_gpu > 1:
                # Replace 'ImageToTensor' to 'DefaultFormatBundle'
                test_data_cfg.pipeline = replace_ImageToTensor(
                    test_data_cfg.pipeline)
        elif isinstance(test_data_cfg, list):
            for ds_cfg in test_data_cfg:
                ds_cfg.test_mode = True
            samples_per_gpu = max(
                [ds_cfg.pop('samples_per_gpu', 1) for ds_cfg in test_data_cfg])
            if samples_per_gpu > 1:
                for ds_cfg in test_data_cfg:
                    ds_cfg.pipeline = replace_ImageToTensor(ds_cfg.pipeline)

        # init distributed env first, since logger depends on the dist info.
        if params.launcher == 'none':
            distributed = False
        else:
            distributed = True
            init_dist(params.launcher, **cfg.dist_params)

        # build the model and load checkpoint
        cfg.model.train_cfg = None
        model = build_detector(cfg.model, test_cfg=cfg.get('test_cfg'))
        fp16_cfg = cfg.get('fp16', None)
        if fp16_cfg is not None:
            wrap_fp16_model(model)
        checkpoint = load_checkpoint(model, params.ckpt, map_location='cpu')
        if params.fuse_conv_bn:
            model = fuse_conv_bn(model)
        model = model.cuda()

    _logger = CustomLogger.setup(__name__)
    _data = Data(params.data, _logger)

    try:
        params.set = int(params.set)
    except ValueError:
        params.set = params.data.name_to_id(params.set)

    set_name = _data.sets[params.set]
    n_sequences = len(_data.sequences[set_name])

    seq_ids = params.seq

    if not seq_ids:
        seq_ids = tuple(range(n_sequences))

    if params.start_seq < 0:
        params.start_seq = 0

    if params.end_seq < 0:
        params.end_seq = len(seq_ids) - 1

    seq_ids = seq_ids[params.start_seq:params.end_seq + 1]

    sample = params.slide.sample
    if sample <= 0:
        sample = 1

    seq_info_list = []
    pbar = tqdm(seq_ids)
    for seq_id in pbar:

        if not _data.initialize(params.set, seq_id, 0, _logger, silent=1):
            _logger.error('Data module could not be initialized')
            return None

        start_id = 0
        seq_name = _data.seq_name
        seq_n_frames = _data.seq_n_frames

        assert seq_n_frames % sample == 0, f"sample size {sample} does not divide seq_n_frames {seq_n_frames} evenly"

        win_size = params.slide.size
        if win_size <= 0:
            win_size = int(_data.seq_n_frames / sample)

        win_stride = params.slide.stride
        if win_stride <= 0:
            win_stride = win_size

        win_id = 0
        while True:
            abs_start_id = int(start_id * sample)

            if abs_start_id >= seq_n_frames or win_id >= params.slide.num > 0:
                break

            end_id = start_id + win_size

            abs_end_id = int(end_id * sample)

            if abs_end_id >= seq_n_frames:
                abs_end_id = seq_n_frames
                end_id = int(abs_end_id / sample)

            # suffix = f'{abs_start_id}_{abs_end_id}'

            seq_info_list.append((seq_id, abs_start_id, abs_end_id))

            # print(f'{seq_name}--{suffix}: {abs_start_id} to {abs_end_id}')

            start_id += win_stride

            win_id += 1

    n_seq = len(seq_info_list)

    # exit()

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S_%f")
    out_dir = linux_path('log', f'mot_to_dnc', f'{set_name}_{timestamp}')
    os.makedirs(out_dir, exist_ok=1)

    traj_lengths_out_dir = linux_path(out_dir, 'traj_lengths')
    os.makedirs(traj_lengths_out_dir, exist_ok=1)

    n_proc = min(params.n_proc, n_seq)

    import functools
    func = functools.partial(
        run,
        params=params,
        model=model,
    )

    if n_proc > 1:
        import multiprocessing

        print(f'running in parallel over {n_proc} processes')
        with multiprocessing.Pool(n_proc) as pool:
            results = pool.map(func, seq_info_list)

        results.sort(key=lambda x: x[0])
    else:
        results = []
        for seq_info in seq_info_list:
            result = func(seq_info)

            results.append(result)


if __name__ == '__main__':
    main()
