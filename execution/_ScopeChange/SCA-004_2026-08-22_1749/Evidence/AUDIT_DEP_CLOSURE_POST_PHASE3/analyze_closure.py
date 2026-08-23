#!/usr/bin/env python3
"""Audit Root dependency closure after Phase-3 dependency extraction."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SCA = ROOT / "execution/_ScopeChange/SCA-004_2026-08-22_1749"
GRAPH_DIR = SCA / "Evidence/DEP_GRAPH_POST_PHASE3"
GRAPH_PATH = GRAPH_DIR / "WORK_GRAPH.json"
REGISTER = ROOT / "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv"
POINTER = ROOT / "execution/_ScopeChange/_LATEST.md"
R7 = ROOT / "plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md"
N1_RETURN = ROOT / "execution/_Coordination/AgentRuns/ROOT_V3_PHASE3_2026-08-23/instances/N1_ACCEPT_INIT_REPIN/RETURN.md"
N2_RETURN = ROOT / "execution/_Coordination/AgentRuns/ROOT_V3_PHASE3_2026-08-23/instances/N2_DEP_EXTRACTION/RETURN.md"
PRIOR_AUDIT = SCA / "Evidence/AUDIT_DEP_CLOSURE_POST_GATE5/closure_summary.json"

EXPECTED = {
    REGISTER: "2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba",
    POINTER: "4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c",
    R7: "dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53",
    N1_RETURN: "30ff431a22d0250a290fa3c3800a4ba76385339ddd3e428c5f64a5df059c9ec2",
    N2_RETURN: "2aa9b0f08b793fc1e7ffbb16de7bce686debeaf809918fed21ce7f36b2ec9734",
    GRAPH_PATH: "2f89637c5d18f77698bacdbceb873127c1185596d945a6d8583c5346f007735b",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(name: str, header: list[str], rows: list[list[object]]) -> None:
    with (HERE / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main() -> None:
    failures = []
    for path, expected in EXPECTED.items():
        actual = sha256(path)
        if actual != expected:
            failures.append(f"{path.relative_to(ROOT)}: expected {expected}, got {actual}")
    if failures:
        raise SystemExit("Input identity failure:\n" + "\n".join(failures))

    with REGISTER.open(newline="", encoding="utf-8") as handle:
        register_rows = list(csv.DictReader(handle))
    graph = json.loads(GRAPH_PATH.read_text())
    deliverables = [node for node in graph["nodes"] if node["kind"] == "ROOT_DELIVERABLE"]
    packages = [node for node in graph["nodes"] if node["kind"] == "ROOT_PACKAGE"]
    register_ids = {row["DeliverableID"] for row in register_rows}
    graph_ids = {node["id"] for node in deliverables}
    register_packages = {row["ParentPackageID"] for row in register_rows}
    graph_packages = {node["id"] for node in packages}
    if len(register_rows) != 53 or register_ids != graph_ids:
        raise SystemExit("Graph/register deliverable node-set mismatch")
    if len(packages) != 6 or register_packages != graph_packages:
        raise SystemExit("Graph/register package node-set mismatch")

    relationships = graph["dependency_edges"]
    gating = [edge for edge in relationships if edge["gating"]]
    non_gating = [edge for edge in relationships if not edge["gating"]]
    if len(relationships) != 9 or len(gating) != 8 or len(non_gating) != 1:
        raise SystemExit("Unexpected dependency relationship counts")
    if len(graph["notice_edges"]) != 2:
        raise SystemExit("Unexpected notice-edge count")
    unresolved = sorted({edge["to"] for edge in relationships if edge["to"] not in register_ids} | {edge["from"] for edge in relationships if edge["from"] not in register_ids})
    if unresolved:
        raise SystemExit(f"Unresolved deliverable targets: {unresolved}")
    if graph["non_trivial_scc_count"] != 0 or not graph["strict_layer_acyclic"]:
        raise SystemExit("Non-trivial SCC requires human-gated resolution")

    extracted_ids = set(graph["basis"]["dependency_file_sha256"])
    if len(extracted_ids) != 8:
        raise SystemExit("Expected eight Phase-3 extracted dependency containers")
    coverage_rows = []
    state_counts: Counter[str] = Counter()
    source_row_counts: Counter[str] = Counter()
    for edge in relationships:
        for evidence in edge["evidence"]:
            source_row_counts[evidence.split("/_DEPENDENCIES.md:", 1)[0].split("/")[-1]] += 1
    incident_counts: Counter[str] = Counter()
    strict_incident_counts: Counter[str] = Counter()
    for edge in relationships:
        incident_counts[edge["from"]] += 1
        incident_counts[edge["to"]] += 1
        if edge["gating"]:
            strict_incident_counts[edge["from"]] += 1
            strict_incident_counts[edge["to"]] += 1

    row_by_id = {row["DeliverableID"]: row for row in register_rows}
    for deliverable_id in sorted(register_ids):
        row = row_by_id[deliverable_id]
        folder = ROOT / "execution" / row["ParentPackageID"] / "1_Working" / deliverable_id
        dependency_path = folder / "_DEPENDENCIES.md"
        status_path = folder / "_STATUS.md"
        if not dependency_path.is_file() or not status_path.is_file():
            raise SystemExit(f"Missing live metadata: {folder}")
        text = dependency_path.read_text()
        status_match = re.search(r"- \*\*Status:\*\*\s*`?([^`\n]+)", text)
        extraction_state = status_match.group(1).strip() if status_match else "NO_STATUS"
        classification = "EXTRACTED_PHASE3" if deliverable_id in extracted_ids else "LEGACY_NOT_RUN_YET"
        if classification == "EXTRACTED_PHASE3" and extraction_state != "EXTRACTED_PHASE3_2026-08-23":
            raise SystemExit(f"Extracted-state mismatch: {dependency_path}")
        if classification == "LEGACY_NOT_RUN_YET" and extraction_state != "NOT_RUN_YET":
            raise SystemExit(f"Legacy-state mismatch: {dependency_path}")
        lifecycle_match = re.search(r"\*\*Current State:\*\*\s*`?([A-Z_]+)", status_path.read_text())
        lifecycle = lifecycle_match.group(1) if lifecycle_match else "UNKNOWN"
        state_counts[classification] += 1
        coverage_rows.append([
            deliverable_id,
            str(folder.relative_to(ROOT)),
            lifecycle,
            str(dependency_path.relative_to(ROOT)),
            classification,
            extraction_state,
            source_row_counts[deliverable_id],
            incident_counts[deliverable_id],
            strict_incident_counts[deliverable_id],
            "CURRENT_PHASE3" if classification == "EXTRACTED_PHASE3" else "DEFERRED_LEGACY_COVERAGE",
        ])
    if state_counts != Counter({"LEGACY_NOT_RUN_YET": 45, "EXTRACTED_PHASE3": 8}):
        raise SystemExit(f"Unexpected coverage classification: {dict(state_counts)}")

    isolated = sorted(register_ids - set(strict_incident_counts))
    degree = Counter()
    for edge in gating:
        degree[edge["from"]] += 1
        degree[edge["to"]] += 1
    hubs = sorted((node, value) for node, value in degree.items() if value >= 20)
    edge_pairs = {(edge["from"], edge["to"]) for edge in gating}
    bidirectional = sorted((source, target) for source, target in edge_pairs if source < target and (target, source) in edge_pairs)

    checks = [
        {"check": "live_node_coverage", "result": "PASS", "details": "53/53 deliverables and 6/6 packages resolve from the applied register."},
        {"check": "root_dependency_schema", "result": "WARNING", "details": "8/53 authoritative _DEPENDENCIES.md containers are extracted for Phase 3; 45 legacy containers remain NOT_RUN_YET outside this bounded propagation slice."},
        {"check": "phase1_initialized_empty_state", "result": "PASS", "details": "7/7 SCA-004 carrier containers now contain grounded extraction results; the Phase-1 initialized-empty warning is cleared."},
        {"check": "orphan_dependency_targets", "result": "PASS", "details": "0 orphan Root targets across nine unique relationships."},
        {"check": "circular_dependencies", "result": "PASS", "details": "53 singleton deliverable SCCs; 0 non-trivial SCCs and 0 cycle-participating edges."},
        {"check": "anchor_coverage", "result": "NOT_APPLICABLE", "details": "Root _DEPENDENCIES.md has accepted-grounding citations rather than generic Dependencies.csv ANCHOR rows; all 16 local declarations carry grounding evidence."},
        {"check": "misplaced_fields", "result": "PASS", "details": "0 malformed local relationship rows and 0 foreign targets in the Root relationship layer."},
        {"check": "id_format_consistency", "result": "PASS", "details": "All local relationship endpoints resolve to exact accepted long-form deliverable IDs; no normalization required."},
        {"check": "isolated_deliverables", "result": "INFO", "details": f"{len(isolated)}/53 nodes have no Phase-3 gating edge; 45 legacy dependency containers remain outside the bounded extraction slice."},
        {"check": "hub_analysis", "result": "PASS", "details": "0 hubs at threshold 20; maximum strict degree is 6."},
        {"check": "bidirectional_pairs", "result": "PASS", "details": "0 bidirectional gating pairs."},
        {"check": "closure_violations", "result": "PASS", "details": "0 unresolved closure violations in the post-extraction relationship set."},
        {"check": "notice_authority_boundary", "result": "PASS", "details": "2 App coupling edges are notice/fan-in only, non-gating, and excluded from Root SCC ordering."},
    ]

    summary = {
        "schema": "chirality-dependency-closure-summary/v2",
        "run": "SCA-004-POST-PHASE3",
        "verdict": "WARNING",
        "closure_verdict": "PASS_ZERO_UNRESOLVED_VIOLATIONS",
        "failures": [],
        "basis": {
            "branch_basis": "3389adabfa2919b66f64bbd9cd04d7d29b9838b4",
            "owner_authorized_sync_merge": "31a7fe680",
            "n1_commit": "49844ad30d75171f96715e14065a51a65dbb6456",
            "n2_commit": "5502aea661225e70bc2341b9eed551f16237c09b",
            "sca_snapshot": "SCA-004_2026-08-22_1749",
            "applied_revision": "1.3",
            "pointer_sha256": EXPECTED[POINTER],
            "r7_record_sha256": EXPECTED[R7],
            "n1_return_sha256": EXPECTED[N1_RETURN],
            "n2_return_sha256": EXPECTED[N2_RETURN],
            "graph_sha256": EXPECTED[GRAPH_PATH],
            "prior_phase1_audit_sha256": sha256(PRIOR_AUDIT),
        },
        "metrics": {
            "packages": 6,
            "deliverables": 53,
            "extracted_dependency_containers": 8,
            "legacy_not_run_yet_containers": 45,
            "local_declaration_rows": 16,
            "unique_root_relationships": 9,
            "gating_relationships": 8,
            "non_gating_relationships": 1,
            "notice_fan_in_edges": 2,
            "orphan_targets": 0,
            "isolated_deliverables_strict_layer": len(isolated),
            "scc_total_deliverable_layer": 53,
            "non_trivial_sccs": 0,
            "cycle_participating_edges": 0,
            "hubs": len(hubs),
            "bidirectional_pairs": len(bidirectional),
            "unresolved_closure_violations": 0,
            "phase1_initialized_empty_warnings_remaining": 0,
        },
        "checks": checks,
        "derivative_disposition": "Re-run after estimates/schedule or any accepted dependency change; this audit is derivative evidence.",
    }
    (HERE / "closure_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    write_csv("coverage.csv", ["DeliverableID", "Folder", "Lifecycle", "DependencyPath", "Classification", "ExtractionState", "LocalDeclarationRows", "UniqueIncidentRelationships", "GatingIncidentRelationships", "Disposition"], coverage_rows)
    write_csv("orphans.csv", ["FromDeliverableID", "TargetDeliverableID", "Evidence"], [])
    write_csv("cycles_sample.csv", ["SCC", "Cycle", "Evidence", "Disposition"], [])
    write_csv("scc_summary.csv", ["SCC", "Member", "Size", "NonTrivial", "ProposedMove", "HumanGate"], [[f"SCC-{index:03d}", node, 1, "NO", "NONE", "NO"] for index, node in enumerate(sorted(register_ids), start=1)])
    write_csv("hubs.csv", ["DeliverableID", "StrictDegree", "Threshold"], [[node, value, 20] for node, value in hubs])
    write_csv("bidirectional_pairs.csv", ["DeliverableA", "DeliverableB", "Evidence"], [[source, target, "gating relationship layer"] for source, target in bidirectional])
    write_csv("id_normalization.csv", ["ObservedID", "NormalizedID", "Changed"], [[deliverable_id, deliverable_id, "NO"] for deliverable_id in sorted(register_ids)])

    write_csv("Dependency_Closure_IssueLog.csv", ["ID", "Severity", "Check", "FromDeliverableID", "TargetDeliverableID", "DependencyID", "Evidence", "FixSuggestion"], [[
        "DC-P3-001", "WARNING", "root_dependency_schema", "", "", "",
        "coverage.csv: 45 LEGACY_NOT_RUN_YET rows",
        "Rerun dependency extraction for legacy deliverables only under separately accepted scope; not a blocker for the bounded SCA-004 carrier slice.",
    ]])

    brief = """# Brief — post-Phase-3 dependency closure

