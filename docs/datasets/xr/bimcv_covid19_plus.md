# BIMCV-COVID19+

BIMCV-COVID19+ is the Valencia Region Image Bank's open dataset of
SARS-CoV-2-positive radiographic and CT studies, released by BIMCV/CIPF
(Spain) starting in 2020 and expanded across three iterations (DOIs:
10.21227/w3aw-rv39 for iters 1+2, 10.21227/f3q6-0986 for iters 1+2+3).
The full release contains 21,342 computed-radiography (CR) studies, 34,829
digital-radiography (DX) studies, and 7,918 chest CT studies from confirmed
COVID-19+ patients, accompanied by Spanish-language radiology reports,
PCR results, IgG/IgM antibody serology, and patient demographics.

Findings are mapped to UMLS terminology in MIDS format (Medical Imaging
Data Structure). 23 images include expert semantic-segmentation overlays
of radiographic findings.

This is one of the largest publicly available paired CXR+report COVID
corpora and the only one with linked PCR and serology - useful for both
VLM pretraining and clinical-context reasoning research. Spanish-language
reports also make it a high-yield multilingual VLM training source
alongside PadChest.

Access requires a research-use application via the BIMCV portal; an
alternate distribution is hosted on IEEE DataPort. Approximate aggregate
size (CR + DX + CT, raw DICOM, all iterations) is ~350 GB; users must
agree not to redistribute or re-identify subjects. The dataset is
combinable with the negative-cohort BIMCV-COVID19- if needed for
balanced classification.

Citation: de la Iglesia Vaya et al., arXiv 2006.01174. https://arxiv.org/abs/2006.01174
