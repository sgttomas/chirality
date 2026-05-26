# Datasheet — DEL-072-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-072-01_scope-of-work | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 558 |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv row 558 |
| Parent Package | PKG-072 — Truck Product Loading Unit 4-25 | PACKAGE_REGISTER.csv row 99 |
| Parent Workbook Row | 99 (WBS 01) | PACKAGE_REGISTER.csv row 99 |
| Discipline | Mechanical | PACKAGE_REGISTER.csv row 99 |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv row 558 |
| Covers Scope Items | SOW-0245; SOW-0246; SOW-0247; SOW-0248 | SCOPE_LEDGER.csv rows 246-249 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | DELIVERABLE_REGISTER.csv row 558 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Tracking Number | 26020-01-23-001 | PACKAGE_REGISTER.csv row 99 |
| Source Basis Heading | 26020-Package_Requirements.docx package heading 26 | PACKAGE_REGISTER.csv row 99; `_REFERENCES.md` |
| Workbook Source Row | Packages row 99 | PACKAGE_REGISTER.csv row 99 |
| Source Basis Documents | `26020-Package_Requirements.docx` (heading 26); `DBM-Deepcut/4-25_Deepcut_DBM.md`; `Bid Docs/Budgetary/26020-01-PT-RFQ-23-001_FG_Skid_2.docx` | PACKAGE_REGISTER.csv row 99 SourceBasisDocs |
| Vendor-Owned Package | TRUE | PACKAGE_REGISTER.csv row 99 |
| Package Vendor Scope | package engineering; package design; vendor documentation; physical equipment package | PACKAGE_REGISTER.csv row 99 |
| EPC Integrator Scope | integration into the functional process facility; interfaces; tie-ins; constructability; procurement/construction coordination; facility-level integration | PACKAGE_REGISTER.csv row 99 |

## Conditions

Operating and design conditions as carried in the source-grounded scope ledger row SOW-0248:

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
| Heater Driver | SCR control panels, 600 V, located in electrical building | SCOPE_LEDGER.csv SOW-0248; SOW-0247 |

## Construction

Construction-relevant package composition as defined by the source scope ledger:

| Item | Source Description | Source |
|---|---|---|
| Skid | A skid for the system to be mounted on | SCOPE_LEDGER.csv SOW-0247 |
| Fuel Gas Heater | Capacity TBD; controlled by SCR (600 V); includes skin temperature thermocouple override control | SCOPE_LEDGER.csv SOW-0247 |
| Fuel Gas Scrubber | Sized using a k factor of 0.35 (imperial) maximum plus de-ration factor for operating pressure; vendor to design | SCOPE_LEDGER.csv SOW-0247 |
| By Others (excluded from vendor scope) | Shipping packages to site; installation; tie-in piping; electrical tie-in, etc. | SCOPE_LEDGER.csv SOW-0248 |

### Applicable Interface Types (PACKAGE_REGISTER row 99)

Process Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Product Loading.

## References

- `_REFERENCES.md` (deliverable-local pointer file)
- `_CONTEXT.md` (deliverable identity)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 99
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 558
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` rows 246-249
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv` rows for OBJ-001/003-010
- `_Sources/26020-Package_Requirements.docx` — package heading 26 (referenced; deliverable-local source slice not yet extracted — location TBD)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — referenced via OBJ-001 mapping; not extracted into deliverable-local slice (location TBD)
