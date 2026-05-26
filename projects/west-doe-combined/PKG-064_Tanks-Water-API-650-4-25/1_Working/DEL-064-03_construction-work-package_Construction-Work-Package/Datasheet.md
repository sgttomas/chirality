# Datasheet — DEL-064-03 Construction Work Package

Production unit: EPC Integrator Construction Work Package for PKG-064 "Tanks, Water (API 650) 4-25".

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-064-03_construction-work-package | `_CONTEXT.md` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | PKG-064 | `_CONTEXT.md` |
| Package Name | Tanks, Water (API 650) 4-25 | PACKAGE_REGISTER.csv (PKG-064) |
| Workbook Row | 96 | PACKAGE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv |
| CoA Tracking Number | 26020-01-19-002 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv |
| Type | EPC Construction Work Package | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| Facility | West Doe Deepcut expansion, 04-25 | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-01 Facility Identity |
| Site (LSD) | 04-25-80-15W6, ~22.2 km north of Dawson Creek, BC | DBM-Deepcut SEC-01 |
| Field construction party | Tourmaline Oil Corporation | DBM-Deepcut SEC-01 Construction Responsibility |

## Attributes — Equipment Carried Within This Construction Work Package

| Tag | Description | Quantity | Source |
|---|---|---:|---|
| TK-5317-1 | Process Water Storage Tank | 1 | DBM-Deepcut equipment/tag table (row 102 / Tanks, Water (API 650) 2) |
| TK-5318-1 | Process Water Storage Tank | 1 | DBM-Deepcut equipment/tag table (row 102 / Tanks, Water (API 650) 2) |

Aggregate: two (2) Process Water Storage Tanks. (Workbook package row uses the descriptor "Two (2) 2,000 bbl Process Water Storage Tank"; per-tank volume `2,000 bbl` is asserted by the workbook scope ledger entry SOW-0235.)

ASSUMPTION: Tags TK-5317-1 and TK-5318-1 correspond to the workbook package "Tanks, Water (API 650) 4-25" (PKG-064). The DBM equipment table identifies them under the package label "Tanks, Water (API 650) 2" with the "(x2, 4-25)" suffix; cross-walking by facility, count, and process service supports the mapping. See Conflict Table in `Guidance.md`.

## Conditions — Design and Service Conditions Carried Into Construction

| Parameter | Value | Source |
|---|---|---|
| Service | Sweet Produced Water & Process Water (per workbook) / Process Water (per DBM-Deepcut narrative) | SOW-0234, SOW-0235; DBM-Deepcut SEC- (process water make-up reference); see Conflict Table |
| Tank quantity | 2 | SOW-0235; DBM equipment table |
| Per-tank capacity | 2,000 bbl | SOW-0235 |
| Design code | Modified API 650 (atmospheric) | SOW-0235; DBM-Deepcut Produced Water Tank design row (analogous basis) |
| Design pressure | 32 oz; 1.0 oz vacuum | SOW-0235 |
| External insulation | Required | SOW-0235 |
| External heating | Required to prevent freezing (arctic / sub-arctic) | SOW-0235 |
| Blanket gas | LP fuel gas blanket to maintain above atmospheric pressure | SOW-0235 |
| Fluid character | Non-sour, clean treated water | SOW-0235 |
| Site ambient design temperature range | -40 °C (min) to 60 °C (max) | SOW-0236 |
| Operating pressure | Atmospheric | SOW-0236 |
| Operating temperature | TBD for Item No. 1 | SOW-0236 |
| Design flow (Item No. 1 to Amine Surge Tank) | 0.55 m3/h continuous (TBD) | SOW-0236 |
| Other throughputs | TBD | SOW-0236 |
| Hazard area / site classification | TBD — site geotechnical and area classification documents not in scope of this register | location TBD |

## Construction — Scope and Responsibility Carried Into Construction Work Package

This deliverable describes how PKG-064 will be physically installed, built, inspected, turned over, and tied into the larger facility systems (per `_CONTEXT.md` and DELIVERABLE_REGISTER.csv).

Per-activity responsibility basis from DBM-Deepcut SEC-01 "Construction Responsibility":

| Construction activity | Responsibility basis (DBM) |
|---|---|
| Construction management | Tourmaline field construction scope |
| Grading, piling, and foundation work | Tourmaline field construction scope |
| Plant roads | Tourmaline field construction scope |
| Off-loading of modules and equipment at site | Tourmaline field construction scope |
| Setting tanks, modules, and equipment on foundations | Tourmaline field construction scope |
| Mechanical hookup of equipment and interconnecting piping | Tourmaline field construction scope |
| Installation of shipped-loose instruments, valves, and components | Tourmaline field construction scope |
| Installation of miscellaneous structural supports | Tourmaline field construction scope |
| Installation of interconnecting piping to ISBL/OSBL tie-in points | External interface; per-tie-in responsibility to be confirmed |
| Field installation of home-run cables; electrical terminations | Tourmaline field construction scope |
| Area lighting | Tourmaline field construction scope |

Scope explicitly excluded from the Package Vendor and assigned "by others" (i.e., to be executed by the EPC Integrator construction scope) per SOW-0236: foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc.

## Construction — Interface Activities Carried Into Construction Work Package

Carried from INTERFACE_REGISTER.csv (PKG-064 rows, all `RequiresEPCManagement = YES`):

| Interface ID | Interface Type |
|---|---|
| IFC-53CAD5DFB7 | Process Piping |
| IFC-570DF70935 | Relief / Flare / Vent |
| IFC-18BD52EF1B | Drain / Containment |
| IFC-20C8E797F3 | Grounding / Bonding |
| IFC-0FE674AE2E | Area / Exterior Lighting |
| IFC-54E4476E7C | Cathodic Protection |
| IFC-715AD7086B | I&C / Control Cabling |
| IFC-73210D3073 | Grading / Site Drainage / Spill Containment |
| IFC-BB6B4BD965 | Structural / Foundations / Supports |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-064-03)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-064)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (SOW-0233 .. SOW-0236)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` (PKG-064 rows)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-01 Construction Responsibility; Atmospheric Tank and Plant Spacing; Produced Water tank basis; equipment/tag table rows 99, 102)
- `_Sources/26020-Package_Requirements.docx` (package heading 19) — listed in `_REFERENCES.md`; not directly readable in markdown form during this run; relevant scope content carried via SCOPE_LEDGER.csv extractions and SOW-* rows.
