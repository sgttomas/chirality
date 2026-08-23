#!/usr/bin/env python3
"""Read-only deterministic validation for the SCA-004 Gate-3 candidate."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DECOMP = ROOT / "execution" / "_Decomposition"
SNAPSHOT = Path(__file__).resolve().parent
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"
REPORT = SNAPSHOT / "Gate_3_Validation.json"

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

PROTECTED = {
    "execution/_ScopeChange/_LATEST.md": "b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Brief.md": "cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_1_Validation.md": "812d0d3a33f0c2740dc89be31566a7b1f30ec833bfd99f3afe45f7bc11c99c14",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Parsed_Actions.csv": "a89b77dc1ce478f7ea5bbc3ebb12706d69e93876e6a7f4cca0cfd5ea5a9e738b",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/WORK_GRAPH.json": "86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DECOMP/coverage_summary.json": "2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45",
}

NEW_IDS = [
    "DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control",
    "DEL-02-08_Exact_Supply_and_Protocol_Pinning",
    "DEL-02-09_Hosted_Account_and_Consent_Boundary",
    "DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2",
    "DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation",
    "DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in",
    "DEL-04-11_Root_Loop_Receipt_Validator",
]
RUNTIME_IDS = NEW_IDS[:6]
RECEIPT_ID = NEW_IDS[6]
PKG02 = "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers"
PKG04 = "PKG-04_Developmental_Machinery_and_Change_Control"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def ids(value: str) -> list[str]:
    return [part for part in value.split(";") if part]


def short(identifier: str) -> str:
    return identifier.split("_", 1)[0]


def main() -> None:
    checks: list[dict[str, object]] = []

    def check(condition: bool, name: str, details: object) -> None:
        checks.append(
            {
                "check": name,
                "status": "PASS" if condition else "FAIL",
                "details": details,
            }
        )

    # Bound live basis and protected snapshot surfaces.
    for name, expected in EXPECTED_BASIS.items():
        observed = sha256(DECOMP / name)
        check(observed == expected, f"basis_untouched::{name}", f"observed={observed} expected={expected}")
    for rel, expected in PROTECTED.items():
        observed = sha256(ROOT / rel)
        check(observed == expected, f"protected_untouched::{rel}", f"observed={observed} expected={expected}")

    candidate_names = sorted(path.name for path in CANDIDATE.iterdir() if path.is_file())
    check(candidate_names == sorted(SURFACES), "candidate_exact_file_set", candidate_names)

    # Gate-4 machine action register: SCA-002/current STRUCTURE schema.
    action_fields, action_rows = csv_rows(SNAPSHOT / "Amendment_Actions.csv")
    expected_action_fields = [
        "AmendmentID",
        "ActionSeq",
        "ActionType",
        "EntityType",
        "EntityID",
        "Description",
        "AffectedFiles",
        "DownstreamReruns",
        "SupersessionBindingPresent",
    ]
    check(
        action_fields == expected_action_fields,
        "amendment_actions_exact_structure_schema",
        action_fields,
    )
    check(
        len(action_rows) == 8 and [row["ActionSeq"] for row in action_rows] == [str(index) for index in range(1, 9)],
        "amendment_actions_eight_ordered_actions",
        [row["ActionSeq"] for row in action_rows],
    )
    check(
        all(
            row["AmendmentID"] == "SCA-004"
            and row["EntityType"] == "DELIVERABLE"
            and row["EntityID"] == identifier
            and row["ActionType"] == ("MODIFY" if index == 0 else "ADD")
            for index, (row, identifier) in enumerate(zip(action_rows, ["DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", *NEW_IDS]))
        ),
        "amendment_actions_exact_entities_and_types",
        [[row["ActionSeq"], row["ActionType"], row["EntityID"]] for row in action_rows],
    )
    check(
        all(row["SupersessionBindingPresent"] == "NO" for row in action_rows),
        "amendment_actions_structural_no_supersession_bindings",
        [row["SupersessionBindingPresent"] for row in action_rows],
    )

    # New IDs are candidates only: absent from all live authoritative IDs and folders.
    _, live_deliverables = csv_rows(DECOMP / DELIVERABLES)
    live_ids = {row["DeliverableID"] for row in live_deliverables}
    check(not (set(NEW_IDS) & live_ids), "candidate_ids_absent_from_live_register", sorted(set(NEW_IDS) & live_ids))
    live_folders = []
    for identifier in NEW_IDS:
        matches = list((ROOT / "execution").glob(f"PKG-*/1_Working/{identifier}"))
        live_folders.extend(str(path.relative_to(ROOT)) for path in matches)
    check(not live_folders, "candidate_ids_unmaterialized", live_folders)

    # Parse basis and candidate registers.
    del_fields, basis_del = csv_rows(DECOMP / DELIVERABLES)
    _, cand_del = csv_rows(CANDIDATE / DELIVERABLES)
    ledger_fields, basis_ledger = csv_rows(DECOMP / LEDGER)
    _, cand_ledger = csv_rows(CANDIDATE / LEDGER)
    obj_fields, basis_obj = csv_rows(DECOMP / OBJECTIVES)
    _, cand_obj = csv_rows(CANDIDATE / OBJECTIVES)
    forward_fields, basis_forward = csv_rows(DECOMP / FORWARD)
    _, cand_forward = csv_rows(CANDIDATE / FORWARD)
    reverse_fields, basis_reverse = csv_rows(DECOMP / REVERSE)
    _, cand_reverse = csv_rows(CANDIDATE / REVERSE)

    expected_columns = {
        DELIVERABLES: 12,
        LEDGER: 12,
        OBJECTIVES: 6,
        FORWARD: 9,
        REVERSE: 6,
    }
    field_sets = {
        DELIVERABLES: del_fields,
        LEDGER: ledger_fields,
        OBJECTIVES: obj_fields,
        FORWARD: forward_fields,
        REVERSE: reverse_fields,
    }
    for name, fields in field_sets.items():
        check(len(fields) == expected_columns[name], f"column_count::{name}", fields)

    check(len(cand_del) == 53, "deliverable_count_53", len(cand_del))
    check(len(cand_ledger) == 104, "scope_item_count_104", len(cand_ledger))
    check(len(cand_obj) == 7, "objective_count_7", len(cand_obj))
    check(len(cand_forward) == 85, "forward_count_85", len(cand_forward))
    check(len(cand_reverse) == 59, "reverse_count_59", len(cand_reverse))
    check(len({row["DeliverableID"] for row in cand_del}) == 53, "deliverable_ids_unique", "53 unique")
    check(len({row["ScopeItemID"] for row in cand_ledger}) == 104, "scope_ids_unique", "104 unique")
    check(len({row["ObjectiveID"] for row in cand_obj}) == 7, "objective_ids_unique", "7 unique")
    check(len({row["UnitID"] for row in cand_reverse}) == 59, "reverse_unit_ids_unique", "59 unique")

    # Preserve record terminators from each bound register.
    endings = {
        DELIVERABLES: (0, 54),
        LEDGER: (105, 105),
        OBJECTIVES: (0, 8),
        FORWARD: (0, 86),
        REVERSE: (60, 60),
    }
    for name, (crlf, lf) in endings.items():
        raw = (CANDIDATE / name).read_bytes()
        check(raw.count(b"\r\n") == crlf and raw.count(b"\n") == lf, f"line_endings::{name}", f"crlf={raw.count(b'\r\n')} lf={raw.count(b'\n')}")

    # Exact changed-row isolation.
    def keyed(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
        return {row[key]: row for row in rows}

    bdel, cdel = keyed(basis_del, "DeliverableID"), keyed(cand_del, "DeliverableID")
    bled, cled = keyed(basis_ledger, "ScopeItemID"), keyed(cand_ledger, "ScopeItemID")
    bobj, cobj = keyed(basis_obj, "ObjectiveID"), keyed(cand_obj, "ObjectiveID")
    bfwd, cfwd = keyed(basis_forward, "PRDItem"), keyed(cand_forward, "PRDItem")
    brev, crev = keyed(basis_reverse, "UnitID"), keyed(cand_reverse, "UnitID")
    changed_del = sorted(key for key in bdel if bdel[key] != cdel[key])
    changed_ledger = sorted(key for key in bled if bled[key] != cled[key])
    changed_obj = sorted(key for key in bobj if bobj[key] != cobj[key])
    changed_fwd = sorted(key for key in bfwd if bfwd[key] != cfwd[key])
    changed_rev = sorted(key for key in brev if brev[key] != crev[key])
    check(changed_del == ["DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance"], "existing_deliverable_change_isolated", changed_del)
    check(changed_ledger == ["SOW-041", "SOW-053", "SOW-104"], "scope_changes_isolated", changed_ledger)
    check(changed_obj == ["OBJ-001", "OBJ-002", "OBJ-003", "OBJ-004", "OBJ-007"], "objective_changes_isolated", changed_obj)
    check(changed_fwd == ["D-7", "E-2", "O-11", "OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4", "OBJ-7"], "forward_changes_isolated", changed_fwd)
    check(
        {
            "DEL-01-04_Human_Authority_and_Three_Judgment_Gate_Model",
            "DEL-03-01_Path_Model_and_ScopePath_Containment_Conformance",
            "DEL-03-06_Root_Materialization_Readiness_and_Deliverable_Stream",
            "DEL-06-04_Downward_Variant_Service_and_Non_Weakening",
            PKG04,
        }.issubset(changed_rev),
        "reverse_recompute_repairs_known_inverse_drift",
        changed_rev,
    )

    # Parent discipline, type/artifact granularity, and required full row fields.
    new_rows = [cdel[identifier] for identifier in NEW_IDS]
    check(all(row["ParentPackageID"] == PKG02 for row in new_rows[:6]), "runtime_parent_pkg02", [row["ParentPackageID"] for row in new_rows[:6]])
    check(new_rows[6]["ParentPackageID"] == PKG04, "receipt_parent_pkg04", new_rows[6]["ParentPackageID"])
    check(new_rows[6]["Type"] == "TEST_SUITE", "receipt_artifact_kind_test_suite", new_rows[6]["Type"])
    expected_types = ["BACKEND_FEATURE_SLICE", "API_CONTRACT", "SECURITY_CONTROL", "API_CONTRACT", "BACKEND_FEATURE_SLICE", "TEST_SUITE", "TEST_SUITE"]
    check([row["Type"] for row in new_rows] == expected_types, "new_artifact_kinds_exact", [row["Type"] for row in new_rows])
    required_fields = ["Name", "Description", "Type", "ContextEnvelope", "ContextEnvelopeNotes", "AnticipatedArtifacts", "SupportsObjectives", "CoversScopeItems", "AnticipatedWriteLocus"]
    check(all(all(row[field].strip() for field in required_fields) for row in new_rows), "new_rows_complete", required_fields)
    check(all(row["ContextEnvelope"] == "M" for row in new_rows), "new_rows_bounded_m", [row["ContextEnvelope"] for row in new_rows])
    check(all("runtime/**" in row["AnticipatedWriteLocus"] for row in new_rows[:6]), "runtime_loci_declared", [row["AnticipatedWriteLocus"] for row in new_rows[:6]])
    check("tools/** (M2)" in new_rows[6]["AnticipatedWriteLocus"], "receipt_tools_locus_separately_gated", new_rows[6]["AnticipatedWriteLocus"])

    # Exact SOW and objective continuity.
    del0206 = cdel["DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance"]
    check(del0206["CoversScopeItems"] == "SOW-104", "del0206_retains_sow104", del0206["CoversScopeItems"])
    check(ids(del0206["SupportsObjectives"]) == ["OBJ-001", "OBJ-002", "OBJ-004", "OBJ-007"], "del0206_retains_four_objectives", del0206["SupportsObjectives"])
    check("REQ-027" in del0206["Description"], "del0206_req027_explicit", del0206["Description"])
    check(ids(cled["SOW-104"]["DeliverableIDs"]) == ["DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", *RUNTIME_IDS], "sow104_exact_remap", cled["SOW-104"]["DeliverableIDs"])
    check(RECEIPT_ID in ids(cled["SOW-041"]["DeliverableIDs"]) and RECEIPT_ID in ids(cled["SOW-053"]["DeliverableIDs"]), "sow041_sow053_exact_receipt_allocation", {key: cled[key]["DeliverableIDs"] for key in ["SOW-041", "SOW-053"]})
    check(new_rows[6]["CoversScopeItems"] == "SOW-041;SOW-053" and new_rows[6]["SupportsObjectives"] == "OBJ-003", "receipt_scope_objective_exact", {key: new_rows[6][key] for key in ["CoversScopeItems", "SupportsObjectives"]})
    check(all(row["CoversScopeItems"] == "SOW-104" and row["SupportsObjectives"] == "OBJ-001;OBJ-002;OBJ-004;OBJ-007" for row in new_rows[:6]), "runtime_scope_objective_exact", "all six map SOW-104 and OBJ-001/002/004/007")

    # No mapping gaps and symmetric companion registers.
    cand_del_ids = set(cdel)
    cand_scope_ids = set(cled)
    cand_obj_ids = set(cobj)
    in_rows = [row for row in cand_ledger if row["InOutStatus"] == "IN"]
    check(len(in_rows) == 95, "in_scope_count_95", len(in_rows))
    check(all(ids(row["DeliverableIDs"]) for row in in_rows), "zero_in_scope_items_without_mapping", [row["ScopeItemID"] for row in in_rows if not ids(row["DeliverableIDs"])])
    check(all(ids(row["MappedDeliverables"]) for row in cand_obj), "zero_objectives_without_support", [row["ObjectiveID"] for row in cand_obj if not ids(row["MappedDeliverables"])])
    dangling_scope_to_del = sorted({identifier for row in cand_ledger for identifier in ids(row["DeliverableIDs"]) if identifier not in cand_del_ids})
    dangling_del_to_scope = sorted({identifier for row in cand_del for identifier in ids(row["CoversScopeItems"]) if identifier not in cand_scope_ids})
    dangling_del_to_obj = sorted({identifier for row in cand_del for identifier in ids(row["SupportsObjectives"]) if identifier not in cand_obj_ids})
    check(not dangling_scope_to_del, "scope_to_deliverable_no_dangling", dangling_scope_to_del)
    check(not dangling_del_to_scope, "deliverable_to_scope_no_dangling", dangling_del_to_scope)
    check(not dangling_del_to_obj, "deliverable_to_objective_no_dangling", dangling_del_to_obj)
    asym_scope = []
    for row in cand_del:
        for scope_id in ids(row["CoversScopeItems"]):
            if row["DeliverableID"] not in ids(cled[scope_id]["DeliverableIDs"]):
                asym_scope.append(f"{row['DeliverableID']}->{scope_id}")
    check(not asym_scope, "scope_deliverable_bidirectional", asym_scope)
    asym_obj = []
    for row in cand_del:
        for obj_id in ids(row["SupportsObjectives"]):
            if row["DeliverableID"] not in ids(cobj[obj_id]["MappedDeliverables"]):
                asym_obj.append(f"{row['DeliverableID']}->{obj_id}")
    check(not asym_obj, "objective_deliverable_bidirectional", asym_obj)
    reverse_asym_obj = []
    for row in cand_obj:
        for deliverable_id in ids(row["MappedDeliverables"]):
            if row["ObjectiveID"] not in ids(cdel[deliverable_id]["SupportsObjectives"]):
                reverse_asym_obj.append(f"{row['ObjectiveID']}->{deliverable_id}")
    check(not reverse_asym_obj, "objective_deliverable_reverse_bidirectional", reverse_asym_obj)

    objective_forward_mismatches = []
    for row in cand_obj:
        forward_row = cfwd.get(row["PRDObjective"])
        mapped = ids(row["MappedDeliverables"])
        expected_packages = list(dict.fromkeys(cdel[identifier]["ParentPackageID"] for identifier in mapped))
        if not forward_row or (
            ids(forward_row["DeliverableIDs"]) != mapped
            or ids(forward_row["ScopeItemIDs"]) != ids(row["MappedScopeItems"])
            or ids(forward_row["PackageIDs"]) != expected_packages
            or forward_row["ObjectiveID"] != row["ObjectiveID"]
        ):
            objective_forward_mismatches.append(row["ObjectiveID"])
    check(
        not objective_forward_mismatches,
        "objective_register_forward_rows_exact",
        objective_forward_mismatches,
    )

    # Forward and reverse trace closure.
    fwd_dangling = sorted({identifier for row in cand_forward for identifier in ids(row["DeliverableIDs"]) if identifier not in cand_del_ids})
    check(not fwd_dangling, "forward_no_dangling_deliverables", fwd_dangling)
    check(all(row["CoverageStatus"] in {"COVERED", "COVERED_WITH_RECORDED_DEFERRAL"} for row in cand_forward), "forward_all_covered_or_deferred", Counter(row["CoverageStatus"] for row in cand_forward))
    check(all(row["TraceStatus"] == "TRACED" for row in cand_reverse), "reverse_all_traced", Counter(row["TraceStatus"] for row in cand_reverse))
    reverse_del_ids = {row["UnitID"] for row in cand_reverse if row["UnitKind"] == "deliverable"}
    check(reverse_del_ids == cand_del_ids, "reverse_covers_every_deliverable", sorted(cand_del_ids - reverse_del_ids))
    package_ids = list(dict.fromkeys(row["ParentPackageID"] for row in cand_del))
    expected_reverse: dict[str, dict[str, str]] = {}
    for package_id in package_ids:
        prd_items = [row["PRDItem"] for row in cand_forward if package_id in ids(row["PackageIDs"])]
        scope_items = [row["ScopeItemID"] for row in cand_ledger if row["PackageID"] == package_id]
        expected_reverse[package_id] = {
            "UnitID": package_id,
            "UnitKind": "package",
            "ParentPackageID": "",
            "PRDItems": ";".join(prd_items),
            "ScopeItemIDs": ";".join(scope_items),
            "TraceStatus": "TRACED" if prd_items and scope_items else "UNTRACED",
        }
    for row in cand_del:
        deliverable_id = row["DeliverableID"]
        prd_items = [item["PRDItem"] for item in cand_forward if deliverable_id in ids(item["DeliverableIDs"])]
        scope_items = [item["ScopeItemID"] for item in cand_ledger if deliverable_id in ids(item["DeliverableIDs"])]
        expected_reverse[deliverable_id] = {
            "UnitID": deliverable_id,
            "UnitKind": "deliverable",
            "ParentPackageID": row["ParentPackageID"],
            "PRDItems": ";".join(prd_items),
            "ScopeItemIDs": ";".join(scope_items),
            "TraceStatus": "TRACED" if prd_items and scope_items else "UNTRACED",
        }
    check(set(crev) == set(expected_reverse), "reverse_exact_unit_set", sorted(set(expected_reverse) ^ set(crev)))
    reverse_inverse_mismatches = [
        identifier for identifier, expected in expected_reverse.items() if crev.get(identifier) != expected
    ]
    check(
        not reverse_inverse_mismatches,
        "reverse_full_inverse_of_candidate_forward_and_scope_truth",
        reverse_inverse_mismatches,
    )
    check(
        "E-2" in ids(crev[PKG04]["PRDItems"]),
        "pkg04_reverse_carries_cross_package_e2_consequence",
        crev[PKG04]["PRDItems"],
    )

    # Accepted G0 A3/A7 carrier semantics are exact candidate content, not prose-only evidence.
    carrier_text = {
        identifier: " ".join(
            cdel[identifier][field]
            for field in ["Description", "AnticipatedArtifacts", "ContextEnvelopeNotes"]
        )
        for identifier in RUNTIME_IDS
    }
    a3_ids = [RUNTIME_IDS[index] for index in [0, 2, 3, 5]]
    a3_text = " ".join(carrier_text[identifier] for identifier in a3_ids)
    a3_tokens = [
        "Agent 0/1/2 role entry",
        "explicit Agent 2/TASK",
        "role not mechanically enforced",
        "instruction-asserted",
        "instruction+config asserted",
        "mechanism-proven",
        "hard filesystem/network/process containment",
        "unchanged",
    ]
    check(all(token in a3_text for token in a3_tokens), "g0_a3_complete_semantics", [token for token in a3_tokens if token not in a3_text])
    a3_carrier_tokens = {
        RUNTIME_IDS[0]: ["Agent 0/1/2 role-entry parity", "hard filesystem/network/process containment"],
        RUNTIME_IDS[2]: ["Agent 0/1/2 role entry", "explicit Agent 2/TASK", "role not mechanically enforced"],
        RUNTIME_IDS[3]: ["role-entry parity", "role not mechanically enforced", "instruction-asserted"],
        RUNTIME_IDS[5]: ["instruction+config asserted", "mechanism-proven", "hard filesystem/network/process containment"],
    }
    check(
        all(all(token in carrier_text[identifier] for token in tokens) for identifier, tokens in a3_carrier_tokens.items()),
        "g0_a3_allocated_to_07_09_10_12",
        {identifier: [token for token in tokens if token not in carrier_text[identifier]] for identifier, tokens in a3_carrier_tokens.items()},
    )

    a7_ids = [RUNTIME_IDS[index] for index in [1, 2, 3, 5]]
    a7_text = " ".join(carrier_text[identifier] for identifier in a7_ids)
    a7_tokens = [
        "no command network by default",
        "ask per destination",
        "networkApprovalContext",
        "host/protocol",
        "queued requests to the same destination",
        "acceptForSession",
        "explicit user act",
        "network_access = true",
        "labelled",
        "enumerated OpenAI",
        "prompt delivery",
        "destination-grouping",
        "exact pin",
    ]
    check(all(token in a7_text for token in a7_tokens), "g0_a7_complete_semantics", [token for token in a7_tokens if token not in a7_text])
    a7_carrier_tokens = {
        RUNTIME_IDS[1]: ["enumerated OpenAI", "three-posture", "exact-pin", "prompt-delivery", "destination-grouping"],
        RUNTIME_IDS[2]: ["no command network by default", "ask per destination", "acceptForSession", "network_access = true"],
        RUNTIME_IDS[3]: ["networkApprovalContext", "host/protocol", "acceptForSession", "same-destination"],
        RUNTIME_IDS[5]: ["three-posture", "G-APPR", "exact-pin", "prompt delivery", "destination-grouping"],
    }
    check(
        all(all(token in carrier_text[identifier] for token in tokens) for identifier, tokens in a7_carrier_tokens.items()),
        "g0_a7_allocated_to_08_09_10_12",
        {identifier: [token for token in tokens if token not in carrier_text[identifier]] for identifier, tokens in a7_carrier_tokens.items()},
    )

    supervisor_text = carrier_text[RUNTIME_IDS[0]]
    supervisor_control_tokens = [
        "DelegatedHarnessProcessSupervisorPort",
        "purpose-limited second private Unix socket",
        "one daemon as the sole runtime broker",
        "0700/0600",
        "authentication-token validation for every socket request",
        "socket owner",
        "worker generation",
        "stale-socket recovery",
        "never renderer- or CLI-callable",
        "no TCP listener",
    ]
    check(
        all(token in supervisor_text for token in supervisor_control_tokens),
        "del0207_complete_accepted_socket_control_set",
        [token for token in supervisor_control_tokens if token not in supervisor_text],
    )

    adapter_text = carrier_text[RUNTIME_IDS[3]]
    adapter_boundary_tokens = [
        "Root runtime API v2",
        "attributed approval request/decision records",
        "managed-network prompt routing",
        "rejects, redacts, or projects unknown provider payloads",
        "Agent 0/1/2 role-entry parity",
        "explicit Agent 2/TASK fallback",
        "role not mechanically enforced",
        "instruction-asserted",
        "networkApprovalContext",
        "host/protocol",
        "same-destination queued-request grouping caveat",
        "acceptForSession only by explicit user act",
        "no command network remains the default",
        "network_access = true",
        "provider-shaped persistence",
        "unattributed decisions are excluded",
    ]
    check(
        all(token in adapter_text for token in adapter_boundary_tokens),
        "del0210_complete_accepted_api_approval_payload_a3_a7_persistence_boundaries",
        [token for token in adapter_boundary_tokens if token not in adapter_text],
    )
    accepted_terminals = {
        "turn.completed",
        "turn.failed",
        "turn.interrupted",
        "turn.cancelled",
    }
    observed_terminals = set(re.findall(r"turn\.[a-z]+", adapter_text))
    check(
        "closed HarnessEvent v2 union whose only terminal identifiers are" in adapter_text
        and observed_terminals == accepted_terminals,
        "del0210_harnessevent_v2_exact_closed_terminal_set",
        {
            "observed": sorted(observed_terminals),
            "expected": sorted(accepted_terminals),
        },
    )

    # Telemetry is derived from candidate registers.
    package_counts = Counter(row["ParentPackageID"] for row in cand_del)
    envelope_counts = Counter(row["ContextEnvelope"] for row in cand_del)
    check(package_counts == Counter({
        "PKG-01_Product_Definition_Normative_Basis_and_Authority": 8,
        PKG02: 12,
        "PKG-03_Governed_Execution_Structure_and_Root_Containment": 6,
        PKG04: 11,
        "PKG-05_Evidence_Provenance_and_Audit": 8,
        "PKG-06_Self_Application_Variants_and_Release": 8,
    }), "package_count_parity", dict(package_counts))
    check(envelope_counts == Counter({"S": 14, "M": 38, "L": 1}), "context_envelope_parity", dict(envelope_counts))
    categories: dict[str, set[str]] = defaultdict(set)
    for row in cand_ledger:
        for category in ids(row["Categories"]):
            categories[category].update(ids(row["DeliverableIDs"]))
    expected_category_counts = {"NormativeBasis": 21, "OperativeProduct": 25, "DevelopmentalMachinery": 26, "Evidence": 24}
    check({key: len(value) for key, value in categories.items()} == expected_category_counts, "category_deliverable_counts_recomputed", {key: len(value) for key, value in categories.items()})
    telemetry = (CANDIDATE / TELEMETRY).read_text(encoding="utf-8")
    required_telemetry_tokens = [
        "| DeliverableCount | 53 |",
        "| PackageCount | 6 |",
        "| ObjectiveCount | 7 |",
        "| ScopeItemCount | 104 |",
        "| ContextEnvelopeCounts | S=14, M=38, L=1, XL=0 |",
        "| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | 12 |",
        "| PKG-04_Developmental_Machinery_and_Change_Control | 11 |",
        "| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 59 (6 packages + 53 deliverables) | 59 TRACED, 0 UNTRACED |",
    ]
    check(all(token in telemetry for token in required_telemetry_tokens), "telemetry_projected_counts_exact", [token for token in required_telemetry_tokens if token not in telemetry])

    candidate_main = (CANDIDATE / MAIN).read_text(encoding="utf-8")
    responsibility_counts = Counter(row["ResponsibleParty"] for row in cand_del)
    check(
        responsibility_counts == Counter({"Ryan Tufts": 53}),
        "responsibility_assignment_complete_all_53",
        dict(responsibility_counts),
    )
    oi011_marker = (
        "| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | "
        "RESPONSIBILITY_UNASSIGNED | all 53 deliverables |"
    )
    check(
        oi011_marker in candidate_main,
        "oi011_working_surface_affected_count_53",
        next((line for line in candidate_main.splitlines() if line.startswith("| OI-011 |")), "missing"),
    )
    responsibility_lineage_tokens = [
        "all 53 deliverables",
        "original 45",
        "SCA-001",
        "DEL-02-06",
        "seven SCA-004 candidate rows",
    ]
    check(
        all(token in candidate_main and token in telemetry for token in responsibility_lineage_tokens),
        "oi011_working_surface_telemetry_concordance",
        {
            "working_missing": [token for token in responsibility_lineage_tokens if token not in candidate_main],
            "telemetry_missing": [token for token in responsibility_lineage_tokens if token not in telemetry],
        },
    )
    check(
        "developmental machinery is decomposed as product scope (PKG-04, 11\ndeliverables)" in candidate_main,
        "working_surface_d12_pkg04_current_count_11",
        next((line for line in candidate_main.splitlines() if "developmental machinery is decomposed" in line), "missing"),
    )
    del0409_accepted = (
        "| L | DEL-04-09_PRD_Source_Currency_Check_Capability | Accepted at Context Envelope L "
        "by D-GOV-25 Gate 5; OI-010 is CLOSED_ACCEPTED_AT_GATE_5."
    )
    check(
        del0409_accepted in telemetry
        and "Proposed as large-but-single-domain, for owner acceptance at Gate 5/6" not in telemetry,
        "telemetry_del0409_accepted_closed_current_state",
        next((line for line in telemetry.splitlines() if line.startswith("| L | DEL-04-09")), "missing"),
    )

    main_current = candidate_main.split("## 9. Deliverables", 1)[1].split("## 12.", 1)[0]
    telemetry_current = telemetry.split("## 1. Base telemetry", 1)[1].split("## 6. Open issues", 1)[0]
    explicit_current_tokens = [
        (main_current, "53 deliverables, each belonging"),
        (main_current, "| DeliverableCount | 53 |"),
        (main_current, "PKG-04, 11\ndeliverables"),
        (main_current, "was accepted as\nlarge-but-single-domain under D-GOV-25"),
        (telemetry_current, "| DeliverableCount | 53 |"),
        (telemetry_current, "| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | 12 |"),
        (telemetry_current, "| PKG-04_Developmental_Machinery_and_Change_Control | 11 |"),
        (telemetry_current, "59 (6 packages + 53 deliverables)"),
        (telemetry_current, "OI-010 is CLOSED_ACCEPTED_AT_GATE_5"),
    ]
    forbidden_current_tokens = [
        (main_current, "46 deliverables, each belonging"),
        (main_current, "PKG-04, 10\ndeliverables"),
        (main_current, "all 46 deliverables"),
        (telemetry_current, "| DeliverableCount | 46 |"),
        (telemetry_current, "| PKG-04_Developmental_Machinery_and_Change_Control | 10 |"),
        (telemetry_current, "52 (6 packages + 46 deliverables)"),
        (telemetry_current, "Proposed as large-but-single-domain, for owner acceptance at Gate 5/6"),
    ]
    check(
        all(token in surface for surface, token in explicit_current_tokens)
        and all(token not in surface for surface, token in forbidden_current_tokens),
        "explicit_candidate_current_topology_status_scan",
        {
            "missing": [token for surface, token in explicit_current_tokens if token not in surface],
            "stale": [token for surface, token in forbidden_current_tokens if token in surface],
        },
    )

    # Candidate posture and exact diff completeness.
    posture_tokens = [
        "SCA-004 CANDIDATE v1.3",
        "SCA-004 GATE-3 CANDIDATE — NOT APPROVED OR APPLIED",
        "REQ-027",
        "DEC-025",
        "all ten HELD_UNAVAILABLE bindings remain",
    ]
    check(all(token in candidate_main for token in posture_tokens), "working_surface_candidate_posture", [token for token in posture_tokens if token not in candidate_main])
    handoff = (SNAPSHOT / "Handoff_State.md").read_text(encoding="utf-8")
    check(
        "| DerivativePackageState | `INCOMPLETE`" in handoff,
        "handoff_derivative_package_state_enum",
        next((line for line in handoff.splitlines() if "DerivativePackageState" in line), "missing"),
    )
    diff_text = (SNAPSHOT / "Gate_3_Exact_Amendment.diff").read_text(encoding="utf-8")
    check(all(f"--- a/execution/_Decomposition/{name}" in diff_text and f"+++ b/execution/_Decomposition/{name}" in diff_text for name in SURFACES), "exact_diff_covers_all_seven_surfaces", [name for name in SURFACES if f"--- a/execution/_Decomposition/{name}" not in diff_text])
    check("Gate_5" not in " ".join(path.name for path in SNAPSHOT.iterdir()), "gate5_artifacts_absent", sorted(path.name for path in SNAPSHOT.iterdir() if "Gate_5" in path.name))

    # Protected write-scope check against branch basis: no status/package/live-decomp writes.
    git_names = subprocess.run(
        ["git", "status", "--short", "--untracked-files=all"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    changed_paths = [line[3:] for line in git_names if len(line) >= 4]
    forbidden = [
        path for path in changed_paths
        if path.startswith("execution/_Decomposition/")
        or "/1_Working/" in path
        or path.endswith("_STATUS.md")
        or path == "execution/_ScopeChange/_LATEST.md"
    ]
    check(not forbidden, "protected_live_write_scope_clean", forbidden)

    failures = [item for item in checks if item["status"] == "FAIL"]
    report = {
        "amendment": "SCA-004",
        "gate": 3,
        "posture": "CANDIDATE_ONLY_GATE_3_AND_GATE_4_OWNER_APPROVAL_PENDING",
        "basis_commit": "8635e40995b05f494ae35c6083dabdd50068bb52",
        "accepted_decomposition_revision": "1.2",
        "result": "PASS" if not failures else "FAIL",
        "check_count": len(checks),
        "failure_count": len(failures),
        "candidate_sha256": {name: sha256(CANDIDATE / name) for name in SURFACES},
        "basis_sha256": {name: sha256(DECOMP / name) for name in SURFACES},
        "exact_diff_sha256": sha256(SNAPSHOT / "Gate_3_Exact_Amendment.diff"),
        "checks": checks,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{report['result']}: {len(checks)} checks, {len(failures)} failures -> {REPORT.name}")
    for failure in failures:
        print(f"  FAIL {failure['check']}: {failure['details']}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
