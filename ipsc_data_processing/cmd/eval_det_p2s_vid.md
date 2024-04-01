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
        - [test-strd-2       @ mnist-640-5/resnet-640](#test_strd_2___mnist_640_5_resnet_640_)
    - [ipsc-0_37       @ resnet-640](#ipsc_0_37___resnet_640_)
        - [len-2       @ ipsc-0_37/resnet-640](#len_2___ipsc_0_37_resnet_640_)
            - [stride-1       @ len-2/ipsc-0_37/resnet-640](#stride_1___len_2_ipsc_0_37_resnet_640_)
            - [stride-2       @ len-2/ipsc-0_37/resnet-640](#stride_2___len_2_ipsc_0_37_resnet_640_)
    - [ipsc-16_53       @ resnet-640](#ipsc_16_53___resnet_640_)
        - [len-2       @ ipsc-16_53/resnet-640](#len_2___ipsc_16_53_resnet_64_0_)
            - [stride-1       @ len-2/ipsc-16_53/resnet-640](#stride_1___len_2_ipsc_16_53_resnet_64_0_)
            - [stride-2       @ len-2/ipsc-16_53/resnet-640](#stride_2___len_2_ipsc_16_53_resnet_64_0_)
        - [len-6       @ ipsc-16_53/resnet-640](#len_6___ipsc_16_53_resnet_64_0_)
            - [stride-6       @ len-6/ipsc-16_53/resnet-640](#stride_6___len_6_ipsc_16_53_resnet_64_0_)
            - [stride-1       @ len-6/ipsc-16_53/resnet-640](#stride_1___len_6_ipsc_16_53_resnet_64_0_)

<!-- /MarkdownTOC -->

<a id="resnet_64_0_"></a>
# resnet-640
<a id="detrac_0_9___resnet_640_"></a>
## detrac-0_9       @ resnet-640-->eval_det_p2s_vid
<a id="49_68___detrac_0_9_resnet_640_vi_d_"></a>
<a id="0_9___detrac_0_9_resnet_64_0_"></a>
### 0_9       @ detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty-0_9:nms:gt-1:proc-12:show-0 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-0_9/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-0_9-strd-1-120132
<a id="strd_2___0_9_detrac_0_9_resnet_64_0_"></a>
#### strd-2       @ 0_9/detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:0_9:nms:gt-1:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-2-non_empty-seq-0_9/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-0_9-strd-2-120132
<a id="49_68___detrac_0_9_resnet_64_0_"></a>
### 49_68       @ detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:nms-10:gt-1:nms:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-49_68-strd-1-120132
<a id="strd_2___49_68_detrac_0_9_resnet_64_0_"></a>
#### strd-2       @ 49_68/detrac-0_9/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:nms-10:gt-1:nms:show-0:proc-12  det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_9-batch_18/ckpt-120132-detrac-length-2-stride-2-non_empty-seq-49_68/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_9-len-2-strd-1-49_68-strd-2-120132

<a id="detrac_0_19___resnet_640_"></a>
## detrac-0_19       @ resnet-640-->eval_det_p2s_vid
<a id="49_68___detrac_0_9_resnet_640_vi_d_"></a>
<a id="0_19___detrac_0_19_resnet_640_"></a>
### 0_19       @ detrac-0_19/resnet-640-->eval_det_p2s_vid
<a id="strd_1___0_19_detrac_0_19_resnet_64_0_"></a>
#### strd-1       @ 0_19/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty-0_19:gt-1:nms:proc-12:show-0 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-0_19/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-1-334692
<a id="strd_2___0_19_detrac_0_19_resnet_64_0_"></a>
#### strd-2       @ 0_19/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:0_19:gt-1:nms:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-0_19/csv-batch_12 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-0_19-strd-2-301636
<a id="49_68___detrac_0_19_resnet_640_"></a>
### 49_68       @ detrac-0_19/resnet-640-->eval_det_p2s_vid
<a id="strd_1___49_68_detrac_0_19_resnet_640_"></a>
#### strd-1       @ 49_68/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms:show-0:proc-12 det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-334692-detrac-length-2-stride-1-non_empty-seq-49_68/csv-batch_48 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-1-334692
<a id="strd_2___49_68_detrac_0_19_resnet_640_"></a>
#### strd-2       @ 49_68/detrac-0_19/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=p2s:vid,detrac:non_empty:49_68:gt-1:nms:show-0:proc-12  det_paths=resnet_640_detrac-length-2-stride-1-non_empty-seq-0_19-batch_18/ckpt-301636-detrac-length-2-stride-2-non_empty-seq-49_68/csv-batch_12 save_suffix=p2s-resnet_640-detrac-0_19-len-2-strd-1-49_68-strd-2-301636

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
python3 eval_det.py cfg=mnist:640-5:12_1000:test:gt-0:det-0:nms:agn,p2s:vid det_paths=resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-1-test/csv-batch_36 save_suffix=p2s-resnet_640-mnist-640-5-12-len-2-strd-1-test-strd-1-581418
<a id="test_strd_2___mnist_640_5_resnet_640_"></a>
### test-strd-2       @ mnist-640-5/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=mnist:640-5:12_1000:test:gt-1:nms:agn,p2s:vid det_paths=resnet_640_mnist_640_5_12_1000_var-length-2-stride-1-train-batch_18/ckpt-581418-mnist_640_5_12_1000_var-length-2-stride-2-test/csv-batch_48 save_suffix=p2s-resnet_640-mnist-640-5-12-len-2-strd-1-test-strd-2-581418

<a id="ipsc_0_37___resnet_640_"></a>
## ipsc-0_37       @ resnet-640-->eval_det_p2s_vid
<a id="len_2___ipsc_0_37_resnet_640_"></a>
### len-2       @ ipsc-0_37/resnet-640-->eval_det_p2s_vid
<a id="stride_1___len_2_ipsc_0_37_resnet_640_"></a>
#### stride-1       @ len-2/ipsc-0_37/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc:0_37:det-0:gt-0:nms:agn,p2s:vid det_paths=resnet_640_ext_reorg_roi_g2-0_37-length-2-stride-1-batch_18/ckpt-133568-ext_reorg_roi_g2-54_126-length-2-stride-1/csv-batch_36 save_suffix=p2s-resnet_640-ipsc-0_37-len-2-strd-1-54_126-batch_18-133568
<a id="stride_2___len_2_ipsc_0_37_resnet_640_"></a>
#### stride-2       @ len-2/ipsc-0_37/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc:0_37:det-0:gt-0:nms:agn,p2s:vid det_paths=resnet_640_ext_reorg_roi_g2-0_37-length-2-stride-1-batch_18/ckpt-133568-ext_reorg_roi_g2-54_126-length-2-stride-2/csv-batch_36 save_suffix=p2s-resnet_640-ipsc-0_37-len-2-strd-2-54_126-batch_18-133568

<a id="ipsc_16_53___resnet_640_"></a>
## ipsc-16_53       @ resnet-640-->eval_det_p2s_vid
<a id="len_2___ipsc_16_53_resnet_64_0_"></a>
### len-2       @ ipsc-16_53/resnet-640-->eval_det_p2s_vid
<a id="stride_1___len_2_ipsc_16_53_resnet_64_0_"></a>
#### stride-1       @ len-2/ipsc-16_53/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc:16_53:det-0:gt-0:nms:agn,p2s:vid det_paths=resnet_640_ext_reorg_roi_g2-16_53-length-2-stride-1-batch_18/ckpt-161728-ext_reorg_roi_g2-54_126-length-2-stride-1/csv-batch_36 save_suffix=p2s-resnet_640-ipsc-16_53-len-2-strd-1-54_126-batch_18-161728
<a id="stride_2___len_2_ipsc_16_53_resnet_64_0_"></a>
#### stride-2       @ len-2/ipsc-16_53/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc:16_53:det-0:gt-0:nms:agn,p2s:vid det_paths=resnet_640_ext_reorg_roi_g2-16_53-length-2-stride-1-batch_18/ckpt-161728-ext_reorg_roi_g2-54_126-length-2-stride-1/csv-batch_36 save_suffix=p2s-resnet_640-ipsc-16_53-len-2-strd-2-54_126-batch_18-161728

<a id="len_6___ipsc_16_53_resnet_64_0_"></a>
### len-6       @ ipsc-16_53/resnet-640-->eval_det_p2s_vid
<a id="stride_6___len_6_ipsc_16_53_resnet_64_0_"></a>
#### stride-6       @ len-6/ipsc-16_53/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc:16_53:det-0:gt-0:nms:agn,p2s:vid det_paths=resnet_640_ext_reorg_roi_g2-16_53-length-6-stride-1-batch_3/ckpt-123442-ext_reorg_roi_g2-54_126-length-6-stride-6/csv-batch_12 save_suffix=p2s-resnet_640-ipsc-16_53-len-6-strd-6-54_126-batch_8-123442
<a id="stride_1___len_6_ipsc_16_53_resnet_64_0_"></a>
#### stride-1       @ len-6/ipsc-16_53/resnet-640-->eval_det_p2s_vid
python3 eval_det.py cfg=ipsc:16_53:det-0:gt-0:nms:agn,p2s:vid det_paths=resnet_640_ext_reorg_roi_g2-16_53-length-6-stride-1-batch_3/ckpt-123442-ext_reorg_roi_g2-54_126-length-6-stride-1/csv-batch_12 save_suffix=p2s-resnet_640-ipsc-16_53-len-6-strd-1-54_126-batch_8-123442

