# Procedure — DEL-093-02 Package Datasheet (Tanks, Water (API 650) 3-25)

## Purpose

This procedure describes how the EPC Integrator produces, validates, and issues the `DEL-093-02` Package Datasheet from the accepted decomposition snapshot and the governing source documents.

## Prerequisites

- Accepted GATE-07 Final Published PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` populated by PREPARATION (all present for this deliverable).
- Local access to `3-25_Comp_and_Liquids_DBM.md` (DBM-Comp_and_Liquids).
- Local access to `PACKAGE_REGISTER.csv` row `PKG-093` (the authoritative companion register row; identifies TK-9060-2 / TK-9070-2 and the applicable interface set).
- Local rendering of `26020-Package_Requirements.docx` heading 45 — TBD (still binary at this run).
- Local rendering of `26020-Packages_Interfaces_4_export.xlsx` Packages row 95 — TBD.
- Local rendering of `Bid Docs/Budgetary/26020-03-PT-RFQ-19-001 - Water Tanks.docx` — TBD.
- `DEL-093-01` (Scope of Work) draft available for cross-check.

## Steps

1. **Fix the package boundary.** Use `PACKAGE_REGISTER.csv` row PKG-093 as the authoritative scope: two 3,800 bbl Sweet Produced Water Storage Tanks, TK-9060-2 and TK-9070-2. Do not import the wider 7-tank DBM family into this datasheet's equipment list.
2. **Render binary source slices.** Convert `26020-Package_Requirements.docx` heading 45, `26020-Packages_Interfaces_4_export.xlsx` Packages row 95, and the budgetary RFQ docx to readable form (use `tools/pdf2md/` or equivalent docx/xlsx conversion outside this deliverable's scope). Cite resulting source slices.
3. **Populate Identification.** Use `_CONTEXT.md`, `PACKAGE_REGISTER.csv` row PKG-093, and DBM §SEC-01/SEC-02 to set the identity, tag numbers, facility, and site fields.
4. **Populate Attributes.** Equipment identity (TK-9060-2, TK-9070-2), quantity (2 x 3,800 bbl), tank type/code (API 650 Modified), coating (Devchem 253), insulation/heating — from PACKAGE_REGISTER and `3-25_Comp_and_Liquids_DBM.md` §SEC-06.
5. **Populate Process / Design Conditions.** Service (sweet produced water / process water), design SG, ambient, pressure class — from PACKAGE_REGISTER and DBM §SEC-02/SEC-03/SEC-04/SEC-06.
6. **Populate Construction / Materials.** Code basis (API 650 Modified) from DBM; sweet-vs-sour service treatment from `PACKAGE_REGISTER.csv` plus rendered `26020-Package_Requirements.docx` heading 45 once available.
7. **Populate Interfaces.** Use the enumerated interface set from `PACKAGE_REGISTER.csv` row PKG-093: Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports.
8. **Reconcile open conflicts.** For each row in the `Guidance.md` Conflict Table (CONF-093-02-01..05), either close (with source) or leave TBD with the conflict ID.
9. **Cross-check with `DEL-093-01` Scope of Work** for consistency on equipment list, package boundary, and responsibility assignment (EPC Integrator owns integration; Package Vendor owns package engineering/design/documentation/equipment).
10. **Validate completeness.** All `Datasheet.md` rows either carry a source citation (`SourcePath` + `SectionRef`) or `location TBD`.
11. **Update `_STATUS.md`** via `tools/scaffolding/write_status.sh` only when transitioning `OPEN → INITIALIZED` after Pass 1/2 (or to later states per project lifecycle).
12. **Write run record** to `_run_records/TASK_RUN_<timestamp>.md` summarising sources read, conflicts opened, and TBDs raised.

## Verification

- Twelve Specification requirements (REQ-093-02-001 through REQ-093-02-012) are present and source-cited or explicitly TBD.
- `Datasheet.md` Attributes section names TK-9060-2 and TK-9070-2 explicitly and shows 2 x 3,800 bbl rather than the 7-tank DBM family.
- Interface matrix in `Datasheet.md` covers every interface type enumerated in `PACKAGE_REGISTER.csv` row PKG-093.
- Conflict Table in `Guidance.md` contains at least CONF-093-02-01..05 until human ruling closes them.
- No metadata files other than `_STATUS.md` have been modified.
- All four documents exist after the run.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file) — the produced documents.
- `_STATUS.md` — state transition record (OPEN → INITIALIZED).
- `_run_records/TASK_RUN_<timestamp>.md` — durable run report including sources read, tools used (none deterministic in this skill), TBDs raised, and conflict register.
