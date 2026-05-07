# MIMIC-CXR Database

The MIT/BIDMC MIMIC-CXR Database (v2.1.0, 2024) is the gold-standard paired
chest-X-ray and free-text report corpus. It contains 377,110 chest radiographs
(DICOM) corresponding to 227,835 imaging studies on 65,379 patients presenting
to the Beth Israel Deaconess Medical Center Emergency Department between 2011
and 2016. Every study is paired with a de-identified free-text radiology
report, and pre-computed structured labels are provided in two flavours
(CheXpert 14-label and NegBio).

This dataset is the single largest open paired image+report corpus in the
field and is the canonical training source for chest VLMs (CheXagent,
RaDialog, Med-Flamingo, RadFM, MAIRA-2, CheXzero, ELIXR). It is also the basis
for the MIMIC-CXR-VQA, Chest ImaGenome, RadGraph, and ReXrank derivatives.

Access is gated: it is hosted on PhysioNet under a Credentialed Health Data
License 1.5.0. Investigators must hold a credentialed PhysioNet account,
complete CITI "Data or Specimens Only Research" training, and sign the data
use agreement. Files are mirrored on AWS and Google Cloud Storage; transfer
charges may apply at scale.

For VLM training where DICOM is not required, prefer the JPG sibling
(`mimic_cxr_jpg`) which is decoded, smaller (557 GB vs ~4.7 TB), and ships
ChexPert/NegBio labels in the same archive. Keep MIMIC-CXR DICOM only when
you need windowing/scaling control or DICOM metadata for cohort filtering.

DOI: https://doi.org/10.13026/4jqj-jw95
