#!/usr/bin/env python3
"""Read a project's dependency evidence and its accepted project DAG.

Shared by the blocker and closure tools. It applies docs/SPEC.md §5.3 and §5.4
(D-GOV-49):

- The local files are the dependency evidence. A deliverable's recorded
  register is the union of the entries in the declared sections of its
  `_DEPENDENCIES.md` and the rows of its `Dependencies.csv`. A declared entry
  and an ACTIVE EXECUTION row with the same `Direction` and target are one
  edge; where they disagree on required maturity, the declaration governs and
  the disagreement is reported. A declared entry without such a row becomes a
  synthesized `Origin=DECLARED` row; where the only matching row is RETIRED,
  the declaration still wins and the retired row is reported as a
  disagreement.
- A project may accept a project DAG. `{EXECUTION_ROOT}/_DAG/_LATEST.md` names
  the accepted current version. Local evidence departs from it when it adds an
  arc the version does not account for, or lacks an arc the version holds, or
  when the deliverable inventory differs. The endpoints of such arcs, and the
  added or removed deliverables, are `DAG pending`.

This is the simplest check faithful to §5.4. It compares arcs (consumer to
supplier, `DOWNSTREAM` rows reversed) and inventory. It does not verify
source hashes, re-apply the version's selection rules or read rejection
records; those belong to the `project-dag` currency audit, whose result
governs where the two differ.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from materialize_local_dependencies import DECLARED_LISTS, DOWNSTREAM, MODE, UPSTREAM, split_sections

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evaluation"))
from audit_common import inventory  # noqa: E402


LIFECYCLE_ORDER = ("OPEN", "INITIALIZED", "SEMANTIC_READY", "IN_PROGRESS", "CHECKING", "ISSUED")
TRACKING_MODES = ("NOT_TRACKED", "DECLARED", "FULL_GRAPH")
DIRECTION_BY_SECTION = {UPSTREAM: "UPSTREAM", DOWNSTREAM: "DOWNSTREAM"}
# SPEC §5.2 section headings supply the type of a mirrored declaration.
TYPE_BY_DIRECTION = {"UPSTREAM": "PREREQUISITE", "DOWNSTREAM": "ENABLES"}
# A legacy informational downstream heading (for example
# `## Downstream (informational; consumers of this deliverable)`) records a
# consumer list rather than a stated need, so its mirror is IMPLICIT/MEDIUM.
INFORMATIONAL_HEADING = re.compile(r"\binformational\b", re.IGNORECASE)

ID_PATTERN = re.compile(r"^((?:DEL|KTY)-\d{2,3}-\d{2,3}|(?:PKG|CAT)-\d{2,3})(?:_.+)?$")
ENTRY_ID = re.compile(r"^`?(?:[A-Za-z0-9_.-]+::)?((?:DEL|KTY)-\d{2,3}-\d{2,3})(?![0-9])([^`]*)`?(.*)$")
ANY_ID = re.compile(r"(?:DEL|KTY)-\d{2,3}-\d{2,3}")
LEGACY_DIRECTION = re.compile(r"^(upstream|downstream)\s*[:—–-]\s*(.*)$", re.IGNORECASE)
MATURITY = re.compile(r"required maturity\s*:?\**\s*`?([A-Za-z_]+)", re.IGNORECASE)
PAREN_STATE = re.compile(r"\((" + "|".join(LIFECYCLE_ORDER) + r")\)")
REASON = re.compile(r"reason\s*:\s*(.*)$", re.IGNORECASE)
LOCATION = re.compile(r"^location\s*:\s*(.*)$", re.IGNORECASE)
MODE_VALUE = re.compile(r"mode[^A-Za-z\n]*?(NOT_TRACKED|DECLARED|FULL_GRAPH|TRACKED|TBD)\b", re.IGNORECASE)
STATE_LINE = re.compile(r"Current State\W*([A-Z_]+)")
POINTER_LINE = re.compile(
    r"^\s*[-*]?\s*(?:\*\*)?Latest(?: DAG artifact)?(?:\*\*)?\s*:\s*(?:\*\*)?\s*`?([A-Za-z0-9_.-]+)`?\s*$",
    re.MULTILINE,
)

SKIP_PREFIXES = ("none", "tbd", "n/a", "{", "(placeholder)", "dependencies coordinated externally")


def clean(value: object) -> str:
    return str(value or "").strip()


def normalize_id(raw: str) -> str:
    value = clean(raw).strip("`")
    match = ID_PATTERN.fullmatch(value)
    return match.group(1) if match else value


def unit_id(unit: Path) -> str:
    return unit.name.split("_")[0]


def maturity_value(raw: str) -> str:
    value = clean(raw).upper()
    return value if value in LIFECYCLE_ORDER else "TBD"


def maturity_reached(state: str, required: str) -> bool:
    """True when `state` has reached `required` in the SPEC §3.2 order."""
    if state not in LIFECYCLE_ORDER or required not in LIFECYCLE_ORDER:
        return False
    return LIFECYCLE_ORDER.index(state) >= LIFECYCLE_ORDER.index(required)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def arc(row: dict[str, str], require_class: bool = True) -> tuple[str, str] | None:
    """Consumer-to-supplier arc of an EXECUTION row with a deliverable target.

    `ExcludedRows.csv` carries no `DependencyClass`; its rows are read with
    `require_class=False`.
    """
    if require_class and clean(row.get("DependencyClass")) != "EXECUTION":
        return None
    if clean(row.get("TargetType")) != "DELIVERABLE":
        return None
    source, target = normalize_id(row.get("FromDeliverableID", "")), normalize_id(row.get("TargetDeliverableID", ""))
    direction = clean(row.get("Direction"))
    if not source or not target or direction not in {"UPSTREAM", "DOWNSTREAM"}:
        return None
    return (source, target) if direction == "UPSTREAM" else (target, source)


def lifecycle_state(unit: Path | None) -> str:
    """The `Current State` recorded in a deliverable's `_STATUS.md` (SPEC §3.1), or UNKNOWN."""
    if unit is None:
        return "UNKNOWN"
    status = unit / "_STATUS.md"
    if not status.is_file():
        return "UNKNOWN"
    for line in status.read_text(encoding="utf-8", errors="replace").splitlines():
        match = STATE_LINE.search(line)
        if match and match.group(1) in LIFECYCLE_ORDER:
            return match.group(1)
    return "UNKNOWN"


