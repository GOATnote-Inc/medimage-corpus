# Open-i / IU CXR (Indiana University)

**Year:** 2016 | **Paper:** [Demner-Fushman et al. 2016 (JAMIA)](https://doi.org/10.1093/jamia/ocv080)
**Access:** open (NLM Open-i; Kaggle mirror most accessible) | **License:** CC-BY-NC-ND-4.0

## Summary

The Indiana University (IU) Chest X-ray collection, distributed via the National Library of Medicine's Open-i image search, comprises 7,470 frontal and lateral chest radiograph images paired with 3,955 corresponding free-text radiology reports. Each report contains four standardized sections: Comparison (prior patient information), Indication (symptoms or reason for examination), Findings (radiological observations), and Impression (final diagnosis). IU-XRay is one of the earliest and most-cited public chest X-ray report-generation benchmarks and remains a standard held-out evaluation set despite its small size.

## Image modality

Chest radiograph (XR), frontal (PA / AP) and lateral views.

## Text type

Free-text radiology reports with four standardized sections (Comparison / Indication / Findings / Impression). Multiple images per report (typically 2 - frontal + lateral).

## Size

~4 GB (PNG distribution; original DICOM somewhat larger).

## Access

Open download via the NLM Open-i interface; the Kaggle mirror is the most convenient distribution for ML use. Distribution under CC-BY-NC-ND-4.0 (non-commercial, no derivatives).

## Notes for VLM training

Indexed in the modality-specific manifest as `xr/iu_xray`; dedup target id: `xr/iu_xray`. Use as test/eval rather than train for report-generation models because of its small size and standardized section structure. The combination of structured sections + paired views is well-suited for evaluating model capability on producing well-formed clinical reports rather than just chest-finding labels.
