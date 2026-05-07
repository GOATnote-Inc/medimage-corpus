# Open-i / Indiana University Chest X-Rays

The Indiana University Chest X-Ray Collection (typically referenced as
"Open-i" or "IU X-Ray") is one of the longest-standing open paired
image+report CXR datasets and remains the de-facto smaller-scale
benchmark for radiology report generation evaluation. It contains 7,470
frontal or lateral chest X-ray images and 3,955 corresponding
de-identified radiology reports collected by Indiana University.

Each radiology report is structured into four sections that map directly
onto the radiologist's clinical workflow:
- Comparison: prior imaging or examination history.
- Indication: presenting symptoms or reason for examination.
- Findings: enumerated radiological observations.
- Impression: final diagnosis and recommendations.

For each report, multiple paired images may exist (frontal + lateral).
Original images were sourced as raw DICOM and have been classified
manually as frontal vs lateral.

Despite being relatively small, IU X-Ray is the most-cited open report-
generation benchmark in the medical-VLM literature: nearly every
published CXR-VLM (R2Gen, R2GenCMN, M2KT, CvT2DistilGPT2, RaDialog,
CheXagent, MAIRA-2) reports BLEU/METEOR/ROUGE/F1RadGraph scores on
its test split.

Distribution: Open-i hosts metadata and search via NLM
(https://openi.nlm.nih.gov/), but the most reliable bulk download
path is the Academic Torrents image archive
(5a3a439df24931f410fac269b87b050203d9467d) plus the XML reports
torrent (66450ba52ba3f83fbf82ef9c91f2bde0e845aba9). Approximate size
is ~3 GB. Most images are public-domain or PD-equivalent; check
individual record metadata for edge cases.

Reference: Demner-Fushman et al., JAMIA 2016. DOI:
https://doi.org/10.1093/jamia/ocv080
