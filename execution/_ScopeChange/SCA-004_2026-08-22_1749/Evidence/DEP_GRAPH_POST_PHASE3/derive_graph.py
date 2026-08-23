#!/usr/bin/env python3
"""Derive the post-Phase-3 Root objective-relative dependency graph."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REGISTER = ROOT / "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv"
POINTER = ROOT / "execution/_ScopeChange/_LATEST.md"
PROPAGATION = ROOT / "execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md"
R7 = ROOT / "plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md"
N1_RETURN = ROOT / "execution/_Coordination/AgentRuns/ROOT_V3_PHASE3_2026-08-23/instances/N1_ACCEPT_INIT_REPIN/RETURN.md"
N2_RETURN = ROOT / "execution/_Coordination/AgentRuns/ROOT_V3_PHASE3_2026-08-23/instances/N2_DEP_EXTRACTION/RETURN.md"

EXPECTED_INPUTS = {
    REGISTER: "2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba",
    POINTER: "4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c",
    PROPAGATION: "abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05",
    R7: "dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53",
    N1_RETURN: "30ff431a22d0250a290fa3c3800a4ba76385339ddd3e428c5f64a5df059c9ec2",
    N2_RETURN: "2aa9b0f08b793fc1e7ffbb16de7bce686debeaf809918fed21ce7f36b2ec9734",
}

EXPECTED_DEPENDENCY_HASHES = {
    "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance": "20773668bd8086164c1cd7ee4119d7744d0c2f9a045e546b5565791bc772537f",
    "DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control": "2cececdade0f58deadce326e14926e47dfd862b48694cb77bb57c14c1277e8bf",
    "DEL-02-08_Exact_Supply_and_Protocol_Pinning": "2065317900f62f75a76081ce64593b5cf93dbcb53887f35e1b538c53893ebda9",
    "DEL-02-09_Hosted_Account_and_Consent_Boundary": "20b6592c76b7a81ce0705a10daa34d7e4ed52730790c71688951c914e61f1a62",
    "DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2": "4fe6d9bc3d2852d3f43b916c848b56e50535af0a15e352b5ebf1ec23bfa9c28f",
    "DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation": "10c25130e663b6d29c25b5e543f4382302082c447ed82da2da68365607234f60",
    "DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in": "f4a635b3c65523dbe8c819f53b92d1889f3dc34a521e0658422d26e1f7ad2998",
    "DEL-04-11_Root_Loop_Receipt_Validator": "750a0a83e8b93143d6bcf35251c3f716e12c289dc2e0c269f98d33f389279211",
}

EXPECTED_RELATIONSHIPS = {
    ("DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control", "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", "EVIDENCE_FAN_IN", True),
    ("DEL-02-08_Exact_Supply_and_Protocol_Pinning", "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", "EVIDENCE_FAN_IN", True),
    ("DEL-02-09_Hosted_Account_and_Consent_Boundary", "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", "EVIDENCE_FAN_IN", True),
    ("DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2", "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", "EVIDENCE_FAN_IN", True),
    ("DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation", "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", "EVIDENCE_FAN_IN", True),
    ("DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in", "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", "EVIDENCE_FAN_IN", True),
    ("DEL-04-05_Root_Governed_Loop_and_Receipt_Discipline", "DEL-04-11_Root_Loop_Receipt_Validator", "DOCTRINE_INPUT", True),
    ("DEL-05-02_Snapshot_Handoff_and_Receipt_Discipline", "DEL-04-11_Root_Loop_Receipt_Validator", "EVIDENCE_CROSSCHECK_INPUT", True),
    ("DEL-04-11_Root_Loop_Receipt_Validator", "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance", "VALIDATION_RELATIONSHIP", False),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def current_state(path: Path) -> str:
    match = re.search(r"\*\*Current State:\*\*\s*`?([A-Z_]+)", path.read_text())
    if not match:
        raise SystemExit(f"Current State not found: {path}")
    return match.group(1)


def tarjan(nodes: set[str], edges: list[tuple[str, str]]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = defaultdict(list)
    for source, target in edges:
        adjacency[source].append(target)
    for source in adjacency:
        adjacency[source].sort()
    index = 0
    stack: list[str] = []
    indices: dict[str, int] = {}
    lowlinks: dict[str, int] = {}
    on_stack: set[str] = set()
    components: list[list[str]] = []

    def visit(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for target in adjacency.get(node, []):
            if target not in indices:
                visit(target)
                lowlinks[node] = min(lowlinks[node], lowlinks[target])
            elif target in on_stack:
                lowlinks[node] = min(lowlinks[node], indices[target])
        if lowlinks[node] == indices[node]:
            component: list[str] = []
            while True:
                member = stack.pop()
                on_stack.remove(member)
                component.append(member)
                if member == node:
                    break
            components.append(sorted(component))

    for node in sorted(nodes):
        if node not in indices:
            visit(node)
    return sorted(components, key=lambda members: members[0])


def parse_tables(owner: str, path: Path) -> tuple[list[dict[str, object]], int]:
    section = ""
    declarations: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if line.startswith("## Upstream"):
            section = "upstream"
        elif line.startswith("## Downstream"):
            section = "downstream"
        elif line.startswith("## "):
            section = ""
        if section not in {"upstream", "downstream"} or not line.startswith("| `DEL-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            raise SystemExit(f"Unexpected dependency table row at {path}:{line_number}")
        peer = cells[0].strip("`")
        edge_type = cells[1].strip("`")
        gating_text = cells[2].lower()
        if gating_text not in {"yes", "no"}:
            raise SystemExit(f"Unexpected gating value at {path}:{line_number}: {cells[2]}")
        source, target = (peer, owner) if section == "upstream" else (owner, peer)
        declarations.append({
            "from": source,
            "to": target,
            "type": edge_type,
            "gating": gating_text == "yes",
            "citation": cells[3],
            "evidence": f"{path.relative_to(ROOT)}:{line_number}",
            "declared_by": owner,
        })
    return declarations, len(declarations)


def main() -> None:
    failures = []
    for path, expected in EXPECTED_INPUTS.items():
        actual = sha256(path)
        if actual != expected:
            failures.append(f"{path.relative_to(ROOT)}: expected {expected}, got {actual}")
    if failures:
        raise SystemExit("Input identity failure:\n" + "\n".join(failures))

    with REGISTER.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 53 or len({row["DeliverableID"] for row in rows}) != 53:
        raise SystemExit("Applied register must contain 53 unique deliverables")
    row_by_id = {row["DeliverableID"]: row for row in rows}
    package_ids = sorted({row["ParentPackageID"] for row in rows})
    if len(package_ids) != 6:
        raise SystemExit("Applied register must contain six packages")

    dependency_paths: dict[str, Path] = {}
    nodes: list[dict[str, object]] = []
    for package_id in package_ids:
        package_path = ROOT / "execution" / package_id
        if not package_path.is_dir():
            raise SystemExit(f"Missing package: {package_path}")
        nodes.append({
            "id": package_id,
            "canonical_id": package_id.split("_", 1)[0],
            "kind": "ROOT_PACKAGE",
            "path": str(package_path.relative_to(ROOT)),
        })
    for row in sorted(rows, key=lambda value: value["DeliverableID"]):
        deliverable_id = row["DeliverableID"]
        folder = ROOT / "execution" / row["ParentPackageID"] / "1_Working" / deliverable_id
        status_path = folder / "_STATUS.md"
        dependency_path = folder / "_DEPENDENCIES.md"
        if not folder.is_dir() or not status_path.is_file() or not dependency_path.is_file():
            raise SystemExit(f"Missing live metadata for {deliverable_id}")
        dependency_paths[deliverable_id] = dependency_path
        nodes.append({
            "id": deliverable_id,
            "canonical_id": deliverable_id.split("_", 1)[0],
            "kind": "ROOT_DELIVERABLE",
            "path": str(folder.relative_to(ROOT)),
            "parent_package_id": row["ParentPackageID"],
            "lifecycle": current_state(status_path),
            "type": row["Type"],
            "objectives": row["SupportsObjectives"].split(";"),
            "scope_items": row["CoversScopeItems"].split(";"),
            "dependency_metadata": str(dependency_path.relative_to(ROOT)),
        })

    for deliverable_id, expected in EXPECTED_DEPENDENCY_HASHES.items():
        actual = sha256(dependency_paths[deliverable_id])
        if actual != expected:
            raise SystemExit(f"N2 dependency identity drift for {deliverable_id}: {actual}")

    declarations: list[dict[str, object]] = []
    declaration_counts: dict[str, int] = {}
    for deliverable_id in sorted(EXPECTED_DEPENDENCY_HASHES):
        parsed, count = parse_tables(deliverable_id, dependency_paths[deliverable_id])
        declarations.extend(parsed)
        declaration_counts[deliverable_id] = count

    grouped: dict[tuple[str, str, str, bool], list[dict[str, object]]] = defaultdict(list)
    for declaration in declarations:
        key = (
            str(declaration["from"]), str(declaration["to"]),
            str(declaration["type"]), bool(declaration["gating"]),
        )
        grouped[key].append(declaration)
    if set(grouped) != EXPECTED_RELATIONSHIPS:
        missing = sorted(EXPECTED_RELATIONSHIPS - set(grouped))
        extra = sorted(set(grouped) - EXPECTED_RELATIONSHIPS)
        raise SystemExit(f"Extracted relationship mismatch; missing={missing}; extra={extra}")
    if len(declarations) != 16:
        raise SystemExit(f"Expected 16 reciprocal/local declarations, got {len(declarations)}")

    relationships = []
    for index, key in enumerate(sorted(grouped), start=1):
        source, target, edge_type, gating = key
        if source not in row_by_id or target not in row_by_id:
            raise SystemExit(f"Unresolved relationship: {key}")
        evidence = sorted({str(item["evidence"]) for item in grouped[key]})
        citations = sorted({str(item["citation"]) for item in grouped[key]})
        relationships.append({
            "id": f"D-{index:03d}",
            "from": source,
            "to": target,
            "type": edge_type,
            "gating": gating,
            "cycle_participating": False,
            "evidence": evidence,
            "accepted_grounding": citations,
            "declaration_count": len(grouped[key]),
        })

    membership_edges = [{
        "id": f"M-{index:03d}",
        "from": row["ParentPackageID"],
        "to": row["DeliverableID"],
        "type": "PARENT_MEMBERSHIP",
        "gating": False,
    } for index, row in enumerate(sorted(rows, key=lambda value: value["DeliverableID"]), start=1)]

    strict_pairs = [(edge["from"], edge["to"]) for edge in relationships if edge["gating"]]
    all_node_ids = {node["id"] for node in nodes}
    components = tarjan(all_node_ids, strict_pairs)
    nontrivial = [members for members in components if len(members) > 1]
    if nontrivial:
        for edge in relationships:
            if any(edge["from"] in members and edge["to"] in members for members in nontrivial):
                edge["cycle_participating"] = True
                edge["gating"] = False

    sccs = [{
        "id": f"SCC-{index:03d}",
        "members": members,
        "size": len(members),
        "non_trivial": len(members) > 1,
        "proposed_move": "HUMAN_RULING_REQUIRED" if len(members) > 1 else "NONE",
        "human_gate": len(members) > 1,
    } for index, members in enumerate(components, start=1)]

    package_counts = Counter(row["ParentPackageID"].split("_", 1)[0] for row in rows)
    graph = {
        "schema": "chirality-objective-relative-work-graph/v2",
        "graph_id": "ROOT-V3-RELEASE-PATHWAY-SCA-004-POST-PHASE3",
        "status": "DERIVATIVE_CURRENT_POST_DEPENDENCY_EXTRACTION",
        "basis": {
            "branch_basis": "3389adabfa2919b66f64bbd9cd04d7d29b9838b4",
            "owner_authorized_sync_merge": "31a7fe680",
            "n1_commit": "49844ad30d75171f96715e14065a51a65dbb6456",
            "n2_commit": "5502aea661225e70bc2341b9eed551f16237c09b",
            "sca_snapshot": "SCA-004_2026-08-22_1749",
            "applied_revision": "1.3",
            "latest_pointer_sha256": EXPECTED_INPUTS[POINTER],
            "r7_record_sha256": EXPECTED_INPUTS[R7],
            "n1_return_sha256": EXPECTED_INPUTS[N1_RETURN],
            "n2_return_sha256": EXPECTED_INPUTS[N2_RETURN],
            "dependency_file_sha256": EXPECTED_DEPENDENCY_HASHES,
        },
        "objective": "Represent final integration and release-assurance ordering for the accepted SCA-004 Root carriers after Phase-3 dependency extraction.",
        "edge_semantics": {
            "GATING_DEPENDENCY": "from must supply the accepted input or evidence before to can close for this objective",
            "NON_GATING_RELATIONSHIP": "coordination or validation support that does not order or gate closure",
            "PARENT_MEMBERSHIP": "package membership only; never readiness-gating",
            "NOTICE_FAN_IN": "cross-loop coordination only; never foreign authority or a gating dependency",
        },
        "cycle_policy": "Cycle-participating edges stay non-gating pending a recorded decompose/invert/merge/cut move; cut and merge are human-gated.",
        "dependency_source_state": {
            "source_format": "authoritative deliverable-local _DEPENDENCIES.md",
            "extracted_containers": 8,
            "legacy_not_run_yet_containers": 45,
            "local_declaration_rows": len(declarations),
            "unique_root_relationships": len(relationships),
            "gating_relationships": sum(1 for edge in relationships if edge["gating"]),
            "non_gating_relationships": sum(1 for edge in relationships if not edge["gating"]),
            "phase1_initialized_empty_warning": "CLEARED_FOR_SEVEN_SCA004_CARRIERS",
        },
        "node_counts": {
            "total": len(nodes),
            "packages": len(package_ids),
            "deliverables": len(rows),
            "deliverables_by_package": dict(sorted(package_counts.items())),
        },
        "nodes": nodes,
        "membership_edges": membership_edges,
        "dependency_edges": relationships,
        "notice_edges": [
            {
                "id": "N-001", "from": "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance",
                "to": "APP_COORDINATION", "type": "AFFECTED_CLIENT_REQUIREMENTS_NOTICE",
                "gating": False, "foreign_authority": False,
                "evidence": "DEL-02-06 _DEPENDENCIES.md Cross-loop notice / fan-in table",
            },
            {
                "id": "N-002", "from": "APP_COORDINATION",
                "to": "DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in",
                "type": "APP_CONFORMANCE_EVIDENCE_NOTICE_FAN_IN",
                "gating": False, "foreign_authority": False,
                "evidence": "DEL-02-12 _DEPENDENCIES.md Cross-loop notice / fan-in table",
            },
        ],
        "sccs": sccs,
        "strict_layer_acyclic": not nontrivial,
        "non_trivial_scc_count": len(nontrivial),
        "human_gated_cycle_decision_required": bool(nontrivial),
        "derivative_disposition": "Re-derive after estimates/schedule or any accepted dependency change; this package is not authoritative decomposition truth.",
    }
    (HERE / "WORK_GRAPH.json").write_text(json.dumps(graph, indent=2) + "\n", encoding="utf-8")

    strict_lines = [f"{edge['from']} --{edge['type']}--> {edge['to']}" for edge in relationships if edge["gating"]]
    nongating_lines = [f"{edge['from']} --{edge['type']}--> {edge['to']}" for edge in relationships if not edge["gating"]]
    dag = [
        "# Root objective-relative work graph — post-Phase 3", "",
        "Status: `DERIVATIVE_CURRENT_POST_DEPENDENCY_EXTRACTION`", "",
        "## Basis and objective", "",
        "This derivative graph is grounded in accepted SCA-004 revision 1.3, R7-A,",
        "N1 lifecycle initialization, and N2's authoritative `_DEPENDENCIES.md`",
        "extraction. It contains the exact 53 register deliverables plus six package",
        "nodes. It does not replace decomposition or deliverable-local dependency truth.", "",
        "Objective: final integration and release-assurance ordering for the accepted",
        "SCA-004 Root carriers.", "", "## Gating dependency layer", "", "```text",
        *strict_lines, "```", "", "## Non-gating relationships", "", "```text",
        *nongating_lines, "```", "",
        "The two App coupling relationships are notice/fan-in edges only and are not",
        "foreign authority or part of SCC ordering.", "", "## Structural summary", "",
        "- Nodes: 59 = 53 deliverables + 6 packages.",
        "- Package-membership edges: 53, structural and non-gating.",
        f"- Root relationships: {len(relationships)} = 8 gating + 1 non-gating.",
        "- Cross-loop notice/fan-in edges: 2, non-gating.",
        f"- Strict SCCs: {len(components)} singleton components; non-trivial: {len(nontrivial)}.",
        "- Human-gated cut/merge required: no." if not nontrivial else "- Human-gated cut/merge required: yes; see SCC_Report.md and stop.",
        "", "## Derivative status and rerun", "",
        "Re-derive this graph after estimates/schedule or any accepted dependency",
        "change. No cycle has been silently linearized; cycle-participating edges",
        "would remain non-gating until their recorded resolution.", "",
    ]
    (HERE / "DAG.md").write_text("\n".join(dag), encoding="utf-8")

    scc_lines = [
        "# SCC report — post-Phase 3 dependency extraction", "",
        "Verdict: `PASS — NO NON-TRIVIAL SCC`" if not nontrivial else "Verdict: `BLOCKED — HUMAN-GATED SCC RESOLUTION REQUIRED`", "",
        "SCCs are computed over all 59 Root nodes using only the eight gating",
        "dependency relationships. Package membership, the validation relationship,",
        "and App notice/fan-in edges are non-gating and excluded from ordering.", "",
        "| SCC | Members | Size | Non-trivial | Proposed move | Human gate |",
        "|---|---|---:|---|---|---|",
    ]
    for scc in sccs:
        scc_lines.append(f"| {scc['id']} | `{'`; `'.join(scc['members'])}` | {scc['size']} | {'yes' if scc['non_trivial'] else 'no'} | `{scc['proposed_move']}` | {'yes' if scc['human_gate'] else 'no'} |")
    scc_lines.extend(["", "Cycle-participating edges: none." if not nontrivial else "Cycle-participating edges are non-gating pending owner ruling.", "", "Rerun after estimates/schedule or any accepted dependency change.", ""])
    (HERE / "SCC_Report.md").write_text("\n".join(scc_lines), encoding="utf-8")

    decision = """# Decision log — post-Phase-3 graph derivation

