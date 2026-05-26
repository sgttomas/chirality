# Procedure — DEL-082-02 Package Datasheet (Flare KO Drum, Low Pressure, 3-25)

## Purpose

Procedure to produce, verify, and issue the EPC Integrator Package Datasheet for PKG-082 (Flare KO Drum, Low Pressure, V-3900-2 with transfer pump P-3900-2). The procedure covers the steps to draft the datasheet from accessible source material, capture `TBD` items, and route the datasheet for downstream vendor engineering use.

## Prerequisites

- Read access to the deliverable folder `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Read access to the 3-25 DBM at `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (accessible authoritative source).
- Visibility into Gate 7 PROJECT_DECOMP snapshot (`_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`) including the `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- (When available) `26020-Package_Requirements.docx` package heading 35 and `26020-Packages_Interfaces_4_export.xlsx` Packages row 56 — currently `TBD` (not accessible as parsed text in workspace).
- (When available) W242510-PRC-REP-000003-001 (Plant Shutdown and Blowdown Philosophy) — currently `TBD`.
- No declared upstream deliverable dependencies (per `_DEPENDENCIES.md`).

## Steps

1. **Confirm scope and identity.** Read `_CONTEXT.md` and verify package identity (PKG-082, package name "Flare KO Drum (Low Pressure) 3-25", discipline Mechanical, responsible party EPC Integrator).
2. **Open the accessible source slice.** Read the DBM "Flare and Blowdown" section and the equipment summary table. Extract: vessel tag (V-3900-2), pump tag (P-3900-2), inlet streams (TEG regen, VRU, compressor seal-pot), transfer pump count (1 x 100 percent), LP relief header size (508 mm / 20 inch), and shared-flare context.
3. **Open and inventory referenced documents that are not in the workspace.** Record `26020-Package_Requirements.docx` heading 35, `26020-Packages_Interfaces_4_export.xlsx` Packages row 56, and W242510-PRC-REP-000003-001 as known references whose content remains `TBD`.
4. **Populate Datasheet identification, attributes, conditions, construction, and references** using only source-supported values. Mark non-source-supported items as `TBD` and label inferred items as `ASSUMPTION`.
5. **Derive Specification requirements** from the Datasheet entries that are source-supported. Tag each requirement with its source reference and a `FACT` / `ASSUMPTION` / `TBD` label.
6. **Capture Guidance** including principles, considerations, trade-offs, and the Conflict Table for items requiring human ruling.
7. **Cross-check** Datasheet ↔ Specification ↔ Guidance ↔ Procedure for terminology, equipment tag, header size, and interface destination consistency. Resolve discrepancies in favor of the source.
8. **Issue the draft.** Save the four documents in `{DELIVERABLE_PATH}`. Update `_STATUS.md` from `OPEN` to `INITIALIZED` (via `tools/scaffolding/write_status.sh`).
9. **Hand off** to downstream vendor or discipline-package engineering with the explicit list of `TBD` items the vendor or next discipline must close.
10. **Re-run** when any of the following become available: parsed content of `26020-Package_Requirements.docx` heading 35; parsed content of `26020-Packages_Interfaces_4_export.xlsx` Packages row 56; W242510-PRC-REP-000003-001 (shutdown and blowdown philosophy); final shared flare study; materials engineer ruling on sour-service applicability.

## Verification

- All four documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) exist in `{DELIVERABLE_PATH}` with the default section headings.
- Equipment tags V-3900-2 and P-3900-2, header size 508 mm / 20 inch, pump count 1 x 100 percent, and slop transfer destination are stated identically across documents.
- Every non-source-supported value is `TBD`; every inferred statement is labeled `ASSUMPTION`.
- The Conflict Table in `Guidance.md` captures (at minimum) the sour-service applicability open item and the W242510-PRC-REP-000003-001 cross-reference conflict noted in the DBM.
- `_STATUS.md` is `INITIALIZED` (only when transitioning from `OPEN`).
- A `_run_records/TASK_RUN_<timestamp>.md` file is written.

## Records

- Four documents in `{DELIVERABLE_PATH}`.
- Updated `_STATUS.md`.
- Run record under `{DELIVERABLE_PATH}/_run_records/`.
- (When generated) `Dependencies.csv` from `TASK + dependency-extract` (not in scope for this task).