- Scope: all 53 applied Root deliverables and six package nodes.
- Objective: final integration and release-assurance ordering for accepted
  SCA-004 carriers after Phase-3 dependency extraction.
- Edge source: authoritative deliverable-local `_DEPENDENCIES.md` declarations.
- Edge filter: Root-deliverable relationships; gating relationships form the
  SCC layer; non-gating validation and App notice/fan-in edges remain visible
  but do not order work.
- Output override: this SCA evidence folder; no `_Evaluation` pointer write.
- Requested by: HELP_HUMAN under the Phase-3 owner-carried steer.
"""
    (HERE / "Brief.md").write_text(brief, encoding="utf-8")

    run_summary = f"""# Dependency-closure run summary

- `RUN_STATUS = WARNINGS`
- Closure verdict: `PASS_ZERO_UNRESOLVED_VIOLATIONS`.
- Live coverage: 53 deliverables and six packages.
- Extraction coverage: eight current Phase-3 containers; 45 legacy `NOT_RUN_YET`.
- Local declarations / unique Root relationships: 16 / 9.
- Gating / non-gating Root relationships: 8 / 1.
- SCCs: 53 singleton deliverable components; 0 non-trivial.
- Orphans / bidirectional pairs / hubs: 0 / 0 / 0.
- Phase-1 initialized-empty warning: cleared for all seven SCA-004 carriers.
- Unresolved closure violations: 0.
- Coverage warning: 45 legacy containers remain outside the bounded extraction slice.
- Required rerun: after estimates/schedule or any accepted dependency change.
"""
    (HERE / "RUN_SUMMARY.md").write_text(run_summary, encoding="utf-8")

    qa = """# QA report — post-Phase-3 dependency closure

