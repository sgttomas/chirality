# Datasheet — DEL-102-02 Package Datasheet (PKG-102 Monolithic concrete foundations)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-102-02_package-datasheet` | `_CONTEXT.md` Identity table |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` Identity table |
| Parent Package ID | `PKG-102` | `_CONTEXT.md` Identity table |
| Parent Workbook ID | 102 (Workbook row 103) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-102 |
| Package Name | Monolithic concrete foundations | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-102 |
| Discipline | Structural | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-102 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-102 |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (or discipline subcontractor; source-dependent) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-102 (`ResponsibleParty` note) |
| Covers Scope Items | `SOW-0258` | `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-008` (ASSUMPTION: package-grouping heuristic at the package level) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-102-02_package-datasheet` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Monolithic concrete foundations supporting buildings, equipment, towers, tanks, modules, pipe racks, and similar structures within the West Doe Deepcut expansion civil/structural scope | `PACKAGE_REGISTER.csv` row PKG-102; DBM-Deepcut §"Civil Scope", §"Piles and Foundations" |
| Governing building code | National Building Code of Canada (latest edition) | DBM-Deepcut §"Governing Civil and Structural Basis" |
| Governing concrete design standard | CAN/CSA A23.3 — Design of Concrete Structures (latest edition) | DBM-Deepcut §"Governing Civil and Structural Basis" |
| Governing concrete materials/construction/testing standard | CSA A23.1 / A23.2 (latest edition) | DBM-Deepcut §"Governing Civil and Structural Basis" |
| Governing foundation engineering reference | Canadian Foundation Engineering Manual (latest edition) | DBM-Deepcut §"Governing Civil and Structural Basis" |
| Governing steel design standard (embedded/anchor steel where applicable) | CAN/CSA S16 (latest edition) | DBM-Deepcut §"Governing Civil and Structural Basis" |
| Default project foundation basis (project-wide) | Driven steel piles for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless a more specific basis applies | DBM-Deepcut §"Piles and Foundations" (see Conflict C-01 in Guidance.md) |
| Equipment classes with concrete-bearing foundation basis identified in source | Transformers (precast concrete bearing foundations); Compressors (precast concrete block supported on driven steel piles, subject to dynamic analysis) | DBM-Deepcut §"Piles and Foundations" table |
| Bearing capacity | TBD pending geotechnical assessment report | DBM-Deepcut §"Geotechnical and Topographical Assumptions" |
| LPILE load-deflection curves | TBD pending geotechnical assessment report | DBM-Deepcut §"Geotechnical and Topographical Assumptions" |
| Dynamic design criteria | TBD pending geotechnical assessment report | DBM-Deepcut §"Geotechnical and Topographical Assumptions" |
| Concrete mix design (compressive strength `f'c`, exposure class, durability) | TBD; not stated in available sources | location TBD |
| Reinforcement grade and detailing | TBD; not stated in available sources | location TBD |
| Embedment / anchor bolt schedule | TBD; not stated in available sources | location TBD |
| Frost depth / cold-region detailing | TBD; not stated in available sources | location TBD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | West Doe Deepcut expansion facility | DBM-Deepcut §"Civil Scope" |
| Snow / rain / wind / seismic loading | Per National Building Code of Canada, project-site values | DBM-Deepcut §"Buildings and Miscellaneous Facilities"; §"Governing Civil and Structural Basis" |
| Project-site snow load | TBD (NBCC project-site value) | location TBD |
| Project-site wind load | TBD (NBCC project-site value) | location TBD |
| Project-site seismic parameters | TBD (NBCC project-site values) | location TBD |
| Geotechnical parameters | TBD pending geotechnical assessment report (bearing capacity, lateral pile design, LPILE curves, dynamic design criteria) | DBM-Deepcut §"Geotechnical and Topographical Assumptions"; §"External Dependencies" |
| Topographical input | Existing grade surface file to be provided by survey; format/contents TBD | DBM-Deepcut §"Geotechnical and Topographical Assumptions"; §"External Dependencies" |
| Pad grading interface | Pad slopes down from main pipe racks at 1.5% (may be reduced to 1.0% to maintain reasonable top-of-pile-cap elevations) | DBM-Deepcut §"Site Grading and Surface Water Management" |
| Spill / containment design constraint (where applicable, e.g., compressor skid foundations) | Foundation/skid design shall consider containment and management of on-skid equipment oil leaks | DBM-Deepcut §"Piles and Foundations" |

