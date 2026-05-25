# Guidance: DEL-027-06_epc-vendor-package-review-and-acceptance

## Purpose

Explain how the EPC Integrator should perform vendor package review and acceptance for `PKG-027` (Transformer TXP-8301-1 — 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV step-down distribution transformer) without overstating what the accessible source set actually authorizes, and how to record acceptance evidence that downstream activities (construction handover, turnover to operations) can rely upon.

## Principles

- **Authority hierarchy is upstream-fixed.** The accepted EPC Scope of Work, the `DEL-027-02` Package Datasheet, and the `DEL-027-03` Construction Work Package are the acceptance basis. The vendor package is the subject of review, not its own authority.
- **Responsibility split is non-negotiable.** Per `PACKAGE_REGISTER.csv` row `PKG-027`, the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration. Review comments shall not redesign the vendor transformer or accept vendor scope drift into EPC scope.
- **Source gaps are not silently filled.** Where the EPC Scope of Work, Construction Work Package, or vendor data is not accessible, the acceptance criteria are recorded as `TBD` with the missing reference noted — not invented.
- **Interface evidence is the minimum acceptance unit.** Each of the seven declared package interfaces must have an explicit disposition before acceptance is asserted.
- **Status discipline.** This deliverable updates only its own `_STATUS.md` (safe rule). It does not change the Package Datasheet's status or any other deliverable's metadata.

## Considerations

- The accessible source set in `_REFERENCES.md` is a decomposition basis, not a vendor data package. Reviewers should expect the bulk of acceptance criteria to depend on the EPC SoW and the accepted Package Datasheet (`DEL-027-02`) rather than the DBM, and should treat the DBM-Deepcut electrical slices as background design basis (medium-voltage distribution, 13.8 kV / 6.9 kV / 600 V hierarchy, low-resistance grounding regime).
- The package title voltage triplet "13.8kV/6.9kV/0.4kV" implies primary 13.8 kV with two secondaries (6.9 kV and 0.4 kV). The 0.4 kV secondary is non-standard relative to the DBM 600 V / 208/120 V hierarchy (DBM lines ~2933-2937) and must be confirmed against the EPC SoW or vendor data; it is recorded as ASSUMPTION until then.
- Vendor documentation is typically delivered in revisions. The review log should record vendor revision and reviewer disposition for each cycle, not just the latest.
- Test/inspection categories (FAT routine tests — ratio, polarity, no-load loss, load loss/impedance, dielectric, induced voltage; type/temperature-rise tests where required; SAT; electrical inspection; grounding/bonding) are reasonable expectations for an oil-filled step-down distribution transformer, but the specific acceptance criteria belong to the EPC SoW, the applicable transformer standard, and the Package Datasheet; reviewers should not assert acceptance criteria that are not source-supported.
- Turnover categories (mechanical-complete, energization-readiness, handover-to-operations) align with typical EPC construction workflow, but the authoritative gates belong to the Construction Work Package for `PKG-027`; until that document is drafted/accepted the categories serve as placeholders.
- Project grounding basis (DBM line ~2985): each 6.9 kV transformer is grounded using a 100 A, 10 s neutral grounding resistor and operates as a tripping system. The acceptance checklist for the Grounding / Bonding interface should explicitly verify the NGR rating, the tripping configuration, and the two-point ground-grid connection (DBM line ~2989).

## Trade-offs

- **Accept partial vs. hold for completeness.** Where vendor documentation is partial, EPC Integrator may accept-with-comments and carry an explicit punch list rather than rejecting wholesale; the trade-off is schedule continuity vs. acceptance-evidence completeness. Either choice must be recorded in the review log.
- **Re-test vs. accept by analysis.** Where FAT cannot be re-performed, acceptance by certified vendor records and on-site inspection (insulation resistance, turns ratio, dielectric checks) is acceptable when the EPC SoW permits; otherwise the item remains `TBD` and is surfaced for human ruling.
- **Strict interface verification vs. construction sequencing.** Strict verification of all seven package interfaces before energization protects integration integrity; deferring some verification (e.g., Communications / Network, Area / Exterior Lighting) to commissioning may be necessary for sequencing reasons but must be explicit, not implicit.

