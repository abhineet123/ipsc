<a id="all_frames_roi_g2_0_37___coco_to_xm_l_"></a>
# n-1       @ coco_to_xml-->coco_to_xml
python3 coco_to_xml.py root_dir=/data/ipsc/well3/all_frames_roi json=swin_det/ipsc_2_class_all_frames_roi_g2_0_37/g2_38_53/results.segm.json  gt_json=all_frames_roi_g2_38_53.json class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt save_csv=1

python3 coco_to_xml.py root_dir=/data/ipsc/well3/all_frames_roi json=swin_det/ipsc_2_class_all_frames_roi_g2_0_37/g2_38_53/results.segm.json  gt_json=ytvis19/ytvis-ipsc-all_frames_roi_g2_38_53_coco.json class_names_path=lists/classes/predefined_classes_ipsc_2_class.txt