## Construction

| Item | Value | Source |
|---|---|---|
| Material standards | Concrete per CSA A23.1/A23.2; design per CAN/CSA A23.3 | DBM-Deepcut §"Governing Civil and Structural Basis" |
| Default project support method (context for monolithic concrete scope boundary) | Driven steel piles unless more specific basis applies | DBM-Deepcut §"Piles and Foundations" (see Conflict C-01) |
| Identified concrete foundation forms in source | Precast concrete bearing foundations (transformers); precast concrete block on driven steel piles (compressors, subject to dynamic analysis) | DBM-Deepcut §"Piles and Foundations" |
| Cast-in-place monolithic concrete foundation details | TBD; not explicitly described in available sources for this package label | location TBD; see Conflict C-01 in Guidance.md |
| Concrete supply, placement, and curing requirements | TBD; not stated in DBM source slices for this package | location TBD |
| Quality control / testing regime | Per CSA A23.1/A23.2 (general reference); project-specific QC plan TBD | DBM-Deepcut §"Governing Civil and Structural Basis"; project-specific values TBD |
| Tolerances | TBD; not stated in available sources | location TBD |

## Interfaces (Workbook Evidence)

The following interface facts are carried as evidence from the workbook (not as separate deliverables):

| Interface ID | Type | Active (X) | Source |
|---|---|---|---|
| `IFC-1EDEDC0453` | Grading / Site Drainage / Spill Containment | YES | `INTERFACE_REGISTER.csv` row IFC-1EDEDC0453; Workbook Packages row 103 |
| `IFC-8283744B5B` | Structural / Foundations / Supports | YES | `INTERFACE_REGISTER.csv` row IFC-8283744B5B; Workbook Packages row 103 |

## External Dependencies (Source Evidence)

| External Input | Required For | Treatment |
|---|---|---|
| Geotechnical assessment report | Bearing capacity, lateral pile design, LPILE curves, dynamic design criteria, pavement design, geotextile need | TBD pending report — DBM-Deepcut §"External Dependencies" |
| Topographical survey and grade surface file | Existing ground model; grading/drainage coordination at foundation top-of-cap elevations | TBD pending survey — DBM-Deepcut §"External Dependencies" |
| Plot plan (incl. CIV-235633-5002-001 retention-pond reference) | Foundation layout coordination | External drawing dependency — DBM-Deepcut §"External Dependencies" |
| Compressor dynamic analysis | Compressor concrete-block foundation design | TBD — DBM-Deepcut §"External Dependencies" |

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts
- `_REFERENCES.md` — reference index
- `PACKAGE_REGISTER.csv` row PKG-102 — Gate-7 snapshot
- `DELIVERABLE_REGISTER.csv` row `DEL-102-02_package-datasheet` — Gate-7 snapshot
- `INTERFACE_REGISTER.csv` rows IFC-1EDEDC0453, IFC-8283744B5B — Gate-7 snapshot
- `ARTIFACT_REGISTER.csv` rows ART-413738A117, ART-2B819DEF12, ART-BA3D34EA23, ART-05281DC8CE, ART-F35AC96771 — Gate-7 snapshot
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"Civil Scope", §"Governing Civil and Structural Basis", §"Geotechnical and Topographical Assumptions", §"Site Grading and Surface Water Management", §"Piles and Foundations", §"Buildings and Miscellaneous Facilities", §"External Dependencies", §"Assumptions, TBDs, and Design Development Requirements"
- `_Sources/26020-Package_Requirements.docx` (location TBD — binary, not text-accessible from this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 103 (location TBD — binary, not text-accessible from this run; referenced as the canonical workbook row)
