# Datasheet: DEL-041-02 — Package Datasheet (PKG-041)

> EPC Integrator technical handoff datasheet for the 13.8 kV, 3.0 MW Standby Generator Building (490-1). Source-grounded against the Gate-07 PROJECT_DECOMP snapshot. Detailed equipment ratings beyond what is carried in the decomposition registers are marked `TBD` pending access to the workbook source (`_Sources/26020-Packages_Interfaces_4_export.xlsx`, row 43) and the package design basis.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-041-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md`; DELIVERABLE_REGISTER row `DEL-041-02_package-datasheet` |
| Parent Package ID | `PKG-041` | `_CONTEXT.md` |
| Workbook ID | 41 | PACKAGE_REGISTER `PKG-041` |
| Workbook Row | 43 | PACKAGE_REGISTER `PKG-041` |
| Package Name | 13.8 kV, 3.0 MW Standby Generator Building (490-1) | PACKAGE_REGISTER `PKG-041` |
| CoA Tracking Number | 26020-01-30-032 | PACKAGE_REGISTER `PKG-041` |
| WBS | 01 | PACKAGE_REGISTER `PKG-041` |
| Discipline | Electrical | PACKAGE_REGISTER `PKG-041`; `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | DELIVERABLE_REGISTER `DEL-041-02_package-datasheet` |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER `DEL-041-02_package-datasheet` |
| Package Role | authoritative companion register row | PACKAGE_REGISTER `PKG-041` |
| Covers Scope Item | `SOW-0042` | DELIVERABLE_REGISTER `DEL-041-02_package-datasheet` |

## Attributes

### Functional identity (source-supported)

| Attribute | Value | Source |
|---|---|---|
| Package function (declarative) | Standby electrical generation building; vendor-engineered/-supplied package integrated by EPC into the facility | PACKAGE_REGISTER `PKG-041` ScopeDescription |
| Nominal medium-voltage rating | 13.8 kV (package name) | PACKAGE_REGISTER `PKG-041` Name |
| Nominal generator capacity | 3.0 MW (package name) | PACKAGE_REGISTER `PKG-041` Name |
| Building tag | 490-1 (package name) | PACKAGE_REGISTER `PKG-041` Name |
| Responsibility split | Package Vendor: engineering, design, vendor documentation, physical equipment package. EPC Integrator: facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration. | PACKAGE_REGISTER `PKG-041` ResponsibilityModel |

### Equipment and ratings (source TBD beyond decomposition)

