# Datasheet: DEL-001-04_epc-civil-discipline-production-package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-001-04_epc-civil-discipline-production-package |
| Name | EPC / Civil Discipline Production Package |
| Parent package | PKG-001 - Earthworks for foundations |
| Parent workbook row | 2 |
| WBS | 01 |
| CoA tracking number | 26020-01-42-001 |
| Discipline | Civil |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Current source basis | Workbook Packages row 2; Gate 7 PROJECT_DECOMP snapshot; 04-25 Deepcut DBM civil basis |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package name | Earthworks for foundations | 26020-Packages_Interfaces_4_export.xlsx, `Packages` sheet row 2 |
| Workbook discipline | Civil | 26020-Packages_Interfaces_4_export.xlsx, `Packages` sheet row 2 |
| Workbook interface flags | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | 26020-Packages_Interfaces_4_export.xlsx, `Packages` sheet row 2 |
| Package responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources | Gate 7 `PACKAGE_REGISTER.csv`, PKG-001 |
| Scope description | Workbook-defined Civil package for Earthworks for foundations under WBS 01 with recorded physical interfaces | Gate 7 `PACKAGE_REGISTER.csv`, PKG-001 |
| Supported objectives | OBJ-001; OBJ-008 | `_CONTEXT.md`; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Covered scope item | SOW-0001 | `_CONTEXT.md`; Gate 7 `SCOPE_LEDGER.csv` |

## Conditions

| Condition | Current Basis | Source |
|---|---|---|
| Facility/site context | 04-25 West Doe Deepcut expansion; north of Dawson Creek, British Columbia; Unit 03/04-25-80-15 W6M; plant elevation 673 m AMSL | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-02 Site Data Basis |
| Site data finality | Site data is to be updated after receipt of the site geotechnical report | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-02 Site Data Basis |
| Plot plan dependency | Final equipment placement, coordinate-level layout, road/access geometry, spacing verification, and drawing conflict checks are TBD pending CIV-235633-5002 | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-02 Plot Plan Status |
| Geotechnical dependency | Bearing capacity, lateral pile design, LPILE curves, dynamic design criteria, pavement design, pavement layer thicknesses, and geotextile need are TBD pending geotechnical report | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies |
| Topographical dependency | Existing ground model, grading, drainage, and retention-pond design are TBD pending survey completion and grade-surface delivery | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies |

## Construction

| Topic | Current Basis | Source |
|---|---|---|
| Civil scope basis | Civil, structural, site-grading, drainage, road, foundation, building, and miscellaneous-facility basis applies to the facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil Scope |
| Grading and drainage | Prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side; may be reduced to 1.0% where needed to maintain reasonable top-of-pile-cap elevations | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Maximum grade slope | 3H:1V maximum unless specifically engineered or mandated otherwise by the geotechnical report | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Ditch and culvert basis | Ditch slope 0.2% minimum; culvert slope 0.5% minimum and 1.0% preferred; current storm basis is 1:10 year, 15 minute rainfall event; final IDF duration TBD | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Retention pond | On-site retention pond with berm is required; location and capacity are TBD pending plot plan and detailed engineering | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Default foundation support | Driven steel piles are the default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless detailed engineering confirms otherwise | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| Detailed production deliverable register | TBD discipline deliverable register | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` notes source-limited discipline requirements |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 2.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-02 and SEC-11.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, DEL-001-04.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, PKG-001.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-001-04.
