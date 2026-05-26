# Datasheet — DEL-070-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, NGL)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-070-04_vendor-engineered-equipment-package` | `_CONTEXT.md` Identity |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` Identity |
| Parent Package | `PKG-070` — Mole Sieve Drier Unit (NGL) | `_CONTEXT.md` Identity |
| Parent Workbook | 70 | `_CONTEXT.md` Identity |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` Identity |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` Identity |
| Covers Scope Items | SOW-0145, SOW-0146, SOW-0147, SOW-0148 | `_CONTEXT.md`; Deliverable Register (Gate 7) |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouping heuristic) | Deliverable Register (Gate 7) |
| Source basis pointer | Workbook Packages row 74; 26020-Package_Requirements.docx package heading 24 | `_CONTEXT.md` Source Reference |
| Process-basis source slice | 4-25 Deepcut DBM, SEC-07, "Current-Scope NGL Molecular-Sieve Dehydration" | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1574-1623 |

## Attributes (Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Package function | NGL molecular-sieve dehydration unit downstream of NGL mercaptan treating and water wash; produces dry NGL to product storage | DBM-Deepcut SEC-07, lines 1513, 1574-1576 |
| Configuration | 3-tower NGL molecular-sieve dehydration unit | DBM-Deepcut SEC-07, line 1584 |
| Installed sparing (beds) | No installed spare in current basis; one bed regenerating, one bed adsorbing (TBC in detailed engineering; spare bed considered if 5-year sieve life is required) | DBM-Deepcut SEC-07, line 1598 |
| Indicative equipment tag list (from package register) | AC-6895-1, AC-6880-1, F-6810-1, F-6860-1, F-6865-1, E-6890-1, E-6870-1, MX-6727-1, MX-6728-1, P-6725-1, P-6726-1, V-6830-1, V-6840-1, V-6850-1, V-6720-1, V-6885-1 | DBM-Deepcut Packages register, line 2608 |
| Inlet liquid/liquid coalescer | 2 x 100% upstream of beds; coalesced water by level control to produced water tank | DBM-Deepcut SEC-07, line 1602 |
| Outlet filter | P2 bag-filter type housing, nominal 5 micron, 2 x 100% (filter type and drain/fill provisions TBR) | DBM-Deepcut SEC-07, line 1623 |
| Regeneration-gas heater | BEU heat-medium / process-gas shell-and-tube heater inside the NGL mole-sieve building (TBC) | DBM-Deepcut SEC-07, line 1617 |
| Regeneration-gas aerial cooler | Cools hot regen gas to 110 deg F at design; automated warm-air recirculation louvers; plenum heating bundle to be considered for winter freeze protection | DBM-Deepcut SEC-07, line 1619 |
| Regeneration-gas scrubber | Three-phase vessel with mist pad; separates free water and condensed NGL; water to produced water drain; hydrocarbon to stabilizer flash feed separator at ~50 psig | DBM-Deepcut SEC-07, line 1621 |
| Moisture analyzer | One NGL mol-sieve moisture analyzer (MA-6800-1, E&H SpectraSensor), manifolded from common line and from each NGL mol-sieve drier | DBM-Deepcut, lines 2134, 2142 |
| Dry C3+ / NGL sample points | ME-6800-1, ME-6810-1, ME-6820-1 (Aircom) | DBM-Deepcut, line 2143 |

## Process Conditions

| Parameter | Value | Source |
|---|---|---|
| Design throughput | 2,385 m3/d / 15,000 bbl/d | DBM-Deepcut SEC-07, line 1585 |
| Inlet pressure | Low TBC; design 1,978 kPag; high TBC | DBM-Deepcut SEC-07, line 1586 |
| Outlet pressure | Low TBC; design 1,943 kPag; high TBC | DBM-Deepcut SEC-07, line 1587 |
| Inlet temperature | Low 29.7 deg C; design 46.3 deg C; high 51.8 deg C | DBM-Deepcut SEC-07, line 1588 |
| Inlet water content | Saturated at design inlet conditions and flow | DBM-Deepcut SEC-07, line 1589 |
| Expected outlet water content | <1 ppmv H2O | DBM-Deepcut SEC-07, line 1590 |
| Maximum outlet water content | 7 ppmv H2O | DBM-Deepcut SEC-07, line 1591 |
| Governing outlet NGL water content | <7 ppmw (TBC) | DBM-Deepcut SEC-07, line 1592 |
| Bed pressure drop, SOL | <4 psid / 27.6 kPad in adsorption | DBM-Deepcut SEC-07, line 1593 |
| Bed pressure drop, EOL | <10 psid in adsorption including vessel nozzles | DBM-Deepcut SEC-07, line 1594 |
| Adsorption cycle time | 24 h (preliminary) | DBM-Deepcut SEC-07, line 1606 |
| Other cycle steps (draining, heating ramps, hold, cooling, filling, standby, total) | TBC | DBM-Deepcut SEC-07, lines 1607-1615 |
| Regeneration gas flow | 3.5 to 5 MMSCFD (TBC; source tie-in unconfirmed) | DBM-Deepcut SEC-07, line 1617 |
| Regeneration gas inlet-to-bed temperature | 460 deg F (TBC) | DBM-Deepcut SEC-07, line 1617 |
| Regeneration cooler outlet (design) | 110 deg F; maintain 15 deg F above hydrocarbon dewpoint / hydrate point | DBM-Deepcut SEC-07, line 1619 |

## Construction (Materials, Adsorbent)

| Attribute | Value | Source |
|---|---|---|
| Adsorbent | 3A molecular sieve, with silica gel layer for liquid carryover protection | DBM-Deepcut SEC-07, line 1595 |
| Adsorbent lifecycle | 3 years (TBC, vendor-defined) | DBM-Deepcut SEC-07, line 1596 |
| Vessel materials | TBD (not stated in available source slice) | location TBD |
| Code stamps and registration | TBD (Canadian jurisdictional registration assumed for AB/BC service — ASSUMPTION) | location TBD |
| Insulation / heat tracing | TBD | location TBD |
| Building | NGL mole-sieve building enclosure for regeneration heater (TBC) | DBM-Deepcut SEC-07, line 1617 |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-07 "Current-Scope NGL Molecular-Sieve Dehydration" (lines 1574-1623), plus instrumentation lines 2134-2143 and Packages register line 2608.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 411.
- `_Sources/26020-Package_Requirements.docx`, package heading 24 — listed as authoritative scope basis but locally accessible only as a binary .docx; slice not consumed in this draft (location TBD).
