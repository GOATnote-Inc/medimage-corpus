# NIH ChestX-ray14

NIH ChestX-ray14 (Wang et al., CVPR 2017) is the workhorse open chest
radiograph dataset and the foundational large-scale CXR corpus for the
modern era. It contains 112,120 frontal-view PNG chest X-rays from
30,805 unique patients drawn from the NIH Clinical Center PACS.

Each image is multi-labeled across 14 thoracic-disease classes:
atelectasis, cardiomegaly, consolidation, edema, effusion, emphysema,
fibrosis, hernia, infiltration, mass, nodule, pleural_thickening,
pneumonia, pneumothorax. Labels are NLP-mined from the associated
radiology reports with reported accuracy >90%. A subset of ~880 images
is paired with manually drawn bounding boxes for 8 of the 14 classes,
enabling weak-localization research.

Despite the noise inherent in NLP-mined labels, ChestX-ray14 is the
single most-cited open CXR dataset and remains a standard benchmark
for transfer-learning and multi-label classification recipes.

Distribution is exclusively via the NIH Clinical Center's Box folder
(`download_method: nih-box`) at https://nihcc.app.box.com/v/ChestXray-NIHCC.
The dataset ships as 12 image-folder TAR files plus CSV metadata; total
size is approximately 45 GB. Mirror copies exist on Kaggle and Google
Cloud Healthcare API but the NIH Box archive is canonical. Use is
governed by NIH open-access terms (research use; no redistribution).

For VLM training, ChestX-ray14 is unpaired - prefer MIMIC-CXR-JPG or
PadChest. ChestX-ray14 is the pretraining backbone for many open
foundation models and is included in the CheXmask anatomical-mask
overlay (`chexmask`).

Citation: Wang et al., CVPR 2017. DOI:
https://doi.org/10.1109/CVPR.2017.369
