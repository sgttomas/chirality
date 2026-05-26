# Datasheet: DEL-046-04 — Vendor Engineered Equipment Package (Acid Gas Compressors)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-046-04_vendor-engineered-equipment-package | _CONTEXT.md |
| Name | Vendor Engineered Equipment Package | _CONTEXT.md |
| ParentPackageID | PKG-046 | _CONTEXT.md |
| Package Name | Acid Gas Compressors | PACKAGE_REGISTER.csv row PKG-046 |
| Tag Basis | 26020-01-PT-12-001 — Acid Gas Compressor | PACKAGE_REGISTER.csv (`Tag` column) |
| Discipline | Mechanical | _CONTEXT.md |
| Type | Vendor Package Production Unit | _CONTEXT.md |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | _CONTEXT.md |
| Service | Acid Gas Injection (AGI) — H2S/CO2 from amine treating compressed for injection/disposal | PACKAGE_REGISTER.csv row PKG-046; DBM-Deepcut §AGI Compression Basis |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Configuration | Two (2) x 100% acid gas compressor packages plus one (1) spare compressor; ASSUMPTION: aligns with PACKAGE_REGISTER "two (2x) identical induction motor-driven separable reciprocating compressor packages; each designed for 100% of acid gas capacity" | DBM-Deepcut SEC-05 §Acid Gas Compressor Design Conditions; PACKAGE_REGISTER row PKG-046 |
| Compressor type | Separable reciprocating, five-stage; Ariel KBT/6 detailed basis (KBK/6 reference conflict — see Guidance.md Conflict Table) | DBM-Deepcut SEC-05 |
| Driver | Induction motor, 8-pole, 969 kW (1,300 hp), ~10% excess power, on VFD | DBM-Deepcut SEC-05 |
| Driver speed/turndown | 900 rpm at full speed on VFD; minimum 3:1 inverter turndown | DBM-Deepcut SEC-05 |
| Capacity control | Driver speed control + recycle control; adjustable volume pockets excluded to reduce leak points | DBM-Deepcut SEC-05 |
| Design total flow | 4.209 MMSCFD | DBM-Deepcut SEC-05 |
| Design unit flow | 4.5 MMSCFD preliminary; target 1.10 capacity at design | DBM-Deepcut SEC-05 |
| Start-up total flow | 0.603 MMSCFD | DBM-Deepcut SEC-05 |
| Start-up unit flow | 1.5 MMSCFD | DBM-Deepcut SEC-05 |
| 1st stage suction pressure | 3.8 psig low; 7 psig normal/expander/J-T modes | DBM-Deepcut SEC-05 |
| 5th stage discharge pressure | 1,200 psig normal (1,500 psig design-discharge reference unresolved — see Conflict Table) | DBM-Deepcut SEC-05 |
| Aftercooler outlet (stages 1-4) | 110 deg F (43.33 deg C) | DBM-Deepcut SEC-05 |
| Aftercooler outlet (stage 5) | 150 deg F (65.56 deg C); to injection pipeline controlled to 8.3 deg C above max ambient | DBM-Deepcut SEC-05 |
| Recycle | HP recycle: final discharge -> 4th-stage suction (upstream of scrubber). LP recycle: 4th-stage suction -> 1st-stage suction (upstream of scrubber). Both fail open; sized for 100% capacity at minimum driver speed | DBM-Deepcut SEC-05 |
| Blowdown valve | Single fail-open valve on final discharge downstream of aftercooler | DBM-Deepcut SEC-05 |
| Suction scrubbers | Two-phase upstream of each stage; horizontal double-hook vane demisters acceptable; max K = 0.55 Imperial; assumed inlet liquid SG = 1.00; stage-1 liquid pumped to produced water tank by 0.75 hp Hydra-Cell; other stages cascade to prior-stage scrubber | DBM-Deepcut SEC-05 |
| Packing drains/vents | Collected to common seal pot; vapour to VRU suction header; liquids removed by local truck-out | DBM-Deepcut SEC-05 |
| Sweet-gas purge | Manual sweet-gas purge connection at 1st-stage suction downstream of inlet shutdown valve for H2S removal before maintenance | DBM-Deepcut SEC-05 |
| Disposal metering | High-pressure Coriolis mass meter downstream of compression; continuous composition measurement for sulfur and CO2 balance | DBM-Deepcut SEC-05 |
| Lubrication injection | Lube oil injected into compressor valves/cylinders is injected into the disposal well (consumable) | DBM-Deepcut SEC-05 |

## Conditions

