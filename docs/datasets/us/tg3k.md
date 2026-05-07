# TG3K (Thyroid Gland Segmentation)

**Modality:** Ultrasound | **Anatomy:** Thyroid (gland) | **Year:** 2021

## Overview
TG3K is the companion dataset to TN3K, focused on thyroid gland boundary segmentation rather than nodule segmentation. 3,585 ultrasound frames sampled from 16 thyroid ultrasound videos, paired with pixel-level gland masks. Often used jointly with TN3K in multi-task pipelines: gland segmentation as a region prior, nodule segmentation as the downstream task.

## Labels
- Thyroid gland mask (pixel-level)

## Format
JPG images + paired JPG masks. ~350 MB estimated (similar in scale to TN3K).

## Access
Open via the TRFE-Net GitHub repository: https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation.

## Citation
Gong et al., "Multi-task learning for thyroid nodule segmentation with thyroid region prior." IEEE ISBI 2021. DOI: 10.1109/ISBI48211.2021.9434087

## Notes for ingestion
- 16-video provenance means TG3K frames are highly correlated within a single video; do per-video splits.
- Use jointly with TN3K (3,493 nodule images) for multi-task gland + nodule segmentation -- improves nodule mIoU.
- Useful as a pretraining stage for any downstream thyroid-cancer model.
