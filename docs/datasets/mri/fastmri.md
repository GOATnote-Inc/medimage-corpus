# fastMRI (NYU): Knee + Brain + Prostate + Breast k-space

fastMRI is the canonical large-scale raw k-space MRI dataset for accelerated reconstruction research, released by NYU Langone in collaboration with Meta AI. The combined corpus is approximately 17 TB across four anatomies: knee (1398 fully-sampled scans + 10,000 clinical DICOMs), brain (7002 fully-sampled scans split across 3012 at 1.5T and 3990 at 3T), prostate (312 patient exams covering 1560 volumes / 47,468 slices in biparametric T2+DWI), and breast (~300 cases with radial DCE-MRI k-space, ~4.5 GB per case). The fastMRI+ extension adds clinical pathology bounding-box annotations on knee and brain. Native format is ISMRMRD/HDF5 raw multi-coil k-space with paired DICOM reconstructions.

## Access and tier

Registration. Sign per-dataset Data Sharing Agreement at fastmri.med.nyu.edu (separate forms for knee, brain, prostate, breast). Access keys are individual and non-redistributable.

## Format and download

Native: ISMRMRD/HDF5 (k-space) + DICOM (image-domain). Recommended: HDF5 raw k-space directly into PyTorch via the official `fastmri` package, with DICOM/NIfTI as paired ground truth.

## Intended use for this corpus

PRIMARY benchmark for unrolled-network reconstruction, parallel-imaging deep learning, and MR physics-aware models. Also useful as a vision-encoder pretraining source and for pathology detection (knee/brain bounding boxes).

## License

fastMRI Data Sharing Agreement (research and education only, non-commercial, non-redistributable).

## Reference

Knoll F et al., "fastMRI: A Publicly Available Raw k-Space and DICOM Dataset of Knee Images for Accelerated MR Image Reconstruction Using Machine Learning." Radiology AI 2 (2020). DOI: 10.1148/ryai.2020190007. Tibrewala R et al., FastMRI Prostate, Sci Data 2024. Solomon E et al., FastMRI Breast, Radiology AI 2024.
