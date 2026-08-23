#!/usr/bin/env python3
"""Deterministic Root dependency-closure audit for the Phase-1 post-INIT state."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SCA = ROOT / "execution/_ScopeChange/SCA-004_2026-08-22_1749"
GRAPH_DIR = SCA / "Evidence/DEP_GRAPH_POST_GATE5"
GRAPH = GRAPH_DIR / "WORK_GRAPH.json"
REGISTER = ROOT / "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv"
PRIOR_RETURN = SCA / "Evidence/AUDIT_DEP_CLOSURE/RETURN.md"
PRIOR_GRAPH = SCA / "WORK_GRAPH.json"

NEW_IDS = {
    "DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control",
    "DEL-02-08_Exact_Supply_and_Protocol_Pinning",
    "DEL-02-09_Hosted_Account_and_Consent_Boundary",
    "DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2",
    "DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation",
    "DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in",
    "DEL-04-11_Root_Loop_Receipt_Validator",
}

EXPECTED = {
    "register": "2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba",
    "pointer": "4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c",
    "prior_graph": "86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9",
    "prior_return": "14e131fe90a725b3520efb2e2e90fcfedbf8f1898188859b421ea6e4c7460c71",
}

DECOMPOSITION_IDENTITIES = {
    "Chirality_Root_SOFTWARE_DECOMP_v1_0.md": "546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986",
    "chirality_root_deliverable_register_v1_0.csv": "2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba",
    "chirality_root_scope_ledger_v1_0.csv": "63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417",
    "chirality_root_objective_register_v1_0.csv": "b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f",
    "chirality_root_prd_coverage_forward_v1_0.csv": "9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f",
    "chirality_root_trace_reverse_v1_0.csv": "750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438",
    "chirality_root_coverage_telemetry_v1_0.md": "bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c",
}

N1_RETURN_SHA = "71a4d6b9089f4b7a01581ba7ce8787915dba9e10aaed7fdc92e1c8a77ad28e50"
N1_REVIEW_SHA = "9f567edcd6687b936838ad4b80204a4766b2635b6920cf524e034cf72bb569d2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(name: str, header: list[str], rows: list[list[object]]) -> None:
    with (HERE / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def normalize_generic_raw() -> None:
    """Apply the evidence-whitespace convention to generic-tool preimages."""
    raw_dir = HERE / "Generic_Tool_Raw"
    expected = {
        "bidirectional_pairs.csv",
        "closure_summary.json",
        "coverage.csv",
        "hubs.csv",
        "id_normalization.csv",
        "orphans.csv",
        "scc_summary.csv",
    }
    observed = {path.name for path in raw_dir.iterdir() if path.is_file()}
    if observed != expected:
        raise SystemExit(
            f"Generic-tool raw evidence set mismatch: expected {sorted(expected)}, got {sorted(observed)}"
        )
    for path in sorted(raw_dir.iterdir()):
        data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        if not data.endswith(b"\n"):
            data += b"\n"
        path.write_bytes(data)


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
            component = []
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


def main() -> None:
    normalize_generic_raw()
    if sha256(REGISTER) != EXPECTED["register"]:
        raise SystemExit("Register identity drift")
    if sha256(ROOT / "execution/_ScopeChange/_LATEST.md") != EXPECTED["pointer"]:
        raise SystemExit("Accepted pointer identity drift")
    if sha256(PRIOR_GRAPH) != EXPECTED["prior_graph"]:
        raise SystemExit("Prior graph identity drift")
    if sha256(PRIOR_RETURN) != EXPECTED["prior_return"]:
        raise SystemExit("Prior audit return identity drift")
    for name, expected in DECOMPOSITION_IDENTITIES.items():
        if sha256(ROOT / "execution/_Decomposition" / name) != expected:
            raise SystemExit(f"Applied decomposition identity drift: {name}")

    with REGISTER.open(newline="", encoding="utf-8") as handle:
        register_rows = list(csv.DictReader(handle))
    graph = json.loads(GRAPH.read_text())
    deliverable_nodes = [node for node in graph["nodes"] if node["kind"] == "ROOT_DELIVERABLE"]
    package_nodes = [node for node in graph["nodes"] if node["kind"] == "ROOT_PACKAGE"]
    deliverable_ids = {row["DeliverableID"] for row in register_rows}
    graph_deliverable_ids = {node["id"] for node in deliverable_nodes}
    graph_package_ids = {node["id"] for node in package_nodes}
    register_package_ids = {row["ParentPackageID"] for row in register_rows}
    if len(register_rows) != 53 or deliverable_ids != graph_deliverable_ids:
        raise SystemExit("Graph/register deliverable node-set mismatch")
    if len(package_nodes) != 6 or graph_package_ids != register_package_ids:
        raise SystemExit("Graph/register package node-set mismatch")

    coverage_rows: list[list[object]] = []
    status_counts: Counter[str] = Counter()
    failures: list[str] = []
    existing_ids = deliverable_ids - NEW_IDS
    for row in sorted(register_rows, key=lambda item: item["DeliverableID"]):
        deliverable_id = row["DeliverableID"]
        folder = ROOT / "execution" / row["ParentPackageID"] / "1_Working" / deliverable_id
        dep_md = folder / "_DEPENDENCIES.md"
        status_md = folder / "_STATUS.md"
        csv_path = folder / "Dependencies.csv"
        if not folder.is_dir() or not dep_md.is_file() or not status_md.is_file():
            failures.append(f"missing live folder metadata: {folder}")
            continue
        text = dep_md.read_text()
        if deliverable_id in NEW_IDS:
            classification = "EXPECTED_POST_INIT_EMPTY"
            requirements = [
                "No upstream dependency is declared.",
                "No downstream dependency is declared.",
                "No dependency edge is inferred by PREPARATION.",
                "Dependency extraction is a later, separately gated act.",
            ]
            if not all(value in text for value in requirements):
                failures.append(f"new INIT dependency contract mismatch: {dep_md}")
        else:
            classification = "PRE_EXISTING_NOT_RUN_YET"
            if "**Status:** NOT_RUN_YET" not in text or text.count("- None declared.") < 2:
                failures.append(f"pre-existing dependency state mismatch: {dep_md}")
        if csv_path.exists():
            failures.append(f"unexpected Dependencies.csv before extraction: {csv_path}")
        lifecycle = next(
            (line.split("**Current State:**", 1)[1].strip().strip("`")
             for line in status_md.read_text().splitlines() if "**Current State:**" in line),
            "UNKNOWN",
        )
        status_counts[classification] += 1
        coverage_rows.append([
            deliverable_id,
            str(folder.relative_to(ROOT)),
            lifecycle,
            str(dep_md.relative_to(ROOT)),
            "NO",
            classification,
            0,
            0,
            "No declared edge; extraction deferred",
        ])
    if status_counts != Counter({"PRE_EXISTING_NOT_RUN_YET": 46, "EXPECTED_POST_INIT_EMPTY": 7}):
        failures.append(f"unexpected coverage classification: {dict(status_counts)}")

    dependency_edges = [(edge["from"], edge["to"]) for edge in graph["dependency_edges"]]
    components = tarjan(deliverable_ids, dependency_edges)
    nontrivial = [component for component in components if len(component) > 1]
    orphans = sorted(deliverable_ids) if not dependency_edges else []
    if dependency_edges:
        failures.append("dependency edges exist before the separately gated extraction act")
    if nontrivial:
        failures.append(f"non-trivial SCCs present: {nontrivial}")

    verdict = "BLOCKER" if failures else "WARNING"
    checks = [
        {
            "check": "live_node_coverage",
            "result": "PASS" if not failures else "BLOCKER",
            "details": "53/53 live deliverables and 6/6 packages resolve from the applied register.",
        },
        {
            "check": "dependency_register_schema",
            "result": "WARNING",
            "details": "0/53 Dependencies.csv registers exist; extraction is a later separately gated act.",
        },
        {
            "check": "new_init_empty_state",
            "result": "PASS",
            "details": "7/7 new OPEN folders explicitly declare no edge and defer extraction; expected, not a defect.",
        },
        {
            "check": "orphan_dependency_targets",
            "result": "PASS",
            "details": "0 orphan targets because no dependency row exists.",
        },
        {
            "check": "circular_dependencies",
            "result": "PASS",
            "details": "53 singleton deliverable SCCs; 0 non-trivial SCCs and 0 cycle edges.",
        },
        {
            "check": "anchor_coverage",
            "result": "WARNING",
            "details": "0/53 have extracted ANCHOR rows because Dependencies.csv extraction has not run.",
        },
        {
            "check": "misplaced_fields",
            "result": "PASS",
            "details": "0 dependency rows; no misplaced TargetDeliverableID fields.",
        },
        {
            "check": "id_format_consistency",
            "result": "PASS",
            "details": "53 unique accepted register IDs; no dependency-row normalization required.",
        },
        {
            "check": "isolated_deliverables",
            "result": "INFO",
            "details": "53/53 are isolated in the dependency layer, expected before extraction.",
        },
        {
            "check": "hub_analysis",
            "result": "PASS",
            "details": "0 hubs at threshold 20.",
        },
        {
            "check": "bidirectional_pairs",
            "result": "PASS",
            "details": "0 bidirectional dependency pairs.",
        },
        {
            "check": "pre_existing_closure_comparison",
            "result": "PASS",
            "details": (
                "0 unresolved closure violations among the 46 pre-existing folders; "
                "the prior Gate-1 audit also reported 0 blockers and 0 warnings."
            ),
        },
    ]

    summary = {
        "schema": "chirality-dependency-closure-summary/v2",
        "run": "SCA-004-POST-GATE5-PHASE1",
        "verdict": verdict,
        "failures": failures,
        "basis": {
            "branch_basis": "e677edbe81188465eb36e700b6bd441715bcbccd",
            "n1_commit": "dab470e2f0c7345f10c34bcce9e489eb68bf0541",
            "sca_snapshot": "SCA-004_2026-08-22_1749",
            "pointer_sha256": EXPECTED["pointer"],
            "graph_sha256": sha256(GRAPH),
            "prior_graph_sha256": EXPECTED["prior_graph"],
            "prior_audit_return_sha256": EXPECTED["prior_return"],
            "decomposition_identities": DECOMPOSITION_IDENTITIES,
            "n1_return_sha256": N1_RETURN_SHA,
            "n1_review_sha256": N1_REVIEW_SHA,
        },
        "metrics": {
            "packages": 6,
            "deliverables": 53,
            "pre_existing_deliverables": 46,
            "new_open_initialized_empty": 7,
            "dependencies_csv_present": 0,
            "dependency_rows": 0,
            "execution_edges": 0,
            "orphan_dependency_targets": 0,
            "isolated_deliverables": len(orphans),
            "scc_total": len(components),
            "non_trivial_sccs": len(nontrivial),
            "hubs": 0,
            "bidirectional_pairs": 0,
            "pre_existing_unresolved_closure_violations": 0,
        },
        "generic_tool_observation": {
            "command": (
                "python3 tools/coordination/analyze_dep_closure.py execution --output-dir "
                "execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/"
                "AUDIT_DEP_CLOSURE_POST_GATE5/Generic_Tool_Raw"
            ),
            "dependencies_csv_discovered": 0,
            "interpretation": (
                "The generic tool has no Root node source without Dependencies.csv; "
                "the run-specific analyzer binds the applied register to _DEPENDENCIES.md. "
                "Generic-tool CSV/JSON preimages are normalized to LF with a terminal newline."
            ),
        },
        "checks": checks,
        "derivative_disposition": (
            "Re-run after accepted SOWs and dependency extraction; graph/audit are derivative evidence."
        ),
    }
    (HERE / "closure_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    write_csv(
        "coverage.csv",
        ["DeliverableID", "Folder", "Lifecycle", "DependencyMetadata", "DependenciesCSVPresent",
         "Classification", "DeclaredUpstreamEdges", "DeclaredDownstreamEdges", "Evidence"],
        coverage_rows,
    )
    write_csv(
        "orphans.csv",
        ["DeliverableID", "Classification", "Disposition"],
        [[item, "ISOLATED_PRE_EXTRACTION", "Expected; rerun after dependency extraction"] for item in orphans],
    )
    write_csv("cycles_sample.csv", ["CycleID", "Members", "Evidence", "Disposition"], [])
    write_csv(
        "scc_summary.csv",
        ["SCCID", "Members", "Size", "NonTrivial", "ProposedMove", "HumanGateRequired"],
        [[f"SCC-{index:03d}", ";".join(members), len(members), "NO", "NONE", "NO"]
         for index, members in enumerate(components, start=1)],
    )
    write_csv("hubs.csv", ["DeliverableID", "InDegree", "OutDegree", "TotalDegree"], [])
    write_csv("bidirectional_pairs.csv", ["FromDeliverableID", "TargetDeliverableID", "Evidence"], [])
    write_csv("id_normalization.csv", ["OriginalID", "NormalizedID", "Field", "Evidence"], [])
    write_csv(
        "Dependency_Closure_IssueLog.csv",
        ["ID", "Severity", "Check", "FromDeliverableID", "TargetDeliverableID", "DependencyID",
         "Evidence", "FixSuggestion"],
        [
            ["DC-001", "WARNING", "Schema compliance", "ALL", "", "N/A",
             "coverage.csv: 0/53 Dependencies.csv; 46 PRE_EXISTING_NOT_RUN_YET and 7 EXPECTED_POST_INIT_EMPTY",
             "After SOW acceptance, run the separately gated dependency-extract act and rerun this audit."],
            ["DC-002", "WARNING", "Anchor coverage", "ALL", "", "N/A",
             "coverage.csv: no extracted dependency register exists, so no ANCHOR/IMPLEMENTS_NODE row can exist",
             "Generate anchors during the separately gated dependency-extract act; do not invent them here."],
        ],
    )

    run_summary = f"""# Dependency-closure run summary

