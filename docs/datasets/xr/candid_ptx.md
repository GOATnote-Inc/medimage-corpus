# CANDID-PTX (Pneumothorax)

CANDID-PTX (Feng et al., 2021; expanded curation by Tam et al. with
free-text reports, Radiology: Artificial Intelligence 2021) is a
pneumothorax-focused chest-radiograph dataset with paired free-text
reports. It contains 19,237 anonymized adult chest X-rays in 1024x1024
DICOM format, drawn from 295,613 raw images imported from Dunedin
Hospital's PACS in New Zealand between 2010 and 2020. After exclusion
filtering by tier-3 radiologist annotators (RANZCR trainees and
consultants), the curated set comprises 3,196 pneumothorax cases plus
the remainder as no-pneumothorax controls.

Annotations:
- Pneumothorax segmentation masks (RLE-encoded in CSV).
- Acute rib-fracture labels.
- Chest-tube presence labels.
- Free-text radiology reports paired image-by-image - this is the
  VLM-relevant feature.

Demographics: ages 16-101 (mean 60.1), 53.4% male.

CANDID-PTX is one of the few open paired-report CXR datasets outside
the MIMIC-CXR / PadChest / CheXpert-Plus axis, and it provides
dense pixel-level pneumothorax supervision that pairs naturally with
SIIM-ACR Pneumothorax Segmentation for combined PTX-task training.

Distribution is via Figshare (University of Auckland) under an
ethics-restricted research-use agreement; Auckland's terms require
local ethics approval before download.

Paper: Feng et al., Radiology: AI 2021. DOI:
https://doi.org/10.1148/ryai.2021210136
