# ACDC (Automated Cardiac Diagnosis Challenge)

ACDC is the most-cited cardiac MRI segmentation and classification benchmark, organized at MICCAI 2017. The dataset contains 150 cine SSFP exams from 5 evenly-distributed groups (30 patients each): healthy, dilated cardiomyopathy, hypertrophic cardiomyopathy, myocardial infarction, and abnormal right ventricle. End-diastolic and end-systolic phases are manually annotated for left ventricle (LV), myocardium (Myo), and right ventricle (RV). Train: 100 cases; test: 50 cases.

## Access and tier

Registration via INSA Lyon (https://www.creatis.insa-lyon.fr/Challenge/acdc/databases.html) and the HumanHeart Project. Click-through; citation required.

## Format and download

Native: NIfTI 4D cine sequences with ED/ES phase indicators. Recommended: 2D-per-slice or 3D segmentation; 5-class classification head.

## Intended use for this corpus

Cardiac multi-structure segmentation baseline; pathology classification (5 groups). Strong nnU-Net baseline available; ideal foundation-model finetuning target.

## License

Citation-required (no formal SPDX). Cite Bernard et al. 2018.

## Reference

Bernard O et al., "Deep Learning Techniques for Automatic MRI Cardiac Multi-Structures Segmentation and Diagnosis: Is the Problem Solved?" IEEE Trans Med Imaging 37, 2514-2525 (2018). DOI: 10.1109/TMI.2018.2837502
