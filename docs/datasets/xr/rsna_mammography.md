# RSNA Screening Mammography Breast Cancer Detection (2023)

The RSNA Screening Mammography Breast Cancer Detection Challenge (Kaggle,
2023) released a large screening-mammography dataset assembled from two
international screening programs (Australia + United States). The corpus
contains just under 20,000 imaging studies (~54,706 individual DICOM
images, typically 4 views per patient: bilateral CC + MLO), with detailed
labels covering radiologist evaluations and pathology-confirmed
malignancy outcomes. BI-RADS assessment, breast density, biopsy result,
and follow-up class are all present.

The challenge attracted 2,146 competitors / 1,687 teams - the largest
RSNA AI challenge participation since 2017. Top solutions used DICOM
JPEG-2000 decoding pipelines (the per-image decompression bottleneck is
the main practical hurdle) followed by ConvNeXt-V2 / EfficientNet-V2
backbones with extreme class imbalance handling (cancer prevalence ~2%).

For VLM training the dataset is structured-label only - no free-text
reports - so it is best used for fine-tuning a mammography classifier or
detector head. It pairs well with EMBED (3.4M-image scale, fairness
balance) and VinDr-Mammo (rigorous radiologist double-read with bbox
ground truth).

Hosted on Kaggle; access requires Kaggle account + competition rules
acceptance (research use). Approximate raw DICOM size is ~314 GB; PNG /
JPEG-256 mirror sets are also community-mirrored on Kaggle Datasets.

Paper: Performance of Algorithms Submitted in the 2023 RSNA Screening
Mammography Breast Cancer Detection AI Challenge. Radiology, 2024.
https://doi.org/10.1148/radiol.241447
