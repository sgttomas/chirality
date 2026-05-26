# Specification — DEL-070-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, NGL)

## Scope

This specification governs the Package Vendor's engineering, design, fabrication/supply, and physical delivery of the NGL Mole Sieve Drier Unit equipment package for `PKG-070` at the 4-25 Deepcut facility. The package is anchored upstream by the EPC Integrator's Scope of Work (`DEL-070-01`) and Package Datasheet (`DEL-070-02`), and is integration-reviewed by the EPC Integrator before acceptance (`DEL-070-06`).

**Included.** Three-tower NGL molecular-sieve dehydration unit with inlet liquid/liquid coalescer, adsorbent charge, regeneration-gas heater, regeneration-gas aerial cooler, regeneration-gas scrubber, outlet filter, moisture analyzer, sample points, building enclosure for the regeneration heater (TBC), package piping, instrumentation, and controls within the vendor battery limit (sources: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1574-1623; line 2608).

**Excluded.** Upstream NGL mercaptan treating and water-wash systems (separate package), downstream NGL storage bullets and product pumps, the stabilizer overheads compressor and its modifications for any future dedicated NGL regen cylinder, sales-gas supply for regeneration upstream of the vendor battery limit, and produced-water and flare headers downstream of the package interface. Interface tie-in points are defined by the EPC Integrator's Package Datasheet (`DEL-070-02`).

## Requirements

### R-1 — Process duty (source-grounded)

| ID | Requirement | Value | Source |
|---|---|---|---|
| R-1.1 | Configuration | 3-tower NGL mol-sieve dehydration unit | DBM-Deepcut line 1584 |
| R-1.2 | Design throughput | 2,385 m3/d / 15,000 bbl/d | DBM-Deepcut line 1585 |
| R-1.3 | Inlet design pressure | 1,978 kPag (low / high pressure envelope TBC) | DBM-Deepcut line 1586 |
| R-1.4 | Outlet design pressure | 1,943 kPag (low / high TBC) | DBM-Deepcut line 1587 |
| R-1.5 | Inlet temperature envelope | 29.7 / 46.3 / 51.8 deg C (low / design / high) | DBM-Deepcut line 1588 |
| R-1.6 | Inlet water content basis | Saturated at design inlet conditions and flow | DBM-Deepcut line 1589 |
| R-1.7 | Outlet water content — expected | <1 ppmv H2O | DBM-Deepcut line 1590 |
| R-1.8 | Outlet water content — maximum | 7 ppmv H2O | DBM-Deepcut line 1591 |
| R-1.9 | Governing outlet NGL water content | <7 ppmw (TBC by EPC Integrator) | DBM-Deepcut line 1592 |
| R-1.10 | Bed pressure drop, SOL | <4 psid (27.6 kPad) in adsorption | DBM-Deepcut line 1593 |
| R-1.11 | Bed pressure drop, EOL | <10 psid in adsorption including vessel nozzles | DBM-Deepcut line 1594 |
| R-1.12 | Adsorbent | 3A molecular sieve with silica gel carryover-protection layer | DBM-Deepcut line 1595 |
| R-1.13 | Adsorbent lifecycle target | 3 years (TBC; vendor to define and warrant) | DBM-Deepcut line 1596 |
| R-1.14 | Sulphur co-adsorption | System shall minimize sulphur co-adsorption; vendor shall describe regeneration-gas blow-down-to-flare provisions for contamination events | DBM-Deepcut line 1578 |

### R-2 — Mechanical scope of supply

| ID | Requirement | Source |
|---|---|---|
| R-2.1 | Inlet liquid/liquid coalescer: 2 x 100%, with coalesced water routed by level control to produced-water drain | DBM-Deepcut line 1602 |
| R-2.2 | Outlet filter: P2 bag-filter type, nominal 5 micron, 2 x 100% (filter type and drain/fill provisions to be reviewed) | DBM-Deepcut line 1623 |
| R-2.3 | Regeneration-gas heater inside the NGL mole-sieve building: BEU heat-medium / process-gas shell-and-tube design (TBC) | DBM-Deepcut line 1617 |
| R-2.4 | Regeneration-gas aerial cooler: design cold-side outlet 110 deg F; automated warm-air recirculation louvers; consider plenum heating bundle for winter freeze protection | DBM-Deepcut line 1619 |
| R-2.5 | Regeneration-gas scrubber: three-phase vessel with mist pad; water drain by level control; hydrocarbon level-control to stabilizer flash feed separator at ~50 psig | DBM-Deepcut line 1621 |
| R-2.6 | Indicative tagged equipment within the vendor battery limit (subject to EPC Integrator P&ID confirmation): AC-6895-1, AC-6880-1, F-6810-1, F-6860-1, F-6865-1, E-6890-1, E-6870-1, MX-6727-1, MX-6728-1, P-6725-1, P-6726-1, V-6830-1, V-6840-1, V-6850-1, V-6720-1, V-6885-1 | DBM-Deepcut Packages register, line 2608 |
| R-2.7 | Materials of construction, weld procedures, NDE, PWHT, and jurisdictional registration | TBD — to be set by EPC Integrator Package Datasheet (`DEL-070-02`) (location TBD) |

