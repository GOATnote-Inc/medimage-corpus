# AbdomenAtlas 1.0 Mini

## What it is
AbdomenAtlas 1.0 Mini is the NeurIPS 2023 baseline release from JHU's CCVL group. It contains 5,195 abdominal CT volumes with voxel-level masks for 8 organs: spleen, liver, kidneys, stomach, gallbladder, pancreas, aorta, IVC. 326 GB total.

## Why it matters for training
This is the original AbdomenAtlas release and is the most-commonly-cited starting point for abdominal CT segmentation pretraining. It is roughly half the size of 1.1 Mini but has stable, well-validated 8-organ masks. Useful for:
- Reproducing AbdomenAtlas baselines
- Smaller pretrain budgets
- Ablation studies against the 1.1/3.0 expansions

## Access
Tier: registration. https://huggingface.co/datasets/AbdomenAtlas/AbdomenAtlas1.0Mini . Also mirrored on Dropbox and Baidu Wangpan. `huggingface-cli download` with HF token.

## Conversion notes
NIfTI per volume. Use class IDs 1-8. Many volumes are aggregated from upstream public collections (BTCV, MSD, KiTS, CHAOS, AMOS, FLARE, TotalSegmentator); annotation pipeline harmonized them under one schema.

## License
CC BY-NC-SA 4.0.

## Citation
Qu C, Zhang Y, et al. "AbdomenAtlas-8K: Annotating 8,000 CT Volumes for Multi-Organ Segmentation in Three Weeks." NeurIPS 2023. arXiv:2305.09666.

## Gotchas
- Source-mixing means resolution and contrast vary widely; bake heavy intensity augmentation into training.
- 1.1 Mini supersedes this for 25-class work; only choose 1.0 if specifically benchmarking against the original baseline.
