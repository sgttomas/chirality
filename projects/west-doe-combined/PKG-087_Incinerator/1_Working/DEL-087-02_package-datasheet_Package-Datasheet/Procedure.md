# Procedure: DEL-087-02 — PKG-087 Incinerator Package Datasheet

## Purpose

Operational steps to **produce, verify, and maintain** the PKG-087 Incinerator Package Datasheet (`Datasheet.md`) so it satisfies the requirements in `Specification.md` and is fit for use as the Gate 5 EPC handoff document.

This procedure describes how to author the datasheet within the deliverable folder. It is not a procedure for operating the field incinerator package.

## Prerequisites

1. Deliverable-local truth set is initialized in `{DELIVERABLE_PATH}`:
   - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` are present (PREPARATION seeded fileset).
2. Accepted decomposition snapshot is reachable at the path recorded in `_REFERENCES.md` (Gate 7 final published PROJECT_DECOMP snapshot 2026-05-24).
3. Authoritative source `26020-Package_Requirements.docx` heading 40 is locally accessible (extractable via `textutil` or equivalent) under `_Sources/`.
4. Supporting source `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` is locally accessible under `_Sources/`.
5. The RFQ Source Basis `Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx` and `26020-Packages_Interfaces.3.xlsx` row 64 are EITHER (a) accessible — in which case dependent fields are filled from source — OR (b) known to be inaccessible — in which case dependent fields are carried as `location TBD`.
6. `_STATUS.md` Current State is in `ALLOW_OVERWRITE_STATES` (per brief: `OPEN, INITIALIZED`). If not, abort and return `SKIPPED_PROTECT_HUMAN_WORK`.
7. No declared upstream dependencies block this work (`_DEPENDENCIES.md` declares none).

## Steps

### S1 — Load context and source set

1. Read `_CONTEXT.md` and extract Identification fields verbatim.
2. Read the deliverable row in `DELIVERABLE_REGISTER.csv` (DEL-087-02) and the package row in `PACKAGE_REGISTER.csv` (PKG-087) from the Gate 7 snapshot.
3. Read `_REFERENCES.md` to enumerate authoritative source materials.
4. Extract the heading 40 slice from `26020-Package_Requirements.docx` (Location/Status, Source Basis, Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables).
5. Read DBM `3-25_Comp_and_Liquids_DBM.md` slices that mention "incinerator", "spent caustic", "caustic regen", and the Exclusions / Emissions / Inter-facility Interfaces sections.
6. Read `_DEPENDENCIES.md`. Treat only declared upstream/downstream lists as constraints (none declared here).

### S2 — Establish DOMAIN

1. Confirm discipline = Mechanical (from `_CONTEXT.md`).
2. Confirm deliverable type = EPC Package Datasheet (from `_CONTEXT.md`).
3. Do not assert standards (NFPA, API, NACE) that the source slice does not state for this package.

### S3 — Establish TASK

1. Identify the four major package items by tag: `FL-6920-1`, `V-6900-1`, `P-6900-1`, `B-6920-1`.
2. Identify process function (vapours from spent caustic tank and caustic regeneration column overheads).
3. Identify EPC-by-others items (DCS, foundations, MCC electrical supply).
4. Identify shared-interface allocation context (DBM Exclusions / Emissions / Inter-facility Interfaces).

### S4 — Generate `Datasheet.md`

1. Populate Identification table from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row PKG-087.
2. Populate Attributes table from heading 40 Basic Scope, Major Included Equipment, Scope Notes, plus DBM allocation language.
3. Populate Conditions table from heading 40 Major Included Equipment and Scope Notes (Design conditions, Operating conditions, Driver). Mark Appendix A fluid conditions as `location TBD`.
4. Populate Construction table from heading 40 Major Included Equipment and Scope Notes (per-tag rows; by-others rows; building row; motor-starting row).
5. Populate Applicable Interface Types from PACKAGE_REGISTER.csv row PKG-087 and corroborate against heading 40 Physical Interface Summary. Record the Building HVAC / Services discrepancy as a pointer to the Conflict Table in `Guidance.md`.
6. Populate References block (primary source, supporting source, decomposition rows, deliverable metadata files, TBD/inaccessible pointers).

### S5 — Generate `Specification.md`

1. Write Scope (in scope, out of scope).
2. Write R1-R11 requirements, each citing the source slice that justifies it.
3. Write Standards section noting that no package-specific standards are quoted in source.
4. Write Verification table mapping R1-R11 to checks on `Datasheet.md`.
5. Write Documentation list from `_CONTEXT.md` Anticipated Artifacts.

### S6 — Generate `Guidance.md`

1. Write Purpose tied to the Gate 5 EPC handoff role.
2. Write Principles (source authority, two scopes, mark unknowns, shared-interface honesty, interface evidence first-class).
3. Write Considerations (process function, stack relief capacity, motor starting, EPC-by-others, cross-package coupling, self-framing building).
4. Write Trade-offs (single-train vs. spare; preliminary vs. final flow; VFD vs. soft start).
5. Write Examples (none transcribable from accessible slice — say so).
6. Write Conflict Table with C-01 (HVAC discrepancy), C-02 (stack relief wording), C-03 (spare philosophy inference), C-04 (open service split).

### S7 — Generate `Procedure.md`

1. Write Purpose distinguishing this as an authoring procedure, not an operating procedure for the field incinerator.
2. Write Prerequisites that lock in source accessibility and the `_STATUS.md` overwrite gate.
3. Write Steps S1-S7 (this section).
4. Write Verification checklist tied to QA expectations.
5. Write Records list (run record under `_run_records/`; `_STATUS.md` history line).

### S8 — Cross-reference consistency sweep (Pass 2)

Run the Step 5 four-documents consistency checks:

| Check | Result |
|---|---|
| Datasheet ↔ Specification: each requirement is reflected by a Datasheet table row or cell | Confirm before closing the run. |
| Specification ↔ Guidance: each requirement has rationale where appropriate | Confirm. |
| Specification ↔ Procedure: each requirement has a verification hook in Procedure or in Specification Verification | Confirm. |
| Terminology: tag IDs (`FL-6920-1`, `V-6900-1`, `P-6900-1`, `B-6920-1`), "spent caustic", "caustic regeneration column overheads", "shared-interface incinerator" used consistently | Confirm. |
| Values: design ambient, KO drum design P/T/CA, incinerator operating P, throughput, transfer-pump capacity, motor ratings — all match source verbatim across documents | Confirm. |

Resolve any inconsistency by reopening the heading 40 slice; do not invent reconciliations.

### S9 — Status update

If `_STATUS.md` Current State is `OPEN`, set it to `INITIALIZED` (Pass 1/2 ran). If state is not `OPEN`, do not modify.

## Verification

1. All four documents exist after the run (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`).
2. Default schema sections are present:
   - Datasheet: Identification, Attributes, Conditions, Construction, References.
   - Specification: Scope, Requirements, Standards, Verification, Documentation.
   - Guidance: Purpose, Principles, Considerations, Trade-offs, Examples (Conflict Table appended where conflicts exist).
   - Procedure: Purpose, Prerequisites, Steps, Verification, Records.
3. Every substantive Datasheet cell cites a source (`_CONTEXT.md`, `PACKAGE_REGISTER.csv`, heading 40, DBM section) or is marked `TBD` / `location TBD`.
4. Conflict Table records C-01 through C-04.
5. `_STATUS.md` either moved `OPEN -> INITIALIZED` (with a history line) or is unchanged (with reason recorded in the run record).

## Records

- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` capturing input echo, resolved state, tools used (`/usr/bin/textutil` for docx extraction is acceptable but invoked operationally outside the TASK-consumed allowed-tools contract), outputs produced, missing items, conflicts, and applied changes.
- `_STATUS.md` history line recording the `OPEN -> INITIALIZED` transition by `TASK+four-documents` when applicable.
- No modifications to `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, or `MEMORY.md` are produced by this procedure.
