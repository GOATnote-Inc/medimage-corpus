# ACCESS — gating workflows by tier

This document explains how to unlock each access tier for the 127 datasets in the registry. Datasets within a tier follow the same general workflow; per-dataset specifics are in each card.

## Tier summary

| Tier | Count | Typical wait | Typical credentials |
|------|-------|--------------|---------------------|
| open | 57 | Immediate | None (some require email registration) |
| registration | 46 | Minutes-Hours | Account + EULA click-through |
| credentialed | 10 | 1-7 days | CITI human-subjects training + DUA |
| application | 14 | Weeks to months | IRB approval + Data Access Committee |


## Open access

Direct download with no credentials required. Some datasets require an email address to receive the download URL but have no review step. The dispatcher routes these via `https`, `s3`, `aws-open-data`, `tcia-cli`, `hf` (public), `kaggle`, `zenodo`, `nih-box`, or `github-release` depending on host.

**Setup needed:**

- For Kaggle: `pip install kaggle` and place `~/.kaggle/kaggle.json` (download from Kaggle account settings).
- For TCIA: `pip install tcia_utils` (no account required for open collections).
- For Hugging Face public datasets: `pip install huggingface_hub`. Token only needed for higher rate limits.

### Largest in this tier (top 12 of 57)

| Dataset | Modality | Size | Card |
|---------|----------|------|------|
| OpenNeuro (BIDS aggregate, MRI subset) | MRI | 1000.0 TB | [card](datasets/mri/openneuro_aggregate.md) |
| BIOMEDICA (BMCA-CLIP archive) | MULTI | 27.0 TB | [card](datasets/multi/biomedica.md) |
| NLST: National Lung Screening Trial | CT | 11.1 TB | [card](datasets/ct/nlst.md) |
| AAPM Low-Dose CT and Projection Data | CT | 1.3 TB | [card](datasets/ct/aapm_lowdose_ct.md) |
| CT COLONOGRAPHY (ACRIN 6664) | CT | 497 GB | [card](datasets/ct/ct_colonography.md) |
| Duke Breast Cancer MRI (TCIA) | MRI | 396 GB | [card](datasets/mri/duke_breast_cancer_mri.md) |
| PI-CAI Public Training (Prostate Cancer AI) | MRI | 350 GB | [card](datasets/mri/pi_cai_public.md) |
| M4Raw (Low-Field 0.3T Brain k-space) | MRI | 350 GB | [card](datasets/mri/m4raw.md) |
| DeepLesion (NIH) | CT | 243 GB | [card](datasets/ct/deeplesion.md) |
| Calgary-Campinas Multi-Coil k-space (Reconstruction) | MRI | 235 GB | [card](datasets/mri/calgary_campinas_kspace.md) |
| CBIS-DDSM (Curated Breast Imaging Subset of DDSM) | XR | 176 GB | [card](datasets/xr/cbis_ddsm.md) |
| RSNA-ASNR-MICCAI BraTS 2021 | MRI | 152 GB | [card](datasets/mri/brats_2021.md) |


## Registration tier

Account creation + click-through EULA. Most are Stanford AIMI (StanfordPHS@stanford.edu account), NIH Box (free NIH account), HF gated datasets (HF account + accept), or Kaggle competitions (accept rules). Approval is automatic; the EULA may restrict to non-commercial research.

**Setup needed:**

- Stanford AIMI: register at https://stanfordaimi.azurewebsites.net/ and accept dataset-specific EULA before download URL appears.
- HF gated (CT-RATE, MedTrinity-25M, etc.): visit dataset page, click Agree to access, then `export HF_TOKEN=...`.
- NIH Box (DeepLesion, NIH ChestX-ray14): use the official Box folder URL; no per-file auth.
- fastMRI: form at https://fastmri.med.nyu.edu/ — automated email returns S3 URLs.

### Largest in this tier (top 12 of 46)

