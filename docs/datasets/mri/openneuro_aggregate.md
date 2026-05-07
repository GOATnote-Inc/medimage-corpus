# OpenNeuro (BIDS aggregate, MRI subset)

OpenNeuro is the de-facto open repository for neuroimaging research data, hosting 1000+ BIDS-validated datasets spanning structural MRI (T1, T2, FLAIR), diffusion (DWI/dMRI), resting-state and task fMRI, ASL, T2*, SWI, plus EEG, MEG, iEEG, and ECoG. Aggregate volume distributed by the platform exceeds 400 TB/year (per the 2021 eLife paper) and the cumulative storage is on the order of 1 PB+ as of 2025. As of October 2021 the catalog contained 604 datasets totaling 20,989 individual participants; the platform deposits new datasets every 4-6 days.

## Access and tier

Open. No registration required for download. Most datasets are CC0; some are CC-BY. Always check per-dataset license in `dataset_description.json`.

## Format and download

Native and recommended: BIDS + NIfTI. Three primary access paths:
1. AWS Open Data S3: `aws s3 ls --no-sign-request s3://openneuro.org/` (us-east-1)
2. DataLad: `datalad install ///openneuro/dsXXXXXX` (best for selective fetch)
3. Web UI direct download per dataset

## Notable large MRI datasets in catalog

- ds000113 (StudyForrest/Forrest Gump fMRI, 7T)
- ds002785 (AOMIC PIOP1: T1, dMRI, rs/task fMRI in 200+ healthy adults)
- ds004215 (NIMH Healthy Research Volunteer Dataset)
- ds002336, ds002338 (large open fMRI studies)
- many MS lesion, glioma, and aging cohorts

## Intended use for this corpus

Vision-encoder pretraining via BIDS-aware loader; downstream task-specific finetuning; reconstruction research with raw-data subsets where available; cross-site domain generalization.

## License

Per-dataset, mostly CC0-1.0 or CC-BY-4.0. Cite OpenNeuro per-dataset DOIs plus Markiewicz et al., eLife 2021. DOI: 10.7554/eLife.71774
