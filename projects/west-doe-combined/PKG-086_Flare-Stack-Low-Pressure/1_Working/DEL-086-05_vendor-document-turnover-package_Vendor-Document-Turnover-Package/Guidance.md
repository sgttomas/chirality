# Guidance: DEL-086-05_vendor-document-turnover-package — Vendor Document Turnover Package

> Directional guidance for assembling, reviewing, and turning over the Package Vendor's document set for PKG-086 (Flare Stack — Low Pressure). Rationale is drawn from accessible sources; items without a source anchor are marked `ASSUMPTION` or `TBD`.

## Purpose

This deliverable exists because the Package Vendor — not the EPC Integrator — owns the source-of-truth engineering documentation for the LP flare stack package, while the EPC Integrator owns facility integration. Without a controlled vendor document register, source-required documentation set, and turnover record, the EPC Integrator and end client cannot verify that the as-supplied package meets the contracted scope (SOW-0091..SOW-0094) and the supported objectives (OBJ-002, OBJ-004..OBJ-010). The deliverable is the documentary substrate that DEL-086-06 (EPC Vendor Package Review and Acceptance) consumes.

## Principles

1. **Vendor-owned, EPC-reviewed.** Vendor authorship and content responsibility; EPC review for interface, integration, and contract scope conformance (`DELIVERABLE_REGISTER.csv` ResponsibleParty).
2. **Source fidelity.** Anything required by `26020-Package_Requirements.docx` package heading 39 must appear; the explicit required list is `TBD` until the source slice is copied locally.
3. **Single document register.** One master register indexes every document. Submittals exist only by reference into the register (ASSUMPTION on registry-as-spine pattern; `location TBD`).
4. **Turnover is evidence, not formality.** Transmittals carry revision state, hold items, and acceptance signatures; absence of any is a turnover defect.
5. **Carry through regulatory anchors.** OGAOM spacing and OGPFR radiation flux criteria, identified in the DBM, must be visible in the vendor calculations and submittals so they can be verified at acceptance.

## Considerations

- **Source coverage gap.** The 26020 package-requirements source is `.docx`; its heading-39 contents have not been copied locally as a markdown slice. Until that slice is brought in, the explicit list of source-required vendor documents remains `TBD` and several requirements (R-086-05-02 in particular) cannot be closed.
- **Sour-service designation.** PKG-086 sour-service applicability is `ASSUMPTION: likely applies` based on OBJ-009. Vendor material selection statements (NACE/ISO 15156 conformance) should be procured even under assumption, then re-validated when the designation is confirmed.
- **Smokeless basis is partly TBC.** The DBM states Ringelmann 1 at approximately 5% (TBC) of emergency design case flare loads. Vendor sizing of the air-assist blower must acknowledge the TBC and surface a proposal.
- **Pilot and purge gas TBC.** DBM line 1892 lists "LP flare stack pilot and purge gas: TBC". Vendor submittals should close this rather than mirror the TBC.
- **Shared stack arrangement.** DBM identifies the LP element as a piggy-back on the common HP/cryo stack; vendor documents must reflect the shared stack arrangement and not assume a standalone stack.
- **Integration with DEL-086-06.** The EPC review log lives in DEL-086-06. Vendor document numbering and the register schema should be compatible with that log structure (`location TBD` for exact convention).

## Trade-offs

- **Document depth vs. submittal cadence.** A heavier upfront submittal package reduces review iterations but slows initial schedule; a lean initial submittal accelerates start but increases hold items at turnover. The PKG-086 contracted convention is `TBD` — `location TBD`.
- **Single transmittal vs. progressive turnover.** Single-event turnover simplifies records but concentrates risk at the end; progressive turnover spreads review load. Choice is `TBD` pending source basis.
- **Vendor calculations vs. EPC re-derivation.** Accepting vendor radiation/dispersion calculations reduces EPC re-work but transfers verification risk; EPC re-derivation increases workload but allows independent confirmation. The DBM's note that OGPFR is an external regulatory reference suggests at least independent regulatory-check is warranted.

## Examples

No locally accessible example vendor-document register or turnover package was identified for this PKG; explicit examples are deferred to `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none open) | The accessible DBM source and decomposition registers are mutually consistent for PKG-086 at the level of detail used here. The principal gap is missing source-slice access to 26020 heading 39; this is a coverage gap, not a conflict. | — | — | — | — | — |
