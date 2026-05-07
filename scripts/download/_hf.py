"""Download a Hugging Face repo (dataset or model) via huggingface_hub.snapshot_download."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import click


def _import_hf():
    try:
        from huggingface_hub import snapshot_download
    except ImportError as e:
        raise SystemExit(
            "missing tool: install huggingface_hub (pip install huggingface-hub)"
        ) from e
    return snapshot_download


@click.command()
@click.option("--repo", required=True, help="HF repo id (owner/name).")
@click.option(
    "--type",
    "repo_type",
    type=click.Choice(["dataset", "model", "space"], case_sensitive=False),
    default="dataset",
    show_default=True,
)
@click.option("--target", required=True, type=click.Path(file_okay=False), help="Local target directory.")
@click.option(
    "--allow-patterns",
    multiple=True,
    default=None,
    help="Optional glob patterns to allow (repeatable).",
)
@click.option(
    "--ignore-patterns",
    multiple=True,
    default=None,
    help="Optional glob patterns to ignore (repeatable).",
)
@click.option("--revision", default=None, help="Optional revision (branch, tag, or commit).")
def main(
    repo: str,
    repo_type: str,
    target: str,
    allow_patterns: tuple[str, ...] | None,
    ignore_patterns: tuple[str, ...] | None,
    revision: str | None,
) -> None:
    snapshot_download = _import_hf()
    target_path = Path(target)
    target_path.mkdir(parents=True, exist_ok=True)

    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_HUB_TOKEN")
    if token:
        click.echo("hf: token loaded from env (value not echoed)")

    click.echo(f"hf: snapshot_download repo={repo} type={repo_type.lower()} -> {target_path}")
    snapshot_download(
        repo_id=repo,
        repo_type=repo_type.lower(),
        local_dir=str(target_path),
        local_dir_use_symlinks=False,
        allow_patterns=list(allow_patterns) if allow_patterns else None,
        ignore_patterns=list(ignore_patterns) if ignore_patterns else None,
        revision=revision,
        token=token,
    )
    click.echo("ok: hf snapshot complete")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
