# CT-RATE

**Year:** 2024 | **Paper:** [arXiv:2403.17834](https://arxiv.org/abs/2403.17834)
**Access:** credentialed (Hugging Face access form) | **License:** CC-BY-NC-SA-4.0

## Summary

CT-RATE is the first public large-scale dataset pairing 3D non-contrast chest CT volumes with full free-text radiology reports. It comprises 25,692 unique chest CT volumes (50,188 reconstructed series) from 21,304 patients, each paired with a Findings/Impressions report and 18 multi-abnormality binary labels. CT-RATE underpins the CT-CLIP and CT-CHAT foundation models; it is the canonical "MIMIC-CXR for chest CT" and the de-facto pretraining anchor for any chest-CT VLM.

## Image modality

Volumetric chest CT (NIfTI, axial). Resolution and slice thickness vary across the cohort.

## Text type

Free-text radiology reports (Findings + Impression sections) plus 18 binary multi-abnormality labels and structured metadata. Reports are de-identified and English-language. RadGenome-ChestCT augments these with grounded sentence-level reports anchored to organ segmentation masks.

## Size

21.3 TB total (NIfTI + reports + metadata). Train: 20,000 patients; validation: 1,304 patients.

## Access

Hugging Face dataset page requires (1) HF account, (2) accepting the data use agreement (no commercial use, no redistribution, no re-identification, citation required). License is CC-BY-NC-SA-4.0 - non-commercial only.

## Notes for VLM training

Also indexed in `ct/ct_rate.jsonl`; dedup target id: `ct/ct_rate`. Pair with RadGenome-ChestCT (same patient cohort) for grounded report supervision and with INSPECT (CTPA + EHR) for cross-cohort diversity. Use NIfTI volume loaders that preserve HU intensities; do not convert to 8-bit before model input.