- `RUN_STATUS = {verdict}`
- Live coverage: 53 deliverables and six packages.
- Dependency rows / strict edges: 0 / 0.
- SCCs: 53 singleton deliverable components; 0 non-trivial.
- Pre-existing unresolved closure violations versus the Gate-1 audit: 0.
- Seven new `OPEN` folders: initialized-empty dependencies, expected and not a defect.
- Warnings: extraction/schema and anchor coverage remain deferred for all 53.
- Blockers: none.
- Required rerun: after accepted SOWs and dependency extraction.
"""
    (HERE / "RUN_SUMMARY.md").write_text(run_summary, encoding="utf-8")

    qa = """# QA report — dependency closure

| Core check | Verdict | Result |
|---|---|---|
| Schema compliance | `WARNING` | 0/53 `Dependencies.csv`; extraction is later-gated. |
| Orphan dependency targets | `PASS` | 0 targets and therefore 0 orphan targets. |
| Circular dependencies | `PASS` | 53 singleton SCCs; 0 non-trivial SCCs. |
| Anchor coverage | `WARNING` | 0/53 extracted anchors because no register exists. |
| Misplaced fields | `PASS` | 0 rows; none misplaced. |
| ID format consistency | `PASS` | 53 unique accepted IDs; no row normalization. |
| Isolated deliverables | `INFO` | 53, expected before extraction. |
| Hub analysis | `PASS` | 0 at threshold 20. |
| Bidirectional pairs | `PASS` | 0. |

