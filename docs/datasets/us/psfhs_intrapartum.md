# PSFHS (Pubic Symphysis-Fetal Head Segmentation)

**Modality:** Ultrasound | **Anatomy:** Maternal pelvis + fetal head | **View:** Transperineal mid-sagittal | **Year:** 2024

## Overview
PSFHS is the dataset behind the MICCAI 2023 Pubic Symphysis-Fetal Head Segmentation Grand Challenge. 4,000 intrapartum transperineal ultrasound images annotated at the pixel level for two structures (pubic symphysis and fetal head) -- enabling automated assessment of angle of progression and fetal head descent during labor. Combines original PSFHS data with the JNU-IFM contribution.

## Labels
- Pubic symphysis segmentation mask
- Fetal head segmentation mask
- Both at 256x256 resolution

## Format
MHA files. 363 MB total download. Recommend converting to PNG + parquet for training.

## Access
Open at Zenodo https://zenodo.org/records/10969427 (CC-BY-4.0). Challenge platform at https://ps-fh-aop-2023.grand-challenge.org/. Test set is held private.

## Citation
Lu et al., "PSFHS: Intrapartum ultrasound image dataset for AI-based segmentation of pubic symphysis and fetal head." *Scientific Data* 11, 402 (2024). DOI: 10.1038/s41597-024-03266-4

## Notes for ingestion
- Complementary to HC18 (which is antepartum, fetal head only): PSFHS is intrapartum + maternal pelvis.
- Two-class semantic segmentation; useful as a moderate-difficulty pretraining task.
- 256x256 fixed resolution makes this trivially compatible with vanilla SAM-style decoders.
