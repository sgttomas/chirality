# Guidance — EPC Vendor Package Review and Acceptance (DEL-082-06)

Directional guidance for the EPC Integrator performing review and acceptance of the PKG-082 Flare KO Drum (Low Pressure) 3-25 vendor package.

## Purpose

This deliverable exists to produce the audit-grade evidence that the EPC Integrator has reviewed the vendor's engineered package (DEL-082-04) and turnover documentation (DEL-082-05) against the project's EPC Scope of Work (DEL-082-01), Package Datasheet (DEL-082-02), and Construction Work Package (DEL-082-03), and that the package is acceptable for handoff. It supports the package's Gate 5 closure (`_CONTEXT.md` Notes: "Additional Gate 5 deliverable framed as EPC-integrator review and acceptance evidence.").

It is NOT an approval record. Binding approval is a human authorship act (K-AUTH-1).

## Principles

1. **Source-anchored acceptance.** Every acceptance decision must be traceable to a specific requirement source (SOW item, Datasheet attribute, CWP step, or DBM clause), not to general convention.
2. **Separate acceptance from approval.** This deliverable produces evidence. Humans approve.
3. **Surface, do not absorb.** Vendor deviations, missing data, and unresolved items must be surfaced in the review log and checklist. The role of the reviewer is to make conflicts visible, not to silently reconcile them.
4. **Sour-service primacy.** LP flare service is sour hydrocarbon relief (DBM SEC-07 — TEG regen, VRU, compressor seal-pot routes). Acceptance must give explicit weight to sour-service isolation philosophy (DBM SEC-09).
5. **Hand the next step a clean baseline.** Turnover evidence is the input to operations and to long-tail records (inspection, compliance). Gaps left here become defects downstream.

## Considerations

- The LP relief header is currently carried at the same nominal size as the HP relief header (508 mm / 20 in) per DBM SEC-07. Reviewers should treat any vendor deviation from this nominal as a finding requiring an engineering ruling, not as a silent acceptance.
- Staggered blowdown is a required control for limiting maximum relief (DBM SEC-07). Acceptance evidence should confirm the vendor package does not assume non-staggered blowdown.
- The detailed blowdown-sequencing source W242510-PRC-REP-000003-001 is referenced but not in the workspace. Reviewers should cross-check vendor assumptions against that document when it is accessible; otherwise flag `location TBD`.
- The LP stack OD is open (TBD per DBM SEC-07). If the vendor package presumes a stack OD, the assumption must be flagged and reconciled.
- Skid-edge isolation, vent/drain class routing, and double-block-and-bleed for sour service are common deviation hot spots in vendor submittals (DBM SEC-09). Build these into the checklist explicitly rather than relying on a general "isolation OK" row.
- The Package Datasheet (DEL-082-02) is the primary local-to-package authority. Where DBM and Datasheet are silent on a parameter, do not invent it; record as `TBD` in the review.

## Trade-offs

- **Depth vs throughput.** A row-by-row source-cite for every vendor document is high effort. Recommended: full source-cite for safety-critical and code-required documents; standard checklist disposition for routine documents, with sampled deep-cite.
- **Concurrent review vs sequential.** Reviewing turnover evidence (DEL-082-05) before the engineered package (DEL-082-04) is fully accepted risks rework if engineering changes are still in flight. Recommended: sequence engineering acceptance ahead of turnover-package final acceptance; allow draft turnover review in parallel.
- **Reviewer specialization.** Mechanical lead should own vessel/relief acceptance; process safety should own sour-service and relief-routing acceptance; pumps SME should own P-3900-2 acceptance. Single-reviewer acceptance increases the chance of missed sour-service findings.

## Examples

The locally accessible sources do not provide worked-example acceptance evidence for analogous packages. Example artifact templates are TBD — defer to project documentation control plan when available.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-082-06-01 | Disposition vocabulary for the document review log is not fixed in any locally accessible source. | `_CONTEXT.md` Anticipated Artifacts (lists artifact, not vocabulary) | Standard EPC convention (Accepted / Accepted with Comment / Revise and Resubmit / Rejected) | Specification REQ-082-06-01; Procedure Step 2 | Adopt standard EPC vocabulary as PROPOSAL pending human or project documentation-control ruling | TBD |
| C-082-06-02 | Specific code-of-construction and NDE class for V-3900-2 not cited in the locally accessible source slices. | DBM SEC-09 (general vessel design philosophy) | DEL-082-02 Package Datasheet (not yet locally extracted) | Specification REQ-082-06-05 | Defer authority to DEL-082-02 when accessible; record `location TBD` in interim | TBD |

## Source citations used in this Guidance

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06, SEC-07, SEC-09
- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- Decomposition register row for DEL-082-06 (GATE-07 snapshot)
