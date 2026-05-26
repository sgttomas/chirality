# Procedure — DEL-041-03 Construction Work Package

## Purpose

This Procedure governs the production and use of the Construction Work Package for PKG-041 (13.8 kV, 3.0 MW Standby Generator Building, 490-1). It covers both:

- the EPC Integrator workflow to **author** the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist (`_CONTEXT.md` Anticipated Artifacts), and
- the field workflow to **execute and turn over** that package once issued.

## Prerequisites

### Inputs that must be available

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` (deliverable-local).
- GATE-07 PROJECT_DECOMP snapshot rows for DEL-041-03, PKG-041, ART-* on DEL-041-03, IFC-* on PKG-041, and OBJECTIVE_DELIVERABLE_MAP rows mentioning DEL-041-03.
- DEL-041-01 Scope of Work (workbook authoritative).
- DEL-041-02 Package Datasheet (interface requirements matrix and interface fact evidence).
- DEL-041-04 Vendor Engineered Equipment Package (when matured to at least `INITIALIZED`).
- Workbook Packages row 43 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`).
- Design Basis Memorandum slice (`_Sources/DBM-Deepcut`) — to be opened during authoring; not opened in this initialization run.

### Declared upstream dependencies (from `_DEPENDENCIES.md`)

- None declared during PREPARATION. (NB: undeclared relationships are not blockers in DECLARED mode.)

### Declared downstream dependencies

- None declared during PREPARATION. (Construction execution will feed DEL-041-06 EPC Vendor Package Review and Acceptance — informational, not a declared edge.)

## Steps

### Authoring steps (EPC Integrator)

1. **Confirm package identity and scope.** Re-read `_CONTEXT.md`, GATE-07 `DELIVERABLE_REGISTER.csv` row for DEL-041-03, and `PACKAGE_REGISTER.csv` row for PKG-041. Verify package name, WBS, discipline, responsibility split, and applicable interfaces.
2. **Pull declared interfaces.** Extract the twelve PKG-041 rows from GATE-07 `INTERFACE_REGISTER.csv` (IFC-508C53EB72 through IFC-D0146B1F8C). These become the spine of the workface plan and turnover checklist.
3. **Pull interface fact evidence.** From GATE-07 `ARTIFACT_REGISTER.csv`, take the "Interface fact -" rows on DEL-041-02 (ART-0096A23E12 through ART-E2472057A2) as the integration basis. Do not restate the facts; reference them.
4. **Open source slices.** Open Workbook Packages row 43 and the Design Basis Memorandum (`_Sources/DBM-Deepcut`) for ratings, dimensions, site conditions, and any package-specific construction notes. Where the source is silent, mark `TBD` with `location TBD`.
5. **Draft the construction work package narrative.** Cover site preparation, foundation and structural support, setting the vendor-furnished building, mechanical/electrical/I&C/communications tie-ins, safety system integration, maintenance access provisions, and inspection/turnover. Cite source slices for every non-trivial value.
6. **Draft the installation and tie-in workface plan.** For each interface in step 2, define sequencing, crew/discipline assignment, predecessor/successor relationships, and field tie-in procedure. Quantitative sequencing values are `TBD` until source slices and the vendor package (DEL-041-04) are opened.
7. **Draft the construction interface and turnover checklist.** Rows: interface ID, tie-in physical scope, inspection criteria, sign-off responsibility, turnover acceptance status. (Row structure ASSUMPTION.)
8. **Cross-check upstream consistency.** Compare against DEL-041-01 (boundaries, tagged equipment) and DEL-041-02 (interface matrix). Log any conflict in the Conflict Table on `Guidance.md`; do not silently reconcile.
9. **Trace objectives.** For each of OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (GATE-07 `OBJECTIVE_DELIVERABLE_MAP.csv`), record which construction sub-activity supports it; mark gaps `TBD`.
10. **Submit for human review.** Per K-AUTH-1, only humans author binding approval; the construction work package is proposed until reviewed.

### Field-execution steps (after the work package is approved)

11. **Mobilize and verify prerequisites on site.** Confirm vendor delivery readiness, foundation completion, and crew/equipment availability.
12. **Execute each interface tie-in per the workface plan.** Work through interfaces in the sequenced order. Record installation evidence against the interface ID.
13. **Inspect each interface against the turnover checklist.** Sign off when acceptance criteria are met; raise non-conformances against the originating discipline.
14. **Roll up turnover evidence.** Submit completed checklist and installation records to DEL-041-06 (EPC Vendor Package Review and Acceptance).

## Verification

| Check | Method | Evidence |
|---|---|---|
| All twelve PKG-041 interfaces appear in the workface plan and turnover checklist | Tabular cross-check against GATE-07 `INTERFACE_REGISTER.csv` | Coverage matrix attached to the work package |
| Every non-trivial value cites a source | Source-grounding audit (REQ-CWP-07) | Source citations in-line or footnoted |
| No silent reconciliation of upstream conflicts | Review of Conflict Table on `Guidance.md` | Conflict rows with human rulings |
| Objective traceability complete or explicit `TBD` per objective | Traceability matrix review | Per-objective rows for OBJ-001, OBJ-004 .. OBJ-010 |
| Turnover checklist sign-offs complete before handoff | Field audit | Signed turnover checklist |

## Records

The following records SHALL result from execution of this Procedure:

- Authored Construction Work Package narrative (ART-55CB0F50C6).
- Installation and tie-in workface plan (anticipated artifact, ID TBD).
- Construction interface and turnover checklist (anticipated artifact, ID TBD), with sign-offs.
- Source-grounding citations and `TBD`/`ASSUMPTION` log.
- Conflict Table entries with human rulings (if any conflicts were raised).
- Objective traceability matrix to OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010.
- Field execution evidence: installation records, inspection sign-offs, non-conformance log (if any).
- Run records under `_run_records/` capturing each TASK invocation that touched this deliverable.
