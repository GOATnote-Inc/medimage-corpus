# BRAX (Brazilian labeled chest X-ray dataset)

BRAX (Reis et al., 2022) is a Brazilian chest X-ray dataset released by
Hospital Israelita Albert Einstein (Sao Paulo) on PhysioNet. It contains
40,967 chest radiographs from 24,959 imaging studies on 19,351 unique
patients. Images are provided in both anonymized DICOM and PNG-converted
folders, organized hierarchically by patient -> study -> series.

Labels follow the CheXpert-14 schema (atelectasis, cardiomegaly,
consolidation, edema, enlarged_cardiomediastinum, fracture, lung_lesion,
lung_opacity, no_finding, pleural_effusion, pleural_other, pneumonia,
pneumothorax, support_devices), but are derived by an NLP labeler
adapted for Brazilian Portuguese radiology-report text. Each label is
coded as 1 (positive), 0 (negative), or -1 (uncertain), matching the
original CheXpert convention.

The full free-text reports are NOT released, so BRAX is not strictly
VLM-paired - but the underlying labels were Portuguese-derived, making
it the largest open Portuguese-source CXR corpus available. Useful for
multilingual robustness analysis and for cross-population pretraining
(South American imaging differs in baseline demographics and disease
prevalence from US/EU cohorts).

Access is via PhysioNet under the Credentialed Health Data License
1.5.0; users must complete CITI training and sign the DUA. Approximate
full-DICOM size is ~60 GB.

DOI: https://doi.org/10.13026/grwk-yh18
