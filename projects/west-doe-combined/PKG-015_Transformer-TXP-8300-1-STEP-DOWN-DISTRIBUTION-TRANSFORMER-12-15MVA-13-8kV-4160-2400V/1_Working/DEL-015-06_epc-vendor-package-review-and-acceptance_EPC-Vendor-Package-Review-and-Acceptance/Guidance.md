# Guidance: DEL-015-06_epc-vendor-package-review-and-acceptance

## Purpose

Explain how the EPC Integrator should perform vendor package review and acceptance for `PKG-015` (Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V) without overstating what the accessible source set actually authorizes, and how to record acceptance evidence that downstream activities (construction handover, turnover to operations) can rely upon.

## Principles

- **Authority hierarchy is upstream-fixed.** The accepted EPC Scope of Work (DEL-015-01), Package Datasheet (DEL-015-02), and Construction Work Package (DEL-015-03) are the acceptance basis. The vendor package (DEL-015-04 / DEL-015-05) is the subject of review, not its own authority.
- **Responsibility split is non-negotiable.** Per `PACKAGE_REGISTER.csv` row `PKG-015`, the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration. Review comments must not redesign the vendor package or absorb vendor scope drift into EPC scope.
- **Source gaps are not silently filled.** Where the EPC SoW, Package Datasheet, Construction Work Package, or vendor data is not accessible, acceptance criteria are recorded as `TBD` with the missing reference noted — not invented.
- **Interface evidence is the minimum acceptance unit.** Each of the seven declared package interfaces (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) must have an explicit disposition before acceptance is asserted.
- **Status discipline.** This deliverable updates only its own `_STATUS.md` per the safe rule; it does not change the Package Datasheet's status or any other deliverable's metadata.

## Considerations

- The accessible source set in `_REFERENCES.md` is a decomposition basis, not a vendor data package. Reviewers should expect the bulk of acceptance criteria to depend on the EPC SoW and the accepted Package Datasheet (DEL-015-02) rather than the DBM, and should treat the DBM electrical slices (lines 732-768) as background facility design basis.
- The package name encodes voltages "13.8kV/4160/2400V" and a dual rating "12/15MVA"; the accessible DBM slice cites a single 12 MVA transformer 13.8 kV / 4.16 kV (line 744) feeding the 4160V MCC. The 2400 V tap and the 15 MVA upper rating are not described in the DBM. Reviewers should treat the package name as identity rather than as a verified rating, and pursue reconciliation through the EPC SoW and Package Datasheet.
- Vendor documentation is typically delivered in revisions. The review log should record vendor revision and reviewer disposition for each cycle, not just the latest.
- Test/inspection categories (FAT, SAT, dielectric, insulation resistance, ratio/polarity, no-load loss, load loss, sound level, grounding/bonding) are reasonable expectations for a power transformer package, but the binding acceptance criteria belong to the EPC SoW and the Package Datasheet; reviewers should not assert acceptance criteria that are not source-supported.
- Turnover categories (mechanical-complete, energization-readiness, handover-to-operations) align with typical EPC construction workflow, but authoritative gates belong to the Construction Work Package for `PKG-015` (DEL-015-03); until that document is accessible the categories serve as placeholders.
- The site low-temperature basis (-40 deg C minimum) governs exposed transformer accessories (radiators, conservator/breather where applicable, control cabinets, tap-changer drives). Reviewers should look for explicit vendor confirmation of cold-start, oil grade, and accessory heating provisions.

## Trade-offs

- **Accept partial vs. hold for completeness.** Where vendor documentation is partial, the EPC Integrator may accept-with-comments and carry an explicit punch list rather than rejecting wholesale; the trade-off is schedule continuity vs. acceptance-evidence completeness. The choice must be recorded in the review log.
- **Re-test vs. accept by analysis.** Where FAT/SAT cannot be re-performed, acceptance by certified vendor test records plus on-site inspection is acceptable when the EPC SoW permits; otherwise the item remains `TBD` and is surfaced for human ruling.
- **Strict interface verification vs. construction sequencing.** Strict verification of all seven package interfaces before energization protects integration integrity; deferring some verification (e.g., communications/network commissioning) to a later commissioning window may be necessary for sequencing but must be explicit, not implicit.

