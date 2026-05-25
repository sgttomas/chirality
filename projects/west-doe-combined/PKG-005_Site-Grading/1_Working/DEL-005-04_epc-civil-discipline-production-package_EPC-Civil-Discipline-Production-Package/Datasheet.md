# Datasheet: EPC / Civil Discipline Production Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-005-04_epc-civil-discipline-production-package |
| Deliverable name | EPC / Civil Discipline Production Package |
| Parent package | PKG-005 - Site Grading |
| Workbook ID / row | 5 / row 6 |
| WBS | 03 |
| CoA tracking number | 26020-01-42-003 |
| Discipline | Civil |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or civil discipline subcontractor as assigned |
| Covered scope item | SOW-0005 |
| Supported objectives | OBJ-002, OBJ-007, OBJ-008, OBJ-009 |

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-005-04_epc-civil-discipline-production-package`; `PACKAGE_REGISTER.csv` row `PKG-005`.

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package name | Site Grading |
| Package discipline | Civil |
| Package role | Authoritative companion register row |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. |
| Package scope description | Workbook-defined Civil package for Site Grading under WBS 03 with recorded physical interfaces. |
| Applicable interface types | Drain / Containment; Grading / Site Drainage / Spill Containment |
| Applicable workbook interface flags | Drain / Containment = X; Grading / Site Drainage / Spill Containment = X |
| Anticipated artifacts | Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record |

Sources: `PACKAGE_REGISTER.csv` row `PKG-005`; `INTERFACE_REGISTER.csv` rows `IFC-590C44EF2F` and `IFC-F6589335A4`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 6.

## Conditions

| Condition | Value / status |
|---|---|
| Civil design scope | Grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security are identified as civil design coverage for the 3-25 facility. |
| Surface-water management | Must prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. |
| Process-contaminated drainage | Must route to the appropriate drain or containment system rather than surface-water discharge. |
| Main pipe rack grading | High equal-elevation ridges along main pipe racks. |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side. |
| Reduced pad slope allowance | Pad slope may be reduced to 1.0% where required to maintain reasonable top-of-pile-cap elevations. |
| Maximum grade slope | 3H:1V maximum unless specifically engineered or mandated otherwise by the geotechnical report. |
| External design inputs | Geotechnical report, topographical survey/grade surface file, plot plan, and detailed drainage engineering remain TBD/open inputs. |

Sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` sections `Civil and infrastructure`, `Construction Scope Summary`, `Civil Scope`, `Surface Water and Drainage`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` sections `Civil Scope`, `Site Grading and Surface Water Management`, `External Inputs`, `Open Assumptions and Unresolved Items`.

## Construction

| Construction / production item | Status |
|---|---|
| Discipline production package basis | Required artifact for DEL-005-04. |
| Discipline deliverable register | TBD; not detailed in accepted source set. |
| Requirements closure record | Required artifact; detailed discipline requirements are source-limited and remain open. |
| Interface basis | Drain / Containment and Grading / Site Drainage / Spill Containment interfaces must be carried into the civil production package. |
| Dependency basis | No declared upstream or downstream dependencies in `_DEPENDENCIES.md`; blockers are advisory and limited to declared edges. |

Sources: `ARTIFACT_REGISTER.csv` rows `ART-84267B95AF` and `ART-3BB0AFBF4A`; `_DEPENDENCIES.md`.

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
