# NLST: National Lung Screening Trial

## What it is
The National Lung Screening Trial is a U.S. randomized controlled trial run from 2002-2010 that compared low-dose helical CT to chest radiography in 53,454 high-risk smokers across 33 sites. Imaging is now openly available via TCIA: 26,254 CT-screened subjects with 21,082,265 individual images across 11.14 TB of DICOM (CC BY 4.0). Limited clinical metadata is bundled with the imaging release; full trial covariates require an NCI/CDAS data application.

## Why it matters for training
NLST is the largest open low-dose lung CT screening corpus by an order of magnitude. Its scale, longitudinal multi-screen design (T0/T1/T2), real-world scanner diversity, and multi-year follow-up labels make it a pretraining-grade base for:
- 3D vision encoder pretraining (lung-focused or general-purpose)
- Lung nodule detection / characterization
- Risk modeling and longitudinal change prediction
- Lung cancer outcome prediction

Combine with LIDC-IDRI (annotated subset) and LUNA16 for a graduated supervision pipeline.

## Access
Tier: open (imaging) + application (full clinical). The TCIA collection at https://www.cancerimagingarchive.net/collection/nlst/ is fully open. Download with the NBIA Data Retriever or `tcia-cli` from a manifest file. Plan for 11+ TB of pull. Embargo on imaging lifted September 2021.

## Conversion notes
DICOM with consistent vendor metadata. Convert to NIfTI per series (use dcm2niix). Dose is low (CTDIvol ~1.5-2.0 mGy), thin-slice (1.0-2.5 mm). Resample to 1mm isotropic for SSL pretraining.

## License
CC BY 4.0 (TCIA imaging). Cite NCI/NLST.

## Citation
National Lung Screening Trial Research Team. "Reduced lung-cancer mortality with low-dose computed tomographic screening." NEJM 365:395-409 (2011). DOI 10.1056/NEJMoa1102873.

## Gotchas
- 11+ TB pull; rate-limit politely on TCIA.
- Histopathology slides and full clinical CSV require separate CDAS application.
- Slice thickness varies by site; filter for thin-slice if running nodule detection.
