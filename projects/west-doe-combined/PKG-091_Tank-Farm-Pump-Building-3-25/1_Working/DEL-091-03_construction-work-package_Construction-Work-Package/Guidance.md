# Guidance — DEL-091-03 Construction Work Package

## Purpose

The Construction Work Package (CWP) exists because the **Tank Farm Pump Building 3-25** is a Package-Vendor-engineered Mechanical package whose execution risk concentrates at the **integration boundary** between the vendor-supplied building/skids and the surrounding 03-25 facility (tank farm piping, MCC feeds, DCS, foundations). Per the Gate 5 EPC anchor model (PROJECT_DECOMP §Gate 5; DEC-013), the EPC Integrator owns this boundary and must produce a CWP that lets construction proceed predictably and turn over cleanly to commissioning.

The deliverable's downstream role is to feed DEL-091-06 (EPC Vendor Package Review and Acceptance) and the facility-wide mechanical completion / commissioning workflow with auditable construction-interface evidence.

## Principles

1. **Treat the package as an integration job, not an installation job.** The pumps and building are vendor-engineered. Most CWP value comes from sequencing field tie-ins, not from re-engineering equipment.
2. **Respect the "By Others" cut.** SOW-0188 is explicit: DCS integration, foundations, and electrical supply to the MCC are out of EPC construction scope. The CWP must show — through interface points — exactly where those handoffs occur, but must not absorb their work.
3. **Plan for sour service throughout.** The package handles sour condensate and is adjacent to sour produced water; construction sequencing, materials handling, and personnel safety practices must reflect that, even where the source language does not call it out per step.
4. **Plan for -40 °C start-up.** Motor sizing assumes -40 °C start (SOW-0188); installation provisions that protect that assumption (insulation, heat tracing, dry-piping) are critical even when their scope split is `TBD`.
5. **Preserve seal-plan integrity.** API-682 Plan 14/52 (SOW-0187) is non-negotiable for the affected vertical inline centrifugal pumps; field changes must be vendor-endorsed.

## Considerations

- **Single source of equipment truth.** SOW-0187 is the authoritative pump list for this package. Tag-by-tag changes belong in the Package Vendor's DEL-091-04 deliverable, not in CWP markups.
- **Workface planning over narrative prose.** The "installation and tie-in workface plan" (anticipated artifact) is the operationally useful artifact; the rest of the CWP supports it.
- **Local control philosophy.** Each pump motor receives a local H-O-A or On-Off switch (SOW-0188); operators should not have to leave the building to bump a pump for line-up.
- **Cold construction season risk.** BC site, 673 m elevation, -40 °C start basis — schedule cold-weather mitigations in the workface plan rather than discovering them at hydrotest.
- **Interface with the Liquids Hub and tank farm.** The CWP is the on-site execution vehicle for SOW-0185 / SOW-0186 process tie-ins (water transfer to produced-water pipeline; sour condensate to sweetening feed). These tie-ins cross other packages and must be coordinated.

## Trade-offs

- **VFD vs. DOL starting (per pump).** SOW-0188 permits either. VFDs add inverter compatibility, harmonics, and footprint considerations at the MCC (by Others); DOL is simpler but harder on the network and pumps at the larger 150 kW water transfer duty. Decision: `TBD` (not resolved in source).
- **Heat tracing scope split between Vendor and EPC.** Vendor packages typically include internal heat tracing for module piping; site-installed tie-in piping is EPC scope. The exact cut for this package: `ASSUMPTION` it follows standard EPC practice; explicit split `TBD`.
- **Pre-commissioning of vendor-supplied seal flush / buffer systems.** API-682 Plan 14/52 systems include vendor-supplied components; whether seal flushing/conditioning is EPC pre-commissioning or vendor commissioning support is `TBD`.

## Examples

- *Tie-in coordination*: The two Water Transfer Pumps (P-9290/9293-2) draw from the produced-water tanks through a bag filter and discharge to the produced-water pipeline (SOW-0186). The CWP workface plan should sequence: tank nozzle isolation, bag filter housing install, suction header pressure test, discharge line tie-in to pipeline pig launcher or header (`TBD`), then loop check from MCC.
- *Equipment grouping*: The vertical inline centrifugal pumps (P-9210/9211/9215/9216/9220/9221-2) share API-682 Plan 14/52 seal plans — group their seal-plan installation verification into a single inspection front for efficiency.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none captured at this pass) | — | — | — | — | — | — |

No source–source contradictions were observed in the accessible slices during this pass. The Conflict Table is retained for human ruling on future passes.
