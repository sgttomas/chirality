# Datasheet — DEL-070-02 Package Datasheet (Mole Sieve Drier Unit, NGL)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-070-02_package-datasheet |
| Name | Package Datasheet |
| ParentPackageID | PKG-070 |
| ParentWorkbookID | 70 |
| PackageName | Mole Sieve Drier Unit (NGL) |
| Discipline | Mechanical |
| Type | EPC Package Datasheet |
| ResponsibleParty | EPC Integrator |
| Facility | 04-25 Deepcut Gas Plant |
| Process service | NGL molecular-sieve dehydration upstream of NGL storage |
| Adsorption media | 3A molecular sieve, with silica gel layer for liquid carryover protection |

Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Current-Scope NGL Molecular-Sieve Dehydration (lines 1574-1623); `_CONTEXT.md`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Configuration | 3-tower NGL molecular-sieve dehydration unit | DBM-Deepcut §NGL Molecular-Sieve Design Parameters |
| Bed sparing | One bed in adsorption, one in regeneration; no installed spare in current basis (ASSUMPTION: third tower used for staging per 3-tower configuration); sparing review pending detailed engineering | DBM-Deepcut line 1598 |
| Design throughput | 2,385 m3/d (15,000 bbl/d) | DBM-Deepcut line 1585 |
| Adsorbent | 3A molecular sieve; silica gel guard layer | DBM-Deepcut line 1595 |
| Adsorbent lifecycle | 3 years (vendor-defined, TBC) | DBM-Deepcut line 1596 |
| Inlet liquid/liquid coalescer | 2 x 100%, removes entrained free water to produced water tank | DBM-Deepcut line 1602 |
| Regeneration heater | BEU shell-and-tube, heat medium / process gas, inside NGL mole-sieve building | DBM-Deepcut line 1617 |
| Regeneration gas cooler | Aerial cooler, design outlet 110 deg F, automated warm-air recirculation louvers; plenum heating bundle to be considered for winter | DBM-Deepcut line 1619 |
| Regeneration-gas scrubber | Three-phase vessel with mist pad; separates water and condensed NGL | DBM-Deepcut line 1621 |
| Outlet filter | P2 bag-filter housing, nominal 5 micron, 2 x 100% (filter type and drain/filling TBR) | DBM-Deepcut line 1623 |

## Conditions

### Process design conditions

| Parameter | Low | Design | High | Source |
|---|---|---|---|---|
| Inlet pressure (kPag) | TBC | 1,978 | TBC | DBM-Deepcut line 1586 |
| Outlet pressure (kPag) | TBC | 1,943 | TBC | DBM-Deepcut line 1587 |
| Inlet temperature (deg C) | 29.7 | 46.3 | 51.8 | DBM-Deepcut line 1588 |
| Inlet water content | Saturated at design inlet conditions and flow | — | — | DBM-Deepcut line 1589 |
| Expected outlet water content | — | <1 ppmv H2O | — | DBM-Deepcut line 1590 |
| Maximum outlet water content | — | 7 ppmv H2O | — | DBM-Deepcut line 1591 |
| Governing outlet NGL water content | — | <7 ppmw (TBC) | — | DBM-Deepcut line 1592 |
| Bed pressure drop, start of life | — | <4 psid (27.6 kPad) in adsorption | — | DBM-Deepcut line 1593 |
| Bed pressure drop, end of life | — | <10 psid in adsorption (incl. vessel nozzles) | — | DBM-Deepcut line 1594 |

### Regeneration conditions

| Parameter | Value | Source |
|---|---|---|
| Regeneration gas service | Sales gas (existence and final source tie-in TBC) | DBM-Deepcut line 1617 |
| Regeneration gas flow | 3.5 to 5 MMSCFD (basis pending confirmation) | DBM-Deepcut line 1617 |
| Regeneration heating temperature | 460 deg F before flow to bed in regeneration mode | DBM-Deepcut line 1617 |
| Regeneration cooler outlet | 110 deg F at design; maintain 15 deg F above hydrocarbon dewpoint / hydrate point | DBM-Deepcut line 1619 |
| Adsorption cycle time | 24 h (preliminary) | DBM-Deepcut line 1606 |
| Draining / heating ramps / hold / cooling / filling / standby / total | TBC | DBM-Deepcut lines 1607-1615 |

### Material/contamination conditions

- Co-adsorption of sulphur compounds is undesirable; sulphur spikes during regeneration could recycle and create off-spec product. Provision for blowdown of regeneration gas to flare on contamination is required. (Source: DBM-Deepcut line 1578.)

## Construction

| Item | Basis | Source |
|---|---|---|
| Vessel quantity | 3 towers | DBM-Deepcut line 1584 |
| Inlet coalescer | 2 x 100% liquid/liquid coalescer | DBM-Deepcut line 1602 |
| Outlet filter | 2 x 100%, P2 bag-filter, nominal 5 micron | DBM-Deepcut line 1623 |
| Regeneration heater | BEU shell-and-tube, located inside NGL mole-sieve building | DBM-Deepcut line 1617 |
| Regeneration cooler | Aerial cooler with automated warm-air recirculation; plenum heating for winter TBR | DBM-Deepcut line 1619 |
| Regeneration scrubber | Three-phase vessel with mist pad; sized with scrubber drain capacity TBC | DBM-Deepcut line 1621 |
| Materials of construction | TBD (not stated in available source slice) | location TBD |
| Code stamps / flange ratings (NGL service) | TBD (process-gas mole-sieve system uses 900# flanges; NGL service flange basis not stated in available source slice) | location TBD; cross-reference DBM-Deepcut line 628 (process-gas system) |
| Building / enclosure | NGL mole-sieve building referenced (regeneration heater located within) | DBM-Deepcut line 1617 |

## Interfaces (carried as evidence per _CONTEXT.md Notes)

| Interface | Counterparty / Service | Source |
|---|---|---|
| NGL inlet | Downstream of NGL water wash / mercaptan treating | DBM-Deepcut line 1513, 1558 |
| Dry NGL outlet | Mole-sieve outlet filter, then downstream heat exchange to NGL storage | DBM-Deepcut line 1623, §Current-Scope NGL Molecular-Sieve Dehydration |
| Regeneration gas supply | Sales gas, upstream of sales-gas compressors (TBC) | DBM-Deepcut line 1617 |
| Regeneration gas return | Stabilizer flash feed separator (separated hydrocarbon at ~50 psig); stabilizer overheads compressor as transient recycle path (TBC) | DBM-Deepcut line 1621 |
| Produced water | Coalesced free water by level control to produced water tank; scrubber water to produced water drain | DBM-Deepcut lines 1602, 1621 |
| Flare | Blowdown of regeneration gas to flare on sulphur contamination | DBM-Deepcut line 1578 |
| Heat medium / process gas | BEU regeneration gas heater inside NGL mole-sieve building | DBM-Deepcut line 1617 |
| Vendor regeneration compressor (alternate) | Dedicated cylinder at stabilizer overheads compressor (alternate isolation path; TBR detailed engineering) | DBM-Deepcut line 1578 |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Current-Scope NGL Molecular-Sieve Dehydration (lines 1574-1623).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Sales-Gas and NGL Treating and Dehydration overview (lines 1400-1410).
- `_CONTEXT.md` for deliverable identity and scope.
- Decomposition entry: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-070-02.
- Inaccessible (no text extraction available locally): `_Sources/26020-Package_Requirements.docx` (heading 24), `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages row 74). Content depending on these remains TBD.
