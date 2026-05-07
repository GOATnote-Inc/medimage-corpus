# EchoNet-Dynamic

**Modality:** Ultrasound | **Anatomy:** Heart (LV) | **View:** Apical-4-chamber (A4C) | **Year:** 2020

## Overview
EchoNet-Dynamic is the de facto benchmark for video-based deep learning in echocardiography. 10,030 single-cycle A4C videos from Stanford Hospital, each annotated with end-systolic / end-diastolic LV tracings and clinically reported ejection fraction. Published in Nature 2020. Standardized 112x112 pixel AVI -- meaning downstream code can ingest at FP16 video tensors directly without resampling.

## Labels
- Ejection fraction (EF, %)
- End-systolic volume (ESV, mL)
- End-diastolic volume (EDV, mL)
- Endocardial border tracings at ES and ED frames
- Per-cycle keyframe indices

## Format
AVI, ~150 frames/video, 112x112 grayscale. Approximately 7.5 GB total. Trivial to convert to MP4 + frame parquet for fast loaders.

## Access
Stanford AIMI portal (https://aimi.stanford.edu/datasets/echonet-dynamic-cardiac-ultrasound). Registration + signed Research Use Agreement. Non-commercial only.

## Citation
Ouyang et al., "Video-based AI for beat-to-beat assessment of cardiac function." *Nature* 580, 252-256 (2020). DOI: 10.1038/s41586-020-2145-8

## Notes for ingestion
- Use as primary echo-video pretraining substrate; results transfer to EchoNet-Pediatric and external datasets.
- Already de-identified at Stanford -- no PHI scrub needed.
- For VLM training, pair with cardiology report text from MIMIC-IV-Echo or synthetic text from EF / ESV / EDV templating.