# --- Declared sections (SPEC §5.2 entry form) --------------------------------


@dataclass(frozen=True)
class DeclaredEntry:
    direction: str
    target_id: str
    target_name: str
    reason: str
    required_maturity: str
    location: str
    heading: str
    raw: str


@dataclass
class Declarations:
    mode: str = "UNKNOWN"
    entries: list[DeclaredEntry] = field(default_factory=list)
    unread: list[str] = field(default_factory=list)


def _entry_blocks(lines: list[str]) -> list[tuple[str, list[str]]]:
    blocks: list[tuple[str, list[str]]] = []
    for line in lines:
        text = line.rstrip("\n")
        if re.match(r"^[-*] ", text):
            blocks.append((text[2:].strip(), []))
        elif blocks and re.match(r"^\s+[-*] ", text):
            blocks[-1][1].append(text.strip()[2:].strip())
        elif text.startswith("|") and not re.match(r"^\|[\s|:-]*\|?$", text):
            blocks.append((text, ["__table__"]))
    return blocks


def _parse_entry(head: str, subs: list[str], direction: str | None, heading: str) -> DeclaredEntry | str | None:
    """A DeclaredEntry, the raw text when it cannot be read, or None for a non-entry."""
    raw = head
    if subs == ["__table__"]:
        # Table rows are not in the §5.2 form; a row naming a deliverable is unread.
        return raw
    if head.lower().startswith(SKIP_PREFIXES) or not head:
        return None
    if direction is None:
        legacy = LEGACY_DIRECTION.match(head)
        if not legacy:
            return raw
        direction, head = legacy.group(1).upper(), legacy.group(2).strip()
    match = ENTRY_ID.match(head)
    if not match:
        return raw
    target_id = match.group(1)
    rest = (match.group(2) + match.group(3)).strip()
    reason_match = REASON.search(rest)
    name = rest[: reason_match.start()] if reason_match else rest
    name = name.strip().lstrip("_").strip(" —–-").strip()
    reason = reason_match.group(1).strip() if reason_match else ""
    required = "TBD"
    location = "TBD"
    maturity_inline = MATURITY.search(head) or PAREN_STATE.search(head)
    if maturity_inline:
        required = maturity_value(maturity_inline.group(1))
    for sub in subs:
        if MATURITY.search(sub):
            required = maturity_value(MATURITY.search(sub).group(1))
        elif LOCATION.match(sub):
            location = LOCATION.match(sub).group(1).strip() or "TBD"
        elif REASON.match(sub) and not reason:
            reason = REASON.match(sub).group(1).strip()
    return DeclaredEntry(direction, target_id, name, reason, required, location, heading, raw)


