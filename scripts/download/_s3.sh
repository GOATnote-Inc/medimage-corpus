#!/usr/bin/env bash
# USAGE: bash _s3.sh <s3_url> <target_dir>
#   Wraps `aws s3 cp --recursive --no-sign-request` for AWS Open Data buckets.
#   If --no-sign-request fails, falls back to authenticated mode (assumes
#   AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY are configured).

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "usage: bash $(basename "${BASH_SOURCE[0]}") <s3_url> <target_dir>" >&2
    exit 2
fi

src="$1"
target="$2"

if ! command -v aws >/dev/null 2>&1; then
    echo "error: missing tool: install aws CLI (pip install awscli, or brew install awscli)" >&2
    exit 1
fi

if [[ "${src}" != s3://* ]]; then
    echo "error: expected s3:// url, got: ${src}" >&2
    exit 1
fi

mkdir -p "${target}"

echo "s3: ${src} -> ${target} (anon)"
if aws s3 cp --recursive --no-sign-request "${src}" "${target}"; then
    echo "ok: anonymous transfer complete"
    exit 0
fi

echo "warn: anonymous transfer failed; retrying with credentials"
echo "      (ensure AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY are set or 'aws configure' has run)"
aws s3 cp --recursive "${src}" "${target}"
echo "ok: authenticated transfer complete"
