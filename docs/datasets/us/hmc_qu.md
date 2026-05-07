# HMC-QU (Hamad Medical-Qatar Echocardiogram, Myocardial Infarction)

**Modality:** Ultrasound | **Anatomy:** Heart (LV walls) | **Views:** A4C + A2C | **Year:** 2022

## Overview
HMC-QU is a multi-view 2D echocardiography dataset for myocardial infarction (MI) detection developed jointly by Hamad Medical Corporation, Tampere University, and Qatar University. The publicly released subset contains 109 A4C recordings paired with full LV-wall segmentation masks (72 MI patients + 37 non-MI subjects), plus A2C recordings of the same patients. The broader background corpus from which the public subset was sampled covers >10,000 echocardiography exams and >800 cases of acute ST-elevation MI.

## Labels
- MI / non-MI binary label
- Pixel-level LV-wall mask (A4C subset)

## Format
2D B-mode echocardiography recordings (despite some prior descriptions calling it M-mode -- it is not). MP4/AVI mixed. ~200 MB estimated.

## Access
Open via Kaggle: https://www.kaggle.com/datasets/aysendegerli/hmcqu-dataset. Non-commercial research use.

## Citation
Degerli et al., "Early Detection of Myocardial Infarction in Low-Quality Echocardiography." *IEEE Access* (2022). DOI: 10.1109/ACCESS.2022.3146148

## Notes for ingestion
- Multi-view paired data (A4C + A2C of same patients) supports joint embedding learning.
- LV-wall masks are provided only on the A4C subset; A2C is class-label only.
- Smaller cohort -- treat as fine-tuning / evaluation rather than primary pretraining.
