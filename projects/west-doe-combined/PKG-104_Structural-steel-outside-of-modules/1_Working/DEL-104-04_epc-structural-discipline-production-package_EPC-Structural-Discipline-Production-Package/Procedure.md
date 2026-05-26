# Procedure: DEL-104-04 — EPC / Structural Discipline Production Package

## Purpose

Produce the discipline production package basis, the TBD discipline deliverable register, and the source-limited requirements closure record for PKG-104 (Structural steel - outside of modules), grounded in the GATE-07 PROJECT_DECOMP snapshot and accessible source materials. (Source: `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` rows for DEL-104-04.)

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` for this deliverable.
- Access to the GATE-07 PROJECT_DECOMP snapshot at:
  `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Access to the shared source root:
  `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources` (workbook, package requirements docx, DBM markdown including `DBM-Deepcut/4-25_Deepcut_DBM.md`).
- Declared upstream dependencies: none declared during PREPARATION (per `_DEPENDENCIES.md`).
- Human-recorded responsibility assignment (EPC Integrator vs discipline subcontractor) — required before binding production work begins (R-104-04-08).
- Sibling deliverables DEL-104-01 (Scope of Work), DEL-104-02 (Package Datasheet), DEL-104-03 (Construction Work Package) drafts available for boundary alignment (context only; no authority hierarchy violation).

## Steps

1. **Confirm scope and identity.** Re-extract PKG-104 row from `PACKAGE_REGISTER.csv` and DEL-104-04 row from `DELIVERABLE_REGISTER.csv`; verify identity, scope description, inclusion criteria, exclusions, and interface types are unchanged. (Verifies R-104-04-04, R-104-04-05.)
2. **Open the workbook source slice.** Open `26020-Packages_Interfaces_4_export.xlsx` row 105 and capture the source-of-truth fields for PKG-104 (name, WBS, CoA tracking, discipline, interface X-columns, outside-of-modules framing). Record any field that diverges from the register as a Conflict Table entry in `Guidance.md`. (Resolves CONF-104-04-02 partially; addresses CONF-104-04-03.)
3. **Open candidate standards/basis sources.** Open `26020-Package_Requirements.docx` and `DBM-Deepcut/4-25_Deepcut_DBM.md` (directly cited as SourceBasis); identify any PKG-104-relevant text including outside-of-modules structural steel scope. If none found, record that finding in the closure record. (Supports R-104-04-02; resolves CONF-104-04-02.)
4. **Author the discipline production package basis (ART-26DA5854ED).** Compose the basis document grounded in workbook row 105 and DBM-supported context; preserve the two declared interfaces; do not introduce structural-steel design values, member sizes, connection details, loadings, or fabrication/erection criteria absent from sources. (Verifies R-104-04-01, R-104-04-04, R-104-04-07.)
5. **Author the TBD discipline deliverable register.** List each discipline-level deliverable the production unit will issue within source-supported scope (e.g., structural steel general arrangement drawings, member schedules, connection details, erection drawings — each marked TBD until source-supported). Where the source set does not warrant a deliverable, record it as TBD with a brief rationale. (Verifies R-104-04-03.)
6. **Author the source-limited requirements closure record (ART-E815C1D6F1).** Enumerate the requirements gaps identified in Steps 2-3; for each gap, record: gap statement, supporting/missing source, proposed disposition, and human-ruling slot. Flag for Gate 5 review. (Verifies R-104-04-02.)
7. **Record responsibility assignment.** Capture the human ResponsibleParty decision (EPC Integrator or named discipline subcontractor) in the production package basis. Do not proceed past this step without the recorded human decision. (Verifies R-104-04-06, R-104-04-08; respects K-AUTH-1.)
8. **Cross-check sibling boundary.** Confirm that artifacts produced under DEL-104-04 do not duplicate scope of work, datasheet, or construction work package content owned by DEL-104-01..03; cite the sibling deliverable instead of replicating. Pay special attention to interface evidence already carried in DEL-104-02 (ART-2280F54DB3, ART-41502579DF). (Supports Specification Scope.)
9. **Resolve or escalate Conflict Table entries.** For each conflict listed in `Guidance.md`, either resolve with new source evidence or update the proposed authority and leave the human-ruling slot for Gate 5.
10. **Update `_STATUS.md` via the safe state helper** when the four-document kit is in place: `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (only when state is `OPEN`). Subsequent state transitions (e.g., `SEMANTIC_READY`, `SUBMITTED`, etc.) follow downstream skills/orchestrator phases.

## Verification

| Step | Verification Check |
|---|---|
| 1 | Identity fields in `Datasheet.md` match `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. |
| 2 | Workbook row 105 source slice has been opened and captured; divergences recorded in Conflict Table. |
| 3 | Each candidate standards/basis source has either been opened (with findings recorded) or marked TBD with rationale. |
| 4 | Production package basis artifact exists, cites workbook row 105 + DBM context, and preserves both declared interfaces. |
| 5 | Discipline deliverable register exists; each entry is either source-supported or marked TBD with rationale. |
| 6 | Closure record exists and enumerates each gap with provenance and proposed disposition. |
| 7 | Responsibility assignment is recorded by a human; no agent-authored binding decision present. |
| 8 | No duplication of DEL-104-01..03 content; sibling references cited. |
| 9 | Conflict Table entries are each resolved or carry a clear human-ruling slot. |
| 10 | `_STATUS.md` reflects `INITIALIZED` after a successful Pass 1/2 run (only when prior state was `OPEN`). |

## Records

The following artifacts/records must exist on completion of the production work (note: this Pass 1/2 run produces the four-document kit; the artifacts below are downstream production outputs that the four-document kit prescribes):

- Discipline production package basis (ART-26DA5854ED) — within DEL-104-04 working folder.
- TBD discipline deliverable register — within DEL-104-04 working folder.
- Source-limited requirements closure record (ART-E815C1D6F1) — within DEL-104-04 working folder.
- Responsibility assignment record (human-authored).
- Run record for this TASK run: `_run_records/TASK_RUN_2026-05-25_<HHMM>.md`.
- Updated `_STATUS.md` (safe transitions only).
