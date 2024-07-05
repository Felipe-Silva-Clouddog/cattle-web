# Copyright (c) OpenMMLab. All rights reserved.
from .coco_api import COCO, COCOeval
from .panoptic_evaluation import pq_compute_multi_core, pq_compute_single_core
from .cocoeval_mp import COCOevalMP
from .coco_api import COCO, COCOeval, COCOPanoptic

__all__ = [
    'COCO', 'COCOeval', 'pq_compute_multi_core', 'pq_compute_single_core', 'COCOevalMP', 'COCOPanoptic'
]
