_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_CosineAnnealingLr_1x.py', '../_base_/default_runtime.py'
]


lr_config = dict(
    policy='CosineAnnealing',
    min_lr=0.001)