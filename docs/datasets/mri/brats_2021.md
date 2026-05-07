# RSNA-ASNR-MICCAI BraTS 2021

The 2021 BraTS challenge is the most-downloaded brain tumor segmentation MRI dataset, jointly organized by RSNA, ASNR, and MICCAI. It comprises 1480 adult glioma cases (originally cited as 2040 across all releases) with four structural mpMRI sequences per case: native T1, post-contrast T1 (T1c), T2, and T2-FLAIR, totaling 407,245 images at 142 GB. Data are pre-processed via the standard BraTS pipeline (co-registered to common anatomical template, isotropic 1 mm resolution, skull-stripped). Tumor sub-region annotations cover enhancing tumor, tumor core, and whole tumor; MGMT promoter methylation status labels are provided for the radiogenomic classification task.

## Access and tier

Open. TCIA hosts the finalized release (DOI: 10.7937/jc8x-9874); Synapse hosts the original challenge data (syn25829067).

## Format and download

Native: NIfTI (already preprocessed). Recommended training: NIfTI 4-channel input stack. Synapse CLI for original; `tcia-cli` for finalized.

## Intended use for this corpus

PRIMARY tumor segmentation pretraining benchmark. Strong baselines exist (nnU-Net, MedNeXt, SwinUNETR). Also supports radiogenomic MGMT classification.

## License

CC BY 4.0.

## Reference

Baid U et al., "The RSNA-ASNR-MICCAI BraTS 2021 Benchmark on Brain Tumor Segmentation and Radiogenomic Classification." arXiv:2107.02314. TCIA DOI: 10.7937/jc8x-9874
