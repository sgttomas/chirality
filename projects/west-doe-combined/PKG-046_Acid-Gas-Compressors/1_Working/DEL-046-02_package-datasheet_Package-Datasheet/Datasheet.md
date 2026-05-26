# Datasheet — PKG-046 Acid Gas Compressors (Package Datasheet)

> Deliverable: `DEL-046-02_package-datasheet` — Package Datasheet
> ParentPackageID: `PKG-046` (Acid Gas Compressors)
> Discipline: Mechanical | Type: EPC Package Datasheet | ResponsibleParty: EPC Integrator
> Source authority: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-05 (Compression and Acid Gas Handling Basis), in particular "Acid Gas Injection Compression Basis" and "Acid Gas Disposal Well Interface".

## Identification

| Field | Value | Source |
|---|---|---|
| Package ID | PKG-046 | `_CONTEXT.md` |
| Package Name | Acid Gas Compressors | `_CONTEXT.md` |
| Parent Workbook ID | 46 | `_CONTEXT.md` |
| Service | Acid gas (H2S + CO2, water-saturated) injection compression from amine regenerator to existing shared disposal well/reservoir | DBM-Deepcut SEC-05 "Acid Gas Injection Compression Basis" |
| Facility | West Doe 04-25 Deepcut expansion | DBM-Deepcut SEC-05 |
| Configuration (operating basis) | Two 100% acid gas compressor packages plus one installed spare; potential 3 x 50% arrangement remains TBD | DBM-Deepcut SEC-05 "Acid Gas Compressor Design Conditions" table |
| Compressor type | Ariel KBT/6, five-stage separable reciprocating compressor (conflicting KBK/6 reference) | DBM-Deepcut SEC-05 "Acid Gas Compressor Design Conditions" — see Conflict Table in Guidance |
| Number of stages | 5 | DBM-Deepcut SEC-05 ("the compressor is designed with five stages of compression") |
| Capacity control | Driver speed control plus high-pressure and low-pressure recycle; adjustable volume pockets excluded to reduce acid-gas leakage points | DBM-Deepcut SEC-05 |

## Attributes (Design)

### Flow & Composition

| Parameter | Value | Units | Source |
|---|---|---|---|
| Design total flow | 4.209 | MMSCFD | DBM-Deepcut SEC-05 Acid Gas Compressor Design Conditions |
| Design unit flow | 4.5 (preliminary; target 1.10 capacity factor at design) | MMSCFD | DBM-Deepcut SEC-05 |
| Start-up total flow | 0.603 | MMSCFD | DBM-Deepcut SEC-05 |
| Start-up unit flow | 1.5 | MMSCFD | DBM-Deepcut SEC-05 |
| Dry-out case flow | TBC | — | DBM-Deepcut SEC-05 |
| Minimum methane content (design) | 0.5 | mol% | DBM-Deepcut SEC-05 |
| Start-up methane content (typical) | ~1.4 | mol% C1 | DBM-Deepcut SEC-05 |
| Water status at suction | Water-saturated from amine unit | — | DBM-Deepcut SEC-05 |

Design / Start-up / High-CO2 acid gas composition (mol%):

| Compound | Design | Start-up | High CO2 |
|---|---:|---:|---:|
| Carbon dioxide | 21.28662 | 41.50620 | 72.94712 |
| Hydrogen sulfide | 72.94712 | 49.67490 | 21.28662 |
| Methane | 0.19560 | 1.88949 | 0.19560 |
| Water | 5.47959 | 5.47780 | 5.47959 |
| Ethane | 0.05104 | 0.66463 | 0.05104 |
| Propane | 0.01200 | 0.18432 | 0.01200 |
| Methyl mercaptan | 0.01355 | 0.01361 | 0.01355 |
| Ethyl mercaptan | 0.00878 | 0.01495 | 0.00878 |

Source: DBM-Deepcut SEC-05 "Acid Gas Composition Basis" table.

### Pressures & Temperatures

