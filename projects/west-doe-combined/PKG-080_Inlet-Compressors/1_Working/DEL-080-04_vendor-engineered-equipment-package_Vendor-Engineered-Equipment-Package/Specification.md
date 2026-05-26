# Specification: DEL-080-04 — PKG-080 Inlet Compressors Vendor Engineered Equipment Package

> Source-grounding note: Requirements derive from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 and `_Sources/26020-Package_Requirements.docx` package heading 33. Items inferred (not directly stated) are labeled `ASSUMPTION`. Items not source-grounded are marked `TBD`.

## Scope

### In Scope (Package Vendor)
The Package Vendor shall engineer, design, fabricate/supply, and deliver a complete vendor-engineered equipment package consisting of two (2) identical parallel sour inlet gas reciprocating compressor packages for the 03-25 West Doe Compressor Station, including all in-package piping, instrumentation, electrical, HVAC, package auxiliaries, and modular self-framing buildings, plus the vendor engineering deliverable set enumerated below.
Source: `26020-Package_Requirements.docx` heading 33 "Basic Scope", "Major Included Equipment", "Vendor Engineering Deliverables"; DBM SEC-05.

### Out of Scope
The following interfaces are listed as "No" in heading 33 Physical Interface Summary and are NOT in the vendor package scope: Cathodic Protection; Communications/Network; Building HVAC/Services (site building services beyond modular package buildings); Grading/Site Drainage/Spill Containment; Product Loading; Pipeline/Pigging.
Source: `26020-Package_Requirements.docx` heading 33 "Physical Interface Summary".

EPC Integrator owns facility-level integration, tie-ins, constructability, procurement/construction coordination, and review/acceptance of the vendor package (see DEL-080-06).

## Requirements

### R-080-04-001 — Configuration
Supply two (2) identical parallel reciprocating compressor packages arranged 2 x 50%, with no dedicated installed spare. Each package shall handle 40 MMSCFD; combined facility capacity 80 MMSCFD.
Source: DBM SEC-05 Compressor Item table; heading 33 "Scope Notes".

### R-080-04-002 — Compressor Type and Model
Each package shall be a two-stage separable reciprocating compressor with intercooling and aftercooling. Preliminary model: Ariel KBC/6 (TBC). The cylinder arrangement shall be three (3) first-stage and three (3) second-stage cylinders.
Source: DBM SEC-05; heading 33 "Major Included Equipment".
NOTE (Conflict-01): heading 33 cites "Ariel KBZ/6"; DBM cites "Ariel KBC/6". Final model designation requires human ruling — see `Guidance.md` Conflict Table.

### R-080-04-003 — Process Operating Envelope
The packages shall be designed to the operating envelope in `Datasheet.md` "Conditions — Process Operating Envelope". Compressor discharge pressure is fixed at 800 psig normal/design with 1,350 psig MAWP on the second-stage discharge side.
Source: DBM SEC-05 "Compression Design Conditions".
NOTE (Conflict-02): heading 33 cites suction ~1275 kPag / discharge ~6550 kPag; DBM cites psig values. Pressure basis reconciliation TBD; see Conflict Table.

### R-080-04-004 — Sour Service Materials
All wetted materials, seals, and pressure-containing components shall be compliant with NACE sour-service requirements (NACE MR0175 / ISO 15156 family — clause `location TBD` until heading-33 NACE clause text is parsed at the clause level).
Source: heading 33 "Scope Notes" ("NACE-compliant materials and seals are required"); ASSUMPTION on specific standard cite.

### R-080-04-005 — Driver and Starting Basis
Each compressor shall be driven by a 4,000 V, 3-phase, 60 Hz electric motor rated 5,200 hp / 3,878 kW, TEFC or WPII enclosure, non-sparking bidirectional fans, Class F insulation with Class B rise, ~891 rpm 8-pole, continuous inverter-duty service, compliant with NEMA MG1. Starting shall be by VFD per SCA-001 VE #34. Motor tags KM-2150 and KM-2250.
Source: DBM SEC-05 "Electric Driver and Starting Basis".

### R-080-04-006 — Scrubbers, Coolers, Recycle, Purge
First-stage suction scrubber shall be cyclonic; second-stage suction scrubber shall use vertical-flow mesh/vane internals; design liquid SG 0.68. Each package shall include aerial coolers with not less than 10% excess surface area and first/second-stage outlet temperatures of 43.3 deg C. Recycle control valves shall be dedicated per package (failure action: expected fail-open; final action TBC). Start-up sweet-gas purge shall be taken from the fuel-gas system. Packing drains and vents shall route to a common seal pot with vapour to VRU suction and a vacuum pump interface defined by the package.
Source: DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge".

### R-080-04-007 — Modularization and Transport
Packages shall be shop-assembled, disassembled into three (3) pieces for transport, and field-installed in modular self-framing buildings.
Source: DBM SEC-05 "Inlet Compression Overview"; heading 33.

