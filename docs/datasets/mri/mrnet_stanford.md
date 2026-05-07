# MRNet Stanford Knee MRI

MRNet is the Stanford knee MRI exam classification dataset containing 1370 knee exams from 1199 patients performed at Stanford University Medical Center. Three orientations (sagittal, coronal, axial) with mixed sequences (T1, T2, PD) are pre-extracted as 2D NumPy slice arrays. Labels are exam-level binary indicators: abnormal (1104 abnormal / 80.6%), ACL tear (319 / 23.3%), meniscal tear (508 / 37.1%), derived through clinical-report parsing.

## Access and tier

Registration via Stanford AIMI Shared Datasets (https://aimi.stanford.edu/datasets/mrnet-knee-mris). Stanford Research Use Agreement.

## Format and download

Native: per-orientation NumPy .npy slice stacks. Recommended: load via the official MRNet starter code with 3-orientation late-fusion architectures. Total dataset 5.67 GB.

## Intended use for this corpus

Exam-level multi-orientation classification (3D-aware via per-slice CNN + temporal aggregation), ACL/meniscus pathology detection, weak-label learning from radiology reports. Note: dataset cannot be redistributed and download links cannot be shared.

## License

Stanford Research Use Agreement; non-commercial.

## Reference

Bien N et al., "Deep-learning-assisted diagnosis for knee magnetic resonance imaging: Development and retrospective validation of MRNet." PLoS Med 15, e1002699 (2018). DOI: 10.1371/journal.pmed.1002699
