# VinDr-CXR

VinDr-CXR (Vingroup Big Data Institute, 2022) is the de-facto bounding-box
reference dataset for chest-X-ray detection. It contains 18,000
postero-anterior (PA) DICOM scans curated from a starting pool of 100,000
raw images at two Vietnamese hospitals. Annotation rigour is unusually
high for an open corpus: each of the 15,000 training scans was
independently labeled by 3 radiologists, and each of the 3,000 test scans
was labeled by 5-radiologist consensus.

Labels comprise:
- 22 local labels (bounding boxes): aortic enlargement, atelectasis,
  calcification, cardiomegaly, clavicle fracture, consolidation, edema,
  emphysema, enlarged PA, ILD, infiltration, lung cavity, lung cyst,
  lung opacity, mediastinal shift, nodule/mass, pleural effusion,
  pleural thickening, pneumothorax, pulmonary fibrosis, rib fracture,
  other lesion.
- 6 global labels (image-level disease): pneumonia, tuberculosis, COPD,
  lung tumour, other diseases, no_finding.

VinDr-CXR is the standard benchmark for CXR object-detection model
development (DETR / DINO / RT-DETR variants), and is included in the
CheXmask segmentation overlay (`chexmask`).

Access is via PhysioNet under the Credentialed Health Data License 1.5.0;
users must hold a credentialed PhysioNet account, complete CITI training,
and sign the DUA. Approximate full-DICOM size is ~195 GB.

DOI: https://doi.org/10.1038/s41597-022-01498-w
