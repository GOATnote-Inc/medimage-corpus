# ISLES 2022 (Ischemic Stroke Lesion Segmentation)

ISLES 2022 is the modern multi-center MRI stroke lesion segmentation benchmark, containing 400 acute-to-subacute stroke MRI cases split 250 training / 150 hidden test. Each case provides three sequences: FLAIR, diffusion-weighted imaging (DWI, b=1000), and the corresponding apparent diffusion coefficient (ADC) map. Training data was acquired at TUM Munich (Philips Achieva and Ingenia 3T) and University of Bern (Siemens Verio 3T); test data adds a third site for cross-site generalization assessment.

## Access and tier

Open. Training data publicly available on Zenodo (CC BY 4.0); test set held out for challenge.

## Format and download

Native: NIfTI. Recommended: 3-channel input stack (FLAIR + DWI + ADC). Direct download from Zenodo (DOI: 10.5281/zenodo.7153326).

## Intended use for this corpus

Acute stroke lesion segmentation using clinical diffusion sequences (most relevant for hyperacute stroke). Companion to ATLAS (which uses chronic-phase T1).

## License

CC BY 4.0.

## Reference

Hernandez Petzsche MR et al., "ISLES 2022: A multi-center magnetic resonance imaging stroke lesion segmentation dataset." Sci Data 9, 762 (2022). DOI: 10.1038/s41597-022-01875-5
