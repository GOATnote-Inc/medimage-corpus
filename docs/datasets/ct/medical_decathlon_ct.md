# Medical Segmentation Decathlon (CT tasks)

## What it is
The Medical Segmentation Decathlon (MSD) is a 10-task biomedical image segmentation benchmark. The CT-only tasks are: Spleen (61 volumes), Liver (201), Pancreas (420), Lung (96), Colon (190), Hepatic Vessel (443). Approximately 1,300 NIfTIs total. Tasks designed to test whether a method that performs well on multiple tasks will generalize to an unseen task.

## Why it matters for training
- The single most-cited multi-task CT segmentation benchmark
- nnU-Net's standard test bench
- Heterogeneous task scope (organs + tumors + vessels) tests architecture generality
- Cross-task transfer learning experiments

Use as a benchmark suite, as a multi-task supervision signal, or as a calibration dataset for new model evaluations.

## Access
Tier: open. AWS Open Data Registry: `s3://msd-for-monai/` (us-west-2) and `s3://msd-for-monai-eu/` (eu-west-2). No-auth: `aws s3 sync --no-sign-request s3://msd-for-monai/ ./`. Original portal http://medicaldecathlon.com/ has TLS certificate issues; prefer S3.

## Conversion notes
NIfTI in `imagesTr/`, `labelsTr/`, `imagesTs/` per task. Standard nnU-Net training works out of the box. Total CT-task footprint is small enough (~13 GB) to keep on local SSD.

## License
CC BY-SA 4.0.

## Citation
Antonelli M et al. "The Medical Segmentation Decathlon." Nature Communications 13:4128 (2022). DOI 10.1038/s41467-022-30695-9.

## Gotchas
- Total includes 4 non-CT tasks (Brain, Heart, Hippocampus, Prostate); filter to CT only for this scope.
- Pancreas task is intentionally hard due to small foreground; do not benchmark with naive Dice.
- TLS error on the medicaldecathlon.com domain has been intermittent for years; AWS mirror is reliable.
