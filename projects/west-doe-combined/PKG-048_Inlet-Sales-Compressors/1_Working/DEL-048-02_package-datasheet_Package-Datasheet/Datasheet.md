# Datasheet: DEL-048-02 — PKG-048 Inlet / Sales Compressors Package Datasheet

> Source-grounding note: Substantive equipment values are drawn from the accessible Design Basis Memorandum `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-05 "Compression and Acid Gas Handling Basis", referenced by the PROJECT_DECOMP package row for PKG-048. The companion source `26020-Package_Requirements.docx` package heading 3 and the RFQ document `Bid Docs/Budgetary/RFQ/Bid Docs/26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx` are referenced by the decomposition row but are not locally accessible in Markdown form; entries that depend solely on them are marked `location TBD` or `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-048-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | PKG-048 | `_CONTEXT.md` |
| Parent Workbook ID | 48 | `_CONTEXT.md` |
| Package Name | Inlet / Sales Compressors | `_CONTEXT.md` |
| Package Tag (vendor handoff) | 26020-01-PT-12-003 — Inlet / Sales Compressors | `PACKAGE_REGISTER.csv` row PKG-048, `ArtifactName` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-048 |
| Responsible Party (deliverable owner) | EPC Integrator | `_CONTEXT.md` |
| Package Vendor Scope | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` row PKG-048 |
| EPC Integrator Scope | Integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) | `PACKAGE_REGISTER.csv` row PKG-048 |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; PROJECT_DECOMP objective mapping (ASSUMPTION — package-grouped heuristic, per brief `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |
| Covers Scope Items | SOW-0115, SOW-0116, SOW-0117, SOW-0118 | `_CONTEXT.md` |

## Attributes — Process and Mechanical Basis

| Attribute | Value | Source |
|---|---|---|
| Service | Multi-service sour inlet gas (one stage) + sweet sales gas (two stages) on a common compressor frame | DBM-Deepcut SEC-05 "Compression Configuration"; "Inlet / Sales Compressor Basis" |
| Number of packages | Five (5) identical parallel multi-service packages | DBM-Deepcut SEC-05 "Compression Configuration" table; PACKAGE_REGISTER.csv row PKG-048 ("Supply Five (5) inlet/sales gas compressors") |
| Spare philosophy | Five x 20%; no installed spare package; per-package outage equals approximately 20% production loss | DBM-Deepcut SEC-05 "Compression Configuration"; "Inlet / Sales Compressor Basis" |
| Compressor type | Multi-service induction-motor-driven separable reciprocating; one inlet stage + two sales stages on common frame (three compression stages per package) | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis" |
| Preliminary model | Ariel KBC/6 (TBC; legacy conflicting frame reference remains unresolved — see Conflict Table) | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis"; "Open Items / TBC Items" |
| Inlet service — per-package capacity | 62.4 MMSCFD current supported basis (detailed capacity tables also carry 60 MMSCFD — conflict TBC) | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions"; "Open Items / TBC Items" |
| Inlet service — total facility capacity | Approximately 312 MMSCFD (5 x 62.4) current supported basis; detailed table also carries 300 MMSCFD TBC | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions" |
| Sales service — per-package capacity | 57.6 MMSCFD | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions" |
| Sales service — total facility capacity | 288 MMSCFD TBC | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions" |
| Driver type | Three-phase electric induction motor | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis" |
| Driver rating (each) | 6,700 hp (current basis; 7,000 hp legacy value remains TBD — see Conflict Table) | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis"; "Open Items / TBC Items" |
| Motor electrical | 4,000 V, three-phase, 60 Hz (basis stated for compression motors of this class) | DBM-Deepcut SEC-05 (general compression motor basis) — ASSUMPTION applied verbatim from companion sales gas booster basis in SEC-05; location TBD for inlet/sales-specific reconfirmation in `26020-Package_Requirements.docx` heading 3 |
| Start method | Starting VFD with synchronous transfer to normal-service bus after reaching full speed | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis" |
| Note on PACKAGE_REGISTER scope wording | PACKAGE_REGISTER.csv row PKG-048 description states "DOL driver with a soft-start" while DBM-Deepcut SEC-05 states starting VFD. The DBM is authoritative under Authority Hierarchy item 1 (accessible source) over the register summary; the discrepancy is logged in the Conflict Table. | PACKAGE_REGISTER.csv row PKG-048 vs DBM-Deepcut SEC-05 |
| Modularization / delivery | Modular package; field-installed in self-framing buildings (per general SEC-05 compression-package basis and SEC-08 "Buildings/Interfaces") | DBM-Deepcut SEC-05; ASSUMPTION — exact transport piece-count for this package is `location TBD` (heading 3 not accessible) |
| Sour service basis | Sour inlet gas (mol% H2S per facility composition tables); sales service gas is sweet downstream of amine | DBM-Deepcut SEC-05 (composition); detailed mol% H2S for inlet/sales compressor service `location TBD` in heading 3 |
| H2S material requirements | NACE/MR-class sour service requirements expected for inlet-service wetted parts; sweet sales-service materials per project standards. Specific material clauses `location TBD` (`26020-Package_Requirements.docx` heading 3 not accessible) | ASSUMPTION based on sour service; detailed metallurgy basis `location TBD` |
| Standards compliance (motors) | NEMA MG1 (general compression-motor basis in SEC-05) | DBM-Deepcut SEC-05 — applied by ASSUMPTION to inlet/sales compressor motors; explicit re-statement `location TBD` for heading 3 |

