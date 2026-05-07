# STOIC2021 COVID-19 CT

## What it is
STOIC2021 is the largest open COVID-19 chest CT corpus. It contains 10,735 chest CT scans from suspected SARS-CoV-2 patients collected during the wave-1 French outbreak (March-April 2020). Each scan has an associated PCR result (positive / negative) and a severity outcome label (intubation or death within 30 days).

The qualification (training) set comprises 2,000 scans; the test set is 1,000. The full 10,735-scan corpus is available under a data-use agreement.

## Why it matters for training
- Largest open COVID-CT corpus
- Severity / outcome labels (rare, clinically actionable)
- Real-world wave-1 data with diverse acquisition
- Useful as a chest CT pretraining base when paired with non-COVID corpora

Use for COVID severity prediction benchmarks, chest CT pretraining (especially for ground-glass opacity recognition), and combined with NLST + LIDC for a balanced lung CT stack.

## Access
Tier: application. Public sample (qualification set) is downloadable under CC BY-NC 4.0 from https://stoic2021.grand-challenge.org/ . Full 10,735-scan release requires a signed data-use agreement.

## Conversion notes
DICOM in original release. Public sample is also available as MHA. Voxel spacing varies; resample to 1.5x1.5x1.5 mm for SSL pretraining.

## License
CC BY-NC 4.0 (public sample); custom DUA for full set.

## Citation
Revel MP et al. "Study of Thoracic CT in COVID-19: The STOIC project." Radiology 301:E361-E370 (2021). DOI 10.1148/radiol.2021210384.

## Gotchas
- French data; metadata fields may include French strings.
- Wave-1 cohort is severity-skewed (more sick patients); not representative of all COVID presentations.
- Imaging size ~50 GB estimated; confirm before pulling.
