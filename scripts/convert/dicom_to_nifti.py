"""Convert a DICOM series tree to NIfTI volumes via dcm2niix or pydicom+nibabel fallback."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import click


def _have_dcm2niix() -> bool:
    return shutil.which("dcm2niix") is not None


def _convert_with_dcm2niix(dicom_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "dcm2niix",
        "-z", "y",       # gzip output
        "-b", "y",       # write BIDS sidecars
        "-f", "%i_%s_%d", # patient_series_desc
        "-o", str(out_dir),
        str(dicom_root),
    ]
    click.echo("dcm2niix: " + " ".join(cmd))
    subprocess.run(cmd, check=True)


def _convert_with_pydicom_fallback(dicom_root: Path, out_dir: Path) -> None:
    try:
        import nibabel as nib  # type: ignore
        import numpy as np  # type: ignore
        import pydicom  # type: ignore
    except ImportError as e:
        raise SystemExit(
            "missing tool: install pydicom+nibabel+numpy (pip install pydicom nibabel numpy) "
            "or install dcm2niix (preferred)."
        ) from e

    out_dir.mkdir(parents=True, exist_ok=True)

    # Group files by SeriesInstanceUID so each series becomes one volume.
    series: dict[str, list[Path]] = {}
    for p in dicom_root.rglob("*"):
        if not p.is_file():
            continue
        try:
            ds = pydicom.dcmread(str(p), stop_before_pixels=True, force=True)
        except Exception:  # noqa: BLE001
            continue
        uid = getattr(ds, "SeriesInstanceUID", None)
        if not uid:
            continue
        series.setdefault(uid, []).append(p)

    if not series:
        click.echo("warn: no DICOM series found in input tree")
        return

    for uid, files in series.items():
        files.sort()
        slices = []
        for fp in files:
            try:
                slc = pydicom.dcmread(str(fp), force=True)
                if hasattr(slc, "pixel_array"):
                    slices.append(slc)
            except Exception:  # noqa: BLE001
                continue
        if not slices:
            continue
        slices.sort(key=lambda s: float(getattr(s, "InstanceNumber", 0) or 0))
        try:
            volume = np.stack([s.pixel_array for s in slices], axis=-1).astype(np.float32)
        except Exception as e:  # noqa: BLE001
            click.echo(f"warn: cannot stack series {uid}: {e}")
            continue
        out_path = out_dir / f"{uid}.nii.gz"
        nib.save(nib.Nifti1Image(volume, affine=np.eye(4)), str(out_path))
        click.echo(f"ok: {out_path} (shape={volume.shape})")


@click.command()
@click.option(
    "--in",
    "in_dir",
    "in_dir",
    required=True,
    type=click.Path(exists=True, file_okay=False),
    help="DICOM root (study/series tree).",
)
@click.option(
    "--out",
    "out_dir",
    required=True,
    type=click.Path(file_okay=False),
    help="Output NIfTI directory.",
)
@click.option(
    "--force-fallback",
    is_flag=True,
    help="Skip dcm2niix even if installed; use pydicom+nibabel.",
)
def main(in_dir: str, out_dir: str, force_fallback: bool) -> None:
    in_path = Path(in_dir)
    out_path = Path(out_dir)
    if not force_fallback and _have_dcm2niix():
        _convert_with_dcm2niix(in_path, out_path)
    else:
        if not force_fallback:
            click.echo("info: dcm2niix not on PATH; using pydicom+nibabel fallback")
        _convert_with_pydicom_fallback(in_path, out_path)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
