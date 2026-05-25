# Guidance: DEL-031-06_epc-vendor-package-review-and-acceptance

## Purpose

EPC Vendor Package Review and Acceptance exists so that the EPC Integrator can demonstrate that the Package Vendor's engineered equipment package for `PKG-031` (Transformer TXP-8500-1, 3 MVA, 13.8 kV / 600 V / 347 V) integrates into the facility scope before it is released to construction and turnover. The deliverable separates *vendor authoring* (engineering, design, vendor documentation, equipment supply) from *EPC acceptance* (review, integration verification, conditional/final disposition).

## Principles

- **Authoring vs. acceptance separation.** The vendor authors the package; the EPC Integrator reviews and accepts. Do not let acceptance language re-author vendor decisions; record comments and dispositions, not redesigns.
- **Source over restatement.** Acceptance criteria draw from the EPC Scope of Work (`DEL-031-01`), Package Datasheet (`DEL-031-02`), Construction Work Package (`DEL-031-03`), and the facility electrical design basis (DBM). Do not invent facility-level requirements during acceptance.
- **Interface-anchored review.** The seven `PKG-031` interface facts (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) drive the review structure.
- **Conservative TBD.** Where source material is silent (e.g., transformer construction type, impedance, BIL, tap-changer arrangement, installation location), preserve `TBD` rather than inferring vendor data.
- **Human-authored acceptance.** Per `K-AUTH-1`, only humans author binding acceptance records. Agent outputs may scaffold the checklist; the disposition signature is human.

## Considerations

- **Construction type unknown.** Source material discusses both large oil-filled transformers (CEC spacing, secondary containment review) and dry-type transformers (e.g., LACT 480 V transformer). TXP-8500-1's construction type is not stated in accessible source; spacing and containment requirements should be applied conditionally based on certified vendor data.
- **Grounding architecture.** The 600 V secondary requires 5 A continuous high-resistance grounding per the facility design basis. The 13.8 kV primary side grounding follows the medium-voltage facility architecture (low-resistance grounded). Acceptance must verify both ends are addressed.
- **Installation location.** Distribution transformers in this facility may be installed in electrical buildings or on outdoor pads. The specific installation site for TXP-8500-1 is not assigned in accessible source slices and should be confirmed through the Package Datasheet and Construction Work Package before acceptance.
- **Vendor document register reuse.** The vendor document register itself is owned by `DEL-031-05`. Acceptance reuses that register's identifiers rather than re-listing documents, and records EPC review status and comment closure against it.
- **Test evidence variability.** FAT scope for distribution transformers depends on the certified construction (routine tests vs. type tests vs. special tests). Reviewers should match received test reports to the contractually required scope rather than to a generic transformer test list.
- **Conditional acceptance discipline.** Conditional acceptance must be time-bounded, tied to specific remediation actions, and tracked through closure. Open conditions at facility turnover are out of process.

## Trade-offs

- **Breadth vs. depth.** Broad checklists may catch interface omissions but dilute attention to transformer-specific risks (impedance match, harmonic content from downstream loads, voltage regulation). A package-tailored checklist depth is preferred over generic completeness.
- **Early acceptance vs. evidence completeness.** Releasing the package early supports construction sequencing but risks downstream rework if test or document evidence arrives later. Conditional acceptance with strict closure tracking can balance the two.
- **Vendor scope respect vs. EPC integration needs.** EPC commentary should focus on integration boundaries (interfaces, tie-ins, constructability) rather than vendor engineering preferences inside the package boundary.

## Examples

- A vendor submittal omits the high-resistance grounding resistor connection detail on the 600 V secondary; EPC marks the Grounding / Bonding interface "conditional" with a comment citing the DBM grounding paragraph; resolution closes the condition before acceptance.
- A vendor general arrangement shows clearance interference with an area lighting pole; EPC marks Area / Exterior Lighting and Maintenance Access interfaces "conditional" pending revised GA; acceptance proceeds after revision.
- The vendor's FAT report omits one routine test required by the Package Datasheet; EPC issues a comment requiring the test or written waiver justification; acceptance disposition reflects the resolution.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-031-06-001 | Transformer construction type (oil-filled vs. dry-type) is not stated for TXP-8500-1; spacing and containment requirements differ accordingly. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph (oil-filled spacing) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, LACT paragraph (dry-type example) | Datasheet/Attributes (spacing basis); Specification/REQ-031-06-005; Procedure/Steps | PROPOSAL: defer construction-type-specific acceptance criteria to the Package Datasheet (`DEL-031-02`) and accepted vendor data; carry as `TBD` here. | TBD |
| CFL-031-06-002 | Installation location (electrical building vs. outdoor pad) is not assigned for TXP-8500-1 in accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph | Datasheet/Construction (installation location); Procedure/Prerequisites | PROPOSAL: defer to Construction Work Package (`DEL-031-03`); do not assume a location. | TBD |
