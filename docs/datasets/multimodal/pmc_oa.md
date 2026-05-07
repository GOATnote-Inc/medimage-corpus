# PMC-OA

**Year:** 2023 | **Paper:** [arXiv:2303.07240](https://arxiv.org/abs/2303.07240)
**Access:** open | **License:** Per-article PMC OA mix

## Summary

PMC-OA is one of the standard biomedical figure-caption corpora derived from the PubMed Central Open Access subset, containing approximately 1.6 million figure-caption pairs. The dataset ships in two variants: `pmc_oa.jsonl` decomposes compound captions into separate single-image-single-caption pairs using ChatGPT, while `pmc_oa_beta.jsonl` keeps the original compound captions. PMC-OA is the canonical pretraining corpus for the PMC-CLIP family of biomedical CLIP models and is widely used as a baseline by downstream biomedical VLMs.

## Image modalities

Mixed biomedical: radiology (X-ray, CT, MRI, ultrasound), pathology, microscopy, fundus, dermatology, endoscopy. Per-paper modality varies; figure-level modality labels are not part of the standard release.

## Text type

PMC figure captions. Both compound (multi-panel) and decomposed-caption variants are provided.

## Size

28.8 GB (images + JSONL).

## Access

Open download from Hugging Face. Each source paper carries its own PMC OA license; the dataset itself does not impose additional license terms beyond the source. Users should respect per-article licensing.

## Notes for VLM training

Heavy overlap with MedICaT, BIOMEDICA, and the PMC-derived shards of MedTrinity-25M. Dedup by `pmc_id + figure_id`. PMC-OA's caption-decomposition variant is well-suited for direct CLIP-style training; the beta (compound) variant is closer to raw figure context and is the recommended substrate for figure-grounded VLMs. Loading requires the `jsonlines` Python package.
