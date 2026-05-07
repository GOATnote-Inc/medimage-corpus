# VinDr-PCXR (Pediatric Chest X-Ray)

VinDr-PCXR (Pham et al., 2022) is the first and largest open pediatric
chest X-ray dataset with both lesion-level bounding boxes and image-level
disease labels. It contains 9,125 PA-view DICOM scans of pediatric
patients younger than 10 years old, collected at a Vietnamese hospital.
The dataset is split into 7,728 training and 1,397 test scans.

Annotations cover:
- 36 critical findings with bounding-box localization (e.g. peri-bronchial
  thickening, bronchitis, perihilar fibrosis, mediastinal mass, foreign
  object, lung consolidation, pleural effusion, atelectasis, cardiomegaly,
  pneumothorax, etc.).
- 15 image-level disease labels (e.g. bronchitis, pneumonia, brocho-
  pneumonia, lung opacity, COVID-19, tuberculosis, etc.).

Adult CXR datasets (ChestX-ray14, MIMIC-CXR, PadChest) systematically
under-represent pediatric anatomy and disease patterns - chest size
ratio, mediastinal contour, and characteristic pediatric findings differ
markedly from adult imaging. VinDr-PCXR is therefore essential for
age-diverse pretraining and for safety evaluation of CXR models intended
for pediatric deployment.

Hosted on PhysioNet under the Restricted Health Data License 1.5.0; any
registered user can download after signing the DUA (no CITI training
required). Approximate full-DICOM size is ~30 GB.

DOI: https://doi.org/10.13026/k8qc-na36
