# ROCOv2 (Radiology Objects in COntext v2)

**Year:** 2024 | **Paper:** [arXiv:2405.10004](https://arxiv.org/abs/2405.10004) | **DOI:** 10.57967/hf/3489
**Access:** open | **License:** CC-BY-NC-SA-4.0

## Summary

ROCOv2 is the second-generation Radiology Objects in COntext dataset of 79,789 PMC-derived radiology figures with associated captions and UMLS Concept Unique Identifier annotations. Splits: 59,958 train, 9,904 validation, 9,927 test. Each image carries one or more UMLS CUIs (1,947 unique CUIs total) extracted via the Medical Concept Annotation Toolkit (MedCAT) v1.10.0. ROCOv2 is widely used for biomedical CLIP pretraining and concept-based image classification.

## Image modalities

Radiology only (filtered from PMC OA): CT, MRI, X-ray, ultrasound, fluoroscopy, PET, echocardiography, and other radiology modalities.

## Text type

Image captions plus UMLS CUI labels (multi-label per image).

## Size

18.6 GB.

## Access

Open download from Hugging Face under CC-BY-NC-SA-4.0 (non-commercial, share-alike). Source articles are PMC OA (CC-BY or CC-BY-NC).

## Notes for VLM training

Direct successor to ROCO 2018; substantially cleaner radiology filter. Overlaps with PMC-OA, MedICaT, and BIOMEDICA (all PMC-derived). Dedup by `pmc_id + figure_id`. Can be paired with MedCLIP/PMC-CLIP/BiomedCLIP-style training pipelines; the UMLS CUI labels are useful auxiliary supervision for concept-conditioned generation. Use train+val for VLM pretraining; reserve test for cross-paper retrieval evaluation.
