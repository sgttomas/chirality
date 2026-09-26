from __future__ import annotations

import csv
from pathlib import Path


from audit_dag import ARCHITECTURE_BASIS, REQUIRED_COLUMNS  # noqa: E402
from build_dev001_blocker_queue import (  # noqa: E402
    ACTIVE,
    BLOCKED,
    CANDIDATE,
    COMMITTED,
    UNBLOCKED,
    build_queue,
)


NODE_COLUMNS = ["NodeID", "PackageID", "DeliverableID", "DeliverableName", "LifecycleState"]
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


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def node(deliverable_id: str, package_id: str = "PKG-01", name: str | None = None) -> dict[str, str]:
    return {
        "NodeID": deliverable_id,
        "PackageID": package_id,
        "DeliverableID": deliverable_id,
        "DeliverableName": name or f"{deliverable_id} name",
        "LifecycleState": "SEMANTIC_READY",
    }


def edge(
    dependency_id: str,
    from_deliverable: str,
    target_deliverable: str,
    from_package: str = "PKG-01",
    target_package: str = "PKG-01",
    status: str = ACTIVE,
    dependency_type: str = "DOMAIN_MODEL",
) -> dict[str, str]:
    row = {column: "" for column in REQUIRED_COLUMNS}
    row.update({
        "RegisterSchemaVersion": "v3.1",
        "DependencyID": dependency_id,
        "FromPackageID": from_package,
        "FromDeliverableID": from_deliverable,
        "FromDeliverableName": f"{from_deliverable} name",
        "DependencyClass": "EXECUTION",
        "AnchorType": "DELIVERABLE",
        "Direction": "UPSTREAM",
        "DependencyType": dependency_type,
        "TargetType": "DELIVERABLE",
        "TargetPackageID": target_package,
        "TargetDeliverableID": target_deliverable,
        "TargetRefID": target_deliverable,
        "TargetName": f"{target_deliverable} name",
        "Statement": f"{from_deliverable} depends on {target_deliverable}",
        "EvidenceFile": "_CONTEXT.md",
        "SourceRef": "fixture",
        "EvidenceQuote": "fixture evidence",
        "Explicitness": "EXPLICIT",
        "RequiredMaturity": "SEMANTIC_READY",
        "ProposedMaturity": "SEMANTIC_READY",
        "SatisfactionStatus": "UNKNOWN",
        "Confidence": "HIGH",
        "Origin": "TEST",
        "FirstSeen": "2026-05-01",
        "LastSeen": "2026-05-01",
        "Status": status,
        "Notes": "fixture",
    })
    return row


def evidence(deliverable_id: str, state: str = COMMITTED, package_id: str = "PKG-01") -> dict[str, str]:
    return {
        "DeliverableID": deliverable_id,
        "PackageID": package_id,
        "EvidenceState": state,
        "EvidenceKind": "FIXTURE",
        "Commit": "abc1234",
        "CommitSubject": "fixture commit",
        "CommittedDate": "2026-05-01",
        "HandoffCommit": "",
        "Notes": "fixture",
    }


def build_fixture(
    tmp_path: Path,
    nodes: list[dict[str, str]],
    edges: list[dict[str, str]],
    evidence_rows: list[dict[str, str]] | None = None,
) -> dict[str, object]:
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    evidence_path = tmp_path / "DEV-001_IMPLEMENTATION_EVIDENCE.csv"
    write_csv(nodes_path, nodes, NODE_COLUMNS)
    write_csv(edges_path, edges, REQUIRED_COLUMNS)
    write_csv(evidence_path, evidence_rows or [], EVIDENCE_COLUMNS)
    return build_queue(edges_path=edges_path, nodes_path=nodes_path, evidence_path=evidence_path)


