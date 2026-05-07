# BIOMEDICA (BMCA-CLIP archive)

**Year:** 2025 (CVPR 2025) | **Paper:** [arXiv:2501.07171](https://arxiv.org/abs/2501.07171)
**Access:** open (per-article PMC license) | **Download:** Hugging Face / streaming

## Summary

BIOMEDICA converts the entire PubMed Central Open Access subset into a deep-learning-ready multimodal corpus of approximately 24.07 million unique image-caption pairs (and ~30M image-references) drawn from 6+ million open-access biomedical articles. It is the largest open biomedical image-text archive currently available and is the upstream training data for the BMCA-CLIP family of vision-language models. Each pair is annotated with 27 metadata fields, including PMID, MeSH terms, license, publication date, journal title, plus coarse-grained image-type metadata. The authors define 12 global concepts and 170 local concepts via expert annotation.

## Image modalities

Mixed biomedical: pathology, microscopy, radiology (X-ray, CT, MRI, ultrasound), ophthalmology (fundus), dermatology, surgery, cell biology, and parasitology. Radiology is a substantial but minority subset; metadata fields enable filtering before training a radiology-only VLM.

## Text type

PMC figure captions, in-paragraph figure references, and structured article-level metadata.

## Size

~27 TB raw. Streaming the archive via the published dataset toolkit avoids local download. The smaller `BIOMEDICA-Compact` subsets are intended for downstream finetuning; refer to the dataset card on Hugging Face for current variants.

## License caveat

Per-article licensing applies (CC0, CC-BY, CC-BY-SA, CC-BY-NC, CC-BY-NC-SA, CC-BY-NC-ND). The toolkit emits a `commercial_use_allowed` flag per record so commercial training mixtures can be filtered. Always honor original article licensing.

## Notes for VLM training

Heavy expected overlap with PMC-OA, MedICaT, and ROCOv2. When training, dedupe by `pmid + figure_id` against those datasets to avoid double-counting. Metadata-side filtering (`mesh_terms` containing radiology terms, or `image_type in {radiology}`) yields a clean radiology-only subset.
