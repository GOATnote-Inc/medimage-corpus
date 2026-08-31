"""Download TCIA (The Cancer Imaging Archive) collections via tcia_utils or REST."""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path
from typing import Any

import click

# Slug-to-collection mapping. Keys are stable repo slugs; values are TCIA collection
# identifiers (case-sensitive; check https://www.cancerimagingarchive.net/browse-collections/).
SLUG_TO_COLLECTION: dict[str, str] = {
    "lidc-idri": "LIDC-IDRI",
    "rider-lung-ct": "RIDER Lung CT",
    "nsclc-radiogenomics": "NSCLC Radiogenomics",
    "tcga-luad": "TCGA-LUAD",
    "tcga-lusc": "TCGA-LUSC",
    "tcga-brca": "TCGA-BRCA",
    "tcga-gbm": "TCGA-GBM",
    "qin-headneck": "QIN-HEADNECK",
    "head-neck-cetuximab": "Head-Neck Cetuximab",
    "ct-colonography": "CT COLONOGRAPHY",
    "rider-pilot": "RIDER PHANTOM PET-CT",
    "rsna-2024-lumbar": "RSNA 2024 Lumbar Spine",
    "nlst": "NLST",
    "ldct-and-projection-data": "LDCT-and-Projection-data",
    "fdg-pet-ct-lesions": "FDG-PET-CT-Lesions",
    "ct-org": "CT-ORG",
    "pancreatic-ct-cbct-seg": "Pancreatic-CT-CBCT-SEG",
    "pancreas-ct": "Pancreas-CT",
    "cbis-ddsm": "CBIS-DDSM",
}

TCIA_BASE = "https://services.cancerimagingarchive.net/services/v4/TCIA/query"


def _try_import_tcia_utils():
    try:
        import tcia_utils.nbia as nbia  # type: ignore
        return nbia
    except ImportError:
        return None


def _rest_get_series(collection: str) -> list[dict[str, Any]]:
    url = f"{TCIA_BASE}/getSeries?Collection={urllib.parse.quote(collection)}"
    click.echo(f"tcia: GET {url}")
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _rest_download_series(series_uid: str, target_dir: Path) -> None:
    url = f"{TCIA_BASE}/getImage?SeriesInstanceUID={urllib.parse.quote(series_uid)}"
    out = target_dir / f"{series_uid}.zip"
    click.echo(f"tcia: GET image series {series_uid} -> {out.name}")
    with urllib.request.urlopen(url, timeout=600) as resp, open(out, "wb") as fh:
        while True:
            chunk = resp.read(1 << 20)
            if not chunk:
                break
            fh.write(chunk)


@click.command()
@click.option(
    "--collection",
    required=True,
    help="TCIA collection name OR repo slug from SLUG_TO_COLLECTION.",
)
@click.option("--target", required=True, type=click.Path(file_okay=False))
@click.option("--max-series", type=int, default=None, help="Optional cap for testing.")
def main(collection: str, target: str, max_series: int | None) -> None:
    target_path = Path(target)
    target_path.mkdir(parents=True, exist_ok=True)

    resolved = SLUG_TO_COLLECTION.get(collection.lower(), collection)
    click.echo(f"tcia: collection={resolved} (input={collection}) -> {target_path}")

    nbia = _try_import_tcia_utils()
    if nbia is not None:
        click.echo("tcia: using tcia_utils.nbia")
        try:
            series_df = nbia.getSeries(collection=resolved, format="df")
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"error: tcia_utils.getSeries failed: {e}") from e
        if series_df is None or len(series_df) == 0:
            raise SystemExit(f"error: no series for collection={resolved}")
        if max_series:
            series_df = series_df.head(max_series)
        nbia.downloadSeries(series_data=series_df, path=str(target_path))
        click.echo("ok: tcia download complete (tcia_utils)")
        return

    click.echo("tcia: tcia_utils not installed; falling back to REST API")
    series = _rest_get_series(resolved)
    if not series:
        raise SystemExit(f"error: no series for collection={resolved}")
    if max_series:
        series = series[:max_series]
    for entry in series:
        uid = entry.get("SeriesInstanceUID")
        if uid:
            _rest_download_series(uid, target_path)
    click.echo("ok: tcia download complete (REST)")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
