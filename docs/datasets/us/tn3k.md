# TN3K (Thyroid Nodule Segmentation)

**Modality:** Ultrasound | **Anatomy:** Thyroid | **Year:** 2021

## Overview
TN3K (Thyroid-Nodule 3K) is a single-center thyroid ultrasound dataset from Zhujiang Hospital, Southern Medical University (China). 3,493 thyroid ultrasound images from 2,421 patients collected between January 2016 and August 2020, with pixel-level masks for thyroid nodules. The dataset was curated from over 30,000 raw images, retaining only frames where the thyroid nodule region is clearly visible (excludes lymph-node images and frames with large colored Doppler regions). Multiple device vendors and views included.

## Labels
- Thyroid nodule mask (pixel-level)
- Optional thyroid-gland mask (paired with TG3K)
- Binary classification: benign (0) / malignant (1)

## Format
JPG images + paired masks. 376 MB total. Train/test split: 2,879 / 614.

## Access
Open. Mirrored on HuggingFace Hub at https://huggingface.co/datasets/haifan-gong/TN3K (MIT-licensed there). Original release via https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation.

## Citation
Gong et al., "Multi-task learning for thyroid nodule segmentation with thyroid region prior." IEEE ISBI 2021. DOI: 10.1109/ISBI48211.2021.9434087

## Notes for ingestion
- MIT license + permissive HuggingFace mirror = safe for commercial pretraining.
- Single-center / single-population (Chinese cohort) -- pair with DDTI (Colombian) for cross-domain robustness.
- Pixel masks + binary class labels enable joint multi-task heads.