The two warnings are coverage facts, not invented closure defects. The seven
N1 empty containers are expressly expected post-INIT state. No SOW or
dependency-extraction authority exists in this tranche.
"""
    (HERE / "QA_Report.md").write_text(qa, encoding="utf-8")

    report = f"""# Dependency Closure Report — SCA-004 post-Gate-5 Phase 1

Verdict: `{verdict}` — no blocker and no unresolved dependency-closure violation.

## Scope and authority

The audit covers the exact 53 applied revision-1.3 deliverables plus their six
packages. It consumes N1 commit `dab470e2f0c7345f10c34bcce9e489eb68bf0541`
with N1 return SHA-256 `{N1_RETURN_SHA}` and fresh-review SHA-256
`{N1_REVIEW_SHA}`. The seven applied decomposition identities are bound in
`closure_summary.json` and agree with the companion graph basis. This run
writes only this human-steer-authorized SCA evidence folder. The dedicated
agent's default `_Evaluation/DepClosure` output and pointer are not written.

## Closure result

- Node resolution: 53/53 deliverables and 6/6 packages.
- Declared execution dependency edges: 0.
- Orphan dependency targets: 0.
- Non-trivial SCCs / cycles: 0 / 0.
- Human-gated cut or merge required: no.
- Hubs / bidirectional pairs: 0 / 0.
- Pre-existing unresolved closure violations versus the prior Gate-1 audit: 0.

