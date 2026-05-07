# BIMCV-COVID19+

**Year:** 2020 (initial release; multiple iterations through 2022) | **Paper:** [arXiv:2006.01174](https://arxiv.org/abs/2006.01174)
**Access:** application (BIMCV) | **License:** Custom research-only

## Summary

BIMCV-COVID19+ is the Valencia Region Image Bank's COVID-19-specific imaging corpus, combining chest X-ray and chest CT data with paired Spanish-language radiologist reports, COVID-19 diagnostic test results (PCR, IgG, IgM antibody), and clinical metadata. The initial-iteration release contains 21,342 CR (Computed Radiography), 34,829 DX (Digital Radiography), and 7,918 CT studies from 1,311 confirmed COVID-19 patients; later iterations expanded these counts. Findings are mapped to UMLS CUIs (sharing taxonomy with PadChest).

## Image modalities

Chest X-ray (CR + DX) and chest CT (DICOM).

## Text type

Anonymized Spanish-language radiology reports paired per study, plus structured COVID-19 diagnostic test results and pathology annotations mapped to UMLS.

## Size

~700 GB (full multi-iteration distribution; sizes vary across iterations).

## Access

Application-tier: free for non-commercial research, formal request via BIMCV. Repository code is MIT-licensed; per-image data carries the BIMCV custom DUA. Do not redistribute.

## Notes for VLM training

Distinct from PadChest: PadChest is general CXR (no COVID), BIMCV-COVID19+ is COVID-specific with multimodal (XR + CT) coverage and lab results. Useful for COVID-era distribution-shift studies and for multimodal report-generation models. Dedup target ids: `xr/bimcv_covid` and `ct/bimcv_covid` if those exist in the modality-specific manifests.