### R-080-04-008 — Physical Interface Provision
The package shall provide engineered terminations and interface points for each interface flagged "Yes" in heading 33 Physical Interface Summary (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Area/Exterior Lighting [per heading 33 column M, row 66, in `26020-Packages_Interfaces.3.xlsx`]; EHT; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports).
Source: heading 33 "Physical Interface Summary".

### R-080-04-009 — Vendor Engineering Deliverable Set
The vendor shall produce the engineering deliverable set listed under heading 33 "Vendor Engineering Deliverables", organized as Core vendor documents, Core package engineering, Rotating equipment / compressors, Relief / flare / vent design, Process piping interfaces, Utility piping interfaces, Drainage / containment interfaces, Electrical / lighting / EHT / grounding, Instrumentation and controls interfaces, Building / HVAC / code interfaces, Fire and gas / technical safety interfaces, and Structural / foundations / supports / access categories. The full ID list is enumerated in `Procedure.md` "Records".
Source: heading 33 "Vendor Engineering Deliverables".

### R-080-04-010 — FAT and Vendor Documentation
The vendor shall execute an Equipment FAT / Performance Test per MEC-021 (procedure) and issue MEC-022 (report), plus the Manufacturing Record Book / Vendor Data Book (QLT-021 / MEC-023 / PRQ-016) and Mechanical IOM Manual (MEC-025).
Source: heading 33 deliverable list.

### R-080-04-011 — Pressure Equipment Registration
Provide the Pressure Equipment Registration Package (REG-022) sufficient for AB / provincial registration in the applicable jurisdiction (British Columbia; ASSUMPTION based on site location LSD 03-25-80-15W6M per DBM SEC-01 — registration jurisdiction `location TBD`).
Source: heading 33 deliverable list; DBM SEC-01 site location.

### R-080-04-012 — Relief and Flare Interface Design
Provide PRO-014 Relief and Flare Design Basis, PRO-015 PSV sizing calculations, PRO-016 Relief Valve Data Sheets, PRO-017 Flare Load Summary, and PRO-018 Blowdown / Depressurization Study, sufficient to integrate with the facility flare/relief system.
Source: heading 33 deliverable list.

## Standards

| Standard | Applies To | Source / Location |
|---|---|---|
| NEMA MG1 | Driver motors | DBM SEC-05 |
| NACE MR0175 / ISO 15156 (family) | Sour-service materials and seals | heading 33 "Scope Notes" (NACE-compliant required); specific clause `location TBD` |
| ASME B31.3 (process piping) | In-package process piping | ASSUMPTION (industry convention; not explicitly cited in accessible source slices) |
| ASME BPVC Section VIII Div. 1 (pressure vessels) | Scrubbers, KO drums on package | ASSUMPTION; `location TBD` |
| Provincial pressure equipment registration code (BC) | Pressure equipment registration (REG-022) | DBM SEC-01 site location; `location TBD` for specific code |
| API 618 (reciprocating compressors) | Compressor mechanical design | ASSUMPTION (industry convention); `location TBD` in accessible sources |

## Verification

| Requirement | Verification Method | Evidence |
|---|---|---|
| R-080-04-001 Configuration | Document review of MEC-002 Mechanical Equipment List; FAT count | MEC-002; MEC-022 FAT report |
| R-080-04-002 Compressor type/model | Vendor Data Sheets review | MEC-003 / MEC-008 Compressor Data Sheets |
| R-080-04-003 Operating envelope | Process datasheet / FAT performance curves | MEC-008; MEC-022 |
| R-080-04-004 Sour service materials | MTR / certificate review | QLT-013 Material Test Reports |
| R-080-04-005 Driver / starting | Motor data sheet review; ELE-011 Motor Starting Study; FAT no-load and load test | ELE-020; ELE-011; MEC-022 |
| R-080-04-006 Scrubbers/coolers/recycle/purge | Vendor calculations and FAT | MEC-003; MEC-014 |
| R-080-04-007 Modularization | Transport analysis and lifting/handling study review | STR-014; MEC-018 |
| R-080-04-008 Interface provision | Tie-in list / interface drawing review | PIP-004 Tie-In List; ELE-028; CTL-026 |
| R-080-04-009 Deliverable set | Vendor Document Index completeness check | PRQ-009 Vendor Document Index |
| R-080-04-010 FAT / vendor doc book | FAT witness / Vendor Data Book sign-off | MEC-021/022; PRQ-016 |
| R-080-04-011 Pressure equipment registration | Registration package acceptance by AHJ | REG-022 |
| R-080-04-012 Relief/flare interface | Integration review by EPC Integrator | DEL-080-06 review record |

## Documentation

The vendor shall deliver the complete document set per heading 33 "Vendor Engineering Deliverables", controlled per DOC-008 Vendor Document Control Procedure and indexed by PRQ-009 Vendor Document Index. Final turnover packaging is the responsibility of DEL-080-05 (Vendor Document Turnover Package).
Source: heading 33 deliverable list; `_CONTEXT.md` (sibling DEL-080-05).
