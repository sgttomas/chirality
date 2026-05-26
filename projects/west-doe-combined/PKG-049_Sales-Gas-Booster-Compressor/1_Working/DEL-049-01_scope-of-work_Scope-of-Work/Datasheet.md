# Datasheet — DEL-049-01 Scope of Work (Sales Gas Booster Compressor)

> Descriptive datasheet for the EPC Integrator Scope of Work covering PKG-049 Sales Gas Booster Compressor package.
> Pass 1/Pass 2 draft; values are source-grounded where the locally accessible DBM supports them. Unsupported values are `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-049-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package | `PKG-049` Sales Gas Booster Compressor | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Facility | West Doe Deepcut Expansion (04-25 Deep Cut Gas Plant) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-05 |
| Decomposition Basis | GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP snapshot | `_REFERENCES.md` |
| Covers Scope Items | SOW-0169, SOW-0170, SOW-0171, SOW-0172 | `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouping heuristic) | `_CONTEXT.md`; SKILL.md Step 1 §3 |

## Attributes (Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Package function | Single-package sweet-gas reciprocating compressor that boosts treated sales gas from sales compressor discharge to TC sales gas pipeline delivery pressure | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-05 "Sales Gas Booster Compressor Basis" |
| Configuration | One x 100% sweet sales gas booster compressor; no installed spare | DBM-Deepcut §SEC-05 Table "Compression Configuration"; §SEC-05 Sales Gas Booster Design Conditions table |
| Compression stages | One stage | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Frame | Ariel KBK/4 (larger high-efficiency cylinder on two-throw to be evaluated in detailed engineering) | DBM-Deepcut §SEC-05 "Sales Gas Booster Compressor Basis" |
| Driver | Electric induction motor, 6,700 hp, 4,000 V, 3-phase, 60 Hz; NEMA MG 1; Class F insulation, Class B rise; non-sparking bidirectional cooling fans; TEFC or WPII enclosure; DOL with soft-start; no driver speed turndown | DBM-Deepcut §SEC-05 "Sales Gas Booster Compressor Basis" |
| Tagged Equipment List | TBD — equipment tag numbers not present in locally accessible DBM source slice | source not local |

## Conditions (Design Basis)

| Parameter | Value | Source |
|---|---|---|
| Suction pressure | 6,137 kPag (890 psig); low suction pressure TBD | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Suction temperature | 43 deg C service basis (35 deg C winter / 43.3 deg C summer in design table) | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Discharge pressure | 12,866 kPag (1,866 psig); normal discharge pressure TBC | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Capacity | 3,962 e3m3/d (140 MMSCFD) design in both J-T and expander modes; high and excess capacity TBC | DBM-Deepcut §SEC-05 "Sales Gas Booster Compressor Basis"; Design Conditions table |
| Minimum MAWP | 13,100 kPag (1,900 psig) for suction and discharge | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Design temperature | Suction 149 °F (300 °F alternate); discharge 177 °F (350 °F alternate) | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Water content | < 0.1 ppmv (upstream molecular-sieve dehydration) | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Inlet composition (expander mode) | C1 88.31, C2 11.32, C3 0.03, N2 0.17, CO2 0.15 mol% | DBM-Deepcut §SEC-05 booster design compositions |
| Inlet composition (J-T mode) | C1 84.84, C2 9.61, C3 3.63, N2 0.46, CO2 0.42 mol% | DBM-Deepcut §SEC-05 booster design compositions |

## Construction (Package Constituents)

| Item | Description | Source |
|---|---|---|
| Suction scrubber | Two-phase suction scrubber upstream of compression; need to be re-evaluated in detailed engineering due to very low inlet dewpoint; assumed inlet liquid density 0.61 SG; horizontal double-hook vane-style demister internals acceptable; size per API-11P or vendor vane-style sizing | DBM-Deepcut §SEC-05 "Sales Gas Booster Compressor Basis" |
| Suction pressure control valve | Full-port automated ball valve, 5 psid differential, fails closed; upstream manual isolation | DBM-Deepcut §SEC-05 booster description |
| Aftercooler | Horizontal airflow, single-fan, on-module air cooler; winter outlet 35.0 °C, summer outlet 43.3 °C; simulated first-stage aftercooler gas-section pressure drop 69.0 kPad (design dP TBC); automated pneumatic louver control | DBM-Deepcut §SEC-05 booster description |
| Blowdown valve | One blowdown valve, fails closed | DBM-Deepcut §SEC-05 booster description |
| Start-up | Designed to start from equalization pressure; equalization pressure must not exceed system MAWP; alternate option to depressure back into sales compressor discharge header | DBM-Deepcut §SEC-05 booster description |
| Automation | Isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, and shutdown sequences automated; electric circulating lube oil heater included | DBM-Deepcut §SEC-05 booster description |
| Sweet gas purge | Manual sweet gas purge NOT included on this package; external-responsibility item | DBM-Deepcut §SEC-05 booster description |
| Packing drains/vents | Collected to common seal pot; seal-pot vapour to VRU suction header; liquids trucked out locally; distance-piece sweep purge required | DBM-Deepcut §SEC-05 booster description |
| Recycle control valve | Sized for 100% capacity at minimum pipeline operating pressure and high suction pressure (start-up case); fail closed (TBC); single full-port manual isolation valve on outlet | DBM-Deepcut §SEC-05 booster description |
| Clearance pockets | Automated continuously variable or fixed-volume clearance pockets to be evaluated against manual VVCP in detailed engineering | DBM-Deepcut §SEC-05 booster description |
| Sparing equipment / instrumentation | No spare compressor and no spare package equipment/instrumentation | DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions |
| Equipment / instrument tag list | TBD — not present in accessible source | source not local |
| Module / building scope | TBD — not stated in accessible source slice (`location TBD`) | source not local |

## Integration Narrative (Whole-Facility)

The sales gas booster compressor is a single sweet-gas reciprocating package downstream of the inlet/sales multi-service compressor units at the 04-25 Deep Cut Gas Plant. It receives sweet sales gas from two sales compressor units and delivers high-pressure gas to the downstream high-pressure sales gas coalescer and splitter for delivery to the TC sales gas pipeline. Plant sales gas is capable of flowing to TC, Enbridge, and Alliance receipt points; the booster is the dedicated boost stage that lifts sales gas to TC pipeline delivery pressure. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-02 Plant Overview, §SEC-05 Compression Configuration, §SEC-05 Sales Gas Booster Compressor Basis.

## Responsibility Assignment (Summary)

| Function | Party | Source |
|---|---|---|
| EPC Scope of Work authorship and integration | EPC Integrator | `_CONTEXT.md` ResponsibleParty |
| Vendor package engineering, design, fabrication/supply of physical equipment | Package Vendor (with EPC Integrator integration review) | GATE-07 DELIVERABLE_REGISTER row DEL-049-04 |
| Vendor documentation register, submittals, turnover records | Package Vendor (with EPC Integrator review) | GATE-07 DELIVERABLE_REGISTER row DEL-049-05 |
| Vendor package review and acceptance, integration handoff | EPC Integrator (lead) | GATE-07 DELIVERABLE_REGISTER row DEL-049-06 |

## References

- `_REFERENCES.md`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-02, §SEC-05
- GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv (rows DEL-049-01..06)
- Workbook Packages row 80; 26020-Package_Requirements.docx package heading 4 — NOT locally accessible as extracted markdown (`location TBD`)
