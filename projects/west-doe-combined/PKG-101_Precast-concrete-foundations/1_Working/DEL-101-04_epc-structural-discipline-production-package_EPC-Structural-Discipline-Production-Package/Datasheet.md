# Datasheet: DEL-101-04 — EPC / Structural Discipline Production Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-101-04_epc-structural-discipline-production-package` | `_CONTEXT.md` / `DELIVERABLE_REGISTER.csv` |
| Name | EPC / Structural Discipline Production Package | `DELIVERABLE_REGISTER.csv` row DEL-101-04 |
| ParentPackageID | `PKG-101` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-101 |
| PackageName | Precast concrete foundations | `PACKAGE_REGISTER.csv` row PKG-101 |
| WorkbookID / Row | 101 / 102 | `PACKAGE_REGISTER.csv` row PKG-101 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-101 |
| CoA Tracking | 26020-01-36-001 | `PACKAGE_REGISTER.csv` row PKG-101 |
| Discipline | Structural | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Type | EPC/Discipline Production Unit | `DELIVERABLE_REGISTER.csv` row DEL-101-04 |
| Responsible Party | TBD — EPC Integrator or discipline subcontractor as assigned | `DELIVERABLE_REGISTER.csv`; `PACKAGE_REGISTER.csv` (responsibility model is source-dependent) |
| Covers Scope Items | `SOW-0257` | `SCOPE_LEDGER.csv` row SOW-0257; `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-008` (ASSUMPTION — package-grouping heuristic) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` SupportsObjectives |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope description | "Workbook-defined Structural package for 'Precast concrete foundations' under WBS 01 with recorded physical interfaces." | `PACKAGE_REGISTER.csv` ScopeDescription |
| Inclusion criteria | Workbook row 102; discipline Structural; WBS 01. Applicable interface types: Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` InclusionCriteria |
| Exclusions | TBD; no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` Exclusions |
| Interface types (declared) | Grading / Site Drainage / Spill Containment (IFC-26343B703C); Structural / Foundations / Supports (IFC-BED3DE4194) | `INTERFACE_REGISTER.csv` rows for PKG-101 |
| Production-unit role | Non-vendor package scope, carried conservatively from workbook and DBM support. | `DELIVERABLE_REGISTER.csv` Description; `_CONTEXT.md` Scope |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source-set completeness | Detailed non-vendor discipline requirements are source-limited and remain open for Gate 5 disposition. | `DELIVERABLE_REGISTER.csv` Notes; `ARTIFACT_REGISTER.csv` ART-5FB1815B54 |
| Vendor-package model | None separately inferred; responsibility model is source-dependent. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Open issues / package flag | OpenIssue = FALSE | `PACKAGE_REGISTER.csv` row PKG-101 |
| Maturity gate target | Gate 5 disposition required for full closure | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` Notes |

## Construction

| Item | Value | Source |
|---|---|---|
| Anticipated artifacts | Discipline production package basis (ART-D61EA18810); TBD discipline deliverable register; source-limited requirements closure record (ART-5FB1815B54) | `ARTIFACT_REGISTER.csv` rows for DEL-101-04; `_CONTEXT.md` |
| Discipline deliverable register | TBD — to be defined by the discipline production team within source-supported scope. | `_CONTEXT.md` Anticipated Artifacts |
| Closure record | A source-limited requirements closure record is required to capture remaining scope gaps for human ruling. | ART-5FB1815B54; `DELIVERABLE_REGISTER.csv` Notes |
| Construction interfaces | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports (both marked YES in interface register). | `INTERFACE_REGISTER.csv` rows for PKG-101 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot) — row DEL-101-04
- `PACKAGE_REGISTER.csv` (GATE-07 snapshot) — row PKG-101
- `SCOPE_LEDGER.csv` (GATE-07 snapshot) — row SOW-0257
- `ARTIFACT_REGISTER.csv` (GATE-07 snapshot) — DEL-101-04 artifact rows
- `INTERFACE_REGISTER.csv` (GATE-07 snapshot) — PKG-101 interface rows
- `OBJECTIVE_REGISTER.csv` (GATE-07 snapshot) — OBJ-001, OBJ-008
- Workbook Packages row 102 — referenced but not opened as a source slice (location TBD inside the workbook file `26020-Packages_Interfaces_4_export.xlsx`).
