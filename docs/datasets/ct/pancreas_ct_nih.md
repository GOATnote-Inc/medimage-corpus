# Pancreas-CT (NIH)

## What it is
NIH Pancreas-CT is a foundational pancreas segmentation dataset on TCIA. It contains 82 abdominal contrast-enhanced 3D CT scans (acquired ~70 seconds after IV contrast in portal-venous phase) from 80 subjects (53 male, 27 female; ages 18-76). 17 of the subjects are healthy kidney donors; the remaining 65 were selected to lack major abdominal pathology or pancreatic cancer. 9.95 GB total. Manual pancreas segmentations are radiologist-verified.

## Why it matters for training
- Reference baseline for pancreas segmentation
- Cited in essentially every pancreas-segmentation paper since 2016
- Compact, simple to ingest, useful for sanity-checking pipelines
- Often combined with Medical Decathlon Pancreas for stronger supervision

Use as a fine-tuning or evaluation set, not a primary training source (too small).

## Access
Tier: open. https://www.cancerimagingarchive.net/collection/pancreas-ct/ . Pull via NBIA Data Retriever or `tcia-cli`.

## Conversion notes
DICOM with NIfTI mask supplements. Convert to NIfTI with dcm2niix. Voxel spacing typically 0.66-0.98 mm in-plane / 0.5-1.0 mm through-plane. Resample to 1mm isotropic for nnU-Net.

## License
CC BY 3.0.

## Citation
Roth HR et al. "Data From Pancreas-CT" [data set]. The Cancer Imaging Archive (2016). Original methodology paper: Roth HR et al. "DeepOrgan: Multi-level Deep Convolutional Networks for Automated Pancreas Segmentation." MICCAI 2015. DOI 10.1007/978-3-319-24553-9_68.

## Gotchas
- Only 80 subjects; do not benchmark generalization claims on this alone.
- Healthy / mostly healthy cohort; will not test pathology-handling.
- Single institution.
