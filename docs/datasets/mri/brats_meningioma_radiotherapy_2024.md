# BraTS 2024 Meningioma Radiotherapy (BraTS-MEN-RT)

The 2024 BraTS Meningioma Radiotherapy challenge is the first BraTS task targeting radiation therapy planning workflows. 570 contrast-enhanced 3D T1-weighted MRIs were acquired specifically for radiotherapy planning at multiple institutions, retaining native resolutions and orientation (NOT the standard BraTS preprocessing of skull-stripping and template co-registration, which would distort radiation dose planning). 500 cases include expert-annotated gross tumor volume (GTV) segmentations; the remaining 70 are validation. Total approximate size 70 GB.

## Access and tier

Open via Synapse. Sign click-through agreement.

## Format and download

Native: DICOM and NIfTI. Recommended: NIfTI at native resolution (do NOT register to atlas - preserves clinical RT workflow). Synapse CLI for download.

## Intended use for this corpus

Meningioma GTV segmentation, radiotherapy-planning auto-contouring, native-resolution segmentation models that respect clinical-acquisition geometry. Important departure from prior BraTS preprocessing conventions.

## License

CC BY 4.0.

## Reference

LaBella D et al., "The 2024 Brain Tumor Segmentation Challenge Meningioma Radiotherapy (BraTS-MEN-RT) dataset." Sci Data (2026, in press). DOI: 10.1038/s41597-026-06649-x
