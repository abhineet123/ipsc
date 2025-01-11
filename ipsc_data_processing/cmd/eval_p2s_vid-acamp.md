<!-- MarkdownTOC -->

- [mid](#mid_)
    - [1k8_vid_entire_seq       @ mid](#1k8_vid_entire_seq___mi_d_)
        - [on-train       @ 1k8_vid_entire_seq/mid](#on_train___1k8_vid_entire_seq_mid_)
        - [on-inv       @ 1k8_vid_entire_seq/mid](#on_inv___1k8_vid_entire_seq_mid_)
    - [10k6_vid_entire_seq       @ mid](#10k6_vid_entire_seq___mi_d_)
        - [on-inv       @ 10k6_vid_entire_seq/mid](#on_inv___10k6_vid_entire_seq_mi_d_)
    - [1k8_vid_entire_seq-aug       @ mid](#1k8_vid_entire_seq_aug___mi_d_)
        - [on-inv       @ 1k8_vid_entire_seq-aug/mid](#on_inv___1k8_vid_entire_seq_aug_mid_)
    - [10k6_vid_entire_seq-aug       @ mid](#10k6_vid_entire_seq_aug___mi_d_)
        - [on-inv       @ 10k6_vid_entire_seq-aug/mid](#on_inv___10k6_vid_entire_seq_aug_mi_d_)
    - [20k6_5_video-aug       @ mid](#20k6_5_video_aug___mi_d_)
        - [on-inv       @ 20k6_5_video-aug/mid](#on_inv___20k6_5_video_aug_mid_)
    - [1k8_vid_entire_seq-aug-fbb       @ mid](#1k8_vid_entire_seq_aug_fbb___mi_d_)
        - [on-inv-2_per_seq       @ 1k8_vid_entire_seq-aug-fbb/mid](#on_inv_2_per_seq___1k8_vid_entire_seq_aug_fbb_mid_)
        - [on-inv-6_per_seq       @ 1k8_vid_entire_seq-aug-fbb/mid](#on_inv_6_per_seq___1k8_vid_entire_seq_aug_fbb_mid_)
        - [on-inv       @ 1k8_vid_entire_seq-aug-fbb/mid](#on_inv___1k8_vid_entire_seq_aug_fbb_mid_)
    - [10k6_vid_entire_seq-aug-fbb       @ mid](#10k6_vid_entire_seq_aug_fbb___mi_d_)
        - [on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-fbb/mid](#on_inv_2_per_seq___10k6_vid_entire_seq_aug_fbb_mi_d_)
        - [on-inv-12_per_seq       @ 10k6_vid_entire_seq-aug-fbb/mid](#on_inv_12_per_seq___10k6_vid_entire_seq_aug_fbb_mi_d_)
        - [on-inv       @ 10k6_vid_entire_seq-aug-fbb/mid](#on_inv___10k6_vid_entire_seq_aug_fbb_mi_d_)
    - [20k6_5_video-aug-fbb       @ mid](#20k6_5_video_aug_fbb___mi_d_)
        - [on-inv-2_per_seq       @ 20k6_5_video-aug-fbb/mid](#on_inv_2_per_seq___20k6_5_video_aug_fbb_mid_)
        - [on-inv-12_per_seq       @ 20k6_5_video-aug-fbb/mid](#on_inv_12_per_seq___20k6_5_video_aug_fbb_mid_)
        - [on-inv       @ 20k6_5_video-aug-fbb/mid](#on_inv___20k6_5_video_aug_fbb_mid_)
    - [1k8_vid_entire_seq-aug-cls_eq-fbb       @ mid](#1k8_vid_entire_seq_aug_cls_eq_fbb___mi_d_)
        - [on-inv-2_per_seq       @ 1k8_vid_entire_seq-aug-cls_eq-fbb/mid](#on_inv_2_per_seq___1k8_vid_entire_seq_aug_cls_eq_fbb_mi_d_)
    - [1k8_vid_entire_seq-aug-cls_eq-fbb-b64       @ mid](#1k8_vid_entire_seq_aug_cls_eq_fbb_b64___mi_d_)
        - [on-inv-2_per_seq       @ 1k8_vid_entire_seq-aug-cls_eq-fbb-b64/mid](#on_inv_2_per_seq___1k8_vid_entire_seq_aug_cls_eq_fbb_b64_mi_d_)
        - [on-inv       @ 1k8_vid_entire_seq-aug-cls_eq-fbb-b64/mid](#on_inv___1k8_vid_entire_seq_aug_cls_eq_fbb_b64_mi_d_)
    - [10k6_vid_entire_seq-aug-cls_eq-fbb       @ mid](#10k6_vid_entire_seq_aug_cls_eq_fbb___mi_d_)
        - [on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-cls_eq-fbb/mid](#on_inv_2_per_seq___10k6_vid_entire_seq_aug_cls_eq_fbb_mid_)
    - [10k6_vid_entire_seq-aug-cls_eq-fbb-b64       @ mid](#10k6_vid_entire_seq_aug_cls_eq_fbb_b64___mi_d_)
        - [on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-cls_eq-fbb-b64/mid](#on_inv_2_per_seq___10k6_vid_entire_seq_aug_cls_eq_fbb_b64_mid_)
        - [on-inv       @ 10k6_vid_entire_seq-aug-cls_eq-fbb-b64/mid](#on_inv___10k6_vid_entire_seq_aug_cls_eq_fbb_b64_mid_)
    - [10k6_vid_entire_seq-aug-cls_eq-b64       @ mid](#10k6_vid_entire_seq_aug_cls_eq_b64___mi_d_)
        - [on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-cls_eq-b64/mid](#on_inv_2_per_seq___10k6_vid_entire_seq_aug_cls_eq_b64_mid_)
        - [on-inv       @ 10k6_vid_entire_seq-aug-cls_eq-b64/mid](#on_inv___10k6_vid_entire_seq_aug_cls_eq_b64_mid_)

<!-- /MarkdownTOC -->
<a id="mid_"></a>
# mid
<a id="1k8_vid_entire_seq___mi_d_"></a>
## 1k8_vid_entire_seq       @ mid-->eval_p2s_vid-acamp
<a id="on_train___1k8_vid_entire_seq_mid_"></a>
### on-train       @ 1k8_vid_entire_seq/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq:vnms-0:nms-0:agn:gt-0:proc-0:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_18/ckpt-77082-1k8_vid_entire_seq-length-2-stride-1/csv-batch_2:_out_-p2s-mid-acamp-1k8_vid_entire_seq-len-2-train
<a id="on_inv___1k8_vid_entire_seq_mid_"></a>
### on-inv       @ 1k8_vid_entire_seq/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv:vnms:nms-1:agn:gt-1:proc-12:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_18/ckpt-77082-1k8_vid_entire_seq_inv-length-2-stride-1/csv-batch_48:_out_-p2s-mid-acamp-1k8_vid_entire_seq-len-2
`nms20`
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv:vnms-20:nms-20:agn:gt-1:proc-2:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_18/ckpt-77082-1k8_vid_entire_seq_inv-length-2-stride-1/csv-batch_48:_out_-p2s-mid-acamp-1k8_vid_entire_seq-len-2-nms20

<a id="10k6_vid_entire_seq___mi_d_"></a>
## 10k6_vid_entire_seq       @ mid-->eval_p2s_vid-acamp
<a id="on_inv___10k6_vid_entire_seq_mi_d_"></a>
### on-inv       @ 10k6_vid_entire_seq/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv:vnms:nms-1:agn:gt-1:proc-12:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_18/ckpt-278964-10k6_vid_entire_seq_inv-length-2-stride-1/csv-batch_24:_out_-p2s-mid-acamp-10k6_vid_entire_seq-len-2
`nms20`
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv:vnms-20:nms-20:agn:gt-1:proc-2:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_18/ckpt-278964-10k6_vid_entire_seq_inv-length-2-stride-1/csv-batch_24:_out_-p2s-mid-acamp-10k6_vid_entire_seq-len-2-nms20


<a id="1k8_vid_entire_seq_aug___mi_d_"></a>
## 1k8_vid_entire_seq-aug       @ mid-->eval_p2s_vid-acamp
<a id="on_inv___1k8_vid_entire_seq_aug_mid_"></a>
### on-inv       @ 1k8_vid_entire_seq-aug/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv:strds-2:vnms-1:nms-1:agn:gt-0:proc-12:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_18-jtr-res_1280/ckpt-1229325-1k8_vid_entire_seq_inv-length-2-stride-1/csv-batch_12:_out_-p2s-mid-acamp-1k8_vid_entire_seq-len-2-aug
`nms20`
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv:vnms-20:nms-20:agn:gt-1:proc-2:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_18-jtr-res_1280/ckpt-1229325-1k8_vid_entire_seq_inv-length-2-stride-1/csv-batch_12:_out_-p2s-mid-acamp-1k8_vid_entire_seq-len-2-aug-nms20

<a id="10k6_vid_entire_seq_aug___mi_d_"></a>
## 10k6_vid_entire_seq-aug       @ mid-->eval_p2s_vid-acamp
<a id="on_inv___10k6_vid_entire_seq_aug_mi_d_"></a>
### on-inv       @ 10k6_vid_entire_seq-aug/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv:strds-2:vnms-1:nms-1:agn:gt-0:proc-12:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_18-jtr-res_1280/ckpt-1145745-10k6_vid_entire_seq_inv-length-2-stride-1/csv-batch_12:_out_-p2s-mid-acamp-10k6_vid_entire_seq-len-2-aug
`nms20`
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv:vnms-20:nms-20:agn:gt-1:proc-2:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_18-jtr-res_1280/ckpt-1145745-10k6_vid_entire_seq_inv-length-2-stride-1/csv-batch_12:_out_-p2s-mid-acamp-10k6_vid_entire_seq-len-2-aug-nms20

<a id="20k6_5_video_aug___mi_d_"></a>
## 20k6_5_video-aug       @ mid-->eval_p2s_vid-acamp
<a id="on_inv___20k6_5_video_aug_mid_"></a>
### on-inv       @ 20k6_5_video-aug/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:20k6_5_video_inv:strds-2:vnms-1:nms-1:agn:gt-0:proc-0:show-0:_in_-resnet_640_20k6_5_video-length-2-stride-1-batch_18-jtr-res_1280/ckpt-1176528-20k6_5_video_inv-length-2-stride-1/csv-batch_16:_out_-p2s-mid-acamp-20k6_5_video-len-2-aug
`nms20`
python3 eval_det.py cfg=p2s:vid,acamp:20k6_5_video_inv:vnms-20:nms-20:agn:gt-1:proc-2:show-0:_in_-resnet_640_20k6_5_video-length-2-stride-1-batch_18-jtr-res_1280/ckpt-1176528-20k6_5_video_inv-length-2-stride-1/csv-batch_16:_out_-p2s-mid-acamp-20k6_5_video-len-2-augg-nms20

<a id="1k8_vid_entire_seq_aug_fbb___mi_d_"></a>
## 1k8_vid_entire_seq-aug-fbb       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___1k8_vid_entire_seq_aug_fbb_mid_"></a>
### on-inv-2_per_seq       @ 1k8_vid_entire_seq-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv_2_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_80-jtr-res_1280-fbb/ckpt-__var__-1k8_vid_entire_seq_inv_2_per_seq-length-2-stride-1/csv-batch_2:_out_-p2s-mid-1k8-len-2-aug-fbb-2_per_seq
<a id="on_inv_6_per_seq___1k8_vid_entire_seq_aug_fbb_mid_"></a>
### on-inv-6_per_seq       @ 1k8_vid_entire_seq-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv_6_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_80-jtr-res_1280-fbb/ckpt-__var__-1k8_vid_entire_seq_inv_6_per_seq-length-2-stride-1/csv-batch_8:_out_-p2s-mid-1k8-len-2-aug-fbb-6_per_seq
<a id="on_inv___1k8_vid_entire_seq_aug_fbb_mid_"></a>
### on-inv       @ 1k8_vid_entire_seq-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_80-jtr-res_1280-fbb/ckpt-__var__-1k8_vid_entire_seq_inv-length-2-stride-1/csv-batch_2:_out_-p2s-mid-1k8-len-2-aug-fbb

<a id="10k6_vid_entire_seq_aug_fbb___mi_d_"></a>
## 10k6_vid_entire_seq-aug-fbb       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___10k6_vid_entire_seq_aug_fbb_mi_d_"></a>
### on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv_2_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_72-jtr-res_1280-fbb/ckpt-__var__-10k6_vid_entire_seq_inv_2_per_seq-length-2-stride-1/csv-batch_2:_out_-p2s-mid-10k6-len-2-aug-fbb-2_per_seq
<a id="on_inv_12_per_seq___10k6_vid_entire_seq_aug_fbb_mi_d_"></a>
### on-inv-12_per_seq       @ 10k6_vid_entire_seq-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv_12_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_72-jtr-res_1280-fbb/ckpt-__var__-10k6_vid_entire_seq_inv_12_per_seq-length-2-stride-1/csv-batch_2:_out_-p2s-mid-10k6-len-2-aug-fbb-12_per_seq
<a id="on_inv___10k6_vid_entire_seq_aug_fbb_mi_d_"></a>
### on-inv       @ 10k6_vid_entire_seq-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_72-jtr-res_1280-fbb/ckpt-__var__-10k6_vid_entire_seq_inv-length-2-stride-1/csv-batch_2:_out_-p2s-mid-10k6-len-2-aug-fbb

<a id="20k6_5_video_aug_fbb___mi_d_"></a>
## 20k6_5_video-aug-fbb       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___20k6_5_video_aug_fbb_mid_"></a>
### on-inv-2_per_seq       @ 20k6_5_video-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:20k6_5_video_inv_2_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_20k6_5_video-length-2-stride-1-batch_72-jtr-res_1280-fbb/ckpt-__var__-20k6_5_video_inv_2_per_seq-length-2-stride-1/csv-batch_2:_out_-p2s-mid-20k6-len-2-aug-fbb-2_per_seq
<a id="on_inv_12_per_seq___20k6_5_video_aug_fbb_mid_"></a>
### on-inv-12_per_seq       @ 20k6_5_video-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:20k6_5_video_inv_12_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_20k6_5_video-length-2-stride-1-batch_72-jtr-res_1280-fbb/ckpt-__var__-20k6_5_video_inv_12_per_seq-length-2-stride-1/csv-batch_8:_out_-p2s-mid-20k6-len-2-aug-fbb-12_per_seq
<a id="on_inv___20k6_5_video_aug_fbb_mid_"></a>
### on-inv       @ 20k6_5_video-aug-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:20k6_5_video_inv:vnms-1:nms-1:gt-1:proc-1:show-0:_in_-resnet_640_20k6_5_video-length-2-stride-1-batch_72-jtr-res_1280-fbb/ckpt-__var__-20k6_5_video_inv-length-2-stride-1/csv-batch_2:_out_-p2s-mid-20k6-len-2-aug-fbb
`agn`
python3 eval_det.py cfg=p2s:vid,acamp:20k6_5_video_inv:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_20k6_5_video-length-2-stride-1-batch_72-jtr-res_1280-fbb/ckpt-__var__-20k6_5_video_inv-length-2-stride-1/csv-batch_2:_out_-p2s-mid-20k6-len-2-aug-fbb:iif


<a id="1k8_vid_entire_seq_aug_cls_eq_fbb___mi_d_"></a>
## 1k8_vid_entire_seq-aug-cls_eq-fbb       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___1k8_vid_entire_seq_aug_cls_eq_fbb_mi_d_"></a>
### on-inv-2_per_seq       @ 1k8_vid_entire_seq-aug-cls_eq-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv_2_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_32-jtr-res_1280-fbb-cls_eq/ckpt-__var__-1k8_vid_entire_seq_inv_2_per_seq-length-2-stride-1/csv-batch_4:_out_-p2s-mid-1k8-len-2-aug-cls_eq-fbb-2_per_seq:excp-0


<a id="1k8_vid_entire_seq_aug_cls_eq_fbb_b64___mi_d_"></a>
## 1k8_vid_entire_seq-aug-cls_eq-fbb-b64       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___1k8_vid_entire_seq_aug_cls_eq_fbb_b64_mi_d_"></a>
### on-inv-2_per_seq       @ 1k8_vid_entire_seq-aug-cls_eq-fbb-b64/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv_2_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_64-jtr-res_1280-fbb-cls_eq/ckpt-__var__-1k8_vid_entire_seq_inv_2_per_seq-length-2-stride-1/csv-batch_8:_out_-p2s-mid-1k8-len-2-aug-cls_eq-fbb-2_per_seq-b64
<a id="on_inv___1k8_vid_entire_seq_aug_cls_eq_fbb_b64_mi_d_"></a>
### on-inv       @ 1k8_vid_entire_seq-aug-cls_eq-fbb-b64/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:1k8_vid_entire_seq_inv:vnms:nms:agn:gt-1:proc-1:show-0:_in_-resnet_640_1k8_vid_entire_seq-length-2-stride-1-batch_64-jtr-res_1280-fbb-cls_eq/ckpt-281976-1k8_vid_entire_seq_inv-length-2-stride-1/csv-batch_32:_out_-p2s-mid-1k8-len-2-aug-cls_eq-fbb-b64:vbs


<a id="10k6_vid_entire_seq_aug_cls_eq_fbb___mi_d_"></a>
## 10k6_vid_entire_seq-aug-cls_eq-fbb       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___10k6_vid_entire_seq_aug_cls_eq_fbb_mid_"></a>
### on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-cls_eq-fbb/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv_2_per_seq:vnms-1:nms-1:agn:gt-1:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_32-jtr-res_1280-fbb-cls_eq/ckpt-__var__-10k6_vid_entire_seq_inv_2_per_seq-length-2-stride-1/csv-batch_4:_out_-p2s-mid-10k6-len-2-aug-cls_eq-fbb-2_per_seq


<a id="10k6_vid_entire_seq_aug_cls_eq_fbb_b64___mi_d_"></a>
## 10k6_vid_entire_seq-aug-cls_eq-fbb-b64       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___10k6_vid_entire_seq_aug_cls_eq_fbb_b64_mid_"></a>
### on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-cls_eq-fbb-b64/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv_2_per_seq:vnms-1:nms-1:agn:gt-0:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_64-jtr-res_1280-fbb-cls_eq/ckpt-__var__-10k6_vid_entire_seq_inv_2_per_seq-length-2-stride-1/csv-batch_6:_out_-p2s-mid-10k6-len-2-aug-cls_eq-fbb-b64-2_per_seq
<a id="on_inv___10k6_vid_entire_seq_aug_cls_eq_fbb_b64_mid_"></a>
### on-inv       @ 10k6_vid_entire_seq-aug-cls_eq-fbb-b64/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv:vnms:nms:agn:gt-1:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_64-jtr-res_1280-fbb-cls_eq/ckpt-__var__-10k6_vid_entire_seq_inv-length-2-stride-1/csv-batch_32:_out_-p2s-mid-10k6-len-2-aug-cls_eq-fbb-b64:dbg


<a id="10k6_vid_entire_seq_aug_cls_eq_b64___mi_d_"></a>
## 10k6_vid_entire_seq-aug-cls_eq-b64       @ mid-->eval_p2s_vid-acamp
<a id="on_inv_2_per_seq___10k6_vid_entire_seq_aug_cls_eq_b64_mid_"></a>
### on-inv-2_per_seq       @ 10k6_vid_entire_seq-aug-cls_eq-b64/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv_2_per_seq:vnms-1:nms-1:agn:gt-0:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_18-jtr-res_1280-cls_eq/ckpt-__var__-10k6_vid_entire_seq_inv_2_per_seq-length-2-stride-1/csv-batch_6:_out_-p2s-mid-10k6-len-2-aug-cls_eq-2_per_seq
<a id="on_inv___10k6_vid_entire_seq_aug_cls_eq_b64_mid_"></a>
### on-inv       @ 10k6_vid_entire_seq-aug-cls_eq-b64/mid-->eval_p2s_vid-acamp
python3 eval_det.py cfg=p2s:vid,acamp:10k6_vid_entire_seq_inv:vnms:nms:agn:gt-1:proc-1:show-0:_in_-resnet_640_10k6_vid_entire_seq-length-2-stride-1-batch_64-jtr-res_1280-fbb-cls_eq/ckpt-__var__-10k6_vid_entire_seq_inv-length-2-stride-1/csv-batch_32:_out_-p2s-mid-10k6-len-2-aug-cls_eq-fbb-b64:dbg



