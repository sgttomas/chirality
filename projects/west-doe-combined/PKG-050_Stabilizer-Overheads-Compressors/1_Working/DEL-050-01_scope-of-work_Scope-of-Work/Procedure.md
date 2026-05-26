# Procedure — DEL-050-01_scope-of-work (PKG-050 Stabilizer Overheads Compressors)

## Purpose

Procedure to **produce** the EPC Integrator-authored Scope of Work for PKG-050. The Procedure assembles the artifact set listed in ARTIFACT_REGISTER.csv for DEL-050-01 (ART-AF6ADA74A4, ART-8BA2B0B695, ART-CA258CB1DF, ART-769C18AA16, ART-A06F144C77) from the accepted Gate 7 PROJECT_DECOMP snapshot and locally accessible source materials.

## Prerequisites

- **Declared upstream dependencies:** none declared (`_DEPENDENCIES.md`).
- **Accepted upstream snapshot:** Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- **Required reference rows (must resolve before drafting):**
  - SCOPE_LEDGER.csv: SOW-0173, SOW-0174, SOW-0175, SOW-0176.
  - PACKAGE_REGISTER.csv: PKG-050 row.
  - INTERFACE_REGISTER.csv: PKG-050 rows (13 IFC- entries).
  - ARTIFACT_REGISTER.csv: DEL-050-01 artifact rows.
  - OBJECTIVE_DELIVERABLE_MAP.csv (for objective association cross-check).
- **Required source materials (locally accessible):**
  - Workbook `_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 81).
  - Package requirements `_Sources/26020-Package_Requirements.docx` (package heading 5).
  - DBM context: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **Authorization:** `_STATUS.md` Current State must be `OPEN` or `INITIALIZED` for overwrite by this skill (per `ALLOW_OVERWRITE_STATES`).

## Steps

1. **Confirm identity.** Open `_CONTEXT.md`. Confirm DeliverableID `DEL-050-01_scope-of-work`, ParentPackageID `PKG-050`. Confirm against PACKAGE_REGISTER.csv (workbook row 81; CoA 26020-01-12-005; WBS 01; Mechanical).
2. **Resolve scope items.** Pull SOW-0173, SOW-0174, SOW-0175, SOW-0176 from SCOPE_LEDGER.csv. Treat their text as the authoritative scope content for this package.
3. **Resolve interfaces.** Pull the 13 IFC- rows for PKG-050 from INTERFACE_REGISTER.csv. Carry the interface-type names verbatim.
4. **Resolve responsibility split.** Reproduce the PACKAGE_REGISTER.csv PKG-050 responsibility narrative verbatim (Package Vendor vs. EPC Integrator).
5. **Resolve objectives.** From `_CONTEXT.md` Supports Objectives, list OBJ-001 / OBJ-003..OBJ-010. Cross-check OBJECTIVE_DELIVERABLE_MAP.csv at the deliverable-ID level; if only package-level mapping is present, label the association ASSUMPTION (PACKAGE_HEURISTIC).
6. **Draft Datasheet.** Populate Identification, Attributes, Conditions (Operating), Conditions (Design), Construction, Tagged-Equipment list, Applicable Interfaces, References. Use `TBD` for any source-truncated value (e.g., stage-3 / stage-4 cooler discharge temperatures).
7. **Draft Specification.** Encode the Scope (in/out), Requirements (REQ-01..REQ-14 anchored to SCOPE_LEDGER / PACKAGE_REGISTER / INTERFACE_REGISTER), Standards (NEMA MG 1 with `location TBD`; Ariel KBC/6 vendor basis), Verification approaches per REQ, Documentation list from ARTIFACT_REGISTER.csv.
8. **Draft Guidance.** Encode Purpose (anchor for PKG-050), Principles (decomposition routes, sources determine content), Considerations (granularity, standards, KBC/6, objective heuristic, bid doc, exclusions), Trade-offs, Examples, Conflict Table for the four unresolved items (truncated cooler temps; "Other MAWP TBC"; objective heuristic; unparsed bid doc).
9. **Draft Procedure (this document).** Record prerequisites, steps, verification, records.
10. **Cross-document consistency sweep (Pass 2).** For each cross-check (Datasheet ↔ Specification, Specification ↔ Guidance, Specification ↔ Procedure, terminology, values), confirm alignment. Where a value differs and source does not arbitrate, prefer `TBD` and log to the Conflict Table.
11. **Status update.** If `_STATUS.md` Current State is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh` (or equivalent safe-write). Do not regress state.
12. **Persist run record.** Update `_run_records/TASK_RUN_<timestamp>.md` from `PENDING` to final status with all completion sections populated.

## Verification

- **V-01 (REQ-01..REQ-12 traceability).** Each Specification requirement traces to a SCOPE_LEDGER / PACKAGE_REGISTER / INTERFACE_REGISTER row cited in the Source column of the requirements table.
- **V-02 (Interface count).** Datasheet "Applicable Interfaces" list contains 13 entries matching INTERFACE_REGISTER.csv PKG-050 rows by IFC- identifier.
- **V-03 (Identity consistency).** Datasheet Identification table and Specification REQ-01 reference the same workbook row, CoA tracking number, WBS, and discipline.
- **V-04 (Value consistency).** Per-stage capacities and pressures appearing in Datasheet match those carried in Specification REQ-06 / REQ-07; truncated values are uniformly `TBD` in both.
- **V-05 (Responsibility consistency).** Datasheet Construction "Package vendor responsibility" / "EPC Integrator responsibility" and Specification REQ-10 reproduce the PACKAGE_REGISTER.csv PKG-050 responsibility narrative without paraphrase divergence.
- **V-06 (Objective association).** Specification REQ-13 and Guidance Considerations both label the objective association ASSUMPTION (PACKAGE_HEURISTIC) until deliverable-ID-level confirmation.
- **V-07 (Conflict-table coverage).** Each `TBD` in the Datasheet / Specification that depends on missing source extraction has a corresponding entry in the Guidance Conflict Table.
- **V-08 (Scope-boundary check).** No content within the four documents introduces requirements, design values, or work scope that belongs to DEL-050-02..DEL-050-06.
- **V-09 (Status safety).** `_STATUS.md` history shows `OPEN → INITIALIZED` only; no regression and no other state changes.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- Updated `_STATUS.md` with history entry for the OPEN → INITIALIZED transition.
- Run record at `_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill state, tools used, outputs, and Conflict-Table-backed `TBD`s.
- Conflict Table entries in `Guidance.md` (`CONF-01` truncated cooler temps; `CONF-02` Other MAWP TBC; `CONF-03` objective heuristic; `CONF-04` unparsed bid doc).
