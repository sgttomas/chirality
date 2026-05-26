# Datasheet: DEL-103-04 — EPC / Structural Discipline Production Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-103-04_epc-structural-discipline-production-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-103-04 |
| Name | EPC / Structural Discipline Production Package | `DELIVERABLE_REGISTER.csv` row DEL-103-04 |
| ParentPackageID | `PKG-103` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-103 |
| PackageName | Pipe Rack Modules | `PACKAGE_REGISTER.csv` row PKG-103 |
| WorkbookID / Row | 103 / 104 | `PACKAGE_REGISTER.csv` row PKG-103 |
| WBS | 03 | `PACKAGE_REGISTER.csv` row PKG-103 |
| CoA Tracking | 26020-03-36-003 | `PACKAGE_REGISTER.csv` row PKG-103 |
| Discipline | Structural | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Type | EPC/Discipline Production Unit | `DELIVERABLE_REGISTER.csv` row DEL-103-04 |
| Responsible Party | TBD — EPC Integrator or discipline subcontractor as assigned | `DELIVERABLE_REGISTER.csv`; `PACKAGE_REGISTER.csv` (responsibility model is source-dependent) |
| Covers Scope Items | `SOW-0259` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-103-04 |
| Supports Objectives | `OBJ-002`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` SupportsObjectives |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope description | "Workbook-defined Structural package for 'Pipe Rack Modules' under WBS 03 with recorded physical interfaces." | `PACKAGE_REGISTER.csv` ScopeDescription, PKG-103 |
| Inclusion criteria | Workbook row 104; discipline Structural; WBS 03. Applicable interface types: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; EHT; I&C / Control Cabling; Communications / Network; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` InclusionCriteria, PKG-103 |
| Exclusions | TBD; no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` Exclusions, PKG-103 |
| Interface types (declared) | Process Piping (IFC-1B5D83EC66); Utility Piping (IFC-AECC45897E); Relief / Flare / Vent (IFC-933A9B9DC3); Electrical Power (IFC-3268483707); EHT (IFC-489CEA5AA8); I&C / Control Cabling (IFC-FC76A7E07D); Communications / Network (IFC-38D5605A15); Grading / Site Drainage / Spill Containment (IFC-E2FEA8FA23); Structural / Foundations / Supports (IFC-BC9813EE49). All marked YES (applicable). | `INTERFACE_REGISTER.csv` rows for PKG-103 |
| Production-unit role | Non-vendor package scope, carried conservatively from workbook and DBM support. | `DELIVERABLE_REGISTER.csv` Description, DEL-103-04; `_CONTEXT.md` Scope |
| Design responsibility note | Gate 6 disposition: "Pipe racks and pipe rack modules are designed exclusively by the EPC Integrator." Carried on every PKG-103 interface fact. | `INTERFACE_REGISTER.csv` rows for PKG-103 (Note field) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source-set completeness | Detailed non-vendor discipline requirements are source-limited and remain open for Gate 5 disposition. | `DELIVERABLE_REGISTER.csv` Notes, DEL-103-04; `_CONTEXT.md` Notes |
| Vendor-package model | No separate vendor-package ownership inferred; EPC Integrator owns pipe rack and pipe rack module design per Gate 6 disposition. | `PACKAGE_REGISTER.csv` ResponsibilityModel, PKG-103; `INTERFACE_REGISTER.csv` Note column |
| Open issues / package flag | OpenIssue = FALSE | `PACKAGE_REGISTER.csv` OpenIssue, PKG-103 |
| Maturity gate target | Gate 5 disposition required for full closure. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` Notes |
| Site/environmental basis | -40 deg C to +35 deg C ambient; elevation 673 m AMSL; snow/wind/seismic per NBCC; geotechnical values are placeholders until the final geotechnical report is accepted. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Site and Civil Conditions" |
| Rack-supported commodities | Should be confirmed against plot plan/model (carried as note on every PKG-103 interface). | `INTERFACE_REGISTER.csv` Note, rows for PKG-103 |

## Construction

| Item | Value | Source |
|---|---|---|
| Anticipated artifacts | Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts, DEL-103-04 |
| Discipline deliverable register | TBD — to be defined by the discipline production team within source-supported scope. | `_CONTEXT.md` Anticipated Artifacts |
| Closure record | A source-limited requirements closure record is required to capture remaining scope gaps for human ruling. | `DELIVERABLE_REGISTER.csv` Notes, DEL-103-04 |
| Foundation basis | Driven steel piles as default support for pipe racks and modules unless detailed engineering confirms otherwise. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Piles and Foundations" |
| Steel design basis | CSA G40.20/G40.21 350W for W-flange and HSS; 300W for channels, plates, and angles; design per CAN/CSA-S16. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Governing Civil and Structural Basis" |
| Module erection basis | Civil/building inventory uses module labels per DBM module/erection table; pipe rack modules per se are not enumerated as named modules in the DBM erection table — shop vs. field erection split is TBD for the pipe rack modules themselves. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Buildings and Miscellaneous Facilities" module table (PKG-103 rack modules not individually listed; location TBD) |
| Construction interfaces | Nine applicable physical interface types (see Attributes). | `INTERFACE_REGISTER.csv` rows for PKG-103 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot) — row DEL-103-04
- `PACKAGE_REGISTER.csv` (GATE-07 snapshot) — row PKG-103
- `ARTIFACT_REGISTER.csv` (GATE-07 snapshot) — DEL-103-04 artifact rows (none declared for DEL-103-04 in current snapshot; ASSUMPTION based on grep result)
- `INTERFACE_REGISTER.csv` (GATE-07 snapshot) — PKG-103 interface rows (nine applicable interfaces)
- `OBJECTIVE_DELIVERABLE_MAP.csv` (GATE-07 snapshot) — OBJ-002, OBJ-005..010 (package-grouping heuristic; ASSUMPTION)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Civil Scope; Governing Civil and Structural Basis; Geotechnical and Topographical Assumptions; Site Grading and Surface Water Management; Piles and Foundations; Buildings and Miscellaneous Facilities; External Dependencies
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Site and Civil Conditions; Foundations and Structural Supports; Area Classification (pipe rack non-hazardous baseline)
- Workbook Packages row 104 — referenced but not opened as a source slice (location TBD inside `_Sources/26020-Packages_Interfaces_4_export.xlsx`).
