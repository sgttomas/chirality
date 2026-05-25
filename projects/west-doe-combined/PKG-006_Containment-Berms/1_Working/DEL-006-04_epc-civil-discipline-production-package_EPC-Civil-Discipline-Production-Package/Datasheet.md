# Datasheet: EPC / Civil Discipline Production Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-006-04_epc-civil-discipline-production-package |
| Deliverable name | EPC / Civil Discipline Production Package |
| Parent package | PKG-006 - Containment Berms |
| Workbook ID / row | 6 / row 7 |
| WBS | 03 |
| CoA tracking number | 26020-03-42-006 |
| Discipline | Civil |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Covers scope item | SOW-0006 |
| Supports objectives | OBJ-002; OBJ-007; OBJ-008; OBJ-009 |

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package description | Workbook-defined Civil package for Containment Berms under WBS 03 with recorded physical interfaces. | PACKAGE_REGISTER.csv, PKG-006 |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. | PACKAGE_REGISTER.csv, PKG-006 |
| Applicable interface type | Drain / Containment. | INTERFACE_REGISTER.csv, IFC-62ACD644F9 |
| Applicable interface type | Grading / Site Drainage / Spill Containment. | INTERFACE_REGISTER.csv, IFC-2A535A882C |
| Production package artifacts | Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record. | DELIVERABLE_REGISTER.csv, DEL-006-04 |
| Detailed discipline requirements | TBD; detailed discipline requirements are not present in the current source set and remain open. | ARTIFACT_REGISTER.csv, ART-5AEDE189AA |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Civil design scope context | Civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | 3-25_Comp_and_Liquids_DBM.md, Site and Civil Conditions |
| Rainfall basis | NBCC 2020 Dawson Creek intensity-duration-frequency data is used as a proxy pending site-specific update; civil drainage, retention pond sizing, and surface-water management carry this uncertainty until final hydrology inputs are confirmed. | 3-25_Comp_and_Liquids_DBM.md, rainfall basis |
| Civil/structural basis applicability | Civil and structural basis applies to the facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings. | 4-25_Deepcut_DBM.md, civil/structural scope |
| Geotechnical and topographical inputs | Geotechnical report, topographical survey, and grade surface file remain required inputs; several parameters are TBD. | 4-25_Deepcut_DBM.md, Geotechnical and Topographical Assumptions; External Dependencies |
| Retention pond | On-site retention pond with berm shall be installed to capture natural runoff; location and capacity are detailed-engineering TBDs. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management |

## Construction

| Item | Current basis | Source |
|---|---|---|
| Surface-water management intent | Prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | 3-25_Comp_and_Liquids_DBM.md, Surface Water and Drainage |
| Contaminated drainage routing | Process-contaminated drainage shall route to the appropriate drain or containment system rather than surface-water discharge. | 3-25_Comp_and_Liquids_DBM.md, Surface Water and Drainage |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side; may reduce to 1.0% where required to maintain reasonable top-of-pile-cap elevations. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management |
| Maximum grade slope | 3H:1V maximum for road-fill side slopes, ditches, stockpiles, pond slopes, and similar grade surfaces unless specifically engineered or mandated otherwise by geotechnical report. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management |
| Ditch slope | 0.2% minimum. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management |
| Culvert slope | 0.5% minimum; 1.0% preferred. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management |
| Ditch and culvert storm basis | IDF curve for the 1:10 year, 15 minute rainfall event; IDF duration to be confirmed during detailed engineering. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management |
| NGL storage area surface control | Berm, elevation decline, or other surface-control feature shall be considered for containment of accidental leak or spill; grading under NGL bullets shall redirect NGL away from pipe rack and process areas. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management |

## References

- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md
