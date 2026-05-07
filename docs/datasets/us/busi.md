# BUSI (Breast Ultrasound Images, Cairo)

**Modality:** Ultrasound | **Anatomy:** Breast | **Year:** 2020

## Overview
BUSI is the most-cited public breast ultrasound dataset. 780 PNG images from 600 female patients aged 25-75 collected at Baheya Hospital for Early Detection and Treatment of Women's Cancer in Cairo, Egypt. Three classes: 437 benign, 210 malignant, 133 normal. Pixel-level segmentation masks provided for benign and malignant cases. Average image size approximately 500x500 pixels.

## Labels
- 3-class label (normal / benign / malignant)
- Lesion mask (PNG, paired with each non-normal image)

## Format
PNG. 206 MB total. Single-image dataset, no video.

## Access
Open. Original page at Cairo University: https://scholar.cu.edu.eg/?q=afahmy/pages/dataset. Convenient mirrors on Kaggle and Academic Torrents.

## Citation
Al-Dhabyani, Gomaa, Khaled, Fahmy, "Dataset of breast ultrasound images." *Data in Brief* 28, 104863 (2020). DOI: 10.1016/j.dib.2019.104863

## Notes for ingestion
- BUSI has known errata: a 2023 PMC letter documents duplicate images and missing-mask cases. Run dedup + mask-availability filter at ingestion.
- Cairo origin = useful Middle-Eastern population alongside BUS-BRA (Brazil), BUS-UCLM (Spain), UDIAT (Spain), BrEaST (Poland).
- Single device per study assumed; useful as in-domain training set with cross-domain test from BUS-UCLM/UDIAT.
