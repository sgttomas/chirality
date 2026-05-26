# Procedure: DEL-048-01 — Scope of Work, PKG-048 Inlet / Sales Compressors

This procedure describes the steps to **produce** the Scope of Work artifact for PKG-048 (EPC Integrator deliverable). Operating procedures for the physical compressor packages are out of scope; those are the Package Vendor's documentation.

## Prerequisites

- Read deliverable-local context: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
  Source: deliverable folder.
- Read the decomposition register rows for the deliverable and parent package:
  - `DELIVERABLE_REGISTER.csv` row `DEL-048-01_scope-of-work`.
  - `PACKAGE_REGISTER.csv` row `PKG-048`.
  Source: GATE-07 snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Read source slices:
  - `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01 (Scope Boundary), SEC-05 (Compression and Acid Gas Handling Basis — Inlet/Sales Compressor Basis).
  - `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 (cross-reference for 03-25 sour gas feed export).
  - Workbook Packages row 65 (xlsx; location TBD — convert to text before extraction).
  - 26020-Package_Requirements.docx package heading 3 (.docx; location TBD — convert to text before extraction).
  - 26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx (RFQ; location TBD — convert to text before extraction).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` at PREPARATION.
  Source: `_DEPENDENCIES.md`.

## Steps

### Step 1 — Establish deliverable identity

1.1 Capture deliverable ID, name, parent package, discipline, type, responsible party from `_CONTEXT.md` into Datasheet "Identification."
1.2 Cross-check against `DELIVERABLE_REGISTER.csv` row `DEL-048-01_scope-of-work`.
1.3 Record covered scope items (`SOW-0115`..`SOW-0118`) and supported objectives (`OBJ-001`, `OBJ-003`..`OBJ-010`, marked ASSUMPTION under PACKAGE_HEURISTIC) in Datasheet.

### Step 2 — Extract tagged equipment and package identity

2.1 Populate Datasheet "Attributes" — Tagged Equipment / Package Identity from `PACKAGE_REGISTER.csv` (Equipment ID `26020-01-PT-12-003`; per-package count 5; multi-service configuration) and DBM-Deepcut SEC-05 (frame, driver, start method).
2.2 Where multiple values appear in source, record both and flag the conflict in `Guidance.md` Conflict Table.

### Step 3 — Capture design conditions

3.1 Populate Datasheet "Inlet Service Conditions" and "Sales Service Conditions" from the DBM-Deepcut SEC-05 design-condition table.
3.2 For each parameter, transcribe value and units exactly; mark TBD/TBC where source already does so.

### Step 4 — Define process boundaries and interfaces

4.1 Capture process boundaries (inlet/discharge of each service) into Specification R-14 and Datasheet "Conditions / Process Boundaries."
4.2 Capture applicable interface types verbatim from `PACKAGE_REGISTER.csv` (Applicable interface types) into Specification R-13.

### Step 5 — Write requirements (R-1..R-14)

5.1 Draft each requirement grounded in DBM-Deepcut SEC-05 / `PACKAGE_REGISTER.csv` Scope; cite source after each.
5.2 Where source values are TBD or conflicting, write the requirement to the supported-basis value and reference the Conflict Table.

### Step 6 — Standards list

6.1 Record only standards explicitly cited in accessed source slices.
6.2 Mark all other commonly-applicable standards (API 11P, NEMA MG 1, area-classification codes) as ASSUMPTION with location TBD.
6.3 Flag the unread `26020-Package_Requirements.docx` heading 3 as a known source of standards to extract in a future pass.

### Step 7 — Verification mapping

7.1 For each requirement, write a one-line verification approach into Specification "Verification" table.
7.2 Reference Conflict Table IDs where verification depends on a human ruling.

### Step 8 — Responsibility assignment record

8.1 Record Package Vendor vs EPC Integrator responsibilities verbatim from `PACKAGE_REGISTER.csv` (Responsibility) into Specification "Responsibility Assignment."
8.2 Mark commissioning ownership as ASSUMPTION pending explicit source.

### Step 9 — Guidance narrative

9.1 Write Purpose, Principles, Considerations, Trade-offs grounded in DBM-Deepcut SEC-05 Compression Configuration rationale.
9.2 Populate Conflict Table with every cross-source disagreement found in Steps 2-6.

### Step 10 — Cross-document consistency check (Pass 2)

10.1 Verify entities/values consistent across Datasheet, Specification, Guidance, Procedure (capacity, pressure, frame, driver, sparing).
10.2 Verify all Specification requirements have a verification entry.
10.3 Verify all Guidance Conflict Table rows reference Specification and Datasheet sections they impact.
10.4 Where inconsistency cannot be resolved from source, add a row to the Conflict Table rather than guessing.

### Step 11 — Status update

11.1 If `_STATUS.md` current state is `OPEN`, transition to `INITIALIZED` recording actor `TASK+four-documents`.
11.2 If state is not `OPEN`, do not modify `_STATUS.md`.
   Source: skill Step 7.

## Verification

| Check | Acceptance |
|---|---|
| Datasheet identification matches `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` | Field-by-field equality. |
| All Specification requirements (R-1..R-14) cite source | Every R-x has a "Source:" line referencing DBM-Deepcut SEC-05, PACKAGE_REGISTER.csv, or _CONTEXT.md. |
| All TBDs in source preserved as TBD in this deliverable | No silent resolution of source TBDs. |
| Conflict Table includes CT-1 through CT-7 with PROPOSAL and TBD ruling | Present in `Guidance.md`. |
| Cross-document terminology consistency | "Inlet service" and "Sales service" used identically across all four documents. |
| Status update | `_STATUS.md` shows `Current State: INITIALIZED` with history line referencing `TASK+four-documents`. |
| No edits outside deliverable folder | Confirmed by run record `## Applied Changes`. |

## Records

The following artifacts shall result from this procedure and live in the deliverable folder:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md` (including Conflict Table)
- `Procedure.md`
- `_STATUS.md` updated to `INITIALIZED`
- `_run_records/TASK_RUN_<timestamp>.md`

Source: skill four-documents Step 4-7; this deliverable's `_CONTEXT.md` Anticipated Artifacts.