## Examples

- Acceptance-checklist row example (Electrical Power): "Interface: Electrical Power. Vendor evidence: vendor single-line and nameplate data rev N. EPC reference: EPC SoW clause TBD. Disposition: Accepted with comments. Comment: confirm 13.8 kV primary feeder coordination and 6.9 kV secondary protection settings during commissioning." (Form is illustrative; specific clause references depend on accessible EPC SoW.)
- Acceptance-checklist row example (Grounding / Bonding): "Interface: Grounding / Bonding. Vendor evidence: vendor grounding drawing rev N; NGR data sheet. EPC reference: DBM-Deepcut §Electrical (NGR 100 A 10 s on 6.9 kV neutral). Disposition: Accepted with comments. Comment: verify two-point ground-grid connection per DBM line ~2989." (Form is illustrative.)
- Vendor-document review-log row example: "Document: transformer general arrangement and outline drawing. Revision: B. Reviewer: EPC Electrical Lead. Disposition: Accepted with comments. Comments: confirm clearances to adjacent equipment per CEC spacing; coordinate with foundation drawings." (Form is illustrative.)
- Turnover record example: "Mechanical complete: transformer installed and anchored per general arrangement; oil filled and vacuum-degassed per vendor procedure; accessories installed. Evidence: signed installation checklist." (Form is illustrative; authoritative gates per Construction Work Package, `TBD`.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| HRR-027-06-001 | Acceptance criteria depend on the EPC Scope of Work for `PKG-027`, but the EPC SoW is not present in the accessible source set (`_REFERENCES.md` lists no EPC SoW location; companion `DEL-027-01` is not yet at an accepted state). | `_CONTEXT.md` (scope text refers to EPC SoW) | `_REFERENCES.md` (no EPC SoW reference) | Specification REQ-027-06-005, REQ-027-06-006; Procedure steps; Guidance Examples | PROPOSAL: locate the EPC SoW reference for `PKG-027` (or progress `DEL-027-01`) and add it to `_REFERENCES.md`; carry specific acceptance criteria as `TBD` until then. | TBD |
| HRR-027-06-002 | Turnover evidence categories are aligned to a Construction Work Package for `PKG-027`, but the CWP (`DEL-027-03`) is not yet drafted/accepted. | `_CONTEXT.md` (scope text refers to CWP) | Companion `DEL-027-03` folder status | Specification REQ-027-06-006; Procedure turnover steps | PROPOSAL: progress `DEL-027-03` and reference its accepted version; carry CWP-specific transition criteria as `TBD` until then. | TBD |
| HRR-027-06-003 | The companion Package Datasheet `DEL-027-02` is the EPC handoff basis, but it has not yet been drafted/initialized; relying on it as acceptance authority is provisional. | `DEL-027-02` folder (no four-doc kit yet) | This deliverable's role definition (`DELIVERABLE_REGISTER.csv`) | Specification REQ-027-06-001, REQ-027-06-004 | PROPOSAL: progress `DEL-027-02` to at least `INITIALIZED` and re-issue this deliverable's review log against the accepted Datasheet; record reliance explicitly in the review log. | TBD |
| HRR-027-06-004 | The package title voltage triplet includes a 0.4 kV secondary, which does not align with the DBM voltage hierarchy of 600 V / 208/120 V (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical, lines ~2933-2937). | Package name in `PACKAGE_REGISTER.csv` row `PKG-027` (0.4 kV) | DBM-Deepcut §Electrical voltage hierarchy (600 V, 208/120 V) | Datasheet Conditions (Transformer service basis); Specification REQ-027-06-005 | PROPOSAL: confirm 0.4 kV secondary winding against EPC SoW and vendor data; if 0.4 kV is correct, record it as a package-specific exception to the DBM hierarchy. | TBD |