| Parameter | Value | Source |
|---|---|---|
| 1st-stage suction pressure | 3.8 psig low; 7 psig normal (expander mode and J-T mode) | DBM-Deepcut SEC-05 |
| 5th-stage discharge pressure | 1,200 psig normal (expander and J-T mode); low-pressure case TBC; 1,500 psig design-discharge reference unresolved | DBM-Deepcut SEC-05 — see Conflict Table |
| Aftercooler outlet temperature (stages 1-4) | 110 deg F (43.33 deg C) | DBM-Deepcut SEC-05 |
| Aftercooler outlet temperature (stage 5) | 150 deg F (65.56 deg C) | DBM-Deepcut SEC-05 |
| Injection pipeline temperature setpoint | Aftercooler outlet to injection pipeline controlled to 8.3 deg C above maximum ambient at all times | DBM-Deepcut SEC-05 "Acid Gas Disposal Well Interface" |

MAWP and design temperature by system point (per stage):

| System point | Minimum MAWP | Design temperature |
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

Source: DBM-Deepcut SEC-05 "Acid gas compressor MAWP and design-temperature basis" table. NOTE: stated discharge-MAWP values for stages 1 and 2 (197 psig) are lower than the corresponding suction MAWPs (205 psig); see Guidance Conflict Table.

### Driver

| Parameter | Value | Source |
|---|---|---|
| Driver type | Induction motor on VFD | DBM-Deepcut SEC-05 |
| Rated power | 969 kW (1,300 hp), with approximately 10% excess power included | DBM-Deepcut SEC-05 |
| Pole count / speed | 8-pole, 900 rpm at full speed on VFD | DBM-Deepcut SEC-05 |
| Turndown | Minimum 3:1 speed turndown by inverter | DBM-Deepcut SEC-05 |

### Stage-Discharge Water Content (basis for dehydration)

| Compressor discharge stage | Water content (lbm/MMSCFD) |
|---|---:|
| Stage 1 | 2,805 |
| Stage 2 | 1,536 |
| Stage 3 | 769.5 |
| Stage 4 | 398 |
| Final | 199.5 |

Acid gas dehydration by recycle to 35-60 lb H2O/MMSCF is to be considered if required by the disposal system. Source: DBM-Deepcut SEC-05.

## Conditions (Site / Service)

| Item | Value | Source |
|---|---|---|
| Service category | Sour, wet, acid-gas duty (H2S majority in design case) | DBM-Deepcut SEC-05 |
| Inlet origin | Amine regenerator (reflux accumulator) | DBM-Deepcut SEC-05 |
| Outlet destination | Acid gas injection pipeline to existing shared disposal well (basis: existing 02-25 plant disposal well) | DBM-Deepcut SEC-05 "Acid Gas Disposal Well Interface" |
| Injection pipeline NPS (assumption) | 3 in. NPS per Tourmaline; final sizing TBC in detailed engineering | DBM-Deepcut SEC-05 |
| Mercaptan condensation at low temperature | May require three-phase separation; can affect dehydration, recycle, and efficiency | DBM-Deepcut SEC-05 |
| Lubricant disposition | Lubrication oil injected into compressor valves/cylinders is injected into the disposal well | DBM-Deepcut SEC-05 |
| Sweet gas purge | Manual sweet-gas purge connection at 1st-stage suction downstream of inlet shutdown valve to remove H2S before maintenance | DBM-Deepcut SEC-05 |

## Construction

