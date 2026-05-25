# Guidance: DEL-013-06_epc-vendor-package-review-and-acceptance

## Purpose

Explain how the EPC Integrator should perform vendor package review and acceptance for `PKG-013` (100A DC UNINTERUPTIBLE POWER SUPPLY) without overstating what the accessible source set actually authorizes, and how to record acceptance evidence that downstream activities (construction handover, turnover to operations) can rely upon.

## Principles

- **Authority hierarchy is upstream-fixed.** The accepted EPC Scope of Work, the `DEL-013-02` Package Datasheet, and the Construction Work Package are the acceptance basis. The vendor package is the subject of review, not its own authority.
- **Responsibility split is non-negotiable.** Per `PACKAGE_REGISTER.csv` row `PKG-013`, the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration. Review comments shall not redesign the vendor package or accept vendor scope drift into EPC scope.
- **Source gaps are not silently filled.** Where the EPC Scope of Work, Construction Work Package, or vendor data is not accessible, the acceptance criteria are recorded as `TBD` with the missing reference noted — not invented.
- **Interface evidence is the minimum acceptance unit.** Each of the four declared package interfaces must have an explicit disposition before acceptance is asserted.
- **Status discipline.** This deliverable updates only its own `_STATUS.md` (safe rule). It does not change the Package Datasheet's status or any other deliverable's metadata.

## Considerations

- The accessible source set in `_REFERENCES.md` is a decomposition basis, not a vendor data package. Reviewers should expect the bulk of acceptance criteria to depend on the EPC SoW and the accepted Package Datasheet (`DEL-013-02`) rather than the DBM, and should treat the DBM electrical slices as background design basis.
- Vendor documentation is typically delivered in revisions. The review log should record vendor revision and reviewer disposition for each cycle, not just the latest.
- "100A DC" in the package name is a project identifier, not a verified equipment rating; the actual UPS rating, battery autonomy, charger configuration, distribution-panel assignments, and physical location remain vendor-defined and are `TBD` at the package-decomposition level until vendor data is received and accepted.
- Test/inspection categories (FAT, SAT, electrical inspection, grounding/bonding) are reasonable expectations for a vendor-supplied UPS package, but the specific acceptance criteria belong to the EPC SoW and the Package Datasheet; reviewers should not assert acceptance criteria that are not source-supported.
- Turnover categories (mechanical-complete, energization-readiness, handover-to-operations) align with typical EPC construction workflow, but the authoritative gates belong to the Construction Work Package for `PKG-013`; until that document is accessible the categories serve as placeholders.

## Trade-offs

- **Accept partial vs. hold for completeness.** Where vendor documentation is partial, EPC Integrator may accept-with-comments and carry an explicit punch list rather than rejecting wholesale; the trade-off is schedule continuity vs. acceptance-evidence completeness. Either choice must be recorded in the review log.
- **Re-test vs. accept by analysis.** Where FAT/SAT cannot be re-performed, acceptance by certified vendor records and on-site inspection is acceptable when the EPC SoW permits; otherwise the item remains `TBD` and is surfaced for human ruling.
- **Strict interface verification vs. construction sequencing.** Strict verification of all four package interfaces before energization protects integration integrity; deferring some verification to commissioning may be necessary for sequencing reasons but must be explicit, not implicit.

## Examples

- Acceptance-checklist row example (Electrical Power): "Interface: Electrical Power. Vendor evidence: vendor wiring diagram rev N. EPC reference: EPC SoW clause TBD. Disposition: Accepted with comments. Comment: confirm feeder breaker coordination with upstream MCC in commissioning." (Form is illustrative; specific clause references depend on accessible EPC SoW.)
- Vendor-document review-log row example: "Document: UPS general arrangement drawing. Revision: B. Reviewer: EPC Electrical Lead. Disposition: Accepted with comments. Comments: dimensions to be confirmed against final pad layout." (Form is illustrative.)
- Turnover record example: "Mechanical complete: vendor equipment installed and anchored per general arrangement. Evidence: signed installation checklist." (Form is illustrative; authoritative gates per Construction Work Package, `TBD`.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| HRR-013-06-001 | Acceptance criteria depend on the EPC Scope of Work for `PKG-013`, but the EPC SoW is not present in the accessible source set (`_REFERENCES.md` lists no EPC SoW location). | `_CONTEXT.md` (scope text refers to EPC SoW) | `_REFERENCES.md` (no EPC SoW reference) | Specification REQ-013-06-005, REQ-013-06-006; Procedure steps; Guidance Examples | PROPOSAL: locate the EPC SoW reference for `PKG-013` and add it to `_REFERENCES.md`; carry specific acceptance criteria as `TBD` until then. | TBD |
| HRR-013-06-002 | Turnover evidence categories are aligned to a Construction Work Package for `PKG-013`, but the CWP is not in the accessible source set. | `_CONTEXT.md` (scope text refers to CWP) | `_REFERENCES.md` (no CWP reference) | Specification REQ-013-06-006; Procedure turnover steps | PROPOSAL: locate the CWP for `PKG-013` and add it to `_REFERENCES.md`; carry CWP-specific transition criteria as `TBD` until then. | TBD |
| HRR-013-06-003 | The companion Package Datasheet `DEL-013-02` is the EPC handoff basis, but its own `_STATUS.md` is `INITIALIZED`, not an accepted state; relying on it as acceptance authority is provisional. | `DEL-013-02/_STATUS.md` (`INITIALIZED`) | This deliverable's role definition (`DELIVERABLE_REGISTER.csv`) | Specification REQ-013-06-001, REQ-013-06-004 | PROPOSAL: treat `DEL-013-02` as provisional acceptance basis until it reaches a human-accepted state; record this reliance explicitly in the review log. | TBD |
