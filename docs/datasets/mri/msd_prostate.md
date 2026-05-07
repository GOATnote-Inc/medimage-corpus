# Medical Decathlon Task05 Prostate MRI

Task 5 of the Medical Segmentation Decathlon is a small but well-curated prostate MRI segmentation set covering 48 multi-parametric MRI studies (T2 + ADC stacks). Annotations distinguish two anatomical zones: peripheral zone and transition zone. Total package size approximately 230 MB.

## Access and tier

Open via AWS Open Data S3: `aws s3 cp --no-sign-request s3://msd-for-monai/Task05_Prostate.tar .` (us-west-2). EU mirror: `s3://msd-for-monai-eu/`.

## Format and download

Native: NIfTI 2-channel (T2 + ADC) input.

## Intended use for this corpus

Sanity-check baseline for prostate-zone segmentation, MSD multi-task pretraining. Foundation-model finetuning target with very small data; pairs naturally with PI-CAI for full csPCa workflow.

## License

CC BY-SA 4.0.

## Reference

Antonelli M et al., "The Medical Segmentation Decathlon." Nat Commun 13, 4128 (2022). DOI: 10.1038/s41467-022-30695-9
