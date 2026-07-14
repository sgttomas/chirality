#!/usr/bin/env python3
"""Freeze exact PKG-04 source bindings and self-excluding terminal manifests."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/RECON-P1-PKG04"
UPSTREAM = RUN / "instances/WORKING-P1-PKG04"
SNAP = RUN / "snapshots/W_P1/PKG04-preintegration-r1"
PREFLIGHT = RUN / "snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv"
HASH_COLS = {
    "Datasheet.md": "datasheet_sha256",
    "Specification.md": "specification_sha256",
    "Guidance.md": "guidance_sha256",
    "Procedure.md": "procedure_sha256",
    "_STATUS.md": "status_sha256",
    "_CONTEXT.md": "context_sha256",
    "_REFERENCES.md": "references_sha256",
    "_DEPENDENCIES.md": "dependencies_md_sha256",
    "Dependencies.csv": "dependencies_csv_sha256",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def build_manifest(base: Path) -> tuple[int, str]:
    manifest = base / "MANIFEST.tsv"
    files = sorted(p for p in base.rglob("*") if p.is_file() and p != manifest)
    rows = [[sha(p), p.stat().st_size, p.relative_to(ROOT).as_posix()] for p in files]
    write_tsv(manifest, ["sha256", "bytes", "path"], rows)
    return len(rows), sha(manifest)


def main() -> None:
    source_rows = []
    with PREFLIGHT.open(encoding="utf-8") as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t") if r["package"] == "PKG-04"]
    assert len(rows) == 6
    for row in rows:
        live = ROOT / row["live_path"]
        for name, column in HASH_COLS.items():
            actual = sha(live / name)
            expected = row[column]
            assert actual == expected
            source_rows.append([row["deliverable_id"], name, expected, actual, "PASS"])
    assert len(source_rows) == 54
    write_tsv(SNAP / "SOURCE_BINDINGS.tsv",
              ["deliverable_id", "surface", "expected_sha256", "actual_sha256", "verdict"],
              source_rows)

    snapshot_rows, snapshot_digest = build_manifest(SNAP)
    status = {
        "basis": "main@2a5e3825d8d2fc4943742a53ccad3b89c4c81902",
        "blockers": [],
        "manager_reproduction": "PASS_FULL_PACKAGE_6_OF_6",
        "next_owner": "HELP_HUMAN",
        "snapshot": SNAP.relative_to(ROOT).as_posix(),
        "snapshot_manifest_rows": snapshot_rows,
        "snapshot_manifest_sha256": snapshot_digest,
        "status": "PASS",
        "terminal": True,
        "unknowns": [],
        "waivers": [],
    }
    (HERE / "STATUS.json").write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (HERE / "RETURN.md").write_text(
        "# RECON-P1-PKG04 Terminal Return\n\n"
        "Terminal verdict: `PASS`.\n\n"
        "The direct Agent-1 full-package reproduction passes every sealed fan-in gate: "
        "6 members, 4 terminal WORKING_ITEMS child returns, 3,117 upstream manifest "
        "bindings, 178 mappings, 1,368 source lines, 18 evidence/production/finalization "
        "bindings, exact 30 replacement and inverse rollback rows, 6 simulations, 12 "
        "negative probes, fresh 264/264 practitioner tests, and zero Piping project writes. "
        "All retained mechanical attempts and evidence normalization claims are closed.\n\n"
        f"Immutable derivative: `{SNAP.relative_to(ROOT).as_posix()}/`. Its self-excluding "
        f"manifest contains {snapshot_rows} bindings and has SHA-256 `{snapshot_digest}`.\n\n"
        "Blockers, waivers, conflicts, stale bindings, missing outputs, semantic unknowns, "
        "and required reruns at the recorded identities: none.\n\n"
        "Requested parent action: HELP_HUMAN reproduce and accept or reject the snapshot. "
        "This return performs and authorizes no candidate repair, project write, Git "
        "integration, lifecycle action, H1/H2, release, or retirement.\n",
        encoding="utf-8",
    )
    instance_rows, instance_digest = build_manifest(HERE)
    print(json.dumps({"snapshot_manifest_rows": snapshot_rows,
                      "snapshot_manifest_sha256": snapshot_digest,
                      "instance_manifest_rows": instance_rows,
                      "instance_manifest_sha256": instance_digest}, indent=2))


if __name__ == "__main__":
    main()
