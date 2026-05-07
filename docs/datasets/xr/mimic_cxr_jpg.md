# MIMIC-CXR-JPG

MIMIC-CXR-JPG (v2.1.0, 2024) is the JPG-converted, structured-label sibling
of the full MIMIC-CXR DICOM archive. It contains the same 377,110 chest
radiographs as MIMIC-CXR (227,835 studies, 65,379 patients) but in 8-bit JPG
form, eliminating DICOM decoding overhead and reducing total size from ~4.7
TB to 557.6 GB. Images are also paired with the same de-identified free-text
radiology reports as MIMIC-CXR, plus pre-computed CheXpert-14 and NegBio
label sets.

For chest-VLM pretraining and report-generation fine-tuning where DICOM
windowing is not required, MIMIC-CXR-JPG is the recommended source. It
loads ~5x faster than MIMIC-CXR DICOM, fits on a single H100 node SSD,
and is the input format used by virtually all published CXR VLMs.

Access is gated under PhysioNet Credentialed Health Data License 1.5.0 with
the same DUA + CITI training requirements as MIMIC-CXR. Files are also
mirrored on Google Cloud Storage; transfer fees apply at scale.

Practical tips: For training, build WebDataset shards directly from the JPG
files keyed by `dicom_id`. The release includes `mimic-cxr-2.0.0-chexpert.csv`
and `mimic-cxr-2.0.0-negbio.csv` for label joins. The free-text reports live
in a separate `mimic-cxr-reports.zip` archive on the parent MIMIC-CXR page.

Pairs naturally with MIMIC-CXR-VQA, Chest ImaGenome, and RadGraph for
multi-task learning.

DOI: https://doi.org/10.13026/jsn5-t979
