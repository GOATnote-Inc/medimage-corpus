# M3D-Cap

**Year:** 2024 | **Paper:** [arXiv:2404.00578](https://arxiv.org/abs/2404.00578)
**Access:** registration (HF; current DMCA notice) | **License:** Apache-2.0 (manifest); upstream Radiopaedia ToS

## Summary

M3D-Cap is the largest open 3D medical image-text paired dataset, claimed to comprise 120,000 3D CT image-caption pairs scraped from Radiopaedia. Each case includes one or more 3D CT volumes (as JPEG slice stacks per imaging plane) and a free-text English diagnostic report describing findings, lesion locations, measurements, and anomaly classifications. M3D-Cap is the underlying training corpus for the M3D family of 3D medical multimodal LLMs (M3D-LaMed) by BAAI-DCAI.

## Image modality

Volumetric CT (multiple imaging planes per case: axial, coronal, sagittal, pre/post-contrast).

## Text type

Free-text diagnostic reports authored by Radiopaedia case contributors. Includes findings, lesion type/location, measurements, and anomaly classifications.

## Size

~1.07 TB (978 GB images + reports). Two subsplits: `ct_case` (general cases) and `ct_quizze` (medical exam quality).

## Access caveat

The Hugging Face mirror is currently disabled by a DMCA takedown. Treat the mirror as unstable. Source code and preprocessing scripts remain at github.com/BAAI-DCAI/M3D. Re-scraping Radiopaedia directly violates that platform's terms; if the HF mirror is restored, expect a research-only access agreement.

## Notes for VLM training

This is the most accessible large 3D-CT-paired-report corpus aside from CT-RATE/RadGenome-ChestCT. Lower curation quality than CT-RATE (community contributions vs. clinical reports), but covers more anatomical regions (whole-body, not chest-only). If the HF distribution is unavailable, fall back to CT-RATE + RadGenome-ChestCT for chest-CT VLM pretraining.
