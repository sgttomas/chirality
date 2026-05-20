#!/usr/bin/env python3
"""ORCHESTRATOR setup for the Chirality App vNext execution workspace."""

from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as dt
import hashlib
import re
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
EXECUTION_ROOT = PROJECT_ROOT / "execution"
DECOMPOSITION_PATH = EXECUTION_ROOT / "_Decomposition" / "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
PARENT_CHIRALITY_ROOT = Path("/Users/ryan/ai-env/projects/chirality")
SCAFFOLDING_ROOT = PARENT_CHIRALITY_ROOT / "tools" / "scaffolding"
VALIDATION_ROOT = PARENT_CHIRALITY_ROOT / "tools" / "validation"
TODAY = dt.date.today().isoformat()


@dataclasses.dataclass(frozen=True)
class Package:
    package_id: str
    name: str
    scope_description: str
    inclusion_criteria: str
    exclusions: str

    @property
    def label(self) -> str:
        return safe_label(self.name)

    @property
    def folder(self) -> Path:
        return EXECUTION_ROOT / f"{self.package_id}_{self.label}"


@dataclasses.dataclass(frozen=True)
class Deliverable:
    deliverable_id: str
    name: str
    responsible_party: str
    type: str
    description: str
    anticipated_artifacts: str
    covers_scope_items: str
    supports_objectives: str
    context_envelope: str
    context_envelope_notes: str
    package_id: str
    package_name: str

    @property
    def label(self) -> str:
        return safe_label(self.name)

    @property
    def folder(self) -> Path:
        package = package_by_id[self.package_id]
        return package.folder / "1_Working" / f"{self.deliverable_id}_{self.label}"


package_by_id: dict[str, Package] = {}


def safe_label(value: str) -> str:
    clean = re.sub(r"`([^`]+)`", r"\1", value)
    clean = re.sub(r"[^A-Za-z0-9]+", "_", clean).strip("_")
    clean = re.sub(r"_+", "_", clean)
    return clean[:96] or "Unnamed"


