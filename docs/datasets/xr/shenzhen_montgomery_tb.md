# Shenzhen + Montgomery TB CXR Sets (NLM)

The U.S. National Library of Medicine (NLM) released two postero-anterior
chest-radiograph datasets specifically for tuberculosis screening
research: the Montgomery County (MC) set and the Shenzhen Hospital set.
Although small by modern standards, they are the canonical open TB
benchmarks and remain widely cited.

Montgomery County (MC):
- 138 PA chest radiographs (80 normal, 58 abnormal/TB).
- Provided in 12-bit grayscale PNG (4020x4892 or 4892x4020 pixel
  matrix; 0.0875 mm pixel spacing). DICOM available on request.
- Includes left + right lung segmentation masks.

Shenzhen Hospital:
- 662 frontal chest X-rays (326 normal, 336 TB).
- Provided in 12-bit grayscale PNG. DICOM available on request.
- Clinical readings include gender, age, lung status (per image).

Combined: 800 paired chest X-rays from two distinct populations (US
county vs Chinese hospital), enabling cross-population TB-detection
evaluation. The Montgomery lung masks are uniquely valuable as a
small, well-curated lung-segmentation reference set.

Distribution is via the NLM Lister Hill HTTP server
(`download_method: https`); requesters must contact NLM via the
listed contact webpage and agree not to redistribute. The license
permits use within the requesting research group only.

For modern-scale TB research, prefer TBX11K (11,200 images with
bbox annotations) as the primary benchmark; reserve Shenzhen +
Montgomery for cross-population generalization checks and lung-
segmentation baselines.

Citation: Jaeger et al., Quantitative Imaging in Medicine and
Surgery 2014. DOI:
https://doi.org/10.3978/j.issn.2223-4292.2014.11.20
