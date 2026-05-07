# BrEaST (Breast Lesions USG, TCIA)

**Modality:** Ultrasound | **Anatomy:** Breast | **Year:** 2024

## Overview
BrEaST is a curated benchmark dataset hosted on The Cancer Imaging Archive (TCIA) for breast ultrasound lesion analysis. 256 breast ultrasound scans from 256 patients with 266 segmented benign and malignant lesions. Each scan includes manual radiologist annotations, BI-RADS classifications, and histopathological diagnoses confirmed through follow-up care or biopsy. Source is a single Polish institution.

## Labels
- Lesion mask (radiologist-drawn)
- BI-RADS category
- Histopathology outcome

## Format
PNG images + segmentation masks (66.63 MB ZIP) plus a 39.23 KB clinical XLSX.

## Access
Open at TCIA https://www.cancerimagingarchive.net/collection/breast-lesions-usg/. CC-BY-4.0.

## Citation
Pawlowska et al., "A curated benchmark dataset for ultrasound based breast lesion analysis." *Scientific Data* 11, 148 (2024). DOI: 10.1038/s41597-024-02984-z. Dataset DOI: 10.7937/9WKK-Q141.

## Notes for ingestion
- Smaller than BUSI/BUS-BRA but TCIA-hosted = stable persistent identifiers.
- CC-BY-4.0 permits commercial use with attribution.
- Histopathology-confirmed labels make this a high-quality evaluation set; pair with BUSI / BUS-BRA for training.
