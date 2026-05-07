# Medical Segmentation Decathlon - Task 1 BrainTumour

Task 1 of the Medical Segmentation Decathlon is a 484-train / 266-test subset of BraTS 2017 redistributed in standardized NIfTI form. It provides 750 multi-parametric MR cases with four channels (T1, T1-CE, T2, FLAIR) and 3-class tumor sub-region masks (edema, non-enhancing tumor, enhancing tumor). Approximate size 7.7 GB.

## Access and tier

Open via AWS S3 Open Data: `aws s3 cp --no-sign-request s3://msd-for-monai/Task01_BrainTumour.tar .` (us-west-2). EU mirror: `s3://msd-for-monai-eu/`.

## Format and download

Native: NIfTI 4-channel. Recommended: direct .nii.gz read. MONAI provides ready-made loaders.

## Intended use for this corpus

Quick baseline tumor segmentation, MSD multi-task learning experiments, and pretrained-weight initialization (nnU-Net/MedNeXt all ship pretrained MSD weights). Small enough for laptop iteration; large enough for serious benchmarks.

## License

CC BY-SA 4.0.

## Reference

Antonelli M et al., "The Medical Segmentation Decathlon." Nat Commun 13, 4128 (2022). DOI: 10.1038/s41467-022-30695-9
