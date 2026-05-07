# CheXmask Database (Anatomical Segmentation)

CheXmask (Gaggion et al., Scientific Data 2024; v1.0.0 PhysioNet release
2025) is a uniform anatomical-segmentation overlay covering 657,566 chest
radiographs drawn from five major public CXR databases:

- ChestX-ray8 (NIH ChestX-ray14)
- CheXpert
- MIMIC-CXR-JPG
- PadChest
- VinDr-CXR

Each segmentation provides three organ contours per image - left lung,
right lung, and heart - encoded as run-length (RLE) masks in CSV format
together with anatomical landmarks and mask dimensions. Segmentations
were produced by HybridGNet, a hybrid CNN+graph-generative model
specifically designed for anatomically-faithful organ contouring. Each
mask is paired with an automated quality score (Dice RCA - Reverse
Classification Accuracy) for QC-driven filtering.

The dataset is uniquely valuable as auxiliary supervision when
pretraining large vision encoders or VLMs: anatomical-mask alignment
losses (e.g. mask-conditioned contrastive learning) substantially
improve organ-localization quality in downstream report generation
and grounding tasks.

License: Creative Commons Attribution 4.0 International - the only
large-scale CXR overlay with a permissive open license, allowing free
redistribution. Hosted on PhysioNet (note: PhysioNet hosting still
requires a credentialed account, but the data itself is CC-BY-4.0 and
can be re-released downstream). Approximate uncompressed size is 37.3
GB; compressed ZIP is 15.6 GB.

DOI: https://doi.org/10.1038/s41597-024-03358-1
