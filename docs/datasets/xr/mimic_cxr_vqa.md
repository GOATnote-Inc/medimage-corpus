# MIMIC-Ext-MIMIC-CXR-VQA

MIMIC-Ext-MIMIC-CXR-VQA (Bae et al., NeurIPS Datasets and Benchmarks
2023; PhysioNet release v1.0.0 2024) is a large-scale visual question
answering (VQA) dataset built on top of MIMIC-CXR-JPG and the Chest
ImaGenome scene-graph annotations. It contains approximately 377,000
VQA pairs covering all 377,110 MIMIC-CXR images.

Question taxonomy: 48 unique templates spanning seven content types
(presence, anatomy, attribute, abnormality, size, plane, gender),
each developed under board-certified medical-expert guidance to ensure
clinical relevance. Beyond standard-form VQA, the dataset includes
complex set-and-logical-operation queries ("Are pneumothorax and
atelectasis both present in any of the lung zones?"), making it
substantially harder than prior medical VQA benchmarks (VQA-Med,
VQA-RAD, SLAKE).

This is the gold-standard instruction-tuning dataset for chest-VLM
research. It is the input set for nearly every modern CXR
instruction-tuned model (LLaVA-Med, RaDialog, CheXagent, Med-Flamingo,
RadFM).

The release ships annotations only (~3 GB JSON) - the actual image
files are NOT redistributed. Users must independently download
MIMIC-CXR-JPG (`mimic_cxr_jpg`) and join via the `dicom_id` and
`study_id` columns.

Distribution: PhysioNet, under the same Credentialed Health Data
License 1.5.0 as MIMIC-CXR (CITI training + DUA required).

Paper: arXiv 2310.18652. https://arxiv.org/abs/2310.18652