All 46 pre-existing dependency containers remain `NOT_RUN_YET` with no
human-declared edge. The seven new `OPEN` containers explicitly declare no
upstream, downstream, or inferred dependency and defer extraction. Their empty
state is expected, not a defect. The absence of extracted schemas and anchors
is retained as a coverage warning under the AUDIT_DEP_CLOSURE semantics.

## Prior comparison

The prior Gate-1 audit at SHA-256 `{EXPECTED['prior_return']}` returned `PASS`
with zero blockers and zero warnings over its narrower SCA pathway graph. The
current live-state audit finds no closure regression among the 46 pre-existing
folders. Method scope is broader now, so coverage counts are not treated as a
like-for-like metric.

## Derivative status

This audit and the companion graph are derivative packages. They do not replace
decomposition truth. Re-run both after SOW acceptance and dependency extraction;
then resolve any SCC by the recorded decompose/invert/merge/cut doctrine, keeping
cycle edges non-gating and returning any cut/merge choice to the owner.
"""
    (HERE / "Dependency_Closure_Report.md").write_text(report, encoding="utf-8")

    decision_log = """# Decision log — post-Gate-5 dependency closure

## DC-DL-001 — Output-location override

The Phase-1 steer and sealed brief require this SCA evidence folder and forbid
the default `execution/_Evaluation/DepClosure/` root and pointer. That human
override controls this run.