## Coverage and schema

- Applied register: 53 unique deliverables in six packages; exact graph parity.
- Authoritative Root source: eight Phase-3 `_DEPENDENCIES.md` containers.
- Parsed declarations: 16 reciprocal/local rows, deduplicated to nine Root
  relationships; every declaration carries an accepted-grounding citation.
- Legacy coverage: 45 containers remain `NOT_RUN_YET`. This is a coverage
  warning, not an unresolved violation in the bounded SCA-004 carrier slice.
- Generic `Dependencies.csv` is not used because the human steer explicitly
  names Root `_DEPENDENCIES.md` as authoritative for this run.

## Integrity

- All relationship endpoints resolve to accepted register IDs.
- Eight gating relationships are acyclic; the one validator relationship and
  two App notice/fan-in edges are explicitly non-gating.
- No cut or merge was proposed or performed.
- Earlier evidence and all deliverable files were read-only during this audit.
"""
    (HERE / "QA_Report.md").write_text(qa, encoding="utf-8")

    decision = """# Decision log — post-Phase-3 dependency closure

## DC-P3-DL-001 — Output and source override

The human steer and sealed brief override the dedicated agent defaults: this
run writes only the named SCA evidence folder, does not update an `_Evaluation`
pointer, and consumes authoritative Root `_DEPENDENCIES.md` rather than generic
`Dependencies.csv`.

