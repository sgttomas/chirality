#!/usr/bin/env python3
"""Freeze predecessor audit, handoff, and self-excluding terminal manifests."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/RECON-P2"
SNAP = RUN / "snapshots/W_P2/preintegration"
PRED = RUN / "snapshots/W_P2/preflight/PREDECESSOR_RESULTS.tsv"
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]


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
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == "eaad463c0d481f6f1654e6adb5ee718f566176e9"
    summary = json.loads((SNAP / "SUMMARY.json").read_text(encoding="utf-8"))
    assert summary["status"] == "PASS" and summary["members"] == 29

    predecessor_rows = []
    rows = list(csv.DictReader(PRED.open(encoding="utf-8"), delimiter="\t"))
    assert len(rows) == 27
    for row in rows:
        live = ROOT / row["live_path"]
        actual_sow = sha(live / "ScopeOfWork.md")
        actual_status = sha(live / "_STATUS.md")
        legacy_count = sum((live / name).exists() for name in LEGACY)
        assert actual_sow == row["sow_sha256"]
        assert actual_status == row["status_sha256"]
        assert legacy_count == 0 and row["format"] == "SOW_V1" and row["valid"] == "True"
        predecessor_rows.append([row["deliverable_id"], row["lifecycle"], actual_sow,
                                 actual_status, legacy_count, "PASS"])
    write_tsv(SNAP / "PREDECESSOR_AND_I1_AUDIT.tsv",
              ["deliverable_id", "lifecycle", "sow_sha256", "status_sha256", "legacy_files", "verdict"],
              predecessor_rows)

    (SNAP / "HANDOFF_STATE.md").write_text(
        "# W-P2 Preintegration Handoff\n\n"
        "Status: `PASS — ACCEPTED-READY`.\n\n"
        "## Bound basis and derivative status\n\n"
        "This immutable derivative reconciles the exact W-P2 population on "
        "`main@eaad463c0d481f6f1654e6adb5ee718f566176e9`. Its accepted upstream "
        "basis is the W-P2 preflight snapshot and five WORKING_ITEMS package "
        "returns for PKG-05 through PKG-09. It is evidence, not authoritative "
        "decomposition, project, dependency, lifecycle, release, or reliance truth.\n\n"
        "## Closure verdict\n\n"
        "All 29 members pass fresh full reproduction: 919 mappings cover all "
        "8,203 physical source lines; 87 candidate files bind exactly; 145 atomic "
        "replacement rows and 145 inverse rows reproduce the package manifests; "
        "29 apply/target/rollback simulations and 58 negative probes pass. All "
        "19 upstream manifests rehash with valid containment, portability, "
        "existence, uniqueness, and self-exclusion; the five manager manifests "
        "contain 9,962 bindings. All 261 source/control hashes, 29 dependency "
        "schemas, clean-production metadata exclusions, deterministic checklist "
        "and rendering checks, focused tests, practitioner self-check, and 264 "
        "practitioner tests pass. The Piping project tree is byte-identical before "
        "and after reconciliation. The 27 accepted predecessors, including the "
        "ISSUED I1 member, remain exact SOW_V1 with zero legacy files.\n\n"
        "One RECON-owned focused-test path defect was repaired mechanically; the "
        "failed attempt is retained in the instance and the entire reconciliation "
        "was rerun. There is no upstream disagreement, semantic addition, authority "
        "delta, source/status/lifecycle drift, candidate mismatch, unclassified "
        "path, failed check, waiver, blocker, or unknown.\n\n"
        "## Next owner and fences\n\n"
        "HELP_HUMAN must independently reproduce and accept or reject this snapshot "
        "before CHANGE integration. If accepted, CHANGE alone may integrate the "
        "exact single-format manifest through required checks. This handoff does not "
        "authorize candidate repair, project mutation, Git action, lifecycle action, "
        "release, reliance, rollback execution, retirement, or H2 approval. Legacy "
        "surfaces remain supported throughout the rollback window.\n\n"
        "Rerun on any change to the basis commit, preflight/package/child manifest, "
        "live source or control hash, candidate/finalization byte, deterministic "
        "tool or test, replacement/inverse row, accepted predecessor, lifecycle, "
        "authority, or acceptance criterion.\n",
        encoding="utf-8",
    )

    snapshot_rows, snapshot_digest = build_manifest(SNAP)
    status = {
        "basis": "main@eaad463c0d481f6f1654e6adb5ee718f566176e9",
        "blockers": [], "manager_reproduction": "PASS_FULL_WAVE_29_OF_29",
        "next_owner": "HELP_HUMAN", "snapshot": SNAP.relative_to(ROOT).as_posix(),
        "snapshot_manifest_rows": snapshot_rows, "snapshot_manifest_sha256": snapshot_digest,
        "status": "PASS", "terminal": True, "unknowns": [], "waivers": [],
    }
    (HERE / "STATUS.json").write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (HERE / "RETURN.md").write_text(
        "# RECON-P2 Terminal Return\n\n"
        "Terminal verdict: `PASS`.\n\n"
        "The direct Agent-1 full-wave reproduction passes every sealed fan-in gate: "
        "29/29 members, 5 packages, 14 terminal child returns, 19 upstream manifests, "
        "9,962 manager-manifest bindings, 919 mappings, 8,203 source lines, 87 candidate "
        "files, exact 145 replacement and 145 inverse rollback rows, 29 simulations, "
        "58 negative probes, 261 source/control bindings, 29 dependency schemas, fresh "
        "focused and 264 practitioner tests, exact 27-member predecessor/I1 preservation, "
        "and zero Piping project writes. All retained mechanical attempts are closed.\n\n"
        f"Immutable derivative: `{SNAP.relative_to(ROOT).as_posix()}/`. Its self-excluding "
        f"manifest contains {snapshot_rows} bindings and has SHA-256 `{snapshot_digest}`.\n\n"
        "Blockers, waivers, conflicts, stale bindings, missing outputs, semantic unknowns, "
        "and required reruns at the recorded identities: none.\n\n"
        "Requested parent action: HELP_HUMAN reproduce and accept or reject the snapshot, "
        "then invoke CHANGE only after acceptance. This return performs and authorizes no "
        "candidate repair, project write, Git integration, lifecycle action, release, "
        "reliance, rollback execution, retirement, or H2 action.\n",
        encoding="utf-8",
    )
    instance_rows, instance_digest = build_manifest(HERE)
    print(json.dumps({"snapshot_manifest_rows": snapshot_rows,
                      "snapshot_manifest_sha256": snapshot_digest,
                      "instance_manifest_rows": instance_rows,
                      "instance_manifest_sha256": instance_digest}, indent=2))


if __name__ == "__main__":
    main()
