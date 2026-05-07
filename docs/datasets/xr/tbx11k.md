# TBX11K (Tuberculosis CXR)

TBX11K (Liu et al., CVPR 2020) is the largest open chest-radiograph
dataset with bounding-box annotations for tuberculosis. It contains
11,200 frontal CXRs released by Nankai University and InferVision in
2019/2020. The corpus is split into 6,600 training, 1,800 validation,
and 2,800 test images; the test set is held out via the official
CodaLab challenge for unbiased benchmarking.

The class taxonomy is unusually rich for an open TB dataset:
- Healthy
- Sick but non-TB (other thoracic disease)
- Active TB
- Latent TB (treated or inactive disease)
- Uncertain TB

Each TB-positive image is paired with bounding boxes localizing the TB
region(s), enabling detection-grade research.

For global-health and low-resource-setting models, TBX11K is the
single most useful TB-specific corpus. It complements the older but
still-canonical Shenzhen + Montgomery TB sets (NLM, 800 images) by
providing 14x the volume and adding bounding-box localization. Pairs
naturally with PadChest (which contains many TB-positive cases in
Spanish reports) for multi-source TB pretraining.

Distribution is via the Nankai project page (`download_method: https`)
under a Nankai University research-use license (academic, non-
commercial). Approximate PNG-format size is ~12 GB. Test-set ground
truth remains held back via CodaLab.

Citation: Liu et al., CVPR 2020. DOI:
https://doi.org/10.1109/CVPR42600.2020.00299
