"""Download a Synapse entity (e.g. BraTS challenge data) via synapseclient."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import click


def _import_synapse():
    try:
        import synapseclient  # type: ignore
        import synapseutils  # type: ignore
    except ImportError as e:
        raise SystemExit(
            "missing tool: install synapseclient (pip install synapseclient)"
        ) from e
    return synapseclient, synapseutils


@click.command()
@click.option(
    "--id",
    "entity_id",
    required=True,
    help="Synapse id (e.g. syn3193805).",
)
@click.option("--target", required=True, type=click.Path(file_okay=False))
def main(entity_id: str, target: str) -> None:
    synapseclient, synapseutils = _import_synapse()
    target_path = Path(target)
    target_path.mkdir(parents=True, exist_ok=True)

    auth_token = os.environ.get("SYNAPSE_AUTH_TOKEN")
    syn = synapseclient.Synapse()
    if auth_token:
        click.echo("synapse: auth token loaded from env (value not echoed)")
        syn.login(authToken=auth_token)
    else:
        click.echo("synapse: no SYNAPSE_AUTH_TOKEN; relying on ~/.synapseConfig")
        syn.login()

    click.echo(f"synapse: syncFromSynapse {entity_id} -> {target_path}")
    synapseutils.syncFromSynapse(syn, entity=entity_id, path=str(target_path))
    click.echo("ok: synapse sync complete")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
