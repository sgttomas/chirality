# Datasheet: EPC / Civil Discipline Production Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-002-04_epc-civil-discipline-production-package` |
| Deliverable name | EPC / Civil Discipline Production Package |
| Parent package | `PKG-002` - Earthworks for foundations |
| Parent workbook ID | 2 |
| WBS | `02` |
| CoA tracking number | `26020-01-42-001` |
| Discipline | Civil |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Scope item | `SOW-0002` |
| Directionally relevant objectives | `OBJ-002`, `OBJ-008` |

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for `DEL-002-04`; Gate 7 `PACKAGE_REGISTER.csv` row for `PKG-002`; `26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row with ID # 2.

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package name | Earthworks for foundations | Workbook `Packages` sheet row ID # 2; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-002` |
| Workbook discipline | Civil | Workbook `Packages` sheet row ID # 2 |
| Package ownership model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-002` |
| Production package artifacts | Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-002-04` |
| Package interfaces marked applicable | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | Workbook `Packages` sheet row ID # 2; Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-002` |
| Detailed civil design criteria | TBD | Source-limited for this deliverable; Gate 7 notes detailed non-vendor package requirements remain open |

## Conditions

| Condition | Value | Source / status |
|---|---|---|
| Facility basis | 03-25 West Doe Compressor Station and Liquids Hub at LSD 03-25-80-15W6, north of Dawson Creek, BC | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-01 and SEC-02 |
| Site elevation | 673 m AMSL | DBM SEC-02 Site Location |
| Design ambient range | -40 deg C to +35 deg C | DBM SEC-02 Ambient Design Conditions |
| Wind pressure | 0.30 kPa 1-in-10 year; 0.40 kPa 1-in-50 year | DBM SEC-02 Wind, Snow, and Precipitation |
| 1-day rainfall, 1-in-50 year | 75 mm | DBM SEC-02 Wind, Snow, and Precipitation |
| Site class | D | DBM SEC-02 Geotechnical / Seismic Parameter table |
| PGA | 0.142 g | DBM SEC-02 Geotechnical / Seismic Parameter table |
| Soil description | Clay over clay till | DBM SEC-02, TBC status |
| Final geotechnical report | Required before foundation design closure | DBM SEC-02 Design Implications; DBM SEC-11 Site and Civil Conditions |

## Construction

| Topic | Current basis | Source / status |
|---|---|---|
| Civil design coverage | Grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security | DBM SEC-11 Site and Civil Conditions |
| Construction scope overlap | Construction management, grading, piling, foundations, roads, field buildings, offloading and setting modules, pipe supports, interconnecting piping, lighting, fencing, security systems, and related tie-in work where required | DBM SEC-01 Construction Scope Summary |
| Surface water and drainage basis | Prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access | DBM SEC-11 Surface Water and Drainage |
| Process-contaminated drainage | Route to appropriate drain or containment system rather than surface-water discharge | DBM SEC-11 Surface Water and Drainage |
| Foundation design closure | TBD pending final geotechnical report and detailed engineering | DBM SEC-02 and SEC-11 |
| Discipline drawing/register list | TBD | Not present in accessible package-specific sources |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 final published PROJECT_DECOMP snapshot, especially `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, and `PROJECT_DECOMP.md`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row ID # 2
- `_Sources/26020-Package_Requirements.docx`, extracted package coordination text
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-01, SEC-02, and SEC-11 slices