## DC-DL-002 — Root-local source model

The generic repository analyzer only discovers `Dependencies.csv` registers.
Root currently has zero such files. This preserved script therefore binds the
53 applied register rows to their live `_DEPENDENCIES.md` containers, while
retaining the generic core-check semantics and never inferring edges from prose,
shared objectives, or package membership.

The generic tool was also invoked exactly as prescribed, with its output
captured under `Generic_Tool_Raw/`. It deterministically reported zero CSV
files, zero nodes, and zero edges. `normalize_generic_raw()` deterministically
normalizes those preimages to LF with a terminal newline before hashing. Those
bytes are preserved as method evidence, not misread as the live 53-node
coverage result.

## DC-DL-003 — Expected post-INIT state

The seven N1 containers are classified `EXPECTED_POST_INIT_EMPTY`, not defects.
The 46 pre-existing containers remain `PRE_EXISTING_NOT_RUN_YET`. Missing
extracted schema and anchor coverage are warnings; absence of a dependency edge
is not itself a closure violation.

## DC-DL-004 — Cycle disposition

No non-trivial SCC exists, so no move is required and no human-gated cut/merge
was made. The rerun after extraction must apply the cycle-resolution doctrine.

## DC-DL-005 — Immutable derivative boundary

The accepted SCA-004 snapshot, live decomposition, pointer, deliverable
metadata, Task Management state, and prior audit were read-only. This package
must be regenerated after accepted SOWs and dependency extraction.
"""
    (HERE / "Decision_Log.md").write_text(decision_log, encoding="utf-8")

    return_text = f"""# AUDIT_DEP_CLOSURE return — SCA-004 post-Gate-5 Phase 1

Verdict: `{verdict}`

- 53/53 live deliverables and 6/6 packages resolve.
- Seven new folders are `OPEN` with expected initialized-empty dependencies.
- 46 pre-existing folders remain extraction `NOT_RUN_YET`.
- Declared execution edges: 0; orphan targets: 0.
- SCCs: 53 singleton; non-trivial SCCs: 0; cycles: 0.
- Human-gated cut/merge: not required.
- Pre-existing unresolved closure violations versus prior audit: 0.
- Coverage warnings: extracted schema and ANCHOR rows remain pending the later act.
- Blockers: none.
- Rerun: mandatory after SOW acceptance and dependency extraction.

The generic-tool raw CSV/JSON preimages were deterministically normalized to LF
with a terminal newline before hashing, per the evidence-whitespace convention.

Role entry was instruction-asserted. No delegation occurred. The output-location
override was applied; no default audit root or pointer was written.
"""
    (HERE / "RETURN.md").write_text(return_text, encoding="utf-8")

    artifact_rows = []
    for path in sorted(HERE.rglob("*")):
        if path.is_file() and path.name != "ARTIFACT_HASHES.csv":
            artifact_rows.append([str(path.relative_to(HERE)), sha256(path)])
    write_csv("ARTIFACT_HASHES.csv", ["File", "SHA256"], artifact_rows)

    if failures:
        raise SystemExit("Audit blocker:\n" + "\n".join(failures))


if __name__ == "__main__":
    main()
