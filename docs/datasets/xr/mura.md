# MURA - Musculoskeletal Radiographs

MURA (Stanford ML Group, 2018) is the canonical large-scale upper-extremity
musculoskeletal-radiograph dataset. It contains 40,561 multi-view
radiographic images from 14,863 imaging studies on 12,173 unique patients,
collected at Stanford Hospital between 2001 and 2012. All images are
in PNG format and total approximately 3.36 GB - small enough to fit
comfortably in memory on a single GPU node.

Anatomic coverage spans seven upper-extremity body parts:
- Elbow
- Finger
- Forearm
- Hand
- Humerus
- Shoulder
- Wrist

Each study is labeled normal (0) or abnormal (1) at the study level by
board-certified radiologists - a relatively coarse-grained but
high-quality label, which supports normal-vs-abnormal binary
classification benchmarking. Test-set ground truth comes from the
consensus of additional board-certified radiologists.

MURA is the standard MSK upper-extremity benchmark and the natural
companion to LERA (lower-extremity radiographs), VinDr-SpineXR
(spine), and the RSNA Pediatric Bone Age dataset. Together they
provide reasonably full musculoskeletal coverage for pretraining a
broad MSK foundation model.

Distribution is via Stanford AIMI / Redivis (`download_method:
stanford-aimi`) under the Stanford ML Group Research Use Agreement
(non-commercial, no redistribution).

Citation: Rajpurkar et al., arXiv 1712.06957. DOI:
https://doi.org/10.48550/arXiv.1712.06957
