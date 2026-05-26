# Procedure — DEL-051-02 Package Datasheet (Process Heat Medium Unit)

## Purpose

Operational steps to produce, verify, and maintain the Package Datasheet for PKG-051 Process Heat Medium Unit. The procedure covers source extraction, datasheet population, interface declaration, and TBD/conflict tracking required to bring the deliverable from INITIALIZED through downstream maturity states.

## Prerequisites

- Read access to deliverable folder: `PKG-051_Process-Heat-Medium-Unit/1_Working/DEL-051-02_package-datasheet_Package-Datasheet/`.
- Read access to project source set: `_Sources/26020-Package_Requirements.docx` and `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Read access to accepted decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in the deliverable folder (confirmed by PREPARATION).
- Declared upstream dependencies: none declared at PREPARATION (`_DEPENDENCIES.md`).

## Steps

1. **Confirm identity.** From `_CONTEXT.md`, lock DeliverableID, PackageID, package name, discipline, responsible party, workbook row, and CoA tag.
2. **Extract docx source slice.** Open `26020-Package_Requirements.docx`; locate Heading 1 "26020-01-PT-15-001 - Process Heat Medium Unit" (the 6th Heading 1). Capture Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables, and Interface Coordination Notes text verbatim.
3. **Extract xlsx interface slice.** Open `26020-Packages_Interfaces_4_export.xlsx`, Packages sheet, row ID# 51 (Packages = "Process Heat Medium Unit"). Record which interface columns are marked "X" and which are blank. Capture Interface Review Notes if populated.
4. **Populate Datasheet.md.** Fill Identification, Attributes, Conditions, Construction, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes, and References sections with values from steps 2–3. Mark every unfilled value `TBD`. Cite source path + section for each non-trivial value.
5. **Populate Specification.md.** Convert source statements into numbered requirements (REQ-051-02-NN). Each requirement cites its source slice. Map requirements to verification approaches and list documentation artifacts (anticipated artifacts + vendor-supplied datasheets).
6. **Populate Guidance.md.** Write Purpose, Principles, Considerations, Trade-offs, and Examples grounded in the source slices and the deliverable's role per `_CONTEXT.md`. Record source ambiguities and decomposition-driven assumptions in the Conflict Table.
7. **Populate Procedure.md.** Provide this procedure file describing how the datasheet is produced, verified, and maintained.
8. **Cross-document consistency sweep.** Confirm equipment lists, design values, units, and terminology agree across Datasheet, Specification, Guidance, and Procedure. Resolve discrepancies from source where possible; otherwise add Conflict Table entries.
9. **Update `_STATUS.md` safely.** If the current state is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh`. Do not regress state. Do not modify any other metadata file.
10. **Write run record.** Create `_run_records/TASK_RUN_<timestamp>.md` capturing input echo, resolved state, tools used, outputs, missing items, dependency notes, and applied changes.
11. **Coordinate downstream maturation.** Surface open TBDs and conflicts to the human reviewer; queue resolution actions (vendor data-in, source clarification, interface coordination meetings) for subsequent runs and dependent deliverables.

## Verification

| Step | Check |
|---|---|
| 2 | docx heading 6 text matches expected package tag 26020-01-PT-15-001. |
| 3 | xlsx row ID# 51 Packages column equals "Process Heat Medium Unit"; recorded interface set matches source row exactly. |
| 4 | Datasheet contains Identification, Attributes, Conditions, Construction, References sections; each value either cites a source or is marked `TBD`. |
| 5 | Specification contains Scope, Requirements, Standards, Verification, Documentation; each requirement cites a source. |
| 6 | Guidance contains Purpose, Principles, Considerations, Trade-offs, Examples; Conflict Table present when conflicts exist. |
| 7 | Procedure contains Purpose, Prerequisites, Steps, Verification, Records. |
| 8 | No numeric value or unit disagrees across the four documents; terminology stable. |
| 9 | `_STATUS.md` change conforms to `OPEN → INITIALIZED` rule; no regression; no edits to other metadata files. |
| 10 | Run record present with required headings; tool usage and outputs reported truthfully. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this deliverable folder).
- `_STATUS.md` history line for the `OPEN → INITIALIZED` transition.
- `_run_records/TASK_RUN_<timestamp>.md` for each invocation.
- Conflict Table entries inside `Guidance.md` for any unresolved source / decomposition / vendor ambiguities.
- Vendor data-in records (TBD; produced in subsequent runs once vendor submissions arrive).
