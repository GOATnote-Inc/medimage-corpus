# CLAUDE.md — operating notes for this repo

This is a **registry repo** for medical imaging training datasets. It stores manifests, dataset cards, download dispatchers, and conversion scripts. It does NOT store the underlying imaging data — those live on a Brev/RunPod/local pod after a deliberate `bash scripts/download/get.sh ...` run.

## Hard rules

- **Never read .env or any credentials file.** Reading loads contents into the conversation transcript. To check what keys are present without exposing values: `awk -F= '/^[A-Z_]+=/ {print $1, "len:", length($2)}' /path/to/.env` or `grep -c '^HF_TOKEN=' /path/to/.env`.
- **Never run commands that print env values verbatim.** That includes `printenv`, `env`, `cat .env`, `ps -ef | grep docker` (the latter leaks `-e KEY=value` flags), `systemctl show ... --property=Environment`, `cat /proc/*/environ`. Use length-only or count-only checks.
- **Never `git add -A` / `git add .`** in this repo — there are bulky `data/` paths that should never enter version control even if the gitignore happens to miss one. Stage by name.
- **Manifest is canonical.** Treat `manifests/<modality>.jsonl` as source of truth. `manifests/all.jsonl` is a derived artifact — regenerate via `python3 scripts/manifest/aggregate.py`. Never edit `all.jsonl` directly.
- **No fabricated sizes.** If a dataset's authoritative byte count is unknown, set `size_bytes: null` and note in `agent_notes`. Do not guess.
- **No emojis** in any file written here. Plain text only — including dataset cards.

## Where to look

- `README.md` — project summary, quick start, top-N tables.
- `schemas/dataset.schema.json` — manifest contract (JSON Schema 2020-12).
- `manifests/` — per-modality JSONL plus aggregated `all.jsonl`.
- `docs/datasets/<modality>/<id>.md` — one card per dataset (127 total).
- `docs/ACCESS.md` — gating workflows by tier (open / registration / credentialed / application).
- `docs/FORMATS.md` — DICOM / NIfTI / WebDataset / HF parquet decision matrix.
- `docs/DEPLOY_BREV.md` — running downloads on GPU pods.

## Common tasks

### Add a new dataset

1. Pick the right `manifests/<modality>.jsonl`. If it spans modalities (image + text VLM), put it in `multimodal.jsonl`.
2. Append one JSON object on a single line, conforming to `schemas/dataset.schema.json`.
3. Write `docs/datasets/<modality>/<id>.md` (~150-300 words).
4. Run `python3 scripts/manifest/aggregate.py` then `python3 scripts/manifest/validate.py manifests/all.jsonl`.

### Verify a download URL still works

```bash
curl -sI -L "$(python3 -c "import json; print([r for r in (json.loads(l) for l in open('manifests/all.jsonl')) if r['id']=='lidc_idri'][0]['access_url'])")"
```

### Regenerate stats

```bash
python3 scripts/manifest/stats.py --by tier --top 20
python3 scripts/manifest/stats.py --by size --top 20
python3 scripts/manifest/stats.py --by year --top 20
```

## Pod integration (recommended for actual downloads)

Run downloads on a GPU/storage pod with direct SSH access, not on the laptop:

```bash
# Sync the registry over
rsync -av --exclude data --exclude _downloads ./ <pod>:/workspace/medimage-corpus/

# Then on the pod:
ssh <pod> 'cd /workspace/medimage-corpus && bash scripts/download/get.sh ct/ct_rate --target /workspace/data/ct/ct_rate'
```

Set credentials on the pod via the provider's env-var UI, NOT by piping `.env` over SSH.

## Don't

- Don't push the registry to GitHub without `git status` confirming no `data/` paths are staged. The `.gitignore` covers `data/` `_downloads/` `_extract/` `*.dcm` `*.nii.gz` `*.nii` `*.tar` `*.zip` and similar — but stage by name to be safe.
- Don't add a dataset whose primary URL 404s. Verify with `curl -sI -L` first.
- Don't switch a manifest entry's `id` after release — downstream training configs may pin to it. Add a new entry instead and mark the old one's `agent_notes` "superseded by <new_id>".
- Don't commit converted training data. Conversion outputs go to `data/` (gitignored) and onward to object storage / HF Hub if useful.
