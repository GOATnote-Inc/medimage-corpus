#!/usr/bin/env bash
# USAGE: bash _https.sh <url> <target_dir>
#   Wraps `curl -L -O --create-dirs` with progress and resume support.

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "usage: bash $(basename "${BASH_SOURCE[0]}") <url> <target_dir>" >&2
    exit 2
fi

url="$1"
target="$2"

if ! command -v curl >/dev/null 2>&1; then
    echo "error: missing tool: install curl (e.g. apt install curl / brew install curl)" >&2
    exit 1
fi

mkdir -p "${target}"

# Derive output filename from URL (strip query string).
base="${url##*/}"
base="${base%%\?*}"
if [[ -z "${base}" ]]; then
    base="download.bin"
fi
out="${target%/}/${base}"

echo "https: ${url} -> ${out}"
curl -L --fail --retry 3 --retry-delay 5 \
     --continue-at - \
     --create-dirs \
     --progress-bar \
     -o "${out}" \
     "${url}"
echo "ok: $(basename "${out}")"
