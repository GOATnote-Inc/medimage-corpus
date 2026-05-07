# IXI Dataset (Healthy Brain MRI)

IXI is the most widely cited healthy-control brain MRI dataset, providing nearly 600 healthy adult subjects scanned at three London hospitals (Hammersmith Hospital - Philips 3T; Guy's Hospital - Philips 1.5T; Institute of Psychiatry - GE 1.5T). Each subject has T1, T2, PD-weighted, MRA, and 15-direction diffusion-weighted images. The cross-vendor and cross-field-strength diversity makes IXI a standard for vendor-generalization, harmonization, and registration experiments. It is also the canonical "negative-only" pretraining set when paired with pathology datasets.

## Access and tier

Open. Direct download (no registration) from Imperial College: https://biomedic.doc.ic.ac.uk/brain-development/downloads/IXI/

## Format and download

Native: NIfTI per modality. Recommended: NIfTI as-is. Demographic spreadsheet provided separately.

## Intended use for this corpus

Healthy-brain pretraining for vision encoders, cross-vendor harmonization, registration, and as a negative class for pathology classifiers. The DTI subset (15 directions) is small but useful as a teaching/sanity dataset.

## License

CC BY-SA 3.0.

## Reference

Project page: https://brain-development.org/ixi-dataset/. EPSRC IXI Project (Information eXtraction from Images, GR/S21533/02).
