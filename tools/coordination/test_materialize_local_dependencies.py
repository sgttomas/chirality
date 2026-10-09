"""`_DEPENDENCIES.md` refresh by materialize_local_dependencies.py --refresh-pointers.

The refresh writes only agent-owned sections (docs/SPEC.md §5.1-§5.2): human-owned,
legacy and unrecognized sections keep their text, a second identical refresh is a
no-op, and a missing file starts from the §5.2 skeleton with human-owned fields TBD.
"""

from __future__ import annotations

from pathlib import Path

from audit_dag import ACTIVE, REQUIRED_COLUMNS
from materialize_local_dependencies import (
    materialize_local_dependencies,
    refresh_dependencies_text,
    render_console,
    split_sections,
)
from test_dag_control_plane import NODE_COLUMNS, edge, node, read_rows, write_csv


NODE = {"DeliverableID": "DEL-01-01", "DeliverableName": "Project governance baseline"}
EDGES_PATH = Path("execution/_DAG/DAG-001/DependencyEdges.csv")

HUMAN_MODE = (
    "## Dependency Tracking Mode\n"
    "- **Mode:** DECLARED\n"
    "- **Register:** Dependencies.csv (schema v3.1) when present; otherwise the declared sections of this file\n"
    "- **Notes:** see _COORDINATION.md\n"
    "\n---\n\n"
)
HUMAN_UPSTREAM = (
    "## Declared Upstream (I need these before I can proceed)\n"
    "- DEL-01-02 Copyright policy — Reason: licence terms fix the governance scope\n"
    "  - Required maturity: SEMANTIC_READY\n"
    "  - Location: TBD\n"
    "\n"
)
HUMAN_DOWNSTREAM = (
    "## Declared Downstream (These need me)\n"
    "- DEL-02-01 Release plan — Reason: consumes the governance baseline\n"
    "  - Required maturity: ISSUED\n"
    "  - Location: TBD\n"
    "\n---\n\n"
)


