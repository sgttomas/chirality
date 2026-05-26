# Datasheet: DEL-080-04 — PKG-080 Inlet Compressors Vendor Engineered Equipment Package

> Source-grounding note: Substantive values are drawn from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 (locally accessible) and from `_Sources/26020-Package_Requirements.docx` package heading 33 "26020-02-PT-12-001 - Inlet Compressors" (extracted text accessible via DOCX zip; section read for this deliverable). Values without a locally accessible source are marked `TBD` or `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-080-04_vendor-engineered-equipment-package | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package ID | PKG-080 | `_CONTEXT.md` |
| Parent Workbook ID | 80 | `_CONTEXT.md` |
| Package Name | Inlet Compressors | `_CONTEXT.md` |
| Package Tag | 26020-02-PT-12-001 — Inlet Compressors | `26020-Package_Requirements.docx` package heading 33 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment); EPC Integrator integration review | `_CONTEXT.md` |
| Covers Scope Items | SOW-0119, SOW-0120, SOW-0121, SOW-0122 | `_CONTEXT.md` |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION — package-grouped heuristic) | `_CONTEXT.md`; PROJECT_DECOMP objective mapping |

## Attributes — Equipment Package Basis

| Attribute | Value | Source |
|---|---|---|
| Basic scope | Supply two identical parallel sour inlet gas reciprocating compressor packages | `26020-Package_Requirements.docx` heading 33 "Basic Scope" |
| Configuration | 2 x 50%, no dedicated spare | heading 33 "Scope Notes"; DBM SEC-05 Compressor Item table |
| Per-unit capacity | 40 MMSCFD | DBM SEC-05; heading 33 "Scope Notes" |
| Total facility capacity | 80 MMSCFD | DBM SEC-05; heading 33 "Scope Notes" |
| Compressor type | Two-stage separable reciprocating with intercooling and aftercooling | DBM SEC-05; heading 33 "Major Included Equipment" |
| Preliminary model | Ariel KBC/6 (TBC) — heading 33 cites "Ariel KBZ/6"; treat as Conflict-01 | DBM SEC-05; heading 33 |
| Cylinder arrangement | Three first-stage and three second-stage cylinders | DBM SEC-05 |
| Driver type | Electric motor | DBM SEC-05; heading 33 |
| Driver rating (each) | 5,200 hp / 3,878 kW | DBM SEC-05 "Electric Driver and Starting Basis" |
| Motor electrical | 4,000 V, three-phase, 60 Hz | DBM SEC-05 |
| Motor enclosure | TEFC or WPII; non-sparking bidirectional fans | DBM SEC-05 |
| Motor insulation | Class F insulation, Class B temperature rise | DBM SEC-05 |
| Motor speed | Approximately 891 rpm, 8-pole | DBM SEC-05 |
| Motor duty | Continuous, inverter-duty | DBM SEC-05 |
| Starter | Starting VFD (per SCA-001 VE #34) | DBM SEC-05 |
| Motor tags | KM-2150, KM-2250 | DBM SEC-05 |
| Modularization | Shop-assembled; disassembled into three pieces for transport; field-installed in self-framing buildings | DBM SEC-05; heading 33 "Major Included Equipment" |
| Included package auxiliaries | Modular self-framing buildings, piping, instrumentation, electrical, HVAC, package auxiliaries | heading 33 "Major Included Equipment" |
| Materials | NACE-compliant materials and seals (sour service) | heading 33 "Scope Notes" |
| Standards (motor) | NEMA MG1 | DBM SEC-05 |

## Conditions — Process Operating Envelope

| Compression Point | Low | Normal | Design | Max / MAWP | Source |
|---|---:|---:|---:|---:|---|
| 1st-stage suction pressure | 125 psig | 165 psig | 165 psig | 653 psig MAWP | DBM SEC-05 |
| 1st-stage discharge pressure | TBC | 380 psig | 380 psig | 653 psig MAWP | DBM SEC-05 |
| 2nd-stage suction pressure | TBC | 375 psig | 375 psig | 653 psig MAWP | DBM SEC-05 |
| 2nd-stage discharge pressure | TBC | 800 psig | 800 psig | 1,350 psig MAWP | DBM SEC-05 |

Note: Heading 33 "Scope Notes" cites "approximately 1275 kPag suction to 6550 kPag discharge" — recorded as Conflict-02 (pressure basis units / value mismatch versus DBM SEC-05 psig basis); requires human ruling. See `Guidance.md` Conflict Table.

| Temperature Item | Value | Source |
|---|---|---|
| 1st-stage suction T, low | 4 deg C | DBM SEC-05 |
| 1st-stage suction T, high | 15 deg C | DBM SEC-05 |
| 1st-stage suction T, max | 48 deg C | DBM SEC-05 |
| 2nd-stage suction T | TBC | DBM SEC-05 |
| Aerial cooler 1st/2nd stage outlet T | 43.3 deg C; 10% excess surface | DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge" |

| Process Composition Item | Value | Source |
|---|---|---|
| Service | Sour inlet gas compression | DBM SEC-05; heading 33 "Basic Scope" |
| H2S basis | Approximately 0.296 mol% H2S | DBM SEC-05 "Compression Design Conditions" |
| Design liquid SG (scrubbers) | 0.68 | DBM SEC-05 |

## Construction — Package Composition and Boundaries

| Item | Value | Source |
|---|---|---|
| Compressor packages | 2 x Ariel KBC/6 (TBC) separable reciprocating | DBM SEC-05; heading 33 |
| First-stage suction scrubber | Cyclonic separator | DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge" |
| Second-stage suction scrubber | Vertical-flow mesh/vane separation | DBM SEC-05 |
| Aerial coolers | Per package, 10% excess surface; warm-air recirculation, automated louvers, heating/plenum addressed by vendor | DBM SEC-05 |
| Recycle control valves | Dedicated per package; expected fail-open (final action TBC) | DBM SEC-05 |
| Sweet-gas start-up purge | Supplied from fuel-gas system | DBM SEC-05 |
| Packing drains/vents | Common seal pot; vapour to VRU suction; vacuum pump interface per package design | DBM SEC-05 |
| Buildings | Modular self-framing buildings | heading 33; DBM SEC-05 |
| Package contents (in vendor scope) | Compressor packages, piping, instrumentation, electrical, HVAC, package auxiliaries | heading 33 "Major Included Equipment" |
| EPC integration scope | Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, Area/Exterior Lighting, EHT, Grounding/Bonding, I&C/Control Cabling, Fire & Gas/Safety, Maintenance Access, Structural/Foundations/Supports (per Physical Interface Summary "Yes") | heading 33 "Physical Interface Summary" |
| Outside vendor scope (interface "No") | Cathodic Protection; Communications/Network; Building HVAC/Services; Grading/Site Drainage/Spill Containment; Product Loading; Pipeline/Pigging | heading 33 "Physical Interface Summary" |

## References

- `_CONTEXT.md` (deliverable identity, scope, objectives)
- `_REFERENCES.md` (authoritative reference index)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 "Inlet Compression and Sour-Gas Dehydration"
- `_Sources/26020-Package_Requirements.docx` package heading 33 "26020-02-PT-12-001 - Inlet Compressors"
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row PKG-080
- Sibling deliverable `DEL-080-02_package-datasheet` (consumer of this engineered package definition)
