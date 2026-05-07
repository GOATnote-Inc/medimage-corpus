# PadChest

**Year:** 2020 | **Paper:** [Bustos et al. 2020 (Medical Image Analysis)](https://doi.org/10.1016/j.media.2020.101797)
**Access:** application (BIMCV) | **License:** Custom research-only

## Summary

PadChest is one of the largest public chest radiograph datasets and the first in Spanish to include paired free-text radiologist reports. It comprises 168,861 chest X-ray images from 109,931 imaging studies of 67,000 unique patients seen at Hospital Universitario de San Juan, Alicante, Spain (2009-2017). Each study is paired with the original Spanish-language radiologist report and labels for 174 radiographic findings, 19 differential diagnoses, and 104 anatomical locations, organized as a hierarchical taxonomy mapped to UMLS CUIs. ~27% of reports are physician-reviewed; the remainder is auto-labeled with a recurrent neural network with attention (validated at 0.93 micro-F1).

## Image modality

Chest radiograph (XR), frontal (PA/AP) and lateral views, DICOM source distributed as 16-bit PNG by some mirrors.

## Text type

Free-text Spanish radiology reports + structured UMLS-mapped finding labels + diagnostic and anatomical-location taxonomies.

## Size

1.02 TB (full DICOM-equivalent distribution). 167 MB sample subset on Kaggle for prototyping.

## Access

Application-tier: free for researchers, formal access request via the BIMCV CIPF site, agreement to non-redistribution and non-re-identification clauses.

## Notes for VLM training

Indexed in the modality-specific manifest as `xr/padchest`; dedup target id: `xr/padchest`. PadChest is the canonical Spanish-language CXR corpus and the upstream source for PadChest-GR (4,555 grounded bilingual studies) and BIMCV-COVID19+. Critical for non-English VLM training and for Spanish/English cross-lingual generalization studies.
