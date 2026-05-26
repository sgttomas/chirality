# Datasheet — DEL-097-01 Scope of Work

Deliverable type: EPC Scope of Work (descriptive datasheet for the package-level SoW).

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-097-01_scope-of-work` | `_CONTEXT.md` |
| DeliverableName | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-097` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 88 |
| Parent Package Name | Tanks, Condendate (API 650) 3-25 | `PACKAGE_REGISTER.csv` row 88 (spelling preserved from workbook) |
| Workbook Tracking Number | 26020-03-19-006 | `PACKAGE_REGISTER.csv` row 88 |
| WBS | 03 | `PACKAGE_REGISTER.csv` row 88 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 88 |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0201`, `SOW-0202`, `SOW-0203`, `SOW-0204` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 492 |

## Attributes (Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Package function | C5+ Condensate Storage Tanks | `PACKAGE_REGISTER.csv` row 88; `SOW-0202` |
| Basic scope (workbook) | Supply Four (4) 3,800 bbl Condensate Product Storage Tanks | `PACKAGE_REGISTER.csv` row 88; `SOW-0202`; `26020-Package_Requirements.docx` heading 49 (Basic scope) |
| Governing tank code | Modified API 650 | `SCOPE_LEDGER.csv` `SOW-0203`; `26020-Package_Requirements.docx` heading 49 |
| Blanket gas system standard | API 2000 | `SCOPE_LEDGER.csv` `SOW-0203` |
| Internal coating | Devchem 253 (floors, walls, roof) | `SCOPE_LEDGER.csv` `SOW-0203`; cross-reference DBM `Produced-water tanks ... Devchem 253` confirms coating product line — `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC describing produced-water tanks |
| Insulation | Non-insulated atmospheric tanks (winter temperature maintenance may require recycle) | `SCOPE_LEDGER.csv` `SOW-0203` |
| Per-tank fittings | PVRV, EPRV, VRU header connection, blanket-gas connection | `SCOPE_LEDGER.csv` `SOW-0203` |
| Fill limit | Maximum fill 90 % shutdown | `SCOPE_LEDGER.csv` `SOW-0203` |
| Fill rate basis | Tank nozzles sized so plant design capacity can fill a single tank | `SCOPE_LEDGER.csv` `SOW-0203` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating pressure | Atmospheric (ambient) | `SCOPE_LEDGER.csv` `SOW-0204` |
| Operating temperature | 0 °C (min) / 40 °C (max) | `SCOPE_LEDGER.csv` `SOW-0204` |
| Design pressure | 32 oz test pressure | `SCOPE_LEDGER.csv` `SOW-0204` |
| Design temperature | -40 °C (min) / 60 °C (max) | `SCOPE_LEDGER.csv` `SOW-0204` |
| Capacity / design throughput | 94,940 kg/h; 3,187 Am3/d (Preliminary Design conditions) | `SCOPE_LEDGER.csv` `SOW-0204` |
| Service | C5+ stabilized condensate (product) | `PACKAGE_REGISTER.csv` row 88; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling |
| Site ambient minimum (facility) | -40 °C facility design minimum ambient | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis |

## Construction / Equipment Scope (in package)

- Four (4) 3,800 bbl Condensate Product Storage Tanks — modified API 650, atmospheric, non-insulated. (`SCOPE_LEDGER.csv` `SOW-0203`)
- Tank internal coating: Devchem 253 floor/wall/roof. (`SCOPE_LEDGER.csv` `SOW-0203`)
- Per-tank: pressure-vacuum relief valve (PVRV) for vacuum or modulating pressure relief; emergency pressure relief valve (EPRV) sized for the single worst-case relief event; VRU header tie-in connection; blanket-gas connection. (`SCOPE_LEDGER.csv` `SOW-0203`)
- Blanket gas system per API 2000. (`SCOPE_LEDGER.csv` `SOW-0203`)
- Source list ends "tank." indicating truncated/incomplete enumeration in the workbook excerpt — remaining per-tank fittings: `TBD` pending review of full `26020-Package_Requirements.docx` heading 49 text.

## Exclusions (By Others)

- Foundations, mounting tanks at site, electrical / instrumentation, platforms, staircases, etc. (`SCOPE_LEDGER.csv` `SOW-0204`)
- Package-specific exclusions beyond the above: `TBD` (`PACKAGE_REGISTER.csv` row 88 records "TBD; no package-specific exclusions stated in source materials").

## Responsibility Split

| Party | Responsibility | Source |
|---|---|---|
| Package Vendor | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` row 88 (Responsibility model) |
| EPC Integrator | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` row 88; `_CONTEXT.md` |

## Interface Inventory (declared at package level)

| Interface Type | Source |
|---|---|
| Process Piping | `INTERFACE_REGISTER.csv` IFC-FA0F12EEB4 |
| Relief / Flare / Vent | `INTERFACE_REGISTER.csv` IFC-0DF0C05265 |
| Drain / Containment | `INTERFACE_REGISTER.csv` IFC-2244057493 |
| Grounding / Bonding | `INTERFACE_REGISTER.csv` IFC-EC6370C813 |
| Area / Exterior Lighting | `INTERFACE_REGISTER.csv` IFC-E5572113AF |
| Cathodic Protection | `INTERFACE_REGISTER.csv` IFC-D4D71DF1BB |
| I&C / Control Cabling | `INTERFACE_REGISTER.csv` IFC-3B37C71812 |
| Grading / Site Drainage / Spill Containment | `INTERFACE_REGISTER.csv` IFC-BDD5760590 |
| Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` IFC-0AE3FE186A |

## Anticipated Artifacts Produced By This Deliverable

- Package scope of work
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

(Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 492.)

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `PACKAGE_REGISTER.csv` row 88 (`PKG-097`)
- `DELIVERABLE_REGISTER.csv` row 492 (`DEL-097-01_scope-of-work`)
- `SCOPE_LEDGER.csv` `SOW-0201`..`SOW-0204`
- `INTERFACE_REGISTER.csv` rows for `PKG-097`
- `OBJECTIVE_REGISTER.csv` `OBJ-002`..`OBJ-010`
- `26020-Package_Requirements.docx` package heading 49 (binary source; specific clause text outside the workbook-extracted ledger is `location TBD`)
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (facility DBM — Condensate Storage and Product Handling; Site Basis)

Markings: `FACT` items above are sourced from the Gate-07 published registers and DBM. Items marked `TBD` reflect text not present in the available source slices. The objective-to-deliverable mapping is `ASSUMPTION` (package-grouping heuristic).