| Dataset | Modality | Size | Card |
|---------|----------|------|------|
| HCP Young Adult 1200 (Human Connectome Project) | MRI | 80.0 TB | [card](datasets/mri/hcp_young_adult_1200.md) |
| HCP Lifespan (Aging + Development) | MRI | 42.0 TB | [card](datasets/mri/hcp_lifespan_aging_development.md) |
| CT-RATE: Chest CT volumes paired with radiology reports | CT | 21.3 TB | [card](datasets/ct/ct_rate.md) |
| fastMRI (NYU): Knee + Brain + Prostate + Breast k-space | MRI | 17.0 TB | [card](datasets/mri/fastmri.md) |
| OAI (Osteoarthritis Initiative) Knee MRI | MRI | 8.0 TB | [card](datasets/mri/oai_osteoarthritis.md) |
| SKM-TEA Stanford Knee MRI | MRI | 1.7 TB | [card](datasets/mri/skm_tea.md) |
| MedTrinity-25M | MULTI | 1.7 TB | [card](datasets/multi/medtrinity_25m.md) |
| OASIS-3 (Longitudinal Aging/Alzheimer's) | MRI | 1.5 TB | [card](datasets/mri/oasis_3.md) |
| RadGenome-ChestCT | MULTI | 1.3 TB | [card](datasets/multi/radgenome_chestct.md) |
| AbdomenAtlas-8K | CT | 1.2 TB | [card](datasets/ct/abdomenatlas_8k.md) |
| M3D-Cap | MULTI | 1.1 TB | [card](datasets/multi/m3d_cap.md) |
| Emory Breast Imaging Dataset (EMBED) | XR | 1.0 TB | [card](datasets/xr/embed_emory.md) |


## Credentialed tier

PhysioNet credentialed access — required for MIMIC-CXR, MIMIC-CXR-JPG, VinDr-CXR, VinDr-Mammo, VinDr-SpineXR, VinDr-PCXR, CANDID-PTX, BIDMC INSPECT, etc. Workflow:

1. Create PhysioNet account: https://physionet.org/register/
2. Complete CITI Program training (`Data or Specimens Only Research`) — about 4 hours. Submit completion certificate.
3. For each dataset: visit the dataset page, accept the Data Use Agreement (DUA). Approval typically same-day to 1 week.
4. Set env vars: `PHYSIONET_USER` and `PHYSIONET_PASSWORD`. The dispatcher (`_physionet.sh`) reads them and never echoes them.

**Hard rule:** never paste the password into a shell whose output is captured by an agent or transcript. Use a `.env` file loaded with `set -a && source .env && set +a` and confirm the variable is set without printing its value (`test -n "$PHYSIONET_PASSWORD" && echo set`) before running.

### Largest in this tier (top 10 of 10)

| Dataset | Modality | Size | Card |
|---------|----------|------|------|
| MIMIC-CXR Database | XR | 4.7 TB | [card](datasets/xr/mimic_cxr.md) |
| MIMIC-CXR-JPG | XR | 558 GB | [card](datasets/xr/mimic_cxr_jpg.md) |
| AutoPET-III (FDG + PSMA PET/CT) | CT | 419 GB | [card](datasets/ct/autopet_iii.md) |
| VinDr-Mammo | XR | 350 GB | [card](datasets/xr/vindr_mammo.md) |
| VinDr-CXR | XR | 195 GB | [card](datasets/xr/vindr_cxr.md) |
| VinDr-SpineXR | XR | 80 GB | [card](datasets/xr/vindr_spinexr.md) |
| BRAX (Brazilian labeled chest X-ray dataset) | XR | 60 GB | [card](datasets/xr/brax.md) |
| CheXmask Database (Anatomical Segmentation) | XR | 40 GB | [card](datasets/xr/chexmask.md) |
| VinDr-PCXR (Pediatric Chest X-Ray) | XR | 30 GB | [card](datasets/xr/vindr_pcxr.md) |
| MIMIC-Ext-MIMIC-CXR-VQA | XR | 3 GB | [card](datasets/xr/mimic_cxr_vqa.md) |


## Application tier

Full data-access-committee review required. These datasets are massive but you must demonstrate research need and (often) institutional sponsorship. Plan for weeks-to-months wait. Listed in size order:

Per-dataset paths:

- **UK Biobank** (~6 PB): apply at https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access — ~3-6 month review, project fee.
- **ADNI** (~50 TB): https://adni.loni.usc.edu/data-samples/access-data/ — typically 4-8 weeks.
- **ABCD** (~80 TB): https://nda.nih.gov/abcd — NIH NDA account + DUA + Data Access Committee review (~6-12 weeks).
- **NLST** (CT, ~11 TB): https://cdas.cancer.gov/nlst/ — fee + review (~4-12 weeks).
- **PadChest, BIMCV-COVID19+, INSPECT**: institutional Data Use Agreement plus IRB.

### Largest in this tier (top 12 of 14)

| Dataset | Modality | Size | Card |
|---------|----------|------|------|
| UK Biobank Imaging Enhancement (Brain + Cardiac + Abdominal MRI) | MRI | 6000.0 TB | [card](datasets/mri/uk_biobank_imaging.md) |
| ABCD Study (Adolescent Brain Cognitive Development) | MRI | 80.0 TB | [card](datasets/mri/abcd_study.md) |
| ADNI 1/2/3/4 (Alzheimer's Disease Neuroimaging Initiative) | MRI | 50.0 TB | [card](datasets/mri/adni.md) |
| INSPECT (Stanford CT-PA + EHR) | MULTI | 1.5 TB | [card](datasets/multi/inspect.md) |
| PadChest | XR | 1.0 TB | [card](datasets/xr/padchest.md) |
| BIMCV-COVID19+ | XR | 350 GB | [card](datasets/xr/bimcv_covid19_plus.md) |
| MedICaT | MULTI | 104 GB | [card](datasets/multi/medicat.md) |
| STOIC2021 COVID-19 CT | CT | 50 GB | [card](datasets/ct/stoic2021.md) |
| CANDID-PTX (Pneumothorax) | XR | 28 GB | [card](datasets/xr/candid_ptx.md) |
| PadChest-GR (Grounded Report Generation) | XR | 5 GB | [card](datasets/xr/padchest_gr.md) |
| Shenzhen + Montgomery TB CXR Sets (NLM) | XR | 4 GB | [card](datasets/xr/shenzhen_montgomery_tb.md) |
| RVENet (Right Ventricular Echocardiography) | US | 2 GB | [card](datasets/us/rvenet.md) |

