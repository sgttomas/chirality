#!/usr/bin/env python3
"""Finalize W-P4 predecessor, direction, handoff, and immutable manifests."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/RECON-P4"
SNAP = RUN / "snapshots/W_P4/preintegration"
PREF = RUN / "snapshots/W_P4/preflight"
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
BASIS = "e8f59a63372f38d9e788ac39b39995558f5aba73"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def build_manifest(base: Path) -> tuple[int, str]:
    manifest = base / "MANIFEST.tsv"
    rows = [[sha(p), p.stat().st_size, p.relative_to(ROOT).as_posix()]
            for p in sorted(base.rglob("*")) if p.is_file() and p != manifest]
    write_tsv(manifest, ["sha256", "bytes", "path"], rows)
    return len(rows), sha(manifest)


def main() -> None:
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == BASIS
    summary_path = SNAP / "SUMMARY.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["status"] == "PASS" and summary["members"] == 22

    predecessor_rows = []
    predecessors = list(csv.DictReader((PREF / "PREDECESSOR_RESULTS.tsv").open(encoding="utf-8"), delimiter="\t"))
    assert len(predecessors) == 71
    for row in predecessors:
        live = ROOT / row["live_path"]
        actual_sow = sha(live / "ScopeOfWork.md")
        actual_status = sha(live / "_STATUS.md")
        legacy_count = sum((live / name).exists() for name in LEGACY)
        assert actual_sow == row["sow_sha256"] and actual_status == row["status_sha256"]
        assert row["format"] == "SOW_V1" and row["valid"] == "True" and legacy_count == 0 and row["verdict"] == "PASS"
        predecessor_rows.append([row["deliverable_id"], row["lifecycle"], actual_sow, actual_status, legacy_count, "PASS"])
    write_tsv(SNAP / "PREDECESSOR_AUDIT.tsv", ["deliverable_id", "lifecycle", "sow_sha256", "status_sha256", "legacy_files", "verdict"], predecessor_rows)

    selected = list(csv.DictReader((PREF / "P4_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))
    direction: dict[str, list[dict[str, str]]] = defaultdict(list)
    contradictions = []
    wave_packages = {"PKG-14", "PKG-15", "PKG-16", "PKG-17"}
    for member in selected:
        dep = ROOT / member["live_path"] / "Dependencies.csv"
        for row in csv.DictReader(dep.open(encoding="utf-8")):
            if row["Status"] == "ACTIVE" and row["TargetPackageID"] == "PKG-00":
                assert row["Direction"] == "UPSTREAM" and row["FromPackageID"] == member["package"]
                direction[member["package"]].append(row)
            if row["Status"] == "ACTIVE" and row["FromPackageID"] == "PKG-00" and row["TargetPackageID"] in wave_packages:
                contradictions.append(row)
    expected = {"PKG-14": 35, "PKG-15": 28, "PKG-16": 28, "PKG-17": 66}
    expected_members = {"PKG-14": 5, "PKG-15": 4, "PKG-16": 4, "PKG-17": 9}
    direction_rows = []
    for pkg in sorted(expected):
        rows = direction[pkg]
        assert len(rows) == expected[pkg]
        targets = sorted({r["TargetDeliverableID"] for r in rows})
        covered = sorted({r["FromDeliverableID"] for r in rows})
        assert len(covered) == expected_members[pkg]
        direction_rows.append([pkg, len(rows), len(covered), ",".join(targets), "PASS"])
    assert not contradictions and sum(expected.values()) == 157
    write_tsv(SNAP / "PKG00_DIRECTION_AUDIT.tsv", ["package", "active_edges_to_pkg00", "covered_deliverables", "pkg00_targets", "verdict"], direction_rows)

    summary.update({"accepted_predecessors": 71, "full_piping_census": 93,
                    "pkg00_direction": "PASS_157_ACTIVE_UPSTREAM_EDGES_ZERO_CONTRADICTIONS",
                    "predecessor_preservation": "PASS_71_OF_71",
                    "retained_recon_mechanical_attempts": 1})
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    (SNAP / "HANDOFF_STATE.md").write_text(
        "# W-P4 Preintegration Handoff\n\n"
        "Status: `PASS — ACCEPTED-READY`.\n\n"
        "## Bound basis and derivative status\n\n"
        f"This immutable derivative reconciles the exact W-P4 population on `main@{BASIS}`. Its accepted upstream basis is the immutable W-P4 preflight and four WORKING_ITEMS package returns for PKG-14 through PKG-17. It is derivative preparation evidence, not decomposition, dependency, lifecycle, release, reliance, retirement, H2, or professional authority.\n\n"
        "## Closure verdict\n\n"
        "All 22 members pass fresh full reproduction: 729 mappings cover all 6,759 physical source lines; 66 candidate files bind exactly; 110 replacement and 110 inverse rows reproduce package manifests; 22 apply/target/rollback simulations and 154 negative probes pass. Fourteen upstream manifests rehash with valid containment, portability, existence, uniqueness, byte count, content hash, and self-exclusion; the four manager manifests total 5,658 bindings. All 198 source/control hashes, 22 dependency schemas, repeated conversion/finalization/map/parity/checklist/render outputs, metadata exclusions, focused tests, practitioner self-check, and 264 practitioner tests pass. The Piping tree is byte-identical before and after reconciliation.\n\n"
        "The 71 accepted P1/I1/P2/P3 predecessors remain exact SOW_V1 with zero legacy files; together with the 22 read-only P4 members this reproduces the 93-member accepted Piping census. PKG-00 direction remains valid across 157 active upstream edges with zero outbound contradiction. One failed RECON-owned manifest-schema binding attempt remains retained; it caused no upstream or project mutation and the complete reconciliation was restarted after rebinding. There is no semantic or authority delta, source/status/lifecycle drift, candidate mismatch, unclassified path, failed final check, waiver, blocker, or unknown.\n\n"
        "## Next owner and fences\n\n"
        "HELP_HUMAN must reproduce and accept or reject this derivative before CHANGE integration. If accepted, CHANGE alone may integrate the exact single-format manifest through required checks. This handoff authorizes no candidate repair, live-project mutation, lifecycle or dependency action, release, reliance, rollback execution, retirement, or H2 state. All H2 and retirement fences remain intact, and legacy surfaces remain supported throughout the rollback window.\n\n"
        "Rerun on any change to the basis commit, preflight/package/child manifest, live source/control or predecessor hash, candidate/finalization byte, method/tool/test/check profile, replacement/inverse row, lifecycle, authority, acceptance criterion, PKG-00 direction, H2 fence, or retirement fence.\n",
        encoding="utf-8",
    )

    snap_rows, snap_digest = build_manifest(SNAP)
    status = {"basis": f"main@{BASIS}", "blockers": [], "full_reproduction": "PASS_22_OF_22",
              "next_owner": "HELP_HUMAN", "snapshot": SNAP.relative_to(ROOT).as_posix(),
              "snapshot_manifest_rows": snap_rows, "snapshot_manifest_sha256": snap_digest,
              "status": "PASS", "terminal": True, "unknowns": [], "waivers": []}
    (HERE / "STATUS.json").write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (HERE / "RETURN.md").write_text(
        "# RECON-P4 Terminal Return\n\nTerminal verdict: `PASS`.\n\n"
        "The direct Agent-1 full-wave reconciliation passes every sealed fan-in gate: 22/22 members; four packages; ten accepted child returns; fourteen upstream manifests; 5,658 manager-manifest bindings; 729 mappings; 6,759 source lines; 66 candidate files; exact 110 replacement and 110 inverse rows; 22 simulations; 154 negative probes; 198 source/control bindings; 22 dependency schemas; fresh focused and 264 practitioner tests; 71/71 predecessor preservation (93-member full Piping census); 157 valid PKG-00 upstream edges; and zero Piping project writes.\n\n"
        "One failed RECON-owned P4 manifest-schema binding attempt is retained. The harness was rebound to the registered P4 schema and the entire reconciliation restarted; no upstream, candidate, or project state was changed.\n\n"
        f"Immutable derivative: `{SNAP.relative_to(ROOT).as_posix()}/`; self-excluding manifest {snap_rows} rows, SHA-256 `{snap_digest}`. Blockers, waivers, conflicts, stale bindings, semantic unknowns, and required immediate reruns: none.\n\n"
        "Requested parent action: HELP_HUMAN reproduce and accept or reject, then invoke CHANGE only after acceptance. No candidate repair, project write, Git integration, lifecycle action, release, reliance, rollback execution, retirement, or H2 action is performed or authorized.\n",
        encoding="utf-8",
    )
    inst_rows, inst_digest = build_manifest(HERE)
    print(json.dumps({"snapshot_manifest_rows": snap_rows, "snapshot_manifest_sha256": snap_digest,
                      "instance_manifest_rows": inst_rows, "instance_manifest_sha256": inst_digest}, indent=2))


if __name__ == "__main__":
    main()
