# RSNA Cervical Spine Fracture Detection 2022

## What it is
The 2022 RSNA Cervical Spine Fracture Detection corpus is the largest open cervical spine CT trauma dataset. It contains 3,112 CT scans (1,445 fracture-positive, 1,667 negative). Distribution: 2,019 train / 304 public test / 789 private test.

Labels: per-vertebra fracture label (C1-C7), exam-level overall fracture label, plus pixel-level NIfTI segmentation masks of the cervical vertebrae (C1-C7) for a subset.

## Why it matters for training
- Largest open cervical spine CT corpus
- Trauma context (high clinical impact)
- Per-vertebra labels enable structured prediction
- Both DICOM volumes and NIfTI segmentations included

Use for fracture-detection finetuning, spine localization warm-start, and combined with VerSe / CTSpine1K for spine-pretraining stacks.

## Access
Tier: registration. Kaggle: https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection . Accept rules.

## Conversion notes
DICOM volumes, multi-vendor. NIfTI vertebral segmentations have integer labels 1-7 (C1-C7). Convert with dcm2niix; align to NIfTI masks with the SeriesInstanceUID file mapping. Voxel spacing typically 0.5mm in-plane / 0.625-1.25mm through-plane.

## License
RSNA Kaggle competition data license; research use only.

## Citation
Lin HM et al. "The RSNA Cervical Spine Fracture CT Dataset." Radiology: AI 5:e230034 (2023). DOI 10.1148/ryai.230034.

## Gotchas
- Size estimate ~60 GB; confirm via Kaggle CLI.
- Segmentations only on a subset.
- Test set labels are embargoed; benchmark via held-out training split.
