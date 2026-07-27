#!/usr/bin/env python3
"""Deterministically validate the applied SCA-001 Gate 5 decomposition state."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT = Path(__file__).resolve().parent
DECOMP = ROOT / "execution" / "_Decomposition"
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"
PRE = SNAPSHOT / "Pre_Change_Register_Baseline.json"
GATE3 = SNAPSHOT / "Gate_3_Validation.json"
POST = SNAPSHOT / "Post_Change_Coverage.json"
HASHES = SNAPSHOT / "Applied_File_Hashes.json"
AUDIT_ROOT = ROOT / "execution" / "_Evaluation" / "DecompCoverage"

FILES = {
    "main": "Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
    "scope": "chirality_root_scope_ledger_v1_0.csv",
    "deliverables": "chirality_root_deliverable_register_v1_0.csv",
    "objectives": "chirality_root_objective_register_v1_0.csv",
    "forward": "chirality_root_prd_coverage_forward_v1_0.csv",
    "reverse": "chirality_root_trace_reverse_v1_0.csv",
    "telemetry": "chirality_root_coverage_telemetry_v1_0.md",
}
PKG = "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers"
DEL = "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance"
SOW = "SOW-104"
OBJECTIVES = {"OBJ-001", "OBJ-002", "OBJ-004", "OBJ-007"}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def split(value: str) -> set[str]:
    return {part for part in value.split(";") if part}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    pre = json.loads(PRE.read_text())
    gate3 = json.loads(GATE3.read_text())
    audit_pointer = (AUDIT_ROOT / "_LATEST.md").read_text()
    audit_snapshot_name = next(
        line.split(":", 1)[1].strip()
        for line in audit_pointer.splitlines()
        if line.startswith("Latest:")
    )
    audit_summary_path = AUDIT_ROOT / audit_snapshot_name / "coverage_summary.json"
    audit_summary = json.loads(audit_summary_path.read_text())
    scope = read_rows(DECOMP / FILES["scope"])
    deliverables = read_rows(DECOMP / FILES["deliverables"])
    objectives = read_rows(DECOMP / FILES["objectives"])
    forward = read_rows(DECOMP / FILES["forward"])
    reverse = read_rows(DECOMP / FILES["reverse"])
    results: list[dict[str, object]] = []

    def check(condition: bool, name: str, details: object) -> None:
        results.append({
            "check": name,
            "status": "PASS" if condition else "FAIL",
            "details": details,
        })

    applied_hashes = {name: sha(DECOMP / filename) for name, filename in FILES.items()}
    candidate_hashes = {name: sha(CANDIDATE / filename) for name, filename in FILES.items()}
    before_by_name = {
        name: pre["authoritative_file_sha256"][f"execution/_Decomposition/{filename}"]
        for name, filename in FILES.items()
    }
    check(gate3["result"] == "PASS", "approved_candidate_validation", gate3["result"])
    check(
        applied_hashes == candidate_hashes == gate3["candidate_sha256"],
        "applied_candidate_hash_parity",
        {"applied": applied_hashes, "candidate": candidate_hashes},
    )
    check(
        all(before_by_name[name] != applied_hashes[name] for name in FILES),
        "all_seven_authoritative_surfaces_changed",
        {"before": before_by_name, "after": applied_hashes},
    )

    scope_ids = {row["ScopeItemID"] for row in scope}
    package_ids = {row["PackageID"] for row in scope}
    deliverable_ids = {row["DeliverableID"] for row in deliverables}
    objective_ids = {row["ObjectiveID"] for row in objectives}
    status_counts = Counter(row["InOutStatus"] for row in scope)
    envelopes = Counter(row["ContextEnvelope"] for row in deliverables)

    check(len(scope) == 104, "scope_count", len(scope))
    check(status_counts == Counter({"IN": 95, "OUT": 9}), "scope_status_counts", dict(status_counts))
    check(len(package_ids) == 6, "package_count", len(package_ids))
    check(len(deliverables) == 46, "deliverable_count", len(deliverables))
    check(len(objectives) == 7, "objective_count", len(objectives))
    check(len(forward) == 85, "forward_count", len(forward))
    check(len(reverse) == 52, "reverse_count", len(reverse))
    check(envelopes == Counter({"S": 14, "M": 31, "L": 1}), "context_envelopes", dict(envelopes))
    check(len(scope_ids) == len(scope), "unique_scope_ids", len(scope_ids))
    check(len(deliverable_ids) == len(deliverables), "unique_deliverable_ids", len(deliverable_ids))
    check(len(objective_ids) == len(objectives), "unique_objective_ids", len(objective_ids))
    check(all(row["PackageID"] for row in scope), "scope_exactly_one_package", "all populated")
    check(
        all(row["PackageID"] in package_ids for row in scope if row["InOutStatus"] == "IN"),
        "in_scope_package_refs_resolve",
        "all resolve",
    )
    check(
        all(row["DeliverableIDs"] and split(row["DeliverableIDs"]) <= deliverable_ids
            for row in scope if row["InOutStatus"] == "IN"),
        "in_scope_deliverable_refs_resolve",
        "all resolve",
    )
    check(
        all(split(row["ObjectiveIDs"]) <= objective_ids for row in scope),
        "scope_objective_refs_resolve",
        "all resolve",
    )
    check(
        all(row["ParentPackageID"] in package_ids for row in deliverables),
        "deliverable_parent_refs_resolve",
        "all resolve",
    )
    check(
        all(split(row["CoversScopeItems"]) <= scope_ids for row in deliverables),
        "deliverable_scope_refs_resolve",
        "all resolve",
    )
    check(
        all(split(row["SupportsObjectives"]) <= objective_ids for row in deliverables),
        "deliverable_objective_refs_resolve",
        "all resolve",
    )
    check(
        all(split(row["MappedDeliverables"]) <= deliverable_ids for row in objectives),
        "objective_deliverable_refs_resolve",
        "all resolve",
    )
    check(
        all(split(row["MappedScopeItems"]) <= scope_ids for row in objectives),
        "objective_scope_refs_resolve",
        "all resolve",
    )

    sow = next(row for row in scope if row["ScopeItemID"] == SOW)
    deliverable = next(row for row in deliverables if row["DeliverableID"] == DEL)
    check(sow["PackageID"] == PKG, "sow104_package", sow["PackageID"])
    check(sow["DeliverableIDs"] == DEL, "sow104_deliverable", sow["DeliverableIDs"])
    check(split(sow["ObjectiveIDs"]) == OBJECTIVES, "sow104_objectives", sow["ObjectiveIDs"])
    check(sow["Categories"] == "OperativeProduct;Evidence", "sow104_categories", sow["Categories"])
    check(deliverable["ParentPackageID"] == PKG, "del0206_parent", deliverable["ParentPackageID"])
    check(deliverable["Type"] == "REQ_SLICE", "del0206_type", deliverable["Type"])
    check(deliverable["ContextEnvelope"] == "M", "del0206_envelope", deliverable["ContextEnvelope"])
    check(deliverable["CoversScopeItems"] == SOW, "del0206_scope", deliverable["CoversScopeItems"])
    check(split(deliverable["SupportsObjectives"]) == OBJECTIVES, "del0206_objectives", deliverable["SupportsObjectives"])
    check("runtime/**" in deliverable["AnticipatedWriteLocus"], "del0206_runtime_locus", deliverable["AnticipatedWriteLocus"])
    check(
        "separately authorized client-owned tranches" in deliverable["AnticipatedWriteLocus"],
        "del0206_client_boundary",
        deliverable["AnticipatedWriteLocus"],
    )

    o11 = [row for row in forward if row["PRDItem"] == "O-11"]
    check(len(o11) == 1, "o11_forward_unique", len(o11))
    check(
        bool(o11) and o11[0]["ScopeItemIDs"] == SOW and o11[0]["DeliverableIDs"] == DEL,
        "o11_forward_lineage",
        o11[0] if o11 else {},
    )
    reverse_del = [row for row in reverse if row["UnitID"] == DEL]
    check(
        len(reverse_del) == 1 and reverse_del[0]["TraceStatus"] == "TRACED",
        "del0206_reverse_trace",
        reverse_del,
    )
    check(all(row["TraceStatus"] == "TRACED" for row in reverse), "reverse_all_traced", "all traced")
    check(all(row["CoverageStatus"] != "UNCOVERED" for row in forward), "forward_no_uncovered", "none")

    # Gate 3 proved DEL-02-02 unchanged against the predecessor. Gate 5 proves
    # the authoritative bytes are exactly those already-approved candidate bytes.
    gate3_del0202 = next(
        item for item in gate3["checks"] if item["check"] == "del0202_byte_semantics_unchanged"
    )
    check(
        gate3_del0202["status"] == "PASS" and applied_hashes == candidate_hashes,
        "del0202_predecessor_semantics_preserved",
        gate3_del0202,
    )

    category_scope = Counter()
    category_deliverables: dict[str, set[str]] = {}
    for row in scope:
        for category in split(row["Categories"]):
            category_scope[category] += 1
            category_deliverables.setdefault(category, set()).update(split(row["DeliverableIDs"]))
    check(
        dict(category_scope)
        == {"NormativeBasis": 41, "OperativeProduct": 27, "DevelopmentalMachinery": 59, "Evidence": 19},
        "category_scope_counts",
        dict(category_scope),
    )
    check(len(category_deliverables["OperativeProduct"]) == 19, "operative_deliverable_count", 19)
    check(len(category_deliverables["Evidence"]) == 17, "evidence_deliverable_count", 17)

    tracked_changed = subprocess.run(
        ["git", "diff", "--name-only", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    changed = sorted(set(tracked_changed + untracked))
    exact_allowed = {
        f"execution/_Decomposition/{filename}" for filename in FILES.values()
    } | {"execution/_ScopeChange/_LATEST.md", "execution/_Evaluation/DecompCoverage/_LATEST.md"}
    allowed_prefixes = (
        "execution/_ScopeChange/SCA-001_2026-07-26_1454/",
        "execution/_Evaluation/DecompCoverage/COV_SCA001_POSTCHANGE_",
    )
    unexpected = [
        path for path in changed
        if path not in exact_allowed and not path.startswith(allowed_prefixes)
    ]
    prohibited = [
        path for path in changed
        if path.startswith(("runtime/", "execution/_harness/", "projects/"))
        or "/1_Working/" in path
        or path.endswith("/ScopeOfWork.md")
        or path in {"docs/PRD_ROOT.md"}
    ]
    check(not prohibited, "no_prohibited_surface_changes", prohibited)
    check(not unexpected, "gate5_write_set_exact", unexpected)

    hash_evidence = {
        "amendment_id": "SCA-001",
        "gate": 5,
        "application_state": "ACCEPTED_CURRENT_BASIS",
        "files": [
            {
                "path": f"execution/_Decomposition/{filename}",
                "before_sha256": before_by_name[name],
                "approved_candidate_sha256": candidate_hashes[name],
                "applied_sha256": applied_hashes[name],
                "exact_candidate_match": applied_hashes[name] == candidate_hashes[name],
            }
            for name, filename in FILES.items()
        ],
    }
    HASHES.write_text(json.dumps(hash_evidence, indent=2) + "\n")

    failed = [item for item in results if item["status"] == "FAIL"]
    payload = {
        "amendment_id": "SCA-001",
        "gate": 5,
        "state": "ACCEPTED_CURRENT_BASIS",
        "authoritative_decomposition": "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
        "candidate_directory": "execution/_ScopeChange/SCA-001_2026-07-26_1454/Gate_3_Candidate",
        "result": "PASS" if not failed else "FAIL",
        "checks_run": len(results),
        "checks_failed": len(failed),
        "checks": results,
        "counts": {
            "scope_items": len(scope),
            "scope_in": status_counts["IN"],
            "scope_out": status_counts["OUT"],
            "scope_tbd": status_counts["TBD"],
            "packages": len(package_ids),
            "deliverables": len(deliverables),
            "objectives": len(objectives),
            "forward_coverage_rows": len(forward),
            "reverse_trace_rows": len(reverse),
        },
        "lineage": {
            "prd_item": "O-11",
            "scope_item": SOW,
            "package": PKG,
            "deliverable": DEL,
            "objectives": sorted(OBJECTIVES),
        },
        "applied_sha256": applied_hashes,
        "changed_paths_observed": changed,
        "prohibited_changed_paths": prohibited,
        "unexpected_changed_paths": unexpected,
        "downstream_state": {
            "del0206_scaffold": "ABSENT_EXPECTED_PENDING_PROJECT_SETUP",
            "harness_refresh": "NOT_APPLIED_BY_SCOPE_CHANGE",
            "runtime_implementation": "NOT_AUTHORIZED",
        },
        "post_change_audit": {
            "snapshot": str((AUDIT_ROOT / audit_snapshot_name).relative_to(ROOT)),
            "coverage_summary_sha256": sha(audit_summary_path),
            "overall_status": audit_summary["overall_status"],
            "closure_readiness": audit_summary["closure_readiness"],
            "issues_blocker": audit_summary["issues_blocker"],
            "issues_warning": audit_summary["issues_warning"],
            "issues_info": audit_summary["issues_info"],
            "partitions": {
                "declared": audit_summary["partitions_declared"],
                "found": audit_summary["partitions_found"],
            },
            "production_units": {
                "declared": audit_summary["production_units_declared"],
                "found": audit_summary["production_units_found"],
            },
            "sole_blocker_disposition": (
                "DEL-02-06 filesystem scaffold absent; expected downstream "
                "PROJECT_SETUP gap preserved as a real AUDIT_DECOMP blocker"
            ),
        },
    }
    POST.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"result": payload["result"], "checks": len(results), "failed": len(failed)}, indent=2))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
