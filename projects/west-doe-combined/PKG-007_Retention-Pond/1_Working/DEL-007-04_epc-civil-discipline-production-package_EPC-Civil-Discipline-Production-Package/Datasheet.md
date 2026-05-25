# Datasheet: EPC / Civil Discipline Production Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-007-04_epc-civil-discipline-production-package` |
| Deliverable name | EPC / Civil Discipline Production Package |
| Parent package | `PKG-007` - Retention Pond |
| Workbook row | 8 |
| WBS | 02 |
| CoA tracking number | `26020-02-42-007` |
| Discipline | Civil |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Scope item | `SOW-0007` |
| Supported objectives | `OBJ-002`; `OBJ-007`; `OBJ-008`; `OBJ-009` |

Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for `DEL-007-04`; Gate 7 `PACKAGE_REGISTER.csv` row for `PKG-007`.

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package basis | Workbook-defined Civil package for "Retention Pond" under WBS 02. Source: Gate 7 `SCOPE_LEDGER.csv`, `SOW-0007`. |
| Package role | Civil retention pond production package for the non-vendor package scope. Source: Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-007-04`. |
| Applicable workbook interface facts | Drain / Containment; Grading / Site Drainage / Spill Containment. Source: workbook `26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 8; Gate 7 `INTERFACE_REGISTER.csv`, `IFC-AB14FD2A67` and `IFC-1B8CFB3D40`. |
| Discipline production artifacts | Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record. Source: Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-007-04`. |
| Source gap state | Detailed non-vendor package deliverable requirements are source-limited and remain open for Gate 5 disposition. Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-007-04`. |

## Conditions

| Condition | Value |
|---|---|
| Governing civil basis | Civil scope applies to facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `SEC-11 - Civil, Buildings, and Miscellaneous Facilities Basis`. |
| Site grading and drainage objective | Prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| Retention pond basis | On-site retention pond with berm to capture natural runoff; final location and capacity are detailed-engineering items. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| Preliminary civil design values | Pad slope 1.5% from pipe racks, reducible to 1.0% where required; maximum grade slope 3H:1V; ditch slope 0.2% minimum; culvert slope 0.5% minimum and 1.0% preferred; ditch/culvert storm basis is IDF curve for the 1:10 year, 15 minute rainfall event. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| Hydrology uncertainty | Rainfall basis uses NBCC 2020 Dawson Creek IDF data as proxy pending site-specific update; retention pond sizing and surface-water management carry this uncertainty. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SEC-02` rainfall basis. |
| Site climate basis | Elevation 673 m AMSL; design ambient temperature -40 deg C to +35 deg C. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Site and Civil Conditions`. |

## Construction

| Construction / production input | Current treatment |
|---|---|
| Geotechnical assessment report | Required for bearing capacity, lateral pile design, LPILE curves, dynamic design criteria, pavement design, pavement layer thicknesses, and geotextile need; currently TBD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`. |
| Topographical survey and grade surface file | Required for existing ground model, grading, drainage, and retention pond design; currently TBD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`. |
| Plot plan / retention pond reference | `CIV-235633-5002-001` is identified as an external drawing dependency for approximate retention pond location and civil layout coordination. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`. |
| Detailed engineering drainage design | Required for final IDF duration, ditch/culvert sizing, retention pond capacity, and final pond location. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`. |
| Declared upstream dependencies | None declared in deliverable `_DEPENDENCIES.md`; blocker computation is advisory and limited to declared edges. |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 `PROJECT_DECOMP.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `SCOPE_LEDGER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 8
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `SEC-11 - Civil, Buildings, and Miscellaneous Facilities Basis`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, civil design basis sections
