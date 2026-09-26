"""Recorded-register union and accepted-DAG currency readers (docs/SPEC.md §5.3-§5.4)."""

from __future__ import annotations

from pathlib import Path

import pytest

import dependency_evidence as de
from audit_dag import REQUIRED_COLUMNS
from test_dag_control_plane import NODE_COLUMNS, edge, node, write_csv


DECLARED = (
    "# Dependencies: DEL-01-01 A\n\n"
    "## Dependency Tracking Mode\n- **Mode:** DECLARED\n\n"
    "## Declared Upstream (I need these before I can proceed)\n"
    "- DEL-01-02 B — Reason: needs the interface\n"
    "  - Required maturity: ISSUED\n"
    "  - Location: TBD\n"
    "- DEL-01-03 C — Reason: needs the data model\n"
    "- TBD\n"
    "- ~~DEL-01-09 retired~~ — withdrawn\n"
    "\n"
    "## Declared Downstream (These need me)\n"
    "- `chirality-x::DEL-02-01_Consumer`\n"
    "  - Required maturity: Not specified\n"
    "- None declared.\n"
    "| DEL-02-02 (table form) | PROPOSAL |\n"
)


def unit(root: Path, package: str, name: str, state: str | None = None) -> Path:
    path = root / f"{package}_P" / "1_Working" / name
    path.mkdir(parents=True, exist_ok=True)
    if state:
        (path / "_STATUS.md").write_text(f"# Status\n\n**Current State:** {state}\n", encoding="utf-8")
    return path


def test_parse_declarations_reads_only_spec_entries() -> None:
    parsed = de.parse_declarations(DECLARED)

    assert parsed.mode == "DECLARED"
    assert [(e.direction, e.target_id, e.required_maturity) for e in parsed.entries] == [
        ("UPSTREAM", "DEL-01-02", "ISSUED"),
        ("UPSTREAM", "DEL-01-03", "TBD"),
        ("DOWNSTREAM", "DEL-02-01", "TBD"),
    ]
    assert parsed.entries[0].reason == "needs the interface"
    assert parsed.entries[0].target_name == "B"
    assert len(parsed.unread) == 2
    assert any("DEL-01-09" in line for line in parsed.unread)
    assert any("DEL-02-02" in line for line in parsed.unread)


def test_parse_declarations_reads_legacy_combined_section_and_mode() -> None:
    text = (
        "## Coordination (human-owned)\n- Mode: TRACKED\n\n"
        "## Declared upstream/downstream lists\n- Upstream: DEL-01-02 (SEMANTIC_READY)\n- Downstream: DEL-03-01\n- DEL-04-01\n"
    )
    parsed = de.parse_declarations(text)

    assert parsed.mode == "FULL_GRAPH"
    assert [(e.direction, e.target_id, e.required_maturity) for e in parsed.entries] == [
        ("UPSTREAM", "DEL-01-02", "SEMANTIC_READY"),
        ("DOWNSTREAM", "DEL-03-01", "TBD"),
    ]
    assert parsed.unread == ["DEL-04-01"]


