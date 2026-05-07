# AutoPET-III (FDG + PSMA PET/CT)

## What it is
AutoPET-III is the third iteration of the autoPET MICCAI challenge, expanding the original FDG-PET-CT-Lesions cohort with a PSMA prostate-cancer cohort. Public release on TCIA as the FDG-PET-CT-Lesions collection: 418.85 GB total.

- FDG cohort: 1,014 PET/CT studies from 900 subjects (501 with malignant lesions: lymphoma, melanoma, NSCLC; 513 negative controls). University Hospital Tubingen, Germany.
- PSMA cohort: 597 PET/CT studies from 378 male prostate-cancer patients (537 with PSMA-avid lesions, 60 without). University Hospital LMU Munich, Germany.

Manual whole-body tumor lesion segmentations included. Imaging acquired 2014-2018, public release 2022.

## Why it matters for training
This is the premier open whole-body PET/CT corpus. The CT half alone covers head-to-toe anatomy on hundreds of subjects, which is rare. Use cases:
- Whole-body CT pretraining (anatomy spans head to thigh)
- Tumor lesion segmentation
- PET/CT multimodal fusion
- Oncology-aware vision-language models

For "CT" scope, treat the CT volumes as the primary signal and PET as auxiliary.

## Access
Tier: credentialed (NIH Controlled Data Access Policy due to facial reconstruction risk). Apply at https://www.cancerimagingarchive.net/collection/fdg-pet-ct-lesions/ . Approval typically 2-4 weeks.

## Conversion notes
NIfTI. CT is whole-body, low-dose, often without IV contrast. Voxel spacing ~2x2x3 mm. Consider face-defacement before training models that may leak features.

## License
CC BY 4.0 (metadata); NIH Controlled (imaging).

## Citation
Gatidis S, Kuestner T. "A whole-body FDG-PET/CT dataset with manually annotated tumor lesions." Scientific Data 9:601 (2022). DOI 10.1038/s41597-022-01718-3.

## Gotchas
- Imaging gated; do not bake into a public model card without checking the access policy.
- Single-vendor (Siemens Biograph mCT) per cohort; cross-vendor robustness must be tested elsewhere.
- PSMA cohort is male-only and prostate-specific; bias check required.