## Examples

- Acceptance-checklist row example (Electrical Power): "Interface: Electrical Power. Vendor evidence: vendor primary/secondary one-line rev N. EPC reference: EPC SoW clause TBD. Disposition: Accepted with comments. Comment: confirm 13.8 kV LRG ground-fault coordination with 04-25 main switchgear protective relays." (Form is illustrative.)
- Vendor-document review-log row example: "Document: Transformer general arrangement and nameplate drawing. Revision: B. Reviewer: EPC Electrical Lead. Disposition: Accepted with comments. Comments: reconcile 2400 V tap declaration in nameplate vs. EPC SoW load list." (Form is illustrative.)
- Turnover record example: "Mechanical complete: transformer installed and anchored to foundation per general arrangement; oil filled and tested. Evidence: signed installation checklist + oil test report." (Form is illustrative; authoritative gates per DEL-015-03, `TBD`.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| HRR-015-06-001 | Package name carries a 2400 V tap (Transformer TXP-8300-1 ... 13.8kV/4160/2400V), but the accessible DBM electrical service table (lines 732-733) describes only 13.8 kV incoming and 4,160 V medium-voltage service; no 2400 V service or load is identified in the accessible slice. | DELIVERABLE_REGISTER.csv / PACKAGE_REGISTER.csv (package name) | DBM 3-25 lines 732-733, 744 | Specification REQ-015-06-08; Datasheet "Package-named voltage taps"; Guidance Considerations | PROPOSAL: treat the 2400 V tap as unverified at decomposition level; require the EPC SoW and Package Datasheet (DEL-015-02) to either confirm a 2400 V load or rationalize the tap, and carry the acceptance criterion as `TBD` until then. | TBD |
| HRR-015-06-002 | Package name indicates 12/15 MVA dual rating; the accessible DBM transformer reference (line 744) cites a single 12 MVA value for the 13.8 kV / 4.16 kV transformer. The 15 MVA upper rating (typically ONAF for OA/FA dual-rated transformers) is not stated in the accessible source slice. | DELIVERABLE_REGISTER.csv / PACKAGE_REGISTER.csv (package name) | DBM 3-25 line 744 | Specification REQ-015-06-09; Datasheet | PROPOSAL: confirm dual rating basis (e.g., ONAN/ONAF) and cooling mode against the EPC SoW and vendor nameplate; carry as `TBD` until confirmed. | TBD |
| HRR-015-06-003 | Acceptance criteria depend on the EPC Scope of Work for PKG-015, but the EPC SoW is not present in the accessible source set (`_REFERENCES.md` lists no EPC SoW location). | `_CONTEXT.md` (scope text refers to EPC SoW) | `_REFERENCES.md` (no EPC SoW reference) | Specification REQ-015-06-02, REQ-015-06-03, REQ-015-06-08, REQ-015-06-09, REQ-015-06-12; Procedure | PROPOSAL: locate the EPC SoW for PKG-015 and add it to `_REFERENCES.md`; carry specific acceptance criteria as `TBD` until then. | TBD |
| HRR-015-06-004 | Turnover evidence categories are aligned to a Construction Work Package for PKG-015, but the CWP is not in the accessible source set. | `_CONTEXT.md` (scope text refers to CWP) | `_REFERENCES.md` (no CWP reference) | Specification REQ-015-06-04; Procedure turnover steps | PROPOSAL: locate DEL-015-03 outputs (Construction Work Package) when produced and add them to `_REFERENCES.md`; carry CWP-specific transition criteria as `TBD` until then. | TBD |
| HRR-015-06-005 | The companion Package Datasheet DEL-015-02 is the EPC handoff basis. Its own `_STATUS.md` maturity is not verified here; relying on it as acceptance authority is provisional until it reaches a human-accepted state. | DELIVERABLE_REGISTER.csv row DEL-015-02 | This deliverable's role definition (DELIVERABLE_REGISTER.csv row DEL-015-06) | Specification REQ-015-06-02, REQ-015-06-13 | PROPOSAL: treat DEL-015-02 as provisional acceptance basis until it reaches a human-accepted state; record the reliance explicitly in the review log. | TBD |
