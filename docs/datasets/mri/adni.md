# ADNI 1/2/3/4 (Alzheimer's Disease Neuroimaging Initiative)

ADNI is the most-cited Alzheimer's disease longitudinal imaging dataset, now in phase 4 (2022-2027). Cumulative enrollment across phases 1, GO, 2, 3, and 4 exceeds 3500 subjects spanning cognitively normal (CN), mild cognitive impairment (MCI), and Alzheimer's disease (AD), with serial MRI, amyloid PET (PIB, AV45, florbetaben), tau PET (flortaucipir), CSF biomarkers, ApoE genotype, and cognitive assessments. MRI sequences include T1 MPRAGE, T2, FLAIR, DWI, ASL, SWI, and resting-state fMRI on a harmonized 3T protocol with prescribed scanner-specific tuning. Cumulative MRI/PET downloads by qualified researchers exceed 397 million.

## Access and tier

Application-tier. Submit data access request via the LONI IDA archive (https://ida.loni.usc.edu/). Typical approval 1-3 weeks; renewal required annually.

## Format and download

Native: DICOM/NIfTI. Recommended: ADNI-preprocessed NIfTI (gradwarp-corrected, B1-corrected, scaled). Bulk download via IDA web UI (no S3 mirror); per-image curl available via API token.

## Intended use for this corpus

Classification of AD/MCI/CN, longitudinal atrophy modeling, biomarker discovery, and AD-staging vision encoders. Pairs with OASIS-3 for cross-cohort validation.

## License

ADNI Data Use Agreement; results must be returned to ADNI; no redistribution.

## Reference

Petersen RC et al., "Alzheimer's Disease Neuroimaging Initiative (ADNI): clinical characterization." Neurology 74, 201-209 (2010). DOI: 10.1212/WNL.0b013e3181cb3e25
