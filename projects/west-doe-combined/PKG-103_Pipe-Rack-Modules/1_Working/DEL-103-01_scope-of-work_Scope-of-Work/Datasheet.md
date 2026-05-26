# Datasheet — DEL-103-01 Scope of Work (Pipe Rack Modules)

> Descriptive identity, attributes, and conditions for the EPC Integrator Scope of Work covering package PKG-103 "Pipe Rack Modules". Source-grounded per the Gate-07 PROJECT_DECOMP snapshot and DBM-Comp_and_Liquids.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-103-01_scope-of-work` | `_CONTEXT.md`; DELIVERABLE_REGISTER row 584 |
| Name | Scope of Work | DELIVERABLE_REGISTER row 584 |
| Parent Package | `PKG-103` Pipe Rack Modules | PACKAGE_REGISTER row 104 |
| Workbook Tracking Number | `26020-03-36-003` | PACKAGE_REGISTER row 104 |
| Workbook Row | 104 | PACKAGE_REGISTER row 104 |
| WBS | 03 | PACKAGE_REGISTER row 104 |
| Discipline | Structural | PACKAGE_REGISTER row 104; `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | DELIVERABLE_REGISTER row 584 |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER row 584; Gate 6 disposition (INTERFACE_REGISTER rows 909-917) |
| Covers Scope Item | `SOW-0259` | SCOPE_LEDGER row 260 |
| Supports Objectives | OBJ-002, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | DELIVERABLE_REGISTER row 584; OBJECTIVE_REGISTER |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Workbook-defined Structural package for 'Pipe Rack Modules' under WBS 03 with recorded physical interfaces | PACKAGE_REGISTER row 104 |
| Scope-item statement | Carry the workbook-defined Structural package 'Pipe Rack Modules' as a distinct flat project package for WBS 03 | SCOPE_LEDGER row 260 (SOW-0259) |
| Gate 6 design ownership | Pipe racks and pipe rack modules are designed exclusively by the EPC Integrator | INTERFACE_REGISTER rows 909-917 (Gate 6 disposition note) |
| Vendor-package ownership model | None — EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred | PACKAGE_REGISTER row 104 |
| Package exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER row 104 |
| Hazardous area classification | Outdoor pipe racks are general purpose non-hazardous areas unless detailed classification drawings identify otherwise | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md line 722 |
| Tagged equipment list | TBD — no rack-level equipment tag list present in accessible sources; ASSUMPTION: to be developed by EPC Integrator from plot plan/model (see PACKAGE_REGISTER row 104 note: "Rack-supported commodities should be confirmed against plot plan/model") |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Physical interface types in scope | Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; EHT; I&C / Control Cabling; Communications / Network; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | PACKAGE_REGISTER row 104; INTERFACE_REGISTER rows 909-917 |
| Civil/structural facility context | Pipe racks listed within Civil and infrastructure scope alongside grading, foundations, roads, buildings, electrical buildings, field interconnections, lighting, fencing, security | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md line 38 |
| Foundation/support context | Pipe rack supports listed under civil scope (grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, security); final geotechnical report required before foundation design closure | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md line 688 |
| Foundation design loads | Equipment loads, snow/wind/seismic design criteria, frost protection, vibration, settlement, and maintenance access; pipe racks called out as requiring equipment-specific foundation and anchorage checks | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md line 700 |
| Final geotechnical report | Required upstream of foundation design closure (general DBM constraint, applies to rack supports) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md line 688 |
| Open-issue carrier | DEC-001 attached to SOW-0259 | SCOPE_LEDGER row 260 |

## Construction

| Item | Value | Source |
|---|---|---|
| Package classification | Modular structural package (per name "Pipe Rack Modules"); ASSUMPTION: rack modules are shop-fabricated and field-erected — exact modular split is `TBD` (location TBD in accessible sources) | PACKAGE_REGISTER row 104 (package name); ASSUMPTION |
| Rack-supported commodities | To be confirmed against plot plan/model | PACKAGE_REGISTER row 104 note |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record | DELIVERABLE_REGISTER row 584; `_CONTEXT.md` |
| Companion deliverables in package | DEL-103-02 Package Datasheet; DEL-103-03 Construction Work Package; DEL-103-04 EPC/Structural Discipline Production Package | SCOPE_LEDGER row 260; DELIVERABLE_REGISTER rows 585-587 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- Gate-07 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row 104 (PKG-103)
  - `DELIVERABLE_REGISTER.csv` row 584 (DEL-103-01)
  - `SCOPE_LEDGER.csv` row 260 (SOW-0259)
  - `INTERFACE_REGISTER.csv` rows 909-917 (PKG-103 interfaces; Gate 6 EPC-only disposition note)
  - `OBJECTIVE_REGISTER.csv` rows 3, 6-11 (OBJ-002, OBJ-005..OBJ-010)
- DBM source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 38, 688, 700, 722)
- Workbook (binary, not directly text-readable here): `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 104 — content mirrored in PACKAGE_REGISTER row 104
- Workbook (binary): `_Sources/26020-Package_Requirements.docx` — no PKG-103-specific package heading located in accessible derivative sources; `location TBD`
