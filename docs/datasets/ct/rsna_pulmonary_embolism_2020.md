# RSNA STR Pulmonary Embolism Detection 2020

## What it is
The 2020 RSNA-STR Pulmonary Embolism Detection corpus is the largest open CT pulmonary angiography (CTPA) dataset. It contains 9,446 CTPA examinations comprising 2,322,685 images (1,790,594 train across 7,279 exams + 532,091 test across 2,167 exams) from five international research centers across four continents.

Labels: exam-level PE label, slice-level PE label, plus nine PE subtype labels (right ventricular / left ventricular ratio, central PE, right-sided / left-sided, chronic PE, acute and chronic, indeterminate quality, etc.). Bounding-box augmentation was added later by independent groups.

## Why it matters for training
- Largest open CTPA corpus
- Multi-center, multi-vendor
- Multi-task labels (per-slice, per-exam, subtype) - rare for CT
- Foundation for deep learning PE detection benchmarks

Use for PE-specific finetuning and for chest CT pretraining where high-contrast vasculature is preserved.

## Access
Tier: registration. Kaggle: https://www.kaggle.com/competitions/rsna-str-pulmonary-embolism-detection . Mirror on AWS Open Data: `s3://rsna-pulmonary-embolism-detection/`. `aws s3 sync --no-sign-request s3://rsna-pulmonary-embolism-detection/ ./`.

## Conversion notes
DICOM. CTPA acquisitions are contrast-enhanced; pixel intensity in the pulmonary vasculature is much higher than non-contrast chest. Reassemble volumes by SOPInstanceUID + ImagePositionPatient. Slice thickness ~0.625-1.5 mm.

## License
RSNA Kaggle competition data license; research use only.

## Citation
Colak E et al. "The RSNA Pulmonary Embolism CT Dataset." Radiology: AI 3:e200254 (2021). DOI 10.1148/ryai.2021200254.

## Gotchas
- Size estimate ~120 GB - confirm via Kaggle CLI before starting a download.
- All scans are CTPA, so model bias toward contrast-enhanced thorax; don't assume generalization to non-contrast.
- Test labels embargoed.
