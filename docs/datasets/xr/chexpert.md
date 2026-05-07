# CheXpert (Original)

CheXpert (Stanford ML Group, 2019) is a large public chest-radiograph
dataset of 224,316 chest X-rays from 65,240 patients seen at Stanford
Hospital between October 2002 and July 2017. It is the canonical
"uncertainty-label" dataset: each image is labeled along 14 observations
(no_finding, enlarged_cardiomediastinum, cardiomegaly, lung_opacity,
lung_lesion, edema, consolidation, pneumonia, atelectasis, pneumothorax,
pleural_effusion, pleural_other, fracture, support_devices) with values
in {-1 uncertain, 0 negative, 1 positive}, derived by an NLP labeler over
the original radiology reports.

Two scale tiers exist:
- CheXpert-v1.0 (439 GB): full-resolution JPGs and CSV labels.
- CheXpert-v1.0-small (11 GB): 320-pixel downsampled JPGs, 8-bit, ideal
  for fast iteration and CPU-side preprocessing.

CheXpert is hosted on Stanford AIMI's Redivis portal with a research-use
agreement (academic, non-commercial; no redistribution). The Stanford
University School of Medicine retains all rights.

For VLM training, prefer the newer `chexpert_plus` (also Stanford) which
adds the original 187,711 free-text reports, demographics, and 47 DICOM
metadata fields - making it directly comparable to MIMIC-CXR for
report-generation work.

Test-set ground truth is hosted separately at the rajpurkarlab GitHub
repository. The competition has been retired but the leaderboard archive
remains useful for comparing pretraining recipes.

Citation: Irvin et al., AAAI 2019. DOI:
https://doi.org/10.1609/aaai.v33i01.3301590