| Item | Value | Source |
|---|---|---|
| Compressor frame | Ariel KBT/6 (conflicting KBK/6 reference) | DBM-Deepcut SEC-05 — Conflict Table |
| Stage suction scrubbers | Two-phase scrubbers upstream of each stage; horizontal double-hook vane demisters acceptable; K-factor max 0.55 Imperial; inlet liquid density 1.00 SG assumed | DBM-Deepcut SEC-05 |
| Scrubber liquid handling | All scrubbers PID level control; stages 2-5 liquids cascade to prior-stage scrubbers; stage 1 liquid pumped to produced water tank by 0.75 hp motor-driven Hydra-Cell pump | DBM-Deepcut SEC-05 |
| Aftercooling | Common forced-draft motor-driven air cooler for each stage discharge; actuated louver temperature control; warm-air recirculation on low discharge temperature; heat-medium heating for winter freeze protection | DBM-Deepcut SEC-05 |
| Blowdown | Single fail-open blowdown valve on final discharge downstream of aftercooler | DBM-Deepcut SEC-05 |
| Recycle (high-pressure) | Discharge to 4th-stage suction upstream of 4th-stage suction scrubber; fail open; sized for 100% capacity at min driver speed, max suction pressure, min injection pipeline pressure | DBM-Deepcut SEC-05 |
| Recycle (low-pressure) | 4th-stage suction to 1st-stage suction upstream of 1st-stage suction scrubber; fail open | DBM-Deepcut SEC-05 |
| Recycle isolation | Manual isolation of recycle valves excluded (minimize leakage points) | DBM-Deepcut SEC-05 |
| Volume pockets | Adjustable volume pockets excluded from cylinders (reduce acid-gas leakage points) | DBM-Deepcut SEC-05 |
| Packing drains / vents | Collected to common seal pot; seal-pot vapour routed to VRU suction header; liquids removed by local truck-out connection | DBM-Deepcut SEC-05 |
| Disposal metering | High-pressure Coriolis mass meter downstream of compression; low-pressure flare-route acid gas metered separately at PCV; main LP acid gas line to compressor not metered | DBM-Deepcut SEC-05 |
| Composition monitoring | Continuous acid gas composition measurement for sulfur and CO2 balance reporting | DBM-Deepcut SEC-05 |
| Sequencing automation | Isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, shutdown all automated | DBM-Deepcut SEC-05 |

## Interfaces (Package Boundary)

| Interface | Counterparty (TBD vs decomposition INTERFACE_REGISTER.csv at SourcePath location TBD) | Source |
|---|---|---|
| Inlet acid gas from amine regenerator reflux accumulator | Amine regeneration package | DBM-Deepcut SEC-05 |
| Outlet to acid gas injection pipeline / disposal well (existing) | Shared 02-25 disposal well / NorthRiver Midstream | DBM-Deepcut SEC-01 and SEC-05 |
| LP flare routing via amine reflux accumulator BDV/PCV | LP flare header | DBM-Deepcut SEC-05 |
| VRU suction header (packing/seal-pot vapour) | Vapour Recovery Unit | DBM-Deepcut SEC-05 |
| Produced water tank (stage 1 scrubber liquid) | Produced water system | DBM-Deepcut SEC-05 |
| Heat medium (cooler freeze protection) | Heat medium utility | DBM-Deepcut SEC-05 |
| Electrical (969 kW VFD-fed induction motor) | Plant electrical / VFD | DBM-Deepcut SEC-05 |
| Instrument air / control system | Plant automation | DBM-Deepcut SEC-05 (implied for automated sequencing) — ASSUMPTION |
| Interface register cross-reference (PKG-046 rows) | DECOMPOSITION_REF INTERFACE_REGISTER.csv | location TBD (not yet sliced into deliverable) |

## References

- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-05 "Compression and Acid Gas Handling Basis", subsections "Acid Gas Injection Compression Basis" and "Acid Gas Disposal Well Interface".
- `_CONTEXT.md` for identity, parent package, discipline, and scope items.
- `_REFERENCES.md` for authoritative source listing.
- Decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv.
- Source listed in `_REFERENCES.md` but not locally accessible as text in this pass: `26020-Package_Requirements.docx` (binary .docx); `26020-Packages_Interfaces_4_export.xlsx` (binary .xlsx) — location TBD until extracted.

## Notes

- ASSUMPTION (PACKAGE_HEURISTIC): Objectives OBJ-001, OBJ-003 through OBJ-010 are treated as directionally relevant context per `_CONTEXT.md`; not treated as hard requirements pending human confirmation.
- ASSUMPTION: 26020-Package_Requirements.docx clauses are treated as directionally applicable; clause-level requirements derived from that source are deferred until text is extracted.
