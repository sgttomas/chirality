# Guidance — DEL-053-04 Vendor Engineered Equipment Package (Flare KO Drum, Cryo)

> Directional guidance for vendor engineering and EPC integration review of the package. Rationale draws from the project decomposition and accessible source slices.

## Purpose

The Vendor Engineered Equipment Package is the Package Vendor's production unit for engineering, design, fabrication/supply, and delivery of the physical Flare KO Drum (Cryo) equipment package, anchored by the EPC Scope of Work (DEL-053-01) and Package Datasheet (DEL-053-02). It is the realized equipment that EPC review and acceptance (DEL-053-06) judges, and is the technical basis around which vendor documentation (DEL-053-05) and the EPC construction work package (DEL-053-03) are organized. [DELIVERABLE_REGISTER DEL-053-04; PACKAGE_REGISTER row 53]

## Principles

- **Source-authoritative interfaces.** Vendor decisions affecting interfaces (inlet/outlet flange ratings, electrical terminations, structural attachments) must trace to the EPC Package Datasheet (DEL-053-02). Decomposition prose summarizes; DEL-053-02 governs.
- **Cryogenic service first.** Drum and heater must be engineered for the documented service (PSV reliefs from cryogenic and mol-sieve-dehydrated systems relieving below -45.5 degC). [DBM-Deepcut "Cryogenic flare" row]
- **Single-package integrity.** Drum V-4110-1 and immersion heater H-4112-1 are delivered as one engineered, tested, and documented package. [SCOPE_LEDGER SOW-0068, SOW-0069]
- **Non-sour treatment per project brief.** Service is treated as non-sour unless DEL-053-02 supersedes. [SCOPE_LEDGER SOW-0070]
- **Vendor scope is bounded.** Facility integration, tie-ins, constructability, and procurement/construction coordination remain EPC Integrator scope. [PACKAGE_REGISTER row 53]

## Considerations

- **MDMT and impact testing.** Below -45.5 degC service requires MOC selection (typical candidates: low-temperature austenitic stainless, LTCS, or specialty alloys) with appropriate impact-test pedigree. ASSUMPTION: 304SS continuity from the relief header is one defensible candidate for wetted parts; the binding choice is vendor's and must be evidenced.
- **Immersion heater integration.** Heater watt density, sheath material, thermowell location, and over-temperature protection must be coordinated with drum internals and liquid hold-up volume to avoid hot-spotting and to preserve cryogenic relief integrity. Specific values: TBD.
- **No heat tracing on cryogenic flare header.** Project DBM does not heat-trace cryogenic flare headers outside buildings (water not expected). Vendor insulation/heat-trace specifications for the package itself must align with this policy. [DBM-Deepcut flare section]
- **Header geometry.** Inlet from 610 mm (24 in) 304SS cryogenic relief header; outlet combines with HP flare downstream of both KO drums before HP/cryo stack. Nozzle sizing and orientation should respect this routing. [DBM-Deepcut flare equipment / header tables]
- **Documentation pull-through.** DEL-053-05 (Vendor Document Turnover) consumes vendor outputs; DEL-053-06 (EPC Review and Acceptance) judges them. Plan deliverables and revisions to support both downstream activities.

## Trade-offs

- **MOC vs. cost vs. lead time.** Higher-pedigree cryogenic alloys reduce risk but extend delivery; selection should be optimized against the EPC schedule and DEL-053-02 design conditions. [TBD pending datasheet]
- **Package extent vs. interface count.** Including more auxiliaries inside the vendor package reduces field tie-in count but increases vendor scope and cost; the package boundary is set by DEL-053-02 and EPC Integrator direction.
- **FAT extent.** Broader factory acceptance testing reduces field commissioning risk but adds cost/schedule; the right level is informed by the EPC review and acceptance criteria (DEL-053-06).

## Examples

- **Cryogenic-service drum reference**: V-4110-1 is paralleled by the HP flare KO drum V-4100-1 (with pump P-4100-1) in the project flare system architecture; differences in service temperature drive the cryogenic-specific MOC and heater design distinct from the HP KO drum. [DBM-Deepcut "Cryogenic flare" / "High-pressure flare" rows]
- **Header routing example**: 610 mm cryogenic header into V-4110-1, downstream combination with HP into a 762 mm common HP/cryo header upstream of the common stack. [DBM-Deepcut flare header table]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none identified during P1/P2) | — | — | — | — | — | — |

No source/source or source/decomposition conflicts surfaced during this pass. Any conflicts arising during DEL-053-02 issuance or vendor engineering should be added here for human ruling.
