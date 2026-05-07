# MedMD (RadFM training corpus)

**Year:** 2023 | **Paper:** [arXiv:2308.02463](https://arxiv.org/abs/2308.02463)
**Access:** open (text manifest) | **License:** Apache-2.0 (manifest); per-source for images

## Summary

MedMD is the large-scale medical multimodal training corpus underlying RadFM, a generalist radiology foundation model. It comprises 16M image-text pairs total, including ~15.5M 2D images and 500K 3D scans paired with captions, radiology reports, visual-language instruction examples, or disease-diagnosis labels. MedMD is constructed from four newly assembled component datasets (PMC-Inline, PMC-CaseReport, RP3D-Series, MPx-Series) augmented with shards from PMC-OA, MIMIC-CXR, MedPix, mammography corpora, and others. Distributed as a 668 MB CSV manifest; images must be sourced separately from the upstream datasets per their respective access tiers.

## Image modalities

Radiology-broad: X-ray, CT, MRI, ultrasound, mammography, plus pathology shards.

## Text type

Mix of figure captions, radiology reports, instruction-following examples (questions + answers), diagnosis labels, and clinical case excerpts.

## Size

700 MB (text manifest only). Reconstructed full corpus would be in the multi-TB range across all upstream sources.

## Access

Hugging Face open download for the manifest. Image-data access depends on upstream sources: PhysioNet credentialed (MIMIC), open (PMC), application (MedPix), etc. The Apache-2.0 license applies only to the manifest; per-image licensing follows the source.

## Notes for VLM training

This is the most comprehensive open meta-manifest for radiology-paired text. Dedup target IDs: PMC-OA shards overlap heavily with `multimodal/pmc_oa`, MIMIC-CXR shards overlap with `xr/mimic_cxr`, and RP3D shards overlap with `multimodal/rp3d_diagds`. Treat MedMD as a curated assembly recipe rather than an independent corpus.
