# Guidance — DEL-049-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists because PKG-049 is a vendor-engineered package: the Package Vendor owns engineering, design, and equipment supply, while the EPC Integrator owns facility integration (SOW-0169). The EPC Integrator therefore needs a structured review and acceptance discipline to ensure the vendor's package, as delivered, meets the EPC Scope of Work, the Package Datasheet (DEL-049-02), and the Construction Work Package (DEL-049-03), and is ready for facility integration and commissioning.

## Principles

- **Respect vendor engineering authority.** Reviews comment on conformance and interface; they do not redesign the vendor's equipment.
- **Source-traceable acceptance.** Every accepted attribute traces to a numbered SOW item, an artifact register entry, or an explicit vendor submittal.
- **Interface-first.** EPC by-others scope (SOW-0172: shipping, piles, tie-in piping, electrical, platform/stairs) is the highest-risk seam between vendor and EPC scope; review there first.
- **Evidence over assertion.** Acceptance is granted on the basis of vendor documentation, test/inspection records, and turnover checklists, not on verbal assurance.

## Considerations

- **Fixed-speed, no-turndown design** (SOW-0172) means operational flexibility is provided by upstream/downstream systems, not by the booster. Acceptance review should confirm no implicit turndown assumptions were introduced by the vendor.
- **API 661 air cooler and NEMA MG 1 motor** (SOW-0171, SOW-0172): the SOW names the standards but the clause-level text is not locally accessible in this run; reviewers should request the vendor's standard-compliance declarations and the relevant code excerpts when verifying.
- **0.61 SG inlet liquid density assumption** (SOW-0172) is a stated design basis, not a measurement. If actual feed conditions differ at startup, the scrubber sizing assumption should be re-evaluated.
- **140 MMSCFD design vs. process function** (SOW-0170, SOW-0172): the design margin between the 140 MMSCFD design point and the named process duty (sweet sales gas from booster header to coalescer/splitter) should be confirmed in vendor performance documentation.
- **Filter coalescer rating** (SOW-0171, 100 MMSCFD): the coalescer flow rating is lower than the compressor design throughput (140 MMSCFD). Reviewers should confirm intended service alignment with the vendor. ASSUMPTION: this is intentional (different service points along the train); CONFLICT candidate if not resolved.

## Trade-offs

- **Depth of review vs. schedule.** Deeper document review reduces integration risk but extends review cycles. The acceptance checklist (ART-6439AA1852) should encode the minimum sufficient review depth per topic.
- **Witness vs. review of FAT.** Witnessing FAT in person yields stronger evidence than document review alone; cost/travel must be weighed against the criticality of the equipment.
- **Comment vs. hold.** Reviewers should distinguish informational comments from hold points that block acceptance; uniform treatment dilutes both.

## Examples

- Example accepted item: vendor submits Ariel KBX/X compressor datasheet with all cylinders dedicated, matching SOW-0171; reviewer records acceptance against REQ-049-06-02.
- Example hold: vendor proposes a 6-pole motor at variable speed; reviewer issues a hold against REQ-049-06-04 (does not match 8-pole, fixed-speed, 891 rpm requirement from SOW-0172).
- Example interface check: vendor scope drawing shows tie-in piping inside vendor terminal point; reviewer flags conflict against SOW-0172 by-others list (REQ-049-06-08).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-049-06-01 | Filter coalescer rated 100 MMSCFD while compressor package design throughput is 140 MMSCFD; service location and intended duty alignment is not stated in accessible sources | SOW-0171 (Major included equipment) | SOW-0172 (Capacity/design throughput) | Datasheet/Attributes; Spec/REQ-049-06-02; Guidance/Considerations | PROPOSAL: treat the 100 MMSCFD coalescer rating as intentional for a downstream service point; require vendor to confirm in writing | TBD |
