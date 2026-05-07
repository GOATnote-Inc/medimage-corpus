"""Print top-N manifest entries by size, year, or access tier."""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import click


def _load_rows(manifest_dir: Path) -> list[dict]:
    files = ["ct.jsonl", "xr.jsonl", "mri.jsonl", "us.jsonl", "multimodal.jsonl"]
    rows: list[dict] = []
    for f in files:
        p = manifest_dir / f
        if not p.exists():
            continue
        with open(p, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return rows


def _human_bytes(n: int | None) -> str:
    if n is None:
        return "n/a"
    n = int(n)
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    f = float(n)
    i = 0
    while f >= 1024 and i < len(units) - 1:
        f /= 1024
        i += 1
    return f"{f:.2f} {units[i]}"


@click.command()
@click.option(
    "--by",
    type=click.Choice(["size", "year", "tier"]),
    default="size",
    show_default=True,
)
@click.option("--top", type=int, default=20, show_default=True)
@click.option(
    "--manifests-dir",
    "manifests_dir",
    type=click.Path(exists=True, file_okay=False),
    default=None,
)
def main(by: str, top: int, manifests_dir: str | None) -> None:
    repo_root = Path(__file__).resolve().parents[2]
    md = Path(manifests_dir) if manifests_dir else repo_root / "manifests"
    rows = _load_rows(md)
    if not rows:
        click.echo("(no rows found)")
        return

    if by == "size":
        ranked = sorted(
            rows,
            key=lambda r: int(r.get("size_bytes") or 0),
            reverse=True,
        )[:top]
        click.echo(f"top {len(ranked)} by size:")
        for r in ranked:
            click.echo(
                f"  {_human_bytes(r.get('size_bytes')):>10}  "
                f"{r.get('modality',''):<6} {r.get('id',''):<40} {r.get('name','')}"
            )
        return

    if by == "year":
        years = Counter(int(r.get("year") or 0) for r in rows)
        click.echo("rows by year:")
        for y, c in sorted(years.items()):
            click.echo(f"  {y:>4}  {c:>5}")
        # Also list top-N most recent rows.
        click.echo(f"\ntop {top} most recent rows:")
        ranked = sorted(rows, key=lambda r: int(r.get("year") or 0), reverse=True)[:top]
        for r in ranked:
            click.echo(f"  {r.get('year','')}  {r.get('modality',''):<6} {r.get('id','')}")
        return

    # by tier
    by_tier_count: Counter[str] = Counter(r.get("access_tier", "?") for r in rows)
    by_tier_size: dict[str, int] = defaultdict(int)
    for r in rows:
        sz = r.get("size_bytes") or 0
        by_tier_size[r.get("access_tier", "?")] += int(sz)
    click.echo("by access tier:")
    for tier in sorted(by_tier_count):
        click.echo(
            f"  {tier:<14}  count={by_tier_count[tier]:<5}  size={_human_bytes(by_tier_size[tier])}"
        )


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
