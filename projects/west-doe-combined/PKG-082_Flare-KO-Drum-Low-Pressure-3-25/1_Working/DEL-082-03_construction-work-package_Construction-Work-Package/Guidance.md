# Guidance — DEL-082-03 Construction Work Package (LP Flare KO Drum, 3-25)

## Purpose

This deliverable exists to give the EPC Integrator a single mandatory Gate-5 anchor describing how PKG-082 (LP Flare KO Drum, tags V-3900-2 / P-3900-2) is physically installed, inspected, turned over, and tied into the 03-25 facility and the shared HP/Cryo + LP dual flare system. It is the construction-execution counterpart to upstream process and mechanical design work for the LP flare relief path (SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SectionRef: SEC-07 Flare and Blowdown).

## Principles

- **Source authority over convention.** The 3-25 DBM SEC-07 and SEC-09 govern tag identity, sparing, header size, and service routing. Generic CWP templates do not override the DBM.
- **Shared-interface awareness.** The HP/Cryo and LP dual flare stack and incinerator are shared 03-25/04-25 systems (DBM SEC-01 line 56). Construction sequence must respect the interface allocation, which is itself an open item in the current source.
- **Sour-service discipline.** Isolation, vent, drain segregation, and material selection for sour service are not optional embellishments; they are derived from DBM SEC-09 Isolation Philosophy (line 607).
- **Staggered blowdown is a construction-affecting constraint.** Pipe routing, valve sequencing, and control hook-up must support the staggered blowdown basis (DBM SEC-07 line 501).
- **TBD over invention.** Where source values for vessel dimensions, MAWP, NDE extents, or stack OD are not accessible, mark TBD and surface to design — do not back-fill from convention.

## Considerations

- The LP flare KO drum collects liquids from TEG regeneration, VRU, and compressor seal-pot services; construction sequence should align with the readiness of those three upstream sub-systems so that final tie-in does not block earlier mechanical completion of the KO drum scope (DBM SEC-07 line 499).
- The LP relief header (508 mm) ties into the shared LP flare stack whose OD remains TBD in the current source basis; allow margin in pipe rack and stack-base interface design and sequencing.
- Foundations design depends on a final geotechnical report and vibration/anchorage checks (DBM SEC-09 line 700); construction must not start vessel and pump setting before foundation acceptance.
- LV standby power and emergency power configuration is under SCA-001 revision (DBM SEC-07 line 505); confirm electrical interface for P-3900-2 against the current revision before electrical hook-up.

## Trade-offs

- **Fabricate-and-set vs. modular delivery.** The DBM does not state whether the LP KO drum is shop-modularized; main inlet compressors are explicitly modular (DBM SEC-05 line 294) but no parallel statement appears for V-3900-2. Treat as TBD; default to field-set unless vendor data resolves otherwise.
- **Hydrotest medium (water) vs. pneumatic test.** Sour-service material and freezing risk near Dawson Creek climate may push toward hydrotest with corrosion inhibitor; final selection is TBD pending engineering specification.
- **Pre-fabrication of LP relief header sections.** Reduces field welding in sour service but increases handling and lift complexity; trade-off resolution belongs in the workface plan.

## Examples

- LP relief header service inventory (TEG regeneration, VRU, compressor seal-pot) is taken verbatim from DBM SEC-07 line 499 — this is the canonical example of source-grounded routing for this CWP.
- Sparing example: LP flare KO drum transfer pump is 1 x 100 percent (DBM SEC-09 line 584). Construction shall not install a second pump on the assumption of 2 x 100 percent.

## Conflict Table (for human ruling)

| ID | Conflict | Source A | Source B | Impacted | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | LP flare stack OD is required to size the relief tie-in flange and stack-base structure, but DBM SEC-07 line 499 carries OD as TBD. | DBM SEC-07 line 499 | — | Datasheet Attributes, Specification R-11 | PROPOSAL: hold construction of the flare stack base and final tie-in until OD is issued in detailed design. | TBD |
| C-02 | Shared HP/Cryo + LP dual flare stack ownership/allocation is an open interface item (DBM SEC-01 line 56). Construction interface boundary between 03-25 (this CWP) and 04-25 is not fully resolved. | DBM SEC-01 line 56 | DBM SEC-07 line 497 | Specification Scope (excluded vs included) | PROPOSAL: treat the 03-25 LP relief header up to the stack-base flange as in scope; treat the stack column as out of scope pending interface ruling. | TBD |
| C-03 | Final blowdown sequencing is governed by W242510-PRC-REP-000003-001 (DBM SEC-07 line 501) which is not locally accessible. | DBM SEC-07 line 501 | — | Specification R-04, R-12 | PROPOSAL: hold final SIS/BPCS configuration and pre-commissioning blowdown trials until that document is accessible. | TBD |