def rows_fixture() -> list[dict[str, str]]:
    return [edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02", status=ACTIVE)]


def refresh(existing: str | None, rows: list[dict[str, str]] | None = None, generated: str = "2026-09-26") -> str:
    return refresh_dependencies_text(
        existing,
        NODE,
        rows if rows is not None else rows_fixture(),
        generated,
        "DAG-001",
        EDGES_PATH,
        canonical_output=True,
    )


def section_texts(text: str) -> dict[str, str]:
    return {section.heading.strip(): section.text() for section in split_sections(text) if section.heading}


def test_refresh_preserves_human_owned_and_unknown_sections_byte_for_byte() -> None:
    custom = "## Interface Notes\nA human note the tool does not know.\n\n"
    existing = (
        "# Dependencies: DEL-01-01 Project governance baseline\n\n"
        + HUMAN_MODE
        + HUMAN_UPSTREAM
        + HUMAN_DOWNSTREAM
        + custom
        + "## Extracted Dependency Register\n- **Status:** NOT_RUN_YET\n\n---\n\n"
        + "## Lifecycle Summary\n- (placeholder)\n\n---\n\n"
        + "## Run Notes\n- Earlier extraction warning kept by the tool.\n\n"
        + "## Run History\n- 2026-09-01 dependency-extract run\n\n"
        + "## Downstream Handoff Notes\n- handoff text\n"
    )

    refreshed = refresh(existing)

    for block in (HUMAN_MODE, HUMAN_UPSTREAM, HUMAN_DOWNSTREAM, custom, "## Downstream Handoff Notes\n- handoff text\n"):
        assert block in refreshed
    assert refreshed.startswith("# Dependencies: DEL-01-01 Project governance baseline\n\n" + HUMAN_MODE)
    sections = section_texts(refreshed)
    assert "SYNCHRONIZED_FROM_DAG_001" in sections["## Extracted Dependency Register"]
    assert "### Authority Boundary" in sections["## Extracted Dependency Register"]
    assert "| Status=ACTIVE | 1 |" in sections["## Lifecycle Summary"]
    assert sections["## Run Notes"] == "## Run Notes\n- Earlier extraction warning kept by the tool.\n\n"
    history = sections["## Run History"]
    assert history.startswith("## Run History\n- 2026-09-01 dependency-extract run\n- 2026-09-26 — ")
    assert "## Generated Dependency Register" not in refreshed
    headings = [section.heading.strip() for section in split_sections(refreshed) if section.heading]
    assert headings == [
        "## Dependency Tracking Mode",
        "## Declared Upstream (I need these before I can proceed)",
        "## Declared Downstream (These need me)",
        "## Interface Notes",
        "## Extracted Dependency Register",
        "## Lifecycle Summary",
        "## Run Notes",
        "## Run History",
        "## Downstream Handoff Notes",
    ]


def test_refresh_reads_legacy_headings_and_keeps_them() -> None:
    legacy_mode = "## Coordination (human-owned)\n- Mode: TRACKED\n\n"
    legacy_lists = "## Declared upstream/downstream lists\n- Upstream: DEL-01-02 (SEMANTIC_READY)\n\n"
    legacy_register = "## Extracted Dependency Register (populated by TASK+dependency-extract)\n- old summary\n\n"
    legacy_notes = "## Run Notes & History\n- 2026-08-01 earlier run\n\n"
    legacy_handoff = "## Consumer Handoff Notes (optional)\n- consumer text\n"
    existing = (
        "# Dependencies: DEL-01-01 Project governance baseline\n\n"
        + legacy_mode + legacy_lists + legacy_register + legacy_notes + legacy_handoff
    )

    refreshed = refresh(existing)

    assert legacy_mode in refreshed
    assert legacy_lists in refreshed
    assert legacy_handoff in refreshed
    sections = section_texts(refreshed)
    register = sections["## Extracted Dependency Register (populated by TASK+dependency-extract)"]
    assert "old summary" not in register
    assert "SYNCHRONIZED_FROM_DAG_001" in register
    combined = sections["## Run Notes & History"]
    assert combined.startswith("## Run Notes & History\n- 2026-08-01 earlier run\n- 2026-09-26 — ")
    # The combined legacy section covers Run Notes and Run History; neither is added.
    assert "## Run Notes\n" not in refreshed
    assert "## Run History\n" not in refreshed
    # Lifecycle Summary is missing and is added in §5.2 order, before Run Notes & History.
    headings = [section.heading.strip() for section in split_sections(refreshed) if section.heading]
    assert headings.index("## Lifecycle Summary") == headings.index("## Run Notes & History") - 1
    # The legacy mode value is left as written.
    assert "- Mode: TRACKED" in refreshed


def test_refresh_is_idempotent() -> None:
    existing = "# Dependencies: DEL-01-01 Project governance baseline\n\n" + HUMAN_MODE + HUMAN_UPSTREAM + HUMAN_DOWNSTREAM

    first = refresh(existing)
    second = refresh(first)

    assert second == first
    assert first.count("`materialize_local_dependencies.py --refresh-pointers`: synchronized from") == 1


def test_refresh_appends_history_only_for_a_changed_refresh() -> None:
    first = refresh(None)
    later = refresh(first, rows=[], generated="2026-09-27")

    history = section_texts(later)["## Run History"]
    assert "2026-09-26 — " in history
    assert "2026-09-27 — " in history
    assert "- **Rows:** 0 total; 0 ACTIVE; 0 CANDIDATE." in later


def test_refresh_creates_missing_file_from_spec_skeleton() -> None:
    created = refresh(None)

    headings = [section.heading.strip() for section in split_sections(created) if section.heading]
    assert headings == [
        "## Dependency Tracking Mode",
        "## Declared Upstream (I need these before I can proceed)",
        "## Declared Downstream (These need me)",
        "## Extracted Dependency Register",
        "## Lifecycle Summary",
        "## Run Notes",
        "## Run History",
    ]
    sections = section_texts(created)
    assert "- **Mode:** TBD" in sections["## Dependency Tracking Mode"]
    assert sections["## Declared Upstream (I need these before I can proceed)"] == (
        "## Declared Upstream (I need these before I can proceed)\n- TBD\n\n"
    )
    assert sections["## Declared Downstream (These need me)"].startswith("## Declared Downstream (These need me)\n- TBD\n")
    assert "(placeholder)" not in created
    assert "NOT_RUN_YET" not in created
    assert refresh("\n") == created


def test_refresh_replaces_only_this_tools_prior_generated_sections() -> None:
    prior = (
        "# Dependencies: DEL-01-01 Project governance baseline\n\n"
        "## Generated Dependency Register\n"
        "- **Status:** SYNCHRONIZED_FROM_DAG_001\n"
        "- **Source of Truth:** `execution/_DAG/DAG-001/DependencyEdges.csv`\n"
        "- **Local Register:** `Dependencies.csv`\n"
        "- **Rows:** 1 total; 1 ACTIVE; 0 CANDIDATE.\n"
        "- **Generated:** 2026-08-20\n\n"
        "## Authority Boundary\n"
        "- Aggregate `DAG-001` remains the sequencing and blocker-computation authority within its approval boundary.\n"
        "- This local register is a synchronized mirror/evidence surface, not an independent graph authority.\n"
    )
    refreshed = refresh(prior)
    assert "## Generated Dependency Register" not in refreshed
    assert "\n## Authority Boundary" not in refreshed
    assert "## Extracted Dependency Register\n" in refreshed

    edited_boundary = "## Authority Boundary\n- A human-written boundary statement.\n"
    kept = refresh("# Dependencies: DEL-01-01 Project governance baseline\n\n" + edited_boundary)
    assert edited_boundary in kept


def test_materializer_refresh_keeps_human_sections_on_disk(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    del0101_path = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    del0102_path = execution_root / "PKG-01" / "1_Working" / "DEL-01-02_Copyright policy"
    del0101_path.mkdir(parents=True)
    del0102_path.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [
        node("DEL-01-01", "PKG-01", "Project governance baseline", del0101_path),
        node("DEL-01-02", "PKG-01", "Copyright policy", del0102_path),
    ], NODE_COLUMNS)
    write_csv(edges_path, [edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")], REQUIRED_COLUMNS)
    existing = "# Dependencies: DEL-01-01 Project governance baseline\n\n" + HUMAN_MODE + HUMAN_UPSTREAM + HUMAN_DOWNSTREAM
    (del0101_path / "_DEPENDENCIES.md").write_text(existing, encoding="utf-8")

    def run(dry_run: bool = False) -> dict[str, object]:
        return materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            refresh_pointers=True,
            dry_run=dry_run,
            generated_date="2026-09-26",
            source_label="DAG-001",
        )

    dry = run(dry_run=True)
    assert (del0101_path / "_DEPENDENCIES.md").read_text(encoding="utf-8") == existing
    assert not (del0102_path / "_DEPENDENCIES.md").exists()
    assert {item["DeliverableID"]: item["PointerAction"] for item in dry["written"]} == {
        "DEL-01-01": "UPDATED",
        "DEL-01-02": "CREATED",
    }

    run()
    first = (del0101_path / "_DEPENDENCIES.md").read_text(encoding="utf-8")
    assert first.startswith(existing)
    assert (del0102_path / "_DEPENDENCIES.md").read_text(encoding="utf-8").count("- TBD") == 2

    again = run()
    assert (del0101_path / "_DEPENDENCIES.md").read_text(encoding="utf-8") == first
    assert {item["PointerAction"] for item in again["written"]} == {"UNCHANGED"}


def test_refresh_adds_missing_human_owned_sections_as_tbd_placeholders() -> None:
    existing = (
        "# Dependencies: DEL-01-01 Project governance baseline\n\n"
        + HUMAN_UPSTREAM
        + "## Extracted Dependency Register\n- **Status:** NOT_RUN_YET\n\n"
    )

    refreshed = refresh(existing)

    headings = [section.heading.strip() for section in split_sections(refreshed) if section.heading]
    assert headings[:4] == [
        "## Dependency Tracking Mode",
        "## Declared Upstream (I need these before I can proceed)",
        "## Declared Downstream (These need me)",
        "## Extracted Dependency Register",
    ]
    sections = section_texts(refreshed)
    mode = sections["## Dependency Tracking Mode"]
    assert "- **Mode:** TBD\n" in mode and "- **Notes:** TBD\n" in mode
    assert sections["## Declared Downstream (These need me)"] == "## Declared Downstream (These need me)\n- TBD\n\n"
    # The existing declaration keeps its text and is never supplemented.
    assert HUMAN_UPSTREAM in refreshed
    assert refresh(refreshed) == refreshed

    # A combined legacy declared section covers both directions; no placeholder is added for them.
    legacy = "# Dependencies: DEL-01-01 X\n\n## Declared upstream/downstream lists\n- Upstream: DEL-01-02\n\n"
    legacy_headings = [section.heading.strip() for section in split_sections(refresh(legacy)) if section.heading]
    assert "## Declared Upstream (I need these before I can proceed)" not in legacy_headings
    assert legacy_headings[0] == "## Dependency Tracking Mode"


def test_materializer_keeps_local_declared_rows_when_rewriting_csv(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    aggregate = edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")
    colliding = edge("DEP-01-01-002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-04")
    write_csv(edges_path, [aggregate, colliding], REQUIRED_COLUMNS)

    mirror = edge("DEP-01-01-001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03")
    mirror.update(Origin="DECLARED", DependencyType="PREREQUISITE", Notes="mirrored_from=_DEPENDENCIES.md")
    direct = edge("DEP-01-01-002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-04")
    direct.update(Origin="DECLARED", Statement="declared directly in the CSV")
    retired = edge("DEP-01-01-003", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-05", status="RETIRED")
    retired.update(Origin="DECLARED", Notes="mirrored_from=_DEPENDENCIES.md; retired_by=declaration_removed")
    stale = edge("DEP-01-01-004", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-06")
    stale.update(Origin="EXTRACTED")
    columns = REQUIRED_COLUMNS + ["LocalExtension"]
    for row in (mirror, direct, retired, stale):
        row["LocalExtension"] = "kept"
    write_csv(unit / "Dependencies.csv", [mirror, direct, retired, stale], columns)

    def run() -> dict[str, object]:
        return materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            refresh_pointers=True,
            generated_date="2026-09-26",
            source_label="DAG-001",
        )

    summary = run()

    header, rows = read_rows(unit / "Dependencies.csv")
    assert header == REQUIRED_COLUMNS + ["LocalExtension"]
    by_id = {row["DependencyID"]: row for row in rows}
    # Aggregate rows are written; the stale extracted row is replaced as before.
    # In the default mode every local declared row is kept, including the retired mirror.
    assert sorted(by_id) == ["DAG-001-E0001", "DEP-01-01-001", "DEP-01-01-002", "DEP-01-01-003"]
    # Kept local declared rows keep their field values, including extension columns.
    for row in (mirror, direct, retired):
        assert by_id[row["DependencyID"]] == {column: row.get(column, "") for column in header}
    assert by_id["DEP-01-01-002"]["Statement"] == "declared directly in the CSV"
    item = summary["written"][0]
    assert item["PreservedDeclaredRows"] == 3
    assert item["SetAsideDeclaredRows"] == []
    assert item["DeclaredIdCollisions"] == ["DEP-01-01-002"]
    assert summary["total_preserved_declared_rows"] == 3
    assert summary["total_set_aside_declared_rows"] == 0
    assert summary["total_declared_id_collisions"] == 1
    console = render_console(summary)
    assert "DeclaredIdCollisions: 1" in console
    assert "Local Origin=DECLARED rows set aside by status (--canonical-output only): 0" in console
    pointer = (unit / "_DEPENDENCIES.md").read_text(encoding="utf-8")
    assert "- **Rows:** 4 total; 3 ACTIVE; 0 CANDIDATE." in pointer

    # A rerun keeps the same bytes.
    before = (unit / "Dependencies.csv").read_bytes()
    run()
    assert (unit / "Dependencies.csv").read_bytes() == before


def test_canonical_output_keeps_active_and_retired_local_declared_rows(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    write_csv(edges_path, [edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")], REQUIRED_COLUMNS)
    active = edge("DEP-01-01-001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03")
    active.update(Origin="DECLARED")
    candidate = edge("DEP-01-01-002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-04", status="CANDIDATE")
    candidate.update(Origin="DECLARED")
    retired = edge("DEP-01-01-003", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-05", status="RETIRED")
    retired.update(Origin="DECLARED")
    extracted_retired = edge("DEP-01-01-004", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-06", status="RETIRED")
    extracted_retired.update(Origin="EXTRACTED", Notes="retired locally")
    extracted_candidate = edge("DEP-01-01-005", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-07", status="CANDIDATE")
    extracted_candidate.update(Origin="EXTRACTED")
    local = [active, candidate, retired, extracted_retired, extracted_candidate]

    def run(canonical: bool) -> tuple[dict[str, object], dict[str, dict[str, str]]]:
        write_csv(unit / "Dependencies.csv", local, REQUIRED_COLUMNS)
        summary = materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            generated_date="2026-09-26",
            source_label="DAG-001",
            canonical_output=canonical,
        )
        return summary, {row["DependencyID"]: row for row in read_rows(unit / "Dependencies.csv")[1]}

    # Canonical output keeps the canonical v3.1 statuses. ACTIVE and RETIRED rows
    # are kept, since rows are retired and never deleted; CANDIDATE rows stay out.
    summary, by_id = run(canonical=True)
    assert sorted(by_id) == ["DAG-001-E0001", "DEP-01-01-001", "DEP-01-01-003", "DEP-01-01-004"]
    assert by_id["DEP-01-01-003"] == retired
    assert by_id["DEP-01-01-004"] == extracted_retired
    item = summary["written"][0]
    assert item["SetAsideDeclaredRows"] == ["DEP-01-01-002"]
    assert item["PreservedDeclaredRows"] == 2
    assert item["PreservedRetiredRows"] == 1
    assert summary["total_preserved_retired_rows"] == 1

    # The default mode keeps every local declared row whatever its Status, and
    # every local RETIRED row; a non-declared local CANDIDATE row is replaced.
    summary, by_id = run(canonical=False)
    assert sorted(by_id) == ["DAG-001-E0001", "DEP-01-01-001", "DEP-01-01-002", "DEP-01-01-003", "DEP-01-01-004"]
    assert summary["written"][0]["SetAsideDeclaredRows"] == []
    assert summary["written"][0]["PreservedRetiredRows"] == 1


def test_rewrite_keeps_a_local_retired_row_the_aggregate_lacks(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    write_csv(edges_path, [
        edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02"),
        edge("DAG-001-E0003", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-04"),
    ], REQUIRED_COLUMNS)
    retired = edge("DAG-001-E0002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03", status="RETIRED")
    retired.update(Origin="EXTRACTED", Notes="no longer found in source text", LocalExtension="kept")
    stale = edge("DEP-01-01-009", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-09")
    stale.update(Origin="EXTRACTED", LocalExtension="")
    columns = REQUIRED_COLUMNS + ["LocalExtension"]

    def run(canonical: bool) -> dict[str, object]:
        return materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            generated_date="2026-09-26",
            source_label="DAG-001",
            canonical_output=canonical,
        )

    for canonical in (False, True):
        write_csv(unit / "Dependencies.csv", [stale, retired], columns)
        summary = run(canonical)
        header, rows = read_rows(unit / "Dependencies.csv")
        # The kept row's own columns stay in the output header.
        assert header == columns
        # Rows are sorted by DependencyID. The retired row keeps every field value;
        # the stale non-declared ACTIVE row is still replaced from the aggregate.
        assert [row["DependencyID"] for row in rows] == ["DAG-001-E0001", "DAG-001-E0002", "DAG-001-E0003"]
        assert rows[1] == {column: retired.get(column, "") for column in header}
        assert summary["written"][0]["PreservedRetiredRows"] == 1
        assert "Local RETIRED rows preserved: 1" in render_console(summary)
        before = (unit / "Dependencies.csv").read_bytes()
        run(canonical)
        assert (unit / "Dependencies.csv").read_bytes() == before


def test_retired_row_also_in_the_aggregate_is_written_once(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    aggregate_retired = edge("DAG-001-E0002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03", status="RETIRED")
    aggregate_retired.update(Notes="retired; aggregate annotation")
    aggregate_active = edge("DAG-001-E0003", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-04")
    aggregate_active.update(Notes="aggregate carries this row as ACTIVE")
    write_csv(edges_path, [
        edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02"),
        aggregate_retired,
        aggregate_active,
    ], REQUIRED_COLUMNS)
    local_retired = edge("DAG-001-E0002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03", status="RETIRED")
    local_retired.update(Origin="EXTRACTED", Notes="retired")
    local_retired_but_active_in_aggregate = edge(
        "DAG-001-E0003", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-04", status="RETIRED"
    )
    local_retired_but_active_in_aggregate.update(Origin="EXTRACTED", Notes="retired locally")

    for canonical in (False, True):
        write_csv(unit / "Dependencies.csv", [local_retired, local_retired_but_active_in_aggregate], REQUIRED_COLUMNS)
        summary = materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            generated_date="2026-09-26",
            source_label="DAG-001",
            canonical_output=canonical,
        )
        _header, rows = read_rows(unit / "Dependencies.csv")
        assert [row["DependencyID"] for row in rows] == ["DAG-001-E0001", "DAG-001-E0002", "DAG-001-E0003"]
        by_id = {row["DependencyID"]: row for row in rows}
        # The aggregate's RETIRED row is not materialized, so the local copy is
        # kept unchanged, once.
        assert by_id["DAG-001-E0002"] == local_retired
        # Where the aggregate materializes the ID, its row is written as before
        # and the local RETIRED copy is not added.
        assert by_id["DAG-001-E0003"] == aggregate_active
        assert summary["written"][0]["PreservedRetiredRows"] == 1


def test_local_row_the_aggregate_retired_is_written_as_the_aggregate_retired_row(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    aggregate_retired = edge("DAG-001-E0002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03", status="RETIRED")
    aggregate_retired.update(Notes="retired by the accepted DAG")
    write_csv(edges_path, [
        edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02"),
        aggregate_retired,
    ], REQUIRED_COLUMNS)
    local_active = edge("DAG-001-E0002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03")
    local_active.update(Origin="EXTRACTED", Notes="still active locally")

    for canonical in (False, True):
        write_csv(unit / "Dependencies.csv", [local_active], REQUIRED_COLUMNS)
        summary = materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            generated_date="2026-09-27",
            source_label="DAG-001",
            canonical_output=canonical,
        )
        _header, rows = read_rows(unit / "Dependencies.csv")
        # The row is retired, not deleted: the aggregate's RETIRED row is written.
        assert [row["DependencyID"] for row in rows] == ["DAG-001-E0001", "DAG-001-E0002"]
        assert rows[1] == aggregate_retired
        item = summary["written"][0]
        assert item["RetiredFromAggregateRows"] == ["DAG-001-E0002"]
        assert item["DroppedLocalRows"] == []
        assert summary["total_retired_from_aggregate_rows"] == 1
        assert "Local rows written as the aggregate's RETIRED row: 1" in render_console(summary)


def test_local_row_the_aggregate_lacks_is_replaced_and_reported(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    write_csv(edges_path, [edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")], REQUIRED_COLUMNS)
    replaced = edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")
    replaced.update(Origin="EXTRACTED", Notes="local copy of an aggregate row")
    missing_b = edge("DEP-01-01-009", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-09")
    missing_b.update(Origin="EXTRACTED")
    missing_a = edge("DEP-01-01-008", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-08")
    missing_a.update(Origin="EXTRACTED")
    write_csv(unit / "Dependencies.csv", [missing_b, replaced, missing_a], REQUIRED_COLUMNS)

    summary = materialize_local_dependencies(
        edges_path=edges_path,
        nodes_path=nodes_path,
        execution_root=execution_root,
        generated_date="2026-09-27",
        source_label="DAG-001",
    )

    _header, rows = read_rows(unit / "Dependencies.csv")
    # The accepted DAG is authoritative for extracted rows: the rows it lacks are
    # replaced (left out) as before, and now listed. A row it carries is replaced
    # by its content and is not listed as dropped.
    assert [row["DependencyID"] for row in rows] == ["DAG-001-E0001"]
    assert rows[0]["Notes"] != "local copy of an aggregate row"
    item = summary["written"][0]
    assert item["DroppedLocalRows"] == ["DEP-01-01-008", "DEP-01-01-009"]
    assert summary["total_dropped_local_rows"] == 2
    assert "Local rows dropped (replaced by the aggregate, which omits them): 2" in render_console(summary)


def test_status_is_compared_case_insensitively_and_kept_as_written(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    aggregate_retired = edge("DAG-001-E0004", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-05", status="retired")
    write_csv(edges_path, [
        edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02"),
        aggregate_retired,
    ], REQUIRED_COLUMNS)
    extracted = edge("DAG-001-E0002", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-03", status="retired")
    extracted.update(Origin="EXTRACTED")
    declared = edge("DEP-01-01-003", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-04", status=" Retired ")
    declared.update(Origin="DECLARED")
    local_active = edge("DAG-001-E0004", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-05", status="active")
    local_active.update(Origin="EXTRACTED")

    for canonical in (False, True):
        write_csv(unit / "Dependencies.csv", [extracted, declared, local_active], REQUIRED_COLUMNS)
        summary = materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            generated_date="2026-09-27",
            source_label="DAG-001",
            canonical_output=canonical,
        )
        _header, rows = read_rows(unit / "Dependencies.csv")
        by_id = {row["DependencyID"]: row for row in rows}
        assert sorted(by_id) == ["DAG-001-E0001", "DAG-001-E0002", "DAG-001-E0004", "DEP-01-01-003"]
        # Kept rows keep their own spelling.
        assert by_id["DAG-001-E0002"]["Status"] == "retired"
        assert by_id["DEP-01-01-003"]["Status"] == " Retired "
        assert by_id["DAG-001-E0004"] == aggregate_retired
        item = summary["written"][0]
        assert item["PreservedRetiredRows"] == 1
        assert item["SetAsideDeclaredRows"] == []
        assert item["RetiredFromAggregateRows"] == ["DAG-001-E0004"]


def assert_diff_check_clean(text: str) -> None:
    """What `git diff --check` reports: trailing whitespace, and a blank line at end of file."""
    assert text.endswith("\n") and not text.endswith("\n\n"), repr(text[-40:])
    for number, line in enumerate(text.split("\n"), start=1):
        assert line == line.rstrip(" \t"), f"trailing whitespace on line {number}: {line!r}"


ENDS_IN_RUN_HISTORY = (
    "# Dependencies: DEL-01-01 Project governance baseline\n\n"
    + HUMAN_MODE
    + HUMAN_UPSTREAM
    + HUMAN_DOWNSTREAM
    + "## Extracted Dependency Register\n- **Status:** NOT_RUN_YET\n\n---\n\n"
    + "## Lifecycle Summary\n- (placeholder)\n\n---\n\n"
    + "## Run Notes\n- Earlier extraction warning kept by the tool.\n\n"
    + "## Run History\n- 2026-09-01 dependency-extract run\n"
)


def test_file_ending_in_run_history_has_no_blank_line_at_eof_across_dates() -> None:
    first = refresh(ENDS_IN_RUN_HISTORY, generated="2026-09-26")
    assert_diff_check_clean(first)
    assert first.endswith("\n- 2026-09-26 — `materialize_local_dependencies.py --refresh-pointers`: synchronized from "
                          "`DAG-001`; 1 rows (1 ACTIVE, 0 CANDIDATE).\n")
    # Only the end of file differs from the text before the fix; the separators are unchanged.
    assert "- Earlier extraction warning kept by the tool.\n\n## Run History\n" in first
    assert "| SatisfactionStatus=UNKNOWN | 1 |\n\n---\n\n## Run Notes\n" in first
    assert refresh(first, generated="2026-09-26") == first

    later = refresh(first, generated="2026-09-27")
    assert_diff_check_clean(later)
    assert later.startswith(first.replace("- **Run date:** 2026-09-26", "- **Run date:** 2026-09-27"))
    assert later.endswith("synchronized from `DAG-001`; 1 rows (1 ACTIVE, 0 CANDIDATE).\n- 2026-09-27 — "
                          "`materialize_local_dependencies.py --refresh-pointers`: synchronized from `DAG-001`; "
                          "1 rows (1 ACTIVE, 0 CANDIDATE).\n")
    assert refresh(later, generated="2026-09-27") == later


def test_blank_line_left_at_eof_by_an_earlier_run_is_dropped() -> None:
    clean = refresh(ENDS_IN_RUN_HISTORY, generated="2026-09-26")
    # An earlier revision of the tool left a blank line after Run History.
    assert refresh(clean + "\n", generated="2026-09-26") == clean
    later = refresh(clean + "\n\n", generated="2026-09-27")
    assert_diff_check_clean(later)
    assert later == refresh(clean, generated="2026-09-27")
    # A last line without its newline gets one, and the next entry starts on its own line.
    unterminated = refresh(clean[:-1], generated="2026-09-27")
    assert unterminated == later


def test_inserted_sections_keep_separators_and_end_the_file_cleanly() -> None:
    # Run Notes and Run History are missing: both are inserted, the last at end of file.
    existing = (
        "# Dependencies: DEL-01-01 Project governance baseline\n\n"
        + HUMAN_MODE
        + HUMAN_UPSTREAM
        + HUMAN_DOWNSTREAM
        + "## Extracted Dependency Register\n- **Status:** NOT_RUN_YET\n\n---\n\n"
        + "## Lifecycle Summary\n- (placeholder)\n"
    )
    refreshed = refresh(existing, generated="2026-09-26")
    assert_diff_check_clean(refreshed)
    assert "| SatisfactionStatus=UNKNOWN | 1 |\n\n## Run Notes\n- `Dependencies.csv`" in refreshed
    assert "`TBD` there means the human has not yet recorded them.\n\n## Run History\n- 2026-09-26 — " in refreshed
    assert refresh(refreshed, generated="2026-09-26") == refreshed
    later = refresh(refreshed, generated="2026-09-27")
    assert_diff_check_clean(later)
    assert later.count("`materialize_local_dependencies.py --refresh-pointers`: synchronized from") == 2

    # A section inserted before an existing one keeps the blank separator before that section.
    middle = (
        "# Dependencies: DEL-01-01 Project governance baseline\n\n"
        + HUMAN_MODE
        + HUMAN_UPSTREAM
        + HUMAN_DOWNSTREAM
        + "## Extracted Dependency Register\n- **Status:** NOT_RUN_YET\n\n---\n\n"
        + "## Run Notes\n- kept note\n\n"
        + "## Run History\n- 2026-09-01 dependency-extract run\n\n"
        + "## Downstream Handoff Notes\n- handoff text\n"
    )
    refreshed = refresh(middle, generated="2026-09-26")
    assert_diff_check_clean(refreshed)
    assert "| SatisfactionStatus=UNKNOWN | 1 |\n\n## Run Notes\n- kept note\n\n## Run History\n" in refreshed
    assert "(1 ACTIVE, 0 CANDIDATE).\n\n## Downstream Handoff Notes\n- handoff text\n" in refreshed
    assert refreshed.endswith("## Downstream Handoff Notes\n- handoff text\n")

    # A missing file is created from the skeleton and also ends cleanly.
    created = refresh(None)
    assert_diff_check_clean(created)
    assert_diff_check_clean(refresh(created, generated="2026-09-27"))


def test_materializer_writes_files_that_pass_diff_check(tmp_path: Path) -> None:
    execution_root = tmp_path / "execution"
    unit = execution_root / "PKG-01" / "1_Working" / "DEL-01-01_Project governance baseline"
    unit.mkdir(parents=True)
    nodes_path = tmp_path / "DeliverableNodes.csv"
    edges_path = tmp_path / "DependencyEdges.csv"
    write_csv(nodes_path, [node("DEL-01-01", "PKG-01", "Project governance baseline", unit)], NODE_COLUMNS)
    write_csv(edges_path, [edge("DAG-001-E0001", "PKG-01", "DEL-01-01", "PKG-01", "DEL-01-02")], REQUIRED_COLUMNS)
    pointer = unit / "_DEPENDENCIES.md"
    pointer.write_text(ENDS_IN_RUN_HISTORY, encoding="utf-8")

    for day in ("2026-09-26", "2026-09-26", "2026-09-27"):
        materialize_local_dependencies(
            edges_path=edges_path,
            nodes_path=nodes_path,
            execution_root=execution_root,
            refresh_pointers=True,
            generated_date=day,
            source_label="DAG-001",
        )
        assert_diff_check_clean(pointer.read_text(encoding="utf-8"))
        assert_diff_check_clean((unit / "Dependencies.csv").read_text(encoding="utf-8"))


def test_unterminated_run_history_heading_is_not_joined_to_the_entry() -> None:
    base = refresh(None)
    cut = base.index("## Run History")
    unterminated = base[:cut] + "## Run History"
    first = refresh(unterminated, generated="2026-09-27")
    assert "## Run History\n" in first
    assert "## Run History-" not in first
    assert first.endswith("\n") and not first.endswith("\n\n")
    assert refresh(first, generated="2026-09-27") == first


def test_yaml_project_refuses_legacy_materialization_before_writing(tmp_path):
    import pytest
    source = tmp_path / 'PKG-01/DEL-01-01/deliverable.yaml'
    source.parent.mkdir(parents=True)
    source.write_text('id: DEL-01-01\nneeds: []\n')
    with pytest.raises(ValueError, match='legacy CSV materialization is retired'):
        materialize_local_dependencies(tmp_path/'missing-edges.csv', tmp_path/'missing-nodes.csv', tmp_path)
    assert list(tmp_path.rglob('Dependencies.csv')) == []
