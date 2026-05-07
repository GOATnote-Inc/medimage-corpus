# RP3D-DiagDS (RadFM source)

**Year:** 2024 (Nature Communications) | **Paper:** [Zheng et al. 2024](https://www.nature.com/articles/s41467-024-54424-6)
**Access:** registration (HF) | **License:** Research-only (Radiopaedia ToS apply to images)

## Summary

RP3D-DiagDS (Radiopaedia 3D Diagnosis Dataset) is a large-scale long-tailed radiology disease-diagnosis dataset comprising 39,026 cases / 195,010 scans across 9 modalities and 7 anatomical regions, covering 5,568 disorders mapped to 930 unique ICD-10-CM codes. The text manifest is hosted on Hugging Face (2.22 GB JSON); image data is scraped from Radiopaedia per-case via the manifest URLs. RP3D-DiagDS is the foundation for the RP3D-Diag classifier and a key shard of MedMD (the RadFM training corpus).

## Image modalities

Nine modalities: CT, MRI, X-ray, ultrasound, fluoroscopy, nuclear medicine, mammography, DSA (digital subtraction angiography), barium enema. Anatomical regions: head/neck, spine, chest, breast, abdomen/pelvis, upper limb, lower limb.

## Text type

Per-case diagnosis labels (ICD-10-CM + free-text disorder names) plus accompanying captions and excerpted radiology reports where available.

## Size

2.22 GB (text manifest + label dictionaries on Hugging Face). Images are downloaded separately from Radiopaedia per-URL; the Radiopaedia ToS governs scraping.

## Access

Hugging Face registration required for the manifest. Images respect Radiopaedia case-contributor licensing - non-commercial research use.

## Notes for VLM training

Most diverse-modality public radiology dataset by raw modality count (9 modalities vs. typical 4-5). Strong long-tail label distribution (5,568 disorders) makes it an excellent disease-diagnosis evaluation target. Pair with MedMD (RadFM) which uses RP3D as one of its source shards. Be aware of the upstream M3D-Cap DMCA situation - Radiopaedia scraping is an unstable distribution channel.
