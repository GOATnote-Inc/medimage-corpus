# LIDC-IDRI

## What it is
The Lung Image Database Consortium and Image Database Resource Initiative (LIDC-IDRI) is the foundational lung CT corpus. Released by NCI / FNIH and hosted on TCIA. It contains 1,010 patients, 1,308 CT studies, and 244,527 individual images, with associated chest radiographs (290 CR images) on a subset. 133.16 GB total.

Annotations: each pulmonary nodule has been independently rated by four thoracic radiologists in a two-phase process, with per-radiologist contour and per-nodule attribute scores (subtlety, internal structure, calcification, sphericity, margin, lobulation, spiculation, texture, malignancy 1-5). XML format.

## Why it matters for training
LIDC-IDRI underlies almost every modern lung-nodule pipeline:
- LUNA16 (de-duplicated thin-slice subset)
- pylidc / MAX analysis tools
- Most lung CT foundation model evals
- Diagnosis subset (ground truth pathology) for malignancy prediction

It is the supervised-quality complement to NLST's screening scale. Pair them: pretrain on NLST, fine-tune on LIDC.

## Access
Tier: open. https://www.cancerimagingarchive.net/collection/lidc-idri/ . Pull via NBIA Data Retriever or `tcia-cli`. CC BY 3.0.

## Conversion notes
DICOM with XML annotation files (radiologist-specific). Use pylidc to parse: `pip install pylidc`. Convert to NIfTI/MHD with dcm2niix. Pixel spacing varies (0.5-0.9 mm in-plane, 0.6-3.0 mm through-plane). Filter to thin-slice (<= 2.5 mm) for nodule detection (this is what LUNA16 does).

## License
CC BY 3.0.

## Citation
Armato SG III et al. "The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): a completed reference database of lung nodules on CT scans." Med Phys 38:915-931 (2011). DOI 10.1118/1.3528204.

## Gotchas
- Four radiologists may disagree on a nodule; standard practice is to require >=3 of 4 agreement.
- Diagnosis ground truth is only on a small subset; do not assume malignancy_score is a label.
- Mixed slice thickness; filter for clinical use cases.
