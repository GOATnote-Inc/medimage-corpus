# RANZCR CLiP - Catheter and Line Position Challenge

The RANZCR (Royal Australian and New Zealand College of Radiologists)
CLiP - Catheter and Line Position Challenge dataset (Kaggle 2021) is a
chest-radiograph dataset specifically focused on the correct positioning
of medical devices in intensive-care settings. It contains 30,083 chest
X-ray images with 50,612 image-level binary labels and 17,999 manually
labeled annotations, drawn from a Australia/NZ CXR archive plus a subset
of the publicly available NIH ChestX-ray14 corpus.

The dataset annotates three device classes, each with three positional
sub-labels (correct / borderline-abnormal / abnormal):
- ETT (endotracheal tube)
- NGT (nasogastric / nasoenteric tube)
- CVC (central venous catheter)

This is the canonical open dataset for ICU-focused safety evaluation:
incorrectly positioned ETTs and NGTs can cause aspiration, pneumothorax,
or carotid puncture, so accurate device-position classifiers are a
high-value clinical-safety target. RANZCR CLiP is therefore essential
for any chest-VLM intended for inpatient or critical-care deployment.

Distribution is via Kaggle competitions (`download_method: kaggle`)
under standard Kaggle competition rules (research use; no
redistribution). Approximate JPG-format size is ~13 GB. TFRecords are
also provided for direct TensorFlow ingestion.

Reference: Tang et al., Scientific Data 2021. DOI:
https://doi.org/10.1038/s41597-021-01066-8