### R-3 — Regeneration system

| ID | Requirement | Source |
|---|---|---|
| R-3.1 | Regeneration gas source: sales gas (basis), with final source tie-in and existence confirmation by EPC Integrator | DBM-Deepcut line 1617 |
| R-3.2 | Regeneration gas flow basis: 3.5 to 5 MMSCFD (TBC) | DBM-Deepcut line 1617 |
| R-3.3 | Bed-inlet regeneration temperature: 460 deg F (TBC) | DBM-Deepcut line 1617 |
| R-3.4 | Cooler operation: maintain at least 15 deg F above hydrocarbon dewpoint and/or hydrate point at operating conditions | DBM-Deepcut line 1619 |
| R-3.5 | Cycle times: adsorption 24 h preliminary; draining, heating ramps, pre-heat hold, heating, cooling, filling, standby, total regeneration cycle — TBC (vendor to define and confirm during detailed engineering) | DBM-Deepcut lines 1606-1615 |
| R-3.6 | Contamination control: provide capability to blow regeneration gas down to flare on sulphur recycle/contamination events | DBM-Deepcut line 1578 |

### R-4 — Instrumentation and analyzers

| ID | Requirement | Source |
|---|---|---|
| R-4.1 | Moisture analyzer MA-6800-1 (E&H SpectraSensor or vendor-equivalent), manifolded from common dry line and from each NGL mol-sieve drier | DBM-Deepcut lines 2134, 2142 |
| R-4.2 | Dry C3+ / NGL sample points ME-6800-1, ME-6810-1, ME-6820-1 (Aircom or equivalent) | DBM-Deepcut line 2143 |
| R-4.3 | Bed dP, bed temperature profile, switching-valve position, regen-gas heater outlet T, scrubber level controls, aerial cooler control logic | ASSUMPTION (industry-standard mol-sieve instrumentation); detailed P&ID and controls philosophy from EPC Integrator (location TBD) |

### R-5 — Sparing and reliability

| ID | Requirement | Source |
|---|---|---|
| R-5.1 | Beds: no installed spare in current basis; 1 regenerating / 1 adsorbing; vendor shall confirm sparing for the requested adsorbent lifecycle; if 5-year lifecycle is required, vendor shall propose an installed spare bed | DBM-Deepcut line 1598 |
| R-5.2 | Inlet liquid/liquid coalescer and outlet filter: 2 x 100% sparing | DBM-Deepcut lines 1602, 1623 |

## Standards (governing)

| Standard | Application | Source / Status |
|---|---|---|
| Provincial pressure-equipment registration (ABSA / BCSA, as applicable) | All pressure vessels and registered piping | ASSUMPTION based on jurisdiction; confirm in `DEL-070-02` (location TBD) |
| ASME BPVC Section VIII Div. 1 | Pressure vessels | ASSUMPTION; confirm in `DEL-070-02` (location TBD) |
| ASME B31.3 | Process piping | ASSUMPTION; confirm in `DEL-070-02` (location TBD) |
| API / vendor mol-sieve practice | Adsorber internals, cycle design | ASSUMPTION; confirm vendor practice in vendor design basis (location TBD) |
| Project specifications carried forward from EPC Package Datasheet | All disciplines | location TBD pending `DEL-070-02` |

## Verification

| Requirement(s) | Verification Approach |
|---|---|
| R-1.1 to R-1.14 | Vendor process datasheets and simulation/sizing calculations; EPC Integrator review against `DEL-070-02`; performance test on first regeneration cycle |
| R-2.1 to R-2.6 | Mechanical datasheets, GA drawings, P&IDs; mill certs; hydrotest reports; jurisdictional registration |
| R-2.7 | Document review against `DEL-070-02` (TBD) |
| R-3.1 to R-3.6 | Regen cycle dry-run and first-fill commissioning; tie-in confirmation by EPC Integrator |
| R-4.1 to R-4.3 | Loop checks; analyzer calibration certificates; sample-point witness |
| R-5.1 to R-5.2 | Vendor sparing statement; lifecycle warranty terms |

## Documentation

The Vendor shall produce, as a minimum, the following vendor package deliverables to enable EPC Integrator integration review (`DEL-070-06`) and vendor document turnover (`DEL-070-05`):

- Vendor package design basis and datasheet set (anticipated artifact per `_CONTEXT.md`).
- Vessel, exchanger, filter, scrubber, and adsorbent datasheets.
- Skid GA, P&ID, and electrical/instrument schedules within vendor battery limit.
- Adsorbent loading and lifecycle warranty statement; sparing statement (R-5.1).
- Regeneration cycle definition (R-3.5) and contamination-control description (R-3.6).
- Code certificates and jurisdictional registration documents.
- Test/inspection records and turnover dossier.
