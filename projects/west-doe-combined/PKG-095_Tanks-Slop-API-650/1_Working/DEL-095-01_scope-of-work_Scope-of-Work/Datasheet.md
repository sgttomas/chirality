# Datasheet — DEL-095-01 Scope of Work (PKG-095 Tanks, Slop (API 650))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-095-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-095` — Tanks, Slop (API 650) | `PACKAGE_REGISTER.csv` row 91 |
| Workbook Row | 91 | `PACKAGE_REGISTER.csv` (WorkbookRow=91) |
| WBS | 03 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-03-19-004 (also reported as 26020-03-PT-19-004) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (basic scope) | Supply one slop storage tank for off-spec condensate or contaminated hydrocarbon liquids requiring segregation from on-spec condensate product. | `SCOPE_LEDGER.csv` SOW-0214; `26020-Package_Requirements.docx` package heading 47 (Basic scope) |
| Major Equipment | One API 650 modified atmospheric slop storage tank (tag `TK-9130-2`, ASSUMPTION — qualified as "likely" in source), with tank appurtenances, connections to relevant drain/recycle/truck-out systems, and standard tank instrumentation. | `SCOPE_LEDGER.csv` SOW-0215; `26020-Package_Requirements.docx` package heading 47 (Major included equipment) |
| Scope Notes (process integration) | Slop is off-spec condensate product or contaminated hydrocarbon liquid (including material contaminated with water, treating chemicals, or other hydrocarbons that make it unsuitable for on-spec product storage/export). Expected sources may include off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, treating-unit drains, and other contaminated hydrocarbon liquids. Final source list, disposition path, and tank design basis require process confirmation. | `SCOPE_LEDGER.csv` SOW-0216; `26020-Package_Requirements.docx` package heading 47 (Scope notes and open items) |
| Package Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration). | `PACKAGE_REGISTER.csv` PKG-095 ResponsibilityModel; ART-10E6586D28 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Atmospheric storage of off-spec condensate / contaminated hydrocarbon liquids (segregated from on-spec product). | `SCOPE_LEDGER.csv` SOW-0214/0216 |
| Operating regime | Continuous storage availability for slop receipt from off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, and treating-unit drains; truck-out / recycle disposition path. | `SCOPE_LEDGER.csv` SOW-0215/0216 — final disposition path requires process confirmation |
| Design pressures/temperatures | TBD — atmospheric (API 650 modified); specific design conditions reside in `26020-Package_Requirements.docx` package heading 47 detail text not locally extracted. | location TBD |
| Sizing / Capacity (volume, diameter, height) | TBD | location TBD |
| Materials of construction | TBD | location TBD |
| Design code | ASSUMPTION: API 650 (modified for atmospheric service) per package name and SOW-0215. Specific modifications, appendices, and design temperature exception status TBD. | `DELIVERABLE_REGISTER.csv` PackageName "Tanks, Slop (API 650)"; SOW-0215 |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | Mechanical equipment package supplied by Package Vendor; integrated into facility by EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Applicable interface types (package boundary integration) | Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-095 rows (9 rows); `PACKAGE_REGISTER.csv` InterfaceTypes |
| Drains / containment | Connections to relevant drain/recycle/truck-out systems; spill containment at site grading per interface type. | `SCOPE_LEDGER.csv` SOW-0215; `INTERFACE_REGISTER.csv` (Drain / Containment; Grading / Site Drainage / Spill Containment) |
| Tank instrumentation | Standard tank instrumentation (specific instrument list TBD). | `SCOPE_LEDGER.csv` SOW-0215 |

## Scope Items Covered

| Scope Item | Statement |
|---|---|
| `SOW-0213` | Carry workbook-defined vendor-responsible Mechanical package "Tanks, Slop (API 650)" as a distinct flat project package for WBS 03; Package Vendor owns engineering/design/equipment and EPC Integrator owns facility integration. |
| `SOW-0214` | Basic scope: Supply one slop storage tank for off-spec condensate or contaminated hydrocarbon liquids requiring segregation from on-spec condensate product. |
| `SOW-0215` | Major included equipment: One API 650 modified atmospheric slop storage tank (likely `TK-9130-2`), with tank appurtenances, connections to relevant drain/recycle/truck-out systems, and standard tank instrumentation. |
| `SOW-0216` | Scope notes / open items: slop definition, expected sources, and the open requirement for process confirmation of final source list, disposition path, and design basis. |

Source: `SCOPE_LEDGER.csv`.

## Objectives Supported

| Objective | Source |
|---|---|
| `OBJ-002` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-003` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-004` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-005` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-006` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-007` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-008` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-009` | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-010` | `OBJECTIVE_DELIVERABLE_MAP.csv` |

Objective association mode: `OBJECTIVE_DELIVERABLE_MAP.csv` provides explicit DEL-095-01 rows for each listed objective; this is an explicit mapping, not a heuristic association.

## References

- `_CONTEXT.md`; `_REFERENCES.md`; `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 snapshot: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Source basis (per `PACKAGE_REGISTER.csv` SourceRefRaw): Workbook Packages row 91; `26020-Package_Requirements.docx` package heading 47; Word Source Basis: PE definition of slop service plus 3-25 DBM/package-structure analog; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. Per `PACKAGE_REGISTER.csv`: no package-folder brief.md, DOCX, or PDF scope source found. Deliverable-specific source slices were NOT copied into the deliverable folder during PREPARATION; clause-level extraction beyond the SCOPE_LEDGER entries marked `location TBD` above.
