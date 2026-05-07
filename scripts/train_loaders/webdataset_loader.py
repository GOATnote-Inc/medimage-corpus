"""Example PyTorch DataLoader on a WebDataset tar shard directory.

Usage:
    python scripts/train_loaders/webdataset_loader.py \
        --shards "data/ct/lidc-idri/shard-{000000..000031}.tar" \
        --batch-size 4

The decode pipeline reads paired NIfTI image+label bytes per sample; replace the
nibabel-based decoder with a faster path (e.g. SimpleITK in-memory) once the
training stack is settled. Intended as a reference, not a hot path.
"""

from __future__ import annotations

import io
import sys

import click


def _import_deps():
    try:
        import torch  # type: ignore  # noqa: F401
        from torch.utils.data import DataLoader  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install torch (pip install torch)") from e
    try:
        import webdataset as wds  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install webdataset (pip install webdataset)") from e
    try:
        import nibabel as nib  # type: ignore
        import numpy as np  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install nibabel + numpy") from e
    return DataLoader, wds, nib, np


def _decode_nii_gz(buf: bytes, nib, np):
    fh = nib.FileHolder(fileobj=io.BytesIO(buf))
    img = nib.Nifti1Image.from_file_map({"header": fh, "image": fh})
    return np.asarray(img.dataobj)


def make_loader(shards: str, batch_size: int, num_workers: int):
    DataLoader, wds, nib, np = _import_deps()

    def decode(sample: dict):
        out = {"__key__": sample["__key__"]}
        if "image.nii.gz" in sample:
            out["image"] = _decode_nii_gz(sample["image.nii.gz"], nib, np)
        if "label.nii.gz" in sample:
            out["label"] = _decode_nii_gz(sample["label.nii.gz"], nib, np)
        return out

    pipeline = (
        wds.WebDataset(shards, shardshuffle=True)
        .shuffle(100)
        .map(decode)
    )
    return DataLoader(pipeline, batch_size=batch_size, num_workers=num_workers)


@click.command()
@click.option("--shards", required=True, help='Brace-expansion pattern e.g. "data/.../shard-{000000..000031}.tar".')
@click.option("--batch-size", type=int, default=4, show_default=True)
@click.option("--num-workers", type=int, default=4, show_default=True)
@click.option("--max-batches", type=int, default=2, show_default=True, help="Smoke-test cap.")
def main(shards: str, batch_size: int, num_workers: int, max_batches: int) -> None:
    loader = make_loader(shards, batch_size, num_workers)
    for i, batch in enumerate(loader):
        keys = batch.get("__key__")
        click.echo(f"batch {i}: keys={keys}")
        if i + 1 >= max_batches:
            break
    click.echo("ok: loader smoke complete")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
