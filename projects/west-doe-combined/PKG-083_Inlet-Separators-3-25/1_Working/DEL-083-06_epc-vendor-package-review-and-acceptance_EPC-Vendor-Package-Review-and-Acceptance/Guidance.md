# Guidance: EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists so that the EPC Integrator can demonstrate, with evidence, that the Inlet Separators vendor package (PKG-083) has been reviewed against the EPC Scope of Work, the Package Datasheet, and the Construction Work Package, and that it is accepted into the facility integration boundary. It is an additional Gate 5 deliverable framed as EPC-integrator review and acceptance evidence.

## Principles

- **Vendor owns the package; EPC owns the integration.** Acceptance evidence must clearly preserve that boundary: package engineering, design, vendor documentation, and physical equipment are the vendor's responsibility; interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration are the EPC Integrator's responsibility. (Source: PACKAGE_REGISTER.csv, PKG-083 responsibility model.)
- **Acceptance is evidence-bearing, not declarative.** Each acceptance statement must point to a vendor document, a test/inspection record, or a checklist line that supports it. Unsupported claims are recorded as `TBD`, not asserted.
- **Source fidelity beats convention.** When reviewing vendor submissions, compare against the actual facility design basis (3-25 DBM source) and the formal package requirements (26020-Package_Requirements.docx) rather than against generic separator-package convention.
- **TBD/TBC items are tracked, not silently resolved.** The current design basis carries several open items (e.g., normal high pressure TBC; building extent TBD; downstream methanol disposition TBD; inlet temperature reconciliation). Each must be carried into the acceptance log with disposition or carry-forward notation.

## Considerations

- **Two identical packages.** V-1600-2 and V-1700-2 are designed to be identical, each sized for 50% of facility capacity. Review and acceptance should be performed against a single specification with per-tag verification, and any unit-to-unit deviation must be flagged.
- **Heated building scope is a known soft boundary.** Instrumentation and one end of each package are enclosed in a heated self-framing building, but the exact building extent is TBD by vendor design. Acceptance should not lock in this scope before vendor design is firm.
- **Cold-climate basis must be tested in vendor design.** The -40 deg C ambient minimum is the governing site basis and is easy to overlook in vendor catalog selections (valves, instruments, gaskets, building HVAC); acceptance review should explicitly test for cold-climate suitability.
- **Sour-service materials and coatings.** Devchem 253 internal coating, sour-service piping/vessel materials, and absence of piping coating under the current basis are all specifications that must be confirmed in vendor materials documentation, not assumed.
- **Interfaces are the integration risk surface.** Every applicable interface type listed in PACKAGE_REGISTER (process piping, utility piping, relief/flare/vent, drain/containment, EHT, grounding/bonding, area/exterior lighting, I&C/control cabling, fire & gas/safety systems, maintenance access, structural/foundations/supports) is a place where vendor package and facility design can disagree. Each requires explicit acceptance.
- **Handoff coupling with DEL-083-05.** The Vendor Document Turnover Package (DEL-083-05) provides the document index that this acceptance set must reconcile against; do not accept the package before the turnover index is congruent with the review log.

## Trade-offs

- **Depth of FAT witnessing vs. schedule.** The current accessible sources do not specify the depth of EPC FAT witnessing required. A schedule-driven choice to accept vendor FAT reports without witnessing trades cost/schedule for residual integration risk; this trade-off should be made explicitly and recorded.
- **Open-item carry-forward vs. acceptance gating.** Several TBC items in the design basis (e.g., separator scrubber K-factor, normal high pressure, building extent) can either gate acceptance or be carried forward into commissioning. The default should be to carry forward only items that do not affect physical hardware, and to gate acceptance on items that would require equipment rework.
- **Acceptance granularity.** A single combined acceptance for both V-1600-2 and V-1700-2 simplifies documentation but risks masking unit-specific deviations; per-tag acceptance is more defensible but heavier. The current source set does not mandate one approach.

## Examples

The accessible source set does not provide worked examples of prior EPC acceptance logs for inlet separator packages on this project. Examples should be drawn from the eventual issued versions of DEL-083-02 (Package Datasheet) and DEL-083-04 (Vendor Engineered Equipment Package) once available. (Status: TBD.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-083-06-01 | Inlet design temperature: current feed data carries 8.3 deg C, while "some downstream excerpts require confirmation; detailed design shall reconcile the inlet temperature basis before issuing final equipment datasheets." | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation (8.3 deg C) | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation (downstream excerpts, unspecified) | Datasheet Conditions; Specification REQ-083-06-03/06 | PROPOSAL: hold acceptance on equipment datasheets until reconciled inlet temperature is confirmed by detailed engineering. | TBD |
| CONF-083-06-02 | Inlet-separator sizing model: current basis is two identical 50%-capacity packages, but "older 2 x 100 percent table language requires reconciliation." | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation (2 x 50%) | 3-25_Comp_and_Liquids_DBM.md, Mechanical Equipment Summary (older 2 x 100% table) | Datasheet Conditions; Specification REQ-083-06-03 | PROPOSAL: 2 x 50% basis governs; older 2 x 100% language to be marked superseded in acceptance log. | TBD |
| CONF-083-06-03 | Package requirements detail: 26020-Package_Requirements.docx package heading 36 is cited as authoritative for the vendor package scope, but is not locally readable as text in the current workspace. | DELIVERABLE_REGISTER.csv, DEL-083-06 (cites .docx) | Local workspace (no text-accessible rendition) | Specification Standards; Verification | PROPOSAL: extract package heading 36 to a locally readable rendition before final acceptance review. | TBD |
