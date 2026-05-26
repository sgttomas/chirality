# Datasheet: DEL-104-01_scope-of-work — Scope of Work

> Descriptive datasheet for the EPC Integrator Scope of Work covering PKG-104
> "Structural steel - outside of modules". All non-trivial values are cited to
> their source slice; missing values are marked `TBD`, inferences as
> `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-104-01_scope-of-work` | `_CONTEXT.md` Identity |
| Name | Scope of Work | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-104` | `_CONTEXT.md` Identity |
| ParentWorkbookID | 104 | `_CONTEXT.md` Identity |
| PackageName | Structural steel - outside of modules | `_CONTEXT.md` Identity |
| Discipline | Structural | `_CONTEXT.md` Identity; `PACKAGE_REGISTER.csv` row `PKG-104` |
| Type | EPC Scope of Work | `_CONTEXT.md` Identity |
| ResponsibleParty | EPC Integrator (drafting); discipline-subcontractor assignment is source-dependent (`ASSUMPTION`) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` Responsibility note |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-104` |
| CoA Tracking | 26020-01-36-004 | `PACKAGE_REGISTER.csv` row `PKG-104` |
| Workbook source row | Packages row 105 | `_CONTEXT.md` Source Reference; `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Scope item covered | `SOW-0260` (IN scope) | `SCOPE_LEDGER.csv` row `SOW-0260` |
| Supported objectives | `OBJ-001`, `OBJ-008` (PACKAGE_HEURISTIC; **ASSUMPTION** at deliverable-ID granularity) | `_CONTEXT.md` Supports Objectives; `OBJECTIVE_PACKAGE_MAP.csv` |
| Package function (workbook) | Workbook-defined Structural package for "Structural steel - outside of modules" under WBS 01 with recorded physical interfaces | `PACKAGE_REGISTER.csv` row `PKG-104` (Description field) |
| Applicable interface types | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row `PKG-104`; `INTERFACE_REGISTER.csv` `IFC-CCDE4B56CA`, `IFC-ECDD4D3A15` |
| Discipline basis section | DBM-Deepcut SEC-11 "Civil, Buildings, and Miscellaneous Facilities Basis" | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2648 |
| Tagged major equipment | TBD (no specific tagged equipment for `PKG-104` is enumerated in `PACKAGE_REGISTER.csv` or the workbook row available to PREPARATION) | `PACKAGE_REGISTER.csv`; **TBD** |
| Vendor / sub-package ownership model | No separate vendor-package ownership model inferred from current sources | `PACKAGE_REGISTER.csv` Responsibility note |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` row `PKG-104` |

## Conditions

Site/environmental conditions governing this scope are inherited from facility
basis (not restated as deliverable values).

| Condition | Value | Source |
|---|---|---|
| Governing site-load drivers | Snow, rain, wind, and seismic loading per National Building Code of Canada | DBM-Deepcut SEC-11, "Buildings and Miscellaneous Facilities", line 2753 |
| Minimum ambient (affects steel design) | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices | DBM-Comp_and_Liquids SEC-04 line 145 (cross-reference for low-temperature impact on structural steel design) |
| Foundation default | Driven steel piles as default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures | DBM-Deepcut SEC-11, "Piles and Foundations", lines 2738-2749 |
| Site-grading interface | Pad slopes down from pipe racks at 1.5% to each side; equal-elevation ridges along main pipe racks | DBM-Deepcut SEC-11, "Site Grading and Surface Water Management", lines 2706-2719 |

## Construction (Material and Code Basis)

Materials and codes applicable to "structural steel - outside of modules" as
drawn from the project structural basis:

| Item | Requirement | Source |
|---|---|---|
| Building code | National Building Code of Canada | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis", line 2672 |
| Steel design | CAN/CSA-S16 Design of Steel Structures | DBM-Deepcut SEC-11 line 2673; reinforced by CSA S16:19 entry at line 3412 |
| Structural steel material | CSA G40.20/G40.21 350W for W-flange and HSS; 300W for channels, plates, and angles | DBM-Deepcut SEC-11 line 2676 |
| Concrete design (where related foundations apply) | CAN/CSA A23.3 Design of Concrete Structures | DBM-Deepcut SEC-11 line 2674 |
| Concrete materials, construction, testing | CSA A23.1/A23.2 | DBM-Deepcut SEC-11 line 2677 |
| Foundation engineering | Canadian Foundation Engineering Manual | DBM-Deepcut SEC-11 line 2675 |
| Geotechnical inputs (bearing capacity, LPILE, dynamic criteria, pavement) | TBD pending geotechnical report | DBM-Deepcut SEC-11 "Geotechnical and Topographical Assumptions", lines 2687-2697 |

## Anticipated Artifacts (this deliverable produces)

- Package scope of work (`ART-1667AE1F32`)
- Tagged equipment and package identity list (`ART-6192616307`)
- Package function and whole-facility integration narrative (`ART-4288CE535A`)
- Package responsibility assignment record (`ART-FE5EE5E445`)

Source: `ARTIFACT_REGISTER.csv` rows scoped to `DEL-104-01_scope-of-work`.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-11 in particular)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-04 ambient; SEC-11 layout context)
- `_Sources/26020-Package_Requirements.docx` — `location TBD` (not parsed in this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 105 — `location TBD` (xlsx not opened in this run)
