# VQA-RAD

**Year:** 2018 | **Paper:** [Lau et al. 2018 (Sci. Data)](https://doi.org/10.1038/sdata.2018.251)
**Access:** open | **License:** CC0-1.0 (public domain)

## Summary

VQA-RAD is the canonical clinician-generated medical Visual Question Answering benchmark. It contains 2,244 question-answer pairs over 314 radiology images sourced from MedPix. Train / Test split: 1,793 QA / 451 QA. Questions are split between binary yes/no and open-ended free-form types, covering anatomy, modality, plane, finding presence, and quantitative attributes. Each question is naturally created and validated by clinicians, making it the highest-quality clinical-language VQA evaluation set despite its small size.

## Image modalities

Chest X-ray, CT, MRI. Anatomical coverage: head, chest, abdomen.

## Text type

VQA pairs (clinician-authored question + answer). Binary yes/no and open-ended question types.

## Size

34.5 MB.

## Access

Open download from Hugging Face under CC0-1.0 (full public-domain dedication - including commercial use). Full dataset also archived on the Open Science Framework.

## Notes for VLM training

VQA-RAD is the gold standard MedVQA evaluation benchmark and is among the few medical datasets distributed under CC0 (public domain). Despite its small size (2,244 pairs, 314 images), it remains the most-cited clinical-VQA evaluation set because every QA pair is clinician-validated. Use exclusively as evaluation; never train on the test split. Pair with SLAKE (bilingual) and PMC-VQA (large-scale GPT-generated) for a complete MedVQA evaluation suite.
