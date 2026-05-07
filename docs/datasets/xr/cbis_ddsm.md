# CBIS-DDSM (Curated Breast Imaging Subset of DDSM)

CBIS-DDSM (Lee et al., 2017) is the curated, DICOM-converted, standardized
update of the original Digital Database for Screening Mammography (DDSM).
It contains 10,239 mammographic images from 1,566 unique participants
(note that some patients appear under multiple patient IDs in DICOM
metadata, yielding the often-cited 6,671 figure). Total volume is 163.5 GB.

Annotations include 753 calcification cases and 891 mass cases, all with
pathology-confirmed ground truth (benign vs malignant) and pixel-level
ROI segmentation masks. BI-RADS assessment, density, subtlety, and
abnormality type are recorded.

CBIS-DDSM is the open-license bedrock of mammography research: the
data is released under Creative Commons Attribution 3.0 (CC-BY-3.0),
making it one of the very few clinical imaging corpora that can be
freely redistributed and incorporated into derivative works (e.g. for
pretraining checkpoints intended for open release). This makes it
especially valuable for vendor-neutral foundation-model training.

Hosted on The Cancer Imaging Archive (TCIA) at Wake Forest; access via
the TCIA Aspera or NBIA Data Retriever clients (`download_method:
tcia-cli`). All DICOMs are decompressed from the original lossless
JPEG (LJPEG) DDSM files into standard DICOM with CC-BY-3.0 license.

Pair with VinDr-Mammo (rigorous bbox), INbreast (small but
histologically-confirmed reference), and EMBED (large-scale,
fairness-balanced) for full mammography task coverage.

DOI: https://doi.org/10.1038/sdata.2017.177