def test_from_deliverable_is_blocked_by_missing_target_evidence(tmp_path: Path) -> None:
    summary = build_fixture(
        tmp_path,
        [node("DEL-A"), node("DEL-B")],
        [edge("DAG-TEST-E0001", "DEL-A", "DEL-B")],
    )

    row = summary["queue_rows_by_id"]["DEL-A"]  # type: ignore[index]
    assert row["BlockerState"] == BLOCKED
    assert row["BlockingUpstreamDeliverables"] == "DEL-B"
    assert row["BlockingEdgeIDs"] == "DAG-TEST-E0001"


def test_committed_upstream_evidence_unblocks_downstream_item(tmp_path: Path) -> None:
    summary = build_fixture(
        tmp_path,
        [node("DEL-A"), node("DEL-B")],
        [edge("DAG-TEST-E0001", "DEL-A", "DEL-B")],
        [evidence("DEL-B")],
    )

    row = summary["queue_rows_by_id"]["DEL-A"]  # type: ignore[index]
    assert row["BlockerState"] == UNBLOCKED
    assert row["SatisfiedUpstreamCount"] == "1"
    assert row["BlockingUpstreamCount"] == "0"


def test_candidate_edges_are_ignored_for_blocker_computation(tmp_path: Path) -> None:
    summary = build_fixture(
        tmp_path,
        [node("DEL-A"), node("DEL-B")],
        [edge("DAG-TEST-E0001", "DEL-A", "DEL-B", status=CANDIDATE)],
    )

    row = summary["queue_rows_by_id"]["DEL-A"]  # type: ignore[index]
    assert row["BlockerState"] == UNBLOCKED
    assert row["ActiveUpstreamCount"] == "0"
    assert summary["candidate_edge_count"] == 1


def test_pkg00_architecture_basis_edges_are_satisfied_without_implementation_evidence(tmp_path: Path) -> None:
    summary = build_fixture(
        tmp_path,
        [node("DEL-A"), node("DEL-00-01", package_id="PKG-00")],
        [
            edge(
                "DAG-TEST-E0001",
                "DEL-A",
                "DEL-00-01",
                target_package="PKG-00",
                dependency_type=ARCHITECTURE_BASIS,
            )
        ],
    )

    row = summary["queue_rows_by_id"]["DEL-A"]  # type: ignore[index]
    assert row["BlockerState"] == UNBLOCKED
    assert row["SatisfiedUpstreamCount"] == "1"
    assert summary["architecture_basis_satisfied_edges"] == 1


def test_semantic_only_upstreams_do_not_satisfy_implementation_dependencies(tmp_path: Path) -> None:
    summary = build_fixture(
        tmp_path,
        [node("DEL-A"), node("DEL-B")],
        [edge("DAG-TEST-E0001", "DEL-A", "DEL-B")],
        [evidence("DEL-B", state="SEMANTIC_READY")],
    )

    row = summary["queue_rows_by_id"]["DEL-A"]  # type: ignore[index]
    assert row["BlockerState"] == BLOCKED
    assert row["BlockingUpstreamDeliverables"] == "DEL-B"


# --- Project mode (--execution-root): docs/SPEC.md §5.3-§5.4 -------------------

import pytest  # noqa: E402

from build_dev001_blocker_queue import DAG_PENDING, NOT_TRACKED, PKG_00, build_project_queue, main  # noqa: E402


def unit(root: Path, name: str, state: str, dependencies: str | None = None, rows: list[dict[str, str]] | None = None) -> Path:
    path = root / "PKG-01_P" / "1_Working" / name
    path.mkdir(parents=True, exist_ok=True)
    (path / "_STATUS.md").write_text(f"# Status\n\n**Current State:** {state}\n", encoding="utf-8")
    if dependencies is not None:
        (path / "_DEPENDENCIES.md").write_text(dependencies, encoding="utf-8")
    if rows is not None:
        write_csv(path / "Dependencies.csv", rows, REQUIRED_COLUMNS)
    return path


