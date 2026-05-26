# Guidance — Construction Work Package (DEL-084-03)

Pass: P1_P2 (initial draft + cross-reference sweep)

## Purpose

This deliverable exists because the PKG-084 Fuel Gas Skid is a vendor-supplied package whose value depends on disciplined site installation and a clean handover to operations. The CWP gives the EPC Integrator a single, auditable basis for sequencing the physical work, coordinating cross-discipline tie-ins, controlling field risk, and producing the records needed for mechanical completion and operations turnover (source: DELIVERABLE_REGISTER row 326).

## Principles

- **Skid-edge discipline.** Treat the skid boundary as the canonical scope split between vendor-supplied package and field construction. All hookups, isolation, drains, vents, and instrument loops are listed and walked down at that boundary (source: `3-25_Comp_and_Liquids_DBM.md` lines 605, 619).
- **Shared-utility awareness.** Fuel gas at the West Doe complex is a shared 03-25 / 04-25 utility; installation and tie-in plans must recognize that the fuel-gas building is at or associated with 04-25 and that disturbances affect both facilities (source: `3-25_Comp_and_Liquids_DBM.md` lines 452, 456, 706).
- **Source-grounded basis before issue for construction.** The CWP shall not be issued for construction ahead of the accepted plot plan, equipment list, miscellaneous facilities list, and applicable hazard reviews (source: `3-25_Comp_and_Liquids_DBM.md` lines 467-469, 661).
- **No silent placeholders.** Construction values derived from non-accepted basis (e.g., placeholder geotechnical assumptions, TBC flow values) shall be explicitly flagged in the CWP until superseded (source: `3-25_Comp_and_Liquids_DBM.md` lines 141, 463).

## Considerations

- **Cold-weather execution.** -40 deg C ambient basis affects sequencing (winter pours, hydrotest planning, insulation/heat-tracing close-out) (source: `3-25_Comp_and_Liquids_DBM.md` line 696).
- **Mercaptan/purge hazard.** Sweet-gas purge from fuel gas carries a methyl-mercaptan exposure profile; field construction and commissioning must follow the formal hazard review outcome (source: `3-25_Comp_and_Liquids_DBM.md` lines 467-469).
- **Cross-facility outages.** Tie-ins at 04-25 may require coordinated outage planning with the 04-25 operator/owner (ASSUMPTION based on shared-utility nature; explicit outage authority TBD).
- **Modularization legacy.** Process facility precedent is to ship modules in pieces and reassemble in-field; the skid CWP should expect comparable handling for any large skid sub-assemblies (source: `3-25_Comp_and_Liquids_DBM.md` line 294).
- **Vendor package interface.** Vendor documentation expectations (datasheets, cause-and-effect, shipped-loose lists) are inputs the CWP must consume rather than create (source: `3-25_Comp_and_Liquids_DBM.md` line 617).

## Trade-offs

- **Pre-set vs. set-in-place tie-ins.** Pre-setting field piping reduces critical-path field hours but increases re-work risk if the skid arrives with deviations; the CWP should document which strategy is chosen and why (rationale TBD pending detailed schedule basis).
- **Construction-led vs. commissioning-led test boundaries.** Where construction completes loop checks vs. where commissioning takes over is a contractual call (ASSUMPTION: EPC Integrator owns through mechanical completion; explicit split TBD).
- **Workface plan granularity.** Higher granularity improves predictability but increases administrative load; the CWP should choose a granularity matched to package complexity and risk (rationale TBD).

## Examples

- Examples specific to the fuel gas skid CWP are not yet sourced. Skid-specific examples will be added when `26020-Package_Requirements.docx` heading 37 is extracted or when prior West Doe CWP precedents are referenced. Until then, examples are intentionally omitted rather than fabricated. (location TBD)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Emergency buyback fuel gas: required or not | `3-25_Comp_and_Liquids_DBM.md` line 465 citing W242510 (not required) | `3-25_Comp_and_Liquids_DBM.md` line 465 citing Process_DBM_fixed (included in 04-25 utility package) | Specification R-12; Datasheet "Emergency buyback fuel gas"; Procedure tie-in list | Defer until human ruling; CWP carries the item as TBD with explicit flag | TBD |
| C-2 | Skid-specific clause-level requirements (`26020-Package_Requirements.docx` heading 37) | Decomposition row 326 cites this source | Source is binary .docx and not locally accessible as text | All four documents (skid-specific requirements remain TBD) | Extract the source slice (e.g., via docx2md tool) before final issue for construction | TBD |
