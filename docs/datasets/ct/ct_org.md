# CT-ORG

## What it is
CT-ORG is a multi-organ CT segmentation dataset hosted on TCIA. It contains 140 CT scans from 140 subjects with voxel-level masks for six organs: lung, bones, liver, kidneys, bladder, and brain (subset). 16.9 GB total. Cases span abdominal, full-body, contrast and non-contrast, low-dose and high-dose acquisitions; many contain liver lesions.

## Why it matters for training
- Diverse contrast and dose conditions
- Useful for contrast-invariant pretraining
- Six general-purpose organ classes
- Compact size, easy to ingest in initial pipelines

## Access
Tier: open. https://www.cancerimagingarchive.net/collection/ct-org/ . Pull via NBIA Data Retriever or `tcia-cli`.

## Conversion notes
NIfTI. Per-organ mask channels. Convert to nnU-Net format if combining with other datasets. Mixed slice thickness; resample for consistency.

## License
CC BY 3.0.

## Citation
Rister B et al. "CT-ORG, a new dataset for multiple organ segmentation in computed tomography." Sci Data 7:381 (2020). DOI 10.1038/s41597-020-00715-8.

## Gotchas
- Brain class is only annotated on scans whose FOV includes the head; do not assume universal coverage.
- 140 cases is small; use as auxiliary supervision rather than primary training source.
