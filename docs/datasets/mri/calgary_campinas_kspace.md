# Calgary-Campinas Multi-Coil k-space (Reconstruction)

The Calgary-Campinas raw k-space subset provides 167 3D T1-weighted gradient-recalled-echo brain MRI scans (1 mm isotropic sagittal) acquired on a clinical 3T GE Discovery MR750. The dataset is split between 12-channel (117 scans, 70.0%) and 32-channel (50 scans, 30.0%) receiver coils, supporting research on coil-configuration generalization in deep learning reconstruction. Total uncompressed multi-channel volume is approximately 219 GB; an additional single-channel set covers 35 subjects (~8 GB). Subjects are presumed healthy, mean age 44.5 +/- 15.5 years, gender-balanced.

## Access and tier

Open. Hosted on the Canada Open Neuroscience Platform (CONP). Click-through agreement.

## Format and download

Native: HDF5 raw k-space. Companion DICOM/NIfTI image-domain reconstructions provided. Download via CONP portal (https://portal.conp.ca/dataset?id=projects/calgary-campinas).

## Intended use for this corpus

Reconstruction generalization (coil-count, vendor) experiments complementing fastMRI. Used in the Multi-Coil MRI Reconstruction Challenge to assess model robustness to varying coil configurations.

## License

CC BY-ND 4.0 (note: NoDerivatives restricts redistribution of modified versions).

## Reference

Beauferris Y et al., "Multi-Coil MRI Reconstruction Challenge - Assessing Brain MRI Reconstruction Models and Their Generalizability to Varying Coil Configurations." Front Neurosci 16, 919186 (2022). DOI: 10.3389/fnins.2022.919186
