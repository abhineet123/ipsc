# n-1       @ coco_to_xml-->coco_to_xml
python3 eval_det.py cfg=mnist_mot:n1 img_paths=lists/mnist_mot_rgb_512_1k_9600_1_var_test.txt det_paths=log/swi/mnist_mot_rgb_512_1k_9600_1_var-rcnn_no_fpn/best_bbox_mAP_on_test/csv gt_csv_name=annotations.csv save_suffix=mnist_mot-n1 nms_thresh=0 n_proc=1 enable_mask=0
## pool_2       @ n-1-->eval_det_mnist
python3 eval_det.py cfg=mnist_mot:n1 img_paths=lists/mnist_mot_rgb_512_1k_9600_1_var_test.txt det_paths=log/swi/mnist_mot_rgb_512_1k_9600_1_var-rcnn_no_fpn/best_bbox_mAP_on_test_pool_2/csv gt_csv_name=annotations.csv save_suffix=mnist_mot-n1-pool_2 nms_thresh=0 n_proc=1 enable_mask=0
## pool_4       @ n-1-->eval_det_mnist
python3 eval_det.py cfg=mnist_mot:n1 img_paths=lists/mnist_mot_rgb_512_1k_9600_1_var_test.txt det_paths=log/swi/mnist_mot_rgb_512_1k_9600_1_var-rcnn_no_fpn/best_bbox_mAP_on_test_pool_4/csv gt_csv_name=annotations.csv save_suffix=mnist_mot-n1-pool_4 nms_thresh=0 n_proc=1 enable_mask=0
## pool_8       @ n-1-->eval_det_mnist
python3 eval_det.py cfg=mnist_mot:n1 img_paths=lists/mnist_mot_rgb_512_1k_9600_1_var_test.txt det_paths=log/swi/mnist_mot_rgb_512_1k_9600_1_var-rcnn_no_fpn/best_bbox_mAP_on_test_pool_8/csv gt_csv_name=annotations.csv save_suffix=mnist_mot-n1-pool_8 nms_thresh=0 n_proc=1 enable_mask=0
## pool_16       @ n-1-->eval_det_mnist
python3 eval_det.py cfg=mnist_mot:n1 img_paths=lists/mnist_mot_rgb_512_1k_9600_1_var_test.txt det_paths=log/swi/mnist_mot_rgb_512_1k_9600_1_var-rcnn_no_fpn/best_bbox_mAP_on_test_pool_16/csv gt_csv_name=annotations.csv save_suffix=mnist_mot-n1-pool_16 nms_thresh=0 n_proc=1 enable_mask=0