def split_markdown_row(line: str) -> list[str]:
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    in_code = False
    for char in line.strip():
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            current.append(char)
            escaped = True
            continue
        if char == "`":
            in_code = not in_code
            current.append(char)
            continue
        if char == "|" and not in_code:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    cells.append("".join(current).strip())
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def parse_table_after_heading(text: str, heading: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    table_lines: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("|"):
            table_lines.append(line)
        elif table_lines:
            break
    return parse_markdown_table(table_lines)


def parse_markdown_table(lines: list[str]) -> list[dict[str, str]]:
    rows = [split_markdown_row(line) for line in lines if line.startswith("|")]
    rows = [row for row in rows if not is_separator_row(row)]
    if not rows:
        return []
    header = rows[0]
    records: list[dict[str, str]] = []
    for row in rows[1:]:
        if len(row) < len(header):
            row.extend([""] * (len(header) - len(row)))
        records.append(dict(zip(header, row)))
    return records


def parse_packages(text: str) -> list[Package]:
    packages = []
    for row in parse_table_after_heading(text, "## 7. Packages"):
        packages.append(
            Package(
                package_id=row["PackageID"],
                name=row["Name"],
                scope_description=row["ScopeDescription"],
                inclusion_criteria=row["InclusionCriteria"],
                exclusions=row["Exclusions"],
            )
        )
    return packages


def parse_deliverables(text: str) -> list[Deliverable]:
    lines = text.splitlines()
    in_deliverables = False
    current_package_id = ""
    current_package_name = ""
    deliverables: list[Deliverable] = []
    buffer: list[str] = []

    def flush_buffer() -> None:
        nonlocal buffer
        if not buffer:
            return
        for row in parse_markdown_table(buffer):
            deliverables.append(
                Deliverable(
                    deliverable_id=row["DeliverableID"],
                    name=row["Name"],
                    responsible_party=row["ResponsibleParty"],
                    type=row["Type"],
                    description=row["Description"],
                    anticipated_artifacts=row["AnticipatedArtifacts"],
                    covers_scope_items=row["CoversScopeItems"],
                    supports_objectives=row["SupportsObjectives"],
                    context_envelope=row["ContextEnvelope"],
                    context_envelope_notes=row["ContextEnvelopeNotes"],
                    package_id=current_package_id,
                    package_name=current_package_name,
                )
            )
        buffer = []

    for line in lines:
        if line.strip() == "## 8. Deliverables":
            in_deliverables = True
            continue
        if in_deliverables and line.startswith("## 9. "):
            flush_buffer()
            break
        if not in_deliverables:
            continue
        package_match = re.match(r"^###\s+(PKG-\d{2})\s+(.+)$", line)
        if package_match:
            flush_buffer()
            current_package_id = package_match.group(1)
            current_package_name = package_match.group(2)
            continue
        if line.startswith("|"):
            buffer.append(line)
        elif buffer:
            flush_buffer()
    return deliverables


def run_tool(*args: str) -> None:
    subprocess.run(args, cwd=PROJECT_ROOT, check=True, stdout=subprocess.DEVNULL)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def source_refs() -> list[tuple[str, str, str, str]]:
    return [
        ("REF-001", "docs/DIRECTIVE.md", "Intent, authority, professional boundaries", "dee943d3d87bf261bfd393c4dd9d474c01165a09cf0df94207361a4efa014d82"),
        ("REF-002", "docs/CONTRACT.md", "Invariants and enforcement surfaces", "735a85004c157f30c3a48c553b82d543e43bae0272bebf47c7273a41f8e1e8dc"),
        ("REF-003", "docs/SPEC.md", "Physical structures, runtime mechanics, API/file contracts", "ba7a62b2383293b54d059a60ce407aa3acdc3043afe61b6932958442e86343fb"),
        ("REF-004", "docs/TYPES.md", "Vocabulary, identifiers, enums, type targets", "f5ebe6453a871980a0c1fd3ff11c0132048ce4e765a9c23f48968648b133ebc2"),
        ("REF-005", "docs/PLAN.md", "Roadmap and implementation sequencing", "4a8af7de5f6bfdf757cd6a73834c1fa00686b4581d27e13a191735a0b05e467b"),
        ("REF-006", "docs/PRD.md", "Product requirements, runtime direction, and approved vNext scope", "86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34"),
        ("REF-007", "/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md", "Decomposition method and gate protocol", "4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab"),
    ]


def resolve_ref_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return PROJECT_ROOT / candidate


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_audit_rows() -> list[dict[str, str]]:
    rows = []
    for ref_id, path, role, expected in source_refs():
        resolved = resolve_ref_path(path)
        if not resolved.exists():
            actual = "MISSING"
            status = "MISSING"
        else:
            actual = sha256_file(resolved)
            status = "MATCH" if actual == expected else "HASH_MISMATCH"
        rows.append(
            {
                "RefID": ref_id,
                "Path": path,
                "Role": role,
                "ExpectedSHA256": expected,
                "ActualSHA256": actual,
                "Status": status,
            }
        )
    return rows


def source_audit_md() -> str:
    rows = "\n".join(
        f"| {row['RefID']} | `{row['Path']}` | {row['Status']} | `{row['ExpectedSHA256']}` | `{row['ActualSHA256']}` |"
        for row in source_audit_rows()
    )
    return f"""# Source Hash Audit

**Generated:** {TODAY}
**Decomposition:** `{DECOMPOSITION_PATH.relative_to(PROJECT_ROOT)}`

| RefID | Path | Status | ExpectedSHA256 | ActualSHA256 |
|---|---|---|---|---|
{rows}

## Rule

Downstream TASK runs must treat `HASH_MISMATCH` rows as source-state warnings. Do not silently replace accepted decomposition truth with changed source text; surface the discrepancy for human ruling when it affects deliverable content.
"""


def context_md(package: Package, deliverable: Deliverable) -> str:
    return f"""# Context: {deliverable.deliverable_id} {deliverable.name}

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `{DECOMPOSITION_PATH.relative_to(PROJECT_ROOT)}` |
| PackageID | {package.package_id} |
| PackageName | {package.name} |
| DeliverableID | {deliverable.deliverable_id} |
| DeliverableName | {deliverable.name} |
| ResponsibleParty | {deliverable.responsible_party} |
| Type | {deliverable.type} |
| ContextEnvelope | {deliverable.context_envelope} |

## Package Scope

**ScopeDescription:** {package.scope_description}

**InclusionCriteria:** {package.inclusion_criteria}

**Exclusions:** {package.exclusions}

## Deliverable Scope

{deliverable.description}

## Anticipated Artifacts

{deliverable.anticipated_artifacts}

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | {deliverable.covers_scope_items} |
| SupportsObjectives | {deliverable.supports_objectives} |
| ContextEnvelopeNotes | {deliverable.context_envelope_notes} |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
"""


def references_md(deliverable: Deliverable) -> str:
    rows = "\n".join(
        f"| {row['RefID']} | `{row['Path']}` | {row['Role']} | `{row['ExpectedSHA256']}` | `{row['ActualSHA256']}` | {row['Status']} |"
        for row in source_audit_rows()
    )
    return f"""# References: {deliverable.deliverable_id} {deliverable.name}

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
{rows}

## Decomposition Entry

- Decomposition: `{DECOMPOSITION_PATH.relative_to(PROJECT_ROOT)}`
- DeliverableID: `{deliverable.deliverable_id}`
- PackageID: `{deliverable.package_id}`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
"""


def dependencies_md(deliverable: Deliverable) -> str:
    return f"""# Dependencies: {deliverable.deliverable_id} {deliverable.name}

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring, semantic matrix generation, lens register generation, and P3 enrichment. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on {TODAY}.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
"""


def semantic_stub(deliverable: Deliverable) -> str:
    return f"""# Semantic Lens: {deliverable.deliverable_id} {deliverable.name}

Status: NOT_GENERATED

Run `TASK + semantic-matrix-build` after the four-document kit exists for this SOFTWARE deliverable.
"""


def status_md(deliverable: Deliverable) -> str:
    return f"""# Status: {deliverable.deliverable_id}

**Current State:** OPEN
**Last Updated:** {TODAY}

## History

- {TODAY} - State set to OPEN (PREPARATION)
"""


def coordination_md() -> str:
    return f"""# Coordination Record

**Representation:** Full graph
**Dependency tracking mode:** FULL_GRAPH
**External schedule / coordination artifact:** `docs/PLAN.md`
**Default maturity threshold (if computing blockers):** SEMANTIC_READY
**Dependency graph source:** Post-enrichment `TASK + dependency-extract`
**Decomposition authority:** `{DECOMPOSITION_PATH.relative_to(PROJECT_ROOT)}`
**Recorded:** {TODAY}

## Human Rulings

- Use v3.2 as the SOFTWARE_DECOMP working surface.
- Use FULL_GRAPH dependency tracking.
- Treat upstream dependencies as satisfied only when the upstream deliverable is `SEMANTIC_READY`.
- Determine dependencies only after four-document authoring, semantic lensing, and enrichment.

## Reporting Rule

ORCHESTRATOR may report lifecycle state immediately. It must not compute blocked/available state until dependency extraction has produced valid `Dependencies.csv` registers and the merged FULL_GRAPH is acyclic.
"""


def next_instance_prompt() -> str:
    return f"""# NEXT INSTANCE PROMPT - Chirality App vNext

Adopt ORCHESTRATOR when initializing or scanning the workspace.

## Startup Read List

1. `execution/_Coordination/_COORDINATION.md`
2. `execution/_Coordination/NEXT_INSTANCE_STATE.md`
3. `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
4. `docs/PLAN.md`
5. Relevant deliverable-local `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md`

## Operating Invariants

- v3.2 SOFTWARE_DECOMP is the active decomposition authority until a later human ruling replaces it.
- Packages are flat work domains, not phases.
- Deliverables are the bounded execution units.
- Coordination mode is FULL_GRAPH with `SEMANTIC_READY` as the dependency satisfaction threshold.
- Dependency blockers are advisory and must be computed only from accepted dependency registers.
- R0/R1 runtime deliverables precede R2+ capability expansion.
- Read tools and read MCP exposure precede write/edit/bash.
- Domain engine execution, remote MCP, plugins, shipped bypass, non-macOS packaging, and retired PKG-08 hardening scope require governed amendment before implementation.

## Control Loop

1. ORCHESTRATOR scans lifecycle state and dependency-register readiness.
2. TASK executes one deliverable at a time with the selected skill and sealed write scope.
3. For setup, run `four-documents` P1/P2, `semantic-matrix-build`, `lens-register`, then `four-documents` P3.
4. After P3 enrichment reaches `SEMANTIC_READY`, run `dependency-extract`.
5. Validate touched artifacts before computing graph state.
6. Hand coherent work to CHANGE only after human approval gates are satisfied.

## TASK Dispatch Defaults

- `DECOMP_VARIANT=SOFTWARE`
- `DECOMPOSITION_REF={DECOMPOSITION_PATH}`
- `ALLOW_OVERWRITE_STATES=OPEN,INITIALIZED,SEMANTIC_READY`
- one deliverable folder per TASK invocation

## Starter Prompt

Read `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and `execution/_Coordination/NEXT_INSTANCE_STATE.md`, adopt ORCHESTRATOR, scan the filesystem-grounded state, and propose the next gated action without inventing dependency blockers.
"""


def next_instance_state(packages: list[Package], deliverables: list[Deliverable]) -> str:
    package_rows = "\n".join(f"| {pkg.package_id} | {pkg.name} | `{pkg.folder.relative_to(PROJECT_ROOT)}` |" for pkg in packages)
    immediate = "\n".join(
        [
            "1. Run TASK + `four-documents` with `RUN_PASSES=P1_P2` for selected deliverables.",
            "2. Validate generated four-document kits before semantic matrix generation.",
            "3. Run TASK + `semantic-matrix-build`, then `lens-register`, then `four-documents` P3.",
            "4. Run TASK + `dependency-extract` only after enrichment is complete.",
        ]
    )
    mismatches = [row for row in source_audit_rows() if row["Status"] != "MATCH"]
    data_quality = "No source hash mismatches detected."
    if mismatches:
        data_quality = "; ".join(f"{row['RefID']} {row['Path']}={row['Status']}" for row in mismatches)
    return f"""# NEXT INSTANCE STATE - Chirality App vNext

**Last Updated:** {TODAY}
**Updated By:** ORCHESTRATOR

## Current Pointers

| Artifact | Path |
|---|---|
| Coordination policy | `execution/_Coordination/_COORDINATION.md` |
| Stable startup prompt | `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` |
| Decomposition authority | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Source corpus | `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md` |

## Current Program State

| Metric | Value |
|---|---:|
| Packages scaffolded | {len(packages)} |
| Deliverables scaffolded | {len(deliverables)} |
| OPEN | {len(deliverables)} |
| INITIALIZED | 0 |
| SEMANTIC_READY | 0 |
| IN_PROGRESS | 0 |
| CHECKING | 0 |
| ISSUED | 0 |

## Data-Quality Notes

{data_quality}

## Package Folders

| PackageID | Name | Path |
|---|---|---|
{package_rows}

## Active Human Rulings

- Decomposition authority: v3.2 SOFTWARE_DECOMP.
- Coordination representation: FULL_GRAPH.
- Dependency satisfaction threshold: SEMANTIC_READY.
- Dependency extraction is post-enrichment, not pre-scaffold.

## Immediate Next Actions

{immediate}

## Handoff Payload

- Stable invariant instructions: `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- Mutable state and queue: this file
- Deliverable-local continuity: `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- Dependency state: pending post-enrichment extraction

## Update Protocol

WORKING_ITEMS or TASK handoff should update this file when lifecycle distribution, active blockers, or immediate next actions change. ORCHESTRATOR should update it only when explicitly performing a scan or setup-state refresh.
"""


def task_dispatch_plan(deliverables: list[Deliverable]) -> str:
    rows = "\n".join(
        f"| {item.deliverable_id} | {item.package_id} | `{item.folder.relative_to(PROJECT_ROOT)}` | OPEN | P1_P2 pending | semantic pending | lens pending | P3 pending | dependency-extract pending |"
        for item in deliverables
    )
    return f"""# TASK Dispatch Plan

**Generated:** {TODAY}
**Variant:** SOFTWARE_DECOMP
**Decomposition:** `{DECOMPOSITION_PATH.relative_to(PROJECT_ROOT)}`

## Phase Order

1. `TASK + four-documents`, `RUN_PASSES=P1_P2`
2. Validate four-document kit presence and status transition
3. `TASK + semantic-matrix-build`
4. Validate `_SEMANTIC.md`
5. `TASK + lens-register`
6. Validate `_SEMANTIC_LENSING.md`
7. `TASK + four-documents`, `RUN_PASSES=P3_ONLY`
8. Validate P3 disposition and `SEMANTIC_READY` state
9. `TASK + dependency-extract`
10. Validate `Dependencies.csv` v3.1 and merged graph acyclicity

## Dispatch Queue

| DeliverableID | PackageID | ScopePath | CurrentState | FourDocs | Semantic | Lens | P3 | Dependencies |
|---|---|---|---|---|---|---|---|---|
{rows}
"""


def init_md(packages: list[Package], deliverables: list[Deliverable]) -> str:
    return f"""# Chirality App vNext Execution Init

**Created:** {TODAY}
**Created By:** ORCHESTRATOR
**Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Decomposition Variant:** SOFTWARE_DECOMP
**Package Count:** {len(packages)}
**Deliverable Count:** {len(deliverables)}

## Coordination

- Representation: FULL_GRAPH
- Dependency satisfaction threshold: SEMANTIC_READY
- Dependency extraction phase: after four-doc authoring, semantic lensing, and enrichment

## Source Corpus

- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/PLAN.md`
- `docs/PRD.md`

See `execution/_Sources/SOURCE_HASH_AUDIT.md` for expected-vs-actual source hashes.
"""


def scaffold(packages: list[Package], deliverables: list[Deliverable]) -> None:
    for root_name in ["_Coordination", "_Sources"]:
        run_tool(str(SCAFFOLDING_ROOT / "scaffold_tool_root.sh"), str(EXECUTION_ROOT), root_name)

    for package in packages:
        run_tool(str(SCAFFOLDING_ROOT / "scaffold_package.sh"), str(EXECUTION_ROOT), package.package_id, package.label)

    for deliverable in deliverables:
        package = package_by_id[deliverable.package_id]
        run_tool(
            str(SCAFFOLDING_ROOT / "scaffold_deliverable.sh"),
            str(package.folder / "1_Working"),
            deliverable.deliverable_id,
            deliverable.label,
        )
        run_tool(str(SCAFFOLDING_ROOT / "write_status.sh"), str(deliverable.folder), "OPEN", "PREPARATION")
        write_file(deliverable.folder / "_STATUS.md", status_md(deliverable))
        write_file(deliverable.folder / "_CONTEXT.md", context_md(package, deliverable))
        write_file(deliverable.folder / "_REFERENCES.md", references_md(deliverable))
        write_file(deliverable.folder / "_DEPENDENCIES.md", dependencies_md(deliverable))
        write_file(deliverable.folder / "_SEMANTIC.md", semantic_stub(deliverable))

    write_file(EXECUTION_ROOT / "INIT.md", init_md(packages, deliverables))
    write_file(EXECUTION_ROOT / "_Sources" / "SOURCE_HASH_AUDIT.md", source_audit_md())
    write_file(EXECUTION_ROOT / "_Coordination" / "_COORDINATION.md", coordination_md())
    write_file(EXECUTION_ROOT / "_Coordination" / "NEXT_INSTANCE_PROMPT.md", next_instance_prompt())
    write_file(EXECUTION_ROOT / "_Coordination" / "NEXT_INSTANCE_STATE.md", next_instance_state(packages, deliverables))
    write_file(EXECUTION_ROOT / "_Coordination" / "TASK_DISPATCH_PLAN.md", task_dispatch_plan(deliverables))


def validate(packages: list[Package], deliverables: list[Deliverable]) -> None:
    missing_packages = [pkg.folder for pkg in packages if not pkg.folder.is_dir()]
    if missing_packages:
        raise SystemExit(f"Missing package folders: {missing_packages}")
    missing_deliverables = [item.folder for item in deliverables if not item.folder.is_dir()]
    if missing_deliverables:
        raise SystemExit(f"Missing deliverable folders: {missing_deliverables}")
    for item in deliverables:
        run_tool(str(VALIDATION_ROOT / "check_min_viable_fileset.sh"), str(item.folder))

    status_counts: dict[str, int] = {}
    for item in deliverables:
        status_text = (item.folder / "_STATUS.md").read_text(encoding="utf-8")
        match = re.search(r"^\*\*Current State:\*\*\s+(\S+)", status_text, flags=re.MULTILINE)
        state = match.group(1) if match else "UNKNOWN"
        status_counts[state] = status_counts.get(state, 0) + 1

    if status_counts != {"OPEN": len(deliverables)}:
        raise SystemExit(f"Unexpected lifecycle distribution after scaffold: {status_counts}")

    print(f"PACKAGES={len(packages)}")
    print(f"DELIVERABLES={len(deliverables)}")
    print(f"STATUS_COUNTS={status_counts}")


def write_manifest(packages: list[Package], deliverables: list[Deliverable]) -> None:
    manifest_path = EXECUTION_ROOT / "_Coordination" / "WORKSPACE_MANIFEST.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "PackageID",
                "PackageName",
                "PackagePath",
                "DeliverableID",
                "DeliverableName",
                "DeliverablePath",
                "Type",
                "ContextEnvelope",
                "Status",
            ],
        )
        writer.writeheader()
        for item in deliverables:
            package = package_by_id[item.package_id]
            writer.writerow(
                {
                    "PackageID": package.package_id,
                    "PackageName": package.name,
                    "PackagePath": str(package.folder.relative_to(PROJECT_ROOT)),
                    "DeliverableID": item.deliverable_id,
                    "DeliverableName": item.name,
                    "DeliverablePath": str(item.folder.relative_to(PROJECT_ROOT)),
                    "Type": item.type,
                    "ContextEnvelope": item.context_envelope,
                    "Status": "OPEN",
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    text = DECOMPOSITION_PATH.read_text(encoding="utf-8")
    packages = parse_packages(text)
    package_by_id.update({package.package_id: package for package in packages})
    deliverables = parse_deliverables(text)

    if len(packages) != 10:
        raise SystemExit(f"Expected 10 packages, parsed {len(packages)}")
    if len(deliverables) != 51:
        raise SystemExit(f"Expected 51 deliverables, parsed {len(deliverables)}")

    if not args.validate_only:
        scaffold(packages, deliverables)
        write_manifest(packages, deliverables)
    validate(packages, deliverables)


if __name__ == "__main__":
    main()
