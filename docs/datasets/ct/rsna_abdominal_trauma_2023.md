# RSNA Abdominal Trauma Detection 2023

## What it is
The 2023 RSNA Abdominal Trauma Detection corpus is the first multi-phase CT dataset RSNA has assembled. It contains 4,711 CT exams from 23 sites in 14 countries on six continents (more than 4,000 exams with abdominal injuries plus a roughly equal number of negative cases).

Labels: per-organ injury labels (liver, spleen, kidneys: healthy / low-grade / high-grade per AAST), bowel injury, active extravasation, "any injury" exam-level. A subset has voxel-level segmentation masks for liver, spleen, and kidneys. Approximately 90 GiB classification subset.

## Why it matters for training
- Largest open multi-phase abdominal CT corpus
- Trauma-specific labels (rare in open data)
- Multi-organ multi-task supervision
- International multi-center diversity

Use for trauma-classification finetuning, organ-injury grading, and as additional supervised signal during multi-task abdominal CT pretraining.

## Access
Tier: registration. Kaggle: https://www.kaggle.com/competitions/rsna-2023-abdominal-trauma-detection . Accept rules. Pull via `kaggle competitions download -c rsna-2023-abdominal-trauma-detection`.

## Conversion notes
DICOM, multi-phase (non-contrast, arterial, portal-venous), multi-vendor. Convert to NIfTI per series with dcm2niix. Phase metadata is mixed; may need parser. Voxel spacing varies; resample to 1.5mm isotropic for joint detection / segmentation.

## License
RSNA Kaggle competition data license; research use only.

## Citation
Rudie JD et al. "RSNA 2023 Abdominal Trauma AI Challenge: Review and Outcomes." Radiology: AI (2024). DOI 10.1148/ryai.240334.

## Gotchas
- Multi-phase requires phase-aware loaders; do not collapse phases naively.
- Segmentation subset is small relative to total exams; don't expect masks on every case.
- Trauma cases skew to younger adult demographic; bias check needed.
