# CT Colonography (ACRIN 6664)

## What it is
The CT Colonography (ACRIN 6664) collection on TCIA is the imaging archive of the National CT Colonography Trial. It contains 941,771 DICOM images from 825 subjects (3,451 series), 496.67 GB total. Each subject has prone and supine CT volumes plus polyp annotations from optical colonoscopy as ground truth, with histology subtypes for confirmed lesions.

## Why it matters for training
This is the largest open CT colonography corpus by image count and one of the largest open abdominal CT corpora period. Useful for:
- Polyp / colon lesion detection
- Abdominal CT pretraining
- Body habitus diversity (covers screening-age population)
- Prone/supine paired registration
- Foundation for derived datasets (CTSpine1K aggregates 825 of these scans)

## Access
Tier: open. Visit https://www.cancerimagingarchive.net/collection/ct-colonography/ and pull via NBIA Data Retriever or `tcia-cli`. CC BY 3.0.

## Conversion notes
DICOM, multiple slice thicknesses (1.0-2.5 mm). Convert with dcm2niix. Pair prone and supine series by SeriesInstanceUID metadata. Polyp size and segment annotations are in supplemental spreadsheets, not DICOM SR.

## License
CC BY 3.0.

## Citation
Smith K et al. "Data From CT COLONOGRAPHY" [data set]. The Cancer Imaging Archive (2015). DOI 10.7937/K9/TCIA.2015.NWTESAY1. Original trial: Johnson CD et al. NEJM 359:1207-1217 (2008).

## Gotchas
- Annotations are at study (polyp present yes/no, location) level, not voxel-level.
- Colon was prepped (laxative + tagging agent); pixel intensity ranges differ from non-prepped abdominal CT.
- Some series mix CO2-insufflated colon with surrounding abdomen; train accordingly.
