#!/usr/bin/env bash
# USAGE: bash _kaggle.sh <kaggle_ref> <target_dir>
#   <kaggle_ref> formats:
#     dataset: owner/dataset-slug                         -> kaggle datasets download
#     comp   : competition:competition-slug               -> kaggle competitions download
#   Unzips the downloaded archive into <target_dir>.

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "usage: bash $(basename "${BASH_SOURCE[0]}") <owner/slug | competition:slug> <target_dir>" >&2
    exit 2
fi

ref="$1"
target="$2"

if ! command -v kaggle >/dev/null 2>&1; then
    echo "error: missing tool: install kaggle (pip install kaggle)" >&2
    exit 1
fi

if [[ ! -f "${HOME}/.kaggle/kaggle.json" ]]; then
    echo "error: ~/.kaggle/kaggle.json not found." >&2
    echo "  fix: visit https://www.kaggle.com/settings/account -> 'Create New API Token'," >&2
    echo "       move kaggle.json to ~/.kaggle/, then chmod 600 ~/.kaggle/kaggle.json" >&2
    exit 1
fi

mkdir -p "${target}"

if [[ "${ref}" == competition:* ]]; then
    slug="${ref#competition:}"
    echo "kaggle competitions download: ${slug} -> ${target}"
    kaggle competitions download -c "${slug}" -p "${target}"
else
    echo "kaggle datasets download: ${ref} -> ${target}"
    kaggle datasets download -d "${ref}" -p "${target}" --unzip
    exit 0
fi

# For competitions, attempt to unzip the resulting archive.
shopt -s nullglob
for zf in "${target}"/*.zip; do
    echo "unzip: ${zf}"
    if command -v unzip >/dev/null 2>&1; then
        unzip -n -q "${zf}" -d "${target}"
    else
        echo "warn: unzip not on PATH; leaving archive in place"
    fi
done

echo "ok: kaggle ${ref}"
