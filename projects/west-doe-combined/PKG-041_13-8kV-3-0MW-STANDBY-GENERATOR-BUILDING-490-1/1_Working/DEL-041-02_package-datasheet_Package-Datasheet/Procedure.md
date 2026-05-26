# Procedure: DEL-041-02 — Package Datasheet (PKG-041)

> Operational procedure for **producing** the Package Datasheet for PKG-041 (13.8 kV, 3.0 MW Standby Generator Building, 490-1). Steps that require judgment about content not present in locally accessible sources are flagged `TBD`.

## Prerequisites

- Accepted upstream decomposition: GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (cited in `_REFERENCES.md`).
- Deliverable folder initialized by PREPARATION: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` all present.
- `_STATUS.md` Current State is `OPEN` or `INITIALIZED` (the four-documents skill will not overwrite human-edited later states).
- No human-declared upstream dependencies (per `_DEPENDENCIES.md`); upstream truth is the snapshot.
- Sibling PKG-041 deliverables exist and may be cross-referenced read-only: `DEL-041-01_scope-of-work` (scope source for boundary), `DEL-041-03..06` (downstream consumers).
- Source materials (consult when accessible):
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Packages tab, row 43.
  - `_Sources/26020-Package_Requirements.docx` — package requirements convention.
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Deepcut design basis (PACKAGE_REGISTER `PKG-041` SourceRefs).

## Steps

1. **Read context.** Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_SEMANTIC.md` in this folder.
2. **Lift identification block** from PACKAGE_REGISTER row `PKG-041` and DELIVERABLE_REGISTER row `DEL-041-02_package-datasheet` into `Datasheet.md` Identification. Verify the eight values listed in REQ-DS-01.
3. **Lift responsibility split** verbatim from PACKAGE_REGISTER row `PKG-041` ResponsibilityModel into `Datasheet.md` Attributes (REQ-DS-02).
4. **Lift name-derived ratings** (13.8 kV, 3.0 MW, standby, 490-1) into `Datasheet.md` Attributes (REQ-DS-03). Do not infer additional electrical parameters without source.
5. **Build the Interface Requirements Matrix** from INTERFACE_REGISTER rows where `ParentPackageID = PKG-041`. Preserve all twelve `IFC-*` IDs (REQ-DS-04). For each row, attempt to populate battery-limit, tie-point, and sizing fields; mark `TBD` with source pointer where absent (REQ-DS-05).
6. **Resolve workbook row 43 source slice (when possible).** Open `_Sources/26020-Packages_Interfaces_4_export.xlsx`; record the row-43 cell values relevant to: tagged equipment, ratings, building characteristics, environmental envelope. Update Datasheet sections with cited values. If source access is not available in this run, leave entries `TBD` with the pointer.
7. **Resolve package requirements convention slice (when possible).** Open `_Sources/26020-Package_Requirements.docx`; locate the section governing standby generator or building packages. Update `Specification.md` Requirements/Standards as supported by the text.
8. **Resolve Deepcut DBM slice (when possible).** Open `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; locate sections referencing PKG-041 / 490-1 / standby generation. Update `Datasheet.md` Conditions and `Specification.md` Standards accordingly.
9. **Cross-document consistency sweep** (Pass 2, Step 5 of the skill): verify Datasheet ↔ Specification entities, Specification ↔ Procedure verification hooks, terminology, numeric units. Resolve trivially or add to `Guidance.md` Conflict Table.
10. **Write `_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md`** with the four-documents skill outputs, status changes, missing items, and any rulings needed.
11. **Update `_STATUS.md`** safely via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` only when the prior state is `OPEN`. Do not regress state.

## Verification

- Datasheet identification block matches PACKAGE_REGISTER row `PKG-041` field-by-field (Step 2).
- Twelve `IFC-*` IDs in Datasheet matrix match INTERFACE_REGISTER PKG-041 set (Step 5).
- All `TBD` entries carry a source pointer (Step 6/7/8).
- No content outside the deliverable folder is modified (skill scope guarantee).
- Run record exists at `_run_records/TASK_RUN_*.md` (Step 10).
- `_STATUS.md` updated to `INITIALIZED` only when starting state was `OPEN` (Step 11).
- Specification verification approaches for REQ-DS-01..11 reference accessible artifacts.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in this deliverable folder (the four produced documents).
- `_STATUS.md` History entry recording `OPEN → INITIALIZED` transition (when applicable).
- `_run_records/TASK_RUN_*.md` containing input echo, resolved state, outputs produced, and the disposition of every TBD/CONFLICT.
- `MEMORY.md` (optional; only when durable context worth preserving emerges from the run).
