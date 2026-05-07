# SKM-TEA Stanford Knee MRI

SKM-TEA (Stanford Knee MRI Multi-Task Evaluation) is the most comprehensive open knee MRI dataset combining raw k-space, image-domain DICOM, dense tissue segmentations, and pathology bounding boxes from a single clinical population. 155 quantitative double-echo steady-state (qDESS) knee scans were acquired clinically at Stanford, totaling approximately 25,000 slices. Each scan provides raw multi-coil k-space (acquired with 2x1 parallel imaging and elliptical sampling, with missing data estimated by GE ARC), scanner-generated DICOM image-domain reconstructions, manual segmentations of patellar, femoral, and tibial cartilage plus meniscus, and bounding-box annotations for 16 clinically relevant pathologies extracted from radiologist reports. Total dataset size is 1.6 TB.

## Access and tier

Registration via Stanford AIMI Shared Datasets (https://aimi.stanford.edu/datasets/skm-tea-knee-mri). Stanford Research Use Agreement; non-commercial.

## Format and download

Native: HDF5 (raw k-space) + DICOM (image domain) + NIfTI segmentation masks + JSON detection annotations. Use the official `skm-tea` GitHub package for loaders.

## Intended use for this corpus

Multi-task models combining reconstruction, semantic segmentation, and pathology detection on the same scan. Premier benchmark for end-to-end reconstruction-to-clinical-task pipelines on a clinically representative qDESS protocol.

## License

Stanford AIMI Research Use Agreement (non-commercial, registration-gated).

## Reference

Desai AD et al., "SKM-TEA: A Dataset for Accelerated MRI Reconstruction with Dense Image Labels for Quantitative Clinical Evaluation." NeurIPS Datasets and Benchmarks 2021. arXiv:2203.06823
