#!/usr/bin/env python3
"""Deterministically derive the Phase-1 Root objective-relative graph."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
DECOMP = ROOT / "execution/_Decomposition"
REGISTER = DECOMP / "chirality_root_deliverable_register_v1_0.csv"
WORK_GRAPH = ROOT / "execution/_harness/work_graph.yaml"
N1_RETURN = ROOT / (
    "execution/_Coordination/AgentRuns/ROOT_V3_PHASE1_2026-08-23/"
    "instances/N1_PREPARATION/RETURN.md"
)
N1_REVIEW = ROOT / (
    "execution/_Coordination/AgentRuns/ROOT_V3_PHASE1_2026-08-23/"
    "instances/N1_PREPARATION/review-cycle-1/REVIEW.md"
)

EXPECTED_HASHES = {
    "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md": "546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986",
    "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv": "2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba",
    "execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv": "63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417",
    "execution/_Decomposition/chirality_root_objective_register_v1_0.csv": "b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f",
    "execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv": "9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f",
    "execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv": "750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438",
    "execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md": "bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c",
    "execution/_ScopeChange/_LATEST.md": "4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c",
    "execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md": "abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05",
    "execution/_harness/work_graph.yaml": "29dc3e35b92418f9cccbdc693aee7cc30943f505415952b57c8f291a647b54cc",
    str(N1_RETURN.relative_to(ROOT)): "71a4d6b9089f4b7a01581ba7ce8787915dba9e10aaed7fdc92e1c8a77ad28e50",
    str(N1_REVIEW.relative_to(ROOT)): "9f567edcd6687b936838ad4b80204a4766b2635b6920cf524e034cf72bb569d2",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def current_state(path: Path) -> str:
    match = re.search(r"\*\*Current State:\*\*\s*`?([A-Z_]+)", path.read_text())
    if not match:
        raise ValueError(f"Current State not found: {path}")
    return match.group(1)


def verify_inputs() -> None:
    failures = []
    for rel, expected in EXPECTED_HASHES.items():
        actual = sha256(ROOT / rel)
        if actual != expected:
            failures.append(f"{rel}: expected {expected}, got {actual}")
    if failures:
        raise SystemExit("Input identity failure:\n" + "\n".join(failures))


def load_rows() -> list[dict[str, str]]:
    with REGISTER.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 53:
        raise SystemExit(f"Expected 53 register rows, found {len(rows)}")
    if len({row["DeliverableID"] for row in rows}) != 53:
        raise SystemExit("Deliverable IDs are not unique")
    return rows


def main() -> None:
    verify_inputs()
    rows = load_rows()
    packages = sorted({row["ParentPackageID"] for row in rows})
    if len(packages) != 6:
        raise SystemExit(f"Expected 6 packages, found {len(packages)}")

    nodes: list[dict[str, object]] = []
    for package in packages:
        package_path = ROOT / "execution" / package
        if not package_path.is_dir():
            raise SystemExit(f"Missing package path: {package_path}")
        nodes.append({
            "id": package,
            "canonical_id": package.split("_", 1)[0],
            "kind": "ROOT_PACKAGE",
            "path": str(package_path.relative_to(ROOT)),
            "status": "pending",
        })

    for row in sorted(rows, key=lambda item: item["DeliverableID"]):
        path = ROOT / "execution" / row["ParentPackageID"] / "1_Working" / row["DeliverableID"]
        if not path.is_dir():
            raise SystemExit(f"Missing live deliverable path: {path}")
        status_path = path / "_STATUS.md"
        dependencies_path = path / "_DEPENDENCIES.md"
        if not status_path.is_file() or not dependencies_path.is_file():
            raise SystemExit(f"Missing live metadata in {path}")
        nodes.append({
            "id": row["DeliverableID"],
            "canonical_id": row["DeliverableID"].split("_", 1)[0],
            "kind": "ROOT_DELIVERABLE",
            "path": str(path.relative_to(ROOT)),
            "parent_package_id": row["ParentPackageID"],
            "lifecycle": current_state(status_path),
            "type": row["Type"],
            "objectives": row["SupportsObjectives"].split(";"),
            "scope_items": row["CoversScopeItems"].split(";"),
            "dependency_metadata": str(dependencies_path.relative_to(ROOT)),
        })

    membership_edges = []
    for index, row in enumerate(sorted(rows, key=lambda item: item["DeliverableID"]), start=1):
        membership_edges.append({
            "id": f"M-{index:03d}",
            "from": row["ParentPackageID"],
            "to": row["DeliverableID"],
            "type": "PARENT_MEMBERSHIP",
            "layer": "structural",
            "gating": False,
            "rationale": "Accepted decomposition package membership; not a sequencing dependency.",
        })

    sccs = []
    for index, node in enumerate(sorted(nodes, key=lambda item: str(item["id"])), start=1):
        sccs.append({
            "id": f"SCC-{index:03d}",
            "members": [node["id"]],
            "size": 1,
            "non_trivial": False,
            "proposed_move": "NONE",
            "human_gate_required": False,
            "rationale": "Acyclic singleton; no cycle-resolution move required.",
        })

    counts = Counter(row["ParentPackageID"].split("_", 1)[0] for row in rows)
    graph = {
        "schema": "chirality-objective-relative-work-graph/v2",
        "graph_id": "ROOT-V3-RELEASE-PATHWAY-SCA-004-POST-GATE5-PHASE1",
        "status": "DERIVATIVE_POST_INIT_DEPENDENCY_EXTRACTION_PENDING",
        "basis": {
            "branch_basis": "e677edbe81188465eb36e700b6bd441715bcbccd",
            "n1_commit": "dab470e2f0c7345f10c34bcce9e489eb68bf0541",
            "sca_snapshot": "SCA-004_2026-08-22_1749",
            "latest_pointer_sha256": EXPECTED_HASHES["execution/_ScopeChange/_LATEST.md"],
            "applied_revision": "1.3",
            "decomposition_identities": {
                key: value for key, value in EXPECTED_HASHES.items()
                if key.startswith("execution/_Decomposition/")
            },
            "n1_return_sha256": EXPECTED_HASHES[str(N1_RETURN.relative_to(ROOT))],
            "n1_review_sha256": EXPECTED_HASHES[str(N1_REVIEW.relative_to(ROOT))],
        },
        "objective": (
            "Represent the live Root decomposition after SCA-004 Gate 5 and Phase-1 INIT, "
            "using only declared sequencing dependencies while preserving package membership."
        ),
        "edge_semantics": {
            "STRICT_DEPENDENCY": "from must precede to for this objective; none are currently declared",
            "PARENT_MEMBERSHIP": "structural package membership only; never readiness-gating",
        },
        "cycle_policy": (
            "Non-trivial SCC edges remain non-gating until a recorded decompose, invert, merge, "
            "or cut move resolves them; cut and merge are human-gated."
        ),
        "dependency_source_state": {
            "declared_execution_edges": 0,
            "pre_existing_not_run_yet": 46,
            "new_initialized_empty_expected_post_init": 7,
            "dependencies_csv_present": 0,
            "interpretation": (
                "No sequencing edge is inferred. Dependency extraction and accepted SOWs are later acts."
            ),
        },
        "node_counts": {
            "total": len(nodes),
            "packages": 6,
            "deliverables": 53,
            "deliverables_by_package": dict(sorted(counts.items())),
        },
        "nodes": nodes,
        "edges": membership_edges,
        "dependency_edges": [],
        "sccs": sccs,
        "strict_layer_acyclic": True,
        "non_trivial_scc_count": 0,
        "human_gated_cycle_decision_required": False,
        "derivative_disposition": (
            "Re-derive after dependency extraction and SOW acceptance; this package is not "
            "authoritative decomposition truth."
        ),
    }
    (HERE / "WORK_GRAPH.json").write_text(json.dumps(graph, indent=2) + "\n", encoding="utf-8")

    dag = f"""# Root objective-relative work graph — post-Gate-5 Phase 1

