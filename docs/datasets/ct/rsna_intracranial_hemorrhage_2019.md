# RSNA Intracranial Hemorrhage Detection 2019

## What it is
The 2019 RSNA Intracranial Hemorrhage Detection challenge corpus is the largest open head-CT classification dataset. It contains 874,035 individual DICOM slices from over 25,000 head CT exams, contributed by Stanford, Thomas Jefferson, Unity Health Toronto, and other sites, annotated by ~60 volunteer neuroradiologists. Each slice is labeled across five hemorrhage subtypes (epidural, subdural, subarachnoid, intraparenchymal, intraventricular) plus a binary "any hemorrhage" label. Stage-2 zipped release is approximately 180 GB.

## Why it matters for training
This is a foundation pretraining corpus for head CT. Use it for:
- Hemorrhage classification / detection (still the gold standard benchmark)
- Head CT 2D / 2.5D pretraining
- Emergency radiology models
- Stroke triage (combine with normal scans here as the "no-acute-bleed" class)

The 5-subtype labels are slice-level, which is rare for head CT.

## Access
Tier: registration. Kaggle competition: https://www.kaggle.com/competitions/rsna-intracranial-hemorrhage-detection . Accept rules. Also mirrored on AWS Open Data: `s3://rsna-intracranial-hemorrhage-detection/`. Use `kaggle competitions download -c rsna-intracranial-hemorrhage-detection` or `aws s3 sync --no-sign-request s3://rsna-intracranial-hemorrhage-detection/ ./`.

## Conversion notes
DICOM slices, single-vendor mix. Re-stack into volumes by SOPInstanceUID + position. Apply standard head CT windowing (brain ~80/40, subdural ~200/80, bone ~2000/600) for multi-channel input.

## License
RSNA Kaggle competition data license; research use only.

## Citation
Flanders AE et al. "Construction of a Machine Learning Dataset through Collaboration: The RSNA 2019 Brain CT Hemorrhage Challenge." Radiology: AI 2:e190211 (2020). DOI 10.1148/ryai.2020190211.

## Gotchas
- Slice-level labels; volume-level reasoning requires aggregation.
- Test set labels embargoed; use only the training set with public ground truth.
- Some slices have invalid pixel data; filter on PixelData length.
