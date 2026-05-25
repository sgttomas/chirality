# Datasheet: DEL-003-04_epc-civil-discipline-production-package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-003-04_epc-civil-discipline-production-package` |
| Deliverable Name | EPC / Civil Discipline Production Package |
| Parent Package | `PKG-003` - Site Grading |
| Parent Workbook ID | 3 |
| Discipline | Civil |
| Type | EPC/Discipline Production Unit |
| Responsible Party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Scope Item | `SOW-0003` |
| Source Reference | Workbook Packages row 4 |
| Accepted Decomposition Snapshot | `GATE-07_Final_Published_2026-05-24` |

## Attributes

| Attribute | Current Basis | Source |
|---|---|---|
| Package name | Site Grading | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-003-04`; workbook Packages row 4 |
| Workbook row | Row 4: ID 4, WBS `02`, CoA Tracking Number `26020-01-42-003`, Package `Site Grading`, Discipline `Civil` | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 5 in file / workbook Packages row 4 |
| Active workbook interfaces | Drain / Containment; Grading / Site Drainage / Spill Containment | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, workbook row 4 |
| Anticipated artifacts | Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-003-04` |
| Civil deliverable candidates | Grading Plan (`CIV-003`); Drainage / Stormwater Management Report (`CIV-004`); Retention Pond / Containment Basin Design (`CIV-015`); Civil MTO / Quantity Take-Off (`CIV-019`) | `_Sources/26020-Package_Requirements.docx`, civil grading / spill containment interfaces entries |
| Civil scope coverage | Grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions |

## Conditions

| Condition | Value / Treatment | Source |
|---|---|---|
| Governing civil/structural basis | National Building Code of Canada; CAN/CSA-S16; CAN/CSA A23.3; Canadian Foundation Engineering Manual; CSA G40.20/G40.21; CSA A23.1/A23.2; Rational Method for runoff calculations; Manning's equation for ditch and culvert sizing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| Site grading objective | Prevent off-site surface overflow from entering the expansion facility; direct and contain on-site overflow into a retention pond | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Surface-control objective | Consider surface-control features within the facility and around selected equipment to prevent on-site releases from discharging outside facility boundaries | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side; may be reduced to 1.0% where required to maintain reasonable top-of-pile-cap elevations | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Maximum grade slope | 3H:1V maximum unless specifically engineered or mandated otherwise by the geotechnical report | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Ditch slope | 0.2% minimum | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Culvert slope | 0.5% minimum; 1.0% preferred | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Ditch and culvert storm basis | IDF curve for the 1:10 year, 15 minute rainfall event; duration to be confirmed during detailed engineering | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Rainfall basis uncertainty | NBCC 2020 Dawson Creek IDF data is a proxy pending site-specific update | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 rainfall basis |
| Topographical survey / grade surface | Required for existing ground model, grading, drainage, and retention-pond design; final format and contents TBD | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Geotechnical and Topographical Assumptions and External Dependencies |

## Construction

| Item | Current Basis |
|---|---|
| Production package content | TBD discipline deliverable register; production drawings/calculations/reports for civil grading and drainage as required by detailed engineering |
| Required inputs | Geotechnical assessment report; topographical survey and grade surface file; plot plan including retention pond reference; detailed engineering drainage design |
| Retention pond | Pond with berm to capture natural runoff; location and capacity TBD pending plot plan coordination and detailed engineering |
| Operations interface | Operations plans/procedures required for release monitoring, analysis, and confirmation of non-contaminated surface water before removal or pump-out activities |
| Package-specific closure | Source-limited; detailed non-vendor package deliverable requirements remain open for Gate 5 disposition |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-003-04`
- Gate 7 `ARTIFACT_REGISTER.csv`, package `PKG-003` artifact rows where applicable
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, workbook row 4
- `_Sources/26020-Package_Requirements.docx`, civil grading / spill containment interface entries
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil, Buildings, and Miscellaneous Facilities Basis
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 rainfall basis and SEC-11 Plant Layout, Spacing, Civil, and Buildings
