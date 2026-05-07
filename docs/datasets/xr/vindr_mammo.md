# VinDr-Mammo

VinDr-Mammo (Vingroup Big Data Institute, 2022) is a large-scale benchmark
mammography dataset. It contains 5,000 four-view mammographic exams (20,000
DICOM images: bilateral CC + MLO) collected from two Vietnamese hospitals.
Each exam is double-read by experienced radiologists, with discordances
resolved through arbitration - a more rigorous labelling protocol than most
open mammography corpora.

Annotations include:
- BI-RADS assessment categories (1-5) at the breast and lesion level.
- Breast density category (A-D).
- Bounding boxes for masses, calcifications, asymmetries, architectural
  distortion, and associated features.
- Train/test split: 4,000 training exams + 1,000 test exams, stratified.

VinDr-Mammo is the leading open detection-grade mammography dataset.
Combined with EMBED (large-scale, fairness-balanced), CBIS-DDSM (open
license, pathology-confirmed), and INbreast (high-quality reference), it
provides full coverage of the mammography task spectrum: classification,
detection, density, and BI-RADS.

The data is hosted on PhysioNet under the Restricted Health Data License
1.5.0 - a softer access tier than full Credentialed: any registered user
can download after signing the DUA, no CITI training required.
Approximate full-DICOM size is ~350 GB.

DOI: https://doi.org/10.13026/br2v-7517
