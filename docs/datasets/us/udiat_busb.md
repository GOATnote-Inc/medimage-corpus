# UDIAT Dataset B (Sabadell Breast Ultrasound)

**Modality:** Ultrasound | **Anatomy:** Breast | **Year:** 2018

## Overview
The UDIAT Dataset B (sometimes called "Breast Ultrasound Dataset B" or "Yap dataset B") was collected at the UDIAT Diagnostic Centre of Parc Tauli Corporation, Sabadell, Spain on a Siemens ACUSON XP10 scanner. 163 breast ultrasound images: 109 benign + 54 malignant cases, with one lesion per image. Lesion masks provided. Released with Yap et al.'s 2018 IEEE JBHI paper on automated breast lesion detection.

## Labels
- Lesion mask (in `GT/` folder)
- Binary class (benign / malignant)

## Format
PNG. ~30 MB estimated.

## Access
Application via http://www2.docm.mmu.ac.uk/STAFF/m.yap/dataset.php (Manchester Metropolitan University, Prof. Moi Hoon Yap). Research use only.

## Citation
Yap et al., "Automated Breast Ultrasound Lesions Detection Using Convolutional Neural Networks." *IEEE Journal of Biomedical and Health Informatics* (2018). DOI: 10.1109/JBHI.2017.2731873

## Notes for ingestion
- Small but historically important -- frequently cited in BUS lesion papers.
- Useful as cross-domain test against BUSI (Cairo) and BUS-BRA (Brazil); single Spanish device covers a different acquisition regime.
- Application is per-request and may take days; plan early.
