# PadChest-GR (bilingual grounded reports)

**Year:** 2024 | **Paper:** [arXiv:2411.05085](https://arxiv.org/abs/2411.05085)
**Access:** application (BIMCV) | **License:** Custom research-only

## Summary

PadChest-GR is the first bilingual sentence-level grounded chest X-ray report dataset. It contains 4,555 chest radiograph studies (3,099 abnormal, 1,456 normal) drawn from the PadChest cohort, each with sentence-level descriptions in both English and Spanish, and precise spatial bounding-box annotations for both positive and negative findings. The corpus contains 7,037 positive-finding sentences and 3,422 negative-finding sentences. Every positive-finding sentence carries up to two independent sets of bounding boxes from different readers and is tagged with categorical labels for finding type, location, and progression. Co-developed by the University of Alicante, Microsoft Research, University Hospital Sant Joan d'Alacant, and MedBravo.

## Image modality

Chest radiograph (XR), single-frontal view per study, drawn from PadChest source DICOMs.

## Text type

Sentence-level grounded radiology reports in English + Spanish, with bounding box annotations per finding sentence and categorical labels (finding / location / progression).

## Size

~30 GB.

## Access

Application-tier through BIMCV. Subset of PadChest, so users must also have PadChest access.

## Notes for VLM training

This is the highest-quality public chest X-ray grounding benchmark - far smaller than MIMIC-CXR but with substantially richer per-sentence supervision (bounding boxes, finding-type labels, English+Spanish parallel text). Pair with PadChest (full corpus) and MIMIC-CXR for cross-cohort, cross-lingual VLM training. Critical for grounded report generation evaluation; use as held-out eval rather than train if that is the target capability.
