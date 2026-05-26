# Datasheet: DEL-104-04 — EPC / Structural Discipline Production Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-104-04_epc-structural-discipline-production-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-104-04 |
| Name | EPC / Structural Discipline Production Package | `DELIVERABLE_REGISTER.csv` row DEL-104-04 |
| ParentPackageID | `PKG-104` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-104 |
| PackageName | Structural steel - outside of modules | `PACKAGE_REGISTER.csv` row PKG-104 |
| WorkbookID / Row | 104 / 105 | `PACKAGE_REGISTER.csv` row PKG-104 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-104 |
| CoA Tracking | 26020-01-36-004 | `PACKAGE_REGISTER.csv` row PKG-104 |
| Discipline | Structural | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Type | EPC/Discipline Production Unit | `DELIVERABLE_REGISTER.csv` row DEL-104-04 |
| Responsible Party | TBD — EPC Integrator or discipline subcontractor as assigned | `DELIVERABLE_REGISTER.csv`; `PACKAGE_REGISTER.csv` (responsibility model is source-dependent) |
| Covers Scope Items | `SOW-0260` | `SCOPE_LEDGER.csv` row SOW-0260; `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-008` (FACT — explicit rows in `OBJECTIVE_DELIVERABLE_MAP.csv` naming DEL-104-04) | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-104-04; `_CONTEXT.md`; `PACKAGE_REGISTER.csv` SupportsObjectives |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope description | "Workbook-defined Structural package for 'Structural steel - outside of modules' under WBS 01 with recorded physical interfaces." | `PACKAGE_REGISTER.csv` ScopeDescription |
| Inclusion criteria | Workbook row 105; discipline Structural; WBS 01. Applicable interface types: Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` InclusionCriteria |
| Exclusions | TBD; no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` Exclusions |
| Interface types (declared) | Grading / Site Drainage / Spill Containment (IFC-CCDE4B56CA); Structural / Foundations / Supports (IFC-ECDD4D3A15) | `INTERFACE_REGISTER.csv` rows for PKG-104 |
| Production-unit role | Non-vendor package scope, carried conservatively from workbook and DBM support. | `DELIVERABLE_REGISTER.csv` Description; `_CONTEXT.md` Scope |
| Cited source basis | Workbook Packages row 105; `DBM-Deepcut/4-25_Deepcut_DBM.md` | `PACKAGE_REGISTER.csv` SourceBasis |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source-set completeness | Detailed non-vendor discipline requirements are source-limited and remain open for Gate 5 disposition. | `DELIVERABLE_REGISTER.csv` Notes; `ARTIFACT_REGISTER.csv` ART-E815C1D6F1 |
| Vendor-package model | None separately inferred; responsibility model is source-dependent. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Open issues / package flag | OpenIssue = FALSE | `PACKAGE_REGISTER.csv` row PKG-104 |
| Maturity gate target | Gate 5 disposition required for full closure | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` Notes |

## Construction

| Item | Value | Source |
|---|---|---|
| Anticipated artifacts | Discipline production package basis (ART-26DA5854ED); TBD discipline deliverable register; source-limited requirements closure record (ART-E815C1D6F1) | `ARTIFACT_REGISTER.csv` rows for DEL-104-04; `_CONTEXT.md` |
| Discipline deliverable register | TBD — to be defined by the discipline production team within source-supported scope. | `_CONTEXT.md` Anticipated Artifacts |
| Closure record | A source-limited requirements closure record is required to capture remaining scope gaps for human ruling. | ART-E815C1D6F1; `DELIVERABLE_REGISTER.csv` Notes |
| Construction interfaces | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports (both marked YES in interface register). | `INTERFACE_REGISTER.csv` rows for PKG-104 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot) — row DEL-104-04
- `PACKAGE_REGISTER.csv` (GATE-07 snapshot) — row PKG-104
- `SCOPE_LEDGER.csv` (GATE-07 snapshot) — row SOW-0260
- `ARTIFACT_REGISTER.csv` (GATE-07 snapshot) — DEL-104-04 artifact rows (ART-26DA5854ED, ART-E815C1D6F1)
- `INTERFACE_REGISTER.csv` (GATE-07 snapshot) — PKG-104 interface rows (IFC-CCDE4B56CA, IFC-ECDD4D3A15)
- `OBJECTIVE_DELIVERABLE_MAP.csv` (GATE-07 snapshot) — explicit DEL-104-04 rows for OBJ-001, OBJ-008
- Workbook Packages row 105 — referenced but not opened as a source slice (location TBD inside the workbook file `26020-Packages_Interfaces_4_export.xlsx`).
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — cited by PACKAGE_REGISTER.csv SourceBasis; not opened as a source slice during this run (location TBD).
