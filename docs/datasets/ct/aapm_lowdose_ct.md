# AAPM Low-Dose CT and Projection Data

## What it is
The AAPM Low-Dose CT and Projection Data collection on TCIA provides paired full-dose / quarter-dose CT scans alongside the raw projection (sinogram) data, an exceptionally rare resource. It expanded the original 2016 AAPM Low Dose CT Grand Challenge dataset (30 contrast-enhanced abdominal cases) into a 1.3 TB corpus covering chest, abdomen, and head sites.

## Why it matters for training
This is the canonical training and benchmarking corpus for low-dose CT reconstruction, denoising, and dose-aware pretraining. Because raw projection data is bundled, you can:
- Train iterative reconstruction networks (LEARN, FBPConvNet, model-based).
- Build dose-conditional generative priors.
- Run sinogram-domain transformers.
- Pretrain general CT encoders that are dose-agnostic.

## Access
Tier: open for chest and abdomen (CC BY 4.0). Head cases are gated under the NIH Controlled Data Access Policy due to facial-reconstruction concerns. Visit https://www.cancerimagingarchive.net/collection/ldct-and-projection-data/ and pull via the TCIA Data Retriever / `tcia-cli`.

## Conversion notes
Sinograms are DICOM-CT-PD (protected, vendor-specific). Mayo provides an open conversion library. Reconstructed images are standard DICOM. Convert images to NIfTI (dcm2niix); keep sinograms in their native format and write a custom dataloader.

## License
CC BY 4.0 (chest, abdomen). NIH Controlled (head).

## Citation
McCollough CH et al. "Data from Low Dose CT Image and Projection Data" (LDCT-and-Projection-data) [data set]. The Cancer Imaging Archive (2020). DOI 10.7937/9NPB-2637. Original Grand Challenge: McCollough et al. Med Phys 44(10) (2017).

## Gotchas
- Raw projection data is huge and vendor-format; budget conversion engineering time.
- Head cases require NIH application (extra weeks).
- Pairing of full-dose to simulated quarter-dose is per-case; verify metadata before training.
