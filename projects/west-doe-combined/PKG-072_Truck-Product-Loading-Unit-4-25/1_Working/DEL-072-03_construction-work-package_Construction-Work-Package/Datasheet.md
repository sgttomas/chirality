# Datasheet — DEL-072-03 Construction Work Package (Truck Product Loading Unit 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-072-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| Parent Package ID | `PKG-072` | `_CONTEXT.md` |
| Parent Workbook ID | 72 | `_CONTEXT.md` |
| Package Name | Truck Product Loading Unit 4-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0245`, `SOW-0246`, `SOW-0247`, `SOW-0248` | `_CONTEXT.md` |
| Supports Objectives (ASSUMPTION: PACKAGE_HEURISTIC) | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md` (best-effort package-grouped mapping) |
| Source Reference | Workbook Packages row 99; `26020-Package_Requirements.docx` package heading 26 | `_CONTEXT.md`, `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Equipment Tag (vendor package reference) | `26020-01-PT-23-001 — Condensate Truck Loading Stations` | `26020-Package_Requirements.docx` section heading; (NOTE: the same tag is reused in the source under the FG Skid section — see Conflict Table in Guidance) |
| Location / Status | 4-25/3-25 Deepcut truck loading interface; vetted package scope basis | `26020-Package_Requirements.docx` (Location/Status line, Truck Loading Stations section) |
| Service | Condensate truck loading at 04-25 Deep Cut Gas Plant | `26020-Package_Requirements.docx` (section heading) |
| Vendor Source Basis | `Bid Docs/Budgetary/26020-01-PT-RFQ-23-001_FG_Skid_2.docx` (as listed) | `26020-Package_Requirements.docx`; SourcePath `location TBD` for the actual truck-loading RFQ — see Conflict Table |
| NGL truck/rail distribution from 04-25 | Not planned (NGL C3+ routed to NRM NEBC Connector via LACT) | `4-25_Deepcut_DBM.md` line 446 |
| Permitting status | Truck rack permit amendment required once sufficient detail is available | `4-25_Deepcut_DBM.md` line 133 |
| Spacing: pressurized bullets to truck loading station | 15.24 m (50 ft) per API 2510 | `4-25_Deepcut_DBM.md` line 257 |
| Spacing: bullet loading connection to ignition source / process area / storage tank / occupied structure | 15.24 m (50 ft) per API 2510 | `4-25_Deepcut_DBM.md` line 258 |

## Conditions

| Item | Value | Source |
|---|---|---|
| Operating temperature range (ambient) | -19 deg C to 22.2 deg C | TBD (ambient envelope for site; not specifically validated for truck-loading package — `location TBD`) |
| Design temperature range (ambient) | -40 deg C to 35 deg C | TBD (`location TBD`) |
| Hazardous-area classification | TBD | `location TBD` |
| Fire & gas applicability | Yes (interface) | `26020-Package_Requirements.docx` Physical Interface Summary |
| Spill/drain containment applicability | Yes (interface) | `26020-Package_Requirements.docx` Physical Interface Summary |

## Construction

| Item | Value | Source |
|---|---|---|
| Skid/module configuration | TBD | `location TBD` |
| Pumps (loading) | Reference: LPG Loading Pumps `26020-01-PT-18-003`; LPG Booster `26020-01-PT-18-004` (related plant scope) | `26020-Package_Requirements.docx` TOC |
| Truck-out connections (related storage) | Inlet and outlet condensate tanks share a common truck-out connection; slop tank has a dedicated truck-in/out envirobox connection | `4-25_Deepcut_DBM.md` line 1661 |
| Foundations / structural supports | Required (interface = Yes) | `26020-Package_Requirements.docx` Physical Interface Summary |
| Electrical power supply | Required (interface = Yes) | `26020-Package_Requirements.docx` Physical Interface Summary |
| Instrumentation & control | Required (interface = Yes); DCS I/O tie-in expected | `26020-Package_Requirements.docx` Physical Interface Summary |
| Lighting (area / exterior) | Required (interface = Yes) | `26020-Package_Requirements.docx` Physical Interface Summary |
| Grounding / bonding | Required (interface = Yes) | `26020-Package_Requirements.docx` Physical Interface Summary |
| Process piping tie-ins | Required (interface = Yes) | `26020-Package_Requirements.docx` Physical Interface Summary |
| Civil grading / spill containment | Required (interface = Yes) | `26020-Package_Requirements.docx` Physical Interface Summary |
| Product loading interface | Required (interface = Yes) | `26020-Package_Requirements.docx` Physical Interface Summary |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (DEL-072-03 row)
- `_Sources/26020-Package_Requirements.docx` (Package 23-001 Condensate Truck Loading Stations section; pages near heading 26 in source TOC)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (4-25 deepcut design basis — sections on storage, separation distances, NGL distribution, permitting)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 99; `location TBD` for cell-level slice — binary file)

`TBD` rows above represent values that cannot be sourced from locally accessible text and must be resolved during detailed engineering.
