# TotalSegmentator v2

## What it is
TotalSegmentator v2 is the successor to TotalSegmentator v1, expanding to 117 anatomical structures (from 104). It contains 1,228 CT volumes from clinical real-world cases at University Hospital Basel, Switzerland. 23.6 GB. Released October 2023 on Zenodo.

## Why it matters for training
- Most-detailed open whole-body CT label scheme
- Drop-in supervision signal for multi-task pretraining
- Real-world clinical case mix (different scanners, contrasts, pathologies)
- Supersedes v1 for new work

Use as the gold standard for whole-body anatomy supervision. Combine with AbdomenAtlas + LIDC + RSNA challenges for graduated multi-task supervision.

## Access
Tier: open. Zenodo: https://zenodo.org/records/10047292 . Direct download.

## Conversion notes
NIfTI. Single multi-label NIfTI per volume (one of several variants). Voxel spacing varies. The official trained model uses 1.5mm isotropic. Use the `nnUNetv2` framework with the published Task IDs.

## License
CC BY 4.0.

## Citation
Wasserthal J et al. "TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images." Radiology: AI 5:e230024 (2023). DOI 10.1148/ryai.230024.

## Gotchas
- v2 only adds classes; subjects largely overlap v1 (1,204 vs 1,228), so do not double-count if combining.
- Some classes have very limited training cases (rare anatomy); check class frequency before training balanced losses.
- Single institution; validate cross-vendor robustness elsewhere.
