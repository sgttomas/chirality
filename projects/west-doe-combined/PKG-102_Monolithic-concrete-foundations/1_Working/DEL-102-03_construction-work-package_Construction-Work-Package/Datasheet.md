# Datasheet: DEL-102-03 — Construction Work Package (PKG-102 Monolithic Concrete Foundations)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-102-03_construction-work-package` | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-102` | `_CONTEXT.md` |
| ParentWorkbookID | 102 | `_CONTEXT.md` |
| PackageName | Monolithic concrete foundations | `_CONTEXT.md`; PACKAGE_REGISTER.csv row `PKG-102` |
| Discipline | Structural | `_CONTEXT.md`; PACKAGE_REGISTER.csv row `PKG-102` |
| Deliverable Type | EPC Construction Work Package | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row `DEL-102-03` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| WBS | 01 | PACKAGE_REGISTER.csv row `PKG-102` |
| Workbook Tag | 26020-01-36-002 | PACKAGE_REGISTER.csv row `PKG-102` |
| CoversScopeItems | `SOW-0258` | `_CONTEXT.md` |
| SupportsObjectives | `OBJ-001`, `OBJ-008`, `OBJ-010` | `_CONTEXT.md` (ASSUMPTION: package-grouping heuristic per OBJECTIVE_ASSOCIATION_MODE) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package interface types | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row `PKG-102`; INTERFACE_REGISTER.csv rows `IFC-1EDEDC0453`, `IFC-8283744B5B` |
| Package-specific exclusions | TBD — no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv row `PKG-102` |
| Ownership model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred | PACKAGE_REGISTER.csv row `PKG-102` |
| Concrete material / construction / testing basis | CSA A23.1 / A23.2 | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2677) |
| Concrete structural design basis | CAN/CSA A23.3 Design of Concrete Structures | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2674) |
| Foundation engineering basis | Canadian Foundation Engineering Manual | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2675) |
| Building code | National Building Code of Canada | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2672) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site bearing capacity | TBD pending geotechnical report | DBM-Deepcut/4-25_Deepcut_DBM.md §"Geotechnical and Topographical Assumptions" (line ~2691) |
| LPILE load-deflection curves | TBD pending geotechnical report | DBM-Deepcut/4-25_Deepcut_DBM.md §"Geotechnical and Topographical Assumptions" (line ~2692) |
| Dynamic design criteria | TBD pending geotechnical report | DBM-Deepcut/4-25_Deepcut_DBM.md §"Geotechnical and Topographical Assumptions" (line ~2693) |
| Site topographical survey | TBD pending survey completion | DBM-Deepcut/4-25_Deepcut_DBM.md §"Geotechnical and Topographical Assumptions" (line ~2698) |
| Climatic / seismic loading | Per National Building Code of Canada (project site values TBD) | DBM-Deepcut/4-25_Deepcut_DBM.md §"Buildings and Miscellaneous Facilities" (line ~2753) |

## Construction

| Item | Value | Source |
|---|---|---|
| Foundation typology served by this package | Monolithic concrete foundations (cast-in-place) | ASSUMPTION — inferred from PACKAGE_REGISTER.csv `PKG-102` PackageName "Monolithic concrete foundations"; DBM does not enumerate a "monolithic" subtype |
| Examples of equipment using concrete bearing/block foundations in DBM | Transformers (precast concrete bearing foundations); Compressors (precast concrete block on driven steel piles, subject to dynamic analysis) | DBM-Deepcut/4-25_Deepcut_DBM.md §"Piles and Foundations" (lines 2745-2747) |
| Default plant foundation basis (project-wide, non-monolithic items) | Driven steel piles | DBM-Deepcut/4-25_Deepcut_DBM.md §"Piles and Foundations" (line 2740) |
| Specific monolithic foundation count, dimensions, rebar schedules, embeds, anchor bolt patterns, pour sequences | TBD — not in accessible sources; downstream detailed engineering and shop drawings required |
| Concrete mix design (strength, slump, air, admixtures) | TBD — location TBD (CSA A23.1 governs but accessible sources do not give project mix values) |
| Curing and protection requirements | TBD — location TBD (CSA A23.1 governs) |
| Cold-weather / hot-weather concreting controls | TBD — location TBD (CSA A23.1 governs) |
| Surface tolerances and finishing | TBD — location TBD (CSA A23.1 governs) |

## Anticipated Artifacts

| Artifact ID | Artifact | Source |
|---|---|---|
| ART-009507D767 | Construction work package | ARTIFACT_REGISTER.csv |
| ART-E8798F2006 | Installation and tie-in workface plan | ARTIFACT_REGISTER.csv |
| ART-66649A8AE4 | Construction interface and turnover checklist | ARTIFACT_REGISTER.csv |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- GATE-07 PROJECT_DECOMP snapshot 2026-05-24 — DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"Governing Civil and Structural Basis", §"Geotechnical and Topographical Assumptions", §"Site Grading and Surface Water Management", §"Piles and Foundations", §"Buildings and Miscellaneous Facilities"
- Source materials not accessed in this pass: `_Sources/26020-Package_Requirements.docx` (binary; location TBD), `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; location TBD), `_Sources/DBM-Comp_and_Liquids/` (not scoped to this deliverable in this pass)
