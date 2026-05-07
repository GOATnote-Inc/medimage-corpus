# Deploying medimage-corpus on Brev

Brev pods (warm-lavender-narwhal H200, evil-cyan-lobster H200, unnecessary-peach-catfish B300) are the intended run target. The repo only stores a registry; **all downloads and conversions happen on the pod**.

## Mount and clone

Brev pods mount `/workspace` as the persistent volume. Clone there:

```bash
cd /workspace
git clone https://github.com/GOATnote-Inc/medimage-corpus.git
cd medimage-corpus

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ".[convert,download,dev]"
```

System tools to install on the pod (Ubuntu 22.04+):

```bash
sudo apt-get update && sudo apt-get install -y curl wget unzip dcm2niix
```

## Environment variables (load from a `.env`, never read raw)

The download dispatcher reads credentials from environment variables and never prints values:

- `PHYSIONET_USER`, `PHYSIONET_PASSWORD` -- credentialed PhysioNet datasets (MIMIC-CXR, etc.)
- `KAGGLE_USERNAME`, `KAGGLE_KEY` -- Kaggle CLI; or place `~/.kaggle/kaggle.json` (chmod 600)
- `HF_TOKEN` (or `HUGGINGFACE_HUB_TOKEN`) -- gated Hugging Face datasets
- `SYNAPSE_AUTH_TOKEN` -- BraTS via Synapse
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` -- only needed for non-anonymous S3

Load pattern:

```bash
set -a && source .env && set +a
```

## Run a download

```bash
bash scripts/download/get.sh ct/lidc-idri --dry-run    # print plan first
bash scripts/download/get.sh ct/lidc-idri              # fetch
```

Default target is `./data/<modality>/<id>/`. Override with `--target /workspace/scratch/<id>`.

## Parallelism

- One H200/H100 has plenty of CPU for ~8 parallel `_https.sh` jobs. Use `xargs -P 8` over a list of ids.
- `aws s3 cp --recursive` is already multi-threaded; do not stack more than 2-3 concurrent buckets or you will saturate the NIC.
- TCIA REST endpoints throttle aggressively; keep `_tcia.py` to one job per pod.
- For credentialed PhysioNet datasets, `wget -r` is single-stream by design; running 2-3 in parallel against different datasets is safe.

## Convert on the pod

Once raw data lands under `data/<mod>/<id>/`:

```bash
python scripts/convert/dicom_to_nifti.py --in data/ct/lidc-idri --out data/ct/lidc-idri/nifti
python scripts/convert/nifti_to_webdataset.py --in data/ct/lidc-idri/nifti --out data/ct/lidc-idri/wds --shard-size 4
```

Sharding 1 TB of CT volumes takes a few hours single-threaded; run inside `tmux` so a dropped SSH session does not kill the job.

## Don't

- Don't commit anything from `data/` -- the `.gitignore` excludes it but always sanity-check `git status` before staging.
- Don't `git add -A` in this repo (a learned habit from the broader corpus).
- Don't echo credential variables to logs; the helpers already redact them.

## Idle pods get deleted

Pods at <10% utilization for >12h get reclaimed. Run downloads and conversions in foreground tmux sessions with visible progress so utilization registers.
