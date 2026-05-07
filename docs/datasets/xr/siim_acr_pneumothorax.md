# SIIM-ACR Pneumothorax Segmentation

The SIIM-ACR Pneumothorax Segmentation challenge (Kaggle 2019) is a
chest-radiograph dataset for pixel-level pneumothorax segmentation. It
was assembled jointly by the Society for Imaging Informatics in
Medicine (SIIM) and the American College of Radiology (ACR). The
released dataset contains 12,047 chest X-rays in DICOM format with
RLE-encoded binary segmentation masks, split into 10,675 training and
1,372 test images. Of the training set, 9,378 images are unannotated
(no pneumothorax) and 2,669 contain at least one labeled pneumothorax
region.

This is one of the highest-quality open pneumothorax benchmarks. It
pairs especially well with CANDID-PTX (19,237 images with
pneumothorax masks AND paired free-text reports) - together the two
datasets cover ~31,000 high-quality pneumothorax images, the largest
open pool available. CANDID-PTX adds report-text supervision for
VLM training; SIIM-ACR adds raw segmentation volume.

For inference benchmarking, top-100 SIIM-ACR Kaggle solutions
typically use U-Net + EfficientNet/ConvNeXt encoders; recent SOTA
relies on Mask2Former + ViT backbones with multi-scale TTA.

Distribution is via Kaggle competitions / Kaggle Datasets
(`download_method: kaggle`) under standard Kaggle competition rules
(research use). Approximate DICOM-format size is ~11 GB. The
community-mirrored `jesperdramsch/siim-acr-pneumothorax-segmentation-data`
dataset is the most reliable current source.

Reference: SIIM Pneumothorax Kaggle Challenge.
https://siim.org/research-journal/siim-machine-learning-challenges/pneumothorax-kaggle-challenge/
