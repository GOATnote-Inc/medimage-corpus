# Pancreatic-CT-CBCT-SEG

## What it is
Pancreatic-CT-CBCT-SEG is a paired CT and Cone-Beam CT (CBCT) collection from Memorial Sloan Kettering Cancer Center on TCIA. It contains imaging from 40 patients receiving ablative radiation therapy for locally advanced pancreatic cancer: each patient has 1 diagnostic-quality planning CT plus 2 CBCT scans (1 limited-view + 1 full-rotation). 24,246 total images / 370 series. 14.29 GB.

Manual organ-at-risk segmentations included for stomach, duodenum, and small bowel. RT dose files and RTSTRUCT data are bundled.

## Why it matters for training
- Paired CT and CBCT registration (rare in open data)
- Image-guided radiotherapy / IGRT pipeline pretraining
- Pancreatic OAR segmentation (clinically relevant tight tolerances)
- Cone-beam noise simulation / domain adaptation source

## Access
Tier: open. https://www.cancerimagingarchive.net/collection/pancreatic-ct-cbct-seg/ . Pull via NBIA Data Retriever or `tcia-cli`.

## Conversion notes
DICOM with RTSTRUCT. Convert RTSTRUCT to NIfTI masks with `dcmrtstruct2nii` or similar. Acquired during deep-inspiration breath-hold; respiratory state is consistent within a case.

## License
CC BY 4.0.

## Citation
Hong J et al. "Breath-hold CT and cone-beam CT images with expert manual organ-at-risk segmentations from radiation treatments of locally advanced pancreatic cancer." [data set] TCIA (2021). DOI 10.7937/TCIA.ESHQ-4D90.

## Gotchas
- 40-patient cohort is too small for primary training; use as a fine-tuning / registration benchmark.
- Single institution; OAR contouring conventions match MSKCC practice.
- CBCT pixel intensity is uncalibrated relative to HU.
