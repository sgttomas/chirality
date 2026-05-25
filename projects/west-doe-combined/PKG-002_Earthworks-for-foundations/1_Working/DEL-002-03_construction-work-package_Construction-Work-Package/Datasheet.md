# Datasheet: DEL-002-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-002-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-002 - Earthworks for foundations |
| Workbook row | 3 |
| WBS | 02 |
| CoA tracking number | 26020-01-42-001 |
| Discipline | Civil |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Current source status | INITIAL DRAFT from local references; construction execution detail remains TBD where not source-defined |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package scope basis | Workbook-defined Civil package for Earthworks for foundations under WBS 02 with recorded physical interfaces. Source: `PACKAGE_REGISTER.csv`, row `PKG-002`; workbook `Packages` sheet row 3. |
| Mandatory deliverable basis | EPC Integrator construction work package describing physical installation, construction, tie-in, inspection, and turnover into larger systems. Source: `DELIVERABLE_REGISTER.csv`, row `DEL-002-03_construction-work-package`; `PROJECT_DECOMP.md` section 7. |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. Source: `_CONTEXT.md`; `ARTIFACT_REGISTER.csv`, rows for `DEL-002-03_construction-work-package`. |
| Interface types | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: workbook row 3; `INTERFACE_REGISTER.csv`, rows `IFC-E58D0EFA8E` and `IFC-0B377574CA`. |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources. Source: `PACKAGE_REGISTER.csv`, row `PKG-002`. |
| Supported objectives | OBJ-002, OBJ-008, OBJ-010 for this construction work package. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`, row `DEL-002-03_construction-work-package`. |

## Conditions

| Condition | Value / constraint |
|---|---|
| Facility basis | 03-25 compressor station and liquids hub scope. Source: `PROJECT_DECOMP.md` objective `OBJ-002`; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. |
| Civil scope context | Civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. Source: `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions. |
| Construction scope context | Construction scope includes construction management, grading, piling, foundations, roads, field buildings, module offloading/setting, hookups, supports, interconnecting piping, cabling/terminations, lighting, fencing, security systems, utilities, and demolition/removal where required for tie-ins. Source: `3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary. |
| Geotechnical closure | Final geotechnical report is required before foundation design closure. Source: `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions. |
| Ambient design basis | -40 deg C to +35 deg C, with -40 deg C affecting exposed equipment, buildings, control panels, instrumentation, field devices, roads, drainage, foundations, and module layout unless more severe conditions apply. Source: `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions and Design Implications. |
| Final construction package register alignment | Final miscellaneous facilities list shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. Source: `3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities note. |

## Construction

| Construction data item | Current value |
|---|---|
| Earthworks limits | TBD - not defined in accessible package-specific source slices. |
| Excavation, backfill, compaction, and acceptance criteria | TBD - final geotechnical report and civil specifications required. |
| Foundation type / pile design basis | ASSUMPTION: foundation work package must coordinate with final geotechnical report, equipment loads, snow/wind/seismic criteria, frost protection, vibration, settlement, and maintenance access; package-specific foundation design criteria remain TBD. Source: `3-25_Comp_and_Liquids_DBM.md`, Foundations and Structural Supports. |
| Drainage and spill-containment tie-ins | TBD - interface type is source-confirmed, but construction tie-in points and routing are not locally defined. |
| Workface sequencing | TBD - no package-specific construction sequence is available in the local source set. |
| Inspection and test plan | TBD - no source-defined ITP or hold/witness points are available in the local source set. |
| Turnover records | Construction interface and turnover checklist required; detailed signoff matrix TBD. Source: `ARTIFACT_REGISTER.csv`, row `ART-6716AE2168`. |

## References

- `_CONTEXT.md` for deliverable identity, scope, anticipated artifacts, and decomposition pointers.
- `_REFERENCES.md` for accepted Gate 7 and source root pointers.
- `_DEPENDENCIES.md` for declared dependency status.
- `PROJECT_DECOMP.md`, Gate 3 objectives and Gate 5 deliverable basis.
- `DELIVERABLE_REGISTER.csv`, row `DEL-002-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-002`.
- `ARTIFACT_REGISTER.csv`, rows `ART-7FC7329C6F`, `ART-2461156C48`, `ART-6716AE2168`.
- `INTERFACE_REGISTER.csv`, rows `IFC-E58D0EFA8E`, `IFC-0B377574CA`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 3.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary; Site and Civil Conditions; Surface Water and Drainage; Roads and Access; Foundations and Structural Supports.
