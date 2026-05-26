# Specification: DEL-048-04 — Vendor Engineered Equipment Package

> Normative requirements for the Inlet / Sales Compressors vendor-engineered equipment package. Requirements are derived from the Gate-07 PROJECT_DECOMP snapshot rows for PKG-048 and SOW-0115..SOW-0118. Underlying source documents (`26020-Package_Requirements.docx`, RFQ, DBM) exist in `_Sources/` but were not text-extracted at PREPARATION; clause-level citations are recorded as `location TBD` against the named source.

## Scope

### In scope (Package Vendor — engineering, design, fabrication/supply, physical equipment)
- Package engineering and detailed design for five (5) Ariel KBC/6, 3-stage reciprocating gas compressors (inlet service single-stage; sales service double-stage), each sized for 120%, with DOL driver and soft-start. [SOW-0116, SOW-0117]
- Driver supply: 8-pole induction motor, 6600 V/3PH/60Hz, 891 RPM; per-unit ratings: 5,000 kW (6,700 HP) basic; 5,220 kW (7,000 HP) at design with ~10% excess; KBZ frame, 6,700 hp, WEG motor preferred; TEFC or WPII enclosure, non-sparking bidirectional cooling fan; comply with NEMA MG 1. [SOW-0117, SOW-0118]
- Suction scrubbers: two-phase, upstream of each stage; vertical flow vane-style demisters (horizontal or vertical acceptable); K factor <= 0.5 Imperial plus pressure de-ration; liquid density basis 0.61 SG. [SOW-0117]
- Process cooling: one common air cooler frame per package serving both services, with automated louver control via pneumatic temperature control on each process bundle. [SOW-0117]
- Vendor design basis and datasheet set (vendor documentation). [`_CONTEXT.md` Anticipated Artifacts]
- Compliance with the package-level applicable interface set (see Datasheet). [PACKAGE_REGISTER PKG-048]

### Out of scope (By others — EPC Integrator or general construction)
- Shipping of compressor package to site. [SOW-0118]
- Installation on piles. [SOW-0118]
- Tie-in piping. [SOW-0118]
- Electrical connections. [SOW-0118]
- Mounting platform and stairs. [SOW-0118]
- Facility-level integration, including interfaces, tie-ins, constructability, procurement/construction coordination. [PACKAGE_REGISTER PKG-048]

## Requirements

### REQ-1 — Equipment count and configuration
The vendor shall supply five (5) inlet/sales gas compressors of make/model Ariel KBC/6, 3-stage reciprocating, with DOL driver and soft-start. Inlet service is single-stage; sales service is double-stage. Each compressor shall be sized for 120%. [SOW-0116, SOW-0117]

### REQ-2 — Driver
Drivers shall be 8-pole induction motors rated 6600 V / 3-phase / 60 Hz at 891 RPM, with per-unit rating of 5,000 kW (6,700 HP) basic (~10% excess at design), achieving 5,220 kW (7,000 HP) at design conditions. Enclosure shall be TEFC or WPII with non-sparking bidirectional cooling fan and shall comply with NEMA MG 1. Preferred frame is KBZ, 6,700 hp, WEG motor. Total connected load across five units shall be 26,100 kW (35,000 HP). [SOW-0117, SOW-0118]

### REQ-3 — Operating and design conditions

Compressors shall meet the following pressures and capacities:

| Parameter | Inlet | Sales |
|---|---|---|
| Suction pressure | 4,309 kPag (625 psig) | 3,034 kPag (440 psig) |
| Discharge pressure | 7,791 kPag (1,130 psig) | 10,343 kPag (1,500 psig) |
| Design capacity (each) | 1,766 e3m3/d (62.4 MMSCFD) | 1,630 e3m3/d (57.6 MMSCFD) |

No turndown is required. [SOW-0118]

### REQ-4 — Suction scrubbers
Two-phase suction scrubbers shall be provided upstream of each compression stage. Demisters shall be vertical flow vane-style (horizontal or vertical orientation acceptable) with K factor <= 0.5 Imperial plus de-ration for pressure; liquid density basis 0.61 SG. [SOW-0117]

### REQ-5 — Process cooling
One common air cooler frame per package shall serve both inlet and sales services, with automated louver control via pneumatic temperature control on each process bundle. [SOW-0117]

### REQ-6 — Interface compliance
The vendor-engineered package shall be designed to honor the package-level applicable interface set (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports). [PACKAGE_REGISTER PKG-048]

### REQ-7 — Vendor documentation
The vendor shall produce a vendor design basis and datasheet set covering the package. [`_CONTEXT.md` Anticipated Artifacts]

### REQ-8 — Scope demarcation
The vendor shall exclude the "by others" items listed in Scope (shipping, installation, tie-in piping, electrical connections, mounting platform and stairs) from the package supply. [SOW-0118]

### REQ-9 — Materials, area classification, gas composition (TBD)
Materials of construction, area classification, process gas composition, ambient/site design conditions, and noise/vibration limits are TBD; source clauses exist in `26020-Package_Requirements.docx` (location TBD) and `Bid Docs/Budgetary/RFQ/Bid Docs/26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx` (location TBD) and shall be resolved during source-slice extraction.

## Standards

| Standard | Applicability | Source / location |
|---|---|---|
| NEMA MG 1 | Motor (driver) | SOW-0118 |
| API 618 (reciprocating compressors) | ASSUMPTION: customary for 3-stage reciprocating gas compressors of this class; not explicitly cited in decomposition snapshot | location TBD (`26020-Package_Requirements.docx` package heading 3) |
| ASME B31.3 (process piping) | ASSUMPTION: customary for package process piping | location TBD |
| Area classification standard (e.g., API RP 500 / IEC 60079) | TBD | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-1 | Vendor design documentation and factory test records confirm 5 units, Ariel KBC/6, 3-stage configuration, 120% sizing. |
| REQ-2 | Motor nameplate, motor data sheet, NEMA MG 1 compliance certificate; FAT performance run. |
| REQ-3 | Performance curves / mechanical run test demonstrating pressure and capacity per service. |
| REQ-4 | Vessel datasheets and demister sizing calculation showing K factor and SG basis. |
| REQ-5 | Cooler datasheet, control narrative, and FAT of louver controls. |
| REQ-6 | Interface compliance matrix reviewed by EPC Integrator. |
| REQ-7 | Vendor turnover documentation accepted by EPC Integrator (see sibling DEL-048-05). |
| REQ-8 | Vendor scope-of-supply list reviewed against SOW-0118 by-others list. |
| REQ-9 | Resolved once source-slice extraction provides specific values; verification approach to be defined then. |

## Documentation

The vendor shall produce, at minimum:

- Vendor package design basis [`_CONTEXT.md`]
- Vendor package datasheet set [`_CONTEXT.md`]
- Motor and compressor mechanical datasheets (per REQ-1, REQ-2)
- Suction scrubber datasheets and demister sizing calculations (per REQ-4)
- Air cooler datasheet and cooler control narrative (per REQ-5)
- Interface compliance matrix (per REQ-6)
- Factory acceptance test (FAT) records (per Verification)
- Turnover package (handled as DEL-048-05; cross-reference only)
