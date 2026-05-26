# Guidance — DEL-070-06 EPC Vendor Package Review and Acceptance

## Purpose

This guidance helps the EPC Integrator team conduct the review-and-acceptance activity for the PKG-070 Mole Sieve Drier Unit (NGL) vendor package in a way that is consistent with the West Doe Deepcut facility design basis, defensible as binding acceptance evidence, and aligned with sibling deliverables in PKG-070. The acceptance instrument exists to convert vendor-produced engineering and turnover into integrated, accepted project evidence, not to re-engineer the package.

## Principles

1. **Acceptance is human-authorized.** No automated review, checklist tooling, or agent output substitutes for an EPC Integrator authorized signatory accepting the package. (K-AUTH-1; see Specification REQ-070-06-11.)
2. **Acceptance is grounded in upstream truth.** Reviews cite DEL-070-01 SOW, DEL-070-02 Package Datasheet, DEL-070-03 CWP, DEL-070-04 Vendor Engineered Equipment Package, and DEL-070-05 Vendor Document Turnover Package — not generic conventions.
3. **Design-basis fidelity comes first.** Where the DBM-Deepcut specifies a constraint (e.g., 3A adsorbent only; BAHX 66 degC trip; outlet dewpoint targets), acceptance verifies compliance rather than accommodating vendor deviations silently.
4. **Open items must be dispositioned.** Carry forward only items with a named owner and closure plan; do not accept a package that buries open items in narrative.
5. **Deviation discipline.** Treat deviations from the Package Datasheet or SOW as either approved concessions (with reference) or NCRs (with corrective action). Do not normalize undocumented deviation.

## Considerations

- **Mole sieve unit identity in this project.** The DBM identifies multiple molecular-sieve services. PKG-070 is the **NGL** molecular sieve drier (DBM line 73), distinct from the **process gas** molecular sieve dehydration (DBM line 71, §"Molecular-Sieve Dehydration and Mercury Removal Basis" lines 1239+). The DBM provides detailed design basis primarily for the process-gas service. Direct NGL-mole-sieve design values are not enumerated at the same depth in the accessible DBM. **Conflict Table entry C-01** captures this.
- **Three-bed swing configuration.** The process-gas mole-sieve unit uses three driers (two in adsorption, one in standby/regen/cooling). NGL mole-sieve configuration is **TBD** from accessible sources; the acceptance package should require the vendor to declare and demonstrate the configuration explicitly.
- **Adsorbent constraint applies to function, not unit.** The 3A-only constraint protects against H2S adsorption and sulphur spikes in the regen loop. Acceptance should verify whether the NGL service has analogous sulphur-spike concerns and whether the 3A constraint is restated in the NGL package datasheet.
- **Turnover completeness gating.** Do not begin formal acceptance until DEL-070-05 is received and indexed. Partial turnover invites disputes about scope of acceptance.
- **Permitting envelope.** The BC Energy Regulator amendment and the Section 12.4 site-alteration permit (DBM line 131) frame what may be installed; acceptance verifies the as-supplied package falls within the permitted envelope.
- **Cryogenic protection.** The downstream BAHX is the safety-critical reason the mole sieve dehydration must meet outlet dewpoint targets. Acceptance reviewers should treat outlet-water-content evidence as a critical path item, not a routine performance check.

## Trade-offs

| Decision | Trade-off | Recommended posture |
|---|---|---|
| Accept with conditions vs. require revise & resubmit | Schedule recovery vs. residual integration risk | Use conditional acceptance only with named closure plan and date; otherwise R&R |
| Tight checklist (heavy citation) vs. summarized acceptance | Audit defensibility vs. reviewer effort | Bias to tight citation given safety-critical downstream service |
| Single integrated acceptance package vs. per-discipline mini-packages | Single source of truth vs. parallel discipline review velocity | Single package with per-discipline sections; preserves K-STATUS-1 single-state convention |
| Accept vendor-supplied procedures verbatim vs. EPC-rewritten procedures | Vendor warranty preservation vs. EPC operability fit | Accept vendor procedures; EPC adds site-specific addenda as separate documents |

## Examples

- **Example — outlet water content acceptance.** Vendor FAT report shows dewpoint analyzer reading -92 degC at design throughput. DBM (line 1254) states expected outlet <0.1 ppmv H2O, dewpoint <-90 degC. Accept; reference FAT report ID; carry as Pass against REQ-070-06-03.
- **Example — adsorbent material acceptance.** Vendor material certificate states 4A molecular sieve supplied. DBM line 1269 mandates 3A. Reject under REQ-070-06-04; raise NCR; require resupply with 3A media before acceptance can proceed.
- **Example — open-item disposition.** DBM line 1291 lists "final regeneration compressor capacity and design differential" as TBC. If vendor supplied a fixed 25 MMSCFD, 100 psid unit, document acceptance with reference to vendor data and confirm against DBM-stated "assumed design differential 100 psid"; flag the equipment-loop-table 79.5 psid discrepancy (DBM line 1279) for engineering closure.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | PKG-070 deliverable name is "Mole Sieve Drier Unit (NGL)" but DBM-Deepcut provides detailed design basis only for the **process gas** molecular sieve dehydration unit; NGL mole sieve dehydration is referenced (DBM line 73) but design values are not enumerated locally. | `_CONTEXT.md` PackageName ("Mole Sieve Drier Unit (NGL)") | DBM-Deepcut §"Molecular-Sieve Dehydration and Mercury Removal Basis" (process-gas service, lines 1239–1291) | Datasheet Conditions/Construction; Specification REQ-070-06-03..-08; Guidance "Mole sieve unit identity" | Treat process-gas DBM values as analogous reference only; require vendor and EPC Integrator to confirm NGL-specific values from `26020-Package_Requirements.docx` heading 24 once accessible | TBD |
| C-02 | DBM line 1279 records "assumed design differential 100 psid" for regen gas compressor, but the detailed equipment-loop table totals 79.5 psid (same line). | DBM line 1279 (assumed 100 psid) | DBM line 1279 (equipment-loop total 79.5 psid) | Specification REQ-070-06-06; Datasheet Conditions | Defer to engineering closure during detailed engineering; flag for vendor acceptance evidence | TBD |
| C-03 | DBM regeneration heater temperature basis is unresolved between 450 degF (system overview) and 460 degF (heater detail) per line 1280. | DBM line 1280 (450 degF) | DBM line 1280 (460 degF heater detail) | Specification (regen heater FAT acceptance) | Carry as open item; require vendor to declare design value in acceptance evidence | TBD |
| C-04 | `26020-Package_Requirements.docx` heading 24 is the cited project-level source for this deliverable but is a binary DOCX not extracted locally. Many specification clauses therefore depend on inaccessible source text. | `_CONTEXT.md` Source Reference | Local source tree (_Sources/) shows only DBM markdown extractions | Datasheet References; Specification REQ-070-06-12 and Standards row | Extract heading 24 to markdown and re-run Pass 1 for this deliverable before issuing | TBD |
