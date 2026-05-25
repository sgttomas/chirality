# Datasheet: DEL-005-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-005-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-005 - Site Grading |
| Discipline | Civil |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | SOW-0005 |
| Source workbook row | Workbook Packages row 6 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package basis | Workbook-defined Civil package for Site Grading under WBS 03. | PACKAGE_REGISTER.csv, PKG-005 |
| CoA tracking number | 26020-01-42-003 | PACKAGE_REGISTER.csv, PKG-005 |
| Interface types | Drain / Containment; Grading / Site Drainage / Spill Containment | PACKAGE_REGISTER.csv, PKG-005 |
| Deliverable purpose | Describe how the Site Grading package will be physically installed, built, inspected, turned over, and tied into larger facility systems. | DELIVERABLE_REGISTER.csv, DEL-005-03 |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv, DEL-005-03 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, British Columbia | DBM-Comp_and_Liquids, SEC-02 |
| Elevation | 673 m AMSL | DBM-Comp_and_Liquids, SEC-02 |
| Ambient design range | -40 deg C to +35 deg C | DBM-Comp_and_Liquids, SEC-02 |
| Rainfall basis | NBCC 2020 Dawson Creek intensity-duration-frequency data used as a proxy pending site-specific update. | DBM-Comp_and_Liquids, SEC-02 |
| Geotechnical status | Preliminary; clay over clay till; final geotechnical design parameters to be confirmed by geotechnical report. | DBM-Comp_and_Liquids, SEC-02 |
| Surface-water basis | Prevent uncontrolled offsite discharge, protect process areas, support construction and operations access, and route process-contaminated drainage to appropriate drain or containment systems. | DBM-Comp_and_Liquids, SEC-11 |

## Construction

| Construction element | Datasheet basis |
|---|---|
| Included construction scope | Construction management, grading, piling, foundations, roads, field buildings, module offloading and setting, hookups, pipe supports, field cabling/terminations, area lighting, fencing, security, utilities, and tie-in demolition/removal where required by project tie-ins. |
| Civil work coverage | Grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. |
| Access basis | Roads must accommodate construction, module delivery, operations, maintenance, emergency response, and truck-loading traffic, with winter operation considered. |
| Foundation closure | Foundation design closure is blocked until the final geotechnical report is accepted. |
| Package-specific installation sequence | TBD; no deliverable-specific construction sequence source slice was copied during PREPARATION. |
| Package-specific IFC drawing list | TBD; current local references identify the DBM and Gate 7 registers, not a civil IFC drawing package. |

## References

- `_CONTEXT.md` for deliverable identity, scope, and anticipated artifacts.
- `_REFERENCES.md` for accepted decomposition and source pointers.
- Gate 7 PROJECT_DECOMP snapshot registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, especially SEC-02 and SEC-11.
