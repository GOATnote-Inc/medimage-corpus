# MIMIC-CXR-JPG v2.1.0

**Year:** 2019 (data) / 2024 (v2.1.0) | **Paper:** [arXiv:1901.07042](https://arxiv.org/abs/1901.07042)
**Access:** credentialed (PhysioNet) | **License:** PhysioNet Credentialed Health Data License 1.5.0

## Summary

MIMIC-CXR-JPG is the JPEG-decoded distribution of the MIMIC-CXR chest radiograph corpus, derived from 377,110 frontal/lateral chest radiographs across 227,835 imaging studies of 65,379 unique patients seen at Beth Israel Deaconess Medical Center (2011-2016). Every study is paired with a free-text de-identified radiology report (Findings, Impression, Indication, Comparison, Technique sections) and structured CheXpert and NegBio labels for 14 thoracic findings. JPG distribution is preferred over the DICOM source for fast iteration during pretraining of CXR VLMs.

## Image modality

Chest radiograph (XR), frontal (PA / AP) and lateral views, in JPEG format with preprocessed pixel intensity.

## Text type

Free-text de-identified radiology reports (sectioned), plus 14-class CheXpert binary labels and NegBio uncertainty labels. Reports cover ~227K studies (multiple images per study).

## Size

~4.6 TB JPG distribution. Larger than the DICOM source because JPGs are decoded from compressed DICOM into 8-bit pixel arrays.

## Access

PhysioNet credentialed access: requires a PhysioNet account, completion of CITI Data or Specimens Only Research training, and signing the data use agreement. No redistribution, no re-identification.

## Notes for VLM training

Dedup target id: `xr/mimic_cxr` (this entry is also indexed there). MIMIC-CXR-JPG is the most common training corpus for CXR report-generation models (R2Gen, CXR-RePaiR, RadFM, RaDialog, CXR-LLaVA). Pair with CheXpert Plus to expand label diversity; combine with PadChest for Spanish-language report training.