def parse_declarations(text: str) -> Declarations:
    """Read the tracking mode and declared entries of a `_DEPENDENCIES.md` text.

    Only §5.2-form entries are read: a top-level bullet that starts with a
    deliverable ID, with optional `Required maturity:` and `Location:`
    sub-lines. Bullets saying none or TBD, template placeholders and the
    NOT_TRACKED text are not entries. Other bullets and table rows that name a
    deliverable ID are listed as unread; nothing is inferred from prose.
    """
    result = Declarations()
    for section in split_sections(text):
        if section.key == MODE and result.mode == "UNKNOWN":
            found = MODE_VALUE.search("".join(section.lines))
            if found:
                value = found.group(1).upper()
                result.mode = "FULL_GRAPH" if value == "TRACKED" else value
        if section.key not in {UPSTREAM, DOWNSTREAM, DECLARED_LISTS}:
            continue
        direction = DIRECTION_BY_SECTION.get(section.key)
        heading = (section.heading or "").strip()
        for head, subs in _entry_blocks(section.lines):
            parsed = _parse_entry(head, subs, direction, heading)
            if isinstance(parsed, DeclaredEntry):
                result.entries.append(parsed)
            elif isinstance(parsed, str) and ANY_ID.search(parsed):
                result.unread.append(parsed)
    return result


# --- Recorded register: the union (SPEC §5.3) --------------------------------


@dataclass
class RecordedRegister:
    deliverable_id: str
    path: Path | None
    mode: str = "UNKNOWN"
    csv_present: bool = False
    declarations_present: bool = False
    entries: list[DeclaredEntry] = field(default_factory=list)
    rows: list[dict[str, str]] = field(default_factory=list)
    declared_only: list[dict[str, str]] = field(default_factory=list)
    disagreements: list[dict[str, str]] = field(default_factory=list)
    unread: list[str] = field(default_factory=list)

    @property
    def union_rows(self) -> list[dict[str, str]]:
        return self.rows + self.declared_only

    def declared_arcs(self) -> dict[tuple[str, str], list[str]]:
        """Consumer-to-supplier arcs of this deliverable's declared entries, with their stated maturities."""
        arcs: dict[tuple[str, str], list[str]] = {}
        for entry in self.entries:
            item = (
                (self.deliverable_id, entry.target_id)
                if entry.direction == "UPSTREAM"
                else (entry.target_id, self.deliverable_id)
            )
            arcs.setdefault(item, []).append(entry.required_maturity)
        return arcs


def declared_row(deliverable_id: str, entry: DeclaredEntry, ordinal: int) -> dict[str, str]:
    """A synthesized `Origin=DECLARED` row for a declaration that has no CSV row.

    Its fields follow dependency-extract's mirror rows: `SourceRef` is
    `_DEPENDENCIES.md` plus the section heading, the heading supplies the
    `DependencyType` (noted as `type_from=section_heading`), and an entry under
    a legacy informational downstream heading is `IMPLICIT`/`MEDIUM`.
    """
    informational = bool(INFORMATIONAL_HEADING.search(entry.heading))
    return {
        "RegisterSchemaVersion": "v3.1",
        "DependencyID": f"DECLARED-{deliverable_id}-{ordinal:03d}",
        "FromDeliverableID": deliverable_id,
        "DependencyClass": "EXECUTION",
        "AnchorType": "NOT_APPLICABLE",
        "Direction": entry.direction,
        "DependencyType": TYPE_BY_DIRECTION[entry.direction],
        "TargetType": "DELIVERABLE",
        "TargetDeliverableID": entry.target_id,
        "TargetName": entry.target_name,
        "TargetLocation": entry.location,
        "Statement": entry.reason,
        "EvidenceFile": "_DEPENDENCIES.md",
        "SourceRef": f"_DEPENDENCIES.md {entry.heading}".strip(),
        "EvidenceQuote": " ".join(entry.raw.split()[:30]),
        "Explicitness": "IMPLICIT" if informational else "EXPLICIT",
        "RequiredMaturity": entry.required_maturity,
        "SatisfactionStatus": "TBD",
        "Confidence": "MEDIUM" if informational else "HIGH",
        "Origin": "DECLARED",
        "Status": "ACTIVE",
        "Notes": "declared_only=_DEPENDENCIES.md; type_from=section_heading",
    }


