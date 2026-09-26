#!/usr/bin/env python3
"""
Build the DEV-001 implementation-readiness blocker queue.

The queue interprets each active DAG edge as:

    FromDeliverableID consumes and is blocked by TargetDeliverableID.

Implementation blockers are satisfied only by explicit committed implementation
evidence, except for PKG-00 architecture-basis edges, which are satisfied by the
accepted architecture baseline.

That is the behaviour for its original inputs: a DAG directory or explicit
edge and node files (`--dag-dir`, `--edges`, `--nodes`, default
`execution/_DAG/DAG-001`), read as given.

With `--execution-root`, the tool instead computes blockers for a project
under docs/SPEC.md §5.3-§5.4 (D-GOV-49):

- When `{EXECUTION_ROOT}/_DAG/_LATEST.md` names an accepted project DAG, the
  edges come from that accepted version. Deliverables whose local evidence
  departs from it (an arc added or removed, or a deliverable added or
  removed) are `DAG_PENDING` and get no blocked or unblocked verdict.
  Candidate arcs held by the version are non-gating.
- Otherwise the edges come from each deliverable's recorded register: the
  union of its `_DEPENDENCIES.md` declarations and `Dependencies.csv` rows,
  one edge per arc, the declaration governing required maturity. Arcs in an
  unresolved cycle are held and non-gating. A deliverable whose tracking mode
  is `NOT_TRACKED` gets no verdict.

An arc is satisfied when the supplier's `_STATUS.md` state has reached the
arc's required maturity (`--default-maturity` when it is TBD), or, when
`--evidence` is given, by the DEV-001 committed-evidence rule above.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Iterable

import dependency_evidence as de


ACTIVE = "ACTIVE"
CANDIDATE = "CANDIDATE"
ARCHITECTURE_BASIS = "ARCHITECTURE_BASIS"
PKG_00 = "PKG-00"
COMMITTED = "COMMITTED"
ARCHITECTURE_BASELINE = "ARCHITECTURE_BASELINE"
MISSING_EVIDENCE = "MISSING_EVIDENCE"
BLOCKED = "BLOCKED"
UNBLOCKED = "UNBLOCKED"
DAG_PENDING = "DAG_PENDING"
NOT_TRACKED = "NOT_TRACKED"
RECORDED_REGISTER = "RECORDED_REGISTER"
LIFECYCLE_STATES = ("OPEN", "INITIALIZED", "SEMANTIC_READY", "IN_PROGRESS", "CHECKING", "ISSUED", "RETIRED")

QUEUE_COLUMNS = [
    "DeliverableID",
    "PackageID",
    "DeliverableName",
    "LifecycleState",
    "ImplementationEvidenceState",
    "EvidenceCommit",
    "ActiveUpstreamCount",
    "SatisfiedUpstreamCount",
    "BlockingUpstreamCount",
    "BlockerState",
    "BlockingUpstreamDeliverables",
    "BlockingEdgeIDs",
]

PROJECT_QUEUE_COLUMNS = QUEUE_COLUMNS + ["TrackingMode", "HeldEdgeIDs", "DagPendingReasons"]

EVIDENCE_COLUMNS = [
    "DeliverableID",
    "PackageID",
    "EvidenceState",
    "EvidenceKind",
    "Commit",
    "CommitSubject",
    "CommittedDate",
    "HandoffCommit",
    "Notes",
]

Row = dict[str, str]


def read_csv_rows(path: Path) -> tuple[list[str], list[Row]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def clean(value: object) -> str:
    return str(value or "").strip()


def read_nodes(nodes_path: Path) -> list[Row]:
    _header, rows = read_csv_rows(nodes_path)
    return [row for row in rows if clean(row.get("DeliverableID"))]


def read_edges(edges_path: Path) -> tuple[list[Row], int]:
    _header, rows = read_csv_rows(edges_path)
    active_rows = [
        row for row in rows
        if clean(row.get("Status")) == ACTIVE
        and clean(row.get("FromDeliverableID"))
        and clean(row.get("TargetDeliverableID"))
    ]
    candidate_count = sum(1 for row in rows if clean(row.get("Status")) == CANDIDATE)
    return active_rows, candidate_count


def read_evidence(evidence_path: Path) -> dict[str, Row]:
    _header, rows = read_csv_rows(evidence_path)
    evidence: dict[str, Row] = {}
    for row in rows:
        deliverable_id = clean(row.get("DeliverableID"))
        if deliverable_id:
            evidence[deliverable_id] = row
    return evidence


def filesystem_lifecycle_state(node: Row) -> str:
    execution_path = clean(node.get("ExecutionPath"))
    if execution_path:
        status_path = Path(execution_path) / "_STATUS.md"
        if status_path.exists():
            text = status_path.read_text(encoding="utf-8")
            for line in text.splitlines():
                if "Current State" in line:
                    for state in LIFECYCLE_STATES:
                        if state in line:
                            return state
    return clean(node.get("LifecycleState")) or "UNKNOWN"


def is_architecture_basis_satisfied(edge: Row) -> bool:
    # PKG-00 is the accepted architecture/context baseline. After TP-DAG-004,
    # refreshed local evidence may carry more specific dependency type labels
    # while still pointing at PKG-00 providers, so package identity is the
    # blocker-satisfaction boundary.
    return clean(edge.get("TargetPackageID")) == PKG_00


def committed_evidence(evidence: Row | None) -> bool:
    return clean((evidence or {}).get("EvidenceState")) == COMMITTED


def implementation_state(deliverable_id: str, package_id: str, evidence_by_id: dict[str, Row]) -> tuple[str, str]:
    evidence = evidence_by_id.get(deliverable_id)
    if committed_evidence(evidence):
        return COMMITTED, clean(evidence.get("Commit"))
    if package_id == PKG_00:
        return ARCHITECTURE_BASELINE, ""
    if evidence:
        return clean(evidence.get("EvidenceState")) or MISSING_EVIDENCE, clean(evidence.get("Commit"))
    return MISSING_EVIDENCE, ""


def provider_satisfaction(edge: Row, evidence_by_id: dict[str, Row]) -> tuple[bool, str]:
    if is_architecture_basis_satisfied(edge):
        return True, ARCHITECTURE_BASELINE

    provider_id = clean(edge.get("TargetDeliverableID"))
    evidence = evidence_by_id.get(provider_id)
    if committed_evidence(evidence):
        return True, COMMITTED
    if evidence:
        return False, clean(evidence.get("EvidenceState")) or MISSING_EVIDENCE
    return False, MISSING_EVIDENCE


def build_queue(edges_path: Path, nodes_path: Path, evidence_path: Path) -> dict[str, object]:
    nodes = read_nodes(nodes_path)
    active_edges, candidate_count = read_edges(edges_path)
    evidence_by_id = read_evidence(evidence_path)
    node_by_id = {clean(row.get("DeliverableID")): row for row in nodes}

    blockers_by_consumer: dict[str, list[Row]] = defaultdict(list)
    satisfied_counts: Counter[str] = Counter()
    upstream_counts: Counter[str] = Counter()
    architecture_basis_satisfied_edges = 0

    for edge in active_edges:
        consumer_id = clean(edge.get("FromDeliverableID"))
        upstream_counts[consumer_id] += 1
        satisfied, _reason = provider_satisfaction(edge, evidence_by_id)
        if satisfied:
            satisfied_counts[consumer_id] += 1
            if is_architecture_basis_satisfied(edge):
                architecture_basis_satisfied_edges += 1
        else:
            blockers_by_consumer[consumer_id].append(edge)

    queue_rows: list[Row] = []
    for node in nodes:
        deliverable_id = clean(node.get("DeliverableID"))
        package_id = clean(node.get("PackageID"))
        blocker_edges = blockers_by_consumer.get(deliverable_id, [])
        implementation_evidence_state, commit = implementation_state(deliverable_id, package_id, evidence_by_id)
        queue_rows.append({
            "DeliverableID": deliverable_id,
            "PackageID": package_id,
            "DeliverableName": clean(node.get("DeliverableName")),
            "LifecycleState": filesystem_lifecycle_state(node),
            "ImplementationEvidenceState": implementation_evidence_state,
            "EvidenceCommit": commit,
            "ActiveUpstreamCount": str(upstream_counts[deliverable_id]),
            "SatisfiedUpstreamCount": str(satisfied_counts[deliverable_id]),
            "BlockingUpstreamCount": str(len(blocker_edges)),
            "BlockerState": BLOCKED if blocker_edges else UNBLOCKED,
            "BlockingUpstreamDeliverables": ";".join(clean(edge.get("TargetDeliverableID")) for edge in blocker_edges),
            "BlockingEdgeIDs": ";".join(clean(edge.get("DependencyID")) for edge in blocker_edges),
        })

    row_by_id = {row["DeliverableID"]: row for row in queue_rows}

    missing_provider_groups: dict[str, dict[str, object]] = {}
    for consumer_id, blocker_edges in blockers_by_consumer.items():
        for edge in blocker_edges:
            provider_id = clean(edge.get("TargetDeliverableID"))
            provider_node = node_by_id.get(provider_id, {})
            provider_state, provider_commit = implementation_state(
                provider_id,
                clean(provider_node.get("PackageID") or edge.get("TargetPackageID")),
                evidence_by_id,
            )
            group = missing_provider_groups.setdefault(provider_id, {
                "ProviderDeliverableID": provider_id,
                "ProviderPackageID": clean(provider_node.get("PackageID") or edge.get("TargetPackageID")),
                "ProviderName": clean(provider_node.get("DeliverableName") or edge.get("TargetName")),
                "ProviderEvidenceState": provider_state,
                "ProviderEvidenceCommit": provider_commit,
                "Consumers": set(),
                "EdgeIDs": [],
            })
            group["Consumers"].add(consumer_id)
            group["EdgeIDs"].append(clean(edge.get("DependencyID")))

    missing_provider_rows: list[dict[str, object]] = []
    for provider_id in sorted(missing_provider_groups):
        group = missing_provider_groups[provider_id]
        consumers = sorted(str(item) for item in group["Consumers"])
        group["Consumers"] = consumers
        group["EdgeIDs"] = sorted(str(item) for item in group["EdgeIDs"])
        group["BlockedConsumerCount"] = len(consumers)
        missing_provider_rows.append(group)

    package_summary: dict[str, dict[str, int]] = {}
    for row in queue_rows:
        package = row["PackageID"]
        package_summary.setdefault(package, {UNBLOCKED: 0, BLOCKED: 0})
        package_summary[package][row["BlockerState"]] += 1

    evidence_state_counts = Counter(clean(row.get("EvidenceState")) or "BLANK" for row in evidence_by_id.values())
    lifecycle_state_counts = Counter(row["LifecycleState"] for row in queue_rows)

    return {
        "edges_path": str(edges_path),
        "nodes_path": str(nodes_path),
        "evidence_path": str(evidence_path),
        "package_count": len({clean(row.get("PackageID")) for row in nodes if clean(row.get("PackageID"))}),
        "node_count": len(nodes),
        "active_edge_count": len(active_edges),
        "candidate_edge_count": candidate_count,
        "evidence_record_count": len(evidence_by_id),
        "evidence_state_counts": dict(sorted(evidence_state_counts.items())),
        "lifecycle_state_counts": dict(sorted(lifecycle_state_counts.items())),
        "committed_evidence_count": sum(1 for row in evidence_by_id.values() if committed_evidence(row)),
        "architecture_basis_satisfied_edges": architecture_basis_satisfied_edges,
        "unblocked_count": sum(1 for row in queue_rows if row["BlockerState"] == UNBLOCKED),
        "blocked_count": sum(1 for row in queue_rows if row["BlockerState"] == BLOCKED),
        "package_summary": package_summary,
        "queue_rows": queue_rows,
        "queue_rows_by_id": row_by_id,
        "missing_provider_rows": missing_provider_rows,
    }


# --- Project mode (docs/SPEC.md §5.3-§5.4) ------------------------------------


def unit_package(unit: Path | None) -> str:
    return unit.parent.parent.name.split("_")[0] if unit is not None else ""


def unit_name(unit: Path | None) -> str:
    return unit.name.partition("_")[2].replace("_", " ") if unit is not None else ""


def held_arcs(arcs: set[tuple[str, str]]) -> set[tuple[str, str]]:
    """Arcs inside a non-trivial strongly connected component, and self-loops."""
    graph: dict[str, set[str]] = defaultdict(set)
    for consumer, supplier in arcs:
        graph[consumer].add(supplier)
    nodes = set(graph) | {supplier for _consumer, supplier in arcs}
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    component: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    counter = 0
    for origin in sorted(nodes):
        if origin in index:
            continue
        work = [(origin, iter(sorted(graph.get(origin, ()))))]
        index[origin] = low[origin] = counter
        counter += 1
        stack.append(origin)
        on_stack.add(origin)
        while work:
            node, children = work[-1]
            child = next(children, None)
            if child is None:
                work.pop()
                if work:
                    parent = work[-1][0]
                    low[parent] = min(low[parent], low[node])
                if low[node] == index[node]:
                    while True:
                        member = stack.pop()
                        on_stack.discard(member)
                        component[member] = index[node]
                        if member == node:
                            break
            elif child not in index:
                index[child] = low[child] = counter
                counter += 1
                stack.append(child)
                on_stack.add(child)
                work.append((child, iter(sorted(graph.get(child, ())))))
            elif child in on_stack:
                low[node] = min(low[node], index[child])
    return {(consumer, supplier) for consumer, supplier in arcs if component[consumer] == component[supplier]}


def arc_rows(rows: Iterable[Row]) -> dict[tuple[str, str], list[Row]]:
    grouped: dict[tuple[str, str], list[Row]] = defaultdict(list)
    for row in rows:
        if clean(row.get("Status")) != ACTIVE:
            continue
        item = de.arc(row)
        if item:
            grouped[item].append(row)
    return grouped


def required_maturity(rows: list[Row], default: str) -> str:
    stated = [de.maturity_value(row.get("RequiredMaturity", "")) for row in rows]
    stated = [value for value in stated if value != "TBD"]
    if not stated:
        return default
    return max(stated, key=de.LIFECYCLE_ORDER.index)


def build_project_queue(
    execution_root: Path,
    evidence_path: Path | None = None,
    default_maturity: str = "INITIALIZED",
) -> dict[str, object]:
    """Blockers for a project: the accepted current DAG version, or the recorded registers."""
    registers = de.project_registers(execution_root)
    dag = de.resolve_accepted_dag(execution_root)
    evidence_by_id = read_evidence(evidence_path) if evidence_path is not None else None

    pending: dict[str, list[str]] = {}
    currency: dict[str, object] | None = None
    nodes: dict[str, Row] = {}
    if dag is not None:
        source = f"ACCEPTED_DAG:{dag.name}"
        gating = arc_rows(dag.admitted)
        held = set(arc_rows(dag.candidates))
        result = de.check_currency(dag, registers)
        pending = result.pending
        currency = result.as_dict()
        for row in dag.nodes:
            key = de.normalize_id(row.get("DeliverableID", ""))
            if key:
                nodes[key] = row
    else:
        source = RECORDED_REGISTER
        grouped = arc_rows(row for register in registers.values() for row in register.union_rows)
        held = held_arcs(set(grouped))
        gating = {item: rows for item, rows in grouped.items() if item not in held}
    for key in registers:
        nodes.setdefault(key, {})

    blockers: dict[str, list[tuple[tuple[str, str], list[Row]]]] = defaultdict(list)
    upstream_counts: Counter[str] = Counter()
    satisfied_counts: Counter[str] = Counter()
    held_by_consumer: dict[str, list[str]] = defaultdict(list)
    for consumer, supplier in held:
        held_by_consumer[consumer].append(supplier)
    for (consumer, supplier), rows in sorted(gating.items()):
        upstream_counts[consumer] += 1
        if evidence_by_id is not None:
            satisfied, _reason = provider_satisfaction(rows[0], evidence_by_id)
        else:
            supplier_unit = registers[supplier].path if supplier in registers else None
            satisfied = de.maturity_reached(de.lifecycle_state(supplier_unit), required_maturity(rows, default_maturity))
        if satisfied:
            satisfied_counts[consumer] += 1
        else:
            blockers[consumer].append(((consumer, supplier), rows))

    queue_rows: list[Row] = []
    for deliverable_id in sorted(nodes):
        node = nodes[deliverable_id]
        register = registers.get(deliverable_id)
        unit = register.path if register else None
        package_id = clean(node.get("PackageID")) or unit_package(unit)
        mode = register.mode if register else "UNKNOWN"
        blocking = blockers.get(deliverable_id, [])
        if deliverable_id in pending:
            state = DAG_PENDING
        elif dag is None and mode == NOT_TRACKED:
            state = NOT_TRACKED
        else:
            state = BLOCKED if blocking else UNBLOCKED
        verdict = state in {BLOCKED, UNBLOCKED}
        implementation, commit = (
            implementation_state(deliverable_id, package_id, evidence_by_id) if evidence_by_id is not None else ("", "")
        )
        queue_rows.append({
            "DeliverableID": deliverable_id,
            "PackageID": package_id,
            "DeliverableName": clean(node.get("DeliverableName")) or unit_name(unit),
            "LifecycleState": de.lifecycle_state(unit),
            "ImplementationEvidenceState": implementation,
            "EvidenceCommit": commit,
            "ActiveUpstreamCount": str(upstream_counts[deliverable_id]),
            "SatisfiedUpstreamCount": str(satisfied_counts[deliverable_id]),
            "BlockingUpstreamCount": str(len(blocking)) if verdict else "",
            "BlockerState": state,
            "BlockingUpstreamDeliverables": ";".join(item[1] for item, _rows in blocking) if verdict else "",
            "BlockingEdgeIDs": ";".join(
                clean(row.get("DependencyID")) for _item, rows in blocking for row in rows
            ) if verdict else "",
            "TrackingMode": mode,
            "HeldEdgeIDs": ";".join(f"{deliverable_id}->{supplier}" for supplier in sorted(held_by_consumer.get(deliverable_id, []))),
            "DagPendingReasons": "; ".join(pending.get(deliverable_id, [])),
        })

    states = Counter(row["BlockerState"] for row in queue_rows)
    return {
        "mode": "PROJECT",
        "execution_root": str(execution_root),
        "blocker_source": source,
        "accepted_dag": None if dag is None else {"version": dag.name, "path": str(dag.path), "pointer": str(dag.pointer)},
        "currency": currency,
        "satisfaction_rule": "DEV001_COMMITTED_EVIDENCE" if evidence_by_id is not None else f"STATUS_MATURITY(default={default_maturity})",
        "evidence_path": str(evidence_path) if evidence_path is not None else "",
        "node_count": len(queue_rows),
        "gating_arc_count": len(gating),
        "held_arc_count": len(held),
        "declared_only_count": sum(len(register.declared_only) for register in registers.values()),
        "declared_disagreements": [item for register in registers.values() for item in register.disagreements],
        "unblocked_count": states.get(UNBLOCKED, 0),
        "blocked_count": states.get(BLOCKED, 0),
        "dag_pending_count": states.get(DAG_PENDING, 0),
        "not_tracked_count": states.get(NOT_TRACKED, 0),
        "queue_rows": queue_rows,
        "queue_rows_by_id": {row["DeliverableID"]: row for row in queue_rows},
    }


def render_project_markdown(summary: dict[str, object], generated_date: str) -> str:
    queue_rows: list[Row] = summary["queue_rows"]  # type: ignore[assignment]
    source = str(summary["blocker_source"])
    lines = [
        "# Dependency Blocker Queue",
        "",
        f"Generated {generated_date} by `tools/coordination/build_dev001_blocker_queue.py --execution-root`. "
        "An advisory view computed from the files; it is not a schedule, a work assignment or an acceptance.",
        "",
        "## Computation Rule",
        "",
    ]
    if source == RECORDED_REGISTER:
        lines += [
            "- No accepted project DAG: edges come from each deliverable's recorded register, the union of the "
            "`_DEPENDENCIES.md` declarations and `Dependencies.csv` rows (`docs/SPEC.md` §5.3). A declaration and a row "
            "for the same direction and target are one edge; the declaration governs required maturity.",
            "- Arcs in an unresolved cycle are held and non-gating. `NOT_TRACKED` deliverables get no verdict.",
        ]
    else:
        lines += [
            f"- Accepted project DAG: edges come from `{source.split(':', 1)[1]}`, the version `_DAG/_LATEST.md` names "
            "(`docs/SPEC.md` §5.4). Candidate arcs are held and non-gating.",
            "- `DAG_PENDING`: the deliverable's local evidence departs from the accepted version (an arc or deliverable "
            "added or removed). No verdict is given until the human accepts a new version or rejects the change. "
            "The `project-dag` currency audit governs where it differs from this check.",
        ]
    lines += [
        f"- Satisfaction: {summary['satisfaction_rule']}.",
        "",
        "## Summary",
        "",
        "| State | Count |",
        "|---|---:|",
        markdown_row(["UNBLOCKED", summary["unblocked_count"]]),
        markdown_row(["BLOCKED", summary["blocked_count"]]),
        markdown_row(["DAG_PENDING", summary["dag_pending_count"]]),
        markdown_row(["NOT_TRACKED", summary["not_tracked_count"]]),
        markdown_row(["Held arcs", summary["held_arc_count"]]),
        markdown_row(["Declaration/CSV disagreements", len(summary["declared_disagreements"])]),  # type: ignore[arg-type]
        "",
        "## Queue",
        "",
        "| DeliverableID | State | Lifecycle | Blocking upstream | Held | DAG pending reasons |",
        "|---|---|---|---|---|---|",
    ]
    for row in queue_rows:
        lines.append(markdown_row([
            f"`{row['DeliverableID']}`",
            row["BlockerState"],
            row["LifecycleState"],
            row["BlockingUpstreamDeliverables"],
            row["HeldEdgeIDs"],
            row["DagPendingReasons"],
        ]))
    lines.append("")
    return "\n".join(lines)


def markdown_cell(value: object) -> str:
    text = str(value)
    return text.replace("|", "\\|").replace("\n", "<br>")


def markdown_row(values: Iterable[object]) -> str:
    return "| " + " | ".join(markdown_cell(value) for value in values) + " |"


def render_markdown(summary: dict[str, object], generated_date: str) -> str:
    queue_rows: list[Row] = summary["queue_rows"]  # type: ignore[assignment]
    package_summary: dict[str, dict[str, int]] = summary["package_summary"]  # type: ignore[assignment]
    missing_provider_rows: list[dict[str, object]] = summary["missing_provider_rows"]  # type: ignore[assignment]

    unblocked_rows = [row for row in queue_rows if row["BlockerState"] == UNBLOCKED]
    blocked_rows = [row for row in queue_rows if row["BlockerState"] == BLOCKED]
    source_graph = str(summary["edges_path"])
    evidence_source = str(summary["evidence_path"])

    lines = [
        "---",
        "doc_id: DEV-001-BLOCKER-QUEUE",
        "doc_kind: coordination.blocker_queue",
        "status: computed_active_edges_only",
        "created: 2026-04-30",
        f"updated: {generated_date}",
        f"source_graph: {source_graph}",
        f"implementation_evidence_source: {evidence_source}",
        "implementation_threshold: COMMITTED",
        "architecture_basis: satisfied_by_existing_baseline",
        "candidate_edges: excluded",
        "---",
        "",
        "# DEV-001 Implementation-Readiness Blocker Queue",
        "",
        "This blocker queue is an advisory implementation-readiness view only. It is not a schedule, staffing plan, priority list, lifecycle approval, professional approval, or readiness-for-reliance claim.",
        "",
        "## Computation Rule",
        "",
        f"- Source graph: `{source_graph}`.",
        "- Included edges: `Status=ACTIVE` only.",
        "- Excluded edges: all `Status=CANDIDATE` rows.",
        "- Direction convention: `FromDeliverableID` is the downstream consumer and is blocked by `TargetDeliverableID`, the upstream provider.",
        f"- Satisfaction threshold: upstream provider has `COMMITTED` evidence in `{evidence_source}`.",
        "- `SEMANTIC_READY` remains decomposition/context readiness evidence; it does not satisfy implementation blockers by itself.",
        "- `PKG-00` provider edges are satisfied by the accepted architecture baseline, not by implementation evidence.",
        "- `UNBLOCKED` means all active upstream implementation dependencies satisfy the threshold or are satisfied architecture-basis edges.",
        "- `BLOCKED` means one or more active upstream providers lack committed implementation evidence.",
        "",
        "## Evidence Summary",
        "",
        "| Evidence | Count |",
        "|---|---:|",
        markdown_row(["Packages represented", summary["package_count"]]),
        markdown_row(["Deliverable nodes represented", summary["node_count"]]),
        markdown_row(["Active edges included", summary["active_edge_count"]]),
        markdown_row(["Candidate edges excluded", summary["candidate_edge_count"]]),
        markdown_row(["Implementation evidence records", summary["evidence_record_count"]]),
        markdown_row(["Committed implementation evidence", summary["committed_evidence_count"]]),
        markdown_row(["Filesystem lifecycle `SEMANTIC_READY` (display only)", summary["lifecycle_state_counts"].get("SEMANTIC_READY", 0)]),  # type: ignore[index]
        markdown_row(["PKG-00 architecture-basis edges satisfied", summary["architecture_basis_satisfied_edges"]]),
        markdown_row(["Implementation `UNBLOCKED` deliverables", summary["unblocked_count"]]),
        markdown_row(["Implementation `BLOCKED` deliverables", summary["blocked_count"]]),
        "",
        "## Package Summary",
        "",
        "| PackageID | UNBLOCKED | BLOCKED |",
        "|---|---:|---:|",
    ]

    for package in sorted(package_summary):
        counts = package_summary[package]
        lines.append(markdown_row([f"`{package}`", counts.get(UNBLOCKED, 0), counts.get(BLOCKED, 0)]))

    lines += [
        "",
        "## Unblocked DAG-Ready Items",
        "",
        "These deliverables have no active upstream implementation dependency below the `COMMITTED` threshold. Items without their own committed evidence are DAG-ready candidates, not completed work.",
        "",
        "| DeliverableID | PackageID | Implementation evidence | Active upstream | Name |",
        "|---|---|---|---:|---|",
    ]

    for row in unblocked_rows:
        state = row["ImplementationEvidenceState"]
        evidence = f"`{state}`"
        if row["EvidenceCommit"]:
            evidence = f"`{state}` `{row['EvidenceCommit']}`"
        lines.append(markdown_row([
            f"`{row['DeliverableID']}`",
            f"`{row['PackageID']}`",
            evidence,
            row["ActiveUpstreamCount"],
            row["DeliverableName"],
        ]))

    lines += [
        "",
        "## Blocked Items Grouped By Missing Upstream",
        "",
    ]

    if missing_provider_rows:
        lines += [
            "| Missing upstream | PackageID | Evidence state | Blocked consumers | Consumer IDs | Edge IDs |",
            "|---|---|---|---:|---|---|",
        ]
        for group in missing_provider_rows:
            consumers = "; ".join(f"`{consumer}`" for consumer in group["Consumers"])  # type: ignore[index]
            edge_ids = "; ".join(f"`{edge_id}`" for edge_id in group["EdgeIDs"])  # type: ignore[index]
            lines.append(markdown_row([
                f"`{group['ProviderDeliverableID']}` - {group['ProviderName']}",
                f"`{group['ProviderPackageID']}`",
                f"`{group['ProviderEvidenceState']}`",
                group["BlockedConsumerCount"],
                consumers,
                edge_ids,
            ]))
    else:
        lines.append("No blocked items were found under the implementation-readiness threshold.")

    lines += [
        "",
        "## Per-Deliverable Blocked Items",
        "",
    ]

    if blocked_rows:
        lines += [
            "| DeliverableID | PackageID | Missing upstream count | Missing upstream deliverables | Name |",
            "|---|---|---:|---|---|",
        ]
        for row in blocked_rows:
            missing = "; ".join(f"`{item}`" for item in row["BlockingUpstreamDeliverables"].split(";") if item)
            lines.append(markdown_row([
                f"`{row['DeliverableID']}`",
                f"`{row['PackageID']}`",
                row["BlockingUpstreamCount"],
                missing,
                row["DeliverableName"],
            ]))
    else:
        lines.append("No per-deliverable implementation blockers were found.")

    lines += [
        "",
        "## Candidate Edges Excluded",
        "",
        "Candidate edges remain non-gating pending later `RECONCILIATION` and `CHANGE`; they were not used in the blocker state calculation.",
        "",
        "## Machine-Readable Queue",
        "",
        "Full per-deliverable queue rows are recorded in `execution/_Coordination/DEV-001_BLOCKER_QUEUE.csv`.",
        "",
    ]

    return "\n".join(lines)


def write_queue_csv(path: Path, rows: list[Row], columns: list[str] = QUEUE_COLUMNS) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the DEV-001 implementation-readiness blocker queue.")
    parser.add_argument(
        "--dag-dir",
        type=Path,
        help="Directory containing DependencyEdges.csv and DeliverableNodes.csv (default execution/_DAG/DAG-001).",
    )
    parser.add_argument("--edges", type=Path, help="Override path to DependencyEdges.csv.")
    parser.add_argument("--nodes", type=Path, help="Override path to DeliverableNodes.csv.")
    parser.add_argument(
        "--evidence",
        type=Path,
        help=(
            "DEV-001 implementation evidence register (default execution/_Coordination/DEV-001_IMPLEMENTATION_EVIDENCE.csv; "
            "with --execution-root, only when given)."
        ),
    )
    parser.add_argument(
        "--csv-out",
        type=Path,
        help="Machine-readable blocker queue output (default execution/_Coordination/DEV-001_BLOCKER_QUEUE.csv).",
    )
    parser.add_argument(
        "--markdown-out",
        type=Path,
        help="Markdown blocker queue output (default execution/_Coordination/DEV-001_BLOCKER_QUEUE.md).",
    )
    parser.add_argument(
        "--execution-root",
        type=Path,
        help=(
            "Project mode (docs/SPEC.md §5.3-§5.4): blockers from the accepted DAG named by _DAG/_LATEST.md, with "
            "DAG_PENDING deliverables, or else from the recorded registers. Excludes --dag-dir, --edges and --nodes; "
            "outputs are written only where given."
        ),
    )
    parser.add_argument(
        "--default-maturity",
        choices=de.LIFECYCLE_ORDER,
        default="INITIALIZED",
        help="Project mode: required maturity for an arc whose maturity is TBD (project-setup Phase 1.3 default).",
    )
    parser.add_argument("--json-out", type=Path, help="Project mode: summary JSON output.")
    parser.add_argument("--generated-date", default=date.today().isoformat())
    args = parser.parse_args(argv)
    if args.execution_root is not None and (args.dag_dir or args.edges or args.nodes):
        parser.error("--execution-root cannot be combined with --dag-dir, --edges or --nodes")
    if args.execution_root is None and (args.default_maturity != "INITIALIZED" or args.json_out):
        parser.error("--default-maturity and --json-out apply only with --execution-root")
    return args


def main_project(args: argparse.Namespace) -> int:
    try:
        summary = build_project_queue(args.execution_root, args.evidence, args.default_maturity)
    except (OSError, ValueError) as exc:
        print(f"blocker queue: {exc}", file=sys.stderr)
        return 2
    if args.csv_out:
        write_queue_csv(args.csv_out, summary["queue_rows"], PROJECT_QUEUE_COLUMNS)  # type: ignore[arg-type]
    if args.markdown_out:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(render_project_markdown(summary, args.generated_date), encoding="utf-8")
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        payload = {key: value for key, value in summary.items() if key != "queue_rows_by_id"}
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        f"Blocker queue ({summary['blocker_source']}): "
        f"unblocked={summary['unblocked_count']} blocked={summary['blocked_count']} "
        f"dag_pending={summary['dag_pending_count']} not_tracked={summary['not_tracked_count']} "
        f"held_arcs={summary['held_arc_count']}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.execution_root is not None:
        return main_project(args)
    dag_dir = args.dag_dir or Path("execution/_DAG/DAG-001")
    evidence_path = args.evidence or Path("execution/_Coordination/DEV-001_IMPLEMENTATION_EVIDENCE.csv")
    args.csv_out = args.csv_out or Path("execution/_Coordination/DEV-001_BLOCKER_QUEUE.csv")
    args.markdown_out = args.markdown_out or Path("execution/_Coordination/DEV-001_BLOCKER_QUEUE.md")
    edges_path = args.edges or dag_dir / "DependencyEdges.csv"
    nodes_path = args.nodes or dag_dir / "DeliverableNodes.csv"
    summary = build_queue(edges_path=edges_path, nodes_path=nodes_path, evidence_path=evidence_path)

    write_queue_csv(args.csv_out, summary["queue_rows"])  # type: ignore[arg-type]
    args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_out.write_text(render_markdown(summary, args.generated_date), encoding="utf-8")

    print(
        "DEV-001 implementation blocker queue: "
        f"unblocked={summary['unblocked_count']} "
        f"blocked={summary['blocked_count']} "
        f"active_edges={summary['active_edge_count']} "
        f"candidate_edges_excluded={summary['candidate_edge_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
