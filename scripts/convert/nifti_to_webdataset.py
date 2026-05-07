"""Convert a directory of NIfTI volumes (+ optional masks) to WebDataset .tar shards."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click


def _import_webdataset():
    try:
        import webdataset as wds  # type: ignore
    except ImportError as e:
        raise SystemExit(
            "missing tool: install webdataset (pip install webdataset)"
        ) from e
    return wds


def _read_bytes(p: Path) -> bytes:
    with open(p, "rb") as fh:
        return fh.read()


def _pair_image_label(image_dir: Path, label_dir: Path | None) -> list[tuple[str, Path, Path | None]]:
    pairs: list[tuple[str, Path, Path | None]] = []
    for img in sorted(image_dir.rglob("*.nii*")):
        if not img.is_file():
            continue
        key = img.stem
        # Strip double extension .nii.gz -> stem still keeps .nii; normalize.
        if key.endswith(".nii"):
            key = key[:-4]
        lbl: Path | None = None
        if label_dir is not None:
            for cand in (
                label_dir / f"{key}.nii.gz",
                label_dir / f"{key}.nii",
                label_dir / f"{key}_seg.nii.gz",
                label_dir / f"{key}_label.nii.gz",
            ):
                if cand.exists():
                    lbl = cand
                    break
        pairs.append((key, img, lbl))
    return pairs


@click.command()
@click.option(
    "--in",
    "in_dir",
    "in_dir",
    required=True,
    type=click.Path(exists=True, file_okay=False),
    help="Directory of NIfTI images (.nii / .nii.gz).",
)
@click.option(
    "--label-dir",
    type=click.Path(exists=True, file_okay=False),
    default=None,
    help="Optional directory of paired segmentation masks.",
)
@click.option(
    "--out",
    "out_dir",
    required=True,
    type=click.Path(file_okay=False),
    help="Output directory for tar shards.",
)
@click.option(
    "--shard-size",
    "shard_gb",
    type=float,
    default=4.0,
    show_default=True,
    help="Approximate shard size in gigabytes.",
)
@click.option(
    "--shard-pattern",
    default="shard-%06d.tar",
    show_default=True,
    help="ShardWriter pattern (must include a %d-style placeholder).",
)
def main(
    in_dir: str,
    label_dir: str | None,
    out_dir: str,
    shard_gb: float,
    shard_pattern: str,
) -> None:
    wds = _import_webdataset()
    in_path = Path(in_dir)
    label_path = Path(label_dir) if label_dir else None
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    pairs = _pair_image_label(in_path, label_path)
    if not pairs:
        raise SystemExit(f"error: no .nii or .nii.gz under {in_path}")

    maxsize = int(shard_gb * (1 << 30))
    pattern = str(out_path / shard_pattern)

    click.echo(f"webdataset: {len(pairs)} samples -> {pattern} (shard~{shard_gb} GB)")

    with wds.ShardWriter(pattern, maxsize=maxsize) as sink:
        for key, img, lbl in pairs:
            sample: dict[str, object] = {
                "__key__": key,
                "image.nii.gz": _read_bytes(img),
                "json": json.dumps(
                    {
                        "key": key,
                        "image_path": str(img),
                        "label_path": str(lbl) if lbl else None,
                    }
                ).encode("utf-8"),
            }
            if lbl is not None:
                sample["label.nii.gz"] = _read_bytes(lbl)
            sink.write(sample)

    click.echo("ok: webdataset sharding complete")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
