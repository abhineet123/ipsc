<!-- MarkdownTOC -->

- [resnet-640       @ p2s](#resnet_640___p2_s_)
    - [detrac-non_empty-0_19       @ resnet-640](#detrac_non_empty_0_19___resnet_640_)
        - [0_19       @ detrac-non_empty-0_19/resnet-640](#0_19___detrac_non_empty_0_19_resnet_640_)
        - [49_68       @ detrac-non_empty-0_19/resnet-640](#49_68___detrac_non_empty_0_19_resnet_640_)
    - [detrac-non_empty-0_48-fbb       @ resnet-640](#detrac_non_empty_0_48_fbb___resnet_640_)
        - [49_85-100_per_seq_random       @ detrac-non_empty-0_48-fbb/resnet-640](#49_85_100_per_seq_random___detrac_non_empty_0_48_fbb_resnet_640_)
        - [49_85       @ detrac-non_empty-0_48-fbb/resnet-640](#49_85___detrac_non_empty_0_48_fbb_resnet_640_)
            - [ign       @ 49_85/detrac-non_empty-0_48-fbb/resnet-640](#ign___49_85_detrac_non_empty_0_48_fbb_resnet_640_)
        - [49_85       @ detrac-non_empty-0_48-fbb/resnet-640](#49_85___detrac_non_empty_0_48_fbb_resnet_640__1)
    - [detrac-0_59-fbb       @ resnet-640](#detrac_0_59_fbb___resnet_640_)
        - [0_59-100_per_seq_random       @ detrac-0_59-fbb/resnet-640](#0_59_100_per_seq_random___detrac_0_59_fbb_resnet_640_)
        - [60_99-100_per_seq_random       @ detrac-0_59-fbb/resnet-640](#60_99_100_per_seq_random___detrac_0_59_fbb_resnet_640_)

<!-- /MarkdownTOC -->
<a id="resnet_640___p2_s_"></a>
# resnet-640       @ p2s-->eval_det_p2s
<a id="detrac_non_empty_0_19___resnet_640_"></a>
## detrac-non_empty-0_19       @ resnet-640-->eval_p2s-isl
<a id="0_19___detrac_non_empty_0_19_resnet_640_"></a>
### 0_19       @ detrac-non_empty-0_19/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:non_empty-0_19:nms:gt-1:show-0:proc-12:_in_-resnet_640_detrac-non_empty-seq-0_19-batch_18/ckpt-242990-detrac-non_empty-seq-0_19/csv-batch_48:_out_-p2s-resnet_640-detrac-0_19-0_19-242990
<a id="49_68___detrac_non_empty_0_19_resnet_640_"></a>
### 49_68       @ detrac-non_empty-0_19/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:non_empty:49_68:nms:gt-1:show-0:_in_-resnet_640_detrac-non_empty-seq-0_19-batch_18/ckpt-242990-detrac-non_empty-seq-49_68/csv-batch_48:_out_-p2s-resnet_640-detrac-0_19-49_68-242990

<a id="detrac_non_empty_0_48_fbb___resnet_640_"></a>
## detrac-non_empty-0_48-fbb       @ resnet-640-->eval_p2s-isl
<a id="49_85_100_per_seq_random___detrac_non_empty_0_48_fbb_resnet_640_"></a>
### 49_85-100_per_seq_random       @ detrac-non_empty-0_48-fbb/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:non_empty:49_85:100_per_seq_random:nms-1:gt-0:proc-1:_in_-resnet_640_detrac-non_empty-seq-0_48-batch_60-fbb/ckpt-__var__-detrac-non_empty-100_per_seq_random-seq-49_85/csv-batch_8:_out_-p2s-detrac-0_48-100_per_seq_random-49_85-fbb:ief
`dbg`
python3 eval_det.py cfg=p2s,detrac:non_empty:100_per_seq_random:49_85:nms:gt-0:proc-1:_in_-resnet_640_detrac-non_empty-seq-0_48-batch_60-fbb/ckpt-__var__-detrac-non_empty-100_per_seq_random-seq-49_85/csv-batch_8:_out_-p2s-detrac-0_48-49_85-100_per_seq_random-fbb:dbg:vis:vbs
<a id="49_85___detrac_non_empty_0_48_fbb_resnet_640_"></a>
### 49_85       @ detrac-non_empty-0_48-fbb/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:non_empty:49_85:nms-1:gt-1:proc-1:_in_-resnet_640_detrac-non_empty-seq-0_48-batch_60-fbb/ckpt-__var__-detrac-non_empty-seq-49_85/csv-batch_2:_out_-p2s-detrac-0_48-49_85-fbb
<a id="ign___49_85_detrac_non_empty_0_48_fbb_resnet_640_"></a>
#### ign       @ 49_85/detrac-non_empty-0_48-fbb/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:non_empty:49_85:nms-1:gt-1:ign:proc-1:_in_-resnet_640_detrac-non_empty-seq-0_48-batch_60-fbb/ckpt-__var__-detrac-non_empty-seq-49_85/csv-batch_2:_out_-p2s-detrac-0_48-49_85-fbb-ign
<a id="49_85___detrac_non_empty_0_48_fbb_resnet_640__1"></a>
### 49_85       @ detrac-non_empty-0_48-fbb/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:non_empty:49_85:nms:gt-1:proc-1:_in_-resnet_640_detrac-non_empty-seq-0_48-batch_60-fbb/ckpt-__var__-detrac-non_empty-seq-49_85/csv-batch_8:_out_-p2s-detrac-0_48-49_85-fbb


<a id="detrac_0_59_fbb___resnet_640_"></a>
## detrac-0_59-fbb       @ resnet-640-->eval_p2s-isl
<a id="0_59_100_per_seq_random___detrac_0_59_fbb_resnet_640_"></a>
### 0_59-100_per_seq_random       @ detrac-0_59-fbb/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:0_59:100_per_seq_random:nms-1:gt-0:ign:proc-1:_in_-resnet_640_detrac-seq-0_59-batch_288-jtr-res_1280-fbb-exg/ckpt-__var__-detrac-100_per_seq_random-seq-0_59/csv-batch_4:_out_-p2s-detrac-0_59-100_per_seq-0_59-aug-fbb
<a id="60_99_100_per_seq_random___detrac_0_59_fbb_resnet_640_"></a>
### 60_99-100_per_seq_random       @ detrac-0_59-fbb/resnet-640-->eval_p2s-isl
python3 eval_det.py cfg=p2s,detrac:60_99:100_per_seq_random:nms-1:gt-0:ign:proc-1:_in_-resnet_640_detrac-seq-0_59-batch_288-jtr-res_1280-fbb-exg/ckpt-__var__-detrac-100_per_seq_random-seq-60_99/csv-batch_4:_out_-p2s-detrac-0_59-100_per_seq-60_99-aug-fbb


