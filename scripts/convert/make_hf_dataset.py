"""Wrap a converted directory into a Hugging Face datasets.Dataset and save as parquet shards."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click


def _import_deps():
    try:
        import datasets  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install datasets (pip install datasets)") from e
    try:
        import yaml  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install pyyaml (pip install pyyaml)") from e
    return datasets, yaml


def _index_files(in_dir: Path, exts: list[str]) -> list[Path]:
    out: list[Path] = []
    for ext in exts:
        out.extend(sorted(in_dir.rglob(f"*{ext}")))
    return out


@click.command()
@click.option(
    "--in",
    "in_dir",
    "in_dir",
    required=True,
    type=click.Path(exists=True, file_okay=False),
    help="Converted directory (PNG, NIfTI, npy, jpg).",
)
@click.option(
    "--out",
    "out_dir",
    required=True,
    type=click.Path(file_okay=False),
    help="Output parquet directory.",
)
@click.option(
    "--features-config",
    "features_config",
    required=True,
    type=click.Path(exists=True, dir_okay=False),
    help="YAML file describing schema; see comments below.",
)
@click.option("--shard-size", default="500MB", show_default=True)
def main(in_dir: str, out_dir: str, features_config: str, shard_size: str) -> None:
    """
    features_config YAML schema (minimal):

      extensions: [".png", ".jpg"]   # which files to index
      label_from: parent_dir         # parent_dir | none
      metadata: {modality: "XR"}     # static columns broadcast to every row
    """
    datasets, yaml = _import_deps()
    in_path = Path(in_dir)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    with open(features_config, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}

    exts = cfg.get("extensions") or [".png", ".jpg", ".nii.gz", ".npy"]
    label_from = cfg.get("label_from", "none")
    static_meta: dict[str, object] = cfg.get("metadata") or {}

    files = _index_files(in_path, exts)
    if not files:
        raise SystemExit(f"error: no files matching {exts} under {in_path}")

    rows: list[dict[str, object]] = []
    for fp in files:
        rel = fp.relative_to(in_path)
        row: dict[str, object] = {
            "path": str(fp),
            "rel_path": str(rel),
            "size_bytes": fp.stat().st_size,
        }
        if label_from == "parent_dir":
            row["label"] = fp.parent.name
        row.update(static_meta)
        rows.append(row)

    ds = datasets.Dataset.from_list(rows)
    click.echo(f"hf-dataset: {len(ds)} rows -> {out_path}/dataset.parquet (shard={shard_size})")
    ds.to_parquet(str(out_path / "dataset.parquet"))

    # Drop a tiny manifest sidecar so callers don't need datasets to peek.
    sidecar = out_path / "dataset_info.json"
    with open(sidecar, "w", encoding="utf-8") as fh:
        json.dump(
            {
                "num_rows": len(ds),
                "columns": list(ds.column_names),
                "static_metadata": static_meta,
            },
            fh,
            indent=2,
        )
    click.echo(f"ok: parquet + sidecar written to {out_path}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
