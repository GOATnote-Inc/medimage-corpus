# MedICaT

**Year:** 2020 (EMNLP Findings) | **Paper:** [arXiv:2010.06000](https://arxiv.org/abs/2010.06000)
**Access:** application (AI2) | **License:** Per-article PMC + research-only

## Summary

MedICaT is an Allen Institute for AI dataset of 217,060 medical figure-caption pairs extracted from 131,000 open-access biomedical papers in PubMed Central. ~72% of figures are radiology, ~13% histology, ~3% scope procedures, ~7% other. Inline references for 74% of figures provide additional textual context (paragraphs in the source paper that reference the figure), and a manually-annotated subset includes subfigure/subcaption boundary annotations. MedICaT is one of the canonical figure-caption corpora for biomedical VLM pretraining and was a foundational corpus for early medical CLIP models.

## Image modalities

Mixed: ~72% radiology (X-ray, CT, MRI, ultrasound), ~13% histology, ~3% scope procedures (endoscopy / surgical), ~7% other (microscopy, illustrations, gross specimens).

## Text type

Figure captions, manually-annotated subfigure / subcaption boundaries (small subset), and S2ORC-derived inline reference paragraphs (74% of figures).

## Size

104 GB (figures + captions + inline references). Subcaption/subfigure annotations: 14 MB. Train/val/test splits for the subcaption task: 0.2 MB.

## Access

Application-tier via the AI2 GitHub repo - non-commercial research only. Per-article licensing applies (PMC OA mix: CC, CC-BY, CC-BY-NC).

## Notes for VLM training

Heavy expected overlap with PMC-OA, BIOMEDICA, and ROCOv2 (all PMC-derived). Dedup by `pmc_id + figure_id`. The inline-reference text is a unique signal MedICaT provides over the simpler caption-only PMC-OA, useful for retrieval-augmented and grounded VLM training. The subfigure annotations are valuable supervision for compound-figure decomposition.
