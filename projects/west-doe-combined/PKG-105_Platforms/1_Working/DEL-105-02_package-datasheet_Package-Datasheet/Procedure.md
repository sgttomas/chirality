# Procedure — DEL-105-02 Package Datasheet (PKG-105 Platforms)

> Operational steps to **produce** the Package Datasheet artifact for PKG-105 Platforms and (subordinately) to **use** the completed datasheet for vendor/discipline handoff.

## Purpose

Author and verify the Package Datasheet artifact (`Datasheet.md`) for `PKG-105 Platforms` so it satisfies the requirements in `Specification.md`, preserves interface evidence per `_CONTEXT.md` Notes, and is fit for third-party vendor engineering handoff.

## Prerequisites

- Read access to the deliverable folder: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Read access to GATE-07 snapshot registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_REGISTER.csv`, `SCOPE_LEDGER.csv`.
- Read access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-11 in particular).
- `_STATUS.md` state must be in `ALLOW_OVERWRITE_STATES` (OPEN or INITIALIZED) for the four-documents skill to overwrite drafts.
- Declared upstream dependencies (none currently declared in `_DEPENDENCIES.md`).
- Optional/escalation: access to raw workbook row 106 source (`26020-Packages_Interfaces_4_export.xlsx`) and/or `26020-Package_Requirements.docx` for missing tagged-equipment and detailed structural content.

## Steps

1. **Confirm identity.** From `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row 106, populate the Datasheet Identification block (DeliverableID, PKG-105, Platforms, WBS 01, Structural, EPC Integrator, CoA 26020-01-36-005).
2. **Capture scope-item link.** From `SCOPE_LEDGER.csv` SOW-0261, record the workbook-defined function statement and the deliverables it spans (DEL-105-01..04).
3. **Apply governing structural/civil basis.** From DBM SEC-11 §Governing Civil and Structural Basis, populate Standards/Construction tables (NBC Canada, CAN/CSA-S16, CAN/CSA A23.3, Canadian Foundation Engineering Manual, CSA G40.20/G40.21 350W/300W, CSA A23.1/A23.2).
4. **Set foundation basis.** From DBM SEC-11 §Piles and Foundations, record driven steel piles as default. Mark detailed pile parameters TBD pending geotechnical report (SEC-11 §Geotechnical and Topographical Assumptions).
5. **Set loading basis.** From DBM SEC-11 §Buildings and Miscellaneous Facilities (loading clause for project buildings), record NBC-Canada loading regime as **ASSUMPTION** applied to platforms.
6. **Record grading/drainage coupling.** From DBM SEC-11 §Site Grading and Surface Water Management, note pad-slope envelope (1.5%/1.0%) interaction with platform top-of-pile-cap elevations.
7. **Populate interface requirements matrix.** From `INTERFACE_REGISTER.csv` (filter `PackageID=PKG-105`), copy the three IFC rows (IFC-26E3DCAD56 Lighting; IFC-07C472C58B Grading/Drainage/Containment; IFC-B7C0A01E38 Structural/Foundations/Supports) with applicability and Notes/Gate 6 disposition.
8. **Cross-link interface-fact artifacts.** From `ARTIFACT_REGISTER.csv`, reference ART-39021CDFB3, ART-217A830349, ART-1FA7F21048, ART-749A9EEC06 (and ART-A71A680036 for the matrix, ART-EA98D39386 for vendor handoff, ART-E5A717EC97 for the datasheet itself).
9. **Mark equipment / geometry gaps.** Tagged equipment list, platform counts, footprint, materials beyond steel-grade defaults: enter as `TBD` with the missing source named (workbook row 106 raw slice).
10. **Record objective association.** From `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC), list OBJ-001/005/008/010 with the **ASSUMPTION (best-effort mapping)** label.
11. **Vendor handoff basis section.** Per `ARTIFACT_REGISTER.csv` ART-EA98D39386, enumerate technical basis, battery limits, design expectations, and source-supported requirements. Mark each unresolved sub-item TBD.
12. **Cross-document consistency sweep (Pass 2).** Verify Datasheet ↔ Specification (R-1..R-12 mapped), Specification ↔ Guidance (rationale present), Specification ↔ Procedure (each requirement has a verification hook), and terminology/values consistent across documents.
13. **Conflict capture.** Any unresolved cross-document or source-vs-narrative inconsistency: enter a row in `Guidance.md` §Conflict Table (CT-01..CT-04 already seeded).
14. **Status update.** If `_STATUS.md` Current State is `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Otherwise leave unchanged.
15. **Run record.** Append a `_run_records/TASK_RUN_<DATE>_<HHMM>.md` entry summarizing pass set, files written, key TBDs, and conflicts surfaced.

## Verification

| Step | Verification |
|---|---|
| 1, 2 | Identity fields and SOW-0261 function statement match registers verbatim. |
| 3, 4, 5 | Each cited DBM clause exists at the cited section; values match. |
| 6 | Grading clause cited correctly; coupling note present. |
| 7, 8 | All three IFC rows present with exact IDs; artifact IDs cross-linked. |
| 9 | All gaps marked TBD with missing-source name; no invented values. |
| 10 | Objectives listed with ASSUMPTION label. |
| 11 | All four vendor-handoff content categories present; unresolved items TBD. |
| 12 | Spec R-1..R-12 each verifiable against Datasheet; terminology consistent. |
| 13 | Conflict Table updated for any unresolved item. |
| 14 | `_STATUS.md` reflects new state with TASK+four-documents provenance. |
| 15 | Run record exists with timestamp, pass set, RUN_STATUS. |

## Records

- `Datasheet.md` (primary artifact)
- `Specification.md`, `Guidance.md` (with Conflict Table), `Procedure.md` (this file)
- `_STATUS.md` updated to `INITIALIZED` if previously `OPEN`
- `_run_records/TASK_RUN_<DATE>_<HHMM>.md`
- (Downstream) Vendor handoff package referencing this datasheet; integrator's 3D model and integrated P&ID set carrying platform-to-equipment tie-in resolution per Gate 6 disposition
