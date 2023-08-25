# n-1       @ coco_to_xml-->coco_to_xml
python3 eval_det.py cfg=mnist_mot:n1 img_paths=lists/ext_reorg_roi.txt det_paths=log/swi/mnist_mot_rgb_512_1k_9600_1_var-rcnn_no_fpn/best_bbox_mAP_on_test_pool_16/csv gt_csv_name=annotations.csv save_suffix=mnist_mot-n1 nms_thresh=0 n_proc=1
