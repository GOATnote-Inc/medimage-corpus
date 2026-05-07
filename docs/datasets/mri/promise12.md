# PROMISE12 (Prostate MR Image Segmentation)

PROMISE12 is the classic prostate segmentation MRI benchmark, organized at MICCAI 2012. It provides 100 transverse T2-weighted MR images split into 50 training cases (with whole-gland masks), 30 test cases, and 20 live-challenge cases. Imaging was contributed by four centers (Haukeland University Hospital, Beth Israel Deaconess, University College London, Radboud University Medical Center) on multiple vendors at 1.5T and 3T, providing modest cross-vendor diversity for early prostate segmentation work.

## Access and tier

Registration via the Grand Challenge platform; Zenodo mirror available (DOI: 10.5281/zenodo.8026660).

## Format and download

Native: MetaImage (.mhd + .raw). Recommended: convert to NIfTI for modern pipelines. SimpleITK reads .mhd directly.

## Intended use for this corpus

Whole-prostate segmentation baseline. Most-cited prostate seg dataset; small enough to use as a finetuning benchmark for foundation models pretrained on PI-CAI.

## License

Citation-required (no formal SPDX). Cite Litjens et al. for any use; results on the test set must be submitted through the official challenge website for any publication.

## Reference

Litjens G et al., "Evaluation of prostate segmentation algorithms for MRI: The PROMISE12 challenge." Med Image Anal 18, 359-373 (2014). DOI: 10.1016/j.media.2013.12.002