def declared(mode: str, *entries: str) -> str:
    body = "".join(entries) or "- TBD\n"
    return (
        f"## Dependency Tracking Mode\n- **Mode:** {mode}\n\n"
        f"## Declared Upstream (I need these before I can proceed)\n{body}\n"
    )


def test_project_mode_without_dag_reads_the_union_register(tmp_path: Path) -> None:
    root = tmp_path / "execution"
    # A declaration with no CSV row still blocks until its maturity is reached.
    unit(root, "DEL-01-01_A", "IN_PROGRESS", declared("DECLARED", "- DEL-01-02 B — Reason: r\n  - Required maturity: ISSUED\n"))
    unit(root, "DEL-01-02_B", "CHECKING")
    # A CSV row and a declaration on the same arc count once; the declared maturity governs.
    unit(
        root, "DEL-01-03_C", "IN_PROGRESS",
        declared("FULL_GRAPH", "- DEL-01-02 B — Reason: r\n  - Required maturity: IN_PROGRESS\n"),
        [{**edge("DEP-C-1", "DEL-01-03", "DEL-01-02"), "RequiredMaturity": "ISSUED"}],  # the CSV value would block
    )
    unit(root, "DEL-01-04_D", "OPEN", declared("NOT_TRACKED"), [edge("DEP-D-1", "DEL-01-04", "DEL-01-02")])

    summary = build_project_queue(root)
    rows = summary["queue_rows_by_id"]  # type: ignore[index]

    assert summary["blocker_source"] == "RECORDED_REGISTER"
    assert rows["DEL-01-01"]["BlockerState"] == BLOCKED
    assert rows["DEL-01-01"]["BlockingUpstreamDeliverables"] == "DEL-01-02"
    assert rows["DEL-01-01"]["BlockingEdgeIDs"] == "DECLARED-DEL-01-01-001"
    assert rows["DEL-01-03"]["BlockerState"] == UNBLOCKED
    assert rows["DEL-01-03"]["ActiveUpstreamCount"] == "1"
    assert rows["DEL-01-04"]["BlockerState"] == NOT_TRACKED
    assert rows["DEL-01-04"]["BlockingUpstreamCount"] == ""
    assert summary["declared_disagreements"] == [{
        "DeliverableID": "DEL-01-03", "Direction": "UPSTREAM", "TargetDeliverableID": "DEL-01-02",
        "DependencyID": "DEP-C-1", "Field": "RequiredMaturity", "Declared": "IN_PROGRESS", "Csv": "ISSUED",
    }]


def test_project_mode_without_dag_holds_cycle_arcs(tmp_path: Path) -> None:
    root = tmp_path / "execution"
    unit(root, "DEL-01-01_A", "OPEN", rows=[edge("DEP-A-1", "DEL-01-01", "DEL-01-02")])
    unit(root, "DEL-01-02_B", "OPEN", declared("FULL_GRAPH", "- DEL-01-01 A — Reason: r\n"))

    summary = build_project_queue(root)
    rows = summary["queue_rows_by_id"]  # type: ignore[index]

    assert summary["held_arc_count"] == 2
    assert rows["DEL-01-01"]["BlockerState"] == UNBLOCKED
    assert rows["DEL-01-01"]["HeldEdgeIDs"] == "DEL-01-01->DEL-01-02"
    assert rows["DEL-01-02"]["BlockerState"] == UNBLOCKED


def accepted(root: Path, edges: list[dict[str, str]]) -> None:
    version = root / "_DAG" / "DAG-003"
    write_csv(version / "DeliverableNodes.csv", [node("DEL-01-01"), node("DEL-01-02"), node("DEL-01-03")], NODE_COLUMNS)
    write_csv(version / "DependencyEdges.csv", edges, REQUIRED_COLUMNS)
    (root / "_DAG" / "_LATEST.md").write_text("Latest: DAG-003\nUpdated: 2026-09-26\n", encoding="utf-8")


