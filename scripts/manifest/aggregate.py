"""Concatenate per-modality manifests into all.jsonl, validate against schema, print summary."""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import click


def _import_jsonschema():
    try:
        import jsonschema  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install jsonschema (pip install jsonschema)") from e
    return jsonschema


@click.command()
@click.option(
    "--manifests-dir",
    "manifests_dir",
    type=click.Path(exists=True, file_okay=False),
    default=None,
    help="Defaults to <repo>/manifests.",
)
@click.option(
    "--schema",
    "schema_path",
    type=click.Path(exists=True, dir_okay=False),
    default=None,
    help="Defaults to <repo>/schemas/dataset.schema.json.",
)
@click.option(
    "--out",
    "out_path",
    type=click.Path(dir_okay=False),
    default=None,
    help="Defaults to <manifests-dir>/all.jsonl.",
)
@click.option(
    "--strict/--lenient",
    default=True,
    show_default=True,
    help="Strict: any invalid line aborts. Lenient: log + skip.",
)
def main(manifests_dir: str | None, schema_path: str | None, out_path: str | None, strict: bool) -> None:
    jsonschema = _import_jsonschema()
    repo_root = Path(__file__).resolve().parents[2]
    md = Path(manifests_dir) if manifests_dir else repo_root / "manifests"
    sp = Path(schema_path) if schema_path else repo_root / "schemas" / "dataset.schema.json"
    out = Path(out_path) if out_path else md / "all.jsonl"

    with open(sp, encoding="utf-8") as fh:
        schema = json.load(fh)

    validator = jsonschema.Draft202012Validator(schema)

    files = ["ct.jsonl", "xr.jsonl", "mri.jsonl", "us.jsonl", "multimodal.jsonl"]
    rows: list[dict] = []
    invalid: list[tuple[str, int, str]] = []

    for f in files:
        p = md / f
        if not p.exists():
            click.echo(f"info: {f} not present; skipping")
            continue
        with open(p, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as e:
                    invalid.append((f, ln, f"json: {e}"))
                    continue
                errors = sorted(validator.iter_errors(row), key=lambda e: e.path)
                if errors:
                    msg = "; ".join(f"{'.'.join(map(str, e.path))}: {e.message}" for e in errors)
                    invalid.append((f, ln, msg))
                    continue
                rows.append(row)

    # Duplicate ids are registry corruption: two rows claiming the same slug with
    # potentially contradictory metadata. Always an error, even in lenient mode.
    id_counts: Counter[str] = Counter(row.get("id", "?") for row in rows)
    dup_ids = sorted(k for k, v in id_counts.items() if v > 1)
    if dup_ids:
        for d in dup_ids:
            click.echo(f"DUPLICATE id: {d} appears {id_counts[d]} times", err=True)
        raise SystemExit(f"error: {len(dup_ids)} duplicate id(s); one manifest row per dataset")

    if invalid:
        for f, ln, msg in invalid:
            click.echo(f"INVALID {f}:{ln}: {msg}", err=True)
        if strict:
            raise SystemExit(f"error: {len(invalid)} invalid line(s); aborting (use --lenient to skip)")

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, sort_keys=True) + "\n")

    # Summary table.
    by_mod: Counter[str] = Counter(row.get("modality", "?") for row in rows)
    by_tier: Counter[str] = Counter(row.get("access_tier", "?") for row in rows)
    total_size = sum(int(row["size_bytes"] or 0) for row in rows if row.get("size_bytes") is not None)
    by_mod_size: dict[str, int] = defaultdict(int)
    for row in rows:
        if row.get("size_bytes") is not None:
            by_mod_size[row.get("modality", "?")] += int(row["size_bytes"])

    click.echo("---")
    click.echo(f"wrote: {out}  ({len(rows)} valid row(s))")
    click.echo("rows by modality:")
    for k, v in sorted(by_mod.items()):
        sz = by_mod_size.get(k, 0)
        click.echo(f"  {k:<6} {v:>5}   size_bytes={sz}")
    click.echo("rows by access_tier:")
    for k, v in sorted(by_tier.items()):
        click.echo(f"  {k:<14} {v:>5}")
    click.echo(f"total declared size_bytes: {total_size}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
