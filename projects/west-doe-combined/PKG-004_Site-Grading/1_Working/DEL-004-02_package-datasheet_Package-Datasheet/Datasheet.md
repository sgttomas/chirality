# Datasheet: DEL-004-02_package-datasheet — Package Datasheet

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-004-02_package-datasheet |
| Deliverable name | Package Datasheet |
| Parent package | PKG-004 — Site Grading |
| Workbook row | Packages row 5 |
| Workbook ID | 4 |
| WBS | 02 |
| CoA tracking number | 26020-01-42-003 |
| Discipline | Civil |
| Type | EPC Package Datasheet |
| Responsible party | EPC Integrator |
| Scope item | SOW-0004 |

Source: `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 `DELIVERABLE_REGISTER.csv`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package name | Site Grading | Workbook Packages row 5; Gate 7 `PACKAGE_REGISTER.csv` |
| Discipline | Civil | Workbook Packages row 5; Gate 7 `PACKAGE_REGISTER.csv` |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources. | Gate 7 `PACKAGE_REGISTER.csv` |
| Package scope basis | Workbook-defined Civil package for Site Grading under WBS 02 with recorded physical interfaces. | Gate 7 `PACKAGE_REGISTER.csv` |
| Applicable interface types | Drain / Containment; Grading / Site Drainage / Spill Containment | Workbook Packages row 5; Gate 7 `INTERFACE_REGISTER.csv` |
| Datasheet artifacts | Package technical datasheet; vendor engineering handoff basis; package interface requirements matrix; source-supported equipment and design criteria | `_CONTEXT.md`; Gate 7 `ARTIFACT_REGISTER.csv` |
| Detailed package exclusions | TBD; no package-specific exclusions stated in source materials. | Gate 7 `PACKAGE_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility context | 03-25 compressor station and liquids hub scope includes civil and infrastructure support including site grading, foundations, roads, buildings, electrical buildings, pipe racks, field interconnections, lighting, fencing, and security as assigned to construction scope. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Scope Inclusions |
| Construction context | Construction scope includes construction management, grading, piling, foundations, roads, field buildings, module setting, hookups, interconnecting piping, cabling, area lighting, fencing, security, utilities, and tie-in demolition/removal where required. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary |
| Civil design basis | SEC-02 site-specific design data governs civil design pending final geotechnical confirmation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions |
| Elevation | 673 m AMSL | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions |
| Design ambient temperature | -40 deg C to +35 deg C | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions |
| Rainfall basis | NBCC 2020 Dawson Creek intensity-duration-frequency data is used as proxy pending site-specific update. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 Site-Specific Design Data |
| Geotechnical status | Final geotechnical report is required before foundation design closure. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions |
| Terrain type | TBD | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 Geotechnical and Seismic Basis |

## Construction

| Construction / Design Data Topic | Datasheet Basis | Source |
|---|---|---|
| Grading and drainage | Civil design shall cover grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions |
| Surface-water management | Surface-water management shall prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Surface Water and Drainage |
| Retention pond and drainage sizing | Retention pond sizing and drainage design shall use the current precipitation and storm basis until hydrology is updated. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Surface Water and Drainage |
| Process-contaminated drainage | Process-contaminated drainage shall be routed to the appropriate drain or containment system rather than surface-water discharge. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Surface Water and Drainage |
| Layout interfaces | Drainage design intent is surface-water collection, segregation, and retention consistent with civil and environmental requirements. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Layout Basis |
| Standards and governing content | Civil/structural governing content includes NBCC, geotechnical report, site data, civil drawings, and surface-water management. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-15 table |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 5
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Scope Inclusions, Construction Scope Summary, SEC-02, SEC-11, SEC-15 table
