# Procedure — DEL-044-04 EPC / Instrumentation Discipline Production Package

> Pass 1/2 draft. Procedure describes how to **produce** the discipline production package artifacts. Operational/use procedures are TBD until the production basis stabilizes (decomposition Notes: source-limited).

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- Read DELIVERABLE_REGISTER, PACKAGE_REGISTER, ARTIFACT_REGISTER, INTERFACE_REGISTER, and OBJECTIVE_DELIVERABLE_MAP rows scoped to `DEL-044-04` and `PKG-044` (GATE-07 snapshot).
- Read sibling EPC-anchor deliverables when available: DEL-044-01 (Scope of Work), DEL-044-02 (Package Datasheet), DEL-044-03 (Construction Work Package).
- Resolve access to Workbook Packages row 46 (`26020-Packages_Interfaces_4_export.xlsx`) and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — currently TBD (`_REFERENCES.md` Missing/Deferred References).
- Declared upstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`); treat sibling DEL-044-01..03 as informal upstream context.

## Steps

1. **Scope confirmation.** Confirm the discipline production unit's scope from `_CONTEXT.md` and DELIVERABLE_REGISTER DEL-044-04 Description; reconcile with the package-level scope in DEL-044-01 when published. Record any divergence.
2. **Author the discipline production package basis.** Produce a basis document covering (a) discipline scope statement, (b) interface coverage for each PKG-044 ApplicableInterfaceType, (c) carried Gate 6 plug-n-play disposition, (d) explicit TBDs for source-limited items.
3. **Build the discipline deliverable register.** Enumerate sub-deliverables expected within this production unit (e.g., instrumentation specifications, loop diagrams, instrument index, calibration plans). Mark each sub-deliverable as TBD where source slices have not yet been ruled.
4. **Establish source-limited requirements closure record.** For each TBD item, record: the missing source, the question, the proposed disposition path (Gate 5 ruling, source slice request, or sibling deliverable trace), and the owner.
5. **Cross-trace.** Build a matrix from R-044-04-04..R-044-04-09 to artifacts and verification evidence. Record gaps as new closure-record entries.
6. **Interface alignment.** Walk each ApplicableInterfaceType for PKG-044 (Process Piping; Utility Piping; Electrical Power; I&C/Control Cabling; Communications/Network) and confirm that the production basis assigns or defers each. ASSUMPTION: interface set inherited from PACKAGE_REGISTER row PKG-044.
7. **Responsibility note.** Record that EPC Integrator vs. discipline subcontractor assignment is open (CONF-044-04-01); do not encode a default.
8. **Internal QA.** Verify the four-document cross-consistency checks from `four-documents` SKILL Step 5; update the Conflict Table in `Guidance.md` as needed. TBD where data is not present.
9. **Submit for Gate 5 disposition.** Hand the production basis, deliverable register, and closure record to the responsible reviewer for ruling on open TBDs.

## Verification

| Verification check | Method |
|---|---|
| Three anticipated artifacts exist (basis, register, closure record) | Document inspection within `{DELIVERABLE_PATH}` |
| Each R-044-04-* requirement traces to an artifact or to a closure-record TBD | Trace matrix review |
| Each ApplicableInterfaceType for PKG-044 is either covered or deferred with reason | Cross-check against PACKAGE_REGISTER PKG-044 |
| Objective lineage retained (`OBJ-002; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-010`) | Cross-check against OBJECTIVE_DELIVERABLE_MAP rows |
| No invented engineering values | Review against `_REFERENCES.md` accessibility and ASSUMPTION/TBD labelling |
| `_STATUS.md` state transition is consistent with `four-documents` Step 7 rules | Review of `_STATUS.md` history |

## Records

- Discipline production package basis document.
- Discipline deliverable register (TBD until populated).
- Source-limited requirements closure record (TBD until populated).
- Trace matrix from R-044-04-* requirements to artifacts.
- `_run_records/TASK_RUN_*.md` (this skill's run records).
- Updated `_STATUS.md` history line per `tools/scaffolding/write_status.sh`.
