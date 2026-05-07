# COVID-BLUES Lung Ultrasound

**Modality:** Ultrasound | **Anatomy:** Lung | **View:** Six BLUE-protocol points | **Year:** 2025

## Overview
COVID-BLUES is a Wiedemann/IBM Research et al. prospective study (2021 enrollment, 2025 publication) of 63 patients (33 COVID-positive, 30 COVID-negative) presenting with lung-infection symptoms. 371 lung ultrasound videos (some patients have fewer than six because not every BLUE point was scannable), totaling 31,746 frames. All videos acquired on a single device (Philips Lumify with convex probe) per a standardized BLUE-point protocol -- making this the most internally consistent open LUS dataset.

## Labels
- COVID status (positive/negative)
- Severity assessment by medical experts
- BLUE-point label per video (one of six anatomical points)
- Per-patient clinical variables

## Format
MP4 video files in `lus_videos/` folder, 60-100 frames each. ~1.3 GB estimated.

## Access
Open at GitHub https://github.com/NinaWie/COVID-BLUES, mirrored on Hugging Face Hub. Licensed CC-BY-NC-ND 4.0.

## Citation
Wiedemann et al., "Bluepoint-specific lung ultrasound videos for AI-based diagnostic support." *Scientific Data* (2025).

## Notes for ingestion
- CC-BY-NC-ND prohibits redistribution of derivative works -- do not re-host fine-tuned model checkpoints publicly without re-checking the terms.
- Strong dataset for prospective-validation experiments because of the standardized BLUE-point acquisition.
- Pair with POCOVID + COVIDx-US for domain-randomized LUS pretraining.
