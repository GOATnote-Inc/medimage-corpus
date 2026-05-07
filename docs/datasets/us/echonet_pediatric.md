# EchoNet-Pediatric

**Modality:** Ultrasound | **Anatomy:** Heart (LV) | **Views:** A4C + PSAX | **Year:** 2022

## Overview
EchoNet-Pediatric extends the Stanford EchoNet family to pediatric patients (ages 0-18, 43% female). 7,643 echocardiogram videos: 3,176 apical-4-chamber and 4,424 parasternal short-axis. Data collection 2014-2021 at Lucile Packard Children's Hospital. Clinically reviewed EF, ESV, EDV, plus endocardial tracings.

## Labels
- Ejection fraction (EF)
- ESV / EDV
- End-systole + end-diastole tracings
- Patient demographics (age, sex)

## Format
112x112 standardized AVI (matches EchoNet-Dynamic shape). ~6 GB total estimated. Two view classes -- A4C and PSAX -- enable multi-view consistency / contrastive objectives.

## Access
Stanford AIMI portal. Registration + signed Research Use Agreement. Non-commercial only. Sharing of download links explicitly prohibited.

## Citation
Reddy et al., "Video-based deep learning for automated assessment of left ventricular ejection fraction in pediatric patients." *Journal of the American Society of Echocardiography* (2022). DOI: 10.1016/j.echo.2022.10.014

## Notes for ingestion
- Pediatric domain shift from adult Dynamic / LVH datasets: hearts are smaller, framerates and cycle lengths differ.
- Excellent for testing generalization of a video encoder pretrained on adult data.
- Ages 0-18 means significant intra-cohort heterogeneity -- consider stratifying eval by age band.
