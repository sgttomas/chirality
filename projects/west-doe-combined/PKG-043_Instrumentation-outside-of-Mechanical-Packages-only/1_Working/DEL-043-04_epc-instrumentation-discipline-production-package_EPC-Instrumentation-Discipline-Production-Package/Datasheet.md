# Datasheet — DEL-043-04 EPC / Instrumentation Discipline Production Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-043-04_epc-instrumentation-discipline-production-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-043-04 |
| Name | EPC / Instrumentation Discipline Production Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-043-04 |
| ParentPackageID | `PKG-043` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-043 |
| ParentWorkbookID | 43 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-043 |
| PackageName | Instrumentation (outside of Mechanical Packages only) | `PACKAGE_REGISTER.csv` row PKG-043 |
| Discipline | Instrumentation | `PACKAGE_REGISTER.csv` row PKG-043 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-043 |
| Type | EPC / Discipline Production Unit | `DELIVERABLE_REGISTER.csv` row DEL-043-04 |
| ResponsibleParty | TBD; EPC Integrator or discipline subcontractor as assigned | `DELIVERABLE_REGISTER.csv` row DEL-043-04 |
| CoversScopeItems | `SOW-0044` | `DELIVERABLE_REGISTER.csv` row DEL-043-04 |
| SupportsObjectives | `OBJ-001`, `OBJ-003`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-010` | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-043-04 |
| SourceRef | Workbook Packages row 45 | `DELIVERABLE_REGISTER.csv` row DEL-043-04 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Production unit role | Non-vendor package discipline production unit, carried conservatively from workbook and DBM support | `DELIVERABLE_REGISTER.csv` row DEL-043-04 Description |
| Discipline scope coverage | Instrumentation work outside of Mechanical Packages | `PACKAGE_REGISTER.csv` row PKG-043 PackageName |
| Detailed requirements maturity | Source-limited; remain open for Gate 5 disposition | `DELIVERABLE_REGISTER.csv` row DEL-043-04 Notes; `_CONTEXT.md` Notes |
| Vendor-package ownership model | No separate vendor-package ownership model inferred from current sources | `PACKAGE_REGISTER.csv` row PKG-043 ResponsibleParty note |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating environment | TBD (not stated for the discipline production unit in available registers) | location TBD |
| Process / service conditions | TBD (DBM-Deepcut/4-25_Deepcut_DBM.md slice not locally extracted) | `PACKAGE_REGISTER.csv` SourceRef references DBM but slice not present in `_REFERENCES.md` accessible set |
| Applicable interface types (package-level) | Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network | `INTERFACE_REGISTER.csv` rows IFC-AE83B2D0FC, IFC-F41620D435, IFC-E5A8000199, IFC-4929B68CCD, IFC-35EBF9CD91 |

## Construction

| Item | Value | Source |
|---|---|---|
| Anticipated artifacts | Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-043-04 AnticipatedArtifacts |
| Deliverable register (discipline-level) | TBD — to be enumerated at Gate 5 | ASSUMPTION (best-effort) from `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts |
| Construction / installation specifics | TBD — non-vendor package detail is source-limited | `DELIVERABLE_REGISTER.csv` row DEL-043-04 Notes |

## References

- `DELIVERABLE_REGISTER.csv` row DEL-043-04 — GATE-07 snapshot
- `PACKAGE_REGISTER.csv` row PKG-043 — GATE-07 snapshot
- `INTERFACE_REGISTER.csv` rows IFC-AE83B2D0FC, IFC-F41620D435, IFC-E5A8000199, IFC-4929B68CCD, IFC-35EBF9CD91 — GATE-07 snapshot
- `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-043-04 — GATE-07 snapshot
- `_CONTEXT.md`
- Workbook Packages row 45 — referenced; slice not locally available (location TBD)
- DBM-Deepcut/4-25_Deepcut_DBM.md — referenced by `PACKAGE_REGISTER.csv` SourceRef; slice not locally available (location TBD)
