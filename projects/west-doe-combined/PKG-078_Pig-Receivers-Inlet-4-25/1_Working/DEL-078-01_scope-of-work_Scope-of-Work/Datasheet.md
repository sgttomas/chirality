# Datasheet — DEL-078-01 Scope of Work (PKG-078 Pig Receivers (Inlet) 4-25)

> Descriptive identity datasheet for the EPC Integrator Scope of Work deliverable. Source-grounded to the GATE-07 PROJECT_DECOMP snapshot extracted from `26020-Package_Requirements.docx` package heading 31 and Workbook Packages row 78.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-078-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (GATE-07) |
| Deliverable Name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` row DEL-078-01 |
| Parent Package | `PKG-078` — Pig Receivers (Inlet) 4-25 | `PACKAGE_REGISTER.csv` row PKG-078 |
| Workbook Row | 78 | `PACKAGE_REGISTER.csv`; Workbook Packages row 78 |
| WBS | 01 (Deepcut 04-25 facility) | `PACKAGE_REGISTER.csv` PKG-078 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` PKG-078 |
| Tracking Number | `26020-01-35-001` | `PACKAGE_REGISTER.csv` PKG-078 (TrackingNumber) |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv`; `PACKAGE_REGISTER.csv` (responsibility model) |
| Covered Scope Items | `SOW-0161`, `SOW-0162`, `SOW-0163`, `SOW-0164` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Source Basis | Workbook Packages row 78; `26020-Package_Requirements.docx` package heading 31; `Bid Docs/Budgetary/26020-01-PT-RFQ-35-001-Pig_Recv_2.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md` | `PACKAGE_REGISTER.csv` PKG-078 (SourceBasis) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Plant inlet pipeline gas enters the facility through the pig receivers and moves on into the inlet separators. | `PACKAGE_REGISTER.csv` PKG-078; `SCOPE_LEDGER.csv` SOW-0162 |
| Quantity of Receivers | 3 identical pig receivers | `SCOPE_LEDGER.csv` SOW-0162; `PACKAGE_REGISTER.csv` PKG-078 |
| Receiver Size | 610 mm (24") OD | `SCOPE_LEDGER.csv` SOW-0162, SOW-0163 |
| Tagged Receiver Assemblies | `PR-1010-1`, `PR-1020-1`, `PR-1030-1` | `SCOPE_LEDGER.csv` SOW-0163 |
| Skid Configuration | Dedicated structural steel non-enclosed skids; all skid-mounted isolation or ESDV | `SCOPE_LEDGER.csv` SOW-0162, SOW-0163 |
| HIPPS Package | Each receiver skid includes a High Integrity Pressure Protection System (HIPPS) with ESDVs upstream of the pig receiver; pressure control valve and outlet pressure transmitter via PID control to maintain inlet-separator vessel operating pressure below applicable limit; shutdown valve with pneumatic hi-low shutoff plus a redundant additional shutdown valve with pneumatic hi-low, closing the high-pressure inlet. | `SCOPE_LEDGER.csv` SOW-0163 |
| Sour-Service Design Basis | Design 1.0 mol% H2S | `SCOPE_LEDGER.csv` SOW-0163 |
| Sweet-Gas Purge | Sweet gas purge downstream of manual isolation valve for sour-gas purge of the receiver barrel prior to opening for pig retrieval | `SCOPE_LEDGER.csv` SOW-0163 |
| Vent Routing | Vent line to HP flare system | `SCOPE_LEDGER.csv` SOW-0163 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Design Throughput | 225 MMSCFD | `SCOPE_LEDGER.csv` SOW-0164 |
| Historical Ambient Temperature | −19 °C min, 22.2 °C max | `SCOPE_LEDGER.csv` SOW-0164 |
| Normal Operating Pressure | 653 psig to 725 psig | `SCOPE_LEDGER.csv` SOW-0164 |
| MAOP | 1300 psig | `SCOPE_LEDGER.csv` SOW-0164 |
| Normal Flowrate per Receiver | TBC (per source) | `SCOPE_LEDGER.csv` SOW-0164 |
| Design Pressure (low / normal high) | 653 psig / 725 psig | `SCOPE_LEDGER.csv` SOW-0164 |
| MAWP | 1440 psig | `SCOPE_LEDGER.csv` SOW-0164 |
| Ambient Design Temperature | −40 °C min, +35 °C max | `SCOPE_LEDGER.csv` SOW-0164 |

## Construction (Identity & Boundaries)

| Item | Value | Source |
|---|---|---|
| Package-vs-Facility Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` PKG-078 (ResponsibilityModel) |
| By Others (excluded from package) | Interconnecting piping, DCS integration, foundations, electrical supply to MCC | `SCOPE_LEDGER.csv` SOW-0164 |
| Applicable Interface Types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Pipeline / Pigging | `PACKAGE_REGISTER.csv` PKG-078 (InterfaceTypes) |
| Package Exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` PKG-078 (Exclusions) |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- GATE-07 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
  - `PACKAGE_REGISTER.csv` row `PKG-078`
  - `DELIVERABLE_REGISTER.csv` row `DEL-078-01_scope-of-work`
  - `SCOPE_LEDGER.csv` rows `SOW-0161`, `SOW-0162`, `SOW-0163`, `SOW-0164`
  - `OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-003`–`OBJ-010`
- Upstream source basis (not locally re-read here; cited via register provenance): Workbook Packages row 78; `26020-Package_Requirements.docx` package heading 31; `Bid Docs/Budgetary/26020-01-PT-RFQ-35-001-Pig_Recv_2.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md`

## Open Items

- Normal flowrate per receiver: TBC per `SOW-0164`.
- HIPPS set-point ("operating pressure below applicable") quantitative threshold: `TBD` — source SOW-0163 states the control intent but the numerical setpoint is not in the extracted source slice.
- Detailed sub-deliverable mechanical/vendor-document list: `TBD` — `26020-Package_Requirements.docx` package heading 31 detail beyond the SCOPE_LEDGER extract is not locally re-read in this pass.
