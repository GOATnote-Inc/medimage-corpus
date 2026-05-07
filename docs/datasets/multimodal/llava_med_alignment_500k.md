# LLaVA-Med Alignment 500K (PMC-15M sample)

**Year:** 2023 (NeurIPS Spotlight) | **Paper:** [arXiv:2306.00890](https://arxiv.org/abs/2306.00890)
**Access:** open | **License:** CC-BY-NC-4.0 (research only)

## Summary

LLaVA-Med Alignment 500K is the stage-1 biomedical concept-feature-alignment dataset for the LLaVA-Med vision-language assistant. It contains 500,000 image-caption pairs sampled from the larger PMC-15M corpus (15M figure-caption pairs from PubMed Central biomedical research articles). The sample preserves diversity across imaging modalities (CXR, CT, MRI, histopathology, gross pathology, microscopy, fundus, dermatology) and biomedical concepts. The dataset is distributed as a JSON manifest (358 MB) referencing PMC images; users download the actual images via the Microsoft LLaVA-Med data preparation scripts.

## Image modalities

Mixed biomedical: CXR, CT, MRI, ultrasound, histopathology, gross pathology, microscopy, fundus, dermatology.

## Text type

Single-task figure captions used as instruction-following alignment data ("Describe this figure" - caption).

## Size

358 MB JSON manifest; ~80 GB after downloading PMC images.

## Access

Open via the LLaVA-Med GitHub repository. Microsoft Research License for code; CC-BY-NC-4.0 for data (non-commercial research only).

## Notes for VLM training

Pair with `multimodal/llava_med_instruct_60k` for stage-2 multi-round conversation tuning. LLaVA-Med pioneered a two-stage biomedical VLM training recipe (alignment then instruct-tune) that has been widely replicated. Heavy overlap with PMC-OA, MedICaT, BIOMEDICA - dedup by `pmc_id + figure_id`. Useful as a curated, well-balanced subset of PMC-15M when training infrastructure cannot ingest the full 15M corpus.
