<!-- MarkdownTOC -->

- [resnet-640       @ p2s](#resnet_640___p2_s_)
    - [detrac-0_9       @ resnet-640](#detrac_0_9___resnet_640_)
        - [0_9       @ detrac-0_9/resnet-640](#0_9___detrac_0_9_resnet_64_0_)
            - [strd-2       @ 0_9/detrac-0_9/resnet-640](#strd_2___0_9_detrac_0_9_resnet_64_0_)
        - [49_68       @ detrac-0_9/resnet-640](#49_68___detrac_0_9_resnet_64_0_)
    - [pt       @ resnet-640](#pt___resnet_640_)
        - [on-g2_0_1       @ pt/resnet-640](#on_g2_0_1___pt_resnet_64_0_)
        - [on-g2_16_53       @ pt/resnet-640](#on_g2_16_53___pt_resnet_64_0_)
        - [on-g2_0_15       @ pt/resnet-640](#on_g2_0_15___pt_resnet_64_0_)
        - [on-g2_54_126       @ pt/resnet-640](#on_g2_54_126___pt_resnet_64_0_)
    - [g2_16_53       @ resnet-640](#g2_16_53___resnet_640_)
        - [batch_48       @ g2_16_53/resnet-640](#batch_48___g2_16_53_resnet_64_0_)
            - [ckpt-1975       @ batch_48/g2_16_53/resnet-640](#ckpt_1975___batch_48_g2_16_53_resnet_640_)
                - [on-g2_0_15       @ ckpt-1975/batch_48/g2_16_53/resnet-640](#on_g2_0_15___ckpt_1975_batch_48_g2_16_53_resnet_640_)
                - [on-g2_54_126       @ ckpt-1975/batch_48/g2_16_53/resnet-640](#on_g2_54_126___ckpt_1975_batch_48_g2_16_53_resnet_640_)
            - [ckpt-12275       @ batch_48/g2_16_53/resnet-640](#ckpt_12275___batch_48_g2_16_53_resnet_640_)
                - [on-g2_0_15       @ ckpt-12275/batch_48/g2_16_53/resnet-640](#on_g2_0_15___ckpt_12275_batch_48_g2_16_53_resnet_64_0_)
        - [batch_32       @ g2_16_53/resnet-640](#batch_32___g2_16_53_resnet_64_0_)
            - [on-g2_0_15       @ batch_32/g2_16_53/resnet-640](#on_g2_0_15___batch_32_g2_16_53_resnet_640_)
        - [batch_6       @ g2_16_53/resnet-640](#batch_6___g2_16_53_resnet_64_0_)
            - [on-g2_0_15       @ batch_6/g2_16_53/resnet-640](#on_g2_0_15___batch_6_g2_16_53_resnet_64_0_)
            - [on-g2_54_126       @ batch_6/g2_16_53/resnet-640](#on_g2_54_126___batch_6_g2_16_53_resnet_64_0_)
        - [batch_4-scratch       @ g2_16_53/resnet-640](#batch_4_scratch___g2_16_53_resnet_64_0_)
            - [on-g2_0_15       @ batch_4-scratch/g2_16_53/resnet-640](#on_g2_0_15___batch_4_scratch_g2_16_53_resnet_64_0_)
            - [on-g2_54_126       @ batch_4-scratch/g2_16_53/resnet-640](#on_g2_54_126___batch_4_scratch_g2_16_53_resnet_64_0_)
    - [g2_0_37       @ resnet-640](#g2_0_37___resnet_640_)
        - [on-g2_38_53       @ g2_0_37/resnet-640](#on_g2_38_53___g2_0_37_resnet_640_)
        - [on-g2_38_53-conf_0       @ g2_0_37/resnet-640](#on_g2_38_53_conf_0___g2_0_37_resnet_640_)
- [resnet_1333       @ p2s](#resnet_1333___p2_s_)
    - [g2_16_53       @ resnet_1333](#g2_16_53___resnet_133_3_)
- [resnet-c4-640       @ p2s](#resnet_c4_640___p2_s_)
    - [g2_16_53       @ resnet-c4-640](#g2_16_53___resnet_c4_64_0_)
- [resnet-c4-1333       @ p2s](#resnet_c4_1333___p2_s_)
    - [g2_0_1       @ resnet-c4-1333](#g2_0_1___resnet_c4_1333_)

<!-- /MarkdownTOC -->
<a id="resnet_640___p2_s_"></a>
# resnet-640       @ p2s-->eval_det_p2s
<a id="detrac_0_9___resnet_640_"></a>
## detrac-0_9       @ resnet-640-->eval_det_p2s
<a id="49_68___detrac_0_9_resnet_640_vi_d_"></a>
<a id="0_9___detrac_0_9_resnet_64_0_"></a>
### 0_9       @ detrac-0_9/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=p2s,detrac:non_empty-0_9:nms-1:gt-1:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-0_9/csv-batch_48 save_suffix=p2s-resnet_640-detrac:0_9-len-2-strd-1-0_9-strd-1-120132
<a id="strd_2___0_9_detrac_0_9_resnet_64_0_"></a>
#### strd-2       @ 0_9/detrac-0_9/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=p2s,detrac:non_empty:0_9:nms-1:gt-1:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-2-non_empty-seq-0_9/csv-batch_48 save_suffix=p2s-resnet_640-detrac:0_9-len-2-strd-2-0_9-strd-2-120132

<a id="49_68___detrac_0_9_resnet_64_0_"></a>
### 49_68       @ detrac-0_9/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=p2s,detrac:non_empty:49_68:nms-10:gt-0:show-0 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48 save_suffix=p2s-resnet_640-detrac:0_9-len-2-strd-1-49_68-strd-1-120132
<a id="pt___resnet_640_"></a>
## pt       @ resnet-640-->eval_det_p2s
<a id="on_g2_0_1___pt_resnet_64_0_"></a>
### on-g2_0_1       @ pt/resnet-640-->eval_det_p2s
<a id="resnet_640___ext_reorg_roi_g2_0_1_p2s_"></a>
<a id="batch_2___resnet_640_ext_reorg_roi_g2_0_1_p2_s_"></a>
``batch-2 ``  
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_1,p2s:pt-640 det_paths=ckpt-74844-ext_reorg_roi_g2_0_1/csv-batch-2 save_suffix=p2s-resnet_640-0_1-batch-2 show_vis=1
``batch-48``  
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_1,p2s:pt-640 det_paths=ckpt-74844-ext_reorg_roi_g2_0_1/csv-batch-48 save_suffix=p2s-resnet_640-0_1-batch_48 show_vis=1
<a id="on_g2_16_53___pt_resnet_64_0_"></a>
### on-g2_16_53       @ pt/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_16_53,p2s:pt-640 det_paths=ckpt-74844-ext_reorg_roi_g2_16_53/csv-batch_64 save_suffix=p2s-resnet_640-g2_16_53-batch_64
<a id="on_g2_0_15___pt_resnet_64_0_"></a>
### on-g2_0_15       @ pt/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15,p2s:pt-640 det_paths=ckpt-74844-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_0_15
<a id="on_g2_54_126___pt_resnet_64_0_"></a>
### on-g2_54_126       @ pt/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126,p2s:pt-640 det_paths=ckpt-74844-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_54_126-batch_32

<a id="g2_16_53___resnet_640_"></a>
## g2_16_53       @ resnet-640-->eval_det_p2s
<a id="batch_48___g2_16_53_resnet_64_0_"></a>
### batch_48       @ g2_16_53/resnet-640-->eval_det_p2s
<a id="ckpt_1975___batch_48_g2_16_53_resnet_640_"></a>
#### ckpt-1975       @ batch_48/g2_16_53/resnet-640-->eval_det_p2s
<a id="on_g2_0_15___ckpt_1975_batch_48_g2_16_53_resnet_640_"></a>
##### on-g2_0_15       @ ckpt-1975/batch_48/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-1975-ext_reorg_roi_g2_0_15/csv-batch_16 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_48-1975 show_vis=0 load_gt=0
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-1975-ext_reorg_roi_g2_0_15/csv-batch_16 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_48-1975-cls show_vis=0 load_gt=0
<a id="on_g2_54_126___ckpt_1975_batch_48_g2_16_53_resnet_640_"></a>
##### on-g2_54_126       @ ckpt-1975/batch_48/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-1975-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_54_126-batch_48 show_vis=0
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-1975-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_54_126-batch_48-cls show_vis=0 load_gt=0

<a id="ckpt_12275___batch_48_g2_16_53_resnet_640_"></a>
#### ckpt-12275       @ batch_48/g2_16_53/resnet-640-->eval_det_p2s
<a id="on_g2_0_15___ckpt_12275_batch_48_g2_16_53_resnet_64_0_"></a>
##### on-g2_0_15       @ ckpt-12275/batch_48/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15-agn,p2s:fill det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-12275-ext_reorg_roi_g2_0_15/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_48-12275 show_vis=0 load_gt=0
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15,p2s:cls:fill det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-12275-ext_reorg_roi_g2_0_15/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_48-12275-cls show_vis=0 load_gt=0

<a id="batch_32___g2_16_53_resnet_64_0_"></a>
### batch_32       @ g2_16_53/resnet-640-->eval_det_p2s
<a id="on_g2_0_15___batch_32_g2_16_53_resnet_640_"></a>
#### on-g2_0_15       @ batch_32/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15-agn,p2s:fill det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_32-xe/ckpt-2960-ext_reorg_roi_g2_0_15/csv-batch_64 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_32 show_vis=0 load_gt=0
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15,p2s:cls:fill det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_32-xe/ckpt-2960-ext_reorg_roi_g2_0_15/csv-batch_64 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_32-cls show_vis=0 load_gt=0

<a id="batch_6___g2_16_53_resnet_64_0_"></a>
### batch_6       @ g2_16_53/resnet-640-->eval_det_p2s
<a id="on_g2_0_15___batch_6_g2_16_53_resnet_64_0_"></a>
#### on-g2_0_15       @ batch_6/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_6/ckpt-15876-ext_reorg_roi_g2_0_15/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_6 show_vis=0 load_gt=0
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_6/ckpt-15876-ext_reorg_roi_g2_0_15/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_6-cls show_vis=0 load_gt=0
<a id="on_g2_54_126___batch_6_g2_16_53_resnet_64_0_"></a>
#### on-g2_54_126       @ batch_6/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-15876-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_54_126-batch_6 show_vis=0 load_gt=1
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-15876-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_54_126-batch_6-cls show_vis=0 load_gt=1
<a id="batch_4_scratch___g2_16_53_resnet_64_0_"></a>
### batch_4-scratch       @ g2_16_53/resnet-640-->eval_det_p2s
<a id="on_g2_0_15___batch_4_scratch_g2_16_53_resnet_64_0_"></a>
#### on-g2_0_15       @ batch_4-scratch/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_4-scratch/ckpt-4116-ext_reorg_roi_g2_0_15/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_4-scratch show_vis=0 load_gt=1
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_4-scratch/ckpt-4116-ext_reorg_roi_g2_0_15/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_0_15-batch_4-scratch-cls show_vis=0 load_gt=0
<a id="on_g2_54_126___batch_4_scratch_g2_16_53_resnet_64_0_"></a>
#### on-g2_54_126       @ batch_4-scratch/g2_16_53/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-4116-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_54_126-batch_4-scratch show_vis=0 load_gt=1
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_16_53-batch_48-gxe/ckpt-4116-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_16_53-g2_54_126-batch_4-scratch-cls show_vis=0 load_gt=1

<a id="g2_0_37___resnet_640_"></a>
## g2_0_37       @ resnet-640-->eval_det_p2s
<a id="on_g2_38_53___g2_0_37_resnet_640_"></a>
### on-g2_38_53       @ g2_0_37/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_38_53-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_0_37-batch_48-gxe/ckpt-98175-ext_reorg_roi_g2_38_53/csv-batch_16 save_suffix=p2s-resnet_640-g2_0_37-g2_38_53-batch_48-98175 show_vis=0 load_gt=0
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_38_53-agn,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_0_37-batch_48-gxe/ckpt-98175-ext_reorg_roi_g2_38_53/csv-batch_16 save_suffix=p2s-resnet_640-g2_0_37-g2_38_53-batch_48-98175-cls show_vis=0 load_gt=0
<a id="on_g2_38_53_conf_0___g2_0_37_resnet_640_"></a>
### on-g2_38_53-conf_0       @ g2_0_37/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_38_53-agn,p2s det_paths=resnet_640_ext_reorg_roi_g2_0_37-batch_48-gxe/ckpt-98175-ext_reorg_roi_g2_38_53/csv-batch_16-conf_0 save_suffix=p2s-resnet_640-g2_0_37-g2_38_53-batch_48-98175-conf_0 show_vis=0 load_gt=0
``cls``
python3 eval_det.py cfg=ipsc_2_class:ext:g2_38_53-agn,p2s:cls det_paths=resnet_640_ext_reorg_roi_g2_0_37-batch_48-gxe/ckpt-98175-ext_reorg_roi_g2_38_53/csv-batch_16-conf_0 save_suffix=p2s-resnet_640-g2_0_37-g2_38_53-batch_48-98175-conf_0-cls show_vis=0 load_gt=0

<a id="resnet_1333___p2_s_"></a>
# resnet_1333       @ p2s-->eval_det_p2s
<a id="g2_16_53___resnet_133_3_"></a>
## g2_16_53       @ resnet_1333-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_16_53,p2s:pt-1333 det_paths=ckpt-93324-ext_reorg_roi_g2_16_53/csv-batch_24 save_suffix=p2s-resnet_1333-g2_16_53-batch_24

<a id="resnet_c4_640___p2_s_"></a>
# resnet-c4-640       @ p2s-->eval_det_p2s
<a id="g2_16_53___resnet_c4_64_0_"></a>
## g2_16_53       @ resnet-c4-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_16_53,p2s:pt-c4-640 det_paths=pretrained/resnet_c4_640/ckpt-56364-ext_reorg_roi_g2_16_53/csv-batch_16 save_suffix=p2s-resnet_c4_640-g2_16_53-batch_16 class_agnostic=1 enable_mask=0

<a id="resnet_c4_1333___p2_s_"></a>
# resnet-c4-1333       @ p2s-->eval_det_p2s
<a id="g2_0_1___resnet_c4_1333_"></a>
## g2_0_1       @ resnet-c4-1333-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_1,p2s,p2s:pt-c4-1333 det_paths=pretrained/resnet_c4_1333/ckpt-112728-ext_reorg_roi_g2_0_1/csv-batch_1 save_suffix=p2s-resnet_c4_1333-g2_0_1-batch_1 class_agnostic=1 enable_mask=0 show_vis=0

