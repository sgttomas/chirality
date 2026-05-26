# Datasheet — PKG-104 Package Datasheet (Structural Steel — Outside of Modules)

> Pass 1/P2 draft produced by `TASK + four-documents`. Substantive values are source-grounded to the Gate 7 accepted decomposition snapshot and the locally accessible DBM source slices. Items not supported by accessible source slices are marked `TBD` or `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-104-02_package-datasheet` | `_CONTEXT.md` |
| Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-104` Structural steel — outside of modules | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Workbook Row | 105 | `_CONTEXT.md` (Workbook Packages row 105) |
| Discipline | Structural | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0260` | `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-008` (ASSUMPTION — package-grouping heuristic per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

These are the package-level technical attributes a third-party structural-steel vendor or discipline subcontractor would need to begin engineering. Values are drawn only from accessible source slices; otherwise marked `TBD`.

| Attribute | Value | Source |
|---|---|---|
| Package boundary | Structural steel outside of process and utility modules; i.e., field-erected structural steel for pipe racks, equipment support structures, tank-farm support steel, and similar non-module steel. ASSUMPTION (from package title and PKG-104 inventory context). | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Governing building code | National Building Code of Canada (latest edition at design start) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Governing Civil and Structural Basis" (line ~2672) |
| Governing steel-design code | CAN/CSA-S16 — Design of Steel Structures (latest edition) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Governing Civil and Structural Basis" (line ~2673); §"Codes and Standards" (CSA S16:19, line ~3412) |
| Structural welding code | CSA W59-18 Welded steel construction | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Codes and Standards" (line ~3413) |
| Structural steel material — W-flange and HSS | CSA G40.20/G40.21 350W | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Governing Civil and Structural Basis" (line ~2676) |
| Structural steel material — channels, plates, angles | CSA G40.20/G40.21 300W | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Governing Civil and Structural Basis" (line ~2676) |
| Rolled/welded structural quality steel basis | CSA G40.20-13/G40.21-13 | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Codes and Standards" (line ~3411) |
| Minimum design ambient temperature | -40 deg C (governs metallurgy where affected by low temperature) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Site Basis (line ~145) |
| Snow / rain / wind / seismic loading | Per National Building Code of Canada (project-site values) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Buildings and Miscellaneous Facilities" (line ~2753); §"Foundations and Structural Supports" (`DBM-Comp_and_Liquids` line ~700) |
| Galvanizing / coating | TBD (no accessible source slice for outside-of-module steel coating system in current `_REFERENCES.md`) | TBD |
| Bolting class / fastener basis | TBD | TBD |
| Anchorage to foundations | Driven steel piles are the default foundation support for pipe racks, equipment support structures, tanks, and similar structures; final pile design parameters TBD pending geotechnical report | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Piles and Foundations" (line ~2740, ~2749) |
| Module / non-module boundary | Modules listed in DBM "Module — Shop / Field Erected" table are out of scope for this package; structural steel between, around, and supporting those modules (e.g., pipe racks, equipment support steel, tank-farm steel, truck-loading structures) is in scope. ASSUMPTION | `DBM-Deepcut/4-25_Deepcut_DBM.md` §"Buildings and Miscellaneous Facilities" module table (lines ~2766-2818) |
| Cable-tray module steel | Cable trays are installed on dedicated structural modules located on the uppermost sections of pipe racks; modules include construction walkway and support brackets; tray modules sized with at least 30% future growth | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical (line ~3023) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site minimum ambient | -40 deg C | `DBM-Comp_and_Liquids` line ~145 |
| Site location | West Doe site (BC) | `DBM-Comp_and_Liquids` §Site Basis (general) |
| Geotechnical bearing capacity | TBD pending geotechnical report | `DBM-Deepcut` §"Geotechnical and Topographical Assumptions" (line ~2687) |
| LPILE lateral-pile load-deflection curves | TBD pending geotechnical report | `DBM-Deepcut` line ~2692 |
| Dynamic design criteria | TBD pending geotechnical report (relevant for compressor-area steel that may be in scope) | `DBM-Deepcut` line ~2693 |
| Hazardous-area classification of outdoor pipe racks | General-purpose non-hazardous unless detailed classification drawings identify otherwise | `DBM-Comp_and_Liquids` §Area Classification (line ~722) |
| Cable-tray future-growth allowance on rack modules | At least 30% | `DBM-Deepcut` line ~3023 |

## Construction

| Item | Basis | Source |
|---|---|---|
| Welding | Per CSA W59-18 | `DBM-Deepcut` line ~3413 |
| Foundations supporting this package's steel | Driven steel piles as default; pile cap and connection details TBD pending geotechnical report and detailed engineering | `DBM-Deepcut` lines ~2740, ~2749 |
| Pipe-rack grading interaction | Pipe-rack alignment uses high equal-elevation ridges; pad slopes 1.5% from rack to each side (1.0% allowed to maintain reasonable top-of-pile-cap elevations); steel design must accept pile-cap elevations driven by grading basis | `DBM-Deepcut` §"Site Grading and Surface Water Management" (lines ~2708-2710) |
| Erection sequence and field connections | TBD (no accessible source slice in current `_REFERENCES.md` set) | TBD |
| QA/QC inspection and NDE basis | TBD beyond CSA-S16/W59 statutory inspection; project-specific NDE plan not in accessible source set | TBD |
| Surface preparation / coatings | TBD | TBD |

## References

- `_CONTEXT.md` — deliverable identity and scope.
- `_REFERENCES.md` — authoritative basis and source roots.
- Gate 7 PROJECT_DECOMP snapshot (DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Civil/Structural Basis (SEC-11) and Codes and Standards section.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Site Basis, Foundations and Structural Supports.
- `_Sources/26020-Package_Requirements.docx` — Workbook Packages row 105 (binary; not parsed as a text source slice in this run; location TBD for direct quotation).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — package interface register (binary; not parsed as a text source slice in this run; location TBD).
