2023-08-22 2:27:41 PM
## n-1       @ mnist_mot-->swin_det
python3 tools/test.py config=configs/swin/mnist_mot_rgb_512_1k_9600_1_var-rcnn.py checkpoint=work_dirs/mnist_mot_rgb_512_1k_9600_1_var-rcnn/best_bbox_mAP.pth eval=bbox test_name=val

mmdet/models/detectors/two_stage.py: simple_test:203	
	rpn_head.simple_test_rpn >> mmdet/models/dense_heads/rpn_test_mixin.py: simple_test_rpn:24
	`rpn_outs = self(x)` >>  mmdet/models/dense_heads/rpn_head.py: forward_single: 41
		`rpn_conv`: 3 x 3 conv2d with size preservation
		`rpn_cls`: depthwise conv with 1 channel output
		`rpn_reg`: depthwise conv with 3 x 4 = 12 channel output (3 = num anchors)
	`get_bboxes`: mmdet/models/dense_heads/rpn_head.py:_get_bboxes: 82
		handcrafted post processing (mostly reshaping and such) including NMS		
	`roi_head`: mmdet/models/roi_heads/cascade_roi_head.py: simple_test: 290
		one bbox head and one mask		
		`_bbox_forward`: 140
			bbox_roi_extractor: one for each stage: mmdet/models/roi_heads/roi_extractors/single_level_roi_extractor.py: forward: 54
				`num_levels`: same as number of feature maps in x = 4
				`roi_layers`: num_levels RoIAlign layers >> mmcv/ops/roi_align.py: RoIAlignFunction:14
					or torchvision.ops.roi_align: torchvision/ops/roi_align.py
					"Performs Region of Interest (RoI) Align operator with average pooling, as described in Mask R-CNN."
					so eventually there is indeed avergage pooling after all the annoying layers of abstraction to cloud it up
				`roi_feats`: torch.Size([947, 256, 7, 7]): 947 = number of proposals				
			`bbox_head`: one for each stage: mmdet/models/roi_heads/bbox_heads/convfc_bbox_head.py
				shared_convs, cls_convs, reg_convs: each is a bunch of conv2d layers folowed by fc layers
					shared_convs applied first followed by applying cls_convs and reg_convs separately on its output
					optional AvgPool2d between conv and fc layers in each group

			
		
		
		
	
