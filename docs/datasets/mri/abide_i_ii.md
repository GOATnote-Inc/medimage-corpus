# ABIDE I + II (Autism Brain Imaging Data Exchange)

The Autism Brain Imaging Data Exchange aggregates structural and resting-state functional MRI from individuals with autism spectrum disorder and typically-developing controls across 24+ international sites. ABIDE I (released 2012) contains 1112 datasets from 539 ASD and 573 controls (ages 7-64); ABIDE II (released 2016-2017) adds 1114 datasets from 521 ASD and 593 controls. Combined, the resource provides 2156 unique cross-sectional datasets. Heterogeneous acquisition protocols across sites make ABIDE the canonical benchmark for cross-site domain generalization in functional neuroimaging.

## Access and tier

Open. Hosted on INDI/NITRC and AWS Open Data S3 (`s3://fcp-indi/data/Projects/ABIDE_Initiative/`). Click-through; some sites require additional Data Use Agreement.

## Format and download

Native: NIfTI. CPAC and other preprocessing pipelines provide derivative versions. Recommended: AWS S3 with `--no-sign-request` for bulk fetch.

## Intended use for this corpus

ASD classification, cross-site domain generalization, resting-state functional connectivity learning, and structural-functional fusion. Site-mixed harmonization (ComBat, etc.) experiments are standard.

## License

Mostly CC-BY-NC-SA-3.0; per-site variation. Cite site-specific publications.

## Reference

Di Martino A et al., "The autism brain imaging data exchange: towards a large-scale evaluation of the intrinsic brain architecture in autism." Mol Psychiatry 19, 659-667 (2014). DOI: 10.1038/mp.2013.78
