# MIMIC-CXR (DICOM v2.1.0)

**Year:** 2019 (initial) / 2024 (v2.1.0) | **Paper:** [Johnson et al. 2019 (Sci. Data)](https://doi.org/10.1038/s41597-019-0322-0)
**Access:** credentialed (PhysioNet) | **License:** PhysioNet Credentialed Health Data License 1.5.0

## Summary

MIMIC-CXR is the canonical large-scale public chest radiograph dataset paired with free-text radiology reports. Version 2.1.0 contains 377,110 chest X-ray images across 227,835 imaging studies from 65,379 unique patients seen at Beth Israel Deaconess Medical Center between 2011 and 2016. Each study has one corresponding free-text de-identified radiology report with sectioned content (Indication, Comparison, Findings, Impression, Technique). Images are distributed as DICOM in this version; MIMIC-CXR-JPG is the JPG-decoded sibling dataset.

## Image modality

Chest radiograph (XR), frontal (PA / AP) and lateral views, DICOM format with full preserved header metadata.

## Text type

Free-text de-identified radiology reports (sectioned). Pair with the MIMIC-CXR-JPG label files for 14-class CheXpert and NegBio structured labels.

## Size

~565 GB (DICOM, compressed). MIMIC-CXR-JPG (decoded JPEG) is ~4.6 TB.

## Access

PhysioNet credentialed: PhysioNet account, completion of CITI Data or Specimens Only Research training, and signed Data Use Agreement. No redistribution, no re-identification.

## Notes for VLM training

Indexed in the modality-specific manifest as `xr/mimic_cxr`; dedup target id: `xr/mimic_cxr`. MIMIC-CXR is the report-generation benchmark substrate (BLEU, ROUGE, CheXpert-F1, RadGraph-F1 metrics all reference MIMIC-CXR splits). Use MIMIC-CXR-JPG for training (faster I/O) and the DICOM source only when DICOM metadata is needed.