### Acid Gas Composition Basis (mol%)
| Compound | Design | Start-up | High CO2 |
|---|---:|---:|---:|
| CO2 | 21.28662 | 41.50620 | 72.94712 |
| H2S | 72.94712 | 49.67490 | 21.28662 |
| Methane | 0.19560 | 1.88949 | 0.19560 |
| Water | 5.47959 | 5.47780 | 5.47959 |
| Ethane | 0.05104 | 0.66463 | 0.05104 |
| Propane | 0.01200 | 0.18432 | 0.01200 |
| Methyl mercaptan | 0.01355 | 0.01361 | 0.01355 |
| Ethyl mercaptan | 0.00878 | 0.01495 | 0.00878 |

Source: DBM-Deepcut SEC-05 §Acid Gas Composition Basis.

Minimum methane content for compressor design = 0.5 mol%; turndown cases may produce ~1.4 mol% C1. Acid gas is water-saturated from the amine unit. Dehydration by recycle to 35-60 lb H2O/MMSCF to be considered if required by the disposal system. (DBM-Deepcut SEC-05)

### MAWP / Design Temperature (per stage)
| System point | Min MAWP | Design temperature |
|---|---:|---:|
| 1st stage suction | 205 psig (1,400 kPag) | 300 deg F (149 deg C) |
| 1st stage discharge | 197 psig (1,344 kPag) | 350 deg F (177 deg C) |
| 2nd stage suction | 205 psig (1,400 kPag) | 300 deg F (149 deg C) |
| 2nd stage discharge | 197 psig (1,344 kPag) | 350 deg F (177 deg C) |
| 3rd stage suction | 205 psig (1,400 kPag) | 300 deg F (149 deg C) |
| 3rd stage discharge | 517 psig (3,565 kPag) | 350 deg F (177 deg C) |
| 4th stage suction | 540 psig (3,709 kPag) | 300 deg F (149 deg C) |
| 4th stage discharge | 1,034 psig (7,129 kPag) | 350 deg F (177 deg C) |
| 5th stage suction | 1,075 psig (7,398 kPag) | 300 deg F (149 deg C) |
| 5th stage discharge | 1,551 psig (10,694 kPag) | 350 deg F (177 deg C) |

Source: DBM-Deepcut SEC-05.

### Water Content Across Stages (saturated inlet)
| Discharge stage | Water content (lbm/MMSCFD) |
|---|---:|
| Stage 1 | 2,805 |
| Stage 2 | 1,536 |
| Stage 3 | 769.5 |
| Stage 4 | 398 |
| Final | 199.5 |

Source: DBM-Deepcut §Acid Gas Disposal Well Interface.

### Site/Ambient Envelope
- Ambient temperature range governing equipment: -40 deg C to +35 deg C. (DBM-Comp_and_Liquids SEC site basis; applied facility-wide unless a package-specific basis is stricter.)
- Aftercooler discharge to injection pipeline: 8.3 deg C above maximum ambient at all times. (DBM-Deepcut SEC-05)

## Construction

| Item | Basis | Source |
|---|---|---|
| Package modularization | Shop-assembled package design; field-installed integration TBD by EPC Integrator | ASSUMPTION (consistent with PKG-046 SoW narrative; not explicitly stated in DBM-Deepcut for AGI service) |
| Air cooler | Common forced-draft motor-driven air cooler per stage discharge; actuated louver temperature control; automatic warm-air recirculation on low discharge temperature; heat-medium heating for freeze protection | DBM-Deepcut SEC-05 §Controls and Protection Basis |
| Materials of construction | Sour service per NACE MR0175 / ISO 15156 (ASSUMPTION: standard practice for H2S concentrations of design basis; specific code edition TBD by vendor) | ASSUMPTION |
| Packing seal recovery | Common seal pot, vapour -> VRU suction header, liquids truck-out | DBM-Deepcut SEC-05 |
| Adjustable volume pockets | Excluded | DBM-Deepcut SEC-05 |
| Recycle valve manual isolation | Excluded (minimize leakage points) | DBM-Deepcut SEC-05 |
| Methanol injection provisions | TBD (DBM lists AGI compressor package as a methanol injection point with capacities TBC) | DBM-Deepcut §Hydrate-Inhibition / Operability table |
| Electrical area classification | TBD (vendor scope; reflect facility ACAD) | TBD |
| Noise limits | TBD | TBD |

## References

- _CONTEXT.md (deliverable identity)
- _REFERENCES.md (authoritative basis pointers)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv (row PKG-046)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv (row DEL-046-04)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md (SEC-05 Compression and Acid Gas Handling Basis; §Acid Gas Injection Compression Basis; §Acid Gas Disposal Well Interface; §Controls and Protection Basis)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (acid gas routing context; site ambient envelope)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx (binary; location TBD — not text-readable in this drafting session)
- Bid Docs/Budgetary/26020-01-PT-RFQ-12-001_Acid Gas Compressor.docx (referenced by PACKAGE_REGISTER; not located locally — location TBD)