def test_project_mode_with_accepted_dag_uses_the_version_and_reports_dag_pending(tmp_path: Path) -> None:
    root = tmp_path / "execution"
    unit(root, "DEL-01-01_A", "OPEN", rows=[edge("DEP-A-1", "DEL-01-01", "DEL-01-02")])
    unit(root, "DEL-01-02_B", "INITIALIZED")
    unit(root, "DEL-01-03_C", "OPEN")
    accepted(root, [edge("DEP-A-1", "DEL-01-01", "DEL-01-02")])  # RequiredMaturity SEMANTIC_READY

    current = build_project_queue(root)
    rows = current["queue_rows_by_id"]  # type: ignore[index]
    assert current["blocker_source"] == "ACCEPTED_DAG:DAG-003"
    assert current["currency"]["result"] == "NO_DEPARTURE_FOUND"  # type: ignore[index]
    assert rows["DEL-01-01"]["BlockerState"] == BLOCKED
    assert rows["DEL-01-03"]["BlockerState"] == UNBLOCKED

    # A new local declaration departs from the accepted version: its endpoints are DAG pending.
    (root / "PKG-01_P" / "1_Working" / "DEL-01-03_C" / "_DEPENDENCIES.md").write_text(
        declared("FULL_GRAPH", "- DEL-01-01 A — Reason: new\n"), encoding="utf-8"
    )
    departed = build_project_queue(root)
    rows = departed["queue_rows_by_id"]  # type: ignore[index]
    assert departed["currency"]["result"] == "DEPARTURE"  # type: ignore[index]
    assert rows["DEL-01-03"]["BlockerState"] == DAG_PENDING
    assert rows["DEL-01-01"]["BlockerState"] == DAG_PENDING
    assert rows["DEL-01-01"]["BlockingUpstreamDeliverables"] == ""
    assert "arc added: DEL-01-03 -> DEL-01-01" in rows["DEL-01-01"]["DagPendingReasons"]
    assert rows["DEL-01-02"]["BlockerState"] == UNBLOCKED
    assert departed["dag_pending_count"] == 2


def test_project_mode_cli(tmp_path: Path) -> None:
    root = tmp_path / "execution"
    unit(root, "DEL-01-01_A", "OPEN", declared("DECLARED", "- DEL-01-02 B — Reason: r\n"))
    unit(root, "DEL-01-02_B", "OPEN")
    csv_out = tmp_path / "out" / "queue.csv"
    markdown_out = tmp_path / "out" / "queue.md"
    json_out = tmp_path / "out" / "queue.json"

    assert main([
        "--execution-root", str(root), "--csv-out", str(csv_out), "--markdown-out", str(markdown_out),
        "--json-out", str(json_out), "--generated-date", "2026-09-26",
    ]) == 0
    with csv_out.open(encoding="utf-8", newline="") as handle:
        queue = {row["DeliverableID"]: row for row in csv.DictReader(handle)}
    assert queue["DEL-01-01"]["BlockerState"] == BLOCKED
    assert "No accepted project DAG" in markdown_out.read_text(encoding="utf-8")
    assert json_out.is_file()

    with pytest.raises(SystemExit):
        main(["--execution-root", str(root), "--dag-dir", str(tmp_path)])
    with pytest.raises(SystemExit):
        main(["--json-out", str(json_out)])
    (root / "_DAG").mkdir()
    (root / "_DAG" / "_LATEST.md").write_text("Latest: DAG-404\n", encoding="utf-8")
    assert main(["--execution-root", str(root)]) == 2


def evidence_file(path: Path, committed: list[str]) -> Path:
    write_csv(path, [{"DeliverableID": item, "PackageID": "PKG-01", "EvidenceState": COMMITTED} for item in committed], EVIDENCE_COLUMNS)
    return path


