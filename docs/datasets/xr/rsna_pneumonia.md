# RSNA Pneumonia Detection Challenge (2018)

The RSNA Pneumonia Detection Challenge (Kaggle 2018) is a chest-radiograph
dataset for pneumonia detection and bounding-box localization. It contains
30,227 1024x1024 DICOM-format chest X-rays drawn as a subset of the NIH
ChestX-ray14 archive, with bounding-box annotations re-curated by the
Radiological Society of North America in collaboration with the Society
for Thoracic Radiology.

Annotations include:
- Pneumonia label (positive / negative).
- Bounding boxes localizing pneumonia opacities.
- A "not normal but no pneumonia" class for the abnormal-but-not-pneumonia
  case (clinically important to disambiguate from pneumonia).

This is the standard open benchmark for pneumonia object detection on
chest X-rays. RSNA Pneumonia, SIIM-ACR Pneumothorax, and RANZCR CLiP
together cover the three highest-priority CXR detection tasks (pneumonia,
pneumothorax, line/tube position) at challenge-grade annotation quality.

Distribution is via Kaggle competitions (`download_method: kaggle`) under
standard RSNA AI Challenge research-use license. Approximate raw DICOM
size is ~12 GB. Stage 1 training images, Stage 2 test images, and
labels CSV are released; ground-truth labels for Stage 2 test images
remain held back.

Reference: 2018 RSNA Pneumonia Detection Challenge.
https://www.rsna.org/rsnai/ai-image-challenge/rsna-pneumonia-detection-challenge-2018
