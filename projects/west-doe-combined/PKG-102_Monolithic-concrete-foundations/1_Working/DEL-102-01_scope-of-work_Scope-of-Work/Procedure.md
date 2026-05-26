# Procedure — DEL-102-01 Scope of Work (PKG-102 Monolithic concrete foundations)

> Operational procedure for producing the EPC Integrator Scope of Work for PKG-102 "Monolithic concrete foundations" as a Gate 5 EPC anchor deliverable.

## Purpose

Produce a source-grounded Scope of Work for PKG-102 that satisfies the requirements in `Specification.md` and the boundaries/considerations in `Guidance.md`, using the inputs in `_CONTEXT.md` and `_REFERENCES.md`.

## Prerequisites

- **Declared upstream dependencies:** None declared during PREPARATION. (Source: `_DEPENDENCIES.md` "Declared Upstream Dependencies".)
- **Required references (locally accessible):**
  - `_CONTEXT.md` and `_REFERENCES.md` (this deliverable folder).
  - GATE-07 Final Published PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_PACKAGE_MAP.csv`).
  - DBM-Deepcut: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 in particular.
- **Required references (not parsed in this run, needed to close TBDs):**
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 103 (binary workbook).
  - `_Sources/26020-Package_Requirements.docx` (companion document).
- **Tooling:** Markdown editor; access to scope-extraction tooling for the binary workbook (separate task; not invoked here).

## Steps

1. **Anchor identity.** Populate the SoW identification block (PackageID, WorkbookID, WBS, Discipline, PackageName, ResponsibleParty, Covers SOW-0258, Supports OBJ-001/OBJ-008) from `_CONTEXT.md` and the PKG-102 row of `PACKAGE_REGISTER.csv`. Verify consistency with `Datasheet.md` "Identification".
2. **State package function and source basis.** Draft the package-function statement and explicitly cite Workbook Packages row 103 and DBM-Deepcut SEC-11 as the source basis. Do not introduce equipment or design values that are not present in those sources. (See `Specification.md` R-102-01-002, R-102-01-004.)
3. **Cite governing structural and material basis.** Reproduce the standards block (CAN/CSA A23.3; CSA A23.1/A23.2; NBCC; Canadian Foundation Engineering Manual) from DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" without paraphrasing requirements that the SoW does not own. (See `Specification.md` R-102-01-005 and "Standards".)
4. **Populate tagged-equipment and package-identity list.** Extract the equipment-tag slice for PKG-102 from the workbook row 103 source. If the workbook extraction has not yet been performed, list this artifact as **TBD pending workbook row 103 extraction** and record the dependency. Do not invent tags. (See `Specification.md` R-102-01-003; `Guidance.md` CT-102-01-003.)
5. **Define boundaries.** Write the package-boundary statements:
   - Boundary against driven-steel-pile default basis (DBM-Deepcut SEC-11 "Piles and Foundations");
   - Boundary against PKG-101 (Precast concrete foundations);
   - Boundary against Civil packages (grading, drainage, roads, retention pond);
   - Boundary against vendor-engineered packages.
   (See `Guidance.md` "Considerations".)
6. **Write the whole-facility integration narrative.** Address both PKG-102 declared interface types — Grading / Site Drainage / Spill Containment (IFC-1EDEDC0453) and Structural / Foundations / Supports (IFC-8283744B5B). Cross-reference grading basis (1.5%/1.0% pad slopes; top-of-pile-cap coordination) and spill-containment provisions (NGL storage; compressor skid). (See `Specification.md` R-102-01-007.)
7. **Record responsibility assignment.** State that the EPC Integrator owns scope definition, integration, and oversight; identify the relationship to sibling deliverables DEL-102-02 (Package Datasheet), DEL-102-03 (Construction Work Package), and DEL-102-04 (EPC/Structural Discipline Production Package). (See `Specification.md` R-102-01-008.)
8. **List external dependencies and open issues.** Reproduce the relevant external-input list (geotechnical report; topographical survey; plot plan including retention-pond reference) and TBD set (bearing capacity; LPILE curves; dynamic design criteria; compressor foundation dynamic analysis) from DBM-Deepcut SEC-11. (See `Specification.md` R-102-01-009, R-102-01-010.)
9. **Cross-check consistency.** Verify terminology and values are consistent across `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. Resolve conflicts by re-reading source slices; if not resolvable, record in the `Guidance.md` Conflict Table.
10. **Submit for human review.** The SoW is a Gate 5 EPC anchor deliverable; human review is required before any state transition beyond INITIALIZED.

## Verification

| Check | Method |
|---|---|
| Identification block matches `PACKAGE_REGISTER.csv` PKG-102 | Side-by-side review against the GATE-07 snapshot row |
| Standards block reproduces DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" without paraphrase drift | Diff against source slice |
| Tagged-equipment list either reflects workbook row 103 or is explicitly TBD with the workbook-extraction dependency cited | Review of the SoW's equipment-tag section |
| Both declared interface types appear in the integration narrative | Search the SoW for IFC-1EDEDC0453 and IFC-8283744B5B coverage |
| Open-issues and external-input lists match DBM-Deepcut SEC-11 | Diff against source slice |
| Cross-document consistency (terminology, values, references) holds across the four documents | Review per `Specification.md` Verification table |
| Objective support (OBJ-001; OBJ-008) is traceable via OBJECTIVE_DELIVERABLE_MAP / OBJECTIVE_PACKAGE_MAP and labelled ASSUMPTION at the row level | Trace check |

## Records

The following records should result from execution of this procedure:

- `Datasheet.md`, `Specification.md`, `Guidance.md` (with Conflict Table), `Procedure.md` (this file) within the deliverable folder.
- `_run_records/TASK_RUN_<date>_<time>.md` capturing pass directive, sources consulted, RUN_STATUS, and any unresolved TBDs.
- `_STATUS.md` updated from `OPEN` to `INITIALIZED` only when invoked under a Pass-1/Pass-2 run starting from `OPEN`.
- Workbook-extraction task record (separate deliverable/task) once workbook row 103 has been extracted into deliverable-local form to close CT-102-01-003.
