# PMC-VQA

**Year:** 2023 | **Paper:** [arXiv:2305.10415](https://arxiv.org/abs/2305.10415)
**Access:** open | **License:** CC-BY-SA-4.0

## Summary

PMC-VQA is a large-scale medical visual-question-answering dataset with 227,000 VQA pairs across 149,000 medical images, spanning 20+ imaging modalities and a wide range of diseases. The dataset is constructed by GPT-driven question generation from PubMed Central image-caption pairs, with multiple-choice format (4 candidate answers per question). PMC-VQA-test (50K pairs) is the standard test set; PMC-VQA-test-clean is a 2,000-pair manually curated subset for high-quality evaluation. Two versions exist: v1 (compound figures) and v2 (non-compound, post-decomposition).

## Image modalities

Mixed biomedical: radiology (X-ray, CT, MRI, ultrasound), pathology, microscopy, fundus, dermatology, endoscopy, and 13+ other medical imaging types.

## Text type

VQA pairs (question + correct answer + 3 distractor choices + answer label). Multiple-choice format.

## Size

21.8 GB.

## Access

Open download from Hugging Face. CC-BY-SA-4.0 (with PMC OA source-paper licenses). Note: dataset viewer shows a `DatasetGenerationCastError` due to schema differences between v1 and v2 CSVs - load v1 and v2 separately.

## Notes for VLM training

PMC-VQA is the largest biomedical VQA corpus by a wide margin (227K pairs vs. 14K SLAKE, 2.2K VQA-RAD). Standard usage: pretraining VLMs on PMC-VQA train, then fine-tuning + evaluating on VQA-RAD, SLAKE, and ImageCLEF benchmarks. Use the test-clean split for quality evaluation; the GPT-generated training pairs have known noise.
