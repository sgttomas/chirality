# Datasheet: DEL-005-02_package-datasheet - Package Datasheet

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-005-02_package-datasheet |
| Deliverable name | Package Datasheet |
| Parent package | PKG-005 - Site Grading |
| Workbook ID / row | 5 / row 6 |
| WBS | 03 |
| CoA tracking number | 26020-01-42-003 |
| Discipline | Civil |
| Responsible party | EPC Integrator |
| Deliverable type | EPC Package Datasheet |
| Source scope item | SOW-0005 |
| Source basis | Workbook Packages row 6; Gate 7 PACKAGE_REGISTER, DELIVERABLE_REGISTER, ARTIFACT_REGISTER, and INTERFACE_REGISTER |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package name | Site Grading | 26020-Packages_Interfaces_4_export.xlsx, Packages row 6 |
| Package discipline | Civil | 26020-Packages_Interfaces_4_export.xlsx, Packages row 6 |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred. | Gate 7 PACKAGE_REGISTER row PKG-005 |
| Datasheet purpose | Technical handoff basis required for third-party vendor or discipline package engineering and design. | Gate 7 DELIVERABLE_REGISTER row DEL-005-02_package-datasheet |
| Package role | Workbook-defined Civil package with recorded physical interfaces. | Gate 7 PACKAGE_REGISTER row PKG-005 |

## Conditions

| Condition / interface | Value | Source |
|---|---|---|
| Drain / Containment interface | Applicable | 26020-Packages_Interfaces_4_export.xlsx, Packages row 6, column I; Gate 7 INTERFACE_REGISTER IFC-590C44EF2F |
| Grading / Site Drainage / Spill Containment interface | Applicable | 26020-Packages_Interfaces_4_export.xlsx, Packages row 6, column T; Gate 7 INTERFACE_REGISTER IFC-F6589335A4 |
| Surface-water management | Must prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-11 Surface Water and Drainage |
| Contaminated drainage | Process-contaminated drainage must be routed to the appropriate drain or containment system rather than surface-water discharge. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-11 Surface Water and Drainage |
| Hydrology / rainfall basis | Current rainfall basis uses NBCC 2020 Dawson Creek IDF data as a proxy pending site-specific update; civil drainage, retention pond sizing, and surface-water management carry this uncertainty. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-02 Site and Climatic Design Basis |
| Geotechnical basis | Preliminary; final geotechnical report required before foundation design closure. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-02 Geotechnical and Seismic Basis; SEC-11 Site and Civil Conditions |

## Construction

| Construction datum | Value | Source |
|---|---|---|
| Civil design coverage | Grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-11 Site and Civil Conditions |
| Construction scope linkage | Construction scope includes grading, roads, field buildings, offloading and setting of modules, mechanical hookups, pipe supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, security systems, and related support scope. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Construction Scope Summary |
| Specific grading elevations/slopes | TBD | No package-specific grading values found in accessible source slices. |
| Drainage design flow / retention volume | TBD | Hydrology update and discipline design values not provided in accessible source slices. |

## References

- `_CONTEXT.md`, DEL-005-02 identity and scope.
- Gate 7 final published PROJECT_DECOMP snapshot:
  - `PROJECT_DECOMP.md`, Gate 5 accepted basis.
  - `DELIVERABLE_REGISTER.csv`, row DEL-005-02_package-datasheet.
  - `PACKAGE_REGISTER.csv`, row PKG-005.
  - `ARTIFACT_REGISTER.csv`, rows for DEL-005-02_package-datasheet.
  - `INTERFACE_REGISTER.csv`, rows IFC-590C44EF2F and IFC-F6589335A4.
  - `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for DEL-005-02_package-datasheet.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 6.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 and SEC-11.
