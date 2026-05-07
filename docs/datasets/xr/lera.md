# LERA - Lower Extremity Radiographs

LERA (Lower Extremity RAdiographs) is a Stanford Machine Learning Group
musculoskeletal dataset focused on the lower limb. It contains 93,455
radiographic images sourced from 182 unique patients who underwent
imaging at Stanford University Medical Center between 2003 and 2014.
The unusually low patient count for a high image count reflects the
multi-view, multi-time-point nature of orthopaedic follow-up imaging.

Coverage: foot, ankle, knee, and hip - making it the natural
lower-extremity counterpart to MURA (upper extremity) for
musculoskeletal foundation-model pretraining. Each study is annotated
with body part, laterality, and a radiologist-derived diagnostic label
(normal vs abnormal at study level, with finer-grained labels in some
sub-collections).

Distribution is via Stanford AIMI's Azure portal (`download_method:
stanford-aimi`). The license is the Stanford AIMI Research Use
Agreement: viewing and use are granted at no charge for personal,
non-commercial research only. Commercial use, sale, redistribution, or
sharing of download links is prohibited - a tighter license than CBIS-DDSM
or NIH ChestX-ray14.

For training, LERA is most valuable as a pretraining corpus
(self-supervised SimCLR/DINO/MAE), or as auxiliary supervision for
MSK-aware foundation models. For evaluation, the small patient count
limits its statistical power - prefer VinDr-SpineXR or external
extremity benchmarks for headline metrics.

Reference: Stanford AIMI dataset card.
https://aimi.stanford.edu/datasets/lera-lower-extremity-radiographs
