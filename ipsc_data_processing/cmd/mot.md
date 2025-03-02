<!-- MarkdownTOC -->

- [mot_to_synthetic](#mot_to_syntheti_c_)
    - [CTMC       @ mot_to_synthetic](#ctmc___mot_to_synthetic_)
    - [CTC       @ mot_to_synthetic](#ctc___mot_to_synthetic_)
- [mot_csv_to_xml_coco](#mot_csv_to_xml_coco_)
    - [CTC       @ mot_csv_to_xml_coco](#ctc___mot_csv_to_xml_coc_o_)
        - [annotations       @ CTC/mot_csv_to_xml_coco](#annotations___ctc_mot_csv_to_xml_coc_o_)
    - [CTMC       @ mot_csv_to_xml_coco](#ctmc___mot_csv_to_xml_coc_o_)
        - [annotations       @ CTMC/mot_csv_to_xml_coco](#annotations___ctmc_mot_csv_to_xml_coco_)
    - [ipsc       @ mot_csv_to_xml_coco](#ipsc___mot_csv_to_xml_coc_o_)
    - [gram       @ mot_csv_to_xml_coco](#gram___mot_csv_to_xml_coc_o_)
    - [idot       @ mot_csv_to_xml_coco](#idot___mot_csv_to_xml_coc_o_)
        - [mot       @ idot/mot_csv_to_xml_coco](#mot___idot_mot_csv_to_xml_coco_)
        - [csv       @ idot/mot_csv_to_xml_coco](#csv___idot_mot_csv_to_xml_coco_)
    - [mot15       @ mot_csv_to_xml_coco](#mot15___mot_csv_to_xml_coc_o_)
    - [mot17       @ mot_csv_to_xml_coco](#mot17___mot_csv_to_xml_coc_o_)
    - [detrac       @ mot_csv_to_xml_coco](#detrac___mot_csv_to_xml_coc_o_)
        - [ignored       @ detrac/mot_csv_to_xml_coco](#ignored___detrac_mot_csv_to_xml_coco_)
- [mot_to_csv](#mot_to_cs_v_)
    - [CTC       @ mot_to_csv](#ctc___mot_to_csv_)
        - [annotations       @ CTC/mot_to_csv](#annotations___ctc_mot_to_csv_)
        - [detections_syn_3       @ CTC/mot_to_csv](#detections_syn_3___ctc_mot_to_csv_)
    - [CTMC       @ mot_to_csv](#ctmc___mot_to_csv_)
        - [annotations       @ CTMC/mot_to_csv](#annotations___ctmc_mot_to_cs_v_)
        - [detections_syn_3       @ CTMC/mot_to_csv](#detections_syn_3___ctmc_mot_to_cs_v_)
        - [detections_MOT       @ CTMC/mot_to_csv](#detections_mot___ctmc_mot_to_cs_v_)
    - [MNIST_MOT_RGB       @ mot_to_csv](#mnist_mot_rgb___mot_to_csv_)
    - [mot15_obsolete       @ mot_to_csv](#mot15_obsolete___mot_to_csv_)
    - [mot17_obsolete       @ mot_to_csv](#mot17_obsolete___mot_to_csv_)
        - [frcnn       @ mot17_obsolete/mot_to_csv](#frcnn___mot17_obsolete_mot_to_cs_v_)
        - [sdp       @ mot17_obsolete/mot_to_csv](#sdp___mot17_obsolete_mot_to_cs_v_)
        - [dpm       @ mot17_obsolete/mot_to_csv](#dpm___mot17_obsolete_mot_to_cs_v_)
    - [detrac       @ mot_to_csv](#detrac___mot_to_csv_)
        - [ignored       @ detrac/mot_to_csv](#ignored___detrac_mot_to_cs_v_)
    - [GRAM       @ mot_to_csv](#gram___mot_to_csv_)
        - [no_idot       @ GRAM/mot_to_csv](#no_idot___gram_mot_to_cs_v_)
    - [IDOT       @ mot_to_csv](#idot___mot_to_csv_)
        - [linux       @ IDOT/mot_to_csv](#linux___idot_mot_to_cs_v_)
            - [detrac_48_MVI_40991       @ linux/IDOT/mot_to_csv](#detrac_48_mvi_40991___linux_idot_mot_to_cs_v_)
    - [MOT2015       @ mot_to_csv](#mot2015___mot_to_csv_)
    - [MOT2017       @ mot_to_csv](#mot2017___mot_to_csv_)
        - [FRCNN       @ MOT2017/mot_to_csv](#frcnn___mot2017_mot_to_csv_)
        - [DPM       @ MOT2017/mot_to_csv](#dpm___mot2017_mot_to_csv_)
        - [SDP       @ MOT2017/mot_to_csv](#sdp___mot2017_mot_to_csv_)
- [MOT17_old](#mot17_old_)
        - [temporal_subsampling       @ MOT17_old/](#temporal_subsampling___mot17_old_)
- [csv_to_mot](#csv_to_mo_t_)
    - [isl       @ csv_to_mot](#isl___csv_to_mot_)
    - [ctc       @ csv_to_mot](#ctc___csv_to_mot_)
    - [ctmc       @ csv_to_mot](#ctmc___csv_to_mot_)
    - [detrac       @ csv_to_mot](#detrac___csv_to_mot_)
        - [rec_40       @ detrac/csv_to_mot](#rec_40___detrac_csv_to_mo_t_)
    - [mot15       @ csv_to_mot](#mot15___csv_to_mot_)
    - [mot17       @ csv_to_mot](#mot17___csv_to_mot_)

<!-- /MarkdownTOC -->

<a id="mot_to_syntheti_c_"></a>
# mot_to_synthetic
<a id="ctmc___mot_to_synthetic_"></a>
## CTMC       @ mot_to_synthetic-->mot

python mot_to_synthetic.py root_dir=/data/CTMC/Images list_file_name=ctmc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell

<a id="ctc___mot_to_synthetic_"></a>
## CTC       @ mot_to_synthetic-->mot

python mot_to_synthetic.py root_dir=/data/CTC/Images list_file_name=ctc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell

<a id="mot_csv_to_xml_coco_"></a>
# mot_csv_to_xml_coco

<a id="ctc___mot_csv_to_xml_coc_o_"></a>
## CTC       @ mot_csv_to_xml_coco-->mot
<a id="annotations___ctc_mot_csv_to_xml_coc_o_"></a>
### annotations       @ CTC/mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py root_dir=/data/CTC img_dir=Images seg_dir=Labels_TIF list_file_name=lists/ctc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell show_img=1 seg_ext=tif raw_ctc_seg=1 save_video=1 vis_size=1920x1080

<a id="ctmc___mot_csv_to_xml_coc_o_"></a>
## CTMC       @ mot_csv_to_xml_coco-->mot
<a id="annotations___ctmc_mot_csv_to_xml_coco_"></a>
### annotations       @ CTMC/mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py root_dir=/data/CTMC img_dir=Images list_file_name=lists/ctmc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell show_img=0 save_video=1 vis_size=1920x1080

python mot_csv_to_xml_coco.py root_dir=/data/CTMC img_dir=Images list_file_name=ctmc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell show_img=0 save_video=0 start_id=29

<a id="ipsc___mot_csv_to_xml_coc_o_"></a>
## ipsc       @ mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=ipsc:zip:csv:vid-2:fps-5:show-0:fhd

<a id="gram___mot_csv_to_xml_coc_o_"></a>
## gram       @ mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=gram:zip:mot:vid

<a id="idot___mot_csv_to_xml_coc_o_"></a>
## idot       @ mot_csv_to_xml_coco-->mot
<a id="mot___idot_mot_csv_to_xml_coco_"></a>
### mot       @ idot/mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=idot:1_1:zip:mot:vid
<a id="csv___idot_mot_csv_to_xml_coco_"></a>
### csv       @ idot/mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=idot:zip:csv
python mot_csv_to_xml_coco.py cfg=idot:8_8:zip:csv

<a id="mot15___mot_csv_to_xml_coc_o_"></a>
## mot15       @ mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=mot15:zip:mot:vid

<a id="mot17___mot_csv_to_xml_coc_o_"></a>
## mot17       @ mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=mot17:zip:mot:vid

<a id="detrac___mot_csv_to_xml_coc_o_"></a>
## detrac       @ mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=detrac:non_empty:zip:mot::vid

python mot_csv_to_xml_coco.py cfg=detrac:non_empty:zip:mot:start-19:end-19
python mot_csv_to_xml_coco.py cfg=detrac:non_empty:zip:mot:start-0:end-0
<a id="ignored___detrac_mot_csv_to_xml_coco_"></a>
### ignored       @ detrac/mot_csv_to_xml_coco-->mot
python mot_csv_to_xml_coco.py cfg=detrac:non_empty:mot:ignored
`dbg`
python mot_csv_to_xml_coco.py cfg=detrac:non_empty:mot:ignored:start-0:end-0:show
python mot_csv_to_xml_coco.py cfg=detrac:non_empty:mot:ignored:start-11:end-50:show

<a id="mot_to_cs_v_"></a>
# mot_to_csv

<a id="ctc___mot_to_csv_"></a>
## CTC       @ mot_to_csv-->mot
<a id="annotations___ctc_mot_to_csv_"></a>
### annotations       @ CTC/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/CTC/Images list_file_name=ctc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell show_img=0

python mot_to_csv.py root_dir=/data/CTC/Images list_file_name=ctc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell show_img=0 stats_only=1

<a id="detections_syn_3___ctc_mot_to_csv_"></a>
### detections_syn_3       @ CTC/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/CTC/Images list_file_name=ctc_train.txt data_type=detections_syn_3 mode=1 ignore_invalid=1 start_id=0 show_img=0 label=cell

<a id="ctmc___mot_to_csv_"></a>
## CTMC       @ mot_to_csv-->mot
<a id="annotations___ctmc_mot_to_cs_v_"></a>
### annotations       @ CTMC/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/CTMC/Images list_file_name=ctmc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell show_img=0

python mot_to_csv.py root_dir=/data/CTMC/Images list_file_name=ctmc_train.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=cell show_img=0 stats_only=1


<a id="detections_syn_3___ctmc_mot_to_cs_v_"></a>
### detections_syn_3       @ CTMC/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/CTMC/Images list_file_name=ctmc_train.txt data_type=detections_syn_3 mode=1 ignore_invalid=1 start_id=0 show_img=0 label=cell

<a id="detections_mot___ctmc_mot_to_cs_v_"></a>
### detections_MOT       @ CTMC/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/CTMC/Images list_file_name=ctmc_all.txt data_type=detections_MOT mode=1 ignore_invalid=2 start_id=0 show_img=0 label=cell

<a id="mnist_mot_rgb___mot_to_csv_"></a>
## MNIST_MOT_RGB       @ mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MNIST_MOT_RGB/Images data_type=annotations mode=1 vis_size=600x600

<a id="mot15_obsolete___mot_to_csv_"></a>
## mot15_obsolete       @ mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2015/Images list_file_name=mot15.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=annotations

python mot_to_csv.py root_dir=/data/MOT2015/Images list_file_name=mot15.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=detections percent_scores=1 clamp_scores=1

<a id="mot17_obsolete___mot_to_csv_"></a>
## mot17_obsolete       @ mot_to_csv-->mot
<a id="frcnn___mot17_obsolete_mot_to_cs_v_"></a>
### frcnn       @ mot17_obsolete/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2017/Images list_file_name=mot17_frcnn.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=annotations

python mot_to_csv.py root_dir=/data/MOT2017/Images list_file_name=mot17_frcnn.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=detections percent_scores=0 clamp_scores=1

<a id="sdp___mot17_obsolete_mot_to_cs_v_"></a>
### sdp       @ mot17_obsolete/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2017_SDP/Images list_file_name=mot17_sdp.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=annotations

python mot_to_csv.py root_dir=/data/MOT2017_SDP/Images list_file_name=mot17_sdp.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=detections percent_scores=0 clamp_scores=1

<a id="dpm___mot17_obsolete_mot_to_cs_v_"></a>
### dpm       @ mot17_obsolete/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2017_DPM/Images list_file_name=mot17_dpm.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=annotations

python mot_to_csv.py root_dir=/data/MOT2017_DPM/Images list_file_name=mot17_dpm.txt show_img=0 ignore_occl=0 mode=1 start_id=0 label=person data_type=detections percent_scores=0 clamp_scores=1

<a id="detrac___mot_to_csv_"></a>
## detrac       @ mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/DETRAC/Images show_img=0 mode=1 start_id=0 end_id=0 data_type=annotations ignore_invalid=1 class_names_path=lists/classes/vehicle.txt sample=0

python mot_to_csv.py root_dir=/data/DETRAC/Images show_img=0 mode=1 start_id=0 label=vehicle data_type=detections

<a id="ignored___detrac_mot_to_cs_v_"></a>
### ignored       @ detrac/mot_to_csv-->mot
python mot_to_csv.py list_file_name=lists/detrac.txt root_dir=/data/DETRAC/Images mode=1 start_id=0 end_id=0 data_type=annotations ignore_invalid=1 class_names_path=lists/classes/vehicle_ignored.txt sample=0 allow_ignored=1 show_img=0

python mot_to_csv.py list_file_name=lists/detrac.txt root_dir=/data/DETRAC/Images mode=1 data_type=annotations ignore_invalid=1 class_names_path=lists/classes/vehicle_ignored.txt sample=0 allow_ignored=1 show_img=0


<a id="gram___mot_to_csv_"></a>
## GRAM       @ mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/GRAM/Images show_img=0 ignore_occl=0 mode=1 start_id=0 label=vehicle data_type=annotations

python mot_to_csv.py root_dir=/data/GRAM/Images show_img=0 ignore_occl=0 mode=1 start_id=0 label=vehicle data_type=detections

<a id="no_idot___gram_mot_to_cs_v_"></a>
### no_idot       @ GRAM/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/GRAM/Images list_file_name=gram_only.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=vehicle show_img=0 stats_only=1


<a id="idot___mot_to_csv_"></a>
## IDOT       @ mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/IDOT/Images list_file_name=idot.txt data_type=annotations mode=1 ignore_invalid=1 start_id=0 label=vehicle show_img=0 stats_only=1

<a id="linux___idot_mot_to_cs_v_"></a>
### linux       @ IDOT/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/DETRAC/Images show_img=0 ignore_occl=0 mode=1 start_id=0 label=vehicle

<a id="detrac_48_mvi_40991___linux_idot_mot_to_cs_v_"></a>
#### detrac_48_MVI_40991       @ linux/IDOT/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/DETRAC/Images show_img=1 ignore_occl=0 mode=1 start_id=0 label=vehicle start_id=47

<a id="mot2015___mot_to_csv_"></a>
## MOT2015       @ mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2015/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 percent_scores=1 label=person

python mot_to_csv.py root_dir=/data/MOT2015/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 label=person percent_scores=1 data_type=detections clamp_scores=1

<a id="mot2017___mot_to_csv_"></a>
## MOT2017       @ mot_to_csv-->mot
<a id="frcnn___mot2017_mot_to_csv_"></a>
### FRCNN       @ MOT2017/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2017/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 label=person

python mot_to_csv.py root_dir=/data/MOT2017/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 label=person percent_scores=1 data_type=detections out_suffix=frcnn clamp_scores=1

<a id="dpm___mot2017_mot_to_csv_"></a>
### DPM       @ MOT2017/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2017_DPM/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 label=person

python mot_to_csv.py root_dir=/data/MOT2017_DPM/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 label=person data_type=detections out_suffix=dpm clamp_scores=1

<a id="sdp___mot2017_mot_to_csv_"></a>
### SDP       @ MOT2017/mot_to_csv-->mot
python mot_to_csv.py root_dir=/data/MOT2017_SDP/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 label=person

python mot_to_csv.py root_dir=/data/MOT2017_SDP/Images show_img=0 ignore_occl=0 mode=1 start_id=0 ignore_missing=1 label=person data_type=detections out_suffix=sdp

<a id="mot17_old_"></a>
# MOT17_old
python mot_to_csv.py root_dir=G:\Datasets\MOT17\train show_img=1 ignore_occl=0
python mot_to_csv.py root_dir=G:\Datasets\MOT17\train show_img=1 ignore_occl=0  save_raw=1 ext=jpg

<a id="temporal_subsampling___mot17_old_"></a>
### temporal_subsampling       @ MOT17_old/-->mot
python temporal_subsampling.py root_dir=G:\Datasets\Acamp\acamp10k\mot show_img=1 start_id=0 frame_gap=2 ext=jpg save_raw=1 out_root_dir=G:\Datasets\Acamp\acamp10k\mot\ss_0_2 show_img=0

<a id="csv_to_mo_t_"></a>
# csv_to_mot
<a id="isl___csv_to_mot_"></a>
## isl       @ csv_to_mot-->mot
python csv_to_mot.py root_dir=/data/ISL/Images recursive=1 data_type=annotations

<a id="ctc___csv_to_mot_"></a>
## ctc       @ csv_to_mot-->mot
python csv_to_mot.py root_dir=/data/CTC/Images recursive=1 data_type=detections

<a id="ctmc___csv_to_mot_"></a>
## ctmc       @ csv_to_mot-->mot
python csv_to_mot.py root_dir=/data/CTMC/Images recursive=1 data_type=detections

<a id="detrac___csv_to_mot_"></a>
## detrac       @ csv_to_mot-->mot
python csv_to_mot.py root_dir=/data/DETRAC/Images recursive=1 data_type=detections

<a id="rec_40___detrac_csv_to_mo_t_"></a>
### rec_40       @ detrac/csv_to_mot-->mot
python csv_to_mot.py root_dir=/data/DETRAC/Images recursive=1 data_type=detections_rec_40

<a id="mot15___csv_to_mot_"></a>
## mot15       @ csv_to_mot-->mot
python csv_to_mot.py root_dir=/data/MOT2015/Images recursive=1 data_type=detections
python csv_to_mot.py root_dir=/data/MOT2015/Images recursive=1 data_type=detections_rec_40

<a id="mot17___csv_to_mot_"></a>
## mot17       @ csv_to_mot-->mot
python csv_to_mot.py root_dir=/data/MOT2017/Images recursive=1 data_type=detections
python csv_to_mot.py root_dir=/data/MOT2017/Images recursive=1 data_type=detections_rec_40
