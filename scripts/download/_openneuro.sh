#!/usr/bin/env bash
# USAGE: bash _openneuro.sh <openneuro_id_or_url> <target_dir>
#   Accepts:
#     ds002330                              (dataset id)
#     s3://openneuro.org/ds002330           (full s3 url)
#     https://openneuro.org/datasets/ds002330  (browser url - id extracted)
#   Uses aws s3 cp --no-sign-request against the OpenNeuro AWS Open Data bucket.

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "usage: bash $(basename "${BASH_SOURCE[0]}") <ds-id | s3://... | https://openneuro.org/...> <target_dir>" >&2
    exit 2
fi

ref="$1"
target="$2"

if ! command -v aws >/dev/null 2>&1; then
    echo "error: missing tool: install aws CLI (pip install awscli)" >&2
    exit 1
fi

# Normalise to s3 URL.
if [[ "${ref}" == s3://* ]]; then
    s3_url="${ref}"
elif [[ "${ref}" == https://openneuro.org/datasets/* ]]; then
    ds_id="${ref#https://openneuro.org/datasets/}"
    ds_id="${ds_id%%/*}"
    s3_url="s3://openneuro.org/${ds_id}"
elif [[ "${ref}" =~ ^ds[0-9]+$ ]]; then
    s3_url="s3://openneuro.org/${ref}"
else
    echo "error: cannot parse openneuro reference: ${ref}" >&2
    exit 1
fi

mkdir -p "${target}"
echo "openneuro: ${s3_url} -> ${target}"
aws s3 cp --recursive --no-sign-request "${s3_url}" "${target}"
echo "ok: openneuro mirror complete"