def test_union_counts_an_edge_once_and_the_declaration_governs() -> None:
    declarations = de.parse_declarations(DECLARED)
    row = edge("DEP-1", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")  # RequiredMaturity SEMANTIC_READY
    other = edge("DEP-2", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-07")

    rows, declared_only, disagreements = de.union_register("DEL-01-01", [row, other], declarations)

    assert [r["DependencyID"] for r in rows] == ["DEP-1", "DEP-2"]
    assert rows[0]["RequiredMaturity"] == "ISSUED"
    assert row["RequiredMaturity"] == "SEMANTIC_READY"  # the input is not modified
    assert disagreements == [{
        "DeliverableID": "DEL-01-01", "Direction": "UPSTREAM", "TargetDeliverableID": "DEL-01-02",
        "DependencyID": "DEP-1", "Field": "RequiredMaturity", "Declared": "ISSUED", "Csv": "SEMANTIC_READY",
    }]
    assert [(r["Direction"], r["TargetDeliverableID"], r["DependencyType"], r["Origin"]) for r in declared_only] == [
        ("UPSTREAM", "DEL-01-03", "PREREQUISITE", "DECLARED"),
        ("DOWNSTREAM", "DEL-02-01", "ENABLES", "DECLARED"),
    ]


def test_recorded_register_reads_markdown_without_csv(tmp_path: Path) -> None:
    path = unit(tmp_path, "PKG-01", "DEL-01-01_A")
    (path / "_DEPENDENCIES.md").write_text(DECLARED, encoding="utf-8")

    register = de.recorded_register(path)

    assert register.csv_present is False and register.declarations_present is True
    assert register.rows == []
    assert len(register.union_rows) == 3


@pytest.mark.parametrize("pointer", [
    "Latest: DAG-002\nUpdated: 2026-09-26\nAcceptance: DAG-002/ACCEPTANCE_RECORD.md\n",
    "# Latest DAG Pointer\n\n- Latest DAG artifact: `DAG-002`\n- Latest DAG artifact path: `execution/_DAG/DAG-002/`\n",
])
def test_pointer_forms(pointer: str) -> None:
    assert de.pointer_target(pointer) == "DAG-002"


def accepted_project(tmp_path: Path) -> Path:
    root = tmp_path / "execution"
    a = unit(root, "PKG-01", "DEL-01-01_A")
    unit(root, "PKG-01", "DEL-01-02_B")
    unit(root, "PKG-01", "DEL-01-03_C")
    write_csv(a / "Dependencies.csv", [edge("DEP-1", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")], REQUIRED_COLUMNS)
    version = root / "_DAG" / "DAG-001"
    write_csv(version / "DeliverableNodes.csv", [
        node("DEL-01-01", "PKG-01", "A"), node("DEL-01-02", "PKG-01", "B"), node("DEL-01-03", "PKG-01", "C"),
    ], NODE_COLUMNS)
    write_csv(version / "DependencyEdges.csv", [edge("DEP-1", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")], REQUIRED_COLUMNS)
    (root / "_DAG" / "_LATEST.md").write_text("Latest: DAG-001\nUpdated: 2026-09-26\n", encoding="utf-8")
    return root


def test_currency_finds_no_departure_when_arcs_and_inventory_match(tmp_path: Path) -> None:
    root = accepted_project(tmp_path)
    dag = de.resolve_accepted_dag(root)
    assert dag is not None and dag.name == "DAG-001"

    currency = de.check_currency(dag, de.project_registers(root))

    assert currency.result == "NO_DEPARTURE_FOUND"
    assert currency.pending == {}


def test_currency_flags_added_arc_removed_arc_and_inventory_change(tmp_path: Path) -> None:
    root = accepted_project(tmp_path)
    c = root / "PKG-01_P" / "1_Working" / "DEL-01-03_C"
    (c / "_DEPENDENCIES.md").write_text(
        "## Declared Upstream (I need these before I can proceed)\n- DEL-01-01 A — Reason: new need\n", encoding="utf-8"
    )
    (root / "PKG-01_P" / "1_Working" / "DEL-01-01_A" / "Dependencies.csv").unlink()
    unit(root, "PKG-01", "DEL-01-04_D")

    currency = de.check_currency(de.resolve_accepted_dag(root), de.project_registers(root))

    assert currency.result == "DEPARTURE"
    assert currency.added_arcs == [("DEL-01-03", "DEL-01-01")]
    assert currency.removed_arcs == [("DEL-01-01", "DEL-01-02")]
    assert currency.added_deliverables == ["DEL-01-04"]
    assert sorted(currency.pending) == ["DEL-01-01", "DEL-01-02", "DEL-01-03", "DEL-01-04"]


def test_currency_treats_excluded_and_candidate_arcs_as_accounted_for(tmp_path: Path) -> None:
    root = accepted_project(tmp_path)
    b = root / "PKG-01_P" / "1_Working" / "DEL-01-02_B"
    write_csv(b / "Dependencies.csv", [
        edge("DEP-2", "PKG-01", "DEL-01-02", "PKG-01", "DEL-01-03"),
        edge("DEP-3", "PKG-01", "DEL-01-02", "PKG-01", "DEL-01-01"),
    ], REQUIRED_COLUMNS)
    version = root / "_DAG" / "DAG-001"
    write_csv(version / "ExcludedRows.csv", [{
        "FromDeliverableID": "DEL-01-02", "Direction": "UPSTREAM", "TargetType": "DELIVERABLE",
        "TargetDeliverableID": "DEL-01-03", "Disposition": "TYPE_NOT_SELECTED",
    }], ["FromDeliverableID", "Direction", "TargetType", "TargetDeliverableID", "Disposition"])
    write_csv(version / "CandidateEdges.csv", [edge("DEP-3", "PKG-01", "DEL-01-02", "PKG-01", "DEL-01-01")], REQUIRED_COLUMNS)

    currency = de.check_currency(de.resolve_accepted_dag(root), de.project_registers(root))

    assert currency.result == "NO_DEPARTURE_FOUND"


def test_unresolvable_pointer_is_an_error(tmp_path: Path) -> None:
    root = accepted_project(tmp_path)
    (root / "_DAG" / "_LATEST.md").write_text("Latest: DAG-009\n", encoding="utf-8")
    with pytest.raises(de.DagPointerError):
        de.resolve_accepted_dag(root)
    (root / "_DAG" / "_LATEST.md").write_text("pointer without a version line\n", encoding="utf-8")
    with pytest.raises(de.DagPointerError):
        de.resolve_accepted_dag(root)
    (root / "_DAG" / "_LATEST.md").unlink()
    assert de.resolve_accepted_dag(root) is None


def test_declaration_matching_only_a_retired_row_is_a_visible_disagreement() -> None:
    declarations = de.parse_declarations(DECLARED)
    retired = edge("DEP-1", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02", status="RETIRED")

    rows, declared_only, disagreements = de.union_register("DEL-01-01", [retired], declarations)

    assert rows[0]["Status"] == "RETIRED"
    assert ("UPSTREAM", "DEL-01-02") in {(r["Direction"], r["TargetDeliverableID"]) for r in declared_only}
    assert disagreements == [{
        "DeliverableID": "DEL-01-01", "Direction": "UPSTREAM", "TargetDeliverableID": "DEL-01-02",
        "DependencyID": "DEP-1", "Field": "Status", "Declared": "ACTIVE", "Csv": "RETIRED",
    }]


def test_synthesized_rows_follow_the_dependency_extract_mirror_fields() -> None:
    text = (
        "## Declared Upstream (I need these before I can proceed)\n- DEL-01-02 B — Reason: r\n\n"
        "## Downstream (informational; consumers of this deliverable)\n- DEL-03-01 D — Reason: consumes\n"
    )
    _rows, declared_only, _found = de.union_register("DEL-01-01", [], de.parse_declarations(text))
    upstream, downstream = declared_only

    assert upstream["SourceRef"] == "_DEPENDENCIES.md ## Declared Upstream (I need these before I can proceed)"
    assert "type_from=section_heading" in upstream["Notes"]
    assert (upstream["Explicitness"], upstream["Confidence"]) == ("EXPLICIT", "HIGH")
    assert downstream["DependencyType"] == "ENABLES"
    assert downstream["SourceRef"] == "_DEPENDENCIES.md ## Downstream (informational; consumers of this deliverable)"
    assert (downstream["Explicitness"], downstream["Confidence"]) == ("IMPLICIT", "MEDIUM")


def test_currency_accepts_a_candidate_arc_held_locally_as_candidate(tmp_path: Path) -> None:
    root = accepted_project(tmp_path)
    b = root / "PKG-01_P" / "1_Working" / "DEL-01-02_B"
    write_csv(b / "Dependencies.csv", [edge("DEP-3", "PKG-01", "DEL-01-02", "PKG-01", "DEL-01-03", status="CANDIDATE")], REQUIRED_COLUMNS)
    version = root / "_DAG" / "DAG-001"
    write_csv(version / "CandidateEdges.csv", [edge("DEP-3", "PKG-01", "DEL-01-02", "PKG-01", "DEL-01-03", status="CANDIDATE")], REQUIRED_COLUMNS)

    currency = de.check_currency(de.resolve_accepted_dag(root), de.project_registers(root))

    assert currency.result == "NO_DEPARTURE_FOUND"
    assert currency.removed_arcs == []

    # Without any local row, the candidate arc is removed.
    (b / "Dependencies.csv").unlink()
    currency = de.check_currency(de.resolve_accepted_dag(root), de.project_registers(root))
    assert currency.removed_arcs == [("DEL-01-02", "DEL-01-03")]
