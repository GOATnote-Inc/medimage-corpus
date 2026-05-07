# AMOS 2022 (Abdominal Multi-Organ Segmentation)

## What it is
AMOS 2022 is a multi-modality abdominal segmentation benchmark from Sun Yat-sen University and collaborators. It contains 500 labeled CT scans + 100 labeled MRI scans (plus a planned 2,000 unlabeled CT and 1,200 unlabeled MRI for semi-supervised work) with voxel-level annotations for 15 abdominal organs across multi-center, multi-vendor, multi-phase, multi-disease patients.

The 15 organs: spleen, right kidney, left kidney, gallbladder, esophagus, liver, stomach, aorta, IVC, pancreas, right adrenal gland, left adrenal gland, duodenum, bladder, prostate/uterus.

The successor AMOS-MM (MICCAI 2024) extends with 2,000+ CT-report pairs and 19,562 visual-question-answer pairs for VLM training.

## Why it matters for training
- Cross-modal CT/MRI segmentation (rare for abdominal)
- Multi-vendor, multi-phase coverage
- 15-organ scope is a useful intermediate between BTCV (13) and AbdomenAtlas 1.1 (25)
- AMOS-MM extension provides paired text supervision (VLM-friendly)

## Access
Tier: open. Zenodo: https://zenodo.org/records/7262581 . CC BY 4.0. Direct download.

## Conversion notes
NIfTI volumes and masks. Standard nnU-Net plans available. CT and MRI are clearly tagged in the directory structure; do not mix unintentionally. Resample to 1.5x1.5x2 mm for joint CT/MRI training.

## License
CC BY 4.0.

## Citation
Ji Y et al. "AMOS: A Large-Scale Abdominal Multi-Organ Benchmark for Versatile Medical Image Segmentation." NeurIPS 2022 Datasets & Benchmarks. arXiv:2206.08023.

## Gotchas
- 24.2 GB is for labeled data only; full unlabeled extension is much larger.
- Prostate and uterus are merged into a single class; treat with care for sex-specific tasks.
- AMOS-MM (report extension) is a separate distribution channel via Codabench.
