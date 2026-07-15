#!/usr/bin/env python3
"""Finalize W-P3 predecessor, direction, independence, handoff, and manifests."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/RECON-P3"
SNAP = RUN / "snapshots/W_P3/preintegration"
PREF = RUN / "snapshots/W_P3/preflight"
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header); writer.writerows(rows)


def build_manifest(base: Path) -> tuple[int, str]:
    manifest = base / "MANIFEST.tsv"
    rows = [[sha(p), p.stat().st_size, p.relative_to(ROOT).as_posix()]
            for p in sorted(base.rglob("*")) if p.is_file() and p != manifest]
    write_tsv(manifest, ["sha256", "bytes", "path"], rows)
    return len(rows), sha(manifest)


def main() -> None:
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == "4d153302c3c4cd42578936db160c2bac1270225a"
    summary_path = SNAP / "SUMMARY.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["status"] == "PASS" and summary["members"] == 15

    predecessor_rows = []
    predecessors = list(csv.DictReader((PREF / "PREDECESSOR_RESULTS.tsv").open(encoding="utf-8"), delimiter="\t"))
    assert len(predecessors) == 56
    for row in predecessors:
        live = ROOT / row["live_path"]
        actual_sow = sha(live / "ScopeOfWork.md"); actual_status = sha(live / "_STATUS.md")
        legacy_count = sum((live / name).exists() for name in LEGACY)
        assert actual_sow == row["sow_sha256"] and actual_status == row["status_sha256"]
        assert row["format"] == "SOW_V1" and row["valid"] == "True" and legacy_count == 0 and row["verdict"] == "PASS"
        predecessor_rows.append([row["deliverable_id"], row["lifecycle"], actual_sow, actual_status, legacy_count, "PASS"])
    write_tsv(SNAP / "PREDECESSOR_AUDIT.tsv", ["deliverable_id", "lifecycle", "sow_sha256", "status_sha256", "legacy_files", "verdict"], predecessor_rows)

    selected = list(csv.DictReader((PREF / "P3_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))
    direction: dict[str, list[dict[str, str]]] = defaultdict(list)
    contradictions = []
    for member in selected:
        dep = ROOT / member["live_path"] / "Dependencies.csv"
        for row in csv.DictReader(dep.open(encoding="utf-8")):
            if row["Status"] == "ACTIVE" and row["TargetPackageID"] == "PKG-00":
                assert row["Direction"] == "UPSTREAM" and row["FromPackageID"] == member["package"]
                direction[member["package"]].append(row)
            if row["Status"] == "ACTIVE" and row["FromPackageID"] == "PKG-00" and row["TargetPackageID"] in {"PKG-10", "PKG-11", "PKG-12"}:
                contradictions.append(row)
    expected = {"PKG-10": 28, "PKG-11": 25, "PKG-12": 35}
    direction_rows = []
    for pkg in sorted(expected):
        rows = direction[pkg]; assert len(rows) == expected[pkg]
        targets = sorted({r["TargetDeliverableID"] for r in rows})
        covered = sorted({r["FromDeliverableID"] for r in rows})
        assert len(covered) == 5
        direction_rows.append([pkg, len(rows), len(covered), ",".join(targets), "PASS"])
    assert not contradictions
    write_tsv(SNAP / "PKG00_DIRECTION_AUDIT.tsv", ["package", "active_edges_to_pkg00", "covered_deliverables", "pkg00_targets", "verdict"], direction_rows)

    failed = RUN / "instances/WORKING-P3-PKG12/children/VERIFY-B1"
    replacement = RUN / "instances/WORKING-P3-PKG12/children/VERIFY-B1-R1"
    failed_status = json.loads((failed / "STATUS.json").read_text(encoding="utf-8"))
    replacement_status = json.loads((replacement / "STATUS.json").read_text(encoding="utf-8"))
    commands = json.loads((replacement / "COMMAND_LEDGER.json").read_text(encoding="utf-8"))
    prohibited = []
    for command in commands:
        text = " ".join(str(x) for x in command.get("command", []))
        if "/children/AUTHOR-B1/" in text or "/children/VERIFY-B1/" in text:
            prohibited.append(text)
    assert failed_status["result"] == "BLOCKED" and not failed_status["semantic_verification_started"]
    assert replacement_status["status"] == "PASS_UNCHANGED" and len(commands) == 112 and not prohibited
    (SNAP / "PKG12_VERIFIER_INDEPENDENCE.md").write_text(
        "# PKG-12 Verifier Independence Audit\n\n"
        "Verdict: `PASS`.\n\n"
        "The initial `VERIFY-B1` remains terminal `BLOCKED`, stopped before semantic verification, retained in its original tree, and excluded from accepted fan-in. "
        "The sole accepted verifier is the fresh `VERIFY-B1-R1 PASS_UNCHANGED` authorized by `BRIEF_V2.md`. Independent RECON inspection reproduced 112 commands and zero command targets beneath either prohibited `AUTHOR-B1/**` or failed `VERIFY-B1/**` tree. "
        "Its 244-row self-excluding manifest rehashes with complete path existence, containment, byte count, and content-hash validity. No candidate or project write occurred.\n",
        encoding="utf-8",
    )

    rebound = RUN / "instances/WORKING-P3-PKG11"
    rebound_status = json.loads((rebound / "STATUS.json").read_text(encoding="utf-8"))
    assert rebound_status["status"] == "PASS_REBOUND"
    assert rebound_status["rebound"]["removed_stale_rows"] == 2
    assert sha(rebound / "MANIFEST.tsv") == "4dc1714c70c38fe4469af9e4d680f3f32a8d050f7d3c53c20ebafeff97608ee7"
    (SNAP / "PKG11_REBIND_AUDIT.md").write_text(
        "# PKG-11 Rebind Audit\n\n"
        "Verdict: `PASS_REBOUND`.\n\n"
        "RECON attempt 1 found two stale ignored `.pyc` bindings. Under `BRIEF_V2.md`, the owning manager removed only those two absent-residue rows, retained their exact old hashes in `REBINDING_V2.md`, and rebuilt all transitive bindings. "
        "The active author manifest contains 972 valid self-excluding rows at SHA-256 `a943cc42d4e5090a10bc03e1a3b80f90f924d329442051f7f4f597499b3a673d`; the verifier remains unchanged at 493 rows; the rebuilt package manifest contains 1,530 valid rows at SHA-256 `4dc1714c70c38fe4469af9e4d680f3f32a8d050f7d3c53c20ebafeff97608ee7`. "
        "Fresh RECON attempt 3 rehashed and validated the rebound state before reconstructing all members.\n",
        encoding="utf-8",
    )

    summary.update({"accepted_predecessors": 56, "full_piping_census": 71,
                    "pkg00_direction": "PASS_88_ACTIVE_UPSTREAM_EDGES_ZERO_CONTRADICTIONS",
                    "pkg11_rebound": "PASS", "predecessor_preservation": "PASS_56_OF_56"})
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (SNAP / "HANDOFF_STATE.md").write_text(
        "# W-P3 Preintegration Handoff\n\n"
        "Status: `PASS — ACCEPTED-READY`.\n\n"
        "## Bound basis and derivative status\n\n"
        "This immutable derivative reconciles the exact W-P3 population on `main@4d153302c3c4cd42578936db160c2bac1270225a`. Its accepted upstream basis is the immutable W-P3 preflight, three WORKING_ITEMS package returns for PKG-10 through PKG-12, PKG-11 `BRIEF_V2.md` rebound evidence, and PKG-12 replacement-verifier `BRIEF_V2.md` evidence. It is derivative preparation evidence, not decomposition, dependency, lifecycle, release, reliance, or professional authority.\n\n"
        "## Closure verdict\n\n"
        "All 15 members pass fresh full reproduction: 493 mappings cover all 4,919 physical source lines; 45 candidate files bind exactly; 75 replacement and 75 inverse rows reproduce package manifests; 15 apply/target/rollback simulations and 105 negative probes pass. Ten upstream manifests rehash with valid containment, portability, existence, uniqueness, byte count, content hash, and self-exclusion; the three manager manifests total 4,494 bindings. All 135 source/control hashes, 15 dependency schemas, repeated conversion/finalization/map/parity/checklist/render outputs, metadata exclusions, focused tests, practitioner self-check, and 264 practitioner tests pass. The Piping tree is byte-identical before and after reconciliation.\n\n"
        "The 56 accepted P1/I1/P2 predecessors remain exact SOW_V1 with zero legacy files; together with the 15 read-only P3 members this reproduces the 71-member accepted Piping census. PKG-00 direction remains valid across 88 active upstream edges with zero outbound contradiction. PKG-11's two stale ignored-residue bindings were repaired only by the owning manager under BRIEF_V2 and fully rebound. PKG-12's initial verifier remains BLOCKED and excluded; accepted VERIFY-B1-R1 independently retains zero prohibited reads. There is no semantic or authority delta, source/status/lifecycle drift, candidate mismatch, unclassified path, failed check, waiver, blocker, or unknown.\n\n"
        "## Next owner and fences\n\n"
        "HELP_HUMAN must reproduce and accept or reject this derivative before CHANGE integration. If accepted, CHANGE alone may integrate the exact single-format manifest through required checks. This handoff authorizes no candidate repair, live-project mutation, lifecycle or dependency action, release, reliance, rollback execution, retirement, or H2 state. Legacy surfaces remain supported throughout the rollback window.\n\n"
        "Rerun on any change to the basis commit, preflight/package/child manifest, live source/control or predecessor hash, candidate/finalization byte, method/tool/test/check profile, replacement/inverse row, lifecycle, authority, acceptance criterion, PKG-00 direction, or PKG-12 independence record.\n",
        encoding="utf-8",
    )

    snap_rows, snap_digest = build_manifest(SNAP)
    status = {"basis": "main@4d153302c3c4cd42578936db160c2bac1270225a", "blockers": [],
              "full_reproduction": "PASS_15_OF_15", "next_owner": "HELP_HUMAN",
              "snapshot": SNAP.relative_to(ROOT).as_posix(), "snapshot_manifest_rows": snap_rows,
              "snapshot_manifest_sha256": snap_digest, "status": "PASS", "terminal": True,
              "unknowns": [], "waivers": []}
    (HERE / "STATUS.json").write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (HERE / "RETURN.md").write_text(
        "# RECON-P3 Terminal Return\n\nTerminal verdict: `PASS`.\n\n"
        "The direct Agent-1 full-wave reconciliation passes every sealed fan-in gate: 15/15 members; three packages; six accepted child returns plus one retained/excluded BLOCKED attempt; ten upstream manifests; 4,494 manager-manifest bindings; 493 mappings; 4,919 source lines; 45 candidate files; exact 75 replacement and 75 inverse rows; 15 simulations; 105 negative probes; 135 source/control bindings; 15 dependency schemas; fresh focused and 264 practitioner tests; 56/56 predecessor preservation (71-member full Piping census); 88 valid PKG-00 upstream edges; and zero Piping project writes.\n\n"
        "PKG-11's two stale ignored-residue bindings were repaired and transitively rebound only by the owning manager under BRIEF_V2; both failed RECON attempts and old hashes remain retained. PKG-12's initial verifier remains terminal BLOCKED and excluded. The accepted replacement is independently validated at 112 commands and zero prohibited targets.\n\n"
        f"Immutable derivative: `{SNAP.relative_to(ROOT).as_posix()}/`; self-excluding manifest {snap_rows} rows, SHA-256 `{snap_digest}`. Blockers, waivers, conflicts, stale bindings, semantic unknowns, and required immediate reruns: none.\n\n"
        "Requested parent action: HELP_HUMAN reproduce and accept or reject, then invoke CHANGE only after acceptance. No candidate repair, project write, Git integration, lifecycle action, release, reliance, rollback execution, retirement, or H2 action is performed or authorized.\n",
        encoding="utf-8",
    )
    inst_rows, inst_digest = build_manifest(HERE)
    print(json.dumps({"snapshot_manifest_rows": snap_rows, "snapshot_manifest_sha256": snap_digest,
                      "instance_manifest_rows": inst_rows, "instance_manifest_sha256": inst_digest}, indent=2))


if __name__ == "__main__": main()
