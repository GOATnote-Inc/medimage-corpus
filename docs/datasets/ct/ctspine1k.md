# CTSpine1K

## What it is
CTSpine1K is a large-scale spine CT segmentation dataset assembled by aggregating four open-source CT collections and adding consistent vertebral annotations. It contains 1,005 CT volumes with 11,000+ vertebral instances and 500,000+ labeled slices.

Source breakdown: COLONOG (825 scans), HNSCC-3DCT-RT, MSD Task03 Liver (201 cases), and a COVID-19 CT collection (40 scans).

## Why it matters for training
- Largest open spine CT corpus by volume count
- Vertebra-level localization and segmentation
- Mixes abdominal, head-and-neck, and thoracic FOV (good distributional coverage)
- Best paired with VerSe for vertebral fracture / instance work

## Access
Tier: registration. https://github.com/MIRACLE-Center/CTSpine1K . Download links and access conditions on the README. Annotation files distributed via release; original images must be pulled from each source dataset (so license compliance flows through to the original CC-BY / CC-BY-NC-SA terms).

## Conversion notes
NIfTI. Use the published vertebra-class mapping. Some volumes have partial spine coverage (only the spine within FOV is labeled). About 12 GB on disk after assembly; the source images are larger.

## License
CC BY-NC-SA 4.0 (inheriting from upstream sources).

## Citation
Deng Y et al. "CTSpine1K: A Large-scale Dataset for Spinal Vertebrae Segmentation in Computed Tomography." arXiv:2105.14711 (2021). MICCAI 2024 Open Data accepted.

## Gotchas
- Image side must be downloaded from each source (TCIA / MSD / COVID); only annotations are centrally hosted.
- License is the strictest of the upstream sources (CC BY-NC-SA 4.0).
- Heterogeneous FOV; partial volumes are common - normalize before training.
