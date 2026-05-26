# Datasheet — DEL-050-04 Vendor Engineered Equipment Package (Stabilizer Overheads Compressors)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-050-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-050` — Stabilizer Overheads Compressors | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-050 |
| Workbook Row | 81; WBS 01 | `PACKAGE_REGISTER.csv` row PKG-050 |
| Package Tag | `26020-01-12-005` (RFQ tag `26020-01-PT-12-005`) | `PACKAGE_REGISTER.csv` row PKG-050 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Scope SOW IDs | SOW-0173, SOW-0174, SOW-0175, SOW-0176 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Objectives (ASSUMPTION, package-heuristic) | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC |

## Attributes — Compressor Package

| Attribute | Value | Source |
|---|---|---|
| Service | Stabilizer Overheads Compressor (SOC); compresses and recycles multiple flashed/overhead streams from 50 psig to 1,100 psig; final discharge to amine inlet filter coalescers or recycle to first-stage suction | SOW-0174; `DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04 "Stabilizer Overheads Compressor Basis" L714 |
| Quantity / sparing | 2 × 100 %, operating plus standby (induction-motor-driven separable reciprocating packages) | SOW-0174; DBM §SEC-04 L718 |
| Compressor model | Ariel KBC/6 four-stage separable reciprocating | SOW-0175; DBM §SEC-04 L719 |
| Stages | 4 | SOW-0175; DBM L720 |
| Driver | 4,000 V, 3-phase, 60 Hz electric induction motor, 8-pole, ~891 rpm; with VFD speed control and automated recycle valve | SOW-0175, SOW-0176; DBM L721–L724 |
| Driver power | 2,700 hp / 2,013 kW (includes ~10 % excess power) | SOW-0176; DBM L722 |
| Driver turndown | 3 : 1 inverter turndown | SOW-0176; DBM L724 |
| Driver enclosure | TBD (RFQ quote TEFC); non-sparking bidirectional cooling fans; NEMA MG 1 tested/labelled; no Toshiba motors | SOW-0175, SOW-0176; DBM L828 |
| Motor insulation | Class F with Class B rise at full load | DBM L828 |
| Lube-oil aids | Electric circulating lube-oil heater; supplemental lube-oil pump provisions per OEM | DBM L828 |

## Conditions — Operating and Design

| Parameter | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Source |
|---|---:|---:|---:|---:|---|
| Suction pressure, kPag | 305.67 (design 345) | 723.48 | 1,594.72 | 3,423.59 | SOW-0176; DBM L741 |
| Discharge pressure, kPag | 799.09 | 1,696.74 | 3,600.16 | 8,353.83 (final 7,585 / 1,100 psig) | SOW-0176; DBM L742, L714, L726 |
| Cooler discharge temperature, °C | 65.56 | 87.78 | 65.56 | 77.35 | SOW-0176; DBM L821 |
| Hydrocarbon dewpoint, °C | 53.44 | 85.31 | 58.41 | 71.79 | DBM L822 |
| Design suction temperature, °C | 149 | 149 | 149 | 149 | SOW-0176; DBM L766–L772 |
| Design discharge temperature, °C | 177 | 177 | 177 | 177 | SOW-0176; DBM L767–L773 |
| Minimum MAWP, kPag | 1,723 (1st stage suction) | TBC | TBC | 9,101 (4th stage discharge) | SOW-0176; DBM L766, L773 |
| Design capacity, MMSCFD | 2.5 | 5 | 17 | 17 | SOW-0176; DBM L734–L737 |
| Excess capacity vs. expected, % | 206 | 200 | 151 | 151 | DBM L734–L737 |

Design suction pressure (whole machine): 345 kPag (50 psig); design discharge pressure: 7,585 kPag (1,100 psig). Source: DBM L725–L726.

## Construction — Major Included Equipment (Vendor Scope)

| Sub-item | Basis / Note | Source |
|---|---|---|
| Aerial intercoolers (after each stage) | Common-frame, AP-661 (modified); warm-air recirculation; plenum heater for winter stability; automated louvers with electro-pneumatic transducers and TE in SOC control system; non-sparking bidirectional cooling | SOW-0175; DBM L824 |
| 1st-stage suction scrubber | Two-phase with cyclonic element; mist pad (not mesh/vane); K_max ≤ 0.25 imperial + deration; vendor sizes capacity | SOW-0175; DBM L815 |
| 2nd / 3rd / 4th-stage suction scrubbers | Two-phase with demister; mist pad; vendor sizes capacity | SOW-0175; DBM L815 |
| Packing vent / drain separation pot | Two-phase, DP 101 kPag; vendor sizes capacity | SOW-0175 |
| Vacuum pump | Vendor sizes capacity | SOW-0175 |
| Seal-pot waste-oil transfer pump | Vendor sizes capacity | SOW-0175 |
| Packing drains / vents collection | Header + seal pot; vapour to VRU suction header; liquids removed by local truck-out | DBM L828 |
| Recycle valve | Single, sized for 100 % recycle at 40 % speed and low discharge pressure; full-port manual isolation on outlet; fail position TBC | DBM L826 |
| Start-up bypass valve | Automated quarter-turn full-port ball valve | DBM L826 |
| Suction PCVs | One per side-stream service plus 1st-stage inlet PCV; ET-type preferred; <2 psid at 100 % open; fail closed | DBM L815 |
| Building | Self-framing building enclosing instrumentation; modular shop assembly; disassembled into three pieces for shipment; single-piece shipment TBC | DBM L728 |
| Sweet-gas purge | Manual connection at 1st-stage suction downstream of inlet PCV (maintenance) | DBM L828 |

## Gas Composition (Normal Winter — to be reviewed in detailed engineering)

See DBM §SEC-04 L779–L805 (Stage 1–4 mole-% composition table for Water, H2, N2, CO2, H2S, C1–C8, mercaptans, CS2, BTEX, naphthenics). Inlet H2S basis carried at Stage 1 = 1.37 mol % and Stage 4 = 0.89 mol %; basis flagged TBC due to transient inlet streams.

## Scope by Others (Not Vendor Supply)

- Shipping packages to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs — by others. Source: SOW-0176.

## References

- `_CONTEXT.md` (deliverable identity).
- `_REFERENCES.md` (authoritative basis pointers).
- `GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row PKG-050.
- `GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` rows SOW-0173, SOW-0174, SOW-0175, SOW-0176.
- `GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-050-04.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04 "Stabilizer Overheads Compressor Basis" and "Controls, Protection, and Safeguards" (lines 712–828); package-vendor source `26020-Package_Requirements.docx` package heading 5 (referenced but binary, not directly read in this run — location TBD for clause-level slices).
- `_Sources/26020-Package_Requirements.docx` — binary; clause text not directly accessible in markdown; surfaced through SOW-0173/0174/0175/0176 extracts only. **location TBD** for direct clause references.
