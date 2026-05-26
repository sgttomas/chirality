# Guidance — DEL-070-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, NGL)

## Purpose

This guidance frames how the EPC Integrator and the Package Vendor should approach the NGL Mole Sieve Drier Unit equipment package. It does not restate requirements (see `Specification.md`); it explains rationale, considerations, and trade-offs so design decisions taken downstream remain consistent with the 4-25 Deepcut design basis and the EPC scope envelope (`DEL-070-01`, `DEL-070-02`).

## Principles

1. **Source-of-record discipline.** The 4-25 Deepcut DBM "Current-Scope NGL Molecular-Sieve Dehydration" subsection (SEC-07, lines 1574-1623) is the process-basis anchor. Vendor design decisions that deviate from that basis require an EPC Integrator change against `DEL-070-02`.
2. **Sulphur stewardship.** The unit must avoid recycling co-adsorbed sulphur into product. Regeneration-gas blow-down to flare on contamination is the safety-net of last resort; preferred path is upstream sulphur-quality stewardship in the NGL mercaptan treating and water-wash systems (DBM SEC-07 line 1578).
3. **TBC items are work, not silence.** Many cycle-time entries, the regeneration-gas source tie-in, the outlet water-content number, and pressure low/high envelopes are explicitly TBC in the basis. They must be closed by EPC Integrator + Vendor jointly, not silently assumed by either party (DBM SEC-07 lines 1586-1592, 1607-1617).
4. **Sparing is a lifecycle conversation, not a numbers game.** The 1+1 bed arrangement is tied to a 3-year adsorbent life. A 5-year-life vendor proposal materially changes the sparing arithmetic (DBM SEC-07 lines 1596, 1598).

## Considerations

### Adsorbent selection and protection

3A molecular sieve sized to <7 ppmw outlet, with a silica gel layer above it to absorb sudden liquid carryover, is the documented basis. The vendor's adsorbent supplier and the EPC Integrator should jointly review:

- expected sulphur compound slate at unit inlet (downstream of caustic treating and water wash);
- carryover protection sufficiency at upstream water-wash upset conditions;
- regeneration temperature staying within adsorbent supplier guidance for the chosen 3A grade.

Source: DBM SEC-07 lines 1595, 1578, 1602.

### Regeneration-gas source

The basis identifies sales gas as the regeneration medium, but the existence and final source tie-in remain TBC. The vendor's mechanical design (heater duty, scrubber sizing, aerial cooler duty) is sensitive to the gas composition and flow window (3.5-5 MMSCFD, 460 deg F at the bed). Lock the source tie-in early — ideally before mechanical bid award. (DBM SEC-07 line 1617.)

### Building, heater, and winter operability

The regeneration-gas heater is intended to sit inside the NGL mole-sieve building. The aerial cooler is outdoor with warm-air recirculation louvers and may need a plenum heating bundle for winter freeze protection. Both decisions interact with site civil/structural and HVAC design; the vendor should provide heat-load and freeze-protection requirements early. (DBM SEC-07 lines 1617, 1619.)

### Transient handling: scrubber drains and SOC recycle

Scrubber drain capacity, hot-bed filling rate, and the resulting transient recycle to the stabilizer overheads compressor (SOC) and stabilizer are flagged in the basis as detailed-engineering TBDs. The vendor's cycle definition (R-3.5) should produce transient flows that the EPC Integrator can size the SOC and stabilizer for, rather than vice versa. (DBM SEC-07 line 1621; line 1799-1800 for SOC interaction.)

### Outlet filtration

P2 bag-filter housings at 5 micron, 2 x 100%, with filter type and drain/fill arrangements explicitly noted as "to be reviewed." The vendor should propose a filter type that is changeable without shutting both housings, with drains routed to a safe disposition. (DBM SEC-07 line 1623.)

## Trade-offs

| Decision | Option A | Option B | Notes |
|---|---|---|---|
| Bed sparing | 1 regen + 1 adsorb, 3-year sieve life | 1 regen + 1 adsorb + 1 installed spare, 5-year sieve life | Capital vs. turnaround cadence; vendor warranty terms decisive (DBM SEC-07 lines 1596, 1598) |
| Regen-gas isolation | Sales-gas regen (current basis) | Dedicated SOC cylinder for NGL regen | Lower sulphur recycle risk vs. SOC scope creep (DBM SEC-07 line 1578) |
| Outlet water target | <1 ppmv (expected) | <7 ppmw (governing/TBC) | Driven by downstream NGL product spec, NRM NEBC Connector LACT, and storage-bullet vapour considerations (DBM SEC-07 lines 1590-1592) |
| Winter freeze protection of aerial cooler | Recirculation louvers only | Recirculation louvers + plenum heating bundle | Capital vs. cold-snap reliability (DBM SEC-07 line 1619) |

## Examples

The 4-25 Deepcut DBM treats the NGL mol-sieve drier as a vendor package developed against the EPC Package Datasheet, in the same pattern used for the process-gas mol-sieve dehydration unit (DBM SEC-06 "Molecular-Sieve Dehydration and Mercury Removal Basis", lines 1239-1297). Where the EPC Integrator and vendor face a question that is silent in the NGL basis, the process-gas mol-sieve precedent in SEC-06 is a reasonable analogy — but only as analogy, not as authority for the NGL unit.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-070-04-01 | Outlet NGL water content target stated two ways: "<1 ppmv H2O" (expected) and "7 ppmv H2O" (maximum), with a separate "Governing outlet NGL water content: <7 ppmw (TBC)" line | DBM-Deepcut SEC-07, lines 1590-1591 | DBM-Deepcut SEC-07, line 1592 | Datasheet Process Conditions, Specification R-1.7/R-1.8/R-1.9 | Treat <7 ppmw as governing acceptance criterion; <1 ppmv as design intent; EPC Integrator to confirm in `DEL-070-02` | TBD |
| CFT-070-04-02 | Regeneration-gas source: sales gas in current basis vs. dedicated SOC cylinder under review | DBM-Deepcut SEC-07, line 1578 | DBM-Deepcut SEC-07, line 1617 | Specification R-3.1, R-3.6; Guidance — Regeneration-gas source | Retain sales-gas source as design basis; carry SOC cylinder as a parallel detailed-engineering review item with go/no-go date | TBD |
| CFT-070-04-03 | Bed sparing: 1+1 with 3-year sieve life vs. 1+1+spare with 5-year life | DBM-Deepcut SEC-07, line 1596 | DBM-Deepcut SEC-07, line 1598 | Specification R-5.1; Guidance — Trade-offs | Vendor to submit both options with adsorbent supplier warranty terms; EPC Integrator selects | TBD |
