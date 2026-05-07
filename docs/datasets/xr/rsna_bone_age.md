# RSNA Pediatric Bone Age Challenge (2017)

The RSNA Pediatric Bone Age Challenge (2017) is the canonical pediatric
hand-radiograph dataset for skeletal-maturity (bone age) regression.
It contains 14,236 left-hand and wrist X-ray images covering
developmental stages from birth to 19 years (0-228 months), with each
image labeled by both numerical bone age (in months) and patient sex.

The standard split is 12,611 training / 1,425 validation / 200 test
images. Imaging modality is conventional plain-film hand radiography
(in PNG form for the Kaggle release).

The challenge produced one of the first widely deployed pediatric AI
models in radiology (16finger / RSNA Pediatric Bone Age 16-Bit) and
remains the standard benchmark for skeletal-maturity-prediction
research. Outside the bone-age regression task, the dataset is also
useful as a pediatric MSK pretraining adjunct: its 14k hand X-rays
add anatomic and demographic diversity that pure adult-focused MSK
datasets (MURA upper extremity, LERA lower extremity) lack.

Distribution is via the RSNA AI Challenge Kaggle dataset
(`download_method: kaggle`), under standard RSNA AI Challenge research-
use license. Approximate PNG-format size is ~11 GB. Multiple
community-curated versions exist on Kaggle (`kmader/rsna-bone-age` is
the most widely cited).

Citation: Halabi et al., Radiology 2018 ("The RSNA Pediatric Bone Age
Machine Learning Challenge"). DOI:
https://doi.org/10.1148/radiol.2018180736
