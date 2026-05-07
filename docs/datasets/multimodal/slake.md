# SLAKE (Semantically-Labeled Knowledge-Enhanced VQA)

**Year:** 2021 (ISBI Oral) | **Paper:** [Liu et al. 2021 (ISBI)](https://www.med-vqa.com/slake/)
**Access:** open | **License:** CC-BY-4.0

## Summary

SLAKE is a bilingual (English + Chinese) Medical VQA benchmark designed to evaluate semantically-knowledgeable medical visual question answering. It contains 14,028 VQA pairs (Train 9,840 / Validation 2,100 / Test 2,090) over 642 medical images spanning chest X-ray, CT, and MRI modalities, with 10 content categories: modality, position, organ, abnormality, size, color, knowledge graph, knowledge graph base, plane, quantity. Question types are split between OPEN (free-form generation) and CLOSED (yes/no or multiple-choice). Each question carries a semantic label indicating the type of knowledge probed. SLAKE remains one of the most-cited Medical VQA evaluation benchmarks alongside VQA-RAD and PMC-VQA.

## Image modalities

Chest X-ray, CT, MRI. Anatomical coverage: chest, head, abdomen.

## Text type

VQA pairs (question + answer), bilingual (English + simplified Chinese). Semantic labels per question (modality / position / organ / abnormality / etc.).

## Size

217 MB.

## Access

Open download from Hugging Face. CC-BY-4.0 (commercial use allowed with attribution).

## Notes for VLM training

Standard MedVQA evaluation benchmark. Use as eval rather than train for VLMs targeting medical question answering. Bilingual pairs make SLAKE the canonical Chinese-language MedVQA evaluation dataset; combine with VQA-RAD and PMC-VQA for a complete English-language MedVQA evaluation suite. Its small size (642 images) makes it a stress test for sample-efficient evaluation rather than a generalization benchmark.
