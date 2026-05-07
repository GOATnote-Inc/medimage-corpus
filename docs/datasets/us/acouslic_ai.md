# ACOUSLIC-AI (Fetal Abdominal Circumference, Blind-Sweep)

**Modality:** Ultrasound | **Anatomy:** Fetal abdomen | **View:** Blind-sweep (caudocranial + sagittal) | **Year:** 2024

## Overview
ACOUSLIC-AI provides "blind-sweep" prenatal ultrasound data acquired by novice operators with a low-cost handheld probe (MicrUs Pro-C60S, Telemed) connected to a smartphone, for the task of automated fetal abdominal circumference (AC) measurement in low-resource obstetric settings. Training data was collected from three Public Health Units in Sierra Leone; private validation/test sets are held on Grand Challenge platform.

## Labels
- Fetal abdomen segmentation masks
- AC measurement on frames where it is measurable
- "Optimal frame" indicator for each sweep

## Format
MHA 3D stacks (each sweep = volumetric stack of 2D frames). Total ~38 GB for the open training portion. Recommended pipeline: MHA -> per-frame PNG/parquet for training, with per-sweep splits.

## Access
Open via Zenodo (CC-BY-NC-SA 4.0): https://zenodo.org/records/12697994. Use v1.1 -- v1.0 had a circumference computation bug (off by factor of 2). Validation/test sets are accessible only through Grand Challenge submissions.

## Citation
Sappia et al., "ACOUSLIC-AI challenge report: Fetal abdominal circumference measurement on blind-sweep ultrasound data from low-income countries." *Medical Image Analysis* (2025). DOI: 10.1016/j.media.2025.103608

## Notes for ingestion
- Domain shift is the point: low-skill operators + cheap probe + non-Western population.
- Use as held-out test for any fetal-biometry model trained on FETAL_PLANES_DB or HC18.
- 6-sweep protocol per case (3 transverse + 3 sagittal) -- preserve sweep grouping to avoid leakage.
