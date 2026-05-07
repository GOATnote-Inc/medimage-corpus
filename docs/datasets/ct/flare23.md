# FLARE 2023: Pan-cancer Abdominal CT

## What it is
The MICCAI FLARE 2023 challenge corpus is the largest abdominal CT segmentation benchmark assembled to date. It contains approximately 4,650 CT scans from over 40 medical centers, spanning all CT phases (plain, arterial, portal, delay) and all four major scanner vendors (GE, Philips, Siemens, Toshiba).

Labels: 13 abdominal organ segmentations (liver, spleen, pancreas, kidneys, stomach, gallbladder, esophagus, aorta, IVC, adrenals, duodenum) plus a single pan-cancer lesion class covering nine cancer types. Approximately 2,200 partially labeled volumes, 5,500 unlabeled (semi-supervised setting), and held-out test cases.

The dataset is 23 times larger than LiTS and substantially exceeds prior abdominal-tumor benchmarks.

## Why it matters for training
- Largest multi-center abdominal CT benchmark
- Pan-cancer scope (one tumor class spanning many cancer types)
- Designed for semi-supervised regimes (lots of unlabeled volumes)
- Best-in-class diversity for organ + tumor pretraining

## Access
Tier: registration. Codalab: https://codalab.lisn.upsaclay.fr/competitions/12239 . Sign up and join the challenge to receive the data link. License is challenge-distribution; mostly CC BY-NC-ND derivative.

## Conversion notes
NIfTI. Use the FLARE23 nnU-Net plan or write a custom semi-supervised trainer. Phase metadata is in the filename suffix. Approximately 80 GB on disk - confirm via Codalab before pulling.

## License
CC BY-NC-ND 4.0.

## Citation
Ma J et al. "Automatic Organ and Pan-cancer Segmentation in Abdomen CT: the FLARE 2023 Challenge." arXiv:2408.12534 (2024).

## Gotchas
- Heterogeneous phases; do not assume PV phase only.
- Single tumor class lumps disparate cancers; not a fine-grained tumor classifier source.
- Codalab is the official portal; mirrors are unofficial.
