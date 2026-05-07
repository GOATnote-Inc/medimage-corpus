# BraTS-PEDs (Pediatric Brain Tumor Segmentation)

BraTS-PEDs is the dedicated pediatric brain tumor MRI dataset within the BraTS family, addressing the substantial domain shift between adult and pediatric high-grade gliomas (especially diffuse midline gliomas / DMG). It contains 457 pediatric patients aggregated from major pediatric neuro-oncology consortia, split into 257 training, 91 validation, and 109 testing cases. Each case provides four structural MRI sequences (T1, T1-CE, T2, FLAIR) preprocessed with the standard BraTS pipeline (skull-stripped, co-registered, 1 mm isotropic). Total 32.7 GB.

## Access and tier

Open via TCIA (DOI: 10.7937/dx5c-tj86). IBM Aspera Connect plugin required for Faspex download.

## Format and download

Native: NIfTI (preprocessed). Recommended: NIfTI 4-channel input stack analogous to adult BraTS.

## Intended use for this corpus

Pediatric tumor segmentation; CRITICAL domain-shift benchmark for adult-to-pediatric generalization. Sub-regions include enhancing tumor, tumor core, whole tumor, and cystic component.

## License

CC BY 4.0.

## Reference

Kazerooni AF et al., "The Brain Tumor Segmentation - Pediatrics (BraTS-PEDs) Challenge." TCIA DOI: 10.7937/dx5c-tj86
