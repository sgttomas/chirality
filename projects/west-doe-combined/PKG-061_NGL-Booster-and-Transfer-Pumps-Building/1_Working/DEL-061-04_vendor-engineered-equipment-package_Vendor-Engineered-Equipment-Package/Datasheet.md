# Datasheet: DEL-061-04 Vendor Engineered Equipment Package — NGL Booster and Transfer Pumps Building

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-061-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-061` |
| ParentWorkbookID | 61 |
| PackageName | NGL Booster and Transfer Pumps Building |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| CoversScope | `SOW-0149`, `SOW-0150`, `SOW-0151`, `SOW-0152` |
| SupportsObjectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC association at PKG-061; explicit row mappings confirmed in `OBJECTIVE_SCOPE_MAP.csv`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Building / Package title | NGL Booster and Transfer Pumps Building | DBM-Deepcut `4-25_Deepcut_DBM.md` Trace Appendix package table (NGL Booster and Transfer Pumps Building row) |
| Function | NGL product booster and transfer pumping (downstream of NGL storage, feeding NGL loading and/or product hub) | DBM-Deepcut `4-25_Deepcut_DBM.md` Scope summary line: "NGL ... NGL product pumps, and NGL product booster pumps" |
| Major equipment count | 2 pumps | DBM-Deepcut Trace Appendix row 58: "NGL Booster and Transfer Pumps ... 2" |
| Tagged equipment | `P-9570-1`, `P-9580-1` | DBM-Deepcut Trace Appendix row 58 |
| Equipment category | Pumps (API 610, multi-stage can) | DBM-Deepcut Trace Appendix row 58 (Equipment Category column) |
| Source DBM | 4-25 (Deepcut) | DBM-Deepcut Trace Appendix row 58 |
| Source package row | Workbook Packages row 75; `26020-Package_Requirements.docx` package heading 17 | `_CONTEXT.md` Source Reference; `DELIVERABLE_REGISTER.csv` row 417 |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Service fluid | NGL product (C2+ NGL stream leaving NGL storage) | ASSUMPTION (from package title and DBM scope line — `4-25_Deepcut_DBM.md` line 73); detailed composition `TBD` (location TBD in `26020-Package_Requirements.docx` package heading 17, not locally parseable) |
| Design flow | TBD | location TBD: `26020-Package_Requirements.docx` package heading 17 |
| Differential pressure / head | TBD | location TBD: `26020-Package_Requirements.docx` package heading 17 |
| NPSHa available / NPSHr | TBD | location TBD: `26020-Package_Requirements.docx` package heading 17 |
| Suction / discharge temperature | TBD | location TBD: `26020-Package_Requirements.docx` package heading 17 |
| Suction / discharge pressure | TBD | location TBD: `26020-Package_Requirements.docx` package heading 17 |
| Sparing philosophy | TBD (ASSUMPTION: 2 x 100% based on count of 2 — DBM-Deepcut Trace Appendix row 58; sparing percentages not stated in the NGL Booster row of the DBM Sparing table) | DBM-Deepcut sparing table does not list "NGL Booster" explicitly; confirm against `26020-Package_Requirements.docx` |
| Driver type / rating | TBD | location TBD: `26020-Package_Requirements.docx` |
| Area classification | TBD | location TBD: `26020-Package_Requirements.docx` |
| Site / climate conditions | Per project Basis of Design (cold climate, -40 deg C startup family) | ASSUMPTION based on DBM-Deepcut `4-25_Deepcut_DBM.md` line 1679 (-40 deg C startup language for sister condensate pumps) |

## Construction

| Item | Value | Source |
|---|---|---|
| Pump type | API 610, multi-stage can (VS-type vertical can pump implied by "multi-stage can") | DBM-Deepcut Trace Appendix row 58 ("Pumps (API 610, multi-stage can)") |
| Governing pump standard | API 610 (latest edition adopted by project — edition `TBD`) | DBM-Deepcut Trace Appendix row 58 |
| Seal | TBD (API 682 expected — ASSUMPTION) | API 682 typical companion for API 610; confirmation `TBD` against `26020-Package_Requirements.docx` |
| Driver | Electric motor (ASSUMPTION); voltage / hp `TBD` | Project convention; DBM does not specify driver for `P-9570-1/P-9580-1` |
| Material class | TBD | location TBD: `26020-Package_Requirements.docx` |
| Baseplate / skid | Vendor-supplied skid as part of the engineered equipment package | `_CONTEXT.md` Scope ("physical equipment package") |
| Building / enclosure | "NGL Booster and Transfer Pumps Building" — heated, enclosed building (ASSUMPTION from "Building" descriptor and project cold-climate basis) | DBM-Deepcut Trace Appendix building name |
| Instrumentation | Per API 610 minimum plus project I&C basis (vibration, temperature, pressure, flow — `TBD` detail) | ASSUMPTION |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — DBM scope statement (line 73), Trace Appendix package row 58 (`P-9570-1`, `P-9580-1`), sister-service pump references for cold-climate startup conventions (line 1679).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` package heading 17 — **location TBD** (binary source, not locally text-accessible; detail values must be confirmed by re-extraction or vendor handoff from EPC Package Datasheet `DEL-061-02`).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local).
- Decomposition `DELIVERABLE_REGISTER.csv` row 417; `OBJECTIVE_SCOPE_MAP.csv` rows for PKG-061 (objectives explicitly mapped).
- API 610 (latest project-adopted edition — edition `TBD`).
