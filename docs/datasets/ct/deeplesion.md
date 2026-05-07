# DeepLesion (NIH)

## What it is
DeepLesion is a large-scale CT lesion dataset released by the NIH Clinical Center in 2018. It contains 32,735 lesions in 32,120 axial CT slices from 10,594 studies of 4,427 unique patients. Each lesion has RECIST measurement marks (long and short diameters) recorded by radiologists during routine clinical workflow ("bookmarks" mined from PACS). Lesion types include lung nodules, liver tumors, lymph nodes, kidney lesions, soft tissue, abdomen, mediastinum, pelvis, and bone. 243 GB on disk.

## Why it matters for training
DeepLesion is the canonical training corpus for "universal lesion detection" because:
- Lesion-type diversity (8 categories spanning the body)
- Real-world label distribution (no curation bias toward specific organs)
- Scale (~33k weakly supervised bounding boxes)
- 2D PNG slabs are friendly to slice-level transformers and lightweight pretraining

Use it for weakly supervised detection pretraining and for building 2D pretrained encoders that transfer to 3D volumetric tasks via MIP / 2.5D windows.

## Access
Tier: open. Primary source: https://nihcc.app.box.com/v/DeepLesion (NIH Box, can be flaky). Mirror via Academic Torrents (243.04 GB, 59 files) at https://academictorrents.com/details/de50f4d4aa3d028944647a56199c07f5fa6030ff .

## Conversion notes
16-bit PNG slices. The metadata CSV (DL_info.csv) gives bbox coords, slice indices, RECIST marks, lesion-type, and patient grouping. NOT 3D NIfTI; you cannot reconstruct full volumes from this release - only the bookmarked slice plus 2-3 neighbors are typically available per lesion. For volumetric work pair with NLST or LIDC-IDRI.

## License
NIH terms; non-commercial research use. No SPDX identifier.

## Citation
Yan K, Wang X, Lu L, Summers RM. "DeepLesion: automated mining of large-scale lesion annotations and universal lesion detection with deep learning." J Med Imaging 5(3):036501 (2018). DOI 10.1117/1.JMI.5.3.036501.

## Gotchas
- 2D, NOT 3D. Repeat: you cannot get full reconstructed CT volumes here.
- NIH Box can stall; prefer the Academic Torrents mirror.
- Lesion bboxes are weak supervision; do not assume tight masks.
