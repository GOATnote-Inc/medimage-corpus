# BUS-UCLM (Spain Breast Ultrasound Lesion Segmentation)

**Modality:** Ultrasound | **Anatomy:** Breast | **Year:** 2025

## Overview
BUS-UCLM is a 2025 *Scientific Data* publication from Castilla-La Mancha University, Spain, providing 683 breast ultrasound images from 38 patients (174 benign, 90 malignant, 419 normal) collected at Ciudad Real General University Hospital between 2022 and 2023. All images acquired on a single Siemens ACUSON S2000 device, segmented and reviewed by two consensus-trained radiologists.

## Labels
- Lesion segmentation mask
- 3-class label (benign / malignant / normal)
- Doppler flag (whether image used Doppler)
- Combined-image flag

## Format
PNG images + masks. ~50 MB estimated.

## Access
Open at Mendeley Data https://data.mendeley.com/datasets/7fvgj4jsp7/1 (CC-BY-4.0). Mirror on Kaggle.

## Citation
Vallez et al., "BUS-UCLM: Breast ultrasound lesion segmentation dataset." *Scientific Data* (2025). DOI: 10.1038/s41597-025-04562-3

## Notes for ingestion
- Single-device, single-site = excellent held-out test for cross-vendor / cross-site BUS models trained on BUSI + BUS-BRA.
- Patient count is small (38) -- patient-level splits will give very few held-out subjects; treat as cross-domain evaluation rather than independent training cohort.
- Recent (2025) so well-curated and includes Doppler-vs-B-mode flags that older datasets lack.
