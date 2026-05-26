# Datasheet — DEL-078-04 Vendor Engineered Equipment Package

> Descriptive document for the Pig Receivers (Inlet) 4-25 vendor-engineered equipment package. Values cite source slices where supported; missing values are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-078-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-078` — Pig Receivers (Inlet) 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 78 |
| Package WBS | 01 | `PACKAGE_REGISTER.csv` row 78 |
| Package Tag (RFQ) | 26020-01-PT-35-001 — Pig Receivers (Inlet) | `PACKAGE_REGISTER.csv` row 78 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 78 |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering, design, fabrication/supply, physical equipment) with EPC Integrator integration review | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 78 |
| Facility / Area | 04-25 Deepcut (plant inlet) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Inlet Pipeline (line ~585) |
| Word Source Basis | `Bid Docs/Budgetary/26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` | `PACKAGE_REGISTER.csv` row 78 (location TBD — RFQ not locally accessible) |
| Decomposition Snapshot | GATE-07 Final Published 2026-05-24 | `_REFERENCES.md` |

## Package Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Plant inlet pipeline gas enters the facility through the pig receivers and moves on into the inlet separators | `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Equipment Quantity | 3 identical pig receivers | `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` Package Roster (line 2550) and Line-Item Requirements row 61 (line 2611) |
| Equipment Tags | PR-1010-1, PR-1020-1, PR-1030-1 | `DBM-Deepcut/4-25_Deepcut_DBM.md` Line-Item Requirements row 61 |
| Receiver Size (nominal) | 610 mm OD (24 in) | `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Skid Type | Dedicated structural steel non-enclosed skid (per receiver) | `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Safety Instrumented System | HIPPS package bundled with each receiver skid | `PACKAGE_REGISTER.csv` row 78 |
| Inlet Isolation | Full-port piggable ESDV with position transmitters on the pig receiver inlet skid | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Controls, Protection, and Safeguards (line ~809) |
| Upstream Isolation Valves | Skid-mounted isolation valves or ESDVs upstream of the pig receiver shall be full port for pigging | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Pig Containment | Barred tees shall prevent pigs from entering facility piping | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Purge Provision | Low-pressure fuel gas downstream of manual isolation valve for sweet-gas purge before opening | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Vent Routing | HP flare system | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |

## Service Conditions

| Parameter | Value | Source |
|---|---|---|
| Process Fluid | Sour wet natural gas (plant inlet pipeline gas) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Inlet Pipeline |
| Upstream Sources Feeding Facility | 06-29 Compressor Station, Vermillion Mica Compressor Station, 03-18 Sunrise, Doe 02-11 acid gas, and 03-25 Compressor Station | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Inlet Pipeline |
| 03-25 Stream Delivery Pressure (high-pressure wet sour) | 4,482–5,516 kPag (650–800 psig) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Inlet Pipeline |
| Inlet Gathering MAOP (assumed) | 1300 psig (assumed; to be validated) — `ASSUMPTION` | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Assumptions, TBDs |
| Inlet Gathering MAWP | 1440 psig TBC | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Assumptions, TBDs |
| Inlet Separator Shut ESDV Pressure Shutdown | 1360 psig | `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809 |
| Delivery Point ESDV Pressure Shutdown | TBC | `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809 |
| HIPPS Requirement Driver | If inlet pipeline MAOP exceeds facility inlet design pressure, HIPPS may be required to protect the inlet separators | `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809 |
| HIPPS Architecture / Setpoints | TBD (to be confirmed during detailed engineering) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Assumptions, TBDs |
| Design Temperature | TBD — not stated in accessible sources | `location TBD` |
| Design Pressure (Receiver Vessel) | TBD — not stated in accessible sources | `location TBD` |
| Material of Construction | TBD — not stated in accessible sources | `location TBD` |

## Construction / Mechanical Configuration

| Item | Value | Source |
|---|---|---|
| Skid Layout | Three independent dedicated structural steel non-enclosed skids, each carrying one 24" pig receiver, isolation, ESDV, purge connection, and HIPPS package | `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Enclosure | Non-enclosed (open structural steel) | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 |
| Barred Tee Locations | Downstream of each receiver as required to prevent pig migration into facility piping | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 (ASSUMPTION on exact placement; design detail per vendor) |
| Foundation / Structural Supports | Provided by vendor per skid; site grading, foundations, and structural interface are EPC-integrator-coordinated | `PACKAGE_REGISTER.csv` row 78 (Interface Types: Structural / Foundations / Supports; Grading / Site Drainage / Spill Containment) |
| Electric Heat Tracing (EHT) | Required per applicable interface type; details TBD | `PACKAGE_REGISTER.csv` row 78 (Interface Types: EHT) |
| Instrumentation & Controls | I&C / Control cabling interface to balance-of-plant control system; HIPPS logic vendor-supplied | `PACKAGE_REGISTER.csv` row 78 |

## Interfaces (Package-Level)

The applicable interface types declared for PKG-078 are: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Pipeline / Pigging.
Source: `PACKAGE_REGISTER.csv` row 78.

## Vendor Documentation (Anticipated Artifacts)

- Vendor engineered physical equipment package (three receiver skids with HIPPS).
- Vendor package design basis and datasheet set.
Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` line 435.

Detailed turnover document register, submittals, and turnover records are tracked under sibling deliverable `DEL-078-05_vendor-document-turnover-package` (not produced here).

## References

- `_CONTEXT.md` (deliverable identity and scope)
- `_REFERENCES.md` (reference index)
- `PACKAGE_REGISTER.csv` row 78 (PKG-078 authoritative package definition)
- `DELIVERABLE_REGISTER.csv` line 435 (DEL-078-04 row)
- `DBM-Deepcut/4-25_Deepcut_DBM.md` §Inlet Pipeline (line ~585), §Controls, Protection, and Safeguards (line ~809), §Interfaces (line ~832), §Assumptions/TBDs (line ~846), Package Roster (line ~2550), Line-Item Requirements row 61 (line ~2611)
- `26020-Package_Requirements.docx` package heading 31 (location TBD — .docx not locally rendered)
- RFQ source basis: `26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` (location TBD — not locally accessible)
