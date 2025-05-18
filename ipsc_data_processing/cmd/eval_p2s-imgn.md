<!-- MarkdownTOC -->

- [resnet-640       @ p2s](#resnet_640___p2_s_)
    - [imagenet_vid-aug-fbb       @ resnet-640](#imagenet_vid_aug_fbb___resnet_640_)
        - [train-8_per_seq_random       @ imagenet_vid-aug-fbb/resnet-640](#train_8_per_seq_random___imagenet_vid_aug_fbb_resnet_64_0_)
        - [val-16_per_seq_random       @ imagenet_vid-aug-fbb/resnet-640](#val_16_per_seq_random___imagenet_vid_aug_fbb_resnet_64_0_)
    - [imagenet_vid_det-aug-fbb       @ resnet-640](#imagenet_vid_det_aug_fbb___resnet_640_)
        - [train-8_per_seq_random       @ imagenet_vid_det-aug-fbb/resnet-640](#train_8_per_seq_random___imagenet_vid_det_aug_fbb_resnet_64_0_)
        - [train-ratio_1_10_random       @ imagenet_vid_det-aug-fbb/resnet-640](#train_ratio_1_10_random___imagenet_vid_det_aug_fbb_resnet_64_0_)
        - [val-16_per_seq_random       @ imagenet_vid_det-aug-fbb/resnet-640](#val_16_per_seq_random___imagenet_vid_det_aug_fbb_resnet_64_0_)
    - [imagenet_vid_det-aug       @ resnet-640](#imagenet_vid_det_aug___resnet_640_)
        - [train-ratio_1_10_random       @ imagenet_vid_det-aug/resnet-640](#train_ratio_1_10_random___imagenet_vid_det_aug_resnet_64_0_)
        - [val-16_per_seq_random       @ imagenet_vid_det-aug/resnet-640](#val_16_per_seq_random___imagenet_vid_det_aug_resnet_64_0_)

<!-- /MarkdownTOC -->
<a id="resnet_640___p2_s_"></a>
# resnet-640       @ p2s-->eval_det_p2s
<a id="imagenet_vid_aug_fbb___resnet_640_"></a>
## imagenet_vid-aug-fbb       @ resnet-640-->eval_p2s-imgn
<a id="train_8_per_seq_random___imagenet_vid_aug_fbb_resnet_64_0_"></a>
### train-8_per_seq_random       @ imagenet_vid-aug-fbb/resnet-640-->eval_p2s-imgn
python3 eval_det.py cfg=p2s,imagenet_vid:8_per_seq_random:nms-1:gt-0:agn:proc-1:_in_-resnet_640_imagenet_vid-batch_512-jtr-res_1440-fbb-zexg/ckpt-__var__-imagenet_vid-8_per_seq_random/csv-batch_8:_out_-p2s-imagenet_vid-train-8_per_seq_random-aug-fbb:ief allow_empty_gt=1
<a id="val_16_per_seq_random___imagenet_vid_aug_fbb_resnet_64_0_"></a>
### val-16_per_seq_random       @ imagenet_vid-aug-fbb/resnet-640-->eval_p2s-imgn
python3 eval_det.py cfg=p2s,imagenet_vid:val:16_per_seq_random:nms-1:gt-0:agn:proc-1:_in_-resnet_640_imagenet_vid-batch_512-jtr-res_1440-fbb-zexg/ckpt-__var__-imagenet_vid_val-16_per_seq_random/csv-batch_8:_out_-p2s-imagenet_vid-val-16_per_seq_random-aug-fbb:ief

<a id="imagenet_vid_det_aug_fbb___resnet_640_"></a>
## imagenet_vid_det-aug-fbb       @ resnet-640-->eval_p2s-imgn
<a id="train_8_per_seq_random___imagenet_vid_det_aug_fbb_resnet_64_0_"></a>
### train-8_per_seq_random       @ imagenet_vid_det-aug-fbb/resnet-640-->eval_p2s-imgn
python3 eval_det.py cfg=p2s,imagenet_vid:det:8_per_seq_random:nms-1:gt-0:agn:proc-1:_in_-resnet_640_imagenet_vid_det-sampled_eq-batch_448-jtr-res_1440-fbb-self2-0/ckpt-__var__-imagenet_vid_det-8_per_seq_random/csv-batch_16:_out_-p2s-imagenet_vid_det-train-8_per_seq_random-aug-fbb allow_empty_gt=1
<a id="train_ratio_1_10_random___imagenet_vid_det_aug_fbb_resnet_64_0_"></a>
### train-ratio_1_10_random       @ imagenet_vid_det-aug-fbb/resnet-640-->eval_p2s-imgn
python3 eval_det.py cfg=p2s,imagenet_vid:det:ratio_1_10_random:nms-1:gt-0:agn:proc-1:_in_-resnet_640_imagenet_vid_det-sampled_eq-batch_448-jtr-res_1440-fbb-self2-0/ckpt-__var__-imagenet_vid_det-ratio_1_10_random/csv-batch_32:_out_-p2s-imagenet_vid_det-train-ratio_1_10_random-aug-fbb allow_empty_gt=1
<a id="val_16_per_seq_random___imagenet_vid_det_aug_fbb_resnet_64_0_"></a>
### val-16_per_seq_random       @ imagenet_vid_det-aug-fbb/resnet-640-->eval_p2s-imgn
python3 eval_det.py cfg=p2s,imagenet_vid:val:16_per_seq_random:nms-1:gt-0:agn:proc-1:_in_-resnet_640_imagenet_vid_det-sampled_eq-batch_448-jtr-res_1440-fbb-self2-0/ckpt-__var__-imagenet_vid_val-16_per_seq_random/csv-batch_16:_out_-p2s-imagenet_vid_det-val-16_per_seq_random-aug-fbb

<a id="imagenet_vid_det_aug___resnet_640_"></a>
## imagenet_vid_det-aug       @ resnet-640-->eval_p2s-imgn
<a id="train_ratio_1_10_random___imagenet_vid_det_aug_resnet_64_0_"></a>
### train-ratio_1_10_random       @ imagenet_vid_det-aug/resnet-640-->eval_p2s-imgn
python3 eval_det.py cfg=p2s,imagenet_vid:det:ratio_1_10_random:nms-1:gt-0:agn:proc-1:_in_-resnet_640_imagenet_vid_det-sampled_eq-batch_144-jtr-res_1440-zexg/ckpt-__var__-imagenet_vid_det-ratio_1_10_random/csv-batch_32:_out_-p2s-imagenet_vid_det-train-ratio_1_10_random-aug allow_empty_gt=1
<a id="val_16_per_seq_random___imagenet_vid_det_aug_resnet_64_0_"></a>
### val-16_per_seq_random       @ imagenet_vid_det-aug/resnet-640-->eval_p2s-imgn
python3 eval_det.py cfg=p2s,imagenet_vid:val:16_per_seq_random:nms-1:gt-0:agn:proc-1:_in_-resnet_640_imagenet_vid_det-sampled_eq-batch_144-jtr-res_1440-zexg/ckpt-__var__-imagenet_vid_val-16_per_seq_random/csv-batch_16:_out_-p2s-imagenet_vid_det-val-16_per_seq_random-aug