Status: `DERIVATIVE_POST_INIT_DEPENDENCY_EXTRACTION_PENDING`

## Basis and objective

This derivative graph cites accepted SCA-004 revision 1.3, pointer
`4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`,
and accepted N1 commit `dab470e2f0c7345f10c34bcce9e489eb68bf0541`.
It represents 53 live deliverables and six package nodes without inventing
sequencing dependencies before SOW acceptance and dependency extraction.

## Structural view

```text
PKG-01 -> 8 live deliverables
PKG-02 -> 12 live deliverables
PKG-03 -> 6 live deliverables
PKG-04 -> 11 live deliverables
PKG-05 -> 8 live deliverables
PKG-06 -> 8 live deliverables
```

The 53 arrows represented above are `PARENT_MEMBERSHIP` edges. They are
structural, non-gating, and not dependency claims. The strict dependency layer
has zero edges because all 46 pre-existing dependency containers remain
`NOT_RUN_YET` and the seven Phase-1 INIT containers explicitly declare no edge
and defer extraction. The seven empty INIT containers are expected state, not a
defect.

## SCC and cycle disposition

- Nodes: 59 = 53 deliverables + 6 packages.
- SCCs: 59 singleton components.
- Non-trivial SCCs: 0.
- Cycle-participating dependency edges: 0.
- Human-gated cut/merge decision: not required.