## Conditions — Process Operating Envelope

### Inlet Service (one stage)

| Parameter | Value | Source |
|---|---|---|
| Suction pressure (upstream / service basis) | 4,309 kPag (625 psig) | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions" |
| Suction pressure (compressor cylinder inlet) | 385 psig | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions" |
| Discharge pressure (service basis) | 7,791 kPag (1,130 psig); detailed pressure table normal/design 1,135 psig | DBM-Deepcut SEC-05 |
| Operating inlet temperature, winter | 27.3 deg C | DBM-Deepcut SEC-05 |
| Operating inlet temperature, summer | 35.7 deg C | DBM-Deepcut SEC-05 |
| J-T mode inlet temperature | TBD | DBM-Deepcut SEC-05 |
| Minimum MAWP basis (inlet suction and discharge) | 9,032 kPag (initial estimate) | DBM-Deepcut SEC-05 |
| Compression stages | One stage | DBM-Deepcut SEC-05 |

### Sales Service (two stages)

| Parameter | Value | Source |
|---|---|---|
| First-stage suction pressure (service basis) | 440 psig service basis; 430 psig normal in detailed pressure table | DBM-Deepcut SEC-05 |
| Discharge pressure (current supported basis) | 10,343 kPag (1,500 psig) | DBM-Deepcut SEC-05 |
| Detailed table second-stage discharge alternate | 1,700 psig (initial estimate; TBC) — see Conflict Table | DBM-Deepcut SEC-05; "Open Items / TBC Items" |
| First-stage suction temperature | 43.3 deg C | DBM-Deepcut SEC-05 (cooler basis table) |
| Second-stage suction temperature | 71.1 deg C | DBM-Deepcut SEC-05 (cooler basis table) |
| J-T mode temperatures | TBD | DBM-Deepcut SEC-05 |
| Minimum MAWP basis (lower sales stages) | 9,032 kPag (initial estimate) | DBM-Deepcut SEC-05 |
| Minimum MAWP basis (third-stage discharge) | 13,100 kPag (initial estimate) | DBM-Deepcut SEC-05 |
| Compression stages | Two stages | DBM-Deepcut SEC-05 |

### Air-Cooler Outlet and Pressure Drop (per package, common cooler frame)

| Cooler parameter | 1st stage (inlet service) | 2nd stage (sales service) | 3rd stage (sales service) | Source |
|---|---:|---:|---:|---|
| Winter cooler outlet temperature | 35.0 deg C | 71.1 deg C | 35.0 deg C | DBM-Deepcut SEC-05 cooler basis table |
| Summer cooler outlet temperature | 43.3 deg C | 71.1 deg C | 43.3 deg C | DBM-Deepcut SEC-05 |
| Summer dewpoint temperature | 15.1 deg C | N/A | N/A | DBM-Deepcut SEC-05 |
| Winter hydrate temperature | -2.8 deg C | N/A | N/A | DBM-Deepcut SEC-05 |
| Simulated gas-section pressure drop | 69.0 kPad | 34.5 kPad | 69.0 kPad | DBM-Deepcut SEC-05 |
| Design gas-section pressure drop | TBD | TBD | TBD | DBM-Deepcut SEC-05 |

### Scrubber Sizing Basis (per stage)

