# Guidance: DEL-085-06 — EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists so the EPC Integrator can take controlled, evidence-based acceptance of the High Pressure flare stack vendor package (PKG-085), confirm it integrates with the shared 03-25/04-25 flare system, and hand it over to operations with traceable closure of all material vendor and interface items (`_CONTEXT.md`; decomposition entry per GATE-07 PROJECT_DECOMP snapshot).

It is the closure point where the upstream SOW (`DEL-085-01`), package datasheet (`DEL-085-02`), construction work package (`DEL-085-03`), vendor-engineered equipment (`DEL-085-04`), and vendor document turnover (`DEL-085-05`) converge into a single acceptance record.

## Principles

1. **Acceptance is evidence-based, not narrative.** Each requirement in `Specification.md` must be answered by a tangible artifact (review log entry, inspection record, vendor certification, interface ruling). Narrative summaries are not acceptance evidence.
2. **Shared interfaces are first-class.** The HP/Cryo + LP stack is explicitly a shared 03-25/04-25 interface system (DBM L56, L547). EPC acceptance must reflect the current allocation ruling rather than assume a default split.
3. **Source authority over decomposition prose.** The DBM source slices govern stack geometry and header sizing values (DBM L497, L499). Decomposition narrative provides scope and routing, not normative values.
4. **Open items remain open.** Items where source explicitly says TBD (LP stack OD, final flare studies, permit-final emissions) MUST be carried as open acceptance conditions, not silently closed.
5. **Cold-climate site basis is governing.** -40 °C minimum ambient governs unless a stricter package basis applies (DBM L96, L145). Acceptance evidence must demonstrate qualification across that envelope.

## Considerations

- **Vendor scope boundary.** The vendor delivers a package; the EPC Integrator delivers integration into the facility. Acceptance verifies the latter without re-doing the former. Do not relitigate vendor calculation methodology; verify acceptance criteria are met.
- **Shared service split risk.** DBM L56 marks the 03-25/04-25 HP vs LP service split as an open interface item. Acceptance without an interface ruling exposes both facilities to allocation disputes during commissioning. Treat R-04 as a gating requirement.
- **KO drum scope ambiguity.** HP KO drums V-4100-2, V-4150-2 and LP KO drum V-3900-2 sit upstream of the stack but may be scoped to compressor or tank-farm packages rather than the flare package (DBM L497, L499). The review must confirm which equipment is in PKG-085 vendor scope vs other packages before applying R-07.
- **Flare study dependency.** DBM L548 and L555 state that final flare studies and permit-final emissions are required and not yet complete. Acceptance for *construction turnover* is possible; acceptance for *permit/operations final* is conditional on those studies.
- **Foundation reconciliation.** Vendor loads must be reconciled against the foundation actually built (DBM L700). Foundation acceptance is a structural sign-off, not a vendor sign-off, and the EPC owns the reconciliation.

## Trade-offs

| Trade-off | Direction | Rationale |
|---|---|---|
| Accept with open interface items vs. block until ruling | Prefer block on R-04; document and track all other open items | Interface ambiguity has commissioning-time cost; geometric/test items can be closed in punchlists |
| Detailed test re-witness vs. document review of vendor records | Document review with sample re-witness | Vendor records are primary; EPC re-witness adds confidence on safety-critical functions (pilot/ignition) |
| Permit-final emissions inclusion | Defer to flare-study completion | Source explicitly states current basis is not permit-final (DBM L555) |

## Examples

Examples of vendor package-specific acceptance criteria (e.g., pilot reliability targets, smokeless turndown, radiation contour limits) are not derivable from accessible sources. These should be drawn from `_Sources/26020-Package_Requirements.docx` heading 38 once the relevant text slice is extracted (currently **location TBD**, binary source not text-accessible in this run). TBD.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | LP stack OD value | DBM `3-25_Comp_and_Liquids_DBM.md` L499 ("LP stack OD remains TBD") | None (no second source accessible) | Datasheet Attributes; Spec R-02 | Carry as TBD pending vendor data or interface ruling | TBD |
| C-02 | 03-25 / 04-25 HP vs LP service split | DBM L56 ("open interface items") | DBM L547 ("requires current source ruling") | Spec R-04; Guidance Considerations | Carry as gating open item; do not assume a split | TBD |
| C-03 | Package-specific clause-level requirements | `_Sources/26020-Package_Requirements.docx` heading 38 (text not accessible) | DBM L497-L499 (system-level only) | Spec R-01, R-08; Standards table | Convert `location TBD` markers when source slice extracted | TBD |
| C-04 | Permit-final emissions and flare loads | DBM L548, L555 (not permit-final) | None | Spec R-09; Guidance Considerations | Acceptance for construction turnover only; permit-final acceptance conditional on final flare studies | TBD |
