# MSSEG 2016 (Multiple Sclerosis Segmentation)

MSSEG 2016 is the MICCAI multiple sclerosis lesion segmentation challenge dataset providing 53 patients acquired across 4 different scanners under a harmonized acquisition protocol, with hyperintense lesions delineated on FLAIR by 7 expert raters and consolidated into a consensus segmentation. The dataset includes T1, T2, PD, FLAIR, and post-contrast T1 sequences plus per-expert raw segmentations and the 7-expert consensus. Test data includes scans from a scanner not present in training, supporting cross-scanner generalization assessment.

## Access and tier

Registration via Shanoir-NG (https://shanoir.irisa.fr/shanoir-ng/challenge-request).

## Format and download

Native: NIfTI (raw and preprocessed). Recommended: preprocessed multi-channel NIfTI stack with per-expert masks for inter-rater calibration.

## Intended use for this corpus

MS lesion segmentation; cross-scanner generalization; inter-rater variability modeling (uncertainty-aware models). Premier MS benchmark prior to the larger MSLesSeg.

## License

MSSEG Data Use Agreement; research-only.

## Reference

Commowick O et al., "Multiple sclerosis lesions segmentation from multiple experts: The MICCAI 2016 challenge dataset." NeuroImage 244, 118589 (2021). DOI: 10.1016/j.neuroimage.2021.118589