## DG-DL-001 — Root dependency source override

The human steer and sealed brief require the authoritative Root
`_DEPENDENCIES.md` declarations, not generic `Dependencies.csv`, and require
this SCA evidence folder rather than an `_Evaluation` pointer. That override
controls this run.

## DG-DL-002 — Objective and edge semantics

The objective is final integration and release-assurance ordering for the
accepted SCA-004 Root carriers. Eight accepted relationships are gating. The
DEL-04-11 validator relationship, package membership, and two App notice/fan-in
edges are non-gating and do not determine SCC ordering.

## DG-DL-003 — Cycle disposition

No non-trivial SCC exists. No decompose, invert, merge, or cut move is needed;
no human-gated decision was made and no cycle was silently linearized.

## DG-DL-004 — Derivative boundary

This graph cites accepted SCA-004 revision 1.3, R7, and the N1/N2 returns. It
must be re-derived after estimates/schedule or any accepted dependency change.
"""
    (HERE / "Decision_Log.md").write_text(decision, encoding="utf-8")

    summary = f"""# Graph derivation summary

- Result: `{'PASS' if not nontrivial else 'BLOCKED'}`.
- Node set: exact equality with 53 applied register rows plus six packages.
- Package-membership edges: 53, structural and non-gating.
- Authoritative local declarations: 16 rows across eight `_DEPENDENCIES.md` files.
- Unique Root relationships: 9 (8 gating, 1 non-gating).
- Cross-loop notice/fan-in edges: 2, non-gating and non-authoritative.
- SCCs: {len(components)} singleton, {len(nontrivial)} non-trivial.
- Human-gated cut/merge required: {'yes' if nontrivial else 'no'}.
- Phase-1 initialized-empty warning: cleared for all seven SCA-004 carriers.
- Required rerun: after estimates/schedule or any accepted dependency change.
"""
    (HERE / "SUMMARY.md").write_text(summary, encoding="utf-8")

    with (HERE / "INPUT_HASHES.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["Path", "SHA256", "Role"])
        for path, expected in sorted(EXPECTED_INPUTS.items(), key=lambda item: str(item[0])):
            writer.writerow([str(path.relative_to(ROOT)), expected, "accepted basis"])
        for deliverable_id in sorted(EXPECTED_DEPENDENCY_HASHES):
            path = dependency_paths[deliverable_id]
            writer.writerow([str(path.relative_to(ROOT)), EXPECTED_DEPENDENCY_HASHES[deliverable_id], "N2 dependency truth"])

    artifact_names = ["DAG.md", "Decision_Log.md", "INPUT_HASHES.csv", "SCC_Report.md", "SUMMARY.md", "WORK_GRAPH.json", "derive_graph.py"]
    with (HERE / "ARTIFACT_HASHES.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["File", "SHA256"])
        for name in artifact_names:
            writer.writerow([name, sha256(HERE / name)])

    if nontrivial:
        raise SystemExit("Non-trivial SCC requires human-gated resolution")


if __name__ == "__main__":
    main()
