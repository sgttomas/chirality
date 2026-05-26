# Datasheet — DEL-068-01 Scope of Work (PKG-068 TEG Dehydration Unit)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-068-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package | PKG-068 TEG Dehydration Unit | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-068 |
| Workbook Row | 97 | `PACKAGE_REGISTER.csv` row PKG-068 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` row PKG-068 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-068 |
| Package Tag (Workbook) | 26020-01-22-001 | `PACKAGE_REGISTER.csv` row PKG-068 |
| Package Name (Source) | 26020-01-PT-22-001 - TEG Dehydration Unit | `PACKAGE_REGISTER.csv` row PKG-068 |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-068-01 |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` row DEL-068-01 |
| Source Basis (Word) | 26020-Package_Requirements.docx, package heading 23 | `_REFERENCES.md`; `DELIVERABLE_REGISTER.csv` |
| Source Basis (RFQ) | Bid Docs/Budgetary/26020-01-PT-RFQ-22-001_TEG Dehy Unit.docx | `PACKAGE_REGISTER.csv` row PKG-068; location TBD (not locally accessible) |
| Source Basis (DBM) | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-06 Process-Gas TEG Dehydration Basis (lines 1187–1237) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |

## Attributes — Package Identity and Tagged Equipment

The TEG Dehydration Unit package is to include the following vendor-supplied tagged equipment (per `PACKAGE_REGISTER.csv` row PKG-068 scope statement):

| Item | Equipment | Source |
|---|---|---|
| 1 | Inlet Air Cooler | PACKAGE_REGISTER row 97 |
| 2 | Filter Coalescer | PACKAGE_REGISTER row 97 |
| 3 | TEG Contactor | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1222) |
| 4 | Glycol Flash Tank | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1223) |
| 5 | Glycol Reboiler / Still Column | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1225) |
| 6 | Glycol Circulation Pumps | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1231) |
| 7 | Glycol Particulate Filters | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1233) |
| 8 | Glycol Charcoal Filter | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1233) |
| 9 | Gas/Glycol Exchanger | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1224) |
| 10 | Air/Glycol Exchanger | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1228) |
| 11 | Fuel Gas Scrubber | PACKAGE_REGISTER row 97 |
| 12 | TEG Make-up Tank | PACKAGE_REGISTER row 97; DBM-Deepcut SEC-06 (l. 1232) |
| 13 | Burner Control Panel | PACKAGE_REGISTER row 97 |

Tag-number assignment per item is `TBD` pending the package vendor tag schedule.

## Conditions — Process Design Envelope (from DBM)

Values below are taken directly from DBM-Deepcut SEC-06 "Process-Gas TEG Dehydration Basis" (lines 1195–1214); they frame the EPC scope but do not substitute for the Package Datasheet.

| Parameter | Value | Source |
|---|---|---|
| Inlet gas, summer (Normal / Design) | 303.8 / 329.2 MMSCFD | DBM SEC-06 l.1199 |
| Inlet gas, winter (Normal / Design) | 308.4 / 335 MMSCFD | DBM SEC-06 l.1200 |
| Recycled regeneration gas | 25 MMSCFD (Normal/Design/Max) | DBM SEC-06 l.1201 |
| Operating pressure | 1100 psig / 7584 kPag basis (TBC); 1085 psig / 7481 kPag unresolved | DBM SEC-06 l.1207 |
| TEG inlet temperature | Summer 43 degC (110 degF); Winter 35 degC (95 degF) | DBM SEC-06 l.1208 |
| Contactor design outlet water | <=4 lb H2O/MMSCF | DBM SEC-06 l.1210 |
| Downstream mol-sieve tolerance | 10 lb H2O/MMSCF | DBM SEC-06 l.1211 |
| Contactor turndown | 3:1 (TBC) | DBM SEC-06 l.1212 |
| TEG regen turndown | 2:1 | DBM SEC-06 l.1213 |
| TEG reboiler heat medium | 425 degF heat medium supply | DBM SEC-06 l.1214 |

## Construction — Scope Boundaries (Vendor vs. EPC Integrator)

Per `PACKAGE_REGISTER.csv` row PKG-068 description:

- Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package.
- EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Applicable interface types (from PACKAGE_REGISTER row 97 — `interfaces` column):

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- EHT
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

## Covers Scope Items

- SOW-0237, SOW-0238, SOW-0239, SOW-0240 (per `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`)

## Supports Objectives (deliverable-level mapping)

- OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (per `OBJECTIVE_DELIVERABLE_MAP.csv` explicit rows for DEL-068-01_scope-of-work)

## Exclusions

- Package-level exclusions: TBD; no package-specific exclusions stated in source materials (`PACKAGE_REGISTER.csv` row PKG-068 `exclusions` column).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-068-01)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-068)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-06 Process-Gas TEG Dehydration Basis; lines 1187–1237)
- `_Sources/26020-Package_Requirements.docx` package heading 23 — location TBD (binary; not locally readable)
- Bid Docs/Budgetary/26020-01-PT-RFQ-22-001_TEG Dehy Unit.docx — location TBD (not in `_Sources/`)
