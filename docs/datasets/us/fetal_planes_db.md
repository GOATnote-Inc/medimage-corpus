# FETAL_PLANES_DB (Burgos-Artizzu)

**Modality:** Ultrasound | **Anatomy:** Fetus (multi-plane) | **Year:** 2020

## Overview
A large still-image obstetric ultrasound classification dataset published in *Scientific Reports* (2020). Approximately 12,400 routinely acquired maternal-fetal screening ultrasound images from two Spanish hospitals, multiple operators, and several ultrasound machines. Images cover four standard anatomical planes (Abdomen, Brain, Femur, Thorax), the maternal cervix, plus an "Other" class. The Brain class is sub-divided into trans-thalamic, trans-cerebellum, and trans-ventricular sub-planes.

## Labels
- Plane class (6 main classes)
- Brain plane sub-class (3)
- Patient identifier, ultrasound machine, operator metadata

## Format
PNG still images. ~2.1 GB compressed.

## Access
Open at https://zenodo.org/records/3904280 (CC-BY-4.0).

## Citation
Burgos-Artizzu et al., "Evaluation of deep convolutional neural networks for automatic classification of common maternal fetal ultrasound planes." *Scientific Reports* 10, 10200 (2020). DOI: 10.1038/s41598-020-67076-5

## Notes for ingestion
- Stills only -- no temporal information. Pair with ACOUSLIC-AI sweeps if you need motion priors.
- Operator and machine IDs are present, enabling evaluation of operator/device shift.
- CC-BY makes this safe for commercial pretraining as long as attribution is preserved.
