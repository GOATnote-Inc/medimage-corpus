# AMOS-MR (Abdominal Multi-Organ Segmentation, MRI subset)

AMOS is a large-scale abdominal multi-organ segmentation benchmark released for the MICCAI 2022 challenge. The MRI subset contains 60 multi-planar, multi-sequence abdominal MRI volumes (T1 and T2 in axial and coronal planes) from a multi-center, multi-vendor patient population, with voxel-level annotations of 15 abdominal organs: spleen, right and left kidneys, gallbladder, esophagus, liver, stomach, aorta, inferior vena cava, pancreas, right and left adrenal glands, duodenum, bladder, and prostate/uterus. AMOS additionally includes 500 CT cases supporting cross-modality CT-to-MR transfer experiments.

## Access and tier

Open via Zenodo (DOI: 10.5281/zenodo.7262581) and the AMOS22 challenge platform.

## Format and download

Native: NIfTI. Recommended: 15-class segmentation training with shared architecture across CT (500 cases) and MRI (60 cases).

## Intended use for this corpus

Multi-organ abdominal MRI segmentation; cross-modality CT->MR transfer experiments; foundation-model evaluation on small-MR-data scenarios.

## License

CC BY 4.0.

## Reference

Ji Y et al., "AMOS: A Large-Scale Abdominal Multi-Organ Benchmark for Versatile Medical Image Segmentation." NeurIPS Datasets and Benchmarks 2022. arXiv:2206.08023.
