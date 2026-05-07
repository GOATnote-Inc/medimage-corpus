# UK Biobank Imaging Enhancement (Brain + Cardiac + Abdominal MRI)

UK Biobank's imaging study is the largest population MRI dataset on Earth: 100,000 participants have completed multi-organ scanning, with ~20,000 already returning for repeat imaging by end of 2025. Each visit produces over 12,000 MR images per person spanning brain (T1, T2-FLAIR, SWI, dMRI, resting-state and task fMRI), cardiac (cine SSFP, T1/T2 mapping, T2*, parametric mapping, tagging), and abdominal MRI (Dixon, IDEAL, single-shot T2-HASTE), plus DXA, body composition, and carotid ultrasound. The study began in 2014 and is the imaging follow-up to the original UK Biobank cohort of 500,000 prospectively phenotyped adults with linked genomics, EHR, and outcomes.

## Access and tier

Application-tier. Researchers submit a project proposal via UK Biobank's Access Management System (https://bbams.ndph.ox.ac.uk/ams/) under a Material Transfer Agreement. Approval is fee-based and typically takes 6-12 months end-to-end. There is no open-tier subset.

## Format and download

Native: DICOM. UK Biobank ships per-organ NIfTI extracts and IDPs (image-derived phenotypes) processed through the Oxford pipeline (FSL/FreeSurfer/SPM). Bulk download via AMS-issued credentials; total transferred volume per project is typically multi-TB.

## Intended use for this corpus

Primary anchor for vision-encoder pretraining at population scale, biomarker discovery, longitudinal progression modeling, and disease-risk prediction. Genomics linkage permits radiogenomic studies. Largest MRI dataset by an order of magnitude.

## License

UK Biobank custom MTA, per-project; not redistributable. Cite Bycroft et al., Nature 2018 and Littlejohns et al., Nat Commun 2020.

## Reference

Littlejohns TJ et al., "The UK Biobank imaging enhancement of 100,000 participants: rationale, data collection, management and future directions." Nat Commun 11, 2624 (2020). DOI: 10.1038/s41467-020-15948-9
