# Datasheet: Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-004-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-004 - Site Grading |
| Workbook ID / row | 4 / Workbook Packages row 5 |
| WBS | 02 |
| CoA tracking number | 26020-01-42-003 |
| Discipline | Civil |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Covered scope item | SOW-0004 |
| Supported objectives | OBJ-002; OBJ-007; OBJ-008; OBJ-009 |

Sources: `_CONTEXT.md` Identity and Scope; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-004`; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-004-01_scope-of-work`; `26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 5.

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package name | Site Grading |
| Package discipline | Civil |
| Package responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. |
| Source package basis | Workbook-defined Civil package for Site Grading under WBS 02 with recorded physical interfaces. |
| Required scope-of-work artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. |
| Recorded interface types | Drain / Containment; Grading / Site Drainage / Spill Containment. |
| Tagged equipment | TBD; no tagged equipment list is present in the accessible source slices for this package. |
| Package exclusions | TBD; no package-specific exclusions are stated in the accessible source slices. |

Sources: Gate 7 `PACKAGE_REGISTER.csv` row `PKG-004`; Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-004-01_scope-of-work`; `26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 5.

## Conditions

| Condition | Current basis |
|---|---|
| Existing grade surface | A topographical survey will be performed; an existing grade surface file will be provided as input to plant-site grading and drainage design. Format, data model, and final contents remain TBD pending survey completion. |
| Geotechnical inputs | Bearing capacity, LPILE load-deflection curves, dynamic design criteria, road granular pavement parameters, pavement layer thicknesses, and geotextile need are TBD pending completion and review of the geotechnical report. |
| Site grading intent | Prevent off-site surface overflow from entering the expansion facility while directing and containing on-site overflow into a retention pond. |
| Surface-control intent | Consider surface-control features within the facility and around selected equipment to prevent on-site releases from discharging outside facility boundaries. |
| Storm basis for ditches and culverts | IDF curve for the 1:10 year, 15 minute rainfall event; IDF duration to be confirmed during detailed engineering. |

Sources: `4-25_Deepcut_DBM.md`, `Geotechnical and Topographical Assumptions`, `Site Grading and Surface Water Management`; `3-25_Comp_and_Liquids_DBM.md`, civil design source slice at lines 124 and 688.

## Construction

| Design / construction item | Requirement or basis |
|---|---|
| Main pipe rack grading | High equal-elevation ridges along main pipe racks. |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side. |
| Reduced pad slope allowance | Pad slope may be reduced to 1.0% where required to maintain reasonable top-of-pile-cap elevations. |
| Tank-farm perimeter | Equal elevation around tank farms, with slope or swale out from the exterior of the dike wall as required. |
| Maximum grade slope | 3H:1V maximum for grade surfaces unless specifically engineered or mandated otherwise by the geotechnical report. |
| Ditch slope | 0.2% minimum. |
| Culvert slope | 0.5% minimum; 1.0% preferred. |
| Facility pad surface | Adequate gravel thickness over the entire pad to provide a driving surface. |
| Access-road drainage definition | Only access roads will be defined by ditches on either side. |
| Retention pond | On-site retention pond with berm to capture natural runoff; location and capacity to be planned/sized during detailed engineering. |
| NGL storage area grading | Consider berm, elevation decline, or other surface-control feature; slope grading under NGL bullets to redirect NGL away from pipe rack and process areas. |

Sources: `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`.

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-004_Site-Grading/1_Working/DEL-004-01_scope-of-work_Scope-of-Work/_CONTEXT.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-004_Site-Grading/1_Working/DEL-004-01_scope-of-work_Scope-of-Work/_REFERENCES.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
