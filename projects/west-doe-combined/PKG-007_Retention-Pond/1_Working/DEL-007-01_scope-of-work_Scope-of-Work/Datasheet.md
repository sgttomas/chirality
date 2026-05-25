# Datasheet: DEL-007-01_scope-of-work — Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-007-01_scope-of-work | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row 26 |
| Deliverable name | Scope of Work | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row 26 |
| Parent package | PKG-007 — Retention Pond | `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv` row 8 |
| Workbook / WBS basis | Workbook ID 7; WBS 02 | Gate 7 `PACKAGE_REGISTER.csv` row 8; `_Sources/26020-Packages_Interfaces_4_export.xlsx` worksheet row 8 |
| CoA tracking number | 26020-02-42-007 | Gate 7 `PACKAGE_REGISTER.csv` row 8; `_Sources/26020-Packages_Interfaces_4_export.xlsx` worksheet row 8 |
| Discipline | Civil | `_CONTEXT.md`; workbook export worksheet row 8 |
| Responsible party | EPC Integrator | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row 26 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row 26 |

## Attributes

| Attribute | Value | Source / Status |
|---|---|---|
| Package function | Civil retention pond / surface-water management package supporting the 03-25 compressor station and liquids hub scope. | Gate 7 `PACKAGE_REGISTER.csv` row 8; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Site and Civil Conditions" and "Surface Water and Drainage" |
| Scope unit | SOW-0007 | `_CONTEXT.md`; Gate 7 `SCOPE_LEDGER.csv` row 8 |
| Package inclusion basis | Carry the workbook-defined Civil package "Retention Pond" as a distinct flat project package for WBS 02. | Gate 7 `SCOPE_LEDGER.csv` row 8 |
| Declared interfaces | Drain / Containment; Grading / Site Drainage / Spill Containment. | Gate 7 `INTERFACE_REGISTER.csv` rows 14-15; workbook export worksheet row 8 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md`; Gate 7 `ARTIFACT_REGISTER.csv` rows 86-89 |
| Objective context | OBJ-002, OBJ-007, OBJ-008, OBJ-009. | Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows 368, 2472, 2912, 3470 |

## Conditions

| Condition | Value | Source / Status |
|---|---|---|
| Rainfall basis | 15-minute rainfall 18 mm; 1-day rainfall, 1-in-50 year 75 mm; annual precipitation 475 mm; annual rainfall component 325 mm. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` rainfall basis table |
| Rainfall uncertainty | NBCC 2020 Dawson Creek intensity-duration-frequency data is a proxy pending site-specific update; retention pond sizing and surface-water management carry this uncertainty. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` rainfall basis note |
| Geotechnical basis | Preliminary; soil described as clay over clay till; Site Class D; final geotechnical design parameters to be confirmed. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Geotechnical and Seismic Basis" |
| Civil design environment | Elevation 673 m AMSL; design ambient temperature -40 deg C to +35 deg C. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Site and Civil Conditions" |
| Retention pond capacity / geometry | TBD. | No package-specific capacity, geometry, or location found in accessible source slices. |

## Construction

| Item | Value | Source / Status |
|---|---|---|
| Work covered by civil design | Grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Site and Civil Conditions" |
| Surface-water management intent | Prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Surface Water and Drainage" |
| Process-contaminated drainage | Route to the appropriate drain or containment system rather than surface-water discharge. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Surface Water and Drainage" |
| Scope exclusions | TBD; no package-specific exclusions stated in source materials. | Gate 7 `PACKAGE_REGISTER.csv` row 8 |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- Gate 7 final published snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, worksheet row 8
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, rainfall basis table, "Geotechnical and Seismic Basis", "Site and Civil Conditions", "Surface Water and Drainage"
