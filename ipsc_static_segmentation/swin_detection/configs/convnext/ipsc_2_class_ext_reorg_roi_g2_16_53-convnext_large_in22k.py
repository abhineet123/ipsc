# Copyright (c) Meta Platforms, Inc. and affiliates.

# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


_base_ = [
    '../_base_/models/cascade_mask_rcnn_convnext_fpn_ipsc_2_class.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

dataset_type = 'IPSC2Class'
data_root = '/data/ipsc/well3/all_frames_roi/'
data_root_test = '/data/ipsc/'

model = dict(
    backbone=dict(
        in_chans=3,
        depths=[3, 3, 27, 3], 
        dims=[192, 384, 768, 1536], 
        drop_path_rate=0.7,
        layer_scale_init_value=1.0,
        out_indices=[0, 1, 2, 3],
    ),
    neck=dict(in_channels=[192, 384, 768, 1536]),
    roi_head=dict(
        bbox_head=[
            dict(
                type='ConvFCBBoxHead',
                num_shared_convs=4,
                num_shared_fcs=1,
                in_channels=256,
                conv_out_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=2,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.1, 0.1, 0.2, 0.2]),
                reg_class_agnostic=False,
                reg_decoded_bbox=True,
                norm_cfg=dict(type='SyncBN', requires_grad=True),
                loss_cls=dict(
                    type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
                loss_bbox=dict(type='GIoULoss', loss_weight=10.0)),
            dict(
                type='ConvFCBBoxHead',
                num_shared_convs=4,
                num_shared_fcs=1,
                in_channels=256,
                conv_out_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=2,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.05, 0.05, 0.1, 0.1]),
                reg_class_agnostic=False,
                reg_decoded_bbox=True,
                norm_cfg=dict(type='SyncBN', requires_grad=True),
                loss_cls=dict(
                    type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
                loss_bbox=dict(type='GIoULoss', loss_weight=10.0)),
            dict(
                type='ConvFCBBoxHead',
                num_shared_convs=4,
                num_shared_fcs=1,
                in_channels=256,
                conv_out_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=2,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.033, 0.033, 0.067, 0.067]),
                reg_class_agnostic=False,
                reg_decoded_bbox=True,
                norm_cfg=dict(type='SyncBN', requires_grad=True),
                loss_cls=dict(
                    type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
                loss_bbox=dict(type='GIoULoss', loss_weight=10.0))
        ]))

img_norm_cfg = dict(
    mean=[126.21, 126.21, 126.21],
    std=[19.33, 19.33, 19.33],
    to_rgb=True)

# augmentation strategy originates from DETR / Sparse RCNN
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='AutoAugment',
         policies=[
             [
                 dict(type='Resize',
                      img_scale=[(480, 1333), (512, 1333), (544, 1333), (576, 1333),
                                 (608, 1333), (640, 1333), (672, 1333), (704, 1333),
                                 (736, 1333), (768, 1333), (800, 1333)],
                      multiscale_mode='value',
                      keep_ratio=True)
             ],
             [
                 dict(type='Resize',
                      img_scale=[(400, 1333), (500, 1333), (600, 1333)],
                      multiscale_mode='value',
                      keep_ratio=True),
                 dict(type='RandomCrop',
                      crop_type='absolute_range',
                      crop_size=(384, 600),
                      allow_negative_crop=True),
                 dict(type='Resize',
                      img_scale=[(480, 1333), (512, 1333), (544, 1333),
                                 (576, 1333), (608, 1333), (640, 1333),
                                 (672, 1333), (704, 1333), (736, 1333),
                                 (768, 1333), (800, 1333)],
                      multiscale_mode='value',
                      override=True,
                      keep_ratio=True)
             ]
         ]),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
optimizer = dict(constructor='LearningRateDecayOptimizerConstructor', _delete_=True, type='AdamW',
                 lr=0.0001, betas=(0.9, 0.999), weight_decay=0.05,
                 paramwise_cfg={'decay_rate': 0.7,
                                'decay_type': 'layer_wise',
                                'num_layers': 12})
lr_config = dict(step=[27, 33])
runner = dict(type='EpochBasedRunnerAmp', max_epochs=10000)

# do not use mmdet version fp16
# fp16 = None
# optimizer_config = dict(
#     type="DistOptimizerHook",
#     update_interval=1,
#     grad_clip=None,
#     coalesce=True,
#     bucket_size_mb=-1,
#     use_fp16=False,
# )

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(666, 400),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'ext_reorg_roi_g2_16_53.json',
        img_prefix=data_root,
        pipeline=train_pipeline),
    val=dict(
        samples_per_gpu=1,
        type=dataset_type,
        ann_file=data_root + 'ext_reorg_roi_g2_0_15.json',
        img_prefix=data_root,
        pipeline=test_pipeline),

    g2_0_15=dict(
        samples_per_gpu=1,
        type=dataset_type,
        ann_file=data_root + 'ext_reorg_roi_g2_0_15.json',
        img_prefix=data_root,
        pipeline=test_pipeline),

    Test_230606=dict(
        samples_per_gpu=1,
        type=dataset_type,
        ann_file=data_root_test + 'Test_230606.json',
        img_prefix=data_root_test,
        pipeline=test_pipeline),

    Test_230710=dict(
        samples_per_gpu=1,
        type=dataset_type,
        ann_file=data_root_test + 'Test_230710.json',
        img_prefix=data_root_test,
        pipeline=test_pipeline),

)

evaluation = dict(metric=['bbox', 'segm'])
