<!-- MarkdownTOC -->

- [lfn       @ lfn](#lfn___lf_n_)
    - [len-2-fbb       @ lfn](#len_2_fbb___lf_n_)
        - [on-train-4_per_seq_random_len_2       @ len-2-fbb/lfn](#on_train_4_per_seq_random_len_2___len_2_fbb_lf_n_)
        - [on-val-8_per_seq_random_len_2       @ len-2-fbb/lfn](#on_val_8_per_seq_random_len_2___len_2_fbb_lf_n_)
        - [on-val       @ len-2-fbb/lfn](#on_val___len_2_fbb_lf_n_)
            - [txt       @ on-val/len-2-fbb/lfn](#txt___on_val_len_2_fbb_lfn_)
    - [len-2-fbb-cls_eq       @ lfn](#len_2_fbb_cls_eq___lf_n_)
        - [on-train-4_per_seq_random_len_2       @ len-2-fbb-cls_eq/lfn](#on_train_4_per_seq_random_len_2___len_2_fbb_cls_eq_lfn_)
        - [on-val-8_per_seq_random_len_2       @ len-2-fbb-cls_eq/lfn](#on_val_8_per_seq_random_len_2___len_2_fbb_cls_eq_lfn_)
    - [len-2-fbb-cls_eq-isc       @ lfn](#len_2_fbb_cls_eq_isc___lf_n_)
        - [on-train-4_per_seq_random_len_2       @ len-2-fbb-cls_eq-isc/lfn](#on_train_4_per_seq_random_len_2___len_2_fbb_cls_eq_isc_lfn_)
        - [on-val-8_per_seq_random_len_2       @ len-2-fbb-cls_eq-isc/lfn](#on_val_8_per_seq_random_len_2___len_2_fbb_cls_eq_isc_lfn_)
    - [len-2-fbb-aug       @ lfn](#len_2_fbb_aug___lf_n_)
        - [on-train-4_per_seq_random_len_2       @ len-2-fbb-aug/lfn](#on_train_4_per_seq_random_len_2___len_2_fbb_aug_lf_n_)
        - [on-val-8_per_seq_random_len_2       @ len-2-fbb-aug/lfn](#on_val_8_per_seq_random_len_2___len_2_fbb_aug_lf_n_)

<!-- /MarkdownTOC -->

<a id="lfn___lf_n_"></a>
# lfn       @ lfn-->eval_p2s_vid-isl
<a id="len_2_fbb___lf_n_"></a>
## len-2-fbb       @ lfn-->eval_p2s_vid-imgn
<a id="on_train_4_per_seq_random_len_2___len_2_fbb_lf_n_"></a>
### on-train-4_per_seq_random_len_2       @ len-2-fbb/lfn-->eval_p2s_vid-imgn
`batch-32`
python3 eval_det.py cfg=p2s:vid,imagenet_vid:4_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-lfn-self2-0/ckpt-__var__-imagenet_vid-length-2-stride-2-4_per_seq_random_len_2/csv-batch_32:_out_-p2s-lfn-imagenet_vid-len-2-train-4_per_seq_random_len_2-fbb allow_empty_gt=1
`batch-64`
python3 eval_det.py cfg=p2s:vid,imagenet_vid:4_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-lfn-self2-0/ckpt-__var__-imagenet_vid-length-2-stride-2-4_per_seq_random_len_2/csv-batch_64:_out_-p2s-lfn-imagenet_vid-len-2-train-4_per_seq_random_len_2-fbb allow_empty_gt=1
<a id="on_val_8_per_seq_random_len_2___len_2_fbb_lf_n_"></a>
### on-val-8_per_seq_random_len_2       @ len-2-fbb/lfn-->eval_p2s_vid-imgn
`batch-32`
python3 eval_det.py cfg=p2s:vid,imagenet_vid:val:8_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-lfn-self2-0/ckpt-__var__-imagenet_vid_val-length-2-stride-2-8_per_seq_random_len_2/csv-batch_32:_out_-p2s-lfn-imagenet_vid-len-2-val-8_per_seq_random_len_2-fbb allow_empty_gt=1
`batch-64`
python3 eval_det.py cfg=p2s:vid,imagenet_vid:val:8_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-lfn-self2-0/ckpt-__var__-imagenet_vid_val-length-2-stride-2-8_per_seq_random_len_2/csv-batch_64:_out_-p2s-lfn-imagenet_vid-len-2-val-8_per_seq_random_len_2-fbb allow_empty_gt=1
<a id="on_val___len_2_fbb_lf_n_"></a>
### on-val       @ len-2-fbb/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:val:gt-0:nms-1:vnms:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-lfn-self2-0/ckpt-__var__-imagenet_vid_val-length-2-stride-1/csv-batch_32:_out_-p2s-lfn-imagenet_vid-len-2-val-fbb-strd-1-vnms-25:vbs:dbg 
<a id="txt___on_val_len_2_fbb_lfn_"></a>
#### txt       @ on-val/len-2-fbb/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:val:gt-0:nms-0:vnms:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-lfn-self2-0/ckpt-__var__-imagenet_vid_val-length-2-stride-1/csv-batch_32:_out_-p2s-lfn-imagenet_vid-len-2-val-fbb-strd-1-vnms-25-txt:vbs:dbg:txt



<a id="len_2_fbb_cls_eq___lf_n_"></a>
## len-2-fbb-cls_eq       @ lfn-->eval_p2s_vid-imgn
<a id="on_train_4_per_seq_random_len_2___len_2_fbb_cls_eq_lfn_"></a>
### on-train-4_per_seq_random_len_2       @ len-2-fbb-cls_eq/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:4_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_288-fbb-cls_eq-lfn-zexg/ckpt-__var__-imagenet_vid-length-2-stride-2-4_per_seq_random_len_2/csv-batch_16:_out_-p2s-lfn-imagenet_vid-len-2-train-4_per_seq_random_len_2-fbb-cls_eq allow_empty_gt=1
<a id="on_val_8_per_seq_random_len_2___len_2_fbb_cls_eq_lfn_"></a>
### on-val-8_per_seq_random_len_2       @ len-2-fbb-cls_eq/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:val:8_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_288-fbb-cls_eq-lfn-zexg/ckpt-__var__-imagenet_vid_val-length-2-stride-2-8_per_seq_random_len_2/csv-batch_16:_out_-p2s-lfn-imagenet_vid-len-2-val-8_per_seq_random_len_2-fbb-cls_eq allow_empty_gt=1

<a id="len_2_fbb_cls_eq_isc___lf_n_"></a>
## len-2-fbb-cls_eq-isc       @ lfn-->eval_p2s_vid-imgn
<a id="on_train_4_per_seq_random_len_2___len_2_fbb_cls_eq_isc_lfn_"></a>
### on-train-4_per_seq_random_len_2       @ len-2-fbb-cls_eq-isc/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:4_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-cls_eq-lfn-self2-0/ckpt-__var__-imagenet_vid-length-2-stride-2-4_per_seq_random_len_2/csv-batch_16:_out_-p2s-lfn-imagenet_vid-len-2-train-4_per_seq_random_len_2-fbb-cls_eq allow_empty_gt=1
<a id="on_val_8_per_seq_random_len_2___len_2_fbb_cls_eq_isc_lfn_"></a>
### on-val-8_per_seq_random_len_2       @ len-2-fbb-cls_eq-isc/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:val:8_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_256-fbb-cls_eq-lfn-self2-0/ckpt-__var__-imagenet_vid_val-length-2-stride-2-8_per_seq_random_len_2/csv-batch_16:_out_-p2s-lfn-imagenet_vid-len-2-val-8_per_seq_random_len_2-fbb-cls_eq allow_empty_gt=1


<a id="len_2_fbb_aug___lf_n_"></a>
## len-2-fbb-aug       @ lfn-->eval_p2s_vid-imgn
<a id="on_train_4_per_seq_random_len_2___len_2_fbb_aug_lf_n_"></a>
### on-train-4_per_seq_random_len_2       @ len-2-fbb-aug/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:4_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_288-fbb-jtr-res_1440-lfn-zexg/ckpt-__var__-imagenet_vid-length-2-stride-2-4_per_seq_random_len_2/csv-batch_8:_out_-p2s-lfn-imagenet_vid-len-2-train-4_per_seq_random_len_2-fbb-aug allow_empty_gt=1
<a id="on_val_8_per_seq_random_len_2___len_2_fbb_aug_lf_n_"></a>
### on-val-8_per_seq_random_len_2       @ len-2-fbb-aug/lfn-->eval_p2s_vid-imgn
python3 eval_det.py cfg=p2s:vid,imagenet_vid:val:8_per_seq_random_len_2:gt-0:nms-1:agn:show-0:proc-1:_in_-resnet_640_imagenet_vid-length-2-stride-1-batch_288-fbb-jtr-res_1440-lfn-zexg/ckpt-__var__-imagenet_vid_val-length-2-stride-2-8_per_seq_random_len_2/csv-batch_8:_out_-p2s-lfn-imagenet_vid-len-2-val-8_per_seq_random_len_2-fbb-aug allow_empty_gt=1

