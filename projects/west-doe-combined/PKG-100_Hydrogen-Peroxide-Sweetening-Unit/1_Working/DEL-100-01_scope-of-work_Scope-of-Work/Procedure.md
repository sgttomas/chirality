# Procedure — DEL-100-01 Scope of Work (PKG-100 Hydrogen Peroxide Sweetening Unit)

## Purpose

Produce the EPC Integrator's `PKG-100` Scope of Work artifact set such that the Specification requirements (SPEC-100-01-R01 through R11) are satisfied with source-grounded content and explicit `TBD` markers where source is not locally accessible.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-100 row)
  - `DELIVERABLE_REGISTER.csv` (DEL-100-01 row and sibling DEL-100-02 … DEL-100-06)
  - `SCOPE_LEDGER.csv` (SOW-0107 through SOW-0110)
  - `ARTIFACT_REGISTER.csv` (DEL-100-01 rows: ART-CF28BC5992, ART-DEB15FAA69, ART-2ED2F833EB, ART-5BA6AFE0FD, ART-B77E9A5546)
  - `INTERFACE_REGISTER.csv` (13 PKG-100 rows)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-100-01 rows); `OBJECTIVE_SCOPE_MAP.csv` for PKG-100 corroboration.
- ASSUMPTION: where deeper source extraction is needed, retrieve source slices from `26020-Package_Requirements.docx` package heading 52 and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (residing in `_Sources/`). If not locally extracted, treat as `location TBD`.
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-100-02` … `DEL-100-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-100 row and `DELIVERABLE_REGISTER.csv` DEL-100-01 row. Verify workbook row 63, WBS 03, CoA tracking 26020-03-27-001 (also 26020-03-PT-27-001), discipline Mechanical, package name "Hydrogen Peroxide Sweetening Unit".
2. **Function and equipment.** Reproduce SOW-0108 (basic scope, process function) and SOW-0109 (major included equipment: 400 BBL H₂O₂ storage tank; pumps; static mixer; reactors; self-framing site building) as the package function and tagged-equipment artifacts. Mark vendor-to-design items explicitly.
3. **Conditions and integration narrative.** Reproduce SOW-0110 operating values (24,154 BBL/D; 9 °C; 340.54 kPag; 160 m³/h; ambient −40/+35 °C; 575 V/3PH/60Hz motors with DOL/VFD starting fed from 600 V MCC) and the "by others" list (interconnecting piping, DCS integration, foundations, electrical supply to MCC). Explicitly state that final Design conditions are TBC.
4. **Interface enumeration.** List the 13 PKG-100 interface types from `INTERFACE_REGISTER.csv`: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
5. **Responsibility assignment record.** Reproduce the responsibility model verbatim from `PACKAGE_REGISTER.csv` PKG-100 (Package Vendor scope; EPC Integrator integration scope).
6. **Source basis.** List Workbook Packages row 63, `26020-Package_Requirements.docx` package heading 52, `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; label `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` as budgetary-only.
7. **Objectives + scope items.** Echo `{OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}` and `{SOW-0107, SOW-0108, SOW-0109, SOW-0110}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `SCOPE_LEDGER.csv`.
8. **TBD audit.** Any design value (final design P, T, capacity beyond stated operating values, materials, code citations, reactor sizing, pump capacity) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer.
9. **Conflict capture.** Record open ownership/extraction conflicts in the Guidance Conflict Table (CONF-100-01-01 DCS split; CONF-100-01-02 building supply/erection; CONF-100-01-03 design-conditions extraction; CONF-100-01-04 H₂O₂ compatibility/codes) with proposed authority and `TBD` human ruling.
10. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-100, Hydrogen Peroxide Sweetening Unit, 400 BBL H₂O₂ Storage Tank, Static Mixer, Hydrogen Peroxide Reactors, Hydrogen Peroxide Pumps), the same scope items, the same objectives, and the same 13 interface types.
11. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-100 row in `PACKAGE_REGISTER.csv` (every field). |
| 2 | SOW-0108 and SOW-0109 text is present; vendor-to-design items are flagged. |
| 3 | Operating values appear verbatim or as exact unit-converted equivalents; "Design conditions TBC" is explicit. |
| 4 | The 13 interface types match `INTERFACE_REGISTER.csv` for PKG-100 exactly (set equality). |
| 5 | Responsibility text preserves Vendor/EPC split per `PACKAGE_REGISTER.csv` ResponsibilityModel. |
| 6 | Source basis list cites Workbook row 63, package requirements doc heading 52, DBM-Comp_and_Liquids; budgetary go-by labeled informational. |
| 7 | Objective set equals `{OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`; scope set equals `{SOW-0107, SOW-0108, SOW-0109, SOW-0110}`. |
| 8 | No unsourced numeric value or material exists outside a `TBD` cell. |
| 9 | Conflict Table present in Guidance with at least the four CONF-100-01-0x items, or explicit "resolved" if resolved. |
| 10 | Same terms, equipment names, and lists appear in all four documents (no aliases). |
| 11 | `_STATUS.md` State transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING, and any NEEDS_HUMAN_RULING items.
- Conflict Table entries in `Guidance.md` carry forward as `NEEDS_HUMAN_RULING` items into the run record.
