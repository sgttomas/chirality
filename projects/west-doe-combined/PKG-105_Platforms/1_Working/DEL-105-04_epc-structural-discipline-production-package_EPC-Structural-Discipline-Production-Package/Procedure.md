# Procedure: DEL-105-04 — EPC / Structural Discipline Production Package

## Purpose

Produce the EPC / Structural Discipline Production Package artifacts for `PKG-105 — Platforms`, grounded in accessible workbook and DBM source material and recording all source-limited gaps explicitly. This procedure describes the steps to **produce** the deliverable artifact set defined in `_CONTEXT.md` and `ARTIFACT_REGISTER.csv` for `DEL-105-04`.

## Prerequisites

- Access to the GATE-07 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Access to `_Sources/26020-Package_Requirements.docx` and `_Sources/26020-Packages_Interfaces_4_export.xlsx` (workbook Packages row 106).
- Access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (referenced by `PACKAGE_REGISTER.csv` row PKG-105).
- Assignment of the Responsible Party (currently TBD; EPC Integrator or discipline subcontractor as assigned) — see Guidance Conflict Table CT-02.
- Coordination read of EPC anchor deliverables for PKG-105: `DEL-105-01` (Scope of Work), `DEL-105-02` (Package Datasheet), `DEL-105-03` (Construction Work Package). No declared upstream dependencies exist in `_DEPENDENCIES.md`; this is a functional, not declared, coordination prerequisite.

## Steps

1. **Confirm scope and identity.** Re-read `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv` row `DEL-105-04`, and `PACKAGE_REGISTER.csv` row PKG-105. Confirm: workbook ID `26020-01-36-005`; discipline Structural; WBS 01; package name Platforms; non-vendor scope.
2. **Extract source slices from the workbook.** Open `_Sources/26020-Package_Requirements.docx` to the section corresponding to Workbook Packages row 106 (Platforms). Identify and copy clause text relevant to structural discipline production (loads, materials, codes, connections, fabrication, coatings, fireproofing, inspection). Update `_REFERENCES.md` with the extracted slice locations. If no slices exist, record this in the closure record (Step 6). [Slice extraction is currently TBD per `_REFERENCES.md` Missing/Deferred References.]
3. **Extract interface facts.** From `INTERFACE_REGISTER.csv` (PKG-105 rows): record Area / Exterior Lighting (IFC-26E3DCAD56), Grading / Site Drainage / Spill Containment (IFC-07C472C58B), Structural / Foundations / Supports (IFC-B7C0A01E38). Carry the Gate 6 disposition that platform-to-equipment tie-ins are EPC Integrator responsibility through the 3D model and integrated P&ID set.
4. **Draft the discipline production package basis** (ART-16D83D7454). Compose a single document that records: package identity (Step 1), source-derived structural content (Step 2), interface fact set (Step 3), and explicit linkage to the EPC anchor deliverables. Use TBD for any subject area not supported by extracted slices.
5. **Draft the discipline deliverable register** (Anticipated Artifact; not yet registered in `ARTIFACT_REGISTER.csv` — see Guidance CT-01). Enumerate the structural production deliverables required to execute the non-vendor scope of PKG-105. For each entry: name, brief description, source basis, responsible role (provisional pending CT-02 ruling), and current state. When complete, register each entry in `ARTIFACT_REGISTER.csv` via the appropriate scaffolding workflow.
6. **Draft the source-limited requirements closure record** (ART-10C0D579FC). List every structural-discipline subject area for which the current source set does not contain a requirement, the search that was performed, and the rationale for leaving it open. This record satisfies the "carried conservatively" framing in `DELIVERABLE_REGISTER.csv`.
7. **Cross-check against objectives.** Trace produced content to OBJ-001, OBJ-005, OBJ-008, OBJ-010 via `OBJECTIVE_DELIVERABLE_MAP.csv` (deliverable-ID-explicit). Record the trace in the production package basis (Step 4).
8. **Update `_STATUS.md`.** When ready for review, advance state per the deliverable lifecycle. (This `four-documents` invocation handles only the OPEN→INITIALIZED transition via `tools/scaffolding/write_status.sh`.)

## Verification

| Check | Approach |
|---|---|
| All three Anticipated Artifacts present | Inspect the deliverable folder for the basis document, the discipline deliverable register, and the closure record. |
| Source fidelity | Confirm each non-TBD claim cites a workbook or DBM slice path or a GATE-07 register row. |
| Interface fidelity | Compare carried interface facts to `INTERFACE_REGISTER.csv` PKG-105 rows; confirm Gate 6 tie-in disposition is recorded verbatim in intent. |
| Objective trace | Confirm OBJ-001/005/008/010 trace is present and uses `OBJECTIVE_DELIVERABLE_MAP.csv` as the basis. |
| Closure record completeness | For every TBD in `Specification.md` (R-08..R-10 and others), confirm a corresponding entry in the source-limited closure record. |
| Conflict Table resolution | Confirm Guidance Conflict Table entries (CT-01, CT-02, CT-03) have been routed for human ruling. |

## Records

The following records should result from executing this procedure:

- Discipline production package basis document (ART-16D83D7454).
- Discipline deliverable register (TBD — to be registered in `ARTIFACT_REGISTER.csv` once produced).
- Source-limited requirements closure record (ART-10C0D579FC).
- Updated `_REFERENCES.md` reflecting any extracted source slices.
- Updated `_STATUS.md` history entry recording the four-documents initialization (this run).
- A run record under `_run_records/` for each execution of this procedure.
