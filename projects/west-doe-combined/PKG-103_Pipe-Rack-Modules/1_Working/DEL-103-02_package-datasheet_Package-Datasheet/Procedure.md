# Procedure — DEL-103-02 Package Datasheet (PKG-103 Pipe Rack Modules)

> Operational document. Describes the steps to **produce / maintain** the Package Datasheet artifact for PKG-103. Operating/using the physical pipe-rack package itself is out of scope here (covered downstream in `DEL-103-03` Construction Work Package and `DEL-103-04` Discipline Production Package).

## Purpose

Standardize how the Package Datasheet for PKG-103 is drafted, source-anchored, cross-checked, and re-issued, so it remains a defensible vendor handoff throughout the EPC lifecycle.

## Prerequisites

| Prerequisite | Detail | Source |
|---|---|---|
| Accepted upstream decomposition snapshot | GATE-07 Final Published 2026-05-24 | `_REFERENCES.md`; `_CONTEXT.md` |
| Deliverable identity and scope | `_CONTEXT.md` populated | `_CONTEXT.md` |
| Authoritative source set | At least one locally accessible reference from `_REFERENCES.md` | DBM Comp & Liquids and DBM Deepcut markdown sources present in `_Sources/` |
| Declared dependencies | `_DEPENDENCIES.md` exists; declared upstream / downstream may be empty (none declared at PREPARATION) | `_DEPENDENCIES.md` |
| Lifecycle state | `_STATUS.md` Current State in `ALLOW_OVERWRITE_STATES` (`OPEN`, `INITIALIZED`) for content overwrite | `_STATUS.md` |
| Skill manifest | `skills/four-documents/SKILL.md` | Reasoning-only skill |

## Steps

1. **Read context (always).**
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
   - Locate the deliverable row in `DELIVERABLE_REGISTER.csv` (row 585) and the parent package row in `PACKAGE_REGISTER.csv`.
   - Verification: identity, scope, and discipline match between `_CONTEXT.md` and the register row.

2. **Open source slices.**
   - Open the locally accessible DBM markdown files in `_Sources/` and isolate slices that mention `pipe rack` / `piperack` / `pipe-rack`, cable tray, heat tracing, grounding, skid-edge, area classification, foundation basis, and grading.
   - For each binary workbook source (`26020-Package_Requirements.docx`, `26020-Packages_Interfaces_4_export.xlsx`), record that text content is not accessible and that dependent attributes shall be marked TBD.

3. **Populate Datasheet.md attributes / conditions / construction.**
   - For each row, cite `SourcePath` + line range or section reference.
   - Where the source does not state a value, mark `TBD`; do not derive numerical values from decomposition prose.
   - Inferences are labeled `ASSUMPTION`.

4. **Populate Specification.md requirements / standards / verification / documentation.**
   - One requirement row per substantive datasheet expectation; each row carries a source basis and a label (FACT / ASSUMPTION / TBD).
   - Standards table records both project DBM variants as accessible and external standards (e.g., API RP 505) with `location TBD` when their text is not present locally.
   - Verification table maps each Req ID to a verification approach.

5. **Populate Guidance.md.**
   - Document purpose, principles, considerations, trade-offs, examples.
   - Maintain the Conflict Table (HRR-compliant) even when empty.

6. **Cross-reference consistency sweep (Pass 2).**
   - Run the table-driven checks in `Specification.md` § Verification against the Datasheet rows.
   - Re-open source slices for any value disagreement; prefer TBD over guessing if not resolvable.
   - Record findings in the run record.

7. **Update `_STATUS.md` (safe-update only).**
   - If state is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.
   - If state is not `OPEN`, do not modify.

8. **Write the run record.**
   - File: `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md`.
   - Capture: pass directive (`P1_P2`), inputs, source slices read, dispositions, status update result, and `RUN_STATUS`.

9. **Reissue trigger.**
   - When any cited DBM source slice changes in the snapshot of record, or when previously inaccessible workbook sources become text-accessible, re-run this procedure under the appropriate `RUN_PASSES` directive.

## Verification

| Check | What confirms success |
|---|---|
| Four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present in `{DELIVERABLE_PATH}`. |
| Default schema sections present | Each document carries the default sections defined in `skills/four-documents/SKILL.md` Step 2. |
| Source-grounded claims | Every non-trivial attribute / requirement row cites a `SourcePath` + section reference or is marked `TBD`. |
| Cross-document consistency | Terminology and values match across all four documents (e.g., voltages, foundation basis, classification default). |
| Conflict Table compliance | `Guidance.md` contains a Conflict Table with the prescribed columns. |
| Status update safety | `_STATUS.md` only advanced when state was `OPEN`; no regression. |
| Run record written | `_run_records/TASK_RUN_*.md` exists with `RUN_STATUS` reported. |
| No out-of-scope writes | No edits to `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_MEMORY.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, or sibling deliverables. |

## Records

| Record | Location |
|---|---|
| Datasheet | `{DELIVERABLE_PATH}/Datasheet.md` |
| Specification | `{DELIVERABLE_PATH}/Specification.md` |
| Guidance (with Conflict Table) | `{DELIVERABLE_PATH}/Guidance.md` |
| Procedure | `{DELIVERABLE_PATH}/Procedure.md` |
| Lifecycle state | `{DELIVERABLE_PATH}/_STATUS.md` |
| Run record | `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md` |
| Source slices read (this run) | Enumerated in `Datasheet.md` § References |
