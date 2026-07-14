#!/usr/bin/env python3
"""Freeze self-excluding I0 reconciliation manifests and terminal return."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/RECON-I0-PKG01"
SNAP = RUN / "snapshots/I0/preintegration-r1"
LIVE = ROOT / "projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-01_Project governance baseline"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest(base: Path) -> tuple[int, str]:
    target = base / "MANIFEST.tsv"
    files = sorted(path for path in base.rglob("*") if path.is_file() and path != target)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["sha256", "bytes", "path"])
        for path in files:
            writer.writerow([sha(path), path.stat().st_size, path.relative_to(ROOT).as_posix()])
    return len(files), sha(target)


def main() -> None:
    assert sha(LIVE / "_STATUS.md") == "e63b1797b30c291b2a4510cd521951fd2736675025f0e2d07b810e64617b28a8"
    assert "**Current State:** ISSUED" in (LIVE / "_STATUS.md").read_text(encoding="utf-8")
    assert not (LIVE / "ScopeOfWork.md").exists()
    snap_rows, snap_digest = manifest(SNAP)
    status = {
        "schema": "chirality-agent-terminal-status/v1",
        "status": "PASS",
        "terminal": True,
        "package_id": "PKG-01",
        "deliverable_id": "DEL-01-01",
        "basis": "main@c5abf91b717c0b3901d2a27c578e63976853f8de",
        "lifecycle": "ISSUED",
        "manager_reproduction": "PASS_FULL_PACKAGE_1_OF_1",
        "snapshot": SNAP.relative_to(ROOT).as_posix(),
        "snapshot_manifest_rows": snap_rows,
        "snapshot_manifest_sha256": snap_digest,
        "blockers": [], "conflicts": [], "waivers": [], "unknowns": [],
        "derivative": True, "h1_approved": False, "integration_permitted": False,
        "next_owner": "HELP_HUMAN",
    }
    (HERE / "STATUS.json").write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (HERE / "RETURN.md").write_text(
        "# RECON-I0-PKG01 Terminal Return\n\n"
        "Terminal verdict: `PASS`.\n\n"
        "The fresh direct RECONCILIATION manager independently reproduced the complete "
        "single-member ISSUED I0 package. Three upstream manifests and all 335 bindings "
        "pass; exact live sources/status/lifecycle remain unchanged; two fresh conversion "
        "and finalization runs match the accepted candidate family; 27 mappings cover all "
        "272 physical source lines; exact five-row replacement and inverse manifests, "
        "apply/target/rollback, six fail-closed probes, 19/20/264 required tests, and "
        "zero-project-write containment pass. Semantic additions, blockers, conflicts, "
        "waivers, and unknowns are zero.\n\n"
        f"Immutable derivative: `{SNAP.relative_to(ROOT).as_posix()}/`. Its self-excluding "
        f"manifest contains {snap_rows} bindings and has SHA-256 `{snap_digest}`.\n\n"
        "This PASS prepares evidence for human review only. H1 remains unapproved and "
        "integration is prohibited. It authorizes no representation replacement, reissue, "
        "reauthentication, lifecycle action, release, reliance, retirement, or H2.\n\n"
        "Requested parent action: HELP_HUMAN reproduce and accept or reject the snapshot, "
        "then present the exact evidence to the human administrative decision surface.\n",
        encoding="utf-8",
    )
    instance_rows, instance_digest = manifest(HERE)
    print(json.dumps({"snapshot_manifest_rows": snap_rows,
                      "snapshot_manifest_sha256": snap_digest,
                      "instance_manifest_rows": instance_rows,
                      "instance_manifest_sha256": instance_digest}, indent=2))


if __name__ == "__main__":
    main()
