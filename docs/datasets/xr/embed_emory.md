# Emory Breast Imaging Dataset (EMBED)

EMBED is a racially diverse mammography dataset released by Emory University,
covering 3.4 million screening and diagnostic mammographic images from
110,000 unique patients across four hospital sites between 2013 and 2020.
The dataset is unique for its enrolled-cohort-level fairness design: it
explicitly oversamples Black women so that Black and White representation is
balanced (~50/50), addressing a well-documented underrepresentation problem
in earlier mammography corpora.

Image content includes 2D full-field digital mammograms (FFDM), synthetic 2D
"C-view" reconstructions, and (in later releases) digital breast
tomosynthesis (DBT), ultrasound, and breast MRI. Roughly 364,000 mammographic
exams are paired with structured BI-RADS assessments, breast density, and
ground-truth pathologic outcomes grouped into six severity classes. ~60,000
lesion-level annotations are linked to ROI descriptors.

The current public release on the AWS Open Data Program is approximately 20%
of the full Emory cohort, hosted in the `embed-dataset-open` S3 bucket
(us-west-2). Access requires registration; a research-use license applies.

For VLM-style breast imaging research, EMBED currently lacks paired
free-text reports - it is structured-label only. Pair with INbreast or
DDSM (CC-BY-3.0) for benchmark eval and with VinDr-Mammo for bounding-box
supervision.

Citation: Jeong et al., Radiology: Artificial Intelligence (2023). DOI:
https://doi.org/10.1148/ryai.220047
