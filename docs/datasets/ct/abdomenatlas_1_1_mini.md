# AbdomenAtlas 1.1 Mini

## What it is
AbdomenAtlas 1.1 Mini is currently the largest fully-annotated abdominal CT dataset in the public domain: 9,262 CT volumes with voxel-level segmentation masks for 25 anatomical structures. 328 GB total. Released by JHU's CCVL group.

The 25 classes: aorta, gallbladder, kidneys, liver, pancreas, postcava, spleen, stomach, adrenal glands, bladder, celiac trunk, colon, duodenum, esophagus, femurs, hepatic vessel, intestine, lungs, portal/splenic vein, prostate, rectum.

## Why it matters for training
The class coverage and volume count make this an ideal supervised-pretraining base for:
- Multi-organ abdominal segmentation
- Anatomy-aware 3D vision encoders
- Touchstone benchmark
- Models that need to reason about vasculature (celiac trunk, hepatic vessel, portal vein) as well as organs

## Access
Tier: registration. https://huggingface.co/datasets/AbdomenAtlas/_AbdomenAtlas1.1Mini . `huggingface-cli download AbdomenAtlas/_AbdomenAtlas1.1Mini --token $HF_TOKEN --repo-type dataset --local-dir AbdomenAtlas1.1Mini`.

## Conversion notes
Distributed in WebDataset (.tar shards). Internally NIfTI. Decode with the WebDataset PyTorch loader or unpack to flat NIfTI. Class IDs follow the published `class_map`.

## License
CC BY-NC-SA 4.0. Non-commercial.

## Citation
Bassi PRAS, Li W, Tang Y, et al. "Touchstone Benchmark: Are We on the Right Way for Evaluating AI Algorithms for Medical Segmentation?" arXiv:2411.03670 (2024). Underlying release: Li W et al. "AbdomenAtlas: A Large-Scale, Detailed-Annotated, & Multi-Center Dataset for Efficient Transfer Learning and Open Algorithmic Benchmarking" arXiv:2407.16697 (2024).

## Gotchas
- "Mini" is a misnomer; this is the publicly released subset of the larger internal dataset.
- HF token is required even for free download.
- Some classes (femurs, colon, intestine) extend outside the abdominal field of view; not all volumes contain all 25 classes.
