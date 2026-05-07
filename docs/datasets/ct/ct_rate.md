# CT-RATE

## What it is
CT-RATE is the largest open paired chest-CT-and-radiology-report corpus to date. It contains 25,692 non-contrast chest CT volumes (expanded to 50,188 reconstructions) from 21,304 unique patients at Istanbul Medipol University Hospital, each paired with a free-text radiology report and structured multi-abnormality labels. Released by Hamamci et al. and published in Nature Biomedical Engineering (2026).

## Why it matters for training
This is the gold-standard pretraining corpus for CT vision-language models. It powers three open foundation models built directly on it:
- CT-CLIP (contrastive language-image pretraining for 3D CT)
- CT-CHAT (vision-language chat over CT volumes)
- GenerateCT (text-conditional 3D CT generation)

For VLM work, this is the single most valuable open CT dataset, because volume-level paired text is rare. Use it for image encoder pretraining, report generation, abnormality classification, retrieval, and generative modeling.

## Access
Tier: registration. Visit https://huggingface.co/datasets/ibrahimhamamci/CT-RATE and accept the terms of use (academic/research only, no re-identification, GDPR/HIPAA compliant). Authenticate with `huggingface-cli login` then `huggingface-cli download ibrahimhamamci/CT-RATE --repo-type dataset --local-dir CT-RATE`.

## Conversion notes
Volumes ship as NIfTI under `train/` and `valid/`. Reports are CSV. Voxel spacing varies; resample to 1.5x1.5x3 mm or 1mm isotropic before training. Multi-abnormality CSV has 18 binary findings. ~21.3 TB total - plan storage carefully.

## License
CC-BY-NC-SA-4.0. Non-commercial. Required attribution.

## Citation
Hamamci IE et al. "A foundation model utilizing chest CT volumes and radiology reports for supervised-level zero-shot detection of abnormalities" arXiv:2403.17834 (2024).

## Gotchas
- HF token gate stalls automated pulls until terms accepted.
- Reports are English (translated from Turkish); some translation artifacts.
- Validation patients are disjoint from training; respect for benchmarking.
- 21.3 TB; pre-stage on object store before training.
