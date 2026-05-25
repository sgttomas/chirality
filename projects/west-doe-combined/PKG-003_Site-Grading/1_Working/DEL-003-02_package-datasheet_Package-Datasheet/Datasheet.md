# Datasheet: DEL-003-02_package-datasheet — Package Datasheet

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-003-02_package-datasheet` |
| Deliverable name | Package Datasheet |
| Parent package | `PKG-003` — Site Grading |
| Source scope item | `SOW-0003` |
| Discipline | Civil |
| Deliverable type | EPC Package Datasheet |
| Responsible party | EPC Integrator |
| Workbook source | Workbook Packages row 4 |
| WBS | `01` |
| CoA tracking number | `26020-01-42-003` |
| Package description | Workbook-defined Civil package for Site Grading under WBS 01 with recorded physical interfaces |

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package role | Site grading package data required for third-party vendor or discipline package engineering and design | Gate 7 `PROJECT_DECOMP.md`, Gate 5 accepted deliverable basis |
| Package discipline | Civil | `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv`; workbook Packages row 4 |
| Interface facts carried by this datasheet | Drain / Containment; Grading / Site Drainage / Spill Containment | Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 `ARTIFACT_REGISTER.csv`; workbook Packages row 4 |
| Civil basis scope relevant to the package | Site grading, drainage, ditching, culvert, retention-pond, and surface-control requirements | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil Scope |
| External source dependencies | Geotechnical assessment report; topographical survey and grade surface file; plot plan including retention-pond reference; detailed drainage engineering | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies |

## Conditions

| Condition | Value / treatment | Source |
|---|---|---|
| Facility context | West Doe Deepcut expansion, WBS 01 | `_CONTEXT.md`; workbook Packages row 4; Gate 7 `SCOPE_LEDGER.csv` |
| Surface-water objective | Prevent off-site surface overflow from entering the expansion facility; direct and contain on-site overflow into a retention pond | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Site Grading and Surface Water Management |
| Surface-control objective | Consider surface-control features within the facility and around selected equipment to prevent on-site releases from discharging outside facility boundaries | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Site Grading and Surface Water Management |
| Existing grade surface | ASSUMPTION: grade surface file will represent existing ground elevations suitable for grading and drainage design; final format and content are TBD | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Geotechnical and Topographical Assumptions |
| Geotechnical design basis | TBD pending completion and review of the geotechnical assessment report | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Geotechnical and Topographical Assumptions |
| Retention pond location and capacity | TBD pending plot-plan coordination and detailed engineering | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, External Dependencies and Assumptions |

## Construction

| Design item | Datasheet value |
|---|---|
| Main pipe rack grading | High equal-elevation ridges along main pipe racks |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side |
| Reduced pad slope allowance | Pad slope may be reduced to 1.0% where required to maintain reasonable top-of-pile-cap elevations |
| Maximum grade slope | 3H:1V maximum for road-fill side slopes, ditches, stockpiles, pond slopes, and similar grade surfaces, unless specifically engineered or mandated otherwise by the geotechnical report |
| Ditch slope | 0.2% minimum |
| Culvert slope | 0.5% minimum; 1.0% preferred |
| Ditch and culvert storm basis | IDF curve for the 1:10 year, 15 minute rainfall event |
| IDF duration | TBD; to be confirmed during detailed engineering |
| Facility pad surface | Adequate gravel thickness over the entire pad to provide a driving surface |
| Access-road drainage definition | Only access roads will be defined by ditches on either side |
| NGL storage area surface control | Berm, elevation decline, or other surface-control feature to be considered for accidental leak or spill containment; grading under NGL bullets to redirect NGL away from pipe rack and process areas |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- Gate 7 final published PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row with ID #3 / workbook row 4
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil, Buildings, and Miscellaneous Facilities Basis
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Plant Layout, Spacing, Civil, and Buildings, as supporting cross-facility civil context
