# Guidance: DEL-019-06_epc-vendor-package-review-and-acceptance

## Purpose

Explain how the EPC Integrator should perform vendor package review and acceptance for `PKG-019` (MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD) without overstating what the accessible source set actually authorizes, and how to record acceptance evidence that downstream activities (construction handover, turnover to operations) can rely upon.

## Principles

- **Authority hierarchy is upstream-fixed.** The accepted EPC Scope of Work (`DEL-019-01`), the `DEL-019-02` Package Datasheet, and the `DEL-019-03` Construction Work Package are the acceptance basis. The vendor package is the subject of review, not its own authority.
- **Responsibility split is non-negotiable.** Per `PACKAGE_REGISTER.csv` row `PKG-019`, the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration. Review comments shall not redesign the vendor package or accept vendor scope drift into EPC scope.
- **Source gaps are not silently filled.** Where the EPC Scope of Work, Construction Work Package, or vendor data is not accessible at acceptance-criteria fidelity, the acceptance criteria are recorded as `TBD` with the missing reference noted — not invented.
- **Interface evidence is the minimum acceptance unit.** Each of the six declared package interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) must have an explicit disposition before acceptance is asserted.
- **Status discipline.** This deliverable updates only its own `_STATUS.md` (safe rule). It does not change the Package Datasheet's status or any other deliverable's metadata.

## Considerations

- The accessible source set in `_REFERENCES.md` is a decomposition basis, not a vendor data package. Reviewers should expect the bulk of acceptance criteria to depend on the EPC SoW and the accepted Package Datasheet (`DEL-019-02`) rather than the DBM, and should treat the DBM electrical slices as background design basis.
- Vendor documentation is typically delivered in revisions. The review log should record vendor revision and reviewer disposition for each cycle, not just the latest.
- The package name "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" identifies nameplate-level intent (motor horsepower, supply voltage, phase, frequency, VFD output voltage class), but the actual VFD topology (e.g., cascaded H-bridge, NPC, AFE rectifier), harmonic mitigation strategy, isolation/coupling transformer configuration, cooling, bypass arrangement, and motor-side filtering remain vendor-defined and are `TBD` at the package-decomposition level until vendor data is received and accepted.
- MV VFDs typically have non-trivial I&C and Communications interface scope (run/stop/speed-reference, fault status, network integration to plant control/monitoring). The acceptance checklist must treat I&C and Communications as first-class interfaces alongside Electrical Power, not as afterthoughts.
- Harmonics (IEEE 519) and EMC compliance evidence are commonly required for MV VFD installations; reviewers should confirm the EPC SoW for the specific compliance basis rather than asserting limits not source-supported.
- Test/inspection categories (FAT, SAT, electrical inspection, grounding/bonding, harmonics) are reasonable expectations for a vendor-supplied MV VFD package, but the specific acceptance criteria belong to the EPC SoW and the Package Datasheet; reviewers should not assert acceptance criteria that are not source-supported.
- Turnover categories (mechanical-complete, energization-readiness, handover-to-operations) align with typical EPC construction workflow, but the authoritative gates belong to the Construction Work Package (`DEL-019-03`); until that document is accessible at acceptance-criteria fidelity the categories serve as placeholders.

## Trade-offs

- **Accept partial vs. hold for completeness.** Where vendor documentation is partial, EPC Integrator may accept-with-comments and carry an explicit punch list rather than rejecting wholesale; the trade-off is schedule continuity vs. acceptance-evidence completeness. Either choice must be recorded in the review log.
- **Re-test vs. accept by analysis.** Where FAT/SAT cannot be re-performed, acceptance by certified vendor records and on-site inspection is acceptable when the EPC SoW permits; otherwise the item remains `TBD` and is surfaced for human ruling.
- **Strict interface verification vs. construction sequencing.** Strict verification of all six package interfaces before energization protects integration integrity; deferring some verification (typically harmonics measurement and Communications integration) to commissioning may be necessary for sequencing reasons but must be explicit, not implicit.

## Examples

- Acceptance-checklist row example (Electrical Power): "Interface: Electrical Power. Vendor evidence: vendor single-line and feeder schedule rev N. EPC reference: EPC SoW clause TBD. Disposition: Accepted with comments. Comment: confirm 4160 V supply breaker coordination with upstream switchgear in commissioning." (Form is illustrative; specific clause references depend on accessible EPC SoW.)
- Acceptance-checklist row example (I&C / Control Cabling): "Interface: I&C / Control Cabling. Vendor evidence: vendor I/O list and control schematics rev N. EPC reference: EPC SoW clause TBD. Disposition: Accepted with comments. Comment: confirm run/stop and speed-reference signal mapping with plant DCS at commissioning." (Form is illustrative.)
- Vendor-document review-log row example: "Document: VFD general arrangement and weights drawing. Revision: B. Reviewer: EPC Electrical Lead. Disposition: Accepted with comments. Comments: dimensions and pad-loading to be confirmed against foundation design." (Form is illustrative.)
- Turnover record example: "Mechanical complete: vendor equipment installed and anchored per general arrangement. Evidence: signed installation checklist." (Form is illustrative; authoritative gates per Construction Work Package, `TBD`.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| HRR-019-06-001 | Acceptance criteria depend on the EPC Scope of Work for `PKG-019`, but the EPC SoW is not present in the accessible source set at acceptance-criteria fidelity (`_REFERENCES.md` lists no EPC SoW document beyond the in-project `DEL-019-01` whose status per its own `_STATUS.md` is not yet accepted). | `_CONTEXT.md` (scope text refers to EPC SoW) | `_REFERENCES.md` (no external EPC SoW reference) | Specification REQ-019-06-005, REQ-019-06-006; Procedure steps; Guidance Examples | PROPOSAL: rely on `DEL-019-01_scope-of-work` once accepted and add any external EPC SoW reference to `_REFERENCES.md`; carry specific acceptance criteria as `TBD` until then. | TBD |
| HRR-019-06-002 | Turnover evidence categories are aligned to a Construction Work Package for `PKG-019` (`DEL-019-03`), but its content is not currently accessible at acceptance-criteria fidelity. | `_CONTEXT.md` (scope text refers to CWP) | `_REFERENCES.md` (no CWP detail beyond the in-project deliverable pointer) | Specification REQ-019-06-006; Procedure turnover steps | PROPOSAL: rely on `DEL-019-03_construction-work-package` once it reaches an accepted state; carry CWP-specific transition criteria as `TBD` until then. | TBD |
| HRR-019-06-003 | The companion Package Datasheet `DEL-019-02` is the EPC handoff basis, but its own `_STATUS.md` is `OPEN`, not an accepted state; relying on it as acceptance authority is provisional. | `DEL-019-02/_STATUS.md` (`OPEN`) | This deliverable's role definition (`DELIVERABLE_REGISTER.csv`) | Specification REQ-019-06-001, REQ-019-06-004 | PROPOSAL: treat `DEL-019-02` as provisional acceptance basis until it reaches a human-accepted state; record this reliance explicitly in the review log. | TBD |
| HRR-019-06-004 | Harmonics (IEEE 519) and EMC compliance evidence is widely standard for MV VFD acceptance, but the EPC SoW basis is not accessible to confirm specific limits, measurement methods, or point-of-common-coupling. | Industry practice; this deliverable's Considerations | `_REFERENCES.md` (no EPC SoW harmonic clause) | Specification REQ-019-06-005; Guidance Considerations | PROPOSAL: carry harmonics acceptance criteria as `TBD` (ASSUMPTION: likely applicable) until EPC SoW clause set is accessible. | TBD |