| Parameter | Value | Source |
|---|---|---|
| Type | Two-phase suction scrubbers upstream of each compression stage; sales-service scrubber necessity to be evaluated during detailed engineering | DBM-Deepcut SEC-05 |
| Assumed inlet liquid SG | 0.61 | DBM-Deepcut SEC-05 |
| Demister types acceptable | Horizontal or vertical vane-style | DBM-Deepcut SEC-05 |
| K-factor (sizing) | Not more than 0.5 Imperial, with operating-pressure de-rating | DBM-Deepcut SEC-05 |

## Construction — Package Equipment Scope

| Item | Detail | Source |
|---|---|---|
| Compression-frame configuration | Common compressor frame providing 1 inlet stage + 2 sales stages per package | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis" |
| Suction scrubbers | One two-phase scrubber per compression stage; sales-service scrubber TBC pending detailed engineering | DBM-Deepcut SEC-05 |
| Air-cooler frame | Common air-cooler frame per package; one process bundle per compression stage; automated louver control by pneumatic temperature control | DBM-Deepcut SEC-05 |
| Inlet-service suction pressure control valve | 5 psid allowable differential pressure; ET-type control valve; fails closed | DBM-Deepcut SEC-05 |
| Sales-service suction pressure control valve | None — sales-service suction pressure is controlled by the upstream J-T valve and expander; package loading regulated through the inlet-service suction PCV | DBM-Deepcut SEC-05 |
| Blowdown valves | One per service per package — inlet service blowdown valve fails OPEN; sales service blowdown valve fails CLOSED | DBM-Deepcut SEC-05 |
| Recycle control valves | Dedicated per service; sized for 100% capacity at minimum pipeline operating pressure and high suction pressure. Inlet service recycle fail position currently stated as fail OPEN (TBD); sales service recycle fail position currently stated as fail CLOSED (TBD); single full-port manual isolation valve downstream | DBM-Deepcut SEC-05 |
| Start basis | Designed to start from equalization pressure in both services; equalization > MAWP triggers alternate depressuring path back into respective inlet headers | DBM-Deepcut SEC-05 |
| Lube oil heater | Electric circulating lube-oil heater on each compressor frame for quick start | DBM-Deepcut SEC-05 |
| Start-up purge | Manual sweet-gas purge from fuel gas for sour-inlet maintenance sweeping | DBM-Deepcut SEC-05 |
| Packing drains/vents | Collected to common seal pot; vapour to VRU suction header; liquids removed by local truck-out connection | DBM-Deepcut SEC-05 |
| Sweet-service distance pieces | Require sweep purge to prevent sour-gas backflow from shared packing drain/vent recovery system | DBM-Deepcut SEC-05 |
| Clearance pockets | Automated continuously variable or automated fixed-volume clearance pockets to be evaluated against standard manual variable-volume clearance pockets in detailed engineering; final selection TBD | DBM-Deepcut SEC-05 |
| Foundations / anchorage | Equipment-specific design required (geotechnical, equipment loads, snow/wind/seismic, frost, vibration, settlement, maintenance access) | DBM-Deepcut SEC-08 (general compressor-package foundation basis) — ASSUMPTION applied; package-specific clauses `location TBD` in heading 3 |

### Applicable Interface Types (carried as evidence per `_CONTEXT.md` Notes)

From PACKAGE_REGISTER.csv row PKG-048:

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- EHT (electric heat tracing)
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

Source-grounded interface anchors (DBM-Deepcut SEC-05):

- Inlet-service suction from inlet/TEG heat exchanger combined with West Doe sour gas from 03-25 Compressor Station; discharge to downstream amine sweetening.
- Sales-service suction from turbo expander compressor aftercooler (440 psig, 110 deg F); discharge to downstream sales-gas booster and pipeline meter station train.
- Sweet-gas start-up purge tie from fuel-gas system.
- Packing drains / vents to common seal pot; vapour to VRU suction header; liquids to local truck-out.
- Acid gas / sweet gas separation in shared packing drain/vent system requires distance-piece sweep purge on sweet-service cylinders to prevent sour backflow.
- Electrical power: starting VFD with synchronous transfer to normal-service bus (4,000 V class motor) — specific MCC bus identifier `location TBD` in heading 3.

## References

- Authoritative: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-05; supporting SEC-08 for buildings/foundations)
- Decomposition row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row PKG-048
- Deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-048-02
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable)
- TBD / inaccessible: `26020-Package_Requirements.docx` package heading 3; `Bid Docs/Budgetary/RFQ/Bid Docs/26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx` (location TBD)
