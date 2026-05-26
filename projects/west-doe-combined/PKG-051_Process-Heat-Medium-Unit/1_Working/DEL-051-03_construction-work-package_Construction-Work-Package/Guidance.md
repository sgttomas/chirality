# Guidance — DEL-051-03 Construction Work Package (PKG-051 Process Heat Medium Unit)

## Purpose

This Construction Work Package (CWP) exists to translate the engineered Process Heat Medium Unit (single unified loop at 220 deg C, Brenntag Petrotherm, API-560 direct-fired heater, single pump module, pop tank, and user lateral piping) into an executable field installation, inspection, and turnover plan. It is the EPC Integrator's mandatory Gate 5 anchor for physically delivering PKG-051 (`_CONTEXT.md`, decomposition row 440).

## Principles

1. **Source-grounded over convention.** Where the DBM gives an explicit basis (e.g., 220 deg C loop temperature, 350 psig minimum design pressure, pop-tank PSV discharge, seal-welded HM exchanger tubes), the CWP shall reflect that basis literally rather than substituting generic construction-spec convention. (DBM-Deepcut 4-25 §"Heat Medium Basis".)
2. **Tie-in discipline before module setting.** Heat medium is a utility serving many users; ambiguity in field tie-ins propagates through commissioning. Publish the tie-in list early and freeze it before module offload. (DBM-Deepcut 4-25 line 617.)
3. **Respect open design items.** Several items remain explicitly open in the DBM (heater sparing arrangement, pump sparing philosophy, single-loop circulation rates, fluid vendor rating to maximum bulk temperature). The CWP shall carry these as planning placeholders, not closed install instructions. (DBM-Deepcut 4-25 lines 1961, 1996, 1998, 1951.)
4. **No block valves on ASME Section I PSV piping.** This is a non-negotiable installation rule for the HM heater and must be visible in inspection ITPs, not just buried in piping notes. (DBM-Deepcut 4-25 line 2435.)
5. **Cold-start at -40 deg C site basis.** Field assembly, lagging, heat tracing, and cold-start commissioning shall be planned for a -40 deg C ambient project basis, with cold-start motor demonstration at 15 deg C. (DBM-Comp_and_Liquids 3-25 line 696; DBM-Deepcut 4-25 line 1996.)

## Considerations

- **Module vs stick-built balance.** The HM pump module and heater are typically vendor-modularized; the pop tank and user lateral runs are typically stick-built. The CWP should distinguish vendor-modular content (shipped-loose lists, offload/setting plan) from field-fabricated piping. (DBM-Deepcut 4-25 line 617.)
- **Cross-discipline interface load.** HM unit construction touches civil (foundations), structural (pipe rack), electrical (MCC, pump motors), controls (BMS, ESD, F&G), and HVAC/heat-tracing. The CWP should anchor each interface in the field tie-in list rather than treating them as separate discipline narratives. (DBM-Deepcut 4-25 line 619.)
- **Hot oil cleanliness.** Hot-oil systems are sensitive to fabrication debris and water ingress; a flushing/cleaning/dry-out procedure for the HM loop is appropriate at construction-commissioning interface. ASSUMPTION: locally accessible source slices do not specify a flushing standard, so the CWP shall flag this as a procedure to confirm with the vendor and operations.
- **Pop tank as safety-critical asset.** Pop tank, its level switch, and its sour tube-rupture venting review (DBM-Deepcut 4-25 line 2002) should be flagged as elevated-attention construction items, not generic atmospheric tankage.
- **Heat tracing and lagging.** Single-loop HM piping needs lagging to retain temperature and to provide personnel protection; heat tracing may be required on selected laterals to prevent solidification on a cold start. ASSUMPTION: not explicitly enumerated in the available DBM slices for PKG-051.

## Trade-offs

- **Heater sparing topology (1 x 125% vs 2 x 62.5% vs 3 x 41.7%).** A single-heater install simplifies foundations, stack, and BMS scope, but offers no maintenance redundancy; a multi-heater install raises civil/electrical/control complexity but improves availability and turnaround flexibility. The CWP should not lock either path before the design ruling. (DBM-Deepcut 4-25 line 1998.)
- **Pump sparing topology (legacy 3 x 72% cold + 3 x 72% hot vs consolidated single-loop arrangement).** Consolidation reduces footprint and electrical load but concentrates risk; the CWP foundation/MCC scope should remain flexible until the sparing ruling is final. (DBM-Deepcut 4-25 line 1996.)

## Examples

- **Field tie-in list row (illustrative):** HM-Supply lateral to TEG regenerator reboiler at the 425 deg F mixing-valve interface (per DBM-Deepcut 4-25 line 1214); installation shall confirm mixing-valve orientation and supply temperature limit set point.
- **Inspection ITP entry (illustrative):** Walk-down PSV piping for the HM heater confirming no block valves on inlet/outlet, per ASME Section I; redline any deviation. (DBM-Deepcut 4-25 line 2435.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | Whether PKG-051 (Process Heat Medium Unit) is a local utility on the 03-25 / Comp_and_Liquids side or a 04-25 / Deepcut-side shared loop. The Comp_and_Liquids DBM appendix note (line 933) states the Petrotherm appendix shall not reintroduce a local 03-25 HM utility (SCA-002 removed it); the Deepcut DBM defines a unified single-loop HM system serving 04-25 users. | DBM-Comp_and_Liquids 3-25 line 933 | DBM-Deepcut 4-25 lines 1822, 1832, 1945 | Datasheet, Specification scope boundary, tie-in list | DBM-Deepcut 4-25 is the governing source for PKG-051 process basis; Comp_and_Liquids appendix note governs what is _excluded_ from the 03-25 side. The CWP install scope follows the Deepcut basis. | TBD — human to confirm package physical location and battery-limit ownership. |
| CT-002 | Pop tank fluid SG: DBM gives 1.00 as TBC. | DBM-Deepcut 4-25 line 2002 | (none) | Datasheet conditions, foundation sizing input | Treat SG = 1.00 as planning placeholder; flag foundation load case as TBC pending vendor data. | TBD |