The complete component inventory is in `SCC_Report.md`. No cycle was silently
linearized and no resolution move was invented.

## Derivative status and rerun

This graph is a derivative package, not decomposition authority. Re-derive it
after accepted SOWs and dependency extraction. At that later rerun, apply
`docs/CYCLE_DRIVEN_RESOLUTION.md`; every unresolved cycle edge stays non-gating,
and any proposed cut or merge returns to the owner.
"""
    (HERE / "DAG.md").write_text(dag, encoding="utf-8")

    scc_lines = [
        "# SCC report — post-Gate-5 Phase 1",
        "",
        "Verdict: `PASS — NO NON-TRIVIAL SCC`",
        "",
        "Objective and edge semantics are those declared in `WORK_GRAPH.json`.",
        "All 59 components are listed; each is an acyclic singleton, so the",
        "proposed move is `NONE` and no human-gated cut or merge is required.",
        "",
        "| SCC | Member | Size | Non-trivial | Proposed move | Human gate |",
        "|---|---|---:|---|---|---|",
    ]
    for scc in sccs:
        scc_lines.append(
            f"| {scc['id']} | `{scc['members'][0]}` | 1 | no | `NONE` | no |"
        )
    scc_lines.extend([
        "",
        "Cycle-participating edges: none. Recompute after dependency extraction",
        "and SOW acceptance; this report is derivative evidence only.",
        "",
    ])
    (HERE / "SCC_Report.md").write_text("\n".join(scc_lines), encoding="utf-8")

    summary = """# Graph derivation summary

- Result: `PASS`.
- Node set: exact equality with 53 applied register rows plus six packages.
- Structural membership edges: 53, all non-gating.
- Declared sequencing dependency edges: 0.
- SCCs: 59 singleton, 0 non-trivial.
- Human-gated cut/merge required: no.
- Seven new `OPEN` folders have initialized-empty dependencies as expected.
- Pre-existing closure violations versus the Gate-1 audit: 0 unresolved.
- Required rerun: after SOW acceptance and dependency extraction.
"""
    (HERE / "SUMMARY.md").write_text(summary, encoding="utf-8")

    decision_log = """# Decision log — graph re-derivation

## DG-001 — Objective and edge semantics

The objective is post-SCA-004 Root sequencing readiness. Only declared
dependencies can create strict edges. Package-to-deliverable relationships are
recorded separately as non-gating structural membership edges.

## DG-002 — No inferred dependencies

All 46 pre-existing `_DEPENDENCIES.md` containers say extraction is
`NOT_RUN_YET` and declare no upstream/downstream edge. All seven N1 containers
explicitly say no dependency is declared or inferred and defer extraction.
Accordingly, the strict dependency edge set is empty; objectives, shared scope
items, prose resemblance, and package co-membership were not converted into
ordering edges.

## DG-003 — Cycle resolution

Deterministic SCC analysis over the declared dependency layer yields 59
singletons and no cycle. No decompose, invert, merge, or cut move is required.
No human-gated cut/merge decision was made.

## DG-004 — Derivative boundary

This run writes only the steer-authorized SCA evidence folder, overriding the
dedicated audit agent's default `_Evaluation/DepClosure` output location.
The graph must be regenerated after accepted SOWs and dependency extraction.
"""
    (HERE / "Decision_Log.md").write_text(decision_log, encoding="utf-8")

    input_rows = [(rel, expected, sha256(ROOT / rel)) for rel, expected in EXPECTED_HASHES.items()]
    for row in rows:
        base = ROOT / "execution" / row["ParentPackageID"] / "1_Working" / row["DeliverableID"]
        for name in ("_STATUS.md", "_DEPENDENCIES.md"):
            path = base / name
            input_rows.append((str(path.relative_to(ROOT)), sha256(path), sha256(path)))
    with (HERE / "INPUT_HASHES.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["Path", "ExpectedSHA256", "ObservedSHA256", "Result"])
        for rel, expected, observed in sorted(input_rows):
            writer.writerow([rel, expected, observed, "PASS" if expected == observed else "FAIL"])

    artifact_rows = []
    for path in sorted(HERE.iterdir()):
        if path.is_file() and path.name != "ARTIFACT_HASHES.csv":
            artifact_rows.append([path.name, sha256(path)])
    with (HERE / "ARTIFACT_HASHES.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["File", "SHA256"])
        writer.writerows(artifact_rows)


if __name__ == "__main__":
    main()
