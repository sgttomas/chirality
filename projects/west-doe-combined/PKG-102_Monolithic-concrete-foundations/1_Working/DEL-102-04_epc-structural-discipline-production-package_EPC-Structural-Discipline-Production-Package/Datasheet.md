# Datasheet: DEL-102-04 — EPC / Structural Discipline Production Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-102-04_epc-structural-discipline-production-package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-102-04 |
| Name | EPC / Structural Discipline Production Package | `DELIVERABLE_REGISTER.csv` row DEL-102-04 |
| ParentPackageID | PKG-102 | `_CONTEXT.md` |
| ParentWorkbookID | 102 (workbook row 103) | `PACKAGE_REGISTER.csv` PKG-102 |
| PackageName | Monolithic concrete foundations | `PACKAGE_REGISTER.csv` PKG-102 |
| Discipline | Structural | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-102 |
| WBS | 01 | `PACKAGE_REGISTER.csv` PKG-102 |
| CoA Tracking Number | 26020-01-36-002 | `PACKAGE_REGISTER.csv` PKG-102 |
| Type | EPC/Discipline Production Unit | `DELIVERABLE_REGISTER.csv` row DEL-102-04 |
| Responsible Party | TBD; EPC Integrator or discipline subcontractor as assigned | `_CONTEXT.md` (ASSUMPTION: source-dependent per `PACKAGE_REGISTER.csv` PKG-102 ResponsibilityModel) |
| Covers Scope | SOW-0258 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | OBJ-001; OBJ-008 (ASSUMPTION: PACKAGE_HEURISTIC) | `_CONTEXT.md`; `OBJECTIVE_PACKAGE_MAP.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Production unit role | Non-vendor discipline production unit for the structural scope of the monolithic concrete foundations package | `DELIVERABLE_REGISTER.csv` row DEL-102-04 |
| Carry posture | Conservative carry-forward from workbook and Deepcut DBM support | `DELIVERABLE_REGISTER.csv` row DEL-102-04 |
| Inclusion criteria | Workbook-defined Structural package 'Monolithic concrete foundations' under WBS 01 with recorded physical interfaces | `PACKAGE_REGISTER.csv` PKG-102 |
| Detailed structural design requirements (loads, materials, codes, geometry) | TBD — not present in the locally accessible source set | `_CONTEXT.md` Notes; `ARTIFACT_REGISTER.csv` ART-712FAD4E91 (Source Gap Evidence) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Applicable interface types | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` PKG-102; `INTERFACE_REGISTER.csv` IFC-1EDEDC0453, IFC-8283744B5B |
| Package exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` PKG-102 |
| Vendor ownership model | None; no separate vendor-package ownership model is inferred from current sources | `PACKAGE_REGISTER.csv` PKG-102 |
| Design environmental/site conditions | TBD — not present in locally accessible sources | ASSUMPTION |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction type | Monolithic concrete foundations (structural discipline production unit) | `PACKAGE_REGISTER.csv` PKG-102 |
| Major equipment list | TBD — no detailed equipment text in source for PKG-102 | `PACKAGE_REGISTER.csv` PKG-102 (DocxPackageMatched=FALSE) |
| Construction interfaces | Coupled to Grading/Drainage/Spill Containment and Structural/Foundations/Supports interfaces (carried as facts on DEL-102-02) | `INTERFACE_REGISTER.csv` PKG-102 rows; `ARTIFACT_REGISTER.csv` ART-05281DC8CE, ART-F35AC96771 |
| Tie-in workface plan | Handled by sibling deliverable DEL-102-03 (Construction Work Package) | `ARTIFACT_REGISTER.csv` ART-009507D767 |

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — authoritative reference index
- Gate 7 PROJECT_DECOMP snapshot `DELIVERABLE_REGISTER.csv` (row DEL-102-04)
- Gate 7 `PACKAGE_REGISTER.csv` (row PKG-102)
- Gate 7 `ARTIFACT_REGISTER.csv` (rows ART-5C2432867E, ART-712FAD4E91 for DEL-102-04)
- Gate 7 `INTERFACE_REGISTER.csv` (rows IFC-1EDEDC0453, IFC-8283744B5B)
- Gate 7 `SCOPE_LEDGER.csv` (SOW-0258 — TBD: not located in current ledger slice)
- Workbook Packages row 103 (referenced by registers; underlying workbook slice not copied to deliverable folder — `_REFERENCES.md` Missing/Deferred)
- DBM-Deepcut/4-25_Deepcut_DBM.md (referenced; underlying slice not copied)
