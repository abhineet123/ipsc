<!-- MarkdownTOC -->

- [resnet-640](#resnet_64_0_)
    - [detrac-0_9       @ resnet-640](#detrac_0_9___resnet_640_)
        - [0_9       @ detrac-0_9/resnet-640](#0_9___detrac_0_9_resnet_64_0_)
            - [strd-2       @ 0_9/detrac-0_9/resnet-640](#strd_2___0_9_detrac_0_9_resnet_64_0_)
        - [49_68       @ detrac-0_9/resnet-640](#49_68___detrac_0_9_resnet_64_0_)
            - [strd-2       @ 49_68/detrac-0_9/resnet-640](#strd_2___49_68_detrac_0_9_resnet_64_0_)
    - [detrac-0_19       @ resnet-640](#detrac_0_19___resnet_640_)
        - [0_19       @ detrac-0_19/resnet-640](#0_19___detrac_0_19_resnet_640_)
            - [strd-1       @ 0_19/detrac-0_19/resnet-640](#strd_1___0_19_detrac_0_19_resnet_64_0_)
            - [strd-2       @ 0_19/detrac-0_19/resnet-640](#strd_2___0_19_detrac_0_19_resnet_64_0_)
        - [49_68       @ detrac-0_19/resnet-640](#49_68___detrac_0_19_resnet_640_)
            - [strd-1       @ 49_68/detrac-0_19/resnet-640](#strd_1___49_68_detrac_0_19_resnet_640_)
            - [strd-2       @ 49_68/detrac-0_19/resnet-640](#strd_2___49_68_detrac_0_19_resnet_640_)
    - [mnist-640-1       @ resnet-640](#mnist_640_1___resnet_640_)
        - [test       @ mnist-640-1/resnet-640](#test___mnist_640_1_resnet_640_)
        - [test-strd-2       @ mnist-640-1/resnet-640](#test_strd_2___mnist_640_1_resnet_640_)
    - [mnist-640-5       @ resnet-640](#mnist_640_5___resnet_640_)
        - [test-strd-1       @ mnist-640-5/resnet-640](#test_strd_1___mnist_640_5_resnet_640_)
            - [agn       @ test-strd-1/mnist-640-5/resnet-640](#agn___test_strd_1_mnist_640_5_resnet_640_)
        - [test-strd-2       @ mnist-640-5/resnet-640](#test_strd_2___mnist_640_5_resnet_640_)
            - [agn       @ test-strd-2/mnist-640-5/resnet-640](#agn___test_strd_2_mnist_640_5_resnet_640_)
    - [g2_5_9       @ resnet-640](#g2_5_9___resnet_640_)
        - [on-g2_5_9       @ g2_5_9/resnet-640](#on_g2_5_9___g2_5_9_resnet_64_0_)
        - [on-g2_0_4       @ g2_5_9/resnet-640](#on_g2_0_4___g2_5_9_resnet_64_0_)

<!-- /MarkdownTOC -->

<a id="resnet_64_0_"></a>
# resnet-640
<a id="detrac_0_9___resnet_640_"></a>
## detrac-0_9       @ resnet-640-->eval_det_p2s_vid
<a id="49_68___detrac_0_9_resnet_640_vi_d_"></a>
<a id="0_9___detrac_0_9_resnet_64_0_"></a>
### 0_9       @ detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty-0_9:nms-1:gt-1:proc-12:show-0 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-0_9/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-0_9-strd-1-120132
<a id="strd_2___0_9_detrac_0_9_resnet_64_0_"></a>
#### strd-2       @ 0_9/detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:0_9:nms-1:gt-1:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-2-non_empty-seq-0_9/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-0_9-strd-2-120132
<a id="49_68___detrac_0_9_resnet_64_0_"></a>
### 49_68       @ detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:nms-10:gt-1:nms-1:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-49_68-strd-1-120132
<a id="strd_2___49_68_detrac_0_9_resnet_64_0_"></a>
#### strd-2       @ 49_68/detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:nms-10:gt-1:nms-1:show-0:proc-12  det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-2-non_empty-seq-49_68/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-49_68-strd-2-120132

<a id="detrac_0_19___resnet_640_"></a>
## detrac-0_19       @ resnet-640-->eval_det_p2s_vid
<a id="49_68___detrac_0_9_resnet_640_vi_d_"></a>
<a id="0_19___detrac_0_19_resnet_640_"></a>
### 0_19       @ detrac-0_19/resnet-640-->eval_det_p2s_vid
<a id="strd_1___0_19_detrac_0_19_resnet_64_0_"></a>
#### strd-1       @ 0_19/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty-0_19:gt-1:nms-1:proc-12:show-0 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-0_19/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-1-334692
<a id="strd_2___0_19_detrac_0_19_resnet_64_0_"></a>
#### strd-2       @ 0_19/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:0_19:gt-1:nms-1:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-0_19/csv-batch_12 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-2-301636
<a id="49_68___detrac_0_19_resnet_640_"></a>
### 49_68       @ detrac-0_19/resnet-640-->eval_det_p2s_vid
<a id="strd_1___49_68_detrac_0_19_resnet_640_"></a>
#### strd-1       @ 49_68/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms-1:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-1-334692
<a id="strd_2___49_68_detrac_0_19_resnet_640_"></a>
#### strd-2       @ 49_68/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms-1:show-0:proc-12  det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-49_68/csv-batch_12 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-2-301636

<a id="mnist_640_1___resnet_640_"></a>
## mnist-640-1       @ resnet-640-->eval_det_p2s_vid
<a id="test___mnist_640_1_resnet_640_"></a>
### test       @ mnist-640-1/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=mnist:640-1:12_1000:test,p2s:vid det_paths=resnet_640_mnist_640_1_12_1000_var-length-2-stride-1-train-batch_18/ckpt-186480-mnist_640_1_12_1000_var-length-2-stride-1-test/csv-batch_32 save_suffix=p2s-resnet_640-mnist-640-1-12-len-2-strd-1-test-strd-1-186480 show_vis=0 load_gt=0
<a id="test_strd_2___mnist_640_1_resnet_640_"></a>
### test-strd-2       @ mnist-640-1/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=mnist:640-1:12_1000:test,p2s:vid det_paths=resnet_640_mnist_640_1_12_1000_var-length-2-stride-1-train-batch_18/ckpt-186480-mnist_640_1_12_1000_var-length-2-stride-2-test/csv-batch_48 save_suffix=p2s-resnet_640-mnist-640-1-12-len-2-strd-1-test-strd-2-186480 show_vis=0 load_gt=0
<a id="mnist_640_5___resnet_640_"></a>
## mnist-640-5       @ resnet-640-->eval_det_p2s_vid
<a id="test_strd_1___mnist_640_5_resnet_640_"></a>
### test-strd-1       @ mnist-640-5/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=mnist:640-5:12_1000:test:gt-1:nms-1,p2s:vid det_paths=resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-1-test/csv-batch_36 save_suffix=p2s-resnet_640-mnist-640-5-12-len-2-strd-1-test-strd-1-581418
<a id="agn___test_strd_1_mnist_640_5_resnet_640_"></a>
#### agn       @ test-strd-1/mnist-640-5/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=mnist:640-5:12_1000:test:gt-0:det-0:nms-1:agn,p2s:vid det_paths=resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-1-test/csv-batch_36 save_suffix=p2s-resnet_640-mnist-640-5-12-len-2-strd-1-test-strd-1-581418-agn
<a id="test_strd_2___mnist_640_5_resnet_640_"></a>
### test-strd-2       @ mnist-640-5/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=mnist:640-5:12_1000:test:gt-1:nms-1,p2s:vid det_paths=resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-2-test/csv-batch_48 save_suffix=p2s-resnet_640-mnist-640-5-12-len-2-strd-1-test-strd-2-581418
<a id="agn___test_strd_2_mnist_640_5_resnet_640_"></a>
#### agn       @ test-strd-2/mnist-640-5/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=mnist:640-5:12_1000:test:det-0:gt-0:nms-1:agn,p2s:vid det_paths=resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-2-test/csv-batch_48 save_suffix=p2s-resnet_640-mnist-640-5-12-len-2-strd-1-test-strd-2-581418-agn

<a id="g2_5_9___resnet_640_"></a>
## g2_5_9       @ resnet-640-->eval_det_p2s_vid
<a id="on_g2_5_9___g2_5_9_resnet_64_0_"></a>
### on-g2_5_9       @ g2_5_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc_2_class:ext:g2_5_9,p2s det_paths=resnet_640_ext_reorg_roi_g2_5_9-length-2-stride-1-batch_8/ckpt-1226544-ext_reorg_roi_g2_5_9-length-2-stride-1/csv-batch_4 save_suffix=p2s-resnet_640-g2_5_9-len-2-strd-1-g2_0_4-batch_8-1226544 show_vis=0 load_gt=0
<a id="on_g2_0_4___g2_5_9_resnet_64_0_"></a>
### on-g2_0_4       @ g2_5_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc_2_class:ext:g2_0_4,p2s det_paths=resnet_640_ext_reorg_roi_g2_5_9-length-2-stride-1-batch_8/ckpt-1052144-ext_reorg_roi_g2_0_4-length-2-stride-1/csv-batch_4 save_suffix=p2s-resnet_640-g2_5_9-len-2-strd-1-g2_0_4-batch_8-1052144 show_vis=0 load_gt=0

