# CheXpert Plus

**Year:** 2024 | **Paper:** [Stanford Redivis DOI 10.71718/6nvz-pm34](https://doi.org/10.71718/6nvz-pm34)
**Access:** registration (Stanford AIMI) | **License:** Stanford AIMI Research Use Agreement

## Summary

CheXpert Plus extends the original CheXpert chest radiograph dataset with paired de-identified radiology reports. It comprises 223,462 unique image-report pairs across 187,711 studies from 64,725 unique patients. Each report is split into 11 subsections (Findings, Impression, Indication, Technique, Comparison, History, Procedure, Recommendation, Review, Wet Read, and additional clinical context fields) totaling approximately 36 million text tokens. Images are distributed in DICOM format with up to 47 metadata fields, and each pair is augmented with 8 de-identified patient demographic covariates (age, sex, race, ethnicity, insurance, BMI, deceased status, interpreter needed).

## Image modality

Chest radiograph (XR), DICOM, frontal and lateral views with retained metadata.

## Text type

Free-text radiology reports sectioned into 11 subsections, plus 14-class CheXpert structured labels and 8 demographic covariates.

## Size

~503 GB (DICOM + report archive).

## Access

Stanford AIMI Research Use Agreement, registration-tier (no PI application required, but data use agreement and Stanford Redivis project signup mandatory). Non-commercial research only.

## Notes for VLM training

Dedup target id: `xr/chexpert` (this entry is the report-paired version; CheXpert-only label dataset is the source of dedup). Significantly more diverse demographics than MIMIC-CXR (Stanford patient base vs. Beth Israel Boston). Combine with MIMIC-CXR-JPG to maximize report diversity for English-language CXR VLM training. Demographic covariates make this useful for fairness/bias-aware model evaluation.
