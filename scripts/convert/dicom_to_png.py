"""Convert a 2D DICOM tree (X-ray) to PNG with optional VOI LUT and 16->8 bit normalization."""

from __future__ import annotations

import sys
from pathlib import Path

import click


def _import_deps():
    try:
        import numpy as np  # type: ignore
        import pydicom  # type: ignore
        from PIL import Image  # type: ignore
        from pydicom.pixel_data_handlers.util import apply_voi_lut  # type: ignore
    except ImportError as e:
        raise SystemExit(
            "missing tool: install pydicom + numpy + Pillow "
            "(pip install pydicom numpy pillow)"
        ) from e
    return np, pydicom, Image, apply_voi_lut


def _to_uint8(arr, np, normalize: bool):
    if arr.dtype == np.uint8 and not normalize:
        return arr
    a = arr.astype(np.float32)
    lo, hi = float(a.min()), float(a.max())
    if hi <= lo:
        return np.zeros_like(a, dtype=np.uint8)
    a = (a - lo) / (hi - lo)
    return (a * 255.0).clip(0, 255).astype(np.uint8)


@click.command()
@click.option(
    "--in",
    "in_dir",
    "in_dir",
    required=True,
    type=click.Path(exists=True, file_okay=False),
    help="DICOM root.",
)
@click.option(
    "--out",
    "out_dir",
    required=True,
    type=click.Path(file_okay=False),
    help="Output PNG directory.",
)
@click.option("--voi-lut", is_flag=True, help="Apply DICOM VOI LUT prior to normalization.")
@click.option("--normalize", is_flag=True, help="Min-max normalize 16->8 bits.")
@click.option(
    "--invert-monochrome1",
    is_flag=True,
    help="Invert intensity when PhotometricInterpretation == MONOCHROME1.",
)
def main(
    in_dir: str,
    out_dir: str,
    voi_lut: bool,
    normalize: bool,
    invert_monochrome1: bool,
) -> None:
    np, pydicom, Image, apply_voi_lut = _import_deps()

    in_path = Path(in_dir)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    n = 0
    for p in sorted(in_path.rglob("*")):
        if not p.is_file():
            continue
        try:
            ds = pydicom.dcmread(str(p), force=True)
        except Exception:
            continue
        if not hasattr(ds, "pixel_array"):
            continue
        try:
            arr = ds.pixel_array
            if voi_lut:
                arr = apply_voi_lut(arr, ds)
            if invert_monochrome1 and getattr(ds, "PhotometricInterpretation", "") == "MONOCHROME1":
                arr = arr.max() - arr
            arr8 = _to_uint8(arr, np, normalize=normalize or arr.dtype != np.uint8)
            img = Image.fromarray(arr8)
            rel = p.relative_to(in_path).with_suffix(".png")
            out_file = out_path / rel
            out_file.parent.mkdir(parents=True, exist_ok=True)
            img.save(out_file)
            n += 1
        except Exception as e:  # noqa: BLE001
            click.echo(f"warn: skip {p}: {e}")
            continue

    click.echo(f"ok: wrote {n} PNG(s) under {out_path}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
