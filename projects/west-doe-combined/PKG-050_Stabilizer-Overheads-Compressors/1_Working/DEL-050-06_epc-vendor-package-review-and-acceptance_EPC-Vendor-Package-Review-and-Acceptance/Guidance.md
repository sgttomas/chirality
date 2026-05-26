# Guidance — DEL-050-06 EPC Vendor Package Review and Acceptance

## Purpose

The EPC Integrator is the integrator of record for PKG-050 (Stabilizer Overheads Compressors). The Package Vendor owns engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns whole-facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level acceptance. This deliverable provides the EPC Integrator's review-and-acceptance evidence that bridges the vendor production unit (DEL-050-04) and turnover (DEL-050-05) into the EPC anchor deliverables (DEL-050-01/02/03) so the package is verifiably ready for installation, tie-in, and operation.

Source: PACKAGE_REGISTER.csv row 81; DELIVERABLE_REGISTER.csv rows 450-455.

## Principles

1. **Source authority over convention.** Authority order is: locally accessible source materials > deliverable-local pointers (`_REFERENCES.md`, `_CONTEXT.md`) > decomposition narrative > prior drafts. Where the bid/RFQ source (`26020-01-PT-RFQ-12-005`) and the package requirements document (`26020-Package_Requirements.docx` heading 5) are not locally accessible, the locally accessible DBM (`4-25_Deepcut_DBM.md` §SEC-04) is the operative source slice.
2. **EPC Integrator does not author vendor truth.** This deliverable consumes vendor truth (DEL-050-04, DEL-050-05) and EPC anchors (DEL-050-01/02/03); it does not regenerate them.
3. **No reliance on TBC/TBD as if resolved.** Source slices carry numerous `TBC`/`TBD` items (e.g., MAWP for inter-stage suction/discharge, recycle valve fail position, SOC source flows for several inlets). Acceptance decisions on these items are conditional and require human ruling.
4. **Interface coverage is non-negotiable.** PKG-050 has 13 declared interface types and an explicit SOC process-interface map; acceptance must cover both.
5. **Scope split must be preserved.** Items declared "by others" in SOW-0176 (shipping, installation on piles, tie-in piping, electrical connections, mounting platform, stairs) must remain outside vendor acceptance scope, but the EPC Integrator must confirm those facility-side preparations align with the vendor package as shipped.

## Considerations

- **Modularization.** The package is shop-assembled, then disassembled into three pieces for shipment; self-framing buildings are erected in the field. Acceptance must consider field re-assembly tolerances, sealing, and re-test obligations after re-assembly.
- **Driver/electrical.** The "No Toshiba motors" exclusion is explicit in source; verify in motor datasheets and nameplates.
- **Coolers and dewpoint.** Stage 2 cooler discharge (87.78 °C) is close to its dewpoint (85.31 °C). The narrow margin is a documented review item; the acceptance log should record vendor calculation evidence and an EPC reviewer disposition.
- **Recycle and start-up.** Recycle valve fail position is `TBC` in source; start-up mode (equalized vs. normal-pressure) is also under evaluation. These open items should not be silently closed during acceptance.
- **Suction-scrubber sizing.** The 0.61 SG inlet-liquid-density assumption and the off-design capacity range are flagged for detailed engineering review; acceptance should record whether vendor calculations explicitly address these.
- **MAWP closure.** Only stage-1 suction (1,723 kPag) and stage-4 discharge (≥9,101 kPag) MAWPs are defined; remaining stage MAWPs are `TBC`. Acceptance cannot waive these.
- **Interface coordination.** SOC interfaces include 03-25 VRU and the pressurized caustic drain drum (V-6940-1) with `TBC` flow values; acceptance evidence must record what was confirmed and what remained open at handoff.

## Trade-offs

- **Conditional acceptance vs. release blocker.** Source-confirmed deviations (e.g., unresolved MAWPs) cannot be silently accepted. The trade-off is between deferring full acceptance until detailed engineering closes the open items, versus issuing a conditional acceptance package with explicit human-ruling notes that constrain downstream construction and turnover.
- **Coverage vs. depth.** Thirteen interface types and a multi-source SOC inlet manifold mean a coverage-first acceptance matrix risks shallow verification of safety-critical interfaces (relief/flare, fire & gas, MAWP). Reviewer time should weight relief/flare, electrical, and pressure-containment interfaces over informational items.
- **Three-piece field re-assembly.** Field re-assembly recovers shipping/handling constraints but introduces site QA load. Acceptance should record whether re-assembly inspection plans are in place.

## Examples

Examples from accessible sources:

- The stage 2 cooler-to-dewpoint margin (87.78 °C cooler outlet vs. 85.31 °C dewpoint) is the canonical example of an explicit "review during detailed engineering" item that must be tracked in the acceptance checklist rather than silently passed.
- The SOC source-capacity table lists Pressurized Caustic Drain Drum (V-6940-1), 03-25 VRU, and several side-streams with `TBC` flows; acceptance evidence should record which side-streams were dimensionally confirmed at FAT versus deferred to commissioning.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none observed) | No conflicts surfaced between locally accessible source slices, the decomposition row, and the deliverable-local context during P1/P2. The primary authoritative source slice (DBM-Deepcut §SEC-04 SOC Basis) is consistent with the SCOPE_LEDGER SOW-0173..0176 extract. The cited authoritative bid/RFQ source and package requirements document are not locally accessible; any divergence between those and the DBM remains TBD until those sources are made accessible. | DBM-Deepcut/4-25_Deepcut_DBM.md §SEC-04 | SCOPE_LEDGER.csv rows 174-177 | n/a | TBD | TBD |
