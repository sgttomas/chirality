#!/usr/bin/env python3
"""Deterministic validation for the SCA-004 Gate-5 draft package."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import tempfile
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT = Path(__file__).resolve().parent
DECOMP = ROOT / "execution" / "_Decomposition"
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"
APPLIED = SNAPSHOT / "Gate_5_Applied_Candidate"
APPEND = SNAPSHOT / "Gate_5_Application_Append.diff"
REPORT = SNAPSHOT / "Gate_5_Validation.json"

MAIN = "Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
DELIVERABLES = "chirality_root_deliverable_register_v1_0.csv"
LEDGER = "chirality_root_scope_ledger_v1_0.csv"
OBJECTIVES = "chirality_root_objective_register_v1_0.csv"
FORWARD = "chirality_root_prd_coverage_forward_v1_0.csv"
REVERSE = "chirality_root_trace_reverse_v1_0.csv"
TELEMETRY = "chirality_root_coverage_telemetry_v1_0.md"
SURFACES = [MAIN, DELIVERABLES, LEDGER, OBJECTIVES, FORWARD, REVERSE, TELEMETRY]

EXPECTED_BASIS = {
    MAIN: "23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d",
    DELIVERABLES: "a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395",
    LEDGER: "3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2",
    OBJECTIVES: "c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55",
    FORWARD: "adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84",
    REVERSE: "6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0",
    TELEMETRY: "6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282",
}

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
    "execution/_ScopeChange/_LATEST.md": "b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1",
    "execution/_Coordination/_TaskManagement/REGISTER.csv": "89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Exact_Amendment.diff": "0724668f6fb85189f4c3ee142a21cef938c8dd47373be543d8b108c8e934637b",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Validation.json": "dc5fe4355322a96b7da61606fff7d8dd51943a7d606f132966705bfb70b9f129",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Amendment_Preview.md": "ff7743554270aee177feed4226a4fa35fd503ce34760f69644176878bcffdca4",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md": "abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Amendment_Actions.csv": "4e623bcc5e69d056f71d9ed860ff729a0dfc9b8d8c635e7dd23b3c6b10d2871d",
}

# One-based candidate line numbers. Inserted/replacement lines may expand on
# the applied side, but every removed candidate line must fall in these slots.
ALLOWED_LINES = {
    MAIN: set([1, 6, 10, 11, *range(13, 24), 285, 419, 494, 579, *range(644, 652)]),
    LEDGER: {84, 104},
    TELEMETRY: {5, 6, 7, 20, 126, 128, 129, 162},
}

SLOT_IDS = [
    *[f"WS-{index:03d}" for index in range(1, 11)],
    "SL-001", "SL-002",
    *[f"TEL-{index:03d}" for index in range(1, 7)],
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def run(command: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, check=check, capture_output=True, text=True)


def copy_surfaces(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for name in SURFACES:
        shutil.copy2(source / name, target / name)


def patch_reproduces(source: Path, patch: Path, expected: Path) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw)
        live = root / "execution" / "_Decomposition"
        copy_surfaces(source, live)
        checked = run(["git", "apply", "--unidiff-zero", "--check", str(patch)], root, check=False)
        if checked.returncode:
            return False, checked.stderr.strip()
        applied = run(["git", "apply", "--unidiff-zero", str(patch)], root, check=False)
        if applied.returncode:
            return False, applied.stderr.strip()
        mismatches = [name for name in SURFACES if (live / name).read_bytes() != (expected / name).read_bytes()]
        return not mismatches, f"mismatches={mismatches}"


def run_gate3_clean(
    input_surfaces: Path,
    applied_posture: bool,
) -> tuple[bool, dict[str, object], str]:
    """Run the Phase-0c 98 checks in a clean scratch Phase-0c layout.

    The Phase-0c validator is copied to a clean temporary repository. Its
    `Gate_3_Candidate/` input is either the exact approved candidate or the
    applied preview. For the applied preview only, current-posture literals
    and the OI-011 lineage literal are inverted, and changed-ledger isolation
    admits the two inventoried status-only `Notes` cells (SOW-083/SOW-103).
    Every mapping, trace, count, basis, containment, and other structural
    check is otherwise the exact Phase-0c code. Gate-5 artifacts are absent
    from the scratch layout, so the legacy `gate5_artifacts_absent` check is
    evaluated in the Phase-0c context it was written for and can never mutate
    the protected live `Gate_3_Validation.json`.
    """
    with tempfile.TemporaryDirectory() as raw:
        temp_root = Path(raw)
        temp_snapshot = temp_root / "execution" / "_ScopeChange" / SNAPSHOT.name
        temp_decomp = temp_root / "execution" / "_Decomposition"
        copy_surfaces(DECOMP, temp_decomp)
        copy_surfaces(input_surfaces, temp_snapshot / "Gate_3_Candidate")

        copy_map = {
            SNAPSHOT / "Amendment_Actions.csv": temp_snapshot / "Amendment_Actions.csv",
            SNAPSHOT / "Handoff_State.md": temp_snapshot / "Handoff_State.md",
            SNAPSHOT / "Gate_3_Exact_Amendment.diff": temp_snapshot / "Gate_3_Exact_Amendment.diff",
            SNAPSHOT / "Brief.md": temp_snapshot / "Brief.md",
            SNAPSHOT / "Gate_1_Validation.md": temp_snapshot / "Gate_1_Validation.md",
            SNAPSHOT / "Parsed_Actions.csv": temp_snapshot / "Parsed_Actions.csv",
            SNAPSHOT / "WORK_GRAPH.json": temp_snapshot / "WORK_GRAPH.json",
            SNAPSHOT / "Evidence" / "AUDIT_DECOMP" / "coverage_summary.json": temp_snapshot / "Evidence" / "AUDIT_DECOMP" / "coverage_summary.json",
            ROOT / "execution" / "_ScopeChange" / "_LATEST.md": temp_root / "execution" / "_ScopeChange" / "_LATEST.md",
        }
        for source, target in copy_map.items():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

        source_code = (SNAPSHOT / "validate_gate3_candidate.py").read_text(encoding="utf-8")
        if applied_posture:
            source_code = source_code.replace(
                '"seven SCA-004 candidate rows"',
                '"seven applied SCA-004 rows"',
            ).replace(
                '"SCA-004 CANDIDATE v1.3",',
                '"v1.3 — ACCEPTED CURRENT BASIS",',
            ).replace(
                '"SCA-004 GATE-3 CANDIDATE — NOT APPROVED OR APPLIED",',
                '"SCA-004 REVISION 1.3 — ACCEPTED CURRENT BASIS",',
            ).replace(
                'changed_ledger == ["SOW-041", "SOW-053", "SOW-104"]',
                'changed_ledger == ["SOW-041", "SOW-053", "SOW-083", "SOW-103", "SOW-104"]',
            )
        validator = temp_snapshot / "validate_gate3_candidate.py"
        validator.write_text(source_code, encoding="utf-8")

        run(["git", "init", "-q"], temp_root)
        run(["git", "config", "user.email", "gate5-validator@example.invalid"], temp_root)
        run(["git", "config", "user.name", "Gate5 Validator"], temp_root)
        run(["git", "add", "."], temp_root)
        run(["git", "commit", "-q", "-m", "validation fixture"], temp_root)
        result = run(["python3", str(validator)], temp_root, check=False)
        report_path = temp_snapshot / "Gate_3_Validation.json"
        report = json.loads(report_path.read_text()) if report_path.exists() else {}
        ok = result.returncode == 0 and report.get("result") == "PASS" and report.get("check_count") == 98 and report.get("failure_count") == 0
        return ok, report, (result.stdout + result.stderr).strip()


def main() -> None:
    checks: list[dict[str, object]] = []

    def check(condition: bool, name: str, details: object) -> None:
        checks.append({"check": name, "status": "PASS" if condition else "FAIL", "details": details})

    for name, expected in EXPECTED_BASIS.items():
        observed = sha256(DECOMP / name)
        check(observed == expected, f"live_basis_untouched::{name}", f"observed={observed} expected={expected}")
    for rel, expected in PROTECTED.items():
        observed = sha256(ROOT / rel)
        check(observed == expected, f"protected_approved_bytes::{rel}", f"observed={observed} expected={expected}")
    for name, expected in EXPECTED_CANDIDATE.items():
        observed = sha256(CANDIDATE / name)
        check(observed == expected, f"approved_candidate_sha::{name}", f"observed={observed} expected={expected}")
    for name, expected in EXPECTED_APPLIED.items():
        observed = sha256(APPLIED / name)
        check(observed == expected, f"applied_preview_sha::{name}", f"observed={observed} expected={expected}")

    candidate_names = sorted(path.name for path in CANDIDATE.iterdir() if path.is_file())
    applied_names = sorted(path.name for path in APPLIED.iterdir() if path.is_file())
    check(candidate_names == sorted(SURFACES), "approved_candidate_exact_file_set", candidate_names)
    check(applied_names == sorted(SURFACES), "applied_candidate_exact_file_set", applied_names)

    gate3_ok, gate3_details = patch_reproduces(DECOMP, SNAPSHOT / "Gate_3_Exact_Amendment.diff", CANDIDATE)
    check(gate3_ok, "gate3_exact_diff_reproduces_approved_candidate", gate3_details)
    gate5_ok, gate5_details = patch_reproduces(CANDIDATE, APPEND, APPLIED)
    check(gate5_ok, "gate5_append_check_and_apply_reproduces_applied_candidate", gate5_details)

    # Exact changed-line containment and untouched-surface proof.
    changed_files: list[str] = []
    out_of_slot: list[str] = []
    for name in SURFACES:
        before = (CANDIDATE / name).read_bytes().splitlines(keepends=True)
        after = (APPLIED / name).read_bytes().splitlines(keepends=True)
        if before != after:
            changed_files.append(name)
        matcher = SequenceMatcher(a=before, b=after, autojunk=False)
        for tag, i1, i2, _j1, _j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            removed_lines = set(range(i1 + 1, i2 + 1))
            if not removed_lines or not removed_lines.issubset(ALLOWED_LINES.get(name, set())):
                out_of_slot.append(f"{name}:{tag}:{i1 + 1}-{i2}")
    check(changed_files == [MAIN, LEDGER, TELEMETRY], "only_three_surfaces_have_status_slots", changed_files)
    check(not out_of_slot, "every_append_change_inside_inventoried_candidate_lines", out_of_slot)

    inventory = (SNAPSHOT / "Gate_5_Slot_Inventory.md").read_text(encoding="utf-8")
    missing_slots = [slot for slot in SLOT_IDS if slot not in inventory]
    check(not missing_slots, "slot_inventory_all_18_ids_present", missing_slots)
    check("No row identity, mapping, count, ID" in inventory, "slot_inventory_structural_exclusion_explicit", "boundary present")

    # CSV equality and structural parity. Only two scope-ledger Notes cells may differ.
    csv_names = [DELIVERABLES, LEDGER, OBJECTIVES, FORWARD, REVERSE]
    key_fields = {
        DELIVERABLES: "DeliverableID",
        LEDGER: "ScopeItemID",
        OBJECTIVES: "ObjectiveID",
        FORWARD: "PRDItem",
        REVERSE: "UnitID",
    }
    permitted_cells = {(LEDGER, "SOW-083", "Notes"), (LEDGER, "SOW-103", "Notes")}
    unexpected_cells: list[str] = []
    parsed: dict[str, tuple[list[str], list[dict[str, str]], list[dict[str, str]]]] = {}
    for name in csv_names:
        fields_before, before_rows = rows(CANDIDATE / name)
        fields_after, after_rows = rows(APPLIED / name)
        parsed[name] = (fields_before, before_rows, after_rows)
        check(fields_before == fields_after, f"csv_header_identical::{name}", fields_after)
        check(len(before_rows) == len(after_rows), f"csv_row_count_identical::{name}", [len(before_rows), len(after_rows)])
        key = key_fields[name]
        before_map = {row[key]: row for row in before_rows}
        after_map = {row[key]: row for row in after_rows}
        check(set(before_map) == set(after_map), f"csv_id_set_identical::{name}", sorted(set(before_map) ^ set(after_map)))
        for identifier in before_map:
            for field in fields_before:
                if before_map[identifier][field] != after_map[identifier][field] and (name, identifier, field) not in permitted_cells:
                    unexpected_cells.append(f"{name}:{identifier}:{field}")
    check(not unexpected_cells, "csv_only_two_inventoried_notes_cells_change", unexpected_cells)

    _, candidate_del, applied_del = parsed[DELIVERABLES]
    candidate_parent = Counter(row["ParentPackageID"] for row in candidate_del)
    applied_parent = Counter(row["ParentPackageID"] for row in applied_del)
    check(candidate_parent == applied_parent, "parent_package_distribution_identical", dict(applied_parent))

    mapping_fields = {
        DELIVERABLES: ["CoversScopeItems", "SupportsObjectives", "ParentPackageID"],
        LEDGER: ["PackageID", "DeliverableIDs", "ObjectiveIDs"],
        OBJECTIVES: ["MappedDeliverables", "MappedScopeItems"],
        FORWARD: ["ObjectiveID", "ScopeItemIDs", "PackageIDs", "DeliverableIDs", "CoverageStatus"],
        REVERSE: ["UnitKind", "ParentPackageID", "PRDItems", "ScopeItemIDs", "TraceStatus"],
    }
    mapping_mismatches: list[str] = []
    for name, fields in mapping_fields.items():
        _, before_rows, after_rows = parsed[name]
        key = key_fields[name]
        before_map = {row[key]: row for row in before_rows}
        after_map = {row[key]: row for row in after_rows}
        for identifier in before_map:
            for field in fields:
                if before_map[identifier][field] != after_map[identifier][field]:
                    mapping_mismatches.append(f"{name}:{identifier}:{field}")
    check(not mapping_mismatches, "scope_objective_parent_and_trace_mappings_identical", mapping_mismatches)
    check(len(parsed[REVERSE][1]) == len(parsed[REVERSE][2]) == 59, "trace_unit_count_identical_59", [len(parsed[REVERSE][1]), len(parsed[REVERSE][2])])

    check(len(applied_del) == 53, "applied_deliverable_count_53", len(applied_del))
    check(applied_parent["PKG-02_Operative_Instruction_Surface_and_Runtime_Layers"] == 12, "applied_pkg02_count_12", dict(applied_parent))
    check(applied_parent["PKG-04_Developmental_Machinery_and_Change_Control"] == 11, "applied_pkg04_count_11", dict(applied_parent))
    check(len(parsed[LEDGER][2]) == 104, "applied_scope_count_104", len(parsed[LEDGER][2]))
    check(len(parsed[OBJECTIVES][2]) == 7, "applied_objective_count_7", len(parsed[OBJECTIVES][2]))

    main_text = (APPLIED / MAIN).read_text(encoding="utf-8")
    telemetry_text = (APPLIED / TELEMETRY).read_text(encoding="utf-8")
    applied_tokens = [
        "(v1.3 — ACCEPTED CURRENT BASIS)",
        "Gate 3 was approved by owner R3-A",
        "Gate 4 was approved by owner R3-B",
        "Gate-5 was executed under owner authorization reference",
        "Git effect `TBD`",
        "pointer treatment pending its own authority",
        "applied revision 1.3",
    ]
    combined = main_text + "\n" + telemetry_text
    check(all(token in combined for token in applied_tokens), "applied_status_tokens_complete", [token for token in applied_tokens if token not in combined])
    forbidden_current = ["SCA-004 GATE-3 CANDIDATE — NOT APPROVED OR APPLIED", "candidate only; accepted revision 1.2 remains live"]
    check(all(token not in combined for token in forbidden_current), "current_candidate_only_posture_removed", [token for token in forbidden_current if token in combined])

    original_ok, original_report, original_output = run_gate3_clean(CANDIDATE, applied_posture=False)
    check(original_ok, "approved_candidate_gate3_clean_scratch_pass_98_of_98", {
        "result": original_report.get("result"),
        "check_count": original_report.get("check_count"),
        "failure_count": original_report.get("failure_count"),
        "output": original_output,
        "boundary": "clean scratch Phase-0c layout; Gate-5 artifacts absent; protected live Gate_3_Validation.json not written",
    })

    equivalent_ok, equivalent_report, equivalent_output = run_gate3_clean(APPLIED, applied_posture=True)
    check(equivalent_ok, "applied_state_gate3_equivalent_pass_98_of_98", {
        "result": equivalent_report.get("result"),
        "check_count": equivalent_report.get("check_count"),
        "failure_count": equivalent_report.get("failure_count"),
        "output": equivalent_output,
    })

    failures = [item for item in checks if item["status"] == "FAIL"]
    report = {
        "amendment": "SCA-004",
        "gate": 5,
        "posture": "DRAFT_APPLICATION_PACKAGE_NOT_EXECUTED",
        "result": "PASS" if not failures else "FAIL",
        "check_count": len(checks),
        "failure_count": len(failures),
        "approved_candidate_gate3_clean_scratch": {
            "result": original_report.get("result"),
            "check_count": original_report.get("check_count"),
            "failure_count": original_report.get("failure_count"),
            "method": "unmodified Phase-0c validator in a clean temporary Phase-0c layout with Gate-5 artifacts absent; protected live report remains read-only",
            "report_sha256": sha256(SNAPSHOT / "Gate_3_Validation.json"),
        },
        "applied_state_gate3_equivalent": {
            "result": equivalent_report.get("result"),
            "check_count": equivalent_report.get("check_count"),
            "failure_count": equivalent_report.get("failure_count"),
            "method": "Phase-0c validator in a clean temporary repository with current-posture literals inverted and only SOW-083/SOW-103 status-Notes admitted by changed-row isolation; all mapping/trace/count/basis/containment checks unchanged",
        },
        "repair_evidence": {
            "observed_live_legacy_invocation": "FAIL 98 checks / 1 failure at gate5_artifacts_absent; expected context mismatch after Phase-0d Gate-5 draft artifacts existed",
            "disposition": "not a product or candidate failure; protected Gate_3_Validation.json restored exactly and legacy validator constrained to clean scratch Phase-0c layouts",
        },
        "candidate_sha256": {name: sha256(CANDIDATE / name) for name in SURFACES},
        "applied_sha256": {name: sha256(APPLIED / name) for name in SURFACES},
        "append_sha256": sha256(APPEND),
        "checks": checks,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{report['result']}: {len(checks)} checks, {len(failures)} failures -> {REPORT.name}")
    print(f"Approved-candidate Gate-3 clean scratch: {original_report.get('result')} {original_report.get('check_count')}/98, failures={original_report.get('failure_count')}")
    print(f"Applied-state Gate-3 equivalent: {equivalent_report.get('result')} {equivalent_report.get('check_count')}/98, failures={equivalent_report.get('failure_count')}")
    for failure in failures:
        print(f"  FAIL {failure['check']}: {failure['details']}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
