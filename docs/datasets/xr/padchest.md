# PadChest

PadChest is a large-scale, high-resolution Spanish chest X-ray dataset
released by Hospital Universitario de San Juan (Alicante, Spain) in
collaboration with BIMCV. It contains 160,868 images from approximately
67,000 patients, covering 109,931 studies acquired between 2009 and 2017.
Each study is paired with a free-text radiology report written by one of 18
radiologists, plus structured labels covering 174 radiographic findings, 19
differential diagnoses, and 104 anatomical locations - hierarchically mapped
to UMLS terminology. Approximately 27% of the dataset was manually annotated
by radiologists; the remainder was labeled by a recurrent neural network
trained on the manual subset (Micro-F1 ~0.93).

PadChest is the second-largest open paired image+report CXR dataset after
MIMIC-CXR, and the only large-scale corpus with reports in Spanish - making
it indispensable for multilingual VLM training and cross-lingual transfer.

Distribution is via 54 zip files totalling approximately 1 TB. Access
requires a research-use application via the BIMCV portal; users must agree
not to redistribute or attempt re-identification.

For applications targeting grounded radiology report generation, the derived
PadChest-GR (`padchest_gr`) subset adds bilingual (EN/ES) bounding-box
findings on 4,555 studies.

DOI: https://doi.org/10.1016/j.media.2020.101797
