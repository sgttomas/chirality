# Specification — Vendor Engineered Equipment Package (DEL-073-04)

> Normative requirements for the Package Vendor's engineering, design, fabrication/supply, and physical delivery of the PKG-073 Amine Treating Unit, derived from the EPC package Scope of Work (DEL-073-01), the EPC Package Datasheet (DEL-073-02), and the locally accessible Design Basis Memorandum (DBM-Deepcut SEC-06). Source-anchored values cite the DBM; values from `26020-Package_Requirements.docx` heading 27 are marked `location TBD`.

## Scope

### In scope
- Detailed engineering and design of the Amine Treating Unit (ATU) package serving the 04-25 Deep Cut Gas Plant.
- Fabrication, supply, modularization, shop assembly, and shipping of:
  - Module 520 amine inlet coalescers and amine absorbers (interface with HP sweetening/TEG dehy module);
  - Module 530 amine regeneration module/building (flash drum, exchangers, filters, reboiler, regenerator, surge tank, pumps, make-up storage, slop tank).
- Package design basis documentation, datasheets, and vendor turnover documents required to support the EPC integration review (DEL-073-06) and the Vendor Document Turnover Package (DEL-073-05).

### Out of scope
- Downstream TEG dehydration (handled within Module 520 but not part of the amine package per the Module/area split in DBM SEC-06 L1131; **boundary confirmation TBD** against `26020-Package_Requirements.docx` h.27).
- Acid gas compression and injection (separate acid gas injection compressor packages — DBM SEC-05 L878).
- Stabilizer overheads compressor.
- Plant utilities (LP fuel gas supply, heat medium generation, electrical distribution) at boundaries upstream of the package tie-in flanges.

## Requirements

### R-1 Process performance
| ID | Requirement | Source |
|---|---|---|
| R-1.1 | Sweet gas H2S at amine absorber outlet shall be ≤4 ppmv at design conditions. | DBM SEC-06 L1156 |
| R-1.2 | Solvent selection shall be MDEA-based with selectivity that permits CO2 slip while keeping sales-gas CO2 ≤2 mol%. H2S removal priority over CO2 slip. | DBM SEC-06 L1158 |
| R-1.3 | Process design shall not take credit for mercaptan recovery (0%). | DBM SEC-06 L1157 |
| R-1.4 | The package shall accommodate raw inlet flow design points of 307.5 MMSCFD (summer) and 312.0 MMSCFD (winter), with low-end 300 MMSCFD. | DBM SEC-06 L1150–L1151 |
| R-1.5 | Inlet temperature design envelope: 36.8 °C winter / 44.1 °C summer (at amine inlet). | DBM SEC-06 L1152 |
| R-1.6 | Operating pressure: normal/design 7722 kPag. Low operating pressure TBD; vendor shall request resolution before final design. | DBM SEC-06 L1155 |
| R-1.7 | Maintain inlet ≈6 °C above expected hydrate T and ≈6 °C above expected HC dewpoint; no methanol injection in amine area. | DBM SEC-06 L1153–L1154 |

### R-2 Equipment configuration
| ID | Requirement | Source |
|---|---|---|
| R-2.1 | 2 × 100% amine inlet gas filter/coalescers upstream of absorbers. | DBM SEC-06 L1165 |
| R-2.2 | 2 × 50% upflow amine absorbers with top demister to reduce amine/water entrainment. | DBM SEC-06 L1166 |
| R-2.3 | Amine flash tank at ~60 psig with HC skim box and manual HC drain to amine slop tank. Flash gas routed to SOC first-stage suction (interface). | DBM SEC-06 L1168, L1143 |
| R-2.4 | Full-flow rich-amine particle filtration nominal 5 µm; 25% lean-amine slipstream through activated carbon/charcoal + 5 µm filtration; LP fuel-gas purge before opening sour service. | DBM SEC-06 L1170 |
| R-2.5 | 2 × 50% plate-and-frame lean/rich amine exchangers sized to support amine-circulation turndown. | DBM SEC-06 L1171 |
| R-2.6 | Lean amine cooler outlet 15 °F above absorber inlet or 110 °F (whichever lower); automated warm-air recirculation; plenum heat. | DBM SEC-06 L1172 |
| R-2.7 | Amine surge tank: ~30 min surge at design circulation; insulated; LP fuel-gas blanket; internal coating; heater; truck-out; secondary containment. | DBM SEC-06 L1173 |
| R-2.8 | 2 × 115% single-stage vertical inline booster pumps with single mechanical seals. | DBM SEC-06 L1174 |
| R-2.9 | 3 × 57.5% multi-stage horizontal centrifugal charge pumps (API-610 axial-split casing currently considered; final model TBC). | DBM SEC-06 L1175 |
| R-2.10 | Amine regenerator with 20 actual trays (18 for stripping), two water-wash stages, ≤70% jet/downcomer flood. | DBM SEC-06 L1176 |
| R-2.11 | BKU kettle reboiler on hot oil; 350 °F supply via mixing valves; skin ≤350 °F to limit amine degradation. | DBM SEC-06 L1177 |
| R-2.12 | Reflux condenser/accumulator: partial condenser to 110 °F; demister; HC skim; reflux-water purge to produced-water storage; auto pressure control to LP flare; dilution-gas review for high-CO2 acid gas. | DBM SEC-06 L1178 |
| R-2.13 | 2 × 115% single-stage vertical inline amine reflux pumps with single mechanical seals. | DBM SEC-06 L1179 |

