<!-- MarkdownTOC -->

- [mid](#mid_)
    - [detrac-0_9       @ mid](#detrac_0_9___mi_d_)
        - [on-train       @ detrac-0_9/mid](#on_train___detrac_0_9_mid_)
        - [on-49_68       @ detrac-0_9/mid](#on_49_68___detrac_0_9_mid_)
    - [detrac-0_19-len-2       @ mid](#detrac_0_19_len_2___mi_d_)
        - [on-train       @ detrac-0_19-len-2/mid](#on_train___detrac_0_19_len_2_mi_d_)
        - [on-49_68       @ detrac-0_19-len-2/mid](#on_49_68___detrac_0_19_len_2_mi_d_)
        - [on-49_68-rerun       @ detrac-0_19-len-2/mid](#on_49_68_rerun___detrac_0_19_len_2_mi_d_)
    - [detrac-0_48-len-16-seq3k       @ mid](#detrac_0_48_len_16_seq3k___mi_d_)
        - [on-49_85       @ detrac-0_48-len-16-seq3k/mid](#on_49_85___detrac_0_48_len_16_seq3k_mid_)
    - [detrac-0_48-len-32-fbb-seq5k       @ mid](#detrac_0_48_len_32_fbb_seq5k___mi_d_)
        - [on-49_85-strd-32       @ detrac-0_48-len-32-fbb-seq5k/mid](#on_49_85_strd_32___detrac_0_48_len_32_fbb_seq5k_mid_)
    - [detrac-0_9-1d       @ mid](#detrac_0_9_1d___mi_d_)
        - [on-49_68       @ detrac-0_9-1d/mid](#on_49_68___detrac_0_9_1d_mi_d_)
    - [detrac-0_48-len-64-1d       @ mid](#detrac_0_48_len_64_1d___mi_d_)
        - [on-49_85       @ detrac-0_48-len-64-1d/mid](#on_49_85___detrac_0_48_len_64_1d_mi_d_)
- [lfn](#lfn_)
    - [len-6-aug       @ lfn](#len_6_aug___lf_n_)
        - [on-49_68       @ len-6-aug/lfn](#on_49_68___len_6_aug_lf_n_)
    - [len-9       @ lfn](#len_9___lf_n_)
        - [on-49_68       @ len-9/lfn](#on_49_68___len_9_lf_n_)

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


<a id="detrac_0_19_len_2___mi_d_"></a>
## detrac-0_19-len-2       @ mid-->eval_p2s_vid-isl
<a id="on_train___detrac_0_19_len_2_mi_d_"></a>
### on-train       @ detrac-0_19-len-2/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty-0_19:gt-1:nms:proc-12:show-0:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-0_19/csv-batch_48:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-1-334692
`strd-2` 
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:0_19:gt-1:nms:show-0:proc-12:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-0_19/csv-batch_12:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-2-301636
<a id="on_49_68___detrac_0_19_len_2_mi_d_"></a>
### on-49_68       @ detrac-0_19-len-2/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms:show-0:proc-12:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-1-334692
`strd-2` 
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms:show-0:proc-12 :_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-49_68/csv-batch_12:_out_-p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-2-301636
<a id="on_49_68_rerun___detrac_0_19_len_2_mi_d_"></a>
### on-49_68-rerun       @ detrac-0_19-len-2/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:det-0:vnms-1:nms-0:show-0:proc-1:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_12:_out_-p2s-mid-detrac-0_19-len-2-49_68

<a id="detrac_0_48_len_16_seq3k___mi_d_"></a>
## detrac-0_48-len-16-seq3k       @ mid-->eval_p2s_vid-isl
<a id="on_49_85___detrac_0_48_len_16_seq3k_mid_"></a>
### on-49_85       @ detrac-0_48-len-16-seq3k/mid-->eval_p2s_vid-isl
`strd-16`
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_85:gt-0:nms-1:vnms:show-0:proc-1:_in_-resnet_640_detrac-length-16-stride-1-non_empty-seq-0_48-batch_6-seq3k-exp/ckpt-__var__-detrac-length-16-stride-16-non_empty-seq-49_85/csv-batch_6:_out_-p2s-detrac-0_48-len-16-49_85-strd-16-seq3k
`strd-1`
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_85:gt-0:nms-1:vnms:show-0:proc-1:_in_-resnet_640_detrac-length-16-stride-1-non_empty-seq-0_48-batch_6-seq3k-exp/ckpt-__var__-detrac-length-16-stride-1-non_empty-seq-49_85/csv-batch_8:_out_-p2s-detrac-0_48-len-16-49_85-strd-1-seq3k

<a id="detrac_0_48_len_32_fbb_seq5k___mi_d_"></a>
## detrac-0_48-len-32-fbb-seq5k       @ mid-->eval_p2s_vid-isl
<a id="on_49_85_strd_32___detrac_0_48_len_32_fbb_seq5k_mid_"></a>
### on-49_85-strd-32       @ detrac-0_48-len-32-fbb-seq5k/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_85:gt-0:nms-1:vnms:show-0:proc-1:_in_-resnet_640_detrac-length-32-stride-1-non_empty-seq-0_48-batch_6-seq5k-fbb-gxe/ckpt-__var__-detrac-length-32-stride-32-non_empty-seq-49_85/csv-batch_8:_out_-p2s-detrac-0_48-len-32-49_85-strd-32-fbb

<a id="detrac_0_9_1d___mi_d_"></a>
## detrac-0_9-1d       @ mid-->eval_p2s_vid-isl
<a id="on_49_68___detrac_0_9_1d_mi_d_"></a>
### on-49_68       @ detrac-0_9-1d/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-0:nms-1:vnms-1:agn:show-0:proc-1:_in_-resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_8-quant_160-1d/ckpt-__var__-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_24:_out_-p2s-detrac-0_9-len-2-49_68-strd-1-fbb-1d

<a id="detrac_0_48_len_64_1d___mi_d_"></a>
## detrac-0_48-len-64-1d       @ mid-->eval_p2s_vid-isl
<a id="on_49_85___detrac_0_48_len_64_1d_mi_d_"></a>
### on-49_85       @ detrac-0_48-len-64-1d/mid-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_85:gt-0:nms-1:vnms:agn:show-0:proc-1:_in_-resnet_640_detrac-length-64-stride-1-non_empty-seq-0_48-batch_6-quant_160-1d-seq4k-fbb-exg/ckpt-__var__-detrac-length-64-stride-64-non_empty-seq-49_85/csv-batch_4:_out_-p2s-detrac-0_48-len-64-49_85-strd-64-fbb-1d

<a id="lfn_"></a>
# lfn 

<a id="len_6_aug___lf_n_"></a>
## len-6-aug       @ lfn-->eval_p2s_vid-isl
<a id="on_49_68___len_6_aug_lf_n_"></a>
### on-49_68       @ len-6-aug/lfn-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:det-1:vnms-1:nms-1:show-0:proc-1:_in_-resnet_640_detrac-length-6-stride-1-non_empty-seq-0_19-batch_6-lfn-jtr/ckpt-70932-detrac-length-6-stride-1-non_empty-seq-49_68/csv-batch_12:_out_-p2s-lfn-detrac-0_19-len-6-aug-49_68

<a id="len_9___lf_n_"></a>
## len-9       @ lfn-->eval_p2s_vid-isl
<a id="on_49_68___len_9_lf_n_"></a>
### on-49_68       @ len-9/lfn-->eval_p2s_vid-isl
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:det-0:vnms-1:nms-0:show-0:proc-1:_in_-resnet_640_detrac-length-9-stride-1-non_empty-seq-0_19-batch_2-lfn/ckpt-304392-detrac-length-9-stride-1-non_empty-seq-49_68/csv-batch_10:_out_-p2s-lfn-detrac-0_19-len-9-49_68




