# CheXpert Plus

CheXpert Plus (Chambon et al., 2024) is the long-awaited multimodal
augmentation of the original CheXpert dataset. It pairs 223,462 chest
radiographs (DICOM) from 64,725 patients across 187,711 imaging studies
with the original free-text radiology reports - the same Stanford Hospital
cohort that produced CheXpert v1.0, but now with full text supervision.

Each report is split into 11 standardized subsections (Indication, History,
Comparison, Technique, Findings, Impression, Recommendation, etc.) ready
for structured language modelling. Each DICOM ships with 47 metadata fields
including patient demographics, view position, manufacturer, and study
descriptors. CheXpert-14 structured labels are inherited from the original
release.

This is the natural Stanford-side complement to MIMIC-CXR: it doubles the
paired-report training pool to >600,000 image-report pairs when used jointly
with MIMIC-CXR-JPG and PadChest, and crucially adds geographic + cohort
diversity (Stanford vs BIDMC vs San Juan).

Access is via Stanford AIMI's Azure portal under the CheXpert Plus
Research Use Agreement (academic, non-commercial). Approximate transfer
size is 350 GB (DICOM + text). Subset DICOMs at 320 px and 512 px are
provided for fast iteration.

For VLM training, the recommended pipeline is: (1) decode DICOM with
pydicom + windowing; (2) shard alongside the 11-section reports as
WebDataset; (3) reuse the published CheXagent / RaDialog tokenization
splits.

Paper: arXiv 2405.19538. https://arxiv.org/abs/2405.19538