### R-3 Mechanical / site / environmental
| ID | Requirement | Source |
|---|---|---|
| R-3.1 | Equipment shall be suitable for site design ambient envelope −40 °C to +35 °C, including winterization, heat tracing, insulation, package buildings, and instrumentation rated for the envelope. | DBM SEC-02 L198; SEC-02 §"General Layout Basis" |
| R-3.2 | Module 530 regeneration equipment shall be provided as a modular module/building suitable for shop assembly and field erection. | DBM SEC-06 L1132 (Module/area basis) |
| R-3.3 | Layout shall respect minimum spacing criteria for pressurized, atmospheric, and electrical equipment areas. | DBM SEC-02 §2.5 (L241–L308) |

### R-4 Interfaces (tie-points the vendor must design to)
| ID | Interface | Source |
|---|---|---|
| R-4.1 | Inlet HP sour gas from first-stage inlet-service compressor aftercooler outlet (upstream of amine inlet coalescers). | DBM SEC-06 L1141 |
| R-4.2 | Sweet gas outlet routed to TEG inlet cooler / TEG inlet filter/coalescer (downstream Module 520 chain). | DBM SEC-06 L1141, L1119 |
| R-4.3 | Amine flash gas to SOC first-stage suction header (pressure-controlled). | DBM SEC-06 L1143 |
| R-4.4 | Acid gas overheads to acid-gas compressor first-stage suction scrubber. | DBM SEC-06 L1143, L1371 |
| R-4.5 | Amine surge tank vapors to VRU header; LP flare for regenerator overpressure control. | DBM SEC-06 L1373, L1359 |
| R-4.6 | Heat medium supply: amine reboiler 350 °F. | DBM SEC-06 L1375 |
| R-4.7 | LP fuel gas: surge tank blanket, regenerator blanket, sour-filter purge. | DBM SEC-06 L1374, L1170, L1359 |
| R-4.8 | Drains: HC skim manual drain to amine slop tank; reflux-water purge to produced-water storage; spent/waste amine to amine slop tank for off-site disposal/reclamation. | DBM SEC-03 L532; SEC-06 L1143, L1178 |

## Standards

| Standard | Application | Location |
|---|---|---|
| API-610 | Centrifugal pumps (amine charge pumps; absorber bottoms-style services) | DBM SEC-06 L1175 — location TBD (clause not stated) |
| ASME B&PV / Section VIII | Pressure-containing equipment (absorbers, flash drum, surge tank, regenerator, reboiler) | ASSUMPTION — standard Canadian/EPC practice for this duty; specific edition `location TBD` against `26020-Package_Requirements.docx` h.27 |
| BC CRN registration | Pressure equipment registration in British Columbia | ASSUMPTION based on facility location (04-25 BC); `location TBD` |
| NEMA MG-1 | Electric motors (analogous to upstream/downstream basis) | DBM SEC-04 L828 (analogous); `location TBD` for amine-package motors |
| Vendor/EPC site standards | Heat tracing, winterization, electrical area classification | `location TBD` against `26020-Package_Requirements.docx` h.27 |

## Verification

| Requirement(s) | Verification approach |
|---|---|
| R-1.1, R-1.2, R-1.3 | Vendor process simulation of full operating envelope; vendor-provided performance guarantee; commissioning sweet-gas H2S measurement at absorber outlet. |
| R-1.4, R-1.5, R-1.6, R-1.7 | Heat-and-material balance review against DBM SEC-06 envelope; vendor confirmation of low-pressure operating case (R-1.6 — TBD). |
| R-2.1 – R-2.13 | Equipment datasheet review against requirement table; vendor mechanical drawings; FAT/ITP for pressure equipment; shop hydrotest records. |
| R-3.1 – R-3.3 | Mechanical/material spec review; cold-climate review; module GA review; site/layout interface review with EPC Integrator. |
| R-4.1 – R-4.8 | Interface tie-point review against EPC Package Datasheet (DEL-073-02); P&ID alignment with upstream/downstream packages. |

## Documentation (Required Vendor Documents)

Per `_CONTEXT.md` anticipated artifacts and the Vendor Document Turnover Package scope (DEL-073-05), the vendor package shall deliver:

- Vendor process design basis and heat-and-material balances
- Vendor package datasheet set (per major equipment item in R-2)
- Mechanical equipment drawings and module general arrangements
- P&IDs covering the package boundary
- Electrical and instrumentation drawings and lists
- Cause-and-effect / safeguarding documentation for amine controls (DBM SEC-06 L1359)
- FAT records, hydrotest reports, NDE records
- Operations & maintenance manuals
- Spare parts and consumables lists (including activated carbon, anti-foam, anti-corrosion additives)
- Turnover documentation per DEL-073-05

`location TBD` — specific vendor document index against `26020-Package_Requirements.docx` h.27.
