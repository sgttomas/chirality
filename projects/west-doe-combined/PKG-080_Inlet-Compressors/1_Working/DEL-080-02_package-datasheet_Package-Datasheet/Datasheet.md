# Datasheet: DEL-080-02 — PKG-080 Inlet Compressors Package Datasheet

> Source-grounding note: Substantive equipment values are drawn from the accessible Design Basis Memorandum `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (referenced by the PROJECT_DECOMP package row for PKG-080). The companion source `26020-Package_Requirements.docx` package heading 33 is referenced by the decomposition but is not locally accessible in Markdown form; entries that depend solely on it are marked `location TBD` or `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-080-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | PKG-080 | `_CONTEXT.md` |
| Parent Workbook ID | 80 | `_CONTEXT.md` |
| Package Name | Inlet Compressors | `_CONTEXT.md` |
| Package Tag (vendor handoff) | 26020-02-PT-12-001 — Inlet Compressors | `PACKAGE_REGISTER.csv` row PKG-080, `ArtifactName` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| WBS | 02 | `PACKAGE_REGISTER.csv` row PKG-080 |
| Responsible Party (deliverable owner) | EPC Integrator | `_CONTEXT.md` |
| Package Vendor Scope | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` row PKG-080 |
| EPC Integrator Scope | Integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) | `PACKAGE_REGISTER.csv` row PKG-080 |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; PROJECT_DECOMP objective mapping (ASSUMPTION — package-grouped) |
| Covers Scope Items | SOW-0119, SOW-0120, SOW-0121, SOW-0122 | `_CONTEXT.md` |

## Attributes — Process and Mechanical Basis

| Attribute | Value | Source |
|---|---|---|
| Service | Sour inlet gas compression (approximately 0.296 mol% H2S) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 "Compression Design Conditions" |
| Number of packages | 2 (parallel, identical) | DBM SEC-05 "Inlet Compression Overview"; PACKAGE_REGISTER.csv row PKG-080 ("two identical parallel sour inlet gas reciprocating compressor packages") |
| Spare philosophy | 2 x 50 percent, no installed spare | DBM SEC-05 Compressor Item table |
| Per-package capacity | 40 MMSCFD | DBM SEC-05 Compressor Item table |
| Total facility compression basis | 80 MMSCFD | DBM SEC-05 Inlet Compression Overview |
| Compressor type | Two-stage separable reciprocating | DBM SEC-05 Compressor Item table |
| Preliminary model | Ariel KBC/6 (TBC) | DBM SEC-05 Compressor Item table |
| Cylinder arrangement | Three first-stage cylinders and three second-stage cylinders | DBM SEC-05 Compressor Item table |
| Driver type | Electric motor | DBM SEC-05 Compressor Item table |
| Driver rating (each) | 5,200 hp / 3,878 kW | DBM SEC-05 "Electric Driver and Starting Basis" |
| Motor electrical | 4,000 V, three-phase, 60 Hz | DBM SEC-05 |
| Motor enclosure | TEFC or WPII; non-sparking bidirectional fans | DBM SEC-05 |
| Insulation / temperature rise | Class F insulation, Class B rise | DBM SEC-05 |
| Speed / poles | Approximately 891 rpm, 8-pole | DBM SEC-05 |
| Duty | Continuous, inverter-duty | DBM SEC-05 |
| Starter | Starting VFD (per SCA-001 VE #34; soft starts not used) | DBM SEC-05; DBM SEC-09 (E&I) |
| Motor tags | KM-2150, KM-2250 | DBM SEC-05 / SEC-08 prime-mover table |
| Modularization | Shop-assembled; disassembled into three pieces for transport; field-installed in self-framing buildings | DBM SEC-05 Inlet Compression Overview |
| Standards compliance (motors) | NEMA MG1 | DBM SEC-05 |
| H2S service material requirements | NACE/MR-class sour service expected (location TBD — heading 33 not accessible) | ASSUMPTION based on sour service composition (DBM SEC-05); detailed metallurgy basis location TBD |

## Conditions — Process Operating Envelope

| Compression Point | Low | Normal | Design | Max / MAWP | Source |
|---|---:|---:|---:|---:|---|
| First-stage suction pressure | 125 psig | 165 psig | 165 psig | 653 psig MAWP | DBM SEC-05 "Compression Design Conditions" |
| First-stage discharge pressure | TBC | 380 psig | 380 psig | 653 psig MAWP | DBM SEC-05 |
| Second-stage suction pressure | TBC | 375 psig | 375 psig | 653 psig MAWP | DBM SEC-05 |
| Second-stage discharge pressure | TBC | 800 psig | 800 psig | 1,350 psig MAWP | DBM SEC-05 |

| Temperature Item | Value | Source |
|---|---|---|
| First-stage suction temperature, low | 4 deg C | DBM SEC-05 |
| First-stage suction temperature, high | 15 deg C | DBM SEC-05 |
| First-stage suction temperature, maximum | 48 deg C | DBM SEC-05 |
| Second-stage suction temperatures | TBC | DBM SEC-05 |
| Aftercooler outlet temperature (each stage) | 43.3 deg C | DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge" |

| Pressure Drop Item | Value | Source |
|---|---|---|
| Aerial cooler simulated dP, stage 1 | 20.7 kPad (final TBC) | DBM SEC-05 |
| Aerial cooler simulated dP, stage 2 | 34.5 kPad (final TBC) | DBM SEC-05 |

Discharge pressure is fixed at 800 psig under the current supersession basis; the prior 650 to 800 psig range is superseded. (DBM SEC-05)

## Construction — Package Equipment Scope

| Item | Detail | Source |
|---|---|---|
| Suction scrubbers, stage 1 | Two-phase cyclonic separator (one per package) | DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge" |
| Suction scrubbers, stage 2 | Vertical-flow mesh/vane separator (one per package) | DBM SEC-05 |
| Scrubber design liquid SG | 0.68 | DBM SEC-05 |
| Aerial coolers | Per package; 10 percent excess surface area; vendor handles warm-air recirculation, automated louvers, heating/plenum heat | DBM SEC-05 |
| Recycle control valves | Dedicated per package; expected fail-open (final failure action TBC) | DBM SEC-05 |
| Start-up purge | Sweet-gas purge from fuel-gas system | DBM SEC-05 |
| Packing drains/vents | Common seal pot; vapour to VRU suction; vacuum pump interface per package design | DBM SEC-05 |
| Modular building | Self-framing package building (one per compressor) | DBM SEC-05; SEC-08 "Buildings/Interfaces" |
| Foundations | Equipment-specific foundation and anchorage design required (geotechnical, equipment loads, snow/wind/seismic, frost, vibration, settlement, maintenance access) | DBM SEC-08 |

### Applicable Interface Types (carried as evidence per `_CONTEXT.md` Notes)

From PACKAGE_REGISTER.csv row PKG-080:

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

Source-grounded interface anchors (DBM SEC-05, SEC-09):
- 4.16 kV inlet/overheads compressor electrical building (MCC-8200; field-fused contactors; motor protection relays; EtherNet to plant PLC) — DBM SEC-09.
- Recycle/start-up sweet-gas tie from fuel-gas system — DBM SEC-05.
- Packing drains/vents to VRU suction; vacuum pump interface — DBM SEC-05.
- Downstream TEG dehydration package (1 x 100 percent) treats compressed sour gas before export to 04-25 — DBM SEC-05.
- Drive-gas recycle from aftercoolers returns to inlet separators; drive-gas pressure set above 04-25 stabilizer flash feed separator pressure — DBM SEC-04.

## References

- Authoritative: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-05; supporting SEC-04, SEC-08, SEC-09)
- Decomposition row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` PKG-080
- Deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` DEL-080-02
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable)
- TBD / inaccessible: `26020-Package_Requirements.docx` package heading 33; `Bid Docs/Budgetary/brief.md`; `24292-02-PT-ENR-12-201_Compressors_R2.pdf` (location TBD)
