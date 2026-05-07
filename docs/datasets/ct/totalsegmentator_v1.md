# TotalSegmentator v1

## What it is
TotalSegmentator v1 is the original release of the TotalSegmentator dataset from University Hospital Basel. It contains 1,204 CT volumes with voxel-level masks for 104 anatomical structures spanning organs, vertebrae, ribs, muscles, and major vessels. 28.4 GB total. Released July 2022.

## Why it matters for training
This is the most-cited foundation dataset for whole-body CT anatomical segmentation. Use cases:
- Pretrain or finetune anatomy-aware models
- Reproduce the TotalSegmentator nnU-Net baseline
- Ablation against v2 (which adds 13 classes)
- Drop-in supervision signal for whole-body multi-task pretraining

## Access
Tier: open. Zenodo: https://zenodo.org/records/6802614 . `wget` or `curl`.

## Conversion notes
NIfTI. Each volume has multi-label masks under a per-class subdirectory or as a single multi-label NIfTI (depending on download variant). Use the published `class_map.py` to interpret integer labels. Voxel spacing varies; the standard model uses 1.5mm isotropic.

## License
CC BY 4.0.

## Citation
Wasserthal J et al. "TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images." Radiology: AI 5:e230024 (2023). DOI 10.1148/ryai.230024.

## Gotchas
- v2 supersedes v1 for new work; choose v1 only for replication.
- Real-world clinical mix means quality varies; some volumes have artifacts.
- Single institution (Basel); validate cross-vendor robustness elsewhere.
