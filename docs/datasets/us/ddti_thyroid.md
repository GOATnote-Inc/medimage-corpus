# DDTI (Digital Database of Thyroid Ultrasound Images)

**Modality:** Ultrasound | **Anatomy:** Thyroid | **Year:** 2015

## Overview
DDTI is one of the earliest open-access thyroid ultrasound datasets, released by the CIMA Lab at Universidad Nacional de Colombia using imaging from IDIME (one of Colombia's largest diagnostic imaging centers). 480 ultrasound images from 290 patients. Each image is annotated by a radiology resident and includes diverse pathology: thyroiditis, goiter, nodules, and cancer. TIRADS scoring and biopsy outcomes are also captured for many cases.

## Labels
- Nodule mask / annotation
- TIRADS score
- Biopsy result (subset)

## Format
JPG images + XML annotations (native). Pre-parsed Kaggle mirror provides JPG+PNG mask format directly. ~25 MB estimated.

## Access
Open. Original at https://cimalab.unal.edu.co/?lang=en&mod=project&id=31. Kaggle mirror at https://www.kaggle.com/datasets/dasmehdixtr/ddti-thyroid-ultrasound-images is the more usable download path.

## Citation
Pedraza et al., "An open access thyroid ultrasound-image database." Tenth International Symposium on Medical Information Processing and Analysis. SPIE Vol. 9287 (2015). DOI: 10.1117/12.2073532

## Notes for ingestion
- Diagnostic diversity (goiter / thyroiditis / cancer) is the strength here; complements TN3K's tighter nodule-only curation.
- Colombian population pairs with TN3K (Chinese) for cross-domain robustness experiments.
- XML annotations are awkward -- prefer the Kaggle pre-parsed mirror.
