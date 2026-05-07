# RVENet (Right Ventricular Echocardiography Network)

**Modality:** Ultrasound | **Anatomy:** Heart (right ventricle) | **View:** A4C | **Year:** 2023

## Overview
RVENet is a Hungarian (Semmelweis University) echocardiogram dataset focused on the right ventricle, an under-represented chamber in most echo datasets. 3,583 2D apical four-chamber DICOM videos from 831 individuals across 944 examinations. Ten clinical subgroups including healthy volunteers, athletes, heart-failure patients, valve-disease patients, transplant recipients, and others. Right-ventricular ejection fraction (RVEF) ground truth is derived from 3D echocardiography, making this the largest paired 2D-A4C / 3D-RVEF benchmark.

## Labels
- RV end-diastolic volume / end-systolic volume
- RVEF (3D echo derived)
- Per-video quality rating + image orientation
- Clinical diagnosis label

## Format
DICOM video files plus a CSV label file. ~1.5 GB estimated. Recommend MP4 + frames extraction with anonymized DICOM metadata kept side-by-side.

## Access
Application required via Google Form at https://forms.gle/teurXNjHpFtXwPYB6. Strict non-commercial research use; sharing of download links is explicitly prohibited.

## Citation
Magyar et al., "RVENet: A Large Echocardiographic Dataset for the Deep Learning-Based Assessment of Right Ventricular Function." ECCV Workshops (2023). DOI: 10.1007/978-3-031-25082-8_42

## Notes for ingestion
- Excellent complement to EchoNet-Dynamic since right-ventricular function is poorly addressed there.
- Heterogeneous patient cohorts -- stratify validation by subgroup (athletes vs HF vs transplant).
- DICOM headers contain device + frame-rate metadata; preserve them for video-encoder regularization.