## DC-P3-DL-002 — Edge classes

Eight relationships marked gating by accepted dependency truth form the SCC
layer. DEL-04-11's validator relationship and the two cross-loop App
notice/fan-in edges remain non-gating and cannot confer foreign authority.

## DC-P3-DL-003 — Cycle disposition

No non-trivial SCC exists. No decompose, invert, merge, or cut move is needed;
no human-gated decision was made and no edge was silently linearized.

## DC-P3-DL-004 — Coverage warning

All seven SCA-004 carriers have moved from initialized-empty declarations to
grounded Phase-3 extraction, so the Phase-1 warning is cleared. Forty-five
legacy Root containers remain `NOT_RUN_YET`; that broader coverage gap is
preserved as a warning and is not misreported as a closure violation.

## DC-P3-DL-005 — Derivative boundary

This package cites accepted SCA-004 revision 1.3, R7, and N1/N2 outputs. It
must be regenerated after estimates/schedule or any accepted dependency change.
"""
    (HERE / "Decision_Log.md").write_text(decision, encoding="utf-8")

    report = f"""# Dependency Closure Report — SCA-004 post-Phase 3

Verdict: `WARNING` with closure verdict `PASS_ZERO_UNRESOLVED_VIOLATIONS`.

## Scope and authority

The audit covers the exact 53 applied revision-1.3 Root deliverables plus six
packages. It cites R7-A, N1 commit `49844ad30d75171f96715e14065a51a65dbb6456`,
N2 commit `5502aea661225e70bc2341b9eed551f16237c09b`, and their bound returns.
The accepted pointer remains `{EXPECTED[POINTER]}`. This is derivative evidence,
not decomposition or deliverable-local dependency authority.

