# n-1
## r50       @ n-1-->eval_det_mnist
### set_zero_1_2_3       @ r50/n-1-->eval_det_mnist
#### pool_8       @ set_zero_1_2_3/r50/n-1-->eval_det_mnist
python3 eval_det.py cfg=mnist_mot:n1 img_paths=lists/mnist_mot_rgb_512_1k_9600_1_var_test_1_10.txt det_paths=log/swi/faster_rcnn_r50_fpn_1x_mnist_mot_rgb_512_1k_9600_1_var-rcnn_no_fpn/best_bbox_mAP_on_test_1_10_pool_8_set_zero_1_2_3/csv gt_csv_name=annotations.csv save_suffix=mnist_mot-r50-test_1_10-set_zero_1_2_3-pool_8 iw=0 nms_thresh=0 n_proc=1 enable_mask=0
