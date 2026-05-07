"""Validate a JSONL manifest file against schemas/dataset.schema.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click


def _import_jsonschema():
    try:
        import jsonschema  # type: ignore
    except ImportError as e:
        raise SystemExit("missing tool: install jsonschema (pip install jsonschema)") from e
    return jsonschema


@click.command()
@click.argument("jsonl_file", type=click.Path(exists=True, dir_okay=False))
@click.option(
    "--schema",
    "schema_path",
    type=click.Path(exists=True, dir_okay=False),
    default=None,
    help="Defaults to <repo>/schemas/dataset.schema.json.",
)
def main(jsonl_file: str, schema_path: str | None) -> None:
    jsonschema = _import_jsonschema()
    repo_root = Path(__file__).resolve().parents[2]
    sp = Path(schema_path) if schema_path else repo_root / "schemas" / "dataset.schema.json"

    with open(sp, "r", encoding="utf-8") as fh:
        schema = json.load(fh)
    validator = jsonschema.Draft202012Validator(schema)

    errors = 0
    valid = 0
    with open(jsonl_file, "r", encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                click.echo(f"INVALID {jsonl_file}:{ln}: json: {e}", err=True)
                errors += 1
                continue
            row_errors = sorted(validator.iter_errors(row), key=lambda e: e.path)
            if row_errors:
                msg = "; ".join(f"{'.'.join(map(str, e.path))}: {e.message}" for e in row_errors)
                click.echo(f"INVALID {jsonl_file}:{ln}: {msg}", err=True)
                errors += 1
                continue
            valid += 1

    click.echo(f"summary: {valid} valid, {errors} invalid")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
