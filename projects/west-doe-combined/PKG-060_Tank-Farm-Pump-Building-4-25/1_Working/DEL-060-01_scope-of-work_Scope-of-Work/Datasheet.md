# Datasheet — DEL-060-01 Scope of Work (PKG-060 Tank Farm Pump Building 4-25)

> Descriptive datasheet for the EPC Integrator Scope of Work deliverable for PKG-060. Values are drawn from the GATE-07 PROJECT_DECOMP snapshot (PACKAGE_REGISTER, SCOPE_LEDGER, INTERFACE_REGISTER) and from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. Unsourced values are marked `TBD` or labelled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-060-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-060` | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Parent Workbook Row | 85 | PACKAGE_REGISTER.csv |
| Package Name | Tank Farm Pump Building 4-25 | PACKAGE_REGISTER.csv |
| Facility | 04-25 (West Doe Deepcut expansion) | DBM-Deepcut 4-25 SEC-01 (line 5) |
| WBS | 01 | PACKAGE_REGISTER.csv |
| Tracking Number | `26020-01-18-001` | PACKAGE_REGISTER.csv |
| Vendor Document Title | `26020-01-PT-18-002 - Tank Pumps` | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Counterpart Vendor | Package Vendor (engineering/design/equipment) | PACKAGE_REGISTER.csv ResponsibilityModel |

## Attributes

### Covered Scope Items

| Scope ID | Status | Theme |
|---|---|---|
| SOW-0189 | IN | Package identity and responsibility split (Package Vendor vs EPC Integrator) |
| SOW-0190 | IN | Basic scope and process function of in-package pumps |
| SOW-0191 | IN | Major included equipment (tag-level pump list) |
| SOW-0192 | IN | Scope notes, open items, by-others list, capacity/design throughput |

Source: GATE-07 SCOPE_LEDGER.csv.

### Tagged Equipment (in-package)

| Tag(s) | Service | Configuration | Capacity (per source) |
|---|---|---|---|
| P-9290-1, P-9293-1 | Water Transfer Pumps (radial centrifugal) | 2 x 100% identical | 218 m3/d at TBC TDH; 7.64 kW per pump (SOW-0191) |
| P-9210-1, P-9220-1 | Condensate Transfer Pumps (axial-flow multi-stage horizontal centrifugal) | 2 x 150% | 24 m3/h at TBC TDH; 350 kPad (50 psid) differential to liquids hub (SOW-0190, SOW-0191, SOW-0192; DBM-Deepcut Product Pumps line ~1673) |
| P-9200-1 | Condensate Recycle Pump (diaphragm positive-displacement Hydrocell, sealless, with discharge pulsation dampener and inlet strainer) | 1 x 100% | 20 m3/h at TBC TDH (SOW-0191; DBM-Deepcut line ~1671) |
| (vendor to assign) | Process Water Transfer Pumps (radial centrifugal) | 2 x 100% | Vendor-designed (SOW-0191) |
| (vendor to assign) | Fresh Caustic Transfer Pumps (radial centrifugal) | 2 x 100% | Vendor-designed; corrosive service; no aluminium; flow + density control for caustic strength (SOW-0191) |

ASSUMPTION: tag prefixes (`P-9xxx-1`) align with the 4-25 (Deepcut) tag block per the DBM-Deepcut Process Units table (line 2618-2622).

### Building / Structural Identity

| Field | Value | Source |
|---|---|---|
| Building Form | Self-framing building erected at site | SOW-0191 |
| Co-located equipment grouping | Tank farm pump module (DBM term) | DBM-Deepcut Product Pumps (line 1671); see also DBM Electrical line 2817 "920-1 Tank Farm Pump Module" |
| Process unit reference | "Tank Farm Pump Building 2" (DBM process-unit naming, 4-25 (Deepcut)) | DBM-Deepcut line 2555, 2618-2622 |

NOTE: The decomposition name "Tank Farm Pump Building 4-25" denotes the workbook row 85 package; the DBM table refers to the same physical building as "Tank Farm Pump Building 2" within the 4-25 facility. Both names refer to the same scope item.

## Conditions

| Field | Value | Source |
|---|---|---|
| Site / Facility | LSD 04-25-80-15W6, approx. 22.2 km north of Dawson Creek, BC | DBM-Deepcut SEC-01 (line 7) |
| Cold-start design temperature | -40 deg C startup; motors sized for inlet stabilizer composition density at -40 deg C | SOW-0192; DBM-Deepcut Product Pumps (line 1679) |
| Pump driver electrical service | 575V / 3PH / 60Hz motors | SOW-0192 |
| Starting method | DOL or VFD; local control via H-O-A or On-Off switch | SOW-0192 |
| Motor supply | 600V MCC (electrical supply to MCC is "by others") | SOW-0192 |
| Operating conditions | TBC (operating specs to be confirmed; see Throughput/Capacity and site conditions) | SOW-0192 |
| Design conditions | TBC (design specs to be confirmed) | SOW-0192 |

## Construction

| Field | Value | Source |
|---|---|---|
| Building Construction | Self-framing building erected at site | SOW-0191 |
| Foundations | By others | SOW-0192 |
| Electrical supply to MCC | By others | SOW-0192 |
| DCS integration | By others | SOW-0192 |
| Package vendor scope | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv ResponsibilityModel; OBJ-004 |
| EPC Integrator scope | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration review | PACKAGE_REGISTER.csv ResponsibilityModel; OBJ-004 |

### Applicable Interface Types (PKG-060)

From INTERFACE_REGISTER.csv (14 interface rows for PKG-060):

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- EHT
- Grounding / Bonding
- Area / Exterior Lighting
- Cathodic Protection
- I&C / Control Cabling
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

NOTE: Grading / Site Drainage / Spill Containment is listed for sibling PKG-091 (3-25 sister package) but is NOT among the 14 interface rows recorded for PKG-060. Treated as `TBD` for confirmation.

## Supported Objectives

| OBJ ID | Theme |
|---|---|
| OBJ-001 | 04-25 Deepcut facility scope (sour gas processing chain) |
| OBJ-003 | Commercial stream disposition / interfaces (condensate to 3-25 liquids hub, produced water transfer) |
| OBJ-004 | Vendor-owned package + EPC integration responsibility split |
| OBJ-005 | Electrical infrastructure, MCC/VFD, EHT, lighting, grounding, cathodic protection |
| OBJ-006 | Controls, instrumentation, I&C cabling, fire and gas |
| OBJ-007 | Utility / support-system interfaces (utility piping, drains, relief, HVAC/building services) |
| OBJ-008 | Civil/structural/site (foundations and supports, maintenance access) |
| OBJ-009 | Sour-service safety, relief, fire/gas, drain/containment, codes/standards |
| OBJ-010 | Vendor documentation, sparing, isolation, maintenance access, commissioning/turnover, open-item closure |

Association mode: `PACKAGE_HEURISTIC` (ASSUMPTION at the deliverable-ID level; PKG-060 grouping is authoritative from PACKAGE_REGISTER).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- GATE-07 snapshot: PACKAGE_REGISTER.csv (row PKG-060), DELIVERABLE_REGISTER.csv (DEL-060-01..06), SCOPE_LEDGER.csv (SOW-0189..SOW-0192), INTERFACE_REGISTER.csv (14 IFC rows for PKG-060), OBJECTIVE_REGISTER.csv (OBJ-001, OBJ-003..010)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-01 facility identity, Product Pumps subsection (~lines 1667-1679), Process Units table (~lines 2555, 2618-2622), Electrical Buildings reference (~line 2817)
- 26020-Package_Requirements.docx package heading 15 — referenced source basis for SOW-0189..SOW-0192; native document text not locally accessible (`location TBD`)
- Bid Doc `Bid Docs/Budgetary/26020-01-PT-RFQ-18-002-Tank_Farm_Pump.docx` — referenced in PACKAGE_REGISTER.csv; not locally accessible (`location TBD`)
