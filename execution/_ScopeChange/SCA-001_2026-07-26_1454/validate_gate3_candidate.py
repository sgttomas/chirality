#!/usr/bin/env python3
"""Deterministic SCA-001 Gate 3 candidate validation."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DECOMP = ROOT / "execution" / "_Decomposition"
SNAPSHOT = Path(__file__).resolve().parent
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"
REPORT = SNAPSHOT / "Gate_3_Validation.json"

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
OBJECTIVE_IDS = {"OBJ-001", "OBJ-002", "OBJ-004", "OBJ-007"}
EXPECTED_PRD_SHA = "0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d"


def rows(name: str) -> list[dict[str, str]]:
    with (CANDIDATE / FILES[name]).open(newline="") as handle:
        return list(csv.DictReader(handle))


def split(value: str) -> set[str]:
    return {part for part in value.split(";") if part}


def check(condition: bool, name: str, details: str, results: list[dict[str, str]]) -> None:
    results.append({"check": name, "status": "PASS" if condition else "FAIL", "details": details})


def main() -> None:
    scope = rows("scope")
    deliverables = rows("deliverables")
    objectives = rows("objectives")
    forward = rows("forward")
    reverse = rows("reverse")
    main_text = (CANDIDATE / FILES["main"]).read_text()
    telemetry_text = (CANDIDATE / FILES["telemetry"]).read_text()
    source_deliverables = rows_from_source(DECOMP / FILES["deliverables"])
    results: list[dict[str, str]] = []

    package_ids = {row["PackageID"] for row in scope}
    deliverable_ids = {row["DeliverableID"] for row in deliverables}
    objective_ids = {row["ObjectiveID"] for row in objectives}

    check(len(scope) == 104, "scope_count", f"observed={len(scope)} expected=104", results)
    statuses = Counter(row["InOutStatus"] for row in scope)
    check(statuses == Counter({"IN": 95, "OUT": 9}), "scope_status_counts", str(dict(statuses)), results)
    check(len(package_ids) == 6, "package_count", f"observed={len(package_ids)} expected=6", results)
    check(len(deliverables) == 46, "deliverable_count", f"observed={len(deliverables)} expected=46", results)
    check(len(objectives) == 7, "objective_count", f"observed={len(objectives)} expected=7", results)
    check(len({row["ScopeItemID"] for row in scope}) == len(scope), "unique_scope_ids", "no duplicate ScopeItemID", results)
    check(len(deliverable_ids) == len(deliverables), "unique_deliverable_ids", "no duplicate DeliverableID", results)
    check(all(row["PackageID"] for row in scope), "scope_exactly_one_package", "all scope rows have one PackageID field", results)
    check(
        all(split(row["DeliverableIDs"]) <= deliverable_ids for row in scope),
        "scope_deliverable_refs_resolve",
        "all scope DeliverableIDs resolve",
        results,
    )
    check(
        all(split(row["ObjectiveIDs"]) <= objective_ids for row in scope),
        "scope_objective_refs_resolve",
        "all scope ObjectiveIDs resolve",
        results,
    )
    check(
        all(row["ParentPackageID"] in package_ids for row in deliverables),
        "deliverable_parent_refs_resolve",
        "all deliverable parents resolve",
        results,
    )
    check(
        all(split(row["CoversScopeItems"]) <= {r["ScopeItemID"] for r in scope} for row in deliverables),
        "deliverable_scope_refs_resolve",
        "all deliverable scope references resolve",
        results,
    )
    check(
        all(row["DeliverableIDs"] for row in scope if row["InOutStatus"] == "IN"),
        "in_scope_has_deliverable",
        "all IN scope rows map to at least one deliverable",
        results,
    )

    sow_row = next(row for row in scope if row["ScopeItemID"] == SOW)
    del_row = next(row for row in deliverables if row["DeliverableID"] == DEL)
    check(sow_row["PackageID"] == PKG, "sow104_package", sow_row["PackageID"], results)
    check(sow_row["DeliverableIDs"] == DEL, "sow104_deliverable", sow_row["DeliverableIDs"], results)
    check(split(sow_row["ObjectiveIDs"]) == OBJECTIVE_IDS, "sow104_objectives", sow_row["ObjectiveIDs"], results)
    check(sow_row["Categories"] == "OperativeProduct;Evidence", "sow104_categories", sow_row["Categories"], results)
    check(del_row["ParentPackageID"] == PKG, "del0206_package", del_row["ParentPackageID"], results)
    check(del_row["Type"] == "REQ_SLICE", "del0206_type", del_row["Type"], results)
    check(del_row["ContextEnvelope"] == "M", "del0206_envelope", del_row["ContextEnvelope"], results)
    check(del_row["CoversScopeItems"] == SOW, "del0206_scope", del_row["CoversScopeItems"], results)
    check(split(del_row["SupportsObjectives"]) == OBJECTIVE_IDS, "del0206_objectives", del_row["SupportsObjectives"], results)
    check("runtime/**" in del_row["AnticipatedWriteLocus"], "del0206_runtime_locus", del_row["AnticipatedWriteLocus"], results)
    check("separately authorized client-owned tranches" in del_row["AnticipatedWriteLocus"], "client_write_boundary", del_row["AnticipatedWriteLocus"], results)

    old_del0202 = next(row for row in source_deliverables if row["DeliverableID"].startswith("DEL-02-02_"))
    new_del0202 = next(row for row in deliverables if row["DeliverableID"].startswith("DEL-02-02_"))
    check(old_del0202 == new_del0202, "del0202_byte_semantics_unchanged", "accepted register row unchanged", results)

    for objective in objectives:
        if objective["ObjectiveID"] in OBJECTIVE_IDS:
            check(DEL in split(objective["MappedDeliverables"]), f"{objective['ObjectiveID']}_maps_del0206", objective["MappedDeliverables"], results)
            check(SOW in split(objective["MappedScopeItems"]), f"{objective['ObjectiveID']}_maps_sow104", objective["MappedScopeItems"], results)

    o11 = [row for row in forward if row["PRDItem"] == "O-11"]
    check(len(o11) == 1, "forward_o11_unique", f"rows={len(o11)}", results)
    check(bool(o11) and o11[0]["ScopeItemIDs"] == SOW and o11[0]["DeliverableIDs"] == DEL, "forward_o11_lineage", str(o11[0] if o11 else {}), results)
    check(len(forward) == 85, "forward_count", f"observed={len(forward)} expected=85", results)
    check(all(row["CoverageStatus"] != "UNCOVERED" for row in forward), "forward_no_uncovered", "no UNCOVERED rows", results)

    reverse_new = [row for row in reverse if row["UnitID"] == DEL]
    check(len(reverse) == 52, "reverse_count", f"observed={len(reverse)} expected=52", results)
    check(len(reverse_new) == 1 and reverse_new[0]["TraceStatus"] == "TRACED", "reverse_del0206", str(reverse_new), results)
    check(all(row["TraceStatus"] == "TRACED" for row in reverse), "reverse_all_traced", "all rows TRACED", results)

    envelopes = Counter(row["ContextEnvelope"] for row in deliverables)
    check(envelopes == Counter({"M": 31, "S": 14, "L": 1}), "context_envelopes", str(dict(envelopes)), results)
    check("XL" not in envelopes, "no_xl", str(dict(envelopes)), results)
    check("v1.1" in main_text and DEL in main_text and SOW in main_text, "main_surface_parity", "revision and new IDs present", results)
    check("ScopeItemCount | 104" in main_text and "DeliverableCount | 46" in main_text, "main_counts", "104/46 present", results)
    check("ScopeItemCount | 104" in telemetry_text and "DeliverableCount | 46" in telemetry_text, "telemetry_counts", "104/46 present", results)
    check(hashlib.sha256((ROOT / "docs" / "PRD_ROOT.md").read_bytes()).hexdigest() == EXPECTED_PRD_SHA, "prd_basis_sha", EXPECTED_PRD_SHA, results)
    check(
        all((DECOMP / name).read_bytes() != (CANDIDATE / name).read_bytes() for name in FILES.values()),
        "candidate_is_separate",
        "all seven candidate files differ and authoritative paths remain separate",
        results,
    )

    category_scope = Counter()
    category_deliverables: dict[str, set[str]] = {}
    for row in scope:
        for category in split(row["Categories"]):
            category_scope[category] += 1
            category_deliverables.setdefault(category, set()).update(split(row["DeliverableIDs"]))
    expected_category_counts = {"NormativeBasis": 41, "OperativeProduct": 27, "DevelopmentalMachinery": 59, "Evidence": 19}
    check(dict(category_scope) == expected_category_counts, "category_scope_counts", str(dict(category_scope)), results)
    check(len(category_deliverables["OperativeProduct"]) == 19, "operative_deliverable_count", str(len(category_deliverables["OperativeProduct"])), results)
    check(len(category_deliverables["Evidence"]) == 17, "evidence_deliverable_count", str(len(category_deliverables["Evidence"])), results)

    failed = [result for result in results if result["status"] == "FAIL"]
    payload = {
        "amendment": "SCA-001",
        "gate": 3,
        "candidate_directory": str(CANDIDATE.relative_to(ROOT)),
        "result": "PASS" if not failed else "FAIL",
        "checks": results,
        "candidate_sha256": {
            name: hashlib.sha256((CANDIDATE / filename).read_bytes()).hexdigest()
            for name, filename in FILES.items()
        },
    }
    REPORT.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"result": payload["result"], "checks": len(results), "failed": len(failed)}, indent=2))
    raise SystemExit(1 if failed else 0)


def rows_from_source(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


if __name__ == "__main__":
    main()
