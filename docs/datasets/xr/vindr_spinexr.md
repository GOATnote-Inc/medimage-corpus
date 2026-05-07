# VinDr-SpineXR

VinDr-SpineXR (Vingroup Big Data Institute, 2021) is the largest open
spine X-ray dataset with detection-grade lesion annotations. It contains
10,466 spine X-ray images derived from 5,000 imaging studies at a
Vietnamese hospital, split into 8,389 training images (4,000 studies)
and 2,077 test images (1,000 studies).

Each lesion instance is annotated with:
- A category from 13 spinal-abnormality types: osteophytes, disc-space
  narrowing, surgical implants, foraminal stenosis, spondylolisthesis,
  vertebral collapse, other lesion, and others.
- A bounding box (4-edge rectangle) localizing the lesion in the
  original DICOM coordinate space.

VinDr-SpineXR was the most comprehensive musculoskeletal radiograph
dataset at the time of publication and remains the leading benchmark
for spine-region detection. It is the natural MSK companion to MURA
(upper-extremity classification), LERA (lower-extremity classification)
and VinDr-CXR (chest-region detection) when building broad
musculoskeletal foundation models.

Hosted on PhysioNet under the Restricted Health Data License 1.5.0 -
any registered user can download after signing the DUA (no CITI
training required). Approximate full-DICOM size is ~80 GB.

Paper: Pham et al., MICCAI 2021. DOI:
https://doi.org/10.1007/978-3-030-87240-3_28
