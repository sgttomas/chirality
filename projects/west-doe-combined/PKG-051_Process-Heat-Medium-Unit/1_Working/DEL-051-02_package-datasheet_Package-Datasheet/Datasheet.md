# Datasheet — DEL-051-02 Package Datasheet (Process Heat Medium Unit)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-051-02_package-datasheet | `_CONTEXT.md` |
| PackageID | PKG-051 | `_CONTEXT.md` |
| Package Name | Process Heat Medium Unit | `_CONTEXT.md`; Workbook Packages row (Packages = "Process Heat Medium Unit") |
| Package CoA Tracking Number | 26020-01-15-001 | `26020-Packages_Interfaces_4_export.xlsx` → Packages sheet, row for Process Heat Medium Unit |
| Package Tag (docx) | 26020-01-PT-15-001 | `26020-Package_Requirements.docx` Heading 1 (heading 6) |
| Workbook Row / Workbook ID | Row 79 / Workbook ID 51 | `_CONTEXT.md`; Workbook Packages sheet (ID # = 51) |
| Discipline | Mechanical | `_CONTEXT.md`; Workbook Packages sheet (Discipline = "Mechanical") |
| WBS | 01 | `26020-Packages_Interfaces_4_export.xlsx` (WBS = "01") |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |

## Attributes

### Process Function

| Attribute | Value | Source |
|---|---|---|
| System type | Closed-loop hot oil / heat medium heating system | `26020-Package_Requirements.docx` §"26020-01-PT-15-001 - Process Heat Medium Unit" → Basic Scope |
| Function | Provide heat to various process users in the facility via a pumped thermal heating fluid in a closed loop | docx → Basic Scope |
| Loop arrangement | Hot loop and cold loop; mixing of hot and cold heat medium used to supply optimum temperature | docx → Basic Scope |
| Heat medium fluid | Petro-Canada Petrotherm (ASSUMPTION on exact product spelling — docx text: "Petro Canada Peterotherm") | docx → Major Included Equipment |

### Modules

| Attribute | Value | Source |
|---|---|---|
| Supply Pump Module | One expansion tank, 3 pumps | docx → Basic Scope |
| Medium Heater Module | One medium heater, one heater blower, one air intake pre-heater | docx → Basic Scope |

## Conditions

### Expansion Tank

| Attribute | Value | Source |
|---|---|---|
| Orientation | Horizontal | docx → Major Included Equipment |
| Size & capacity | To be advised by vendor | docx → Major Included Equipment |
| Maximum fill at 274 °C | 85% (expansion volume to fill expansion tank max. 85% at 274 °C) | docx → Major Included Equipment |
| Operating pressure | 125 to 240 kPag (18 to 23 psig) — dependent on heat medium NPSHR | docx → Major Included Equipment |

### Heat Medium Pumps

| Attribute | Value | Source |
|---|---|---|
| Type | Single-stage vertical inline | docx → Major Included Equipment |
| Configuration | 3 × 66% | docx → Major Included Equipment |
| Design pressure | 2413 kPag (350 psig) | docx → Major Included Equipment |
| Operating pressure | 695 kPag (100 psig) | docx → Major Included Equipment |
| Operating temperature | TBD (docx truncates: "Operating pressure 695 Kpag (100 Psig) and temp.") |

### System Operating Temperatures

| Attribute | Value | Source |
|---|---|---|
| Assumed start-up temperature | 20 °C (68 °F) | docx → Major Included Equipment |
| Maximum bulk temperature | 260 °C (500 °F) | docx → Major Included Equipment |
| Expansion design reference temperature | 274 °C (used for expansion-tank fill limit) | docx → Major Included Equipment |

### Medium Heater Module

| Attribute | Value | Source |
|---|---|---|
| Heater count | 1 | docx → Basic Scope |
| Heater blower | 1 | docx → Basic Scope |
| Air intake pre-heater | 1 | docx → Basic Scope |
| Heater duty / design parameters | TBD (not stated in available source slice) |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Heat medium fluid type | Petro-Canada Petrotherm-family heat transfer fluid | docx (spelling per docx: "Peterotherm") |
| Pump arrangement | Vertical inline, 3-pump 66% configuration | docx |
| Expansion-tank orientation | Horizontal | docx |
| Materials of construction | TBD (not specified in source slice) |
| Insulation specification | TBD (not specified in source slice) |

## Physical Interface Summary

Interfaces marked "X" in the workbook interface row for Process Heat Medium Unit (source: `26020-Packages_Interfaces_4_export.xlsx`, Packages sheet, row ID# 51):

| Interface | Applicable | Source |
|---|---|---|
| Process Piping | Not marked | xlsx |
| Utility Piping | X | xlsx |
| Relief / Flare / Vent | Not marked | xlsx |
| Drain / Containment | X | xlsx |
| Electrical Power | X | xlsx |
| EHT | Not marked | xlsx |
| Grounding / Bonding | X | xlsx |
| Area / Exterior Lighting | X | xlsx |
| Cathodic Protection | Not marked | xlsx |
| I&C / Control Cabling | X | xlsx |
| Communications / Network | Not marked | xlsx |
| Building HVAC / Services | X | xlsx |
| Fire & Gas / Safety Systems | X | xlsx |
| Maintenance Access | X | xlsx |
| Grading / Site Drainage / Spill Containment | Not marked | xlsx |
| Structural / Foundations / Supports | X | xlsx |
| Product Loading | Not marked | xlsx |
| Pipeline / Pigging | Not marked | xlsx |
| Interface Review Notes | Not populated in source row | xlsx |

## Vendor Engineering Deliverables

- Source heading present in docx (`Vendor Engineering Deliverables`) but body is empty in the available source slice.
- TBD — to be enumerated from vendor scope-of-supply documentation once available.

## Interface Coordination Notes

- Source: docx → Interface Coordination Notes = "TBD."
- TBD — to be resolved during EPC interface coordination.

## References

- `_Sources/26020-Package_Requirements.docx` — Heading 1 "26020-01-PT-15-001 - Process Heat Medium Unit" (heading 6 by occurrence) with Heading 2 subsections Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Packages sheet, row ID# 51, Packages = "Process Heat Medium Unit", CoA Tracking Number = 26020-01-15-001.
- `_CONTEXT.md`, `_REFERENCES.md` (deliverable-local).
- Decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, INTERFACE_REGISTER.csv).
