#!/usr/bin/env bash
# USAGE: bash _physionet.sh <dataset_url> <target_dir>
#   <dataset_url>: full https://physionet.org/files/<slug>/<version>/ URL.
#   Reads PHYSIONET_USER and PHYSIONET_PASSWORD from env (never echoes them).
#
# Prerequisites: PhysioNet account, CITI training (Data or Specimens Only),
# and signed Data Use Agreement for credentialed datasets (e.g. MIMIC-CXR).

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "usage: bash $(basename "${BASH_SOURCE[0]}") <https://physionet.org/files/.../version/> <target_dir>" >&2
    exit 2
fi

url="$1"
target="$2"

if ! command -v wget >/dev/null 2>&1; then
    echo "error: missing tool: install wget (apt install wget / brew install wget)" >&2
    exit 1
fi

if [[ "${url}" != https://physionet.org/files/* ]]; then
    echo "error: expected https://physionet.org/files/... URL, got: ${url}" >&2
    exit 1
fi

if [[ -z "${PHYSIONET_USER:-}" || -z "${PHYSIONET_PASSWORD:-}" ]]; then
    echo "error: PHYSIONET_USER and PHYSIONET_PASSWORD must be set in the environment" >&2
    echo "       hint: load from a sourced .env (set -a && source .env && set +a)" >&2
    exit 1
fi

mkdir -p "${target}"
echo "physionet: creds loaded from env (user/password not echoed)"
echo "physionet: ${url} -> ${target}"
echo "note: complete CITI training and sign DUA before credentialed downloads succeed."

# wget recursive mirror; -nv keeps logs short, -N respects mtime, -c resumes.
wget -r -N -c -np -nv \
     --user "${PHYSIONET_USER}" \
     --password "${PHYSIONET_PASSWORD}" \
     -P "${target}" \
     "${url}"

echo "ok: physionet mirror complete"
