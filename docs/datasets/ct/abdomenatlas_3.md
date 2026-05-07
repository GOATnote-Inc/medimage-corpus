# AbdomenAtlas 3.0 (RadGPT)

## What it is
AbdomenAtlas 3.0 (the RadGPT dataset) is the third major release in the AbdomenAtlas family from JHU. It contains 9,262 abdominal CT volumes paired with structured medical reports ("superhuman" reports, more accurate, detailed, and standardized than typical human radiologist reports per the authors). Per-voxel tumor masks are provided for liver, kidney, and pancreas. Total dataset size 586 GB.

## Why it matters for training
This is one of only two open abdominal CT corpora that pair volumes with reports at scale (the other being the report subset within AMOS-MM). Use it for:
- Vision-language pretraining over abdominal CT
- Tumor-aware report generation
- Visual question answering over CT
- Retrieval-augmented generation grounded in CT

ICCV 2025 publication.

## Access
Tier: registration. Hugging Face dataset at https://huggingface.co/datasets/AbdomenAtlas/AbdomenAtlas3.0 . Source repo at https://github.com/MrGiovanni/RadGPT . Download via `huggingface-cli download AbdomenAtlas/AbdomenAtlas3.0 --repo-type dataset` after accepting terms.

## Conversion notes
Auto-converted to Apache Parquet on HF. Volumes are NIfTI inside the parquet shards. Reports are JSON / structured text. Train/test IID and OOD splits are pre-computed under TrainTestIDS.

## License
CC BY-NC-SA 4.0.

## Citation
Bassi PRAS, Yavuz M, Wang K et al. "RadGPT: Constructing 3D Image-Text Tumor Datasets" ICCV 2025. arXiv:2501.04678.

## Gotchas
- Reports are LLM-generated and structured; treat them as supervision, not ground truth.
- 18,524 rows on HF includes train + test splits; verify train/test boundary before evaluation.
- Tumor masks only cover liver / kidney / pancreas; for full 25-organ masks pair with AbdomenAtlas 1.1 Mini.