@pytest.mark.parametrize(("committed", "consumer_package", "expected"), [
    (["DEL-01-02"], "PKG-01", UNBLOCKED),  # only the supplier has committed evidence
    (["DEL-01-01"], "PKG-01", BLOCKED),  # only the consumer has committed evidence
    ([], PKG_00, BLOCKED),  # the row's TargetPackageID is the consumer's, so PKG-00 there does not satisfy the arc
])
def test_project_mode_evidence_judges_a_downstream_arc_by_its_supplier(
    tmp_path: Path, committed: list[str], consumer_package: str, expected: str
) -> None:
    root = tmp_path / "execution"
    # Only the supplier records the arc, as a DOWNSTREAM row: From = supplier, Target = consumer.
    downstream = {**edge("DEP-B-1", "DEL-01-02", "DEL-01-01", target_package=consumer_package), "Direction": "DOWNSTREAM"}
    unit(root, "DEL-01-01_A", "OPEN")
    unit(root, "DEL-01-02_B", "OPEN", rows=[downstream])

    summary = build_project_queue(root, evidence_file(tmp_path / "evidence.csv", committed))
    row = summary["queue_rows_by_id"]["DEL-01-01"]  # type: ignore[index]

    assert row["ActiveUpstreamCount"] == "1"
    assert row["BlockerState"] == expected
    assert summary["queue_rows_by_id"]["DEL-01-02"]["ActiveUpstreamCount"] == "0"  # type: ignore[index]


def test_project_mode_holds_legacy_candidate_status_arcs_of_the_version(tmp_path: Path) -> None:
    root = tmp_path / "execution"
    unit(root, "DEL-01-01_A", "OPEN", rows=[edge("DEP-A-1", "DEL-01-01", "DEL-01-02")])
    unit(root, "DEL-01-02_B", "INITIALIZED")
    unit(root, "DEL-01-03_C", "OPEN", rows=[edge("DEP-C-1", "DEL-01-03", "DEL-01-01", status=CANDIDATE)])
    accepted(root, [edge("DEP-A-1", "DEL-01-01", "DEL-01-02"), edge("DEP-C-1", "DEL-01-03", "DEL-01-01", status=CANDIDATE)])

    summary = build_project_queue(root)
    rows = summary["queue_rows_by_id"]  # type: ignore[index]

    assert summary["currency"]["result"] == "NO_DEPARTURE_FOUND"  # type: ignore[index]
    assert summary["held_arc_count"] == 1
    assert rows["DEL-01-03"]["HeldEdgeIDs"] == "DEL-01-03->DEL-01-01"
    assert rows["DEL-01-03"]["BlockerState"] == UNBLOCKED


def test_project_mode_declared_maturity_governs_across_deliverables(tmp_path: Path) -> None:
    root = tmp_path / "execution"
    # The consumer's CSV row asks for ISSUED; the supplier's declaration of the same arc says IN_PROGRESS.
    unit(root, "DEL-01-01_A", "OPEN", rows=[{**edge("DEP-A-1", "DEL-01-01", "DEL-01-02"), "RequiredMaturity": "ISSUED"}])
    unit(root, "DEL-01-02_B", "CHECKING", (
        "## Dependency Tracking Mode\n- **Mode:** DECLARED\n\n"
        "## Declared Downstream (These need me)\n- DEL-01-01 A — Reason: r\n  - Required maturity: IN_PROGRESS\n"
    ))

    summary = build_project_queue(root)
    row = summary["queue_rows_by_id"]["DEL-01-01"]  # type: ignore[index]

    assert row["ActiveUpstreamCount"] == "1"
    assert row["BlockerState"] == UNBLOCKED
    assert summary["declared_disagreements"] == [{
        "DeliverableID": "DEL-01-01", "Direction": "UPSTREAM", "TargetDeliverableID": "DEL-01-02",
        "DependencyID": "DEP-A-1", "Field": "RequiredMaturity", "Declared": "IN_PROGRESS", "Csv": "ISSUED",
    }]
