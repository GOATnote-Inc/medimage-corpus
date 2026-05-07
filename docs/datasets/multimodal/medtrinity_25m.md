# MedTrinity-25M

**Year:** 2024 | **Paper:** [arXiv:2408.02900](https://arxiv.org/abs/2408.02900)
**Access:** registration (HF gated) | **License:** Mixed per-source

## Summary

MedTrinity-25M is a large-scale multimodal medical dataset of 25 million image-text pairs spanning 10 imaging modalities and 65+ diseases, with multigranular textual annotations: disease/lesion type, modality, region descriptions, inter-region relationships, and local annotations (bounding boxes, segmentation masks). It is a meta-aggregation of 90+ source datasets (CheXpert, MIMIC-CXR, MIMIC-CXR-JPG, PadChest, NIH-CXR, CT-RATE, BRATS24, NCT-CRC-HE-100K, Path-VQA, TCGA, ultrasound and brain MRI shards, etc.) re-captioned via a GPT-4V/Gemini pipeline.

## Image modalities

Chest X-ray, CT, MRI, ultrasound, mammography, endoscopy, fundus, dermatology, microscopy, histopathology. Aggregated dataset-by-dataset; per-shard licensing varies.

## Text type

Multigranular captions covering coarse modality identification, disease/lesion classification, region-specific descriptions, and inter-regional relationships. Includes spatial annotations (bounding boxes, segmentation masks) where available.

## Size

1.66 TB. Of the 25M nominal pairs, 18M are accessible after fetching upstream sources; ~7M are gated behind upstream credentialed-access tiers (e.g., PhysioNet for MIMIC-CXR, Stanford RUA for CheXpert).

## Access caveats

The dataset is itself a manifest + caption layer; users must download upstream image data themselves and apply the corresponding licenses. Mixed licenses include CC-BY-4.0, CC0-1.0, OpenRAIL, MIT, PhysioNet Credentialed, Stanford RUA, and CC-BY-NC variants. Read each source license before assembling commercial training mixes.

## Notes for VLM training

Strongly overlaps `xr/mimic_cxr`, `xr/chexpert`, `xr/padchest`, `ct/ct_rate`. Use the per-record `source` field to dedupe against modality-specific manifests. Multigranular caption format is well-suited for grounded captioning + region-VQA training.
