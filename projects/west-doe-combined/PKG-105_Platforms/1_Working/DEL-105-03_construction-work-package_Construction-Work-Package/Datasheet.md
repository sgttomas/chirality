# Datasheet — DEL-105-03 Construction Work Package (Platforms)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-105-03_construction-work-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-105` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| ParentWorkbookID | 105 | `_CONTEXT.md` |
| PackageName | Platforms | `PACKAGE_REGISTER.csv`; Workbook Packages ID# 105 |
| CoA Tracking Number | 26020-01-36-005 | Workbook Packages ID# 105 |
| WBS | 01 | Workbook Packages ID# 105; `PACKAGE_REGISTER.csv` |
| Discipline | Structural | Workbook Packages ID# 105; `_CONTEXT.md` |
| Type | EPC Construction Work Package | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| ScopeItem | `SOW-0261` | `SCOPE_LEDGER.csv`; `_CONTEXT.md` |
| Supported Objectives | `OBJ-001`, `OBJ-005`, `OBJ-008`, `OBJ-010` | `OBJECTIVE_SCOPE_MAP.csv`; `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Workbook-defined Structural package for "Platforms" under WBS 01 with recorded physical interfaces | `PACKAGE_REGISTER.csv` PKG-105 |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources | `PACKAGE_REGISTER.csv` PKG-105 |
| Vendor flag | FALSE (no vendor-package ownership model) | `PACKAGE_REGISTER.csv` PKG-105 |
| Authoritative companion register row | TRUE | `PACKAGE_REGISTER.csv` PKG-105 |
| Stated package-specific exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` PKG-105 |

## Conditions (Physical Interfaces)

Source: Workbook Packages ID# 105 columns marked "X"; `INTERFACE_REGISTER.csv` PKG-105.

| Interface ID | Interface Type | Workbook marked? | Vendor flag | Notes |
|---|---|---|---|---|
| `IFC-26E3DCAD56` | Area / Exterior Lighting | X | YES | Platform-to-equipment tie-ins to be confirmed by layout/model. Gate 6 disposition: EPC Integrator owns tie-ins through overall 3D model and integrated P&ID set. |
| `IFC-07C472C58B` | Grading / Site Drainage / Spill Containment | X | YES | Same Gate 6 disposition as above. |
| `IFC-B7C0A01E38` | Structural / Foundations / Supports | X | YES | Same Gate 6 disposition as above. |

All other workbook interface columns for ID# 105 are blank (not applicable per source).

## Construction (Artifacts to be produced)

Source: `ARTIFACT_REGISTER.csv` rows for `DEL-105-03`; `_CONTEXT.md` Anticipated Artifacts.

| Artifact ID | Artifact | Evidence Type | Description |
|---|---|---|---|
| `ART-B033D6C5F7` | Construction work package | EPC Construction Work Package | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. |
| `ART-C143830D41` | Installation and tie-in workface plan | Construction Tie-In Evidence | Workface planning evidence for installing/building the package and connecting it to adjacent structural, lighting, and grading/drainage/containment systems as applicable. |
| `ART-BEC8A111DC` | Construction interface and turnover checklist | Construction Interface Evidence | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. |

## Quantities / Counts

| Item | Value | Source |
|---|---|---|
| Platform count | TBD (location TBD) | Not stated in workbook ID# 105; no detailed equipment text available in `26020-Package_Requirements.docx` (no heading for Platforms / 26020-01-36-005). |
| Tagged equipment list | TBD (location TBD) | Source-limited; see DEL-105-01 / DEL-105-02 / DEL-105-04 for resolution. |
| Material/coating spec | TBD (location TBD) | Not stated in available sources. |

## References

- Workbook Packages row (ID# 105; CoA `26020-01-36-005`): `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages`.
- Project decomposition snapshot `GATE-07_Final_Published_2026-05-24`:
  - `DELIVERABLE_REGISTER.csv` row `DEL-105-03_construction-work-package`
  - `PACKAGE_REGISTER.csv` row `PKG-105`
  - `INTERFACE_REGISTER.csv` rows `IFC-26E3DCAD56`, `IFC-07C472C58B`, `IFC-B7C0A01E38`
  - `ARTIFACT_REGISTER.csv` rows `ART-B033D6C5F7`, `ART-C143830D41`, `ART-BEC8A111DC`
  - `SCOPE_LEDGER.csv` row `SOW-0261`
  - `OBJECTIVE_SCOPE_MAP.csv` rows `OBJ-001`, `OBJ-005`, `OBJ-008`, `OBJ-010` for PKG-105
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Additional sources cited by `PACKAGE_REGISTER.csv` PKG-105 source line: `DBM-Deepcut/4-25_Deepcut_DBM.md` (no Platforms-specific text located on review — location TBD).
- `26020-Package_Requirements.docx`: no Platforms / `26020-01-36-005` section present on review; treated as not deliverable-local source for this row.
