<!-- MarkdownTOC -->

- [mid](#mid_)
    - [detrac-0_9       @ mid](#detrac_0_9___mi_d_)
        - [on-train       @ detrac-0_9/mid](#on_train___detrac_0_9_mid_)
        - [on-49_68       @ detrac-0_9/mid](#on_49_68___detrac_0_9_mid_)
    - [detrac-0_19       @ mid](#detrac_0_19___mi_d_)
        - [len-2       @ detrac-0_19/mid](#len_2___detrac_0_19_mi_d_)
            - [on-train       @ len-2/detrac-0_19/mid](#on_train___len_2_detrac_0_19_mi_d_)
            - [on-49_68       @ len-2/detrac-0_19/mid](#on_49_68___len_2_detrac_0_19_mi_d_)
        - [len-6-aug       @ detrac-0_19/mid](#len_6_aug___detrac_0_19_mi_d_)
            - [on-49_68       @ len-6-aug/detrac-0_19/mid](#on_49_68___len_6_aug_detrac_0_19_mi_d_)
        - [len-9       @ detrac-0_19/mid](#len_9___detrac_0_19_mi_d_)
            - [on-49_68       @ len-9/detrac-0_19/mid](#on_49_68___len_9_detrac_0_19_mi_d_)

<!-- /MarkdownTOC -->

<a id="mid_"></a>
# mid
<a id="detrac_0_9___mi_d_"></a>
## detrac-0_9       @ mid-->eval_p2s_vid-isl
<a id="on_train___detrac_0_9_mid_"></a>
### on-train       @ detrac-0_9/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty-0_9:nms:gt-1:proc-12:show-0:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-0_9/csv-batch_48:_out_-p2s-resnet_640-detrac-0_9-len-2-strd-1-0_9-strd-1-120132
`strd-2` 
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:0_9:nms:gt-1:show-0:proc-12:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-2-non_empty-seq-0_9/csv-batch_48:_out_-p2s-resnet_640-detrac-0_9-len-2-strd-1-0_9-strd-2-120132
<a id="on_49_68___detrac_0_9_mid_"></a>
### on-49_68       @ detrac-0_9/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:nms-10:gt-1:nms:show-0:proc-12:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48:_out_-p2s-resnet_640-detrac-0_9-len-2-strd-1-49_68-strd-1-120132
 `strd-2` 
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:nms-10:gt-1:nms:show-0:proc-12 :_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-2-non_empty-seq-49_68/csv-batch_48:_out_-p2s-resnet_640-detrac-0_9-len-2-strd-1-49_68-strd-2-120132


<a id="detrac_0_19___mi_d_"></a>
## detrac-0_19       @ mid-->eval_p2s_vid-isl

<a id="len_2___detrac_0_19_mi_d_"></a>
### len-2       @ detrac-0_19/mid-->eval_p2s_vid-isl
<a id="on_train___len_2_detrac_0_19_mi_d_"></a>
#### on-train       @ len-2/detrac-0_19/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty-0_19:gt-1:nms:proc-12:show-0:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-0_19/csv-batch_48:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-1-334692
`strd-2` 
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:0_19:gt-1:nms:show-0:proc-12:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-0_19/csv-batch_12:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-2-301636
<a id="on_49_68___len_2_detrac_0_19_mi_d_"></a>
#### on-49_68       @ len-2/detrac-0_19/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms:show-0:proc-12:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-1-334692
<a id="_strd_2____49_68_detrac_0_19_mi_d_"></a>
`strd-2` 
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms:show-0:proc-12 :_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-49_68/csv-batch_12:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-2-301636


<a id="len_6_aug___detrac_0_19_mi_d_"></a>
### len-6-aug       @ detrac-0_19/mid-->eval_p2s_vid-isl
<a id="on_49_68___len_6_aug_detrac_0_19_mi_d_"></a>
#### on-49_68       @ len-6-aug/detrac-0_19/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms:show-0:proc-12:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-1-334692

<a id="len_9___detrac_0_19_mi_d_"></a>
### len-9       @ detrac-0_19/mid-->eval_p2s_vid-isl
<a id="on_49_68___len_9_detrac_0_19_mi_d_"></a>
#### on-49_68       @ len-9/detrac-0_19/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:strds-9:vnms:nms-1:show-0:proc-12:_in_-resnet_640_detrac-length-9-stride-1-non_empty-seq-0_19-batch_2-lfn/ckpt-304392-detrac-length-9-stride-1-non_empty-seq-49_68/csv-batch_10:_out_-detrac-0_19-len-9-49_68