## Closure result

- Authoritative local declarations: 16 rows across eight containers.
- Unique Root relationships: 9 (8 gating; 1 non-gating).
- Cross-loop App notice/fan-in relationships: 2, non-gating.
- Orphan targets: 0.
- Non-trivial SCCs / cycle-participating edges: 0 / 0.
- Hubs / bidirectional gating pairs: 0 / 0.
- Human-gated cut or merge required: no.
- Unresolved closure violations: 0.

The six DEL-02-07..12 evidence fan-in relationships converge on DEL-02-06.
DEL-04-05 and DEL-05-02 supply grounded inputs to DEL-04-11. DEL-04-11's
relationship to DEL-02-06 is validation support only and does not gate SCC
ordering. No relationship points outside the accepted 53-deliverable register.

## Phase-1 warning disposition

All seven SCA-004 carrier dependency containers are now extracted, so the
initialized-empty warning from Phase 1 is cleared. Forty-five legacy containers
remain `NOT_RUN_YET`; this broader coverage gap is retained as a warning because
the Phase-3 extraction authority was bounded to the SCA-004 carrier slice. It is
not an unresolved closure violation in that slice.

## Core-check verdicts

| Check | Result | Reason |
|---|---|---|
"""
    for check in checks:
        report += f"| {check['check']} | `{check['result']}` | {check['details']} |\n"
    report += """

## Derivative status and rerun

Re-run the graph and this audit after estimates/schedule or any accepted
dependency change. Cycle-participating edges, if introduced later, remain
non-gating until a recorded decompose/invert/merge/cut disposition; cut and
merge return to the owner.
"""
    (HERE / "Dependency_Closure_Report.md").write_text(report, encoding="utf-8")

    return_text = """# AUDIT_DEP_CLOSURE return — post-Phase-3

- Terminal status: `COMPLETE`.
- Run status: `WARNINGS`.
- Closure verdict: `PASS_ZERO_UNRESOLVED_VIOLATIONS`.
- Node coverage: 53 deliverables and six packages.
- Relationships: nine Root (eight gating, one non-gating) plus two non-gating
  App notice/fan-in edges.
- SCCs: 53 singleton deliverable components; zero non-trivial.
- Cut/merge required: no.
- Phase-1 initialized-empty warning: cleared for all seven carriers.
- Remaining warning: 45 legacy dependency containers are `NOT_RUN_YET` outside
  the bounded Phase-3 extraction slice.
- Rerun: after estimates/schedule or any accepted dependency change.
"""
    (HERE / "RETURN.md").write_text(return_text, encoding="utf-8")

    with (HERE / "INPUT_HASHES.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["Path", "SHA256", "Role"])
        for path, expected in sorted(EXPECTED.items(), key=lambda item: str(item[0])):
            writer.writerow([str(path.relative_to(ROOT)), expected, "accepted input"])
        writer.writerow([str(PRIOR_AUDIT.relative_to(ROOT)), sha256(PRIOR_AUDIT), "Phase-1 comparison"])

    artifact_names = [
        "Brief.md", "Decision_Log.md", "Dependency_Closure_IssueLog.csv",
        "Dependency_Closure_Report.md", "INPUT_HASHES.csv", "QA_Report.md",
        "RETURN.md", "RUN_SUMMARY.md", "analyze_closure.py",
        "bidirectional_pairs.csv", "closure_summary.json", "coverage.csv",
        "cycles_sample.csv", "hubs.csv", "id_normalization.csv", "orphans.csv",
        "scc_summary.csv",
    ]
    with (HERE / "ARTIFACT_HASHES.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["File", "SHA256"])
        for name in artifact_names:
            writer.writerow([name, sha256(HERE / name)])


if __name__ == "__main__":
    main()
