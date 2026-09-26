#!/usr/bin/env python3
"""
Materialize deliverable-local Dependencies.csv mirrors from an aggregate DAG.

Only non-PKG-00 deliverables are written. PKG-00 remains architecture context
evidence and does not receive local dependency registers from this tool.

Rewriting a deliverable's Dependencies.csv keeps its existing `Origin=DECLARED`
rows (human declarations and their `dependency-extract` mirrors) with their
field values unchanged: the local files are the dependency evidence
(docs/SPEC.md §5.4), so a declaration is never dropped by a rewrite from the
aggregate. The kept rows are written under the output header, so column order,
quoting and empty cells for columns they lacked follow that header. They are
filtered by the same statuses as the aggregate rows (ACTIVE and CANDIDATE, or
ACTIVE only with --canonical-output); a declared row with another status, such
as a RETIRED mirror of a withdrawn declaration, is set aside and counted.
Where the aggregate carries a row with the same DependencyID, the local
declared row is kept and the difference is reported.

With --refresh-pointers, each deliverable's _DEPENDENCIES.md is refreshed in
place under the docs/SPEC.md §5.2 schema: the tool writes the agent-owned
Extracted Dependency Register (with the authority-boundary statements) and
Lifecycle Summary, fills a placeholder Run Notes body, and appends one Run
History entry per distinct refresh. Human-owned sections (tracking mode and
declarations), unrecognized sections and Downstream Handoff Notes keep their
text unchanged (a blank separator line may be added after one when a missing
section is inserted next to it); legacy headings are read per the SPEC §5.2
table. A missing
human-owned section is added as a TBD placeholder (mode and declarations TBD)
and is never filled. A missing file is created from the §5.2 skeleton with the
human-owned mode and declarations left TBD.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

from audit_dag import ACTIVE, CANDIDATE, PKG_00, read_csv_rows, validate_canonical_rows


MATERIALIZED_STATUSES = {ACTIVE, CANDIDATE}
CANONICAL_MATERIALIZED_STATUSES = {ACTIVE}
DECLARED_ORIGIN = "DECLARED"


def sort_key(row: dict[str, str]) -> tuple[str, str]:
    return (row.get("DependencyID", ""), row.get("TargetDeliverableID", ""))


def read_local_register(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        return [], []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def merge_declared_rows(
    header: list[str],
    rows: list[dict[str, str]],
    local_header: list[str],
    local_rows: list[dict[str, str]],
    statuses: set[str] | frozenset[str] = frozenset(MATERIALIZED_STATUSES),
) -> tuple[list[str], list[dict[str, str]], list[dict[str, str]], list[str], list[dict[str, str]]]:
    """Keep the local register's `Origin=DECLARED` rows in a rewrite from the aggregate.

    Only declared rows whose `Status` is in `statuses` (the materialized
    statuses) are kept; the others are set aside. Returns the output header
    (the aggregate header plus any local columns the kept rows need), the rows
    to write, the kept declared rows, the DependencyIDs where an aggregate row
    with different content was set aside for the local declared row with the
    same ID, and the declared rows set aside by status.
    """
    all_declared = [row for row in local_rows if row.get("Origin", "").strip() == DECLARED_ORIGIN]
    declared = [row for row in all_declared if row.get("Status", "").strip() in statuses]
    set_aside = [row for row in all_declared if row.get("Status", "").strip() not in statuses]
    if not declared:
        return header, rows, [], [], set_aside
    by_id = {row.get("DependencyID", "").strip(): row for row in declared}
    collisions: list[str] = []
    kept_aggregate: list[dict[str, str]] = []
    for row in rows:
        local = by_id.get(row.get("DependencyID", "").strip())
        if local is None:
            kept_aggregate.append(row)
        elif any(row.get(column, "") != local.get(column, "") for column in header if column in local_header):
            collisions.append(row.get("DependencyID", "").strip())
    extra = [column for column in local_header if column not in header]
    merged = sorted(kept_aggregate + declared, key=sort_key)
    return header + extra, merged, declared, sorted(collisions), set_aside


def write_dependency_csv(path: Path, header: list[str], rows: list[dict[str, str]], dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=header, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in header})


def dag_label_from_path(edges_path: Path) -> str:
    parent_name = edges_path.parent.name.strip()
    return parent_name if parent_name else "AGGREGATE_DAG"


def pointer_status(source_label: str) -> str:
    return f"SYNCHRONIZED_FROM_{source_label.replace('-', '_').upper()}"


# --- _DEPENDENCIES.md section handling (docs/SPEC.md §5.1-§5.2) -------------
#
# The file has human-owned sections (tracking mode, declared upstream and
# downstream) and agent-owned sections. This tool writes only the agent-owned
# Extracted Dependency Register and Lifecycle Summary, fills a placeholder
# Run Notes body, and appends to Run History. Human-owned sections,
# unrecognized sections and Downstream Handoff Notes keep their text unchanged,
# apart from a blank separator line added when a missing section follows them.

MODE = "mode"
UPSTREAM = "upstream"
DOWNSTREAM = "downstream"
DECLARED_LISTS = "declared_lists"
REGISTER = "register"
LIFECYCLE = "lifecycle"
RUN_NOTES = "run_notes"
RUN_HISTORY = "run_history"
RUN_NOTES_HISTORY = "run_notes_history"
HANDOFF = "handoff"

# §5.2 order; a combined legacy section takes the position of its first part.
SECTION_ORDER = {
    MODE: 0,
    UPSTREAM: 1,
    DOWNSTREAM: 2,
    DECLARED_LISTS: 1,
    REGISTER: 3,
    LIFECYCLE: 4,
    RUN_NOTES: 5,
    RUN_NOTES_HISTORY: 5,
    RUN_HISTORY: 6,
    HANDOFF: 7,
}

SPEC_HEADINGS = {
    MODE: "Dependency Tracking Mode",
    UPSTREAM: "Declared Upstream (I need these before I can proceed)",
    DOWNSTREAM: "Declared Downstream (These need me)",
    REGISTER: "Extracted Dependency Register",
    LIFECYCLE: "Lifecycle Summary",
    RUN_NOTES: "Run Notes",
    RUN_HISTORY: "Run History",
    HANDOFF: "Downstream Handoff Notes",
}

# §5.2 headings plus the legacy headings SPEC §5.2 reads as equivalent
# (compared case-insensitively, without the agent-owned suffix).
HEADING_KEYS = {
    "dependency tracking mode": MODE,
    "coordination (human-owned)": MODE,
    "coordination mode": MODE,
    "dependency tracking": MODE,
    "declared upstream (i need these before i can proceed)": UPSTREAM,
    "upstream (i need these before i can proceed) — human-owned declarations": UPSTREAM,
    "upstream (this deliverable depends on)": UPSTREAM,
    "upstream (i need these)": UPSTREAM,
    "upstream": UPSTREAM,
    "declared upstream": UPSTREAM,
    "declared upstream dependencies": UPSTREAM,
    "declared downstream (these need me)": DOWNSTREAM,
    "downstream (these need me) — human-owned declarations": DOWNSTREAM,
    "downstream (informational; consumers of this deliverable)": DOWNSTREAM,
    "downstream": DOWNSTREAM,
    "declared downstream": DOWNSTREAM,
    "declared downstream dependencies": DOWNSTREAM,
    "declared upstream/downstream lists": DECLARED_LISTS,
    "extracted dependency register": REGISTER,
    "lifecycle summary": LIFECYCLE,
    "run notes": RUN_NOTES,
    "run history": RUN_HISTORY,
    "run notes & history": RUN_NOTES_HISTORY,
    "downstream handoff notes": HANDOFF,
    "consumer handoff notes (optional)": HANDOFF,
    "consumer handoff notes": HANDOFF,
}

AGENT_SUFFIX = "(populated by task+dependency-extract)"

# Sections written by earlier revisions of this tool, which replaced the whole
# file. They are recognized only when every line is one this tool emitted, and
# are then replaced by the §5.2 Extracted Dependency Register. Otherwise they
# are kept like any other unrecognized section.
PRIOR_REGISTER_HEADING = "generated dependency register"
PRIOR_BOUNDARY_HEADING = "authority boundary"
PRIOR_REGISTER_PREFIXES = (
    "- **Status:** SYNCHRONIZED_FROM_",
    "- **Source of Truth:**",
    "- **Local Register:**",
    "- **Rows:**",
    "- **Generated:**",
)
PRIOR_BOUNDARY_PREFIXES = (
    "- Aggregate `",
    "- This local register is a synchronized mirror",
    "- Candidate rows are excluded from this canonical register",
    "- `CANDIDATE` rows remain non-gating",
    "- `PKG-00` architecture-basis rows are preserved here",
)

PLACEHOLDER_BODIES = frozenset({"", "- (placeholder)", "(placeholder)", "- **Status:** NOT_RUN_YET"})

# Placeholders for a missing human-owned section (docs/SPEC.md §5.2). The tool
# adds them so the file has every §5.2 section; it never fills them.
HUMAN_PLACEHOLDERS = {
    MODE: [
        "- **Mode:** TBD",
        "- **Register:** the declared sections of this file together with Dependencies.csv (schema v3.1) when present (docs/SPEC.md §5.3)",
        "- **Notes:** TBD",
    ],
    UPSTREAM: ["- TBD"],
    DOWNSTREAM: ["- TBD"],
}

RUN_NOTES_LINES = [
    "- `Dependencies.csv`, the Extracted Dependency Register and the Lifecycle Summary are written by "
    "`tools/coordination/materialize_local_dependencies.py --refresh-pointers` from the aggregate DAG named "
    "in the register section.",
    "- The Dependency Tracking Mode and declared sections are human-owned; this tool never writes them "
    "(`docs/SPEC.md` §5.1). `TBD` there means the human has not yet recorded them.",
]


class Section:
    """One `## ` section of `_DEPENDENCIES.md`, or the preamble before the first one."""

    def __init__(self, heading: str | None, lines: list[str]) -> None:
        self.heading = heading
        self.lines = lines
        self.key = section_key(heading) if heading is not None else None

    def text(self) -> str:
        return (self.heading or "") + "".join(self.lines)

    def content_and_tail(self) -> tuple[list[str], list[str]]:
        """Split the body into content and its trailing blank or `---` lines."""
        index = len(self.lines)
        while index > 0 and self.lines[index - 1].strip() in {"", "---"}:
            index -= 1
        return self.lines[:index], self.lines[index:]

    def content_text(self) -> str:
        content, _tail = self.content_and_tail()
        return "".join(content).strip()


def normalize_heading(heading_line: str) -> str:
    title = heading_line.strip()[3:].strip().lower()
    if title.endswith(AGENT_SUFFIX):
        title = title[: -len(AGENT_SUFFIX)].strip()
    return title


def section_key(heading_line: str) -> str | None:
    return HEADING_KEYS.get(normalize_heading(heading_line))


def split_sections(text: str) -> list[Section]:
    sections = [Section(None, [])]
    in_fence = False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            sections.append(Section(line, []))
        else:
            sections[-1].lines.append(line)
    return sections


def is_prior_generated(section: Section, prefixes: tuple[str, ...]) -> bool:
    lines = [line.strip() for line in section.lines if line.strip() not in {"", "---"}]
    return bool(lines) and all(line.startswith(prefixes) for line in lines)


def skeleton_text(deliverable_id: str, deliverable_name: str) -> str:
    """The docs/SPEC.md §5.2 skeleton: human-owned fields TBD, agent sections as placeholders."""
    return "\n".join([
        f"# Dependencies: {deliverable_id} {deliverable_name}".rstrip(),
        "",
        f"## {SPEC_HEADINGS[MODE]}",
        "- **Mode:** TBD",
        HUMAN_PLACEHOLDERS[MODE][1],
        "- **Notes:** TBD",
        "",
        "---",
        "",
        f"## {SPEC_HEADINGS[UPSTREAM]}",
        "- TBD",
        "",
        f"## {SPEC_HEADINGS[DOWNSTREAM]}",
        "- TBD",
        "",
        "---",
        "",
        f"## {SPEC_HEADINGS[REGISTER]}",
        "- **Status:** NOT_RUN_YET",
        "",
        "---",
        "",
        f"## {SPEC_HEADINGS[LIFECYCLE]}",
        "- (placeholder)",
        "",
        "---",
        "",
        f"## {SPEC_HEADINGS[RUN_NOTES]}",
        "- (placeholder)",
        "",
        f"## {SPEC_HEADINGS[RUN_HISTORY]}",
        "- (placeholder)",
        "",
    ])


def count_status(rows: list[dict[str, str]], status: str) -> int:
    return sum(1 for row in rows if row.get("Status", "").strip() == status)


def register_lines(
    rows: list[dict[str, str]],
    generated: str,
    source_label: str,
    source_edges_path: Path,
    canonical_output: bool,
) -> list[str]:
    active = [row for row in rows if row.get("Status", "").strip() == ACTIVE]
    anchor_active = sum(1 for row in active if row.get("DependencyClass", "").strip() == "ANCHOR")
    execution_active = sum(1 for row in active if row.get("DependencyClass", "").strip() == "EXECUTION")
    return [
        f"- **Status:** {pointer_status(source_label)}",
        f"- **Source of Truth:** `{source_edges_path}`",
        "- **Local Register:** `Dependencies.csv` (schema v3.1): this deliverable's aggregate rows plus its local `Origin=DECLARED` rows",
        f"- **Run date:** {generated}",
        f"- **Rows:** {len(rows)} total; {len(active)} ACTIVE; {count_status(rows, CANDIDATE)} CANDIDATE.",
        f"- **ANCHOR rows (ACTIVE):** {anchor_active}",
        f"- **EXECUTION rows (ACTIVE):** {execution_active}",
        "",
        "### Authority Boundary",
        f"- These rows were materialized from aggregate `{source_label}`. Under `docs/SPEC.md` §5.4 an accepted project DAG "
        "version governs blockers only through its acceptance record and only while it is current with the local evidence.",
        "- The local files (`_DEPENDENCIES.md` and `Dependencies.csv`) are the dependency evidence. A departure from the accepted "
        "version is decided by the human; local `Origin=DECLARED` rows are kept when this register is rewritten.",
        (
            "- Candidate rows are excluded from this canonical register and remain in a separate non-authoritative worklist."
            if canonical_output
            else "- `CANDIDATE` rows remain non-gating until later RECONCILIATION plus CHANGE approval."
        ),
        "- `PKG-00` architecture-basis rows are preserved here as injected context evidence; `PKG-00` does not receive local dependency registers.",
        "- Entries in this file's human-owned declared sections remain part of the recorded register (`docs/SPEC.md` §5.3).",
    ]


def lifecycle_lines(rows: list[dict[str, str]]) -> list[str]:
    status_counts: dict[str, int] = defaultdict(int)
    satisfaction_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        status_counts[row.get("Status", "").strip() or "BLANK"] += 1
        satisfaction_counts[row.get("SatisfactionStatus", "").strip() or "BLANK"] += 1
    lines = ["| Dimension | Count |", "|---|---|", f"| Rows | {len(rows)} |"]
    lines += [f"| Status={value} | {count} |" for value, count in sorted(status_counts.items())]
    lines += [f"| SatisfactionStatus={value} | {count} |" for value, count in sorted(satisfaction_counts.items())]
    return lines


def history_line(generated: str, source_label: str, rows: list[dict[str, str]]) -> str:
    return (
        f"- {generated} — `materialize_local_dependencies.py --refresh-pointers`: synchronized from "
        f"`{source_label}`; {len(rows)} rows ({count_status(rows, ACTIVE)} ACTIVE, "
        f"{count_status(rows, CANDIDATE)} CANDIDATE)."
    )


def replace_content(section: Section, new_lines: list[str]) -> None:
    _content, tail = section.content_and_tail()
    section.lines = [line + "\n" for line in new_lines] + (tail or ["\n"])


def append_history(section: Section, entry: str) -> None:
    content, tail = section.content_and_tail()
    if any(line.strip() == entry for line in content):
        return
    if "".join(content).strip() in PLACEHOLDER_BODIES:
        content = []
    section.lines = content + [entry + "\n"] + (tail or ["\n"])


def refresh_dependencies_text(
    existing: str | None,
    node: dict[str, str],
    rows: list[dict[str, str]],
    generated: str,
    source_label: str,
    source_edges_path: Path,
    canonical_output: bool = False,
) -> str:
    """Return `_DEPENDENCIES.md` text with this tool's agent-owned sections refreshed.

    A missing or blank file starts from the §5.2 skeleton. In an existing file,
    human-owned sections, unrecognized sections and Downstream Handoff Notes
    keep their text unchanged; only a blank separator line may be added after
    one when a missing section is inserted next to it. A missing human-owned section is added as a TBD
    placeholder and never filled. Agent-owned sections are refreshed under the
    heading the file already uses, and missing ones are added under their §5.2
    heading in §5.2 order. Refreshing twice with the same inputs is a no-op.
    """
    if existing is None or not existing.strip():
        existing = skeleton_text(node.get("DeliverableID", "").strip(), node.get("DeliverableName", "").strip())
    sections = split_sections(existing)

    has_register = any(section.key == REGISTER for section in sections)
    kept: list[Section] = []
    for section in sections:
        if section.heading is not None and section.key is None:
            name = normalize_heading(section.heading)
            if name == PRIOR_REGISTER_HEADING and is_prior_generated(section, PRIOR_REGISTER_PREFIXES):
                if has_register:
                    continue
                section = Section(f"## {SPEC_HEADINGS[REGISTER]}\n", section.lines)
                has_register = True
            elif name == PRIOR_BOUNDARY_HEADING and is_prior_generated(section, PRIOR_BOUNDARY_PREFIXES):
                continue
        kept.append(section)
    sections = kept

    present = {section.key for section in sections if section.key}
    human = [MODE] + ([] if DECLARED_LISTS in present else [UPSTREAM, DOWNSTREAM])
    agent = [REGISTER, LIFECYCLE] + ([] if RUN_NOTES_HISTORY in present else [RUN_NOTES, RUN_HISTORY])
    for key in human + agent:
        if key in present:
            continue
        position = next(
            (index for index, section in enumerate(sections) if section.key and SECTION_ORDER[section.key] > SECTION_ORDER[key]),
            len(sections),
        )
        previous = sections[position - 1]
        if not previous.text().endswith("\n"):
            previous.lines.append("\n")
        if not previous.text().endswith("\n\n"):
            previous.lines.append("\n")
        body = HUMAN_PLACEHOLDERS.get(key, ["- (placeholder)"])
        sections.insert(position, Section(f"## {SPEC_HEADINGS[key]}\n", [line + "\n" for line in body] + ["\n"]))
        present.add(key)

    entry = history_line(generated, source_label, rows)
    for section in sections:
        if section.key == REGISTER:
            replace_content(section, register_lines(rows, generated, source_label, source_edges_path, canonical_output))
        elif section.key == LIFECYCLE:
            replace_content(section, lifecycle_lines(rows))
        elif section.key == RUN_NOTES and section.content_text() in PLACEHOLDER_BODIES:
            replace_content(section, RUN_NOTES_LINES)
        elif section.key in {RUN_HISTORY, RUN_NOTES_HISTORY}:
            append_history(section, entry)

    return "".join(section.text() for section in sections)


def write_pointer(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.write_text(content, encoding="utf-8")


def materialize_local_dependencies(
    edges_path: Path,
    nodes_path: Path,
    execution_root: Path,
    refresh_pointers: bool = False,
    dry_run: bool = False,
    generated_date: str | None = None,
    source_label: str | None = None,
    deliverable_ids: set[str] | None = None,
    canonical_output: bool = False,
) -> dict[str, object]:
    header, edge_rows, edge_width_issues = read_csv_rows(edges_path)
    _node_header, node_rows, node_width_issues = read_csv_rows(nodes_path)
    generated = generated_date or date.today().isoformat()
    resolved_source_label = source_label or dag_label_from_path(edges_path)
    canonical_findings = validate_canonical_rows(edge_rows) if canonical_output else []
    materialized_statuses = CANONICAL_MATERIALIZED_STATUSES if canonical_output else MATERIALIZED_STATUSES

    rows_by_from: dict[str, list[dict[str, str]]] = defaultdict(list)
    skipped_status_counts: dict[str, int] = defaultdict(int)
    for row in edge_rows:
        status = row.get("Status", "").strip()
        if status not in materialized_statuses:
            skipped_status_counts[status or "BLANK"] += 1
            continue
        from_id = row.get("FromDeliverableID", "").strip()
        if from_id:
            rows_by_from[from_id].append(row)

    written: list[dict[str, object]] = []
    skipped_pkg00: list[str] = []
    missing_execution_paths: list[dict[str, str]] = []

    for node in sorted(node_rows, key=lambda item: item.get("DeliverableID", "")):
        deliverable_id = node.get("DeliverableID", "").strip()
        package_id = node.get("PackageID", "").strip()
        execution_path_raw = node.get("ExecutionPath", "").strip()
        if not deliverable_id:
            continue
        if deliverable_ids is not None and deliverable_id not in deliverable_ids:
            continue
        if package_id == PKG_00:
            skipped_pkg00.append(deliverable_id)
            continue
        if not execution_path_raw:
            missing_execution_paths.append({"DeliverableID": deliverable_id, "Reason": "blank ExecutionPath"})
            continue

        execution_path = Path(execution_path_raw)
        if not execution_path.is_absolute():
            execution_path = execution_root.parent / execution_path

        if not execution_path.exists():
            missing_execution_paths.append({"DeliverableID": deliverable_id, "Reason": str(execution_path)})
            continue

        rows = sorted(rows_by_from.get(deliverable_id, []), key=sort_key)
        active_count = sum(1 for row in rows if row.get("Status", "").strip() == ACTIVE)
        candidate_count = sum(1 for row in rows if row.get("Status", "").strip() == CANDIDATE)
        csv_path = execution_path / "Dependencies.csv"
        pointer_path = execution_path / "_DEPENDENCIES.md"

        local_header, local_rows = read_local_register(csv_path)
        out_header, out_rows, kept_declared, collisions, set_aside = merge_declared_rows(
            header, rows, local_header, local_rows, materialized_statuses
        )
        write_dependency_csv(csv_path, out_header, out_rows, dry_run=dry_run)
        pointer_action = ""
        if refresh_pointers:
            existing = pointer_path.read_text(encoding="utf-8") if pointer_path.exists() else None
            refreshed = refresh_dependencies_text(
                existing,
                node,
                out_rows,
                generated,
                resolved_source_label,
                edges_path,
                canonical_output,
            )
            if existing is None:
                pointer_action = "CREATED"
            elif refreshed == existing:
                pointer_action = "UNCHANGED"
            else:
                pointer_action = "UPDATED"
            if refreshed != existing:
                write_pointer(pointer_path, refreshed, dry_run=dry_run)

        written.append({
            "DeliverableID": deliverable_id,
            "PackageID": package_id,
            "DependenciesCsv": str(csv_path),
            "DependenciesPointer": str(pointer_path) if refresh_pointers else "",
            "PointerAction": pointer_action,
            "Rows": len(rows),
            "ActiveRows": active_count,
            "CandidateRows": candidate_count,
            "PreservedDeclaredRows": len(kept_declared),
            "SetAsideDeclaredRows": [row.get("DependencyID", "").strip() for row in set_aside],
            "DeclaredIdCollisions": collisions,
        })

    total_rows = sum(int(item["Rows"]) for item in written)
    total_active_rows = sum(int(item["ActiveRows"]) for item in written)
    total_candidate_rows = sum(int(item["CandidateRows"]) for item in written)
    total_preserved_declared = sum(int(item["PreservedDeclaredRows"]) for item in written)
    total_set_aside_declared = sum(len(item["SetAsideDeclaredRows"]) for item in written)  # type: ignore[arg-type]
    total_collisions = sum(len(item["DeclaredIdCollisions"]) for item in written)  # type: ignore[arg-type]

    return {
        "edges_path": str(edges_path),
        "nodes_path": str(nodes_path),
        "source_label": resolved_source_label,
        "filtered_deliverable_ids": sorted(deliverable_ids or []),
        "execution_root": str(execution_root),
        "dry_run": dry_run,
        "refresh_pointers": refresh_pointers,
        "canonical_output": canonical_output,
        "canonical_finding_count": len(canonical_findings),
        "canonical_findings": canonical_findings,
        "edge_row_width_issue_count": len(edge_width_issues),
        "node_row_width_issue_count": len(node_width_issues),
        "written_count": len(written),
        "total_rows": total_rows,
        "total_active_rows": total_active_rows,
        "total_candidate_rows": total_candidate_rows,
        "total_preserved_declared_rows": total_preserved_declared,
        "total_set_aside_declared_rows": total_set_aside_declared,
        "total_declared_id_collisions": total_collisions,
        "written": written,
        "skipped_pkg00_count": len(skipped_pkg00),
        "skipped_pkg00": skipped_pkg00,
        "missing_execution_path_count": len(missing_execution_paths),
        "missing_execution_paths": missing_execution_paths,
        "skipped_status_counts": dict(sorted(skipped_status_counts.items())),
    }


def render_console(summary: dict[str, object]) -> str:
    lines = []
    filtered = summary.get("filtered_deliverable_ids") or []
    if filtered:
        lines.append(f"Deliverable filter: {','.join(filtered)}")
    lines.extend([
        f"Written local registers: {summary['written_count']}",
        f"Skipped PKG-00 deliverables: {summary['skipped_pkg00_count']}",
        f"Missing execution paths: {summary['missing_execution_path_count']}",
        f"Rows materialized: total={summary['total_rows']} active={summary['total_active_rows']} candidate={summary['total_candidate_rows']}",
        f"Local Origin=DECLARED rows preserved: {summary['total_preserved_declared_rows']}",
        f"Local Origin=DECLARED rows set aside by status: {summary['total_set_aside_declared_rows']}",
        f"DeclaredIdCollisions: {summary['total_declared_id_collisions']}",
        f"Canonical output: {summary['canonical_output']} canonical_findings={summary['canonical_finding_count']}",
        f"Pointer refresh: {summary['refresh_pointers']}",
        f"Dry run: {summary['dry_run']}",
    ])
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Materialize local Dependencies.csv mirrors from an aggregate DAG. Local Origin=DECLARED rows with a "
            "materialized status are kept with their field values unchanged."
        )
    )
    parser.add_argument(
        "--dag-dir",
        type=Path,
        default=Path("execution/_DAG/DAG-001"),
        help="Directory containing DependencyEdges.csv and DeliverableNodes.csv.",
    )
    parser.add_argument("--edges", type=Path, help="Override path to DependencyEdges.csv.")
    parser.add_argument("--nodes", type=Path, help="Override path to DeliverableNodes.csv.")
    parser.add_argument("--execution-root", type=Path, default=Path("execution"))
    parser.add_argument(
        "--refresh-pointers",
        action="store_true",
        help=(
            "Refresh the agent-owned register sections of _DEPENDENCIES.md (docs/SPEC.md §5.2), creating the "
            "§5.2 skeleton when the file is missing; human-owned and unrecognized sections are preserved."
        ),
    )
    parser.add_argument(
        "--canonical-output",
        action="store_true",
        help=(
            "Materialize only canonical ACTIVE rows, from the aggregate and among the kept local Origin=DECLARED "
            "rows, and report canonical validation findings."
        ),
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json-out", type=Path, help="Write materialization summary JSON.")
    parser.add_argument("--source-label", help="Label to write into generated pointer files, e.g. DAG-002.")
    parser.add_argument(
        "--deliverable-id",
        action="append",
        default=[],
        help="Restrict materialization to a deliverable ID. May be repeated or comma-separated.",
    )
    parser.add_argument(
        "--allow-missing-execution-paths",
        action="store_true",
        help="Return success when some DAG nodes do not yet have PREPARATION-created folders.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    edges_path = args.edges or args.dag_dir / "DependencyEdges.csv"
    nodes_path = args.nodes or args.dag_dir / "DeliverableNodes.csv"
    deliverable_ids = {
        item.strip()
        for value in args.deliverable_id
        for item in value.split(",")
        if item.strip()
    } or None
    summary = materialize_local_dependencies(
        edges_path=edges_path,
        nodes_path=nodes_path,
        execution_root=args.execution_root,
        refresh_pointers=args.refresh_pointers,
        dry_run=args.dry_run,
        source_label=args.source_label,
        deliverable_ids=deliverable_ids,
        canonical_output=args.canonical_output,
    )
    print(render_console(summary))
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    if int(summary["missing_execution_path_count"]) > 0 and not args.allow_missing_execution_paths:
        return 1
    if args.canonical_output and int(summary["canonical_finding_count"]) > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
