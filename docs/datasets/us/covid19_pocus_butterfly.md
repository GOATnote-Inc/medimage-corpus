# POCOVID (Born et al. POCUS COVID-19 Initiative)

**Modality:** Ultrasound | **Anatomy:** Lung | **View:** Point-of-care lung ultrasound | **Year:** 2021

## Overview
The Born et al. POCOVID-Net initiative (jannisborn/covid19_ultrasound) was the first open-access lung ultrasound (LUS) dataset to scale during the pandemic. 261 lung ultrasound recordings (202 videos + 59 still images) collected from 216 patients. Class breakdown: 92 COVID-19, 90 healthy controls, 73 bacterial pneumonia, 6 viral pneumonia. A subset of 45 COVID-19 videos was acquired in Piacenza, Italy at the peak of the European outbreak. Severity labels exist for 136 of the videos.

## Labels
- 4-class: COVID / healthy / bacterial pneumonia / viral pneumonia
- Severity score (subset)

## Format
Mixed MP4 / GIF / PNG sources at native resolution. ~180 MB estimated.

## Access
Open repository at https://github.com/jannisborn/covid19_ultrasound. License is MIT for code; the data folder holds clips contributed under heterogeneous licenses (some not redistributable -- the repo provides `get_and_process_web_data.sh` to download from upstream sources).

## Citation
Born et al., "Accelerating Detection of Lung Pathologies with Explainable Ultrasound Image Analysis." *Applied Sciences* 11(2):672 (2021). DOI: 10.3390/app11020672

## Notes for ingestion
- Much of the data is sourced from grepmed and the Italian ultrasound atlas -- cite contributors carefully.
- Always split on video / patient level, never frame level (README emphasizes this; frame-level splits trivialize the task).
- Pair with COVIDx-US and COVID-BLUES for a complete LUS pretraining cohort.
