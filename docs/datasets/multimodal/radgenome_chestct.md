# RadGenome-ChestCT

**Year:** 2024 | **Paper:** [arXiv:2404.16754](https://arxiv.org/abs/2404.16754)
**Access:** registration (HF) | **License:** CC-BY-4.0

## Summary

RadGenome-ChestCT is a region-guided 3D chest CT interpretation dataset that extends CT-RATE with 665,218 grounded multi-granularity reports plus 1.3M grounded VQA pairs, anchored to organ-level segmentation masks across 197 anatomical categories. It is built from the same 25,692 chest CT volumes (20,000 patients) as CT-RATE - each sentence in the grounded reports is linked to the specific anatomical regions referenced via segmentation masks, supporting grounded report generation, region-specific VQA, and visual grounding training objectives.

## Image modality

Same 3D chest CT volumes as CT-RATE (NIfTI). Adds 197-category organ segmentation masks per volume.

## Text type

Grounded multi-granularity reports (sentence -> region mask), grounded VQA pairs (question + answer + region mask), full-report findings/impression text.

## Size

1.32 TB (volumes are stored separately in CT-RATE; this dataset adds masks + grounded text). 665K rows in the grounded-report split.

## License

CC-BY-4.0 (one of the most permissive licenses among large CT VLM datasets - commercial use allowed with attribution). DOI: 10.57967/hf/5331.

## Notes for VLM training

Pairs naturally with `ct/ct_rate` - the same volumes carry CT-RATE's full-report text and RadGenome's grounded text. Dedup target id: `ct/ct_rate`. Region grounding makes this an ideal source for spatially-grounded VLM training (CXR-RAS-style or RadGenome-style) and for region-conditioned report generation. The 197-category mask vocabulary is finer-grained than TotalSegmentator's 117 classes.