| Attribute | Value | Source |
|---|---|---|
| Tagged equipment list | TBD — not enumerated in the locally accessible decomposition registers; resolve from `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 43 and/or `26020-Package_Requirements.docx` (location TBD) | source-slice unavailable |
| Generator prime mover type | TBD (ASSUMPTION: diesel reciprocating engine typical of 3 MW standby gensets, but not source-stated) | not source-stated |
| Generator electrical configuration (phases, frequency, pf, voltage regulation class) | TBD | not source-stated |
| Standby duty rating class (e.g., ISO 8528 standby/prime/continuous) | TBD | not source-stated |
| Fuel system (tank size, supply mode, days autonomy) | TBD | not source-stated |
| Switchgear/protection within building | TBD | not source-stated |
| Building envelope (dimensions, materials, sound attenuation, fire rating) | TBD | not source-stated |
| HVAC / combustion air / radiator cooling | TBD | not source-stated |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service classification | Standby (per package name) | PACKAGE_REGISTER `PKG-041` Name |
| Site environmental envelope (ambient temperature range, elevation, seismic, snow, wind, classified-area extents) | TBD | not source-stated |
| Electrical system tie-in voltage | 13.8 kV nominal | PACKAGE_REGISTER `PKG-041` Name |
| Grounding system reference | TBD; required interface present per INTERFACE_REGISTER `IFC-134CB10F1D` | INTERFACE_REGISTER PKG-041 |
| Hazardous-area classification at package boundary | TBD | not source-stated |

## Construction

| Item | Value | Source |
|---|---|---|
| Foundations / supports | Required interface present (Structural / Foundations / Supports) | INTERFACE_REGISTER `IFC-D0146B1F8C` |
| Grading, drainage, spill containment | Required interface present | INTERFACE_REGISTER `IFC-B9452850B5` |
| Drain / containment routing | Required interface present | INTERFACE_REGISTER `IFC-1528C860A4` |
| Utility piping tie-ins | Required interface present | INTERFACE_REGISTER `IFC-508C53EB72` |
| Building HVAC / services | Required interface present | INTERFACE_REGISTER `IFC-7D36256CF5` |
| Fire & gas / safety systems | Required interface present | INTERFACE_REGISTER `IFC-5F7FE5FA2A` |
| Area / exterior lighting | Required interface present | INTERFACE_REGISTER `IFC-8E23F09E7C` |
| Maintenance access provisions | Required interface present | INTERFACE_REGISTER `IFC-57828C08C8` |
| Communications / network connections | Required interface present | INTERFACE_REGISTER `IFC-FEEE41EDAA` |
| I&C / control cabling tie-ins | Required interface present | INTERFACE_REGISTER `IFC-1E6785E532` |
| Electrical power tie-ins | Required interface present | INTERFACE_REGISTER `IFC-004BB1B385` |
| Construction tolerances, weld/coating specs, painting | TBD | not source-stated |

## Interface Requirements Matrix (workbook X-column facts)

Per the artifact register, workbook interface facts are carried in this datasheet as evidence rather than separate deliverables (`_CONTEXT.md` Notes).

| Interface Type | Interface ID | Discipline | Applicable | Source |
|---|---|---|---|---|
| Utility Piping | `IFC-508C53EB72` | Electrical | YES | INTERFACE_REGISTER |
| Drain / Containment | `IFC-1528C860A4` | Electrical | YES | INTERFACE_REGISTER |
| Electrical Power | `IFC-004BB1B385` | Electrical | YES | INTERFACE_REGISTER |
| Grounding / Bonding | `IFC-134CB10F1D` | Electrical | YES | INTERFACE_REGISTER |
| Area / Exterior Lighting | `IFC-8E23F09E7C` | Electrical | YES | INTERFACE_REGISTER |
| I&C / Control Cabling | `IFC-1E6785E532` | Electrical | YES | INTERFACE_REGISTER |
| Communications / Network | `IFC-FEEE41EDAA` | Electrical | YES | INTERFACE_REGISTER |
| Building HVAC / Services | `IFC-7D36256CF5` | Electrical | YES | INTERFACE_REGISTER |
| Fire & Gas / Safety Systems | `IFC-5F7FE5FA2A` | Electrical | YES | INTERFACE_REGISTER |
| Maintenance Access | `IFC-57828C08C8` | Electrical | YES | INTERFACE_REGISTER |
| Grading / Site Drainage / Spill Containment | `IFC-B9452850B5` | Electrical | YES | INTERFACE_REGISTER |
| Structural / Foundations / Supports | `IFC-D0146B1F8C` | Electrical | YES | INTERFACE_REGISTER |

Per-interface battery-limit values, sizing parameters, and tie-point coordinates: **TBD** (not present in INTERFACE_REGISTER; resolve from Workbook Packages row 43 source slices, location TBD).

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- GATE-07 PROJECT_DECOMP snapshot (`_GateSnapshots/GATE-07_Final_Published_2026-05-24/`):
  - `PACKAGE_REGISTER.csv` row `PKG-041`
  - `DELIVERABLE_REGISTER.csv` row `DEL-041-02_package-datasheet`
  - `ARTIFACT_REGISTER.csv` rows where `ParentDeliverableID = DEL-041-02_package-datasheet`
  - `INTERFACE_REGISTER.csv` rows where `ParentPackageID = PKG-041`
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (for `OBJ-001, OBJ-004..OBJ-010`)
- Workbook Packages row 43 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) — referenced but binary; source slice **location TBD**.
- `_Sources/26020-Package_Requirements.docx` — referenced at project level; package-specific slices **location TBD**.
