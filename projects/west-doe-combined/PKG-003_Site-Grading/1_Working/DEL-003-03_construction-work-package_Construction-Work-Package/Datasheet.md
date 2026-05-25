# Datasheet: DEL-003-03_construction-work-package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-003-03_construction-work-package` |
| Deliverable name | Construction Work Package |
| Parent package | `PKG-003` - Site Grading |
| Workbook row | Packages row 4 |
| Workbook ID | 3 |
| WBS | 01 |
| CoA tracking number | 26020-01-42-003 |
| Discipline | Civil |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | `SOW-0003` |
| Supported objectives | `OBJ-001`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package scope statement | Carry the workbook-defined Civil package "Site Grading" as a distinct flat project package for WBS 01. |
| Package role | Mandatory EPC Integrator deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into larger facility systems. |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. |
| Workbook interface flags | Drain / Containment; Grading / Site Drainage / Spill Containment. |
| Construction scope context | Construction management, grading, piling, foundations, roads, field buildings, module offloading and setting, hookups, shipped-loose instrument/valve installation, pipe supports, interconnecting piping, cabling, terminations, lighting, fencing, security, control room and maintenance systems, utilities, and tie-in demolition/removal where required by project tie-ins. |
| Applicable civil work context | Civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. |
| Detailed construction sequencing | TBD pending IFC construction drawings, construction execution plan, plot plan, geotechnical report, topographical survey, and detailed drainage design. |

## Conditions

| Condition | Source-grounded value |
|---|---|
| Facility design ambient | -40 deg C to +35 deg C for 03-25 civil/site basis; -40 deg C minimum ambient affects exposed equipment, buildings, control panels, instrumentation, and field devices unless a more severe basis applies. |
| Site elevation | 673 m AMSL for 03-25 site/civil basis. |
| Rainfall basis | NBCC 2020 Dawson Creek intensity-duration-frequency data is used as proxy pending site-specific update; civil drainage, retention pond sizing, and surface-water management carry this uncertainty until hydrology inputs are confirmed. |
| Surface-water management | Prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. Process-contaminated drainage must route to the appropriate drain or containment system rather than surface-water discharge. |
| Deepcut grading/drainage intent | Prevent off-site surface overflow from entering the expansion facility while directing and containing on-site overflow into a retention pond. |
| Existing grade surface | ASSUMPTION from DBM: grade surface file will support grading and drainage design; final format and contents are TBD pending survey completion. |
| Geotechnical closure | Final geotechnical report is required before foundation design closure. |

## Construction

| Construction parameter | Source-grounded value |
|---|---|
| Main pipe rack grading | High equal-elevation ridges along main pipe racks. |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side. |
| Reduced pad slope allowance | Pad slope may be reduced to 1.0% where required to maintain reasonable top-of-pile-cap elevations. |
| Maximum grade slope | 3H:1V maximum, including road-fill side slopes, ditches, stockpiles, pond slopes, and similar grade surfaces, unless specifically engineered or mandated otherwise by the geotechnical report. |
| Ditch slope | 0.2% minimum. |
| Culvert slope | 0.5% minimum; 1.0% preferred. |
| Ditch and culvert storm basis | IDF curve for the 1:10 year, 15 minute rainfall event; final IDF duration to be confirmed during detailed engineering. |
| Facility pad surface | Adequate gravel thickness over the entire pad to provide a driving surface. |
| Access-road drainage definition | Only access roads will be defined by ditches on either side. |
| Retention pond | On-site retention pond with berm to capture natural runoff; location and capacity TBD pending plot plan coordination and detailed engineering. |
| NGL storage area surface control | Berm, elevation decline, or other surface-control feature to be considered for accidental leak or spill containment; grading under NGL bullets to redirect NGL away from pipe rack and process areas. |
| Road pavement layers | Surfacing aggregate, gravel base course, pit run base course, and woven geotextile requirements are TBD pending geotechnical report and soil conditions. |
| Field inspection hold points | TBD pending construction quality plan and IFC civil specifications. |
| Turnover package contents | Construction interface and turnover checklist, inspection records, as-built redlines, open-item register, and acceptance evidence; final record list TBD pending project turnover procedure. |

## References

- `_CONTEXT.md` for deliverable identity, scope, anticipated artifacts, and decomposition pointers.
- Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, and `OBJECTIVE_REGISTER.csv`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet, source row for Site Grading WBS 01 / CoA `26020-01-42-003`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil, Buildings, and Miscellaneous Facilities Basis.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary and SEC-11 Plant Layout, Spacing, Civil, and Buildings.