def union_register(
    deliverable_id: str,
    csv_rows: list[dict[str, str]],
    declarations: Declarations,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    """Apply the union rule to one deliverable.

    Returns the CSV rows (copies, with a declared required maturity applied
    where the declaration governs), the synthesized rows for declarations
    without an ACTIVE CSV row, and the disagreements found. A declaration whose
    only matching rows are RETIRED still yields a synthesized row (the
    declaration governs), and each retired row is reported as a `Status`
    disagreement so that the revival is visible.
    """
    rows = [dict(row) for row in csv_rows]
    index: dict[tuple[str, str], list[dict[str, str]]] = {}
    retired: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in rows:
        if clean(row.get("DependencyClass")) != "EXECUTION":
            continue
        key = (clean(row.get("Direction")), normalize_id(row.get("TargetDeliverableID", "")))
        status = clean(row.get("Status"))
        if status == "ACTIVE":
            index.setdefault(key, []).append(row)
        elif status == "RETIRED":
            retired.setdefault(key, []).append(row)
    declared_only: list[dict[str, str]] = []
    disagreements: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for entry in declarations.entries:
        key = (entry.direction, entry.target_id)
        if key in seen:
            continue
        seen.add(key)
        matches = index.get(key, [])
        if not matches:
            declared_only.append(declared_row(deliverable_id, entry, len(declared_only) + 1))
            for row in retired.get(key, []):
                disagreements.append({
                    "DeliverableID": deliverable_id,
                    "Direction": entry.direction,
                    "TargetDeliverableID": entry.target_id,
                    "DependencyID": clean(row.get("DependencyID")),
                    "Field": "Status",
                    "Declared": "ACTIVE",
                    "Csv": "RETIRED",
                })
            continue
        if entry.required_maturity == "TBD":
            continue
        for row in matches:
            recorded = clean(row.get("RequiredMaturity"))
            if recorded != entry.required_maturity:
                disagreements.append({
                    "DeliverableID": deliverable_id,
                    "Direction": entry.direction,
                    "TargetDeliverableID": entry.target_id,
                    "DependencyID": clean(row.get("DependencyID")),
                    "Field": "RequiredMaturity",
                    "Declared": entry.required_maturity,
                    "Csv": recorded,
                })
                row["RequiredMaturity"] = entry.required_maturity
    return rows, declared_only, disagreements


def recorded_register(unit: Path, include_declared: bool = True) -> RecordedRegister:
    """The recorded register of one deliverable folder (SPEC §5.3).

    With `include_declared=False` the register is the CSV alone (the earlier
    reading): `_DEPENDENCIES.md` is not read, so the mode stays UNKNOWN.
    """
    register = RecordedRegister(unit_id(unit), unit)
    csv_path = unit / "Dependencies.csv"
    md_path = unit / "_DEPENDENCIES.md"
    csv_rows: list[dict[str, str]] = []
    if csv_path.is_file():
        register.csv_present = True
        _header, csv_rows = read_csv(csv_path)
    if not include_declared:
        register.rows = [dict(row) for row in csv_rows]
        return register
    declarations = Declarations()
    if md_path.is_file():
        register.declarations_present = True
        declarations = parse_declarations(md_path.read_text(encoding="utf-8", errors="replace"))
    register.mode = declarations.mode
    register.entries = list(declarations.entries)
    register.unread = declarations.unread
    register.rows, register.declared_only, register.disagreements = union_register(
        register.deliverable_id, csv_rows, declarations
    )
    return register


def project_registers(execution_root: Path, include_declared: bool = True) -> dict[str, RecordedRegister]:
    """Recorded registers of every live production unit under the execution root."""
    registers: dict[str, RecordedRegister] = {}
    for unit in inventory(execution_root):
        registers.setdefault(unit_id(unit), recorded_register(unit, include_declared))
    return registers


# --- Accepted project DAG (SPEC §5.4) ----------------------------------------


class DagPointerError(ValueError):
    """`_DAG/_LATEST.md` exists but does not resolve to an accepted version."""


@dataclass
class AcceptedDag:
    name: str
    path: Path
    pointer: Path
    nodes: list[dict[str, str]]
    admitted: list[dict[str, str]]
    candidates: list[dict[str, str]]
    excluded: list[dict[str, str]]

    @property
    def node_ids(self) -> set[str]:
        return {normalize_id(row.get("DeliverableID", "")) for row in self.nodes if clean(row.get("DeliverableID"))}


def pointer_target(text: str) -> str | None:
    """The version a `_LATEST.md` names: SPEC §11.2 `Latest: DAG-NNN`, or `Latest DAG artifact: DAG-NNN`."""
    match = POINTER_LINE.search(text)
    return match.group(1) if match else None


def resolve_accepted_dag(execution_root: Path) -> AcceptedDag | None:
    """The accepted current version named by `{EXECUTION_ROOT}/_DAG/_LATEST.md`, or None when there is none."""
    pointer = execution_root / "_DAG" / "_LATEST.md"
    if not pointer.is_file():
        return None
    name = pointer_target(pointer.read_text(encoding="utf-8", errors="replace"))
    if not name:
        raise DagPointerError(f"{pointer}: no `Latest:` line naming a version")
    version = execution_root / "_DAG" / name
    if name.startswith("_") or not (version / "DependencyEdges.csv").is_file() or not (version / "DeliverableNodes.csv").is_file():
        raise DagPointerError(f"{pointer}: {name} is not an accepted version folder with DependencyEdges.csv and DeliverableNodes.csv")
    _header, nodes = read_csv(version / "DeliverableNodes.csv")
    _header, edges = read_csv(version / "DependencyEdges.csv")
    admitted = [row for row in edges if clean(row.get("Status")) == "ACTIVE"]
    candidates = [row for row in edges if clean(row.get("Status")) == "CANDIDATE"]
    if (version / "CandidateEdges.csv").is_file():
        candidates += read_csv(version / "CandidateEdges.csv")[1]
    excluded = read_csv(version / "ExcludedRows.csv")[1] if (version / "ExcludedRows.csv").is_file() else []
    return AcceptedDag(name, version, pointer, nodes, admitted, candidates, excluded)


@dataclass
class Currency:
    result: str
    pending: dict[str, list[str]]
    added_arcs: list[tuple[str, str]]
    removed_arcs: list[tuple[str, str]]
    added_deliverables: list[str]
    removed_deliverables: list[str]

    def as_dict(self) -> dict[str, object]:
        return {
            "result": self.result,
            "dag_pending_count": len(self.pending),
            "dag_pending": {key: self.pending[key] for key in sorted(self.pending)},
            "added_arcs": [list(item) for item in self.added_arcs],
            "removed_arcs": [list(item) for item in self.removed_arcs],
            "added_deliverables": self.added_deliverables,
            "removed_deliverables": self.removed_deliverables,
        }


def check_currency(dag: AcceptedDag, registers: dict[str, RecordedRegister]) -> Currency:
    """Compare local evidence with the accepted version (SPEC §5.4 departure).

    Arcs the version accounts for are its admitted, candidate and excluded
    arcs. A local ACTIVE arc outside them is added. An admitted arc with no
    local ACTIVE row is removed; a candidate arc is removed only when no local
    ACTIVE or CANDIDATE row holds it, since a register may keep a candidate
    as `Status=CANDIDATE`. A deliverable present on one side only is an
    inventory change. Endpoints of added and removed arcs, and the added or
    removed deliverables, are `DAG pending`.
    """
    admitted = {item for item in (arc(row) for row in dag.admitted) if item}
    candidate = {item for item in (arc(row) for row in dag.candidates) if item}
    excluded = {item for item in (arc(row, require_class=False) for row in dag.excluded) if item}
    local: set[tuple[str, str]] = set()
    local_candidate: set[tuple[str, str]] = set()
    for register in registers.values():
        for row in register.union_rows:
            status = clean(row.get("Status"))
            if status not in {"ACTIVE", "CANDIDATE"}:
                continue
            item = arc(row)
            if not item:
                continue
            if status == "ACTIVE":
                local.add(item)
            else:
                local_candidate.add(item)
    added = sorted(local - admitted - candidate - excluded)
    removed = sorted((admitted - local) | (candidate - local - local_candidate))
    version_nodes = dag.node_ids
    local_nodes = set(registers)
    added_nodes = sorted(local_nodes - version_nodes)
    removed_nodes = sorted(version_nodes - local_nodes)
    pending: dict[str, list[str]] = {}
    for consumer, supplier in added:
        for node in (consumer, supplier):
            pending.setdefault(node, []).append(f"arc added: {consumer} -> {supplier}")
    for consumer, supplier in removed:
        for node in (consumer, supplier):
            pending.setdefault(node, []).append(f"arc removed: {consumer} -> {supplier}")
    for node in added_nodes:
        pending.setdefault(node, []).append(f"deliverable not in {dag.name}")
    for node in removed_nodes:
        pending.setdefault(node, []).append(f"deliverable of {dag.name} not found locally")
    result = "DEPARTURE" if pending else "NO_DEPARTURE_FOUND"
    return Currency(result, pending, added, removed, added_nodes, removed_nodes)
