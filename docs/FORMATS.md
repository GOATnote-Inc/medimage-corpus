# Formats and Conversion Pipelines

This repo is a **registry**: manifests describe upstream datasets; conversion happens on a Brev pod with the converted artifacts kept under `data/` (gitignored).

## Native formats per modality

- **CT (volumetric)** -- DICOM series (one file per slice, `.dcm`); some collections distribute NIfTI (`.nii.gz`) or NRRD already. Voxel spacing is heterogeneous and must be normalized post-load.
- **XR (planar)** -- DICOM (PA/Lateral chest), occasionally PNG/JPEG re-publications (e.g. CheXpert, MIMIC-CXR-JPG). VOI LUT, photometric interpretation, and bit depth vary per source.
- **MRI (volumetric, multi-sequence)** -- DICOM or NIfTI (BraTS, ADNI, fastMRI). Sequence order (T1, T1c, T2, FLAIR) must be tracked explicitly because folder layouts differ.
- **US (video or still)** -- DICOM secondary capture, AVI, or MP4. Many echo datasets ship as cineloops; segmentation labels are PNG masks per frame.
- **Multimodal (image + report)** -- pairs `(.dcm | .png, report.txt | report.json)` plus a structured CSV linking studies to text. MIMIC-CXR ships JPGs + free-text reports + structured labels.

## Recommended training format per task type

| Task                         | Input format on disk          | Loader                |
| ---------------------------- | ----------------------------- | --------------------- |
| CT / MRI segmentation        | NIfTI volumes + NIfTI masks   | MONAI `LoadImaged`    |
| CT / MRI classification      | NIfTI volumes + parquet labels| MONAI / HF `datasets` |
| 3D streaming (large corpora) | WebDataset `.tar` shards      | `webdataset` + PyTorch|
| XR classification            | PNG/JPG + parquet labels      | HF `datasets`         |
| Echo segmentation / function | Frames as JPG + parquet labels| HF `datasets`         |
| Image-to-text (CXR-Report)   | JPG + parquet text columns    | HF `datasets`         |

## Conversion pipelines (this repo)

- `scripts/convert/dicom_to_nifti.py` -- `dcm2niix` first, `pydicom`+`nibabel` fallback. Walks `study/series` directory tree; one volume per `SeriesInstanceUID`.
- `scripts/convert/dicom_to_png.py` -- 2D X-ray; applies VOI LUT and 16->8 bit normalization, optional MONOCHROME1 inversion.
- `scripts/convert/nifti_to_webdataset.py` -- pairs image and label volumes by stem, writes `.tar` shards (~4 GB by default) using `webdataset.ShardWriter`. Each sample contains `image.nii.gz`, optional `label.nii.gz`, and a JSON sidecar.
- `scripts/convert/echo_video_to_frames.py` -- decords videos at a target FPS; `decord` preferred, OpenCV fallback. Outputs `.jpg` (default) or `.npy`.
- `scripts/convert/make_hf_dataset.py` -- indexes a converted directory and emits parquet shards plus a tiny `dataset_info.json` sidecar.

## Sharding strategy

- WebDataset shards: ~4 GB target so each shard fits comfortably on a worker, downloads quickly during dataloader warm-up, and stays well below the 8-10 GB threshold above which extraction stalls hurt iteration time. Smaller for testing (`--shard-size 1`).
- Parquet shards: ~500 MB by default. Parquet encodes labels efficiently and avoids per-file metadata overhead during HF `datasets` scans. Group by modality and split (`train`, `val`, `test`).
- Metadata-only manifests stay in `manifests/*.jsonl` -- never inline anything large into the registry.

## Modality x format matrix (recommended end state)

| Modality | Source        | Convert to       | Distribution   |
| -------- | ------------- | ---------------- | -------------- |
| CT       | DICOM         | NIfTI            | WebDataset tar |
| MRI      | DICOM / NIfTI | NIfTI (BIDS-ish) | WebDataset tar |
| XR       | DICOM / PNG   | PNG (8-bit)      | parquet        |
| US       | DICOM / AVI   | JPG frames       | parquet        |
| Multi    | DICOM + text  | PNG + parquet    | parquet        |

When choosing formats, optimize for **read throughput per training epoch**, not for fidelity to the source -- preserve the source under `_downloads/` (gitignored) and treat `data/` as a derived artifact you can always regenerate.
