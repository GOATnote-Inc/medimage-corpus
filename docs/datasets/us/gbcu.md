# GBCU (Gallbladder Cancer Ultrasound)

**Modality:** Ultrasound | **Anatomy:** Abdomen / gallbladder | **Year:** 2022

## Overview
GBCU is the first publicly available dataset for gallbladder cancer (GBC) detection from ultrasound, released alongside Basu et al.'s CVPR 2022 paper "Surpassing the Human Accuracy". 1,255 annotated abdominal ultrasound images (432 normal, 558 benign, 265 malignant) from 218 patients (71 normal, 100 benign, 47 malignant). Each image carries a 3-class label and an axis-aligned bounding box around the gallbladder + adjacent liver parenchyma. Both sagittal and axial views are included. Biopsy-confirmed labels.

## Labels
- 3-class: normal / benign / malignant
- Bounding box for gallbladder region

## Format
PNG images at native resolution (801-1556 px wide x 564-947 px tall). ~250 MB estimated. Train/test split: 1,133 / 122.

## Access
Application-gated via https://gbc-iitd.github.io/data/gbcu. License agreement must be signed and emailed to Dr. Pankaj Gupta and Dr. Chetan Arora; only permanent faculty/employee requests are accepted.

## Citation
Basu et al., "Surpassing the Human Accuracy: Detecting Gallbladder Cancer from USG Images with Curriculum Learning." CVPR 2022, pp. 20854-20864.

## Notes for ingestion
- Important non-cardiac, non-breast abdominal benchmark -- adds anatomical diversity to a pretraining mix.
- License is the most restrictive in this manifest (institutional faculty only). Plan early.
- Pair with FocusMAE GBC-video data (2024) once that dataset is publicly available for richer pretraining.
