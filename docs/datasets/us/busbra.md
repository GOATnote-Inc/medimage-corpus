# BUS-BRA (Brazilian Breast Ultrasound)

**Modality:** Ultrasound | **Anatomy:** Breast | **Year:** 2024

## Overview
BUS-BRA is a 2024 Brazilian breast ultrasound dataset that improves on BUSI in size, license permissiveness, and label depth. 1,875 anonymized breast ultrasound images from 1,064 patients, paired with ground-truth lesion delineations and BI-RADS categories 2-5. All non-normal cases have biopsy-proven labels.

## Labels
- Tumor / normal segmentation mask
- BI-RADS category (2, 3, 4, 5)
- Biopsy outcome

## Format
PNG images + masks. ~134 MB compressed download.

## Access
Open at Zenodo https://zenodo.org/records/8231412 under CC-BY-4.0.

## Citation
Gomez-Flores et al., "BUS-BRA: A breast ultrasound dataset for assessing computer-aided diagnosis systems." *Medical Physics* (2024). DOI: 10.1002/mp.16812

## Notes for ingestion
- More permissive than BUSI (CC-BY vs ODbL) -- preferred substrate for any commercial-friendly breast US pretraining.
- BI-RADS-graded labels enable richer multi-class evaluation than BUSI's 3-class.
- South-American population complements BUSI (Egypt) and UDIAT/BUS-UCLM (Spain) for multi-site experiments.
