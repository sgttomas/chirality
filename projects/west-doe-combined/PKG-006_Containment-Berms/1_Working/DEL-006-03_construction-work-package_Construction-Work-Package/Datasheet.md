# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-006-03_construction-work-package` |
| Deliverable name | Construction Work Package |
| Parent package | `PKG-006` - Containment Berms |
| Workbook row | 7 |
| WBS | 03 |
| CoA tracking number | `26020-03-42-006` |
| Discipline | Civil |
| Responsible party | EPC Integrator |
| Deliverable type | EPC Construction Work Package |
| Scope item | `SOW-0006` |

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-006-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-006`.

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package name | Containment Berms | `PACKAGE_REGISTER.csv` row `PKG-006` |
| Package responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. | `PACKAGE_REGISTER.csv` row `PKG-006` |
| Package scope basis | Workbook-defined Civil package for Containment Berms under WBS 03 with recorded physical interfaces. | `PACKAGE_REGISTER.csv` row `PKG-006` |
| Applicable interface types | Drain / Containment; Grading / Site Drainage / Spill Containment | `PACKAGE_REGISTER.csv` row `PKG-006`; `INTERFACE_REGISTER.csv` rows `IFC-62ACD644F9`, `IFC-2A535A882C` |
| Construction work package artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `DELIVERABLE_REGISTER.csv` row `DEL-006-03_construction-work-package`; `ARTIFACT_REGISTER.csv` rows for `DEL-006-03_construction-work-package` |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Facility context | 03-25 West Doe Compressor Station and Liquids Hub includes civil and infrastructure scope such as site grading, foundations, roads, buildings, electrical buildings, pipe racks, field interconnections, lighting, fencing, and security as assigned to construction scope. | `3-25_Comp_and_Liquids_DBM.md` Facility Overview |
| Construction-scope context | Construction scope includes construction management, grading, piling, foundations, roads, field buildings, offloading and setting modules, mechanical hookups, interconnecting piping, cabling, terminations, area lighting, fencing, security systems, control/maintenance systems, potable/septic utilities, non-process building heating and fuel storage, and demolition/removal where required for project tie-ins. | `3-25_Comp_and_Liquids_DBM.md` Construction Scope Summary |
| Surface-water management | Surface-water management must prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | `3-25_Comp_and_Liquids_DBM.md` SEC-11 Surface Water and Drainage |
| Process-contaminated drainage | Process-contaminated drainage must route to the appropriate drain or containment system rather than surface-water discharge. | `3-25_Comp_and_Liquids_DBM.md` SEC-11 Surface Water and Drainage |
| Rainfall / hydrology status | Current rainfall basis uses NBCC 2020 Dawson Creek IDF data as a proxy; drainage, retention pond sizing, and surface-water management carry uncertainty until final hydrology inputs are confirmed. | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Site-Specific Design Data |
| Geotechnical status | Final geotechnical report is required before foundation design closure; current geotechnical values are placeholders where marked. | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Geotechnical and Seismic Basis; SEC-11 Site and Civil Conditions |
| Ambient design implication | The -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies. | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Design Implications |
| Standards status | Where a standard is referenced but unavailable in the workspace, verify the citation before final issue for construction. | `3-25_Comp_and_Liquids_DBM.md` SEC-15 Specifications, Codes, and Standards |

## Construction

| Construction data item | Value |
|---|---|
| Work package boundary | Physical installation, construction, inspection, turnover, and tie-in of Containment Berms to larger facility systems. |
| Workface plan minimum contents | Installation sequence, work area limits, tie-in/interface checkpoints, civil inspection points, turnover records, and unresolved `TBD` criteria. |
| Interface checklist minimum contents | Drain/containment interface checks and grading/site drainage/spill containment checks. |
| Detailed berm geometry | TBD - not present in accessible source slices. |
| Berm material / liner / coating requirements | TBD - not present in accessible source slices. |
| Inspection and acceptance criteria | TBD - to be confirmed from IFC civil drawings, project civil specifications, geotechnical report, and environmental/permitting requirements. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
