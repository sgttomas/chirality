# Guidance: EPC Vendor Package Review and Acceptance

## Purpose

This deliverable gives the EPC Integrator a controlled acceptance record for the PKG-012 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package. It exists to show that vendor-owned engineering, documentation, equipment, and test/inspection evidence have been reviewed for facility integration and handoff readiness.

Sources: _CONTEXT.md; DELIVERABLE_REGISTER.csv row DEL-012-06; PACKAGE_REGISTER.csv row PKG-012.

## Principles

- Preserve the vendor/EPC responsibility split. The EPC Integrator reviews and accepts for integration; it does not become the owner of vendor package engineering or vendor design. Source: PACKAGE_REGISTER.csv row PKG-012; SCOPE_LEDGER.csv row SOW-0013.
- Treat accepted Gate 7 registers as the governing decomposition basis for this Phase 2.2 draft. Do not replace missing source detail with generic acceptance criteria.
- Use the artifact register as the minimum evidence scaffold: review log, acceptance/turnover checklist, and factory/shop test and inspection evidence. Source: ARTIFACT_REGISTER.csv rows for DEL-012-06.
- Make interface acceptance explicit for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. Source: INTERFACE_REGISTER.csv rows for PKG-012.
- Keep open items visible. Missing vendor evidence, unresolved interface checks, and absent detailed acceptance criteria should remain TBD or open until supported by source material.

## Considerations

The accepted decomposition associates this deliverable with objectives for facility scope, vendor package execution, electrical integration, civil/structural support, safety/compliance carry-through, and handoff readiness. These objectives are useful for review framing, but they do not create detailed acceptance criteria by themselves.

Package-specific exclusions, detailed code clauses, inspection criteria, and acceptance thresholds are not present in the deliverable-local copied sources. They should not be invented in the review package.

## Trade-offs

| Topic | Direction |
|---|---|
| Evidence completeness vs. schedule | Accept only what evidence supports; carry missing items as open/TBD rather than treating absence as acceptance. |
| EPC integration review vs. vendor design ownership | EPC review should verify integration readiness without rewriting or assuming ownership of vendor design deliverables. |
| Gate 7 basis vs. unavailable detailed sources | Use Gate 7 for accepted identity, responsibility, artifacts, objectives, and interfaces; keep detailed source-dependent criteria TBD. |
| Interface closure vs. open-item transparency | Interfaces may be conditionally acceptable only when open items are identified and routed to accountable owners. |

## Examples

Example acceptance checklist rows should include:

- Vendor document review log complete: accepted / accepted with comments / rejected / open / TBD.
- Electrical Power interface reviewed against EPC integration needs: accepted / open / TBD.
- Grounding / Bonding interface reviewed: accepted / open / TBD.
- Maintenance Access interface reviewed: accepted / open / TBD.
- Structural / Foundations / Supports interface reviewed: accepted / open / TBD.
- Factory/shop test and inspection evidence received and reviewed: accepted / open / TBD.
- Turnover evidence ready for facility handoff: accepted / open / TBD.

These are ASSUMPTION examples derived from the accepted artifact and interface categories. Final checklist wording should be confirmed against project/vendor source slices.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HR-012-06-001 | Detailed acceptance criteria are required for production use, but no deliverable-specific source slices were copied into the assigned folder. | _REFERENCES.md, Missing / Deferred References | DELIVERABLE_REGISTER.csv row DEL-012-06 and ARTIFACT_REGISTER.csv rows 221-223 identify expected evidence only | Specification Requirements; Procedure Steps; checklist content | Use Gate 7 for evidence structure and keep detailed criteria TBD until source slices are supplied. | TBD |
