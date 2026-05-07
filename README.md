# medimage-corpus

A registry of large open-source medical imaging datasets for training vision and vision-language models. This repo holds the **manifests, dataset cards, download dispatchers, and format converters** — actual data downloads run on H100/H200 pods (or any storage host with enough disk and bandwidth).

## What is in here

- **134 datasets** cataloged across CT, X-ray, MRI, ultrasound, and image-text paired (VLM) collections.
- **~7.4 PB** of imaging data across all entries (heavily skewed by application-tier datasets — UK Biobank ~6 PB, OpenNeuro ~1 PB).
- **~700 TB** of openly accessible or registration-tier data realistically pullable to a single pod over time.
- One JSON Schema (`schemas/dataset.schema.json`) that every manifest line conforms to.
- One dispatcher (`scripts/download/get.sh`) that routes to the right download tool by `download_method`.
- Five conversion scripts: DICOM to NIfTI, NIfTI to WebDataset shards, DICOM to PNG, echo video to frames, and a HuggingFace dataset wrapper.
- 134 markdown dataset cards under `docs/datasets/<modality>/<id>.md`.

## Per-modality breakdown

| Modality          | Count | Size (sized only) | Notes                                                                           |
|-------------------|-------|-------------------|---------------------------------------------------------------------------------|
| CT                | 25    | 38.2 TB           | Largest: CT-RATE 21.3 TB (paired with reports), NLST 11 TB                      |
| X-ray             | 28    | 9.9 TB            | Largest: MIMIC-CXR 4.7 TB, PadChest 1 TB, EMBED ~1 TB                           |
| MRI               | 35    | 7.28 PB           | Largest: UK Biobank ~6 PB (gated), OpenNeuro ~1 PB, ABCD 80 TB, HCP 80 TB       |
| Ultrasound        | 23    | 144 GB            | Largest: EchoNet-LVH ~75 GB, ACOUSLIC-AI ~38 GB                                 |
| Multimodal (VLM)  | 23    | 61.5 TB           | Largest: BIOMEDICA 27 TB, RadFM-MedMD 15 TB, CT-RATE 21.3 TB (also in CT)       |

## Repo layout

```
medimage-corpus/
├── README.md
├── CLAUDE.md                       # Operating notes for Claude Code sessions in this repo
├── pyproject.toml                  # Python deps (convert / download / dev groups)
├── schemas/
│   └── dataset.schema.json         # JSON Schema 2020-12 — canonical manifest contract
├── manifests/
│   ├── ct.jsonl                    # 25 CT entries
│   ├── xr.jsonl                    # 28 X-ray entries
│   ├── mri.jsonl                   # 35 MRI entries
│   ├── us.jsonl                    # 23 ultrasound entries
│   ├── multimodal.jsonl            # 23 VLM-paired entries
│   └── all.jsonl                   # Aggregated, sorted DESC by size_bytes
├── docs/
│   ├── ACCESS.md                   # Per-tier gating workflows
│   ├── FORMATS.md                  # Native vs training formats, sharding strategies
│   ├── DEPLOY_BREV.md              # How to run downloads on Brev pods
│   └── datasets/<modality>/<id>.md # Per-dataset cards (134 total)
├── scripts/
│   ├── download/get.sh             # Dispatcher; routes by download_method
│   ├── download/_https.sh          # curl wrapper
│   ├── download/_s3.sh             # aws s3 cp wrapper (handles Open Data)
│   ├── download/_hf.py             # huggingface_hub.snapshot_download
│   ├── download/_kaggle.sh         # kaggle datasets/competitions
│   ├── download/_tcia.py           # TCIA collections
│   ├── download/_physionet.sh      # wget with PhysioNet creds (env-loaded)
│   ├── download/_synapse.py        # synapseclient (BraTS-style)
│   ├── download/_openneuro.sh      # OpenNeuro AWS Open Data
│   ├── convert/dicom_to_nifti.py
│   ├── convert/nifti_to_webdataset.py
│   ├── convert/dicom_to_png.py
│   ├── convert/echo_video_to_frames.py
│   ├── convert/make_hf_dataset.py
│   ├── manifest/aggregate.py
│   ├── manifest/validate.py
│   ├── manifest/stats.py
│   └── train_loaders/{webdataset_loader,hf_loader}.py
└── .github/workflows/manifest-validate.yml
```

## Quick start

Install deps once on the pod where you will pull data:

```bash
pip install -e ".[convert,download]"
```

List a specific dataset's manifest entry:

```bash
python3 -c "
import json
for line in open('manifests/all.jsonl'):
    r = json.loads(line)
    if r['id'] == 'lidc_idri':
        print(json.dumps(r, indent=2))
        break
"
```

