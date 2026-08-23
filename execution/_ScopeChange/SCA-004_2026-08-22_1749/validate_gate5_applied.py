#!/usr/bin/env python3
"""Validate the live SCA-004 Gate-5 applied state deterministically."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


SNAPSHOT_REL = Path("execution/_ScopeChange/SCA-004_2026-08-22_1749")
DECOMP_REL = Path("execution/_Decomposition")

MAIN = "Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
DELIVERABLES = "chirality_root_deliverable_register_v1_0.csv"
LEDGER = "chirality_root_scope_ledger_v1_0.csv"
OBJECTIVES = "chirality_root_objective_register_v1_0.csv"
FORWARD = "chirality_root_prd_coverage_forward_v1_0.csv"
REVERSE = "chirality_root_trace_reverse_v1_0.csv"
TELEMETRY = "chirality_root_coverage_telemetry_v1_0.md"
SURFACES = [MAIN, DELIVERABLES, LEDGER, OBJECTIVES, FORWARD, REVERSE, TELEMETRY]

EXPECTED_CANDIDATE = {
    MAIN: "0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641",
    DELIVERABLES: "2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba",
    LEDGER: "54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc",
    OBJECTIVES: "b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f",
    FORWARD: "9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f",
    REVERSE: "750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438",
    TELEMETRY: "316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765",
}

EXPECTED_APPLIED = {
    MAIN: "546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986",
    DELIVERABLES: "2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba",
    LEDGER: "63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417",
    OBJECTIVES: "b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f",
    FORWARD: "9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f",
    REVERSE: "750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438",
    TELEMETRY: "bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c",
}

PROTECTED = {
    SNAPSHOT_REL / "Gate_5_Application_Append.diff": "336405845dde5a3ae406b46c750c38a88c1b366f69bdaa74b4078679e04fe6a8",
    SNAPSHOT_REL / "Gate_5_Applied_Preview.md": "eb4a9236e7b6d007ebf11aff75bc3e86884d7158d7b753933b3130d523423d03",
    SNAPSHOT_REL / "Gate_5_Slot_Inventory.md": "79929dfd8a299904d95fa0ab83b7b044452528ecf6e39bc57717675e39928e22",
    SNAPSHOT_REL / "Gate_5_Validation.json": "4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966",
    SNAPSHOT_REL / "validate_gate5_package.py": "8dd6e92577fceba1693e6c1605c9863d33c97002ea47e36a3f05d724d7a157e3",
    SNAPSHOT_REL / "Gate_5_Brief.md": "7f0ab64a16d70c7b48c7f51ed4bbfc3bbd5569bed3fdd05343de1ffe2b7d01de",
    Path("execution/_ScopeChange/_LATEST.md"): "4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c",
}

NEW_DELIVERABLES = {
    "DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control": "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers",
    "DEL-02-08_Exact_Supply_and_Protocol_Pinning": "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers",
    "DEL-02-09_Hosted_Account_and_Consent_Boundary": "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers",
    "DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2": "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers",
    "DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation": "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers",
    "DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in": "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers",
    "DEL-04-11_Root_Loop_Receipt_Validator": "PKG-04_Developmental_Machinery_and_Change_Control",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def status_paths(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    paths: list[str] = []
    for line in result.stdout.splitlines():
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    return paths


def parse_args() -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    snapshot = root / SNAPSHOT_REL
    decomp = root / DECOMP_REL
    candidate = snapshot / "Gate_3_Candidate"
    applied = snapshot / "Gate_5_Applied_Candidate"
    output = args.output or snapshot / "Gate_5_Applied_Validation.json"
    if not output.is_absolute():
        output = root / output

    checks: list[dict[str, object]] = []

    def check(condition: bool, name: str, details: object) -> None:
        checks.append({"check": name, "status": "PASS" if condition else "FAIL", "details": details})

    for name, expected in EXPECTED_CANDIDATE.items():
        observed = sha256(candidate / name)
        check(observed == expected, f"approved_candidate_sha::{name}", f"observed={observed} expected={expected}")
    for name, expected in EXPECTED_APPLIED.items():
        preview_observed = sha256(applied / name)
        live_observed = sha256(decomp / name)
        check(preview_observed == expected, f"applied_candidate_sha::{name}", f"observed={preview_observed} expected={expected}")
        check(live_observed == expected, f"live_applied_sha::{name}", f"observed={live_observed} expected={expected}")
        check((decomp / name).read_bytes() == (applied / name).read_bytes(), f"live_equals_applied_candidate::{name}", "byte-for-byte")

    for rel, expected in PROTECTED.items():
        observed = sha256(root / rel)
        check(observed == expected, f"protected_published_sha::{rel.as_posix()}", f"observed={observed} expected={expected}")

    candidate_names = sorted(path.name for path in candidate.iterdir() if path.is_file())
    applied_names = sorted(path.name for path in applied.iterdir() if path.is_file())
    check(candidate_names == sorted(SURFACES), "candidate_exact_file_set", candidate_names)
    check(applied_names == sorted(SURFACES), "applied_exact_file_set", applied_names)

    parsed: dict[str, tuple[list[str], list[dict[str, str]], list[dict[str, str]]]] = {}
    for name in [DELIVERABLES, LEDGER, OBJECTIVES, FORWARD, REVERSE]:
        live_fields, live_rows = read_rows(decomp / name)
        applied_fields, applied_rows = read_rows(applied / name)
        parsed[name] = (live_fields, live_rows, applied_rows)
        check(live_fields == applied_fields, f"header_matches_applied::{name}", live_fields)
        check(live_rows == applied_rows, f"rows_match_applied::{name}", len(live_rows))

    deliverable_rows = parsed[DELIVERABLES][1]
    ledger_rows = parsed[LEDGER][1]
    objective_rows = parsed[OBJECTIVES][1]
    forward_rows = parsed[FORWARD][1]
    reverse_rows = parsed[REVERSE][1]
    deliverable_map = {row["DeliverableID"]: row for row in deliverable_rows}
    objective_map = {row["ObjectiveID"]: row for row in objective_rows}
    parent_counts = Counter(row["ParentPackageID"] for row in deliverable_rows)

    check(len(deliverable_rows) == 53, "deliverable_count_53", len(deliverable_rows))
    check(parent_counts["PKG-02_Operative_Instruction_Surface_and_Runtime_Layers"] == 12, "pkg02_count_12", dict(parent_counts))
    check(parent_counts["PKG-04_Developmental_Machinery_and_Change_Control"] == 11, "pkg04_count_11", dict(parent_counts))
    check(len(parent_counts) == 6, "package_count_6", dict(parent_counts))
    check(len(ledger_rows) == 104, "scope_item_count_104", len(ledger_rows))
    check(len(objective_rows) == 7, "objective_count_7", len(objective_rows))
    check(len(forward_rows) == 85, "forward_trace_rows_85", len(forward_rows))
    check(len(reverse_rows) == 59, "reverse_trace_rows_59", len(reverse_rows))
    check(
        set(deliverable_map) == {row["DeliverableID"] for row in parsed[DELIVERABLES][2]},
        "deliverable_id_set_matches_applied",
        len(deliverable_map),
    )

    new_row_failures: list[str] = []
    for deliverable_id, parent in NEW_DELIVERABLES.items():
        row = deliverable_map.get(deliverable_id)
        if not row:
            new_row_failures.append(f"{deliverable_id}:missing")
            continue
        if row["ParentPackageID"] != parent:
            new_row_failures.append(f"{deliverable_id}:parent={row['ParentPackageID']}")
        if not row["CoversScopeItems"]:
            new_row_failures.append(f"{deliverable_id}:no-scope")
        if not row["SupportsObjectives"]:
            new_row_failures.append(f"{deliverable_id}:no-objective")
    check(not new_row_failures, "every_new_deliverable_parented_and_mapped", new_row_failures)

    unsupported_objectives = [row["ObjectiveID"] for row in objective_rows if not row["MappedDeliverables"] or not row["MappedScopeItems"]]
    check(not unsupported_objectives, "every_objective_supported", unsupported_objectives)
    unmapped_in = [
        row["ScopeItemID"]
        for row in ledger_rows
        if row["InOutStatus"] == "IN" and (not row["PackageID"] or not row["DeliverableIDs"])
    ]
    check(not unmapped_in, "zero_unmapped_in_scope_items", unmapped_in)
    untraced = [row["UnitID"] for row in reverse_rows if row["TraceStatus"] != "TRACED"]
    check(not untraced, "zero_untraced_reverse_units", untraced)
    check(set(objective_map) == {f"OBJ-{index:03d}" for index in range(1, 8)}, "objective_id_set_complete", sorted(objective_map))

    missing_folders: list[str] = []
    for deliverable_id in NEW_DELIVERABLES:
        package_prefix = deliverable_id[4:6]
        matches = list(root.glob(f"execution/PKG-{package_prefix}_*/1_Working/{deliverable_id}*"))
        if matches:
            missing_folders.extend(path.relative_to(root).as_posix() for path in matches)
    check(not missing_folders, "candidate_live_folders_absent", missing_folders)

    forbidden_changed = [
        path
        for path in status_paths(root)
        if Path(path).name in {"_STATUS.md", "ScopeOfWork.md", "_DEPENDENCIES.md"}
    ]
    check(not forbidden_changed, "no_status_sow_or_dependencies_changed_vs_basis", forbidden_changed)

    main_text = (decomp / MAIN).read_text(encoding="utf-8")
    telemetry_text = (decomp / TELEMETRY).read_text(encoding="utf-8")
    check("(v1.3 — ACCEPTED CURRENT BASIS)" in main_text, "live_working_surface_applied_posture", "accepted-current-basis title")
    check("v1.3 — applied revision 1.3" in telemetry_text, "live_telemetry_applied_posture", "applied revision status")

    failures = [item for item in checks if item["status"] == "FAIL"]
    report = {
        "amendment": "SCA-004",
        "gate": 5,
        "posture": "LIVE_APPLIED_STATE",
        "root": str(root),
        "result": "PASS" if not failures else "FAIL",
        "check_count": len(checks),
        "failure_count": len(failures),
        "expected_topology": {
            "deliverables": 53,
            "pkg_02_deliverables": 12,
            "pkg_04_deliverables": 11,
            "packages": 6,
            "scope_items": 104,
            "objectives": 7,
            "forward_rows": 85,
            "reverse_rows": 59,
        },
        "live_sha256": {name: sha256(decomp / name) for name in SURFACES},
        "checks": checks,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{report['result']}: {len(checks)} checks, {len(failures)} failures -> {output}")
    for failure in failures:
        print(f"  FAIL {failure['check']}: {failure['details']}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
