# PI-CAI Public Training (Prostate Cancer AI)

PI-CAI is the largest open prostate cancer MRI challenge dataset to date. The public training set comprises 1500 anonymized biparametric MRI exams from 1476 patients acquired 2012-2021 across three Dutch centers (Radboud UMC, UMC Groningen, ZGT Twente). Each case contains T2-weighted, diffusion-weighted (high b-value), and apparent diffusion coefficient (ADC) sequences. csPCa lesion delineations are available for 1295 of 1500 cases (86%), with case-level csPCa labels and Gleason scores derived from histopathology and >=3-year follow-up. The full PI-CAI ecosystem includes ~9000 training cases (1500 public), ~100 validation cases, and ~1000 hidden test cases.

## Access and tier

Open (public training set). Hosted on Zenodo; sign click-through agreement.

## Format and download

Native: MHA / NIfTI. Recommended: 3-channel NIfTI biparametric stack (T2 + DWI + ADC). Lesion labels in MHA. Use the picai_eval and picai_baseline GitHub repositories for loaders.

## Intended use for this corpus

PRIMARY benchmark for prostate-cancer detection and segmentation. csPCa classification, lesion segmentation, biparametric end-to-end pipelines. Note bpMRI only - no DCE.

## License

CC BY-NC 4.0. Research-only.

## Reference

Saha A et al., "The PI-CAI Challenge: Public Training and Development Dataset." Zenodo (2022). DOI: 10.5281/zenodo.6517398
