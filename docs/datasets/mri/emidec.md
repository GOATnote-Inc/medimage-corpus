# EMIDEC (Delayed-Enhancement Cardiac MRI)

EMIDEC is the canonical late-gadolinium-enhancement (LGE) cardiac MRI dataset for myocardial infarction quantification, released for the MICCAI STACOM 2020 workshop. The database contains 150 short-axis LGE MRI exams: 50 normal post-contrast and 100 with myocardial infarction. Each case provides paired manual segmentations of myocardium, infarcted region, and persistent microvascular obstruction (no-reflow zone), plus associated clinical characteristics (demographics, ECG, troponin, etc.).

## Access and tier

Registration via http://emidec.com/.

## Format and download

Native: NIfTI short-axis stacks plus paired CSV clinical features. Recommended: 3D NIfTI segmentation with optional clinical-feature multimodal fusion.

## Intended use for this corpus

Infarct and no-reflow zone segmentation, multimodal MRI+clinical models, MI classification. Critical complement to ACDC: ACDC is cine-based functional, EMIDEC is LGE tissue-characterization.

## License

CC BY-NC-SA 4.0.

## Reference

Lalande A et al., "Emidec: A Database Usable for the Automatic Evaluation of Myocardial Infarction from Delayed-Enhancement Cardiac MRI." Data 5, 89 (2020). DOI: 10.3390/data5040089
