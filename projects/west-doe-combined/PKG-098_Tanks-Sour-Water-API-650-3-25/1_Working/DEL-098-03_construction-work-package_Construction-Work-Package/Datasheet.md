# Datasheet — DEL-098-03 Construction Work Package

> Pass: P1_P2 (initial draft + cross-reference). Source-grounded per `_REFERENCES.md`.
> Authority: `_Sources/26020-Package_Requirements.docx` package heading 50 (Tanks, Sour Water 3-25, tag `26020-03-PT-19-007`); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` produced-water storage section.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-098-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-098` |
| Package | Tanks, Sour Water (API 650) 3-25 (`26020-03-PT-19-007`) |
| Discipline | Mechanical (construction execution discipline mix: Civil/Structural, Mechanical Static, E&I, Coatings) [ASSUMPTION] |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Covers Scope Items | SOW-0221, SOW-0222, SOW-0223, SOW-0224 |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouping heuristic per skill default) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Tank count in PKG-098 scope | Three (3) 3,800 bbl Sour Produced Water Storage Tanks: TK-9030-2, TK-9040-2, TK-9050-2 | `26020-Package_Requirements.docx` heading 50, Basic Scope |
| Tank construction code | Modified API 650, atmospheric | `26020-Package_Requirements.docx` heading 50, Major Included Equipment; DBM `3-25_Comp_and_Liquids_DBM.md` §Produced-Water Storage |
| Internal coating | Devchem 253 applied to floor, walls, and roof | `26020-Package_Requirements.docx` heading 50 |
| External insulation | External insulation with electric heat tracing | `26020-Package_Requirements.docx` heading 50; DBM §Produced-Water Storage |
| Skim system | Kennilworth-type HCl float skim system, one per tank | `26020-Package_Requirements.docx` heading 50 |
| Service | Sour produced water | `26020-Package_Requirements.docx` heading 50; DBM §Produced-Water Storage |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating pressure | Atmospheric | `26020-Package_Requirements.docx` heading 50, Scope Notes |
| Operating temperature | 10 °C | `26020-Package_Requirements.docx` heading 50, Scope Notes |
| Design pressure | 32 oz test pressure | `26020-Package_Requirements.docx` heading 50, Scope Notes |
| Design temperature (min) | -40 °C | `26020-Package_Requirements.docx` heading 50, Scope Notes |
| Design temperature (max) | 60 °C | `26020-Package_Requirements.docx` heading 50, Scope Notes |
| Design SG (tank basis) | 1.25 TBC | DBM `3-25_Comp_and_Liquids_DBM.md` §Produced-Water Storage |
| Pump fluid SG basis | 1.18 (note: discrepancy with tank SG flagged for detailed design closure) | DBM §Produced-Water Storage |
| Site minimum ambient | -40 °C governs exposed equipment, package buildings, instrumentation | DBM `3-25_Comp_and_Liquids_DBM.md` §Site Basis (line 145) |

## Construction (EPC Integrator field-execution scope)

| Item | Value | Source |
|---|---|---|
| Foundations | By EPC Integrator (vendor scope excludes foundations) | `26020-Package_Requirements.docx` heading 50, Scope Notes ("By others: Foundations") |
| Mounting tanks at site | By EPC Integrator (vendor scope excludes site mounting) | Same source |
| Electrical / instrumentation | By EPC Integrator (vendor scope excludes E&I) | Same source |
| Platforms, staircase | By EPC Integrator (vendor scope excludes platforms/staircase) | Same source |
| Applicable interfaces | Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports | `26020-Package_Requirements.docx` heading 50, Physical Interface Summary; `PACKAGE_REGISTER.csv` row PKG-098 |
| Non-applicable interfaces | Utility Piping; Electrical Power (direct); EHT (vendor-supplied as part of external heat); Communications/Network; Building HVAC; Fire & Gas; Maintenance Access (vendor row); Product Loading; Pipeline/Pigging | `26020-Package_Requirements.docx` heading 50, Physical Interface Summary |
| Hydrotest / pressure test packages | Vendor produces packages (`PIP-024`); EPC Integrator executes field hydrotest after erection (ASSUMPTION based on EPC integration scope) | Vendor deliverable list, `26020-Package_Requirements.docx` heading 50 |
| Flushing / cleaning / drying | Procedure provided by vendor (`PIP-025`); EPC Integrator executes in field (ASSUMPTION) | Vendor deliverable list |
| Anchorage / lifting | Anchor Bolt / Embedment Drawings (`STR-013`); Lifting Lug / Transport Analysis (`STR-014`) supplied by vendor | Vendor deliverable list, `26020-Package_Requirements.docx` heading 50 |

## Anticipated Artifacts (this deliverable produces)

- Construction work package (master document)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row DEL-098-03.

## References

- `_Sources/26020-Package_Requirements.docx` — package heading 50 (`26020-03-PT-19-007 - Tanks, Sour Water`)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Produced-Water Storage, Site Basis sections
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row DEL-098-03
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` — row PKG-098
- Underlying RFQ source (referenced; not directly read): `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` — location TBD locally
- Tag list for `Item No. 2` (TK-9010-2, TK-9020-2 Sour Inlet PW) and `Item No. 3` (TK-9010-1, TK-9020-1 PW): listed in package heading 50 Major Included Equipment but ASSUMPTION whether these fall inside DEL-098-03 scope (the deliverable scope statement names PKG-098 = the three TK-9030/9040/9050-2 tanks); CWP boundary for Items 2 & 3 — TBD pending human confirmation.
