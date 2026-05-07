# COVIDx-US Lung Ultrasound Benchmark

**Modality:** Ultrasound | **Anatomy:** Lung | **Views:** B-line / A-line / artifact patterns | **Year:** 2022

## Overview
COVIDx-US (NRC Canada) is the most curated open-access lung ultrasound (LUS) benchmark for COVID-19 and other lung pathology. Version 1.5 contains 242 ultrasound videos and 29,651 processed frames from 147 patients across COVID-19, non-COVID infection, other lung conditions, and normal controls.

## Labels
- COVID / non-COVID / other / normal video class
- Standardized LUS severity score per video
- Artifact-class labels (A-lines, B-lines, consolidation)
- Per-patient demographics + symptom metadata

## Format
Mixed MP4 / AVI source files at original resolutions; recommend re-encoding to MP4 + extracting frames into parquet for training. ~2.5 GB total.

## Access
Open at https://github.com/nrc-cnrc/COVID-US -- AGPL-3.0 license. Note: source data has a mix of CC-BY-NC variants on individual contributing clips.

## Citation
Ebadi et al., "COVIDx-US: An Open-Access Benchmark Dataset of Ultrasound Imaging Data for AI-Driven COVID-19 Analytics." *Frontiers in Bioscience-Landmark* 27(7):198 (2022). DOI: 10.31083/j.fbl2707198

## Notes for ingestion
- AGPL-3.0 means viral copyleft for distributed derived works -- consult counsel if shipping commercial weights.
- Heterogeneous source devices (curvilinear + linear probes, mixed POCUS vendors). Strong domain-randomization signal.
- Pair with POCOVID and COVID-BLUES to assemble a ~3-source LUS pretraining cohort.
