<!-- MarkdownTOC -->

- [all_frames_roi_g2_38_53       @ all_frames_roi](#all_frames_roi_g2_38_53___all_frames_roi_)
- [all_frames_roi_g2_seq_1_38_53       @ all_frames_roi](#all_frames_roi_g2_seq_1_38_53___all_frames_roi_)
- [all_frames_roi_g3_53_92       @ all_frames_roi](#all_frames_roi_g3_53_92___all_frames_roi_)
- [ext_reorg_roi_g2_0_37       @ xml_to_ytvis](#ext_reorg_roi_g2_0_37___xml_to_ytvis_)
    - [max_length-20       @ ext_reorg_roi_g2_0_37](#max_length_20___ext_reorg_roi_g2_0_3_7_)
    - [max_length-10       @ ext_reorg_roi_g2_0_37](#max_length_10___ext_reorg_roi_g2_0_3_7_)
- [ext_reorg_roi_g2_38_53       @ xml_to_ytvis](#ext_reorg_roi_g2_38_53___xml_to_ytvis_)
    - [incremental       @ ext_reorg_roi_g2_38_53](#incremental___ext_reorg_roi_g2_38_53_)
- [ext_reorg_roi_g2_16_53       @ xml_to_ytvis](#ext_reorg_roi_g2_16_53___xml_to_ytvis_)
- [ext_reorg_roi_g2_0_1       @ xml_to_ytvis](#ext_reorg_roi_g2_0_1___xml_to_ytvis_)
- [len-2:strd-1](#len_2_strd_1_)
    - [0_4       @ len-2:strd-1](#0_4___len_2_strd_1_)
        - [12094       @ 0_4/len-2:strd-1](#12094___0_4_len_2_strd_1_)
    - [5_9       @ len-2:strd-1](#5_9___len_2_strd_1_)
    - [0_37       @ len-2:strd-1](#0_37___len_2_strd_1_)
    - [16_53       @ len-2:strd-1](#16_53___len_2_strd_1_)
    - [54_126       @ len-2:strd-1](#54_126___len_2_strd_1_)
- [ext_reorg_roi_g2_0_15       @ xml_to_ytvis](#ext_reorg_roi_g2_0_15___xml_to_ytvis_)
    - [incremental       @ ext_reorg_roi_g2_0_15](#incremental___ext_reorg_roi_g2_0_1_5_)
- [ext_reorg_roi_g2_54_126       @ xml_to_ytvis](#ext_reorg_roi_g2_54_126___xml_to_ytvis_)
    - [subseq       @ ext_reorg_roi_g2_54_126](#subseq___ext_reorg_roi_g2_54_12_6_)
- [ext_reorg_roi_g2_0_53       @ xml_to_ytvis](#ext_reorg_roi_g2_0_53___xml_to_ytvis_)
    - [incremental       @ ext_reorg_roi_g2_0_53](#incremental___ext_reorg_roi_g2_0_5_3_)
- [detrac](#detra_c_)
    - [len-2       @ detrac](#len_2___detrac_)
        - [0_0       @ len-2/detrac](#0_0___len_2_detrac_)
        - [0_19       @ len-2/detrac](#0_19___len_2_detrac_)
            - [strd-2       @ 0_19/len-2/detrac](#strd_2___0_19_len_2_detra_c_)
        - [0_9       @ len-2/detrac](#0_9___len_2_detrac_)
            - [strd-2       @ 0_9/len-2/detrac](#strd_2___0_9_len_2_detrac_)
        - [49_68       @ len-2/detrac](#49_68___len_2_detrac_)
            - [strd-2       @ 49_68/len-2/detrac](#strd_2___49_68_len_2_detrac_)

<!-- /MarkdownTOC -->

<a id="all_frames_roi_g2_38_53___all_frames_roi_"></a>
# all_frames_roi_g2_38_53       @ all_frames_roi-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=all_frames_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=38 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 min_val=0 allow_missing_images=0 get_img_stats=0 description=all_frames_roi_g2_38_53 save_masks=0 coco_rle=1

<a id="all_frames_roi_g2_seq_1_38_53___all_frames_roi_"></a>
# all_frames_roi_g2_seq_1_38_53       @ all_frames_roi-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=all_frames_roi.txt n_seq=1 class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=38 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 min_val=0 allow_missing_images=0 get_img_stats=0 description=all_frames_roi_g2_seq_1_38_53 save_masks=0 coco_rle=1

<a id="all_frames_roi_g3_53_92___all_frames_roi_"></a>
# all_frames_roi_g3_53_92       @ all_frames_roi-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=all_frames_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=53 end_frame_id=92 ignore_invalid_label=1 val_ratio=0 min_val=0 allow_missing_images=0 get_img_stats=1 description=all_frames_roi_g3_53_92 save_masks=1

<a id="ext_reorg_roi_g2_0_37___xml_to_ytvis_"></a>
# ext_reorg_roi_g2_0_37       @ xml_to_ytvis-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=37 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_37 save_masks=0

<a id="max_length_20___ext_reorg_roi_g2_0_3_7_"></a>
## max_length-20       @ ext_reorg_roi_g2_0_37-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=37 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_37 save_masks=0 max_length=20 n_proc=12

<a id="max_length_10___ext_reorg_roi_g2_0_3_7_"></a>
## max_length-10       @ ext_reorg_roi_g2_0_37-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=37 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_37 save_masks=0 max_length=10 n_proc=12

<a id="ext_reorg_roi_g2_38_53___xml_to_ytvis_"></a>
# ext_reorg_roi_g2_38_53       @ xml_to_ytvis-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=38 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 min_val=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_38_53 save_masks=0 n_proc=12

<a id="incremental___ext_reorg_roi_g2_38_53_"></a>
## incremental       @ ext_reorg_roi_g2_38_53-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=38 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 min_val=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_38_53 save_masks=0 n_proc=24 incremental=1

<a id="ext_reorg_roi_g2_16_53___xml_to_ytvis_"></a>
# ext_reorg_roi_g2_16_53       @ xml_to_ytvis-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=16 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_16_53 save_masks=0 subseq=1 subseq_split_ids=21 n_proc=12

<a id="ext_reorg_roi_g2_0_1___xml_to_ytvis_"></a>
# ext_reorg_roi_g2_0_1       @ xml_to_ytvis-->xml_to_ytvis
python3 xml_to_ytvis.py cfg=ipsc:2_class start_frame_id=0 end_frame_id=1 description=ext_reorg_roi_g2_0_1 save_masks=0 n_proc=12
length_2-stride_1

<a id="len_2_strd_1_"></a>
# len-2:strd-1
<a id="0_4___len_2_strd_1_"></a>
## 0_4       @ len-2:strd-1-->xml_to_ytvis
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-0:end-4:len-2:strd-1:gz-1:gap-1 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-0:end-4:len-2:strd-1:gz-1:gap-3 

<a id="12094___0_4_len_2_strd_1_"></a>
### 12094       @ 0_4/len-2:strd-1-->xml_to_ytvis
python3 xml_to_ytvis.py cfg=ipsc:12094:2_class:mask-0:proc-12:start-0:end-4:len-2:strd-1:gz-1:gap-1 
python3 xml_to_ytvis.py cfg=ipsc:12094_short:2_class:mask-0:proc-12:start-0:end-4:len-2:strd-1:gz-1:gap-1 

<a id="5_9___len_2_strd_1_"></a>
## 5_9       @ len-2:strd-1-->xml_to_ytvis
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-5:end-9:len-2:strd-1:gz-1:gap-1 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-1:start-5:end-9:len-2:strd-1:gz-1:gap-2 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-1:start-5:end-9:len-2:strd-1:gz-1:gap-3 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-1:start-5:end-9:len-2:strd-1:gz-1:gap-4 

<a id="0_37___len_2_strd_1_"></a>
## 0_37       @ len-2:strd-1-->xml_to_ytvis
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-0:end-37:len-2:strd-1:gz-1:gap-1 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-0:end-37:len-2:strd-1:gz-1:gap-2 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-0:end-37:len-2:strd-1:gz-1:gap-3 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-0:end-37:len-2:strd-1:gz-1:gap-4
<a id="16_53___len_2_strd_1_"></a>
## 16_53       @ len-2:strd-1-->xml_to_ytvis
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-16:end-53:len-2:strd-1:gz-1:gap-1 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-16:end-53:len-2:strd-1:gz-1:gap-2 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-16:end-53:len-2:strd-1:gz-1:gap-3 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-16:end-53:len-2:strd-1:gz-1:gap-4
<a id="54_126___len_2_strd_1_"></a>
## 54_126       @ len-2:strd-1-->xml_to_ytvis
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-54:end-126:len-2:strd-1:gz-1:gap-1 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-54:end-126:len-2:strd-1:gz-1:gap-2 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-54:end-126:len-2:strd-1:gz-1:gap-3 
python3 xml_to_ytvis.py cfg=ipsc:2_class:mask-0:proc-12:start-54:end-126:len-2:strd-1:gz-1:gap-4

<a id="ext_reorg_roi_g2_0_15___xml_to_ytvis_"></a>
# ext_reorg_roi_g2_0_15       @ xml_to_ytvis-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=12
__-max_length-1__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=12 max_length=1
__-max_length-2__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=12 max_length=2
__-max_length-4__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=12 max_length=4
__-max_length-8-__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=12 max_length=8

<a id="incremental___ext_reorg_roi_g2_0_1_5_"></a>
## incremental       @ ext_reorg_roi_g2_0_15-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=24 incremental=1
__-max_length-2__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=2 incremental=1 max_length=2
__-max_length-10__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=15 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_15 save_masks=0 n_proc=2 incremental=1 max_length=10

<a id="ext_reorg_roi_g2_54_126___xml_to_ytvis_"></a>
# ext_reorg_roi_g2_54_126       @ xml_to_ytvis-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=54 end_frame_id=126 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_54_126 save_masks=0 n_proc=12
```
pix_vals_mean: [118.06, 118.06, 118.06]
pix_vals_std: [23.99, 23.99, 23.99]
```
<a id="subseq___ext_reorg_roi_g2_54_12_6_"></a>
## subseq       @ ext_reorg_roi_g2_54_126-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=54 end_frame_id=126 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_54_126 save_masks=0 n_proc=12 subseq=1 subseq_split_ids=15 n_proc=12

<a id="ext_reorg_roi_g2_0_53___xml_to_ytvis_"></a>
# ext_reorg_roi_g2_0_53       @ xml_to_ytvis-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 subseq=1 subseq_split_ids=37
__-max_length-1-__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 max_length=1
__-max_length-2-__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 max_length=2
__-max_length-4-__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 max_length=4
__-max_length-8-__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 max_length=8
__-max_length-19-__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 max_length=19 subseq=1 subseq_split_ids=37

<a id="incremental___ext_reorg_roi_g2_0_5_3_"></a>
## incremental       @ ext_reorg_roi_g2_0_53-->xml_to_ytvis
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 subseq=1 subseq_split_ids=38 incremental=1
__-max_length-2__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 incremental=1 max_length=2
__-max_length-10__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 subseq=1 subseq_split_ids=38 incremental=1 max_length=10
__-max_length-20__
python3 xml_to_ytvis.py root_dir=/data/ipsc/well3/all_frames_roi seq_paths=lists/ext_reorg_roi.txt class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt start_frame_id=0 end_frame_id=53 ignore_invalid_label=1 val_ratio=0 allow_missing_images=0 get_img_stats=0 description=ext_reorg_roi_g2_0_53 save_masks=0 n_proc=12 subseq=1 subseq_split_ids=38 incremental=1 max_length=20

<a id="detra_c_"></a>
# detrac
<a id="len_2___detrac_"></a>
## len-2       @ detrac-->xml_to_ytvis
<a id="0_0___len_2_detrac_"></a>
### 0_0       @ len-2/detrac-->xml_to_ytvis
python xml_to_ytvis.py cfg=detrac:non_empty:0_0:proc-1:len-100:strd-100:gz:gap-1:vis 
<a id="0_19___len_2_detrac_"></a>
### 0_19       @ len-2/detrac-->xml_to_ytvis
python xml_to_ytvis.py cfg=detrac:non_empty:0_19:proc-1:len-2:strd-1:gz:gap-1 
<a id="strd_2___0_19_len_2_detra_c_"></a>
#### strd-2       @ 0_19/len-2/detrac-->xml_to_ytvis
python xml_to_ytvis.py cfg=detrac:non_empty:0_19:proc-1:len-2:strd-2:gz:gap-1 
<a id="0_9___len_2_detrac_"></a>
### 0_9       @ len-2/detrac-->xml_to_ytvis
python xml_to_ytvis.py cfg=detrac:non_empty:0_9:proc-1:len-2:strd-1:gz:gap-1:vis 
<a id="strd_2___0_9_len_2_detrac_"></a>
#### strd-2       @ 0_9/len-2/detrac-->xml_to_ytvis
python xml_to_ytvis.py cfg=detrac:non_empty:0_9:proc-1:len-2:strd-2:gz:gap-1 
<a id="49_68___len_2_detrac_"></a>
### 49_68       @ len-2/detrac-->xml_to_ytvis
python xml_to_ytvis.py cfg=detrac:non_empty:49_68:proc-12:len-2:strd-1:gz:gap-1
<a id="strd_2___49_68_len_2_detrac_"></a>
#### strd-2       @ 49_68/len-2/detrac-->xml_to_ytvis
python xml_to_ytvis.py cfg=detrac:non_empty:49_68:proc-12:len-2:strd-2:gz:gap-1