# INSPECT (Stanford CT-PA + EHR)

**Year:** 2023 (NeurIPS) | **Paper:** [arXiv:2311.10798](https://arxiv.org/abs/2311.10798)
**Access:** application (Stanford AIMI / Redivis DUA) | **License:** Stanford AIMI RDUA, non-commercial

## Summary

INSPECT (Integrating Numerous Sources for Prognostic Evaluation of Clinical Timelines) is a multimodal CT-pulmonary-angiogram dataset designed for image+text+EHR foundation-model research. It contains 23,248 CTPA scans from 19,402 unique Stanford Medicine patients, each paired with the corresponding free-text radiology report (sectioned) and a longitudinal de-identified EHR record covering demographics, diagnoses, procedures, vitals, and outcome labels for pulmonary embolism diagnosis and prognosis.

## Image modality

Volumetric CT pulmonary angiography (chest, contrast-enhanced).

## Text type

Per-scan radiology report sections plus structured EHR (longitudinal). Outcome labels for PE presence, severity, and clinical sequelae are clinician-validated.

## Size

~1.5 TB (image + report + structured EHR). Distributed via Stanford Redivis.

## Access

Stanford AIMI Research Data Use Agreement, non-commercial only. Application-tier access: Stanford Redivis project request, IRB letter, and DUA signature required. Not credentialed-only - it requires named-PI application.

## Notes for VLM training

The largest open multimodal dataset combining 3D CT, paired free-text reports, and longitudinal EHR. Especially valuable for grounded report generation, outcome-prediction VLMs, and EHR-conditioned image understanding. Some overlap likely with the volume of CTPA cases referenced in MedTrinity-25M and RadFM/MedMD; dedup against `ct/inspect` if a sibling CT-only manifest entry exists.
