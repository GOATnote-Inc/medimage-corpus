#!/usr/bin/env bash
# USAGE: bash scripts/download/get.sh <modality>/<id> [--target <path>] [--dry-run]
#   <modality>/<id>   e.g. ct/lidc-idri, xr/chexpert-small (only the id portion is required)
#   --target <path>   override default ./data/<modality>/<id>/
#   --dry-run         resolve and print the dispatch plan; do not download
#
# Looks up the manifest line by id across manifests/{ct,xr,mri,us,multimodal}.jsonl,
# reads download_method + download_url + access_url, and dispatches to the matching
# sub-handler in this directory. Never silently downloads on accident: the dispatcher
# only acts after a positive id lookup; missing handler is a hard error.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
MANIFEST_DIR="${REPO_ROOT}/manifests"

usage() {
    grep -E '^# (USAGE|  )' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    exit 2
}

if [[ $# -lt 1 ]]; then
    usage
fi

raw_arg="$1"; shift
target=""
dry_run="0"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --target)
            target="${2:?--target requires a path}"; shift 2;;
        --dry-run)
            dry_run="1"; shift;;
        -h|--help)
            usage;;
        *)
            echo "error: unknown flag: $1" >&2
            usage;;
    esac
done

# Accept either "modality/id" or just "id".
if [[ "${raw_arg}" == */* ]]; then
    requested_modality="${raw_arg%%/*}"
    requested_id="${raw_arg##*/}"
else
    requested_modality=""
    requested_id="${raw_arg}"
fi

if [[ -z "${requested_id}" ]]; then
    echo "error: empty id" >&2
    usage
fi

# Locate matching jsonl line. Prefer python for robust JSON parsing.
PYTHON_BIN="${PYTHON:-python3}"
if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
    echo "error: python3 not found on PATH" >&2
    exit 1
fi

if [[ ! -d "${MANIFEST_DIR}" ]]; then
    echo "error: manifest dir not found: ${MANIFEST_DIR}" >&2
    exit 1
fi

lookup_json="$("${PYTHON_BIN}" - "${MANIFEST_DIR}" "${requested_id}" "${requested_modality}" <<'PY'
import json, os, sys
manifest_dir, want_id, want_mod = sys.argv[1], sys.argv[2], sys.argv[3]
files = ["ct.jsonl", "xr.jsonl", "mri.jsonl", "us.jsonl", "multimodal.jsonl"]
matches = []
for f in files:
    p = os.path.join(manifest_dir, f)
    if not os.path.isfile(p):
        continue
    with open(p, "r", encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("id") == want_id:
                if want_mod and row.get("modality", "").lower() != want_mod.lower():
                    continue
                row["__manifest_file"] = f
                row["__line"] = ln
                matches.append(row)
if not matches:
    print("__NONE__")
    sys.exit(0)
if len(matches) > 1:
    sys.stderr.write(f"warning: {len(matches)} entries match id={want_id}; picking first\n")
print(json.dumps(matches[0]))
PY
)"

if [[ "${lookup_json}" == "__NONE__" ]]; then
    echo "error: no manifest entry found for id='${requested_id}'" >&2
    echo "       searched: ${MANIFEST_DIR}/{ct,xr,mri,us,multimodal}.jsonl" >&2
    exit 1
fi

# Extract fields one at a time (word-split-safe: values may contain spaces).
field() {
    "${PYTHON_BIN}" -c "
import json, sys
r = json.loads(sys.argv[1])
v = r.get(sys.argv[2])
sys.stdout.write('' if v is None else str(v))
" "${lookup_json}" "$1"
}
entry_id="$(field id)"
entry_modality="$(field modality | tr '[:upper:]' '[:lower:]')"
download_method="$(field download_method)"
download_url="$(field download_url)"
access_url="$(field access_url)"

if [[ -z "${entry_id}" || -z "${download_method}" ]]; then
    echo "error: manifest entry missing id or download_method" >&2
    exit 1
fi

src_url="${download_url:-${access_url}}"
if [[ -z "${src_url}" ]]; then
    echo "error: no download_url or access_url for id='${entry_id}'" >&2
    exit 1
fi

# Normalise the manifest URL into the shape the method's handler expects.
# Manifests record human-facing URLs; handlers want repo ids / slugs / file roots.
normalize_src() {
    local method="$1" url="$2"
    case "${method}" in
        hf)
            if [[ "${url}" == https://huggingface.co/datasets/* ]]; then
                url="${url#https://huggingface.co/datasets/}"
                url="${url%%\?*}"; url="${url%/}"
            elif [[ "${url}" == http*://* ]]; then
                echo "error: cannot derive a Hugging Face repo id from '${url}'" >&2
                echo "       set download_url to a https://huggingface.co/datasets/<owner>/<name> URL in the manifest" >&2
                return 1
            fi
            ;;
        kaggle)
            if [[ "${url}" == *kaggle.com/competitions/* ]]; then
                local slug="${url#*kaggle.com/competitions/}"
                slug="${slug%%/*}"; slug="${slug%%\?*}"
                url="competition:${slug}"
            elif [[ "${url}" == *kaggle.com/datasets/* ]]; then
                local ref="${url#*kaggle.com/datasets/}"
                ref="${ref%%\?*}"; ref="${ref%/}"
                url="$(printf '%s' "${ref}" | cut -d/ -f1,2)"
            fi
            ;;
        physionet)
            if [[ "${url}" == https://physionet.org/content/* ]]; then
                url="https://physionet.org/files/${url#https://physionet.org/content/}"
            fi
            [[ "${url}" == */ ]] || url="${url}/"
            ;;
        synapse)
            if [[ "${url}" =~ (syn[0-9]+) ]]; then
                url="${BASH_REMATCH[1]}"
            fi
            ;;
        tcia-cli)
            if [[ "${url}" == *cancerimagingarchive.net/collection/* ]]; then
                local c="${url#*cancerimagingarchive.net/collection/}"
                c="${c%%/*}"; c="${c%%\?*}"
                url="${c}"
            elif [[ "${url}" == http*://* ]]; then
                echo "error: cannot derive a TCIA collection slug from '${url}'" >&2
                echo "       run scripts/download/_tcia.py --collection <name> directly (see the dataset card)" >&2
                return 1
            fi
            ;;
    esac
    printf '%s\n' "${url}"
}

if ! src_url="$(normalize_src "${download_method}" "${src_url}")"; then
    exit 3
fi

if [[ -z "${target}" ]]; then
    target="${REPO_ROOT}/data/${entry_modality}/${entry_id}"
fi

cat <<INFO
medimage-corpus dispatch:
  id              : ${entry_id}
  modality        : ${entry_modality}
  download_method : ${download_method}
  source          : ${src_url}
  target          : ${target}
  dry_run         : ${dry_run}
INFO

if [[ "${dry_run}" == "1" ]]; then
    echo "dry-run: not invoking handler"
    exit 0
fi

# Landing pages are not downloads. When a direct-file method has no download_url,
# refuse honestly instead of curling an HTML page into the data directory.
case "${download_method}" in
    https|zenodo|github-release)
        if [[ -z "${download_url}" ]]; then
            echo "error: id='${entry_id}' has no direct download_url; its access_url is a landing page." >&2
            echo "       see docs/datasets/${entry_modality}/${entry_id}.md for manual steps." >&2
            exit 3
        fi
        ;;
esac

mkdir -p "${target}"

dispatch() {
    case "${download_method}" in
        https)
            bash "${SCRIPT_DIR}/_https.sh" "${src_url}" "${target}";;
        s3|aws-open-data)
            bash "${SCRIPT_DIR}/_s3.sh" "${src_url}" "${target}";;
        openneuro)
            bash "${SCRIPT_DIR}/_openneuro.sh" "${src_url}" "${target}";;
        physionet)
            bash "${SCRIPT_DIR}/_physionet.sh" "${src_url}" "${target}";;
        kaggle)
            bash "${SCRIPT_DIR}/_kaggle.sh" "${src_url}" "${target}";;
        hf)
            "${PYTHON_BIN}" "${SCRIPT_DIR}/_hf.py" --repo "${src_url}" --type dataset --target "${target}";;
        tcia-cli)
            "${PYTHON_BIN}" "${SCRIPT_DIR}/_tcia.py" --collection "${src_url}" --target "${target}";;
        synapse)
            "${PYTHON_BIN}" "${SCRIPT_DIR}/_synapse.py" --id "${src_url}" --target "${target}";;
        zenodo)
            bash "${SCRIPT_DIR}/_https.sh" "${src_url}" "${target}";;
        github-release)
            bash "${SCRIPT_DIR}/_https.sh" "${src_url}" "${target}";;
        gcs)
            echo "error: gcs handler not yet implemented; install gsutil and use:"
            echo "       gsutil -m cp -r '${src_url}' '${target}'"
            exit 3;;
        nih-box|aspera|stanford-aimi)
            echo "error: '${download_method}' requires manual handling (browser auth or aspera client)." >&2
            echo "       see docs/datasets/${entry_modality}/${entry_id}.md for stepwise instructions." >&2
            exit 3;;
        application)
            echo "error: '${entry_id}' is application-tier: access requires an approved data-access request." >&2
            echo "       see docs/datasets/${entry_modality}/${entry_id}.md and docs/ACCESS.md." >&2
            exit 3;;
        *)
            echo "error: no handler registered for download_method='${download_method}'" >&2
            exit 3;;
    esac
}

dispatch
echo "ok: ${entry_id} -> ${target}"
