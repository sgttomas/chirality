# Datasheet — DEL-072-04 Vendor Engineered Equipment Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-072-04_vendor-engineered-equipment-package | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Deliverable Type | Vendor Package Production Unit | DELIVERABLE_REGISTER.csv (DEL-072-04 row) |
| Parent Package | PKG-072 — Truck Product Loading Unit 4-25 | PACKAGE_REGISTER.csv row 99 |
| Parent Workbook Row | 99 (WBS 01) | PACKAGE_REGISTER.csv row 99 |
| Discipline | Mechanical | PACKAGE_REGISTER.csv row 99 |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Covers Scope Items | SOW-0245; SOW-0246; SOW-0247; SOW-0248 | SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | DELIVERABLE_REGISTER.csv; OBJECTIVE_DELIVERABLE_MAP.csv (ASSUMPTION: package-grouping heuristic — see Guidance) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Tracking Number | 26020-01-23-001 | PACKAGE_REGISTER.csv row 99 |
| Package Tag (companion register) | 26020-01-PT-23-001 — Condensate Truck Loading Stations | PACKAGE_REGISTER.csv row 99 |
| Source Basis Heading | 26020-Package_Requirements.docx package heading 26 | PACKAGE_REGISTER.csv row 99; `_REFERENCES.md` |
| Workbook Source Row | Packages row 99 | PACKAGE_REGISTER.csv row 99 |
| Source Basis Documents | `26020-Package_Requirements.docx` (heading 26); `DBM-Deepcut/4-25_Deepcut_DBM.md`; `Bid Docs/Budgetary/26020-01-PT-RFQ-23-001_FG_Skid_2.docx` | PACKAGE_REGISTER.csv row 99 SourceBasisDocs |
| Vendor-Owned Package | TRUE | PACKAGE_REGISTER.csv row 99 |
| Package Vendor Scope | package engineering; package design; vendor documentation; physical equipment package | PACKAGE_REGISTER.csv row 99 |
| EPC Integrator Scope | integration into the functional process facility; interfaces; tie-ins; constructability; procurement/construction coordination; facility-level integration | PACKAGE_REGISTER.csv row 99 |
| Anticipated Artifacts | Vendor engineered physical equipment package (ART-0BA5F8C575); Vendor package design basis and datasheet set (ART-071DC1CCEF); Major included equipment evidence (ART-9A43B6880A) | ARTIFACT_REGISTER.csv |

## Conditions

Operating and design conditions as carried in the source-grounded scope ledger row SOW-0248 (consistent with sibling DEL-072-01 / DEL-072-02 drafts):

| Condition | Value | Source |
|---|---|---|
| Design Flow Required | > 8.4 MMSCFD (237.5 e3m3/day) | SCOPE_LEDGER.csv SOW-0248 |
| Heated Gas Outlet Temperature | 95 F (35 C) | SCOPE_LEDGER.csv SOW-0248 |
| Final Flow | TBD | SCOPE_LEDGER.csv SOW-0248 |
| Operating Pressure | 150 psig | SCOPE_LEDGER.csv SOW-0248 |
| Ambient Temperature Range | -19 C to 22.2 C | SCOPE_LEDGER.csv SOW-0248 |
| Design Pressure | 150 psig | SCOPE_LEDGER.csv SOW-0248 |
| Design Temperature Range | -40 C to 35 C | SCOPE_LEDGER.csv SOW-0248 |
| MAWP | TBD | SCOPE_LEDGER.csv SOW-0248 |
| Heater Driver | SCR control panels, 600 V, located in electrical building | SCOPE_LEDGER.csv SOW-0247; SOW-0248 |

## Construction

Construction-relevant package composition as defined by the source scope ledger (vendor-engineered content):

| Item | Source Description | Source |
|---|---|---|
| Skid | A skid for the system to be mounted on | SCOPE_LEDGER.csv SOW-0247 |
| Low-Pressure Fuel Gas Heater | Capacity TBD; controlled by SCR (600 V); shall include skin temperature thermocouple override control on the heater | SCOPE_LEDGER.csv SOW-0247 |
| Low-Pressure Fuel Gas Scrubber | Sized using a k factor of 0.35 (imperial) maximum plus de-ration factor for operating pressure; vendor to design | SCOPE_LEDGER.csv SOW-0247 |
| Package Function | Skid serves the low-pressure fuel gas system for the West Doe Deep Cut Facility | SCOPE_LEDGER.csv SOW-0246; PACKAGE_REGISTER.csv row 99 |
| By Others (excluded from vendor scope) | Shipping packages to site; installation; tie-in piping; electrical tie-in, etc. | SCOPE_LEDGER.csv SOW-0248 |

### Applicable Interface Types (PACKAGE_REGISTER row 99)

Process Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Product Loading.

Note: For DEL-072-04, the vendor delivers package-side interface terminations only; EPC Integrator owns facility-side tie-in execution (PACKAGE_REGISTER.csv row 99 Notes).

## References

- `_REFERENCES.md`
- `_CONTEXT.md`
- DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv (GATE-07 Final Published 2026-05-24 snapshot)
- Source basis documents (locations referenced; deliverable-local slices not copied — see `_REFERENCES.md` Missing/Deferred): `26020-Package_Requirements.docx` heading 26 (location TBD — not converted locally); `DBM-Deepcut/4-25_Deepcut_DBM.md`; `Bid Docs/Budgetary/26020-01-PT-RFQ-23-001_FG_Skid_2.docx` (location TBD)