Download (dispatcher uses the manifest's `download_method`):

```bash
# Dry run first — confirms how it will dispatch
bash scripts/download/get.sh ct/lidc_idri --dry-run

# Actual pull (default target: ./data/<modality>/<id>/)
bash scripts/download/get.sh ct/lidc_idri --target /workspace/data/ct/lidc_idri
```

For credentialed datasets, set the appropriate env vars first (never paste them into a shell that gets transcribed — see `docs/ACCESS.md`):

```bash
# PhysioNet (MIMIC-CXR, VinDr family, etc.)
export PHYSIONET_USER=...
export PHYSIONET_PASSWORD=...

# Hugging Face (CT-RATE, MedTrinity-25M, BIOMEDICA, etc.)
export HF_TOKEN=...

# Kaggle
export KAGGLE_USERNAME=...
export KAGGLE_KEY=...
```

## Convert and shard for training

```bash
# DICOM volume tree -> NIfTI
python3 scripts/convert/dicom_to_nifti.py \
  --in /workspace/data/ct/lidc_idri/raw \
  --out /workspace/data/ct/lidc_idri/nifti

# NIfTI directory -> WebDataset .tar shards (good for distributed pretraining)
python3 scripts/convert/nifti_to_webdataset.py \
  --in /workspace/data/ct/lidc_idri/nifti \
  --out /workspace/data/ct/lidc_idri/wds \
  --shard-size 4

# 2D X-ray DICOM -> PNG with VOI LUT applied
python3 scripts/convert/dicom_to_png.py \
  --in /workspace/data/xr/mimic_cxr/raw \
  --out /workspace/data/xr/mimic_cxr/png \
  --voi-lut --normalize

# Echo videos -> frames
python3 scripts/convert/echo_video_to_frames.py \
  --in /workspace/data/us/echonet_dynamic/Videos \
  --out /workspace/data/us/echonet_dynamic/frames \
  --fps 10
```

## Access tiers (summary — full detail in `docs/ACCESS.md`)

| Tier          | Count | Friction                                                                |
|---------------|-------|-------------------------------------------------------------------------|
| open          | 57    | Direct download.                                                        |
| registration  | 47    | Account + EULA click-through (Stanford AIMI, NIH Box, Kaggle, HF gated) |
| credentialed  | 13    | PhysioNet credentialed: CITI training + DUA. Approved in days.          |
| application   | 17    | IRB / data access committee (UK Biobank, ADNI, ABCD, NLST). Weeks/mos.  |

## Top 10 datasets by size

(Note: MRI top entries are estimates — UK Biobank, OpenNeuro, ABCD do not publish single canonical byte totals.)

1. UK Biobank Imaging — ~6 PB — application
2. OpenNeuro aggregate — ~1 PB — open (S3 Open Data)
3. ABCD Study — ~80 TB — application
4. HCP Young Adult 1200 — ~80 TB — registration
5. ADNI — ~50 TB — application
6. HCP Lifespan (Aging + Development) — ~42 TB — registration
7. BIOMEDICA — 27 TB — open
8. CT-RATE — 21.3 TB — registration (HF gated)
9. fastMRI — 17 TB — registration
10. RadFM MedMD — 15 TB — registration

## Validation

```bash
# Re-aggregate from per-modality manifests, sort by size, validate against schema
python3 scripts/manifest/aggregate.py
python3 scripts/manifest/validate.py manifests/all.jsonl
python3 scripts/manifest/stats.py --by tier --top 20
```

CI workflow at `.github/workflows/manifest-validate.yml` runs the same on push.

## How sizes were derived

For most entries, sizes come from official dataset landing pages, accompanying papers, or the dataset's S3 bucket listing (where public). Where authoritative numbers are unavailable, manifests record `null` rather than a guess; where order-of-magnitude estimates were the best signal (UK Biobank, OpenNeuro aggregate, ABCD, ADNI), the `size_human` field uses a `~` prefix and the `agent_notes` flag the estimate. **Re-measure before final storage planning** — these inform first-cut budgeting, not contracts.

## Adding a dataset

1. Edit the relevant `manifests/<modality>.jsonl` — add one line conforming to `schemas/dataset.schema.json`.
2. Add a card at `docs/datasets/<modality>/<id>.md`.
3. Run `python3 scripts/manifest/aggregate.py` to refresh `manifests/all.jsonl`.
4. Run `python3 scripts/manifest/validate.py manifests/all.jsonl`.
5. Commit. CI re-validates on push.

## Provenance

Built 2026-05-06 by a six-team multi-agent dispatch (CT, XR, MRI, US, VLM, format) under Claude Code. Each agent verified URLs and license terms via WebFetch where possible. See `docs/datasets/<modality>/<id>.md` for per-entry citations.

## License

The registry contents (manifests, cards, scripts) are released under MIT.
The underlying datasets are subject to their own licenses — see each card for terms. Apache 2.0 / CC-BY / CC-BY-NC / PhysioNet credentialed / institutional DUA all appear; assume **non-commercial unless verified otherwise** for any given dataset.
