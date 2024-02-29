<!-- MarkdownTOC -->

- [resnet-640-vid       @ p2s](#resnet_640_vid___p2_s_)
    - [detrac-0_9       @ resnet-640-vid](#detrac_0_9___resnet_640_vid_)
        - [test       @ detrac-0_9/resnet-640-vid](#test___detrac_0_9_resnet_640_vi_d_)
    - [mnist-640-1       @ resnet-640-vid](#mnist_640_1___resnet_640_vid_)
        - [test       @ mnist-640-1/resnet-640-vid](#test___mnist_640_1_resnet_640_vid_)
        - [test-strd-2       @ mnist-640-1/resnet-640-vid](#test_strd_2___mnist_640_1_resnet_640_vid_)
    - [mnist-640-5       @ resnet-640-vid](#mnist_640_5___resnet_640_vid_)
        - [test       @ mnist-640-5/resnet-640-vid](#test___mnist_640_5_resnet_640_vid_)
        - [test-strd-2       @ mnist-640-5/resnet-640-vid](#test_strd_2___mnist_640_5_resnet_640_vid_)
    - [g2_5_9       @ resnet-640-vid](#g2_5_9___resnet_640_vid_)
        - [on-g2_5_9       @ g2_5_9/resnet-640-vid](#on_g2_5_9___g2_5_9_resnet_640_vi_d_)
        - [on-g2_0_4       @ g2_5_9/resnet-640-vid](#on_g2_0_4___g2_5_9_resnet_640_vi_d_)
- [resnet-640       @ p2s](#resnet_640___p2_s_)
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

<a id="resnet_640_vid___p2_s_"></a>
# resnet-640-vid       @ p2s-->eval_det_p2s
<a id="mnist_640_1___resnet_640_vid_"></a>


<a id="detrac_0_9___resnet_640_vid_"></a>
## detrac-0_9       @ resnet-640-vid-->eval_det_p2s
<a id="test___detrac_0_9_resnet_640_vi_d_"></a>
### test       @ detrac-0_9/resnet-640-vid-->eval_det_p2s
python3 eval_det.py cfg=detrac:640-1:12_1000:test,p2s det_paths=video/resnet_640_mnist_640_1_12_1000_var-length-2-stride-1-train-batch_18/ckpt-186480-mnist_640_1_12_1000_var-length-2-stride-1-test/csv-batch_32 save_suffix=p2s-resnet_640-g2_mnist:640-1-12-len-2-strd-1-test-strd-1-186480 show_vis=0 load_gt=0
<a id="mnist_640_1___resnet_640_vid_"></a>
## mnist-640-1       @ resnet-640-vid-->eval_det_p2s
<a id="test___mnist_640_1_resnet_640_vid_"></a>
### test       @ mnist-640-1/resnet-640-vid-->eval_det_p2s
python3 eval_det.py cfg=mnist:640-1:12_1000:test,p2s det_paths=video/resnet_640_mnist_640_1_12_1000_var-length-2-stride-1-train-batch_18/ckpt-186480-mnist_640_1_12_1000_var-length-2-stride-1-test/csv-batch_32 save_suffix=p2s-resnet_640-g2_mnist:640-1-12-len-2-strd-1-test-strd-1-186480 show_vis=0 load_gt=0
<a id="test_strd_2___mnist_640_1_resnet_640_vid_"></a>
### test-strd-2       @ mnist-640-1/resnet-640-vid-->eval_det_p2s
python3 eval_det.py cfg=mnist:640-1:12_1000:test,p2s det_paths=video/resnet_640_mnist_640_1_12_1000_var-length-2-stride-1-train-batch_18/ckpt-186480-mnist_640_1_12_1000_var-length-2-stride-2-test/csv-batch_48 save_suffix=p2s-resnet_640-g2_mnist:640-1-12-len-2-strd-1-test-strd-2-186480 show_vis=0 load_gt=0
<a id="mnist_640_5___resnet_640_vid_"></a>
## mnist-640-5       @ resnet-640-vid-->eval_det_p2s
<a id="test___mnist_640_5_resnet_640_vid_"></a>
### test       @ mnist-640-5/resnet-640-vid-->eval_det_p2s
python3 eval_det.py cfg=mnist:640-5:12_1000:test,p2s det_paths=video/resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-1-test/csv-batch_36 save_suffix=p2s-resnet_640-g2_mnist:640-5-12-len-2-strd-1-test-strd-1-581418 show_vis=0 load_gt=0
<a id="test_strd_2___mnist_640_5_resnet_640_vid_"></a>
### test-strd-2       @ mnist-640-5/resnet-640-vid-->eval_det_p2s
python3 eval_det.py cfg=mnist:640-5:12_1000:test,p2s det_paths=video/resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-2-test/csv-batch_48 save_suffix=p2s-resnet_640-g2_mnist:640-1-12-len-2-strd-1-test-strd-2-581418 show_vis=0 load_gt=0
<a id="g2_5_9___resnet_640_vid_"></a>
## g2_5_9       @ resnet-640-vid-->eval_det_p2s
<a id="on_g2_5_9___g2_5_9_resnet_640_vi_d_"></a>
### on-g2_5_9       @ g2_5_9/resnet-640-vid-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_5_9,p2s det_paths=resnet_640_ext_reorg_roi_g2_5_9-length-2-stride-1-batch_8/ckpt-1226544-ext_reorg_roi_g2_5_9-length-2-stride-1/csv-batch_4 save_suffix=p2s-resnet_640-g2_5_9-len-2-strd-1-g2_0_4-batch_8-1226544 show_vis=0 load_gt=0
<a id="on_g2_0_4___g2_5_9_resnet_640_vi_d_"></a>
### on-g2_0_4       @ g2_5_9/resnet-640-vid-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_4,p2s det_paths=resnet_640_ext_reorg_roi_g2_5_9-length-2-stride-1-batch_8/ckpt-1052144-ext_reorg_roi_g2_0_4-length-2-stride-1/csv-batch_4 save_suffix=p2s-resnet_640-g2_5_9-len-2-strd-1-g2_0_4-batch_8-1052144 show_vis=0 load_gt=0
<a id="resnet_640___p2_s_"></a>
# resnet-640       @ p2s-->eval_det_p2s
<a id="pt___resnet_640_"></a>
## pt       @ resnet-640-->eval_det_p2s
<a id="on_g2_0_1___pt_resnet_64_0_"></a>
### on-g2_0_1       @ pt/resnet-640-->eval_det_p2s
<a id="resnet_640___ext_reorg_roi_g2_0_1_p2s_"></a>
<a id="batch_2___resnet_640_ext_reorg_roi_g2_0_1_p2_s_"></a>
``batch-2 ``  
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_1,p2s:640 det_paths=ckpt-74844-ext_reorg_roi_g2_0_1/csv-batch-2 save_suffix=p2s-resnet_640-0_1-batch-2 show_vis=1
``batch-48``  
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_1,p2s:640 det_paths=ckpt-74844-ext_reorg_roi_g2_0_1/csv-batch-48 save_suffix=p2s-resnet_640-0_1-batch_48 show_vis=1
<a id="on_g2_16_53___pt_resnet_64_0_"></a>
### on-g2_16_53       @ pt/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_16_53,p2s:640 det_paths=ckpt-74844-ext_reorg_roi_g2_16_53/csv-batch_64 save_suffix=p2s-resnet_640-g2_16_53-batch_64
<a id="on_g2_0_15___pt_resnet_64_0_"></a>
### on-g2_0_15       @ pt/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_15,p2s:640 det_paths=ckpt-74844-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_0_15
<a id="on_g2_54_126___pt_resnet_64_0_"></a>
### on-g2_54_126       @ pt/resnet-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_54_126,p2s:640 det_paths=ckpt-74844-ext_reorg_roi_g2_54_126/csv-batch_32 save_suffix=p2s-resnet_640-g2_54_126-batch_32

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
python3 eval_det.py cfg=ipsc_2_class:ext:g2_16_53,p2s:1333 det_paths=ckpt-93324-ext_reorg_roi_g2_16_53/csv-batch_24 save_suffix=p2s-resnet_1333-g2_16_53-batch_24

<a id="resnet_c4_640___p2_s_"></a>
# resnet-c4-640       @ p2s-->eval_det_p2s
<a id="g2_16_53___resnet_c4_64_0_"></a>
## g2_16_53       @ resnet-c4-640-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_16_53,p2s:c4-640 det_paths=pretrained/resnet_c4_640/ckpt-56364-ext_reorg_roi_g2_16_53/csv-batch_16 save_suffix=p2s-resnet_c4_640-g2_16_53-batch_16 class_agnostic=1 enable_mask=0

<a id="resnet_c4_1333___p2_s_"></a>
# resnet-c4-1333       @ p2s-->eval_det_p2s
<a id="g2_0_1___resnet_c4_1333_"></a>
## g2_0_1       @ resnet-c4-1333-->eval_det_p2s
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_1,p2s,p2s:c4-1333 det_paths=pretrained/resnet_c4_1333/ckpt-112728-ext_reorg_roi_g2_0_1/csv-batch_1 save_suffix=p2s-resnet_c4_1333-g2_0_1-batch_1 class_agnostic=1 enable_mask=0 show_vis=0

