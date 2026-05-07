# HCP Young Adult 1200 (Human Connectome Project)

The Human Connectome Project Young Adult 1200 release is the gold-standard reference dataset for high-quality multimodal MRI in healthy young adults. It contains data from 1206 participants ages 22-35 (including twins and non-twin siblings) collected 2012-2015 at Washington University, with 889 subjects having complete data across all four 3T modalities: structural (T1w MPRAGE, T2w SPACE), resting-state fMRI (4 x 15-min runs at TR=720 ms), task fMRI (7 paradigms), and high-angular-resolution diffusion MRI (3 b-values, 270 directions). A subset of 184 participants additionally has 7T data. Cumulative platform downloads exceed 5400 TB.

## Access and tier

Registration. Sign the HCP Open Access Data Use Terms via ConnectomeDB.

## Format and download

Native: NIfTI, CIFTI, MGZ. Recommended training: preprocessed CIFTI grayordinate or NIfTI volumes from ConnectomeDB. AWS Open Data: `s3://hcp-openaccess/` (requester-pays for 7T).

## Intended use for this corpus

Pretraining vision encoders for high-resolution structural/diffusion brain MRI, connectomics, dMRI reconstruction baselines, and cortical surface modeling. The harmonized HCP protocol is the de-facto reference for new lifespan and development extensions.

## License

HCP Open Access Data Use Terms; restricted-data tier exists for sensitive variables (family structure).

## Reference

Van Essen DC et al., "The WU-Minn Human Connectome Project: an overview." NeuroImage 80, 62-79 (2013). DOI: 10.1016/j.neuroimage.2013.05.041
