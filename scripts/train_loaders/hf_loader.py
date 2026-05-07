"""Example HF datasets.load_dataset on a parquet directory with a basic transform.

Usage:
    python scripts/train_loaders/hf_loader.py --in data/xr/chexpert/parquet/
"""

from __future__ import annotations

import sys

import click


def _import_deps():
    try:
        import datasets  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install datasets (pip install datasets)") from e
    try:
        from PIL import Image  # type: ignore
    except ImportError:
        Image = None  # noqa: N816
    return datasets, Image


def _example_transform(batch: dict, Image) -> dict:
    """Demo transform: open `path` with PIL, attach height/width."""
    out = dict(batch)
    if "path" in batch and Image is not None:
        heights, widths = [], []
        for p in batch["path"]:
            try:
                with Image.open(p) as im:
                    heights.append(im.height)
                    widths.append(im.width)
            except Exception:
                heights.append(-1)
                widths.append(-1)
        out["height"] = heights
        out["width"] = widths
    return out


@click.command()
@click.option(
    "--in",
    "in_dir",
    "in_dir",
    required=True,
    type=click.Path(exists=True, file_okay=False),
    help="Parquet directory written by make_hf_dataset.py.",
)
@click.option("--max-rows", type=int, default=8, show_default=True)
def main(in_dir: str, max_rows: int) -> None:
    datasets, Image = _import_deps()
    ds = datasets.load_dataset("parquet", data_dir=in_dir, split="train")
    click.echo(f"loaded {len(ds)} rows; columns={ds.column_names}")
    ds = ds.map(lambda b: _example_transform(b, Image), batched=True, batch_size=16)
    for i, row in enumerate(ds):
        click.echo({k: row[k] for k in row if k in {"path", "label", "height", "width"}})
        if i + 1 >= max_rows:
            break
    click.echo("ok: hf loader smoke complete")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
