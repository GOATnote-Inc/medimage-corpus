# AbdomenAtlas-8K

## What it is
AbdomenAtlas-8K is the NeurIPS 2023 release from MrGiovanni's group at Johns Hopkins. It provides 8,448 abdominal CT volumes ( ~3.2M slices, 1.2 TB ) annotated for 8 organs: spleen, liver, kidneys, stomach, gallbladder, pancreas, aorta, and IVC. The annotation pipeline used a human-in-the-loop strategy that compressed labeling time to roughly three weeks.

## Why it matters for training
Until the AbdomenAtlas-1.1 release added 17 more classes, this was the largest fully-annotated abdominal CT dataset in the open. It is still the best-suited corpus for:
- Pretraining 3D vision encoders on abdominal anatomy
- Self-supervised learning with strong organ priors
- SAM / SAM-Med2D / MedSAM 3D extension training
- Multi-task multi-organ model warm-start

## Access
Tier: registration. Distributed via Hugging Face under `AbdomenAtlas/`. Source aggregates several upstream collections (BTCV, MSD, KiTS, FLARE, etc.); confirm secondary licenses if redistributing. Repository: https://github.com/MrGiovanni/AbdomenAtlas .

## Conversion notes
Volumes ship as NIfTI with per-organ masks. Standard nnU-Net training works out of the box. Mixed scanner vendors and contrast phases; consider phase-conditioned augmentation.

## License
CC BY-NC-SA 4.0. Non-commercial, share-alike.

## Citation
Qu C, Zhang Y, et al. "AbdomenAtlas-8K: Annotating 8,000 CT Volumes for Multi-Organ Segmentation in Three Weeks." NeurIPS 2023. arXiv:2305.09666.

## Gotchas
- Annotations are AI-assisted human-in-the-loop, so a small fraction of masks may be imperfect.
- The 8,448 figure is total; only a 3,410 subset has been released to the public so far.
- For full 25-class masks, prefer AbdomenAtlas 1.1 Mini.
