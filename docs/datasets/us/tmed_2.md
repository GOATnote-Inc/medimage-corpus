# TMED-2 (Tufts Medical Echocardiogram Dataset, v2)

**Modality:** Ultrasound | **Anatomy:** Heart | **Views:** PLAX, PSAX, A2C, A4C, Other | **Year:** 2022

## Overview
TMED-2 is a semi-supervised learning benchmark from Tufts Medical Center: 599 echocardiography studies from 577 unique patients (some have multiple studies on different days). The labeled portion contains a mix of view-classification labels (PLAX/PSAX/A2C/A4C/Other) and study-level aortic-stenosis (AS) diagnostic labels (none / early / significant). About 40% of labeled images carry view labels, while all have an AS diagnostic label. The dataset is partitioned per-patient: 360 train / 119 val / 120 test.

## Labels
- View class (5 classes)
- AS severity (none / early / significant)
- Patient and study identifiers for proper held-out splits

## Format
Sampled PNG frames -- *not* full videos. ~350 MB estimated. Single-image classification benchmark.

## Access
Registration-gated -- request via the Tufts Data Access page (https://tmed.cs.tufts.edu/data_access.html). Non-commercial research only.

## Citation
Huang et al., "TMED 2: A Dataset for Semi-Supervised Classification of Echocardiograms." DataPerf @ NeurIPS 2022. arXiv:2306.00003.

## Notes for ingestion
- Single-frame, not video -- complements EchoNet-Dynamic for view-classification head training.
- Partial labels make this a real semi-supervised benchmark; good fit for foundation-model self-supervised pretraining followed by linear-probe view classification.
- AS-diagnosis label is study-level, so accuracy comparisons require multi-frame aggregation.
