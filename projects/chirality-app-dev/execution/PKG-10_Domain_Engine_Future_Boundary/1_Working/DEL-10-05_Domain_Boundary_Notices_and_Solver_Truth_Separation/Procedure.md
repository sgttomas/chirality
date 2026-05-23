# Procedure: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

## Purpose

Use this procedure to produce or review boundary-notice copy for future domain-engine surfaces without activating domain-engine implementation or implying Chirality-owned solver truth.

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the current four-document kit.
- Confirm `ResponsibleParty` remains `TBD` unless a human assigns ownership.
- Confirm PKG-10 remains future-boundary/gated scope unless a governed amendment says otherwise.
- Confirm no accepted upstream dependency edges are available yet; `_DEPENDENCIES.md` records upstream/downstream as TBD.
- Use `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/PRD.md`, `docs/SPEC.md`, `docs/TYPES.md`, and the v3.2 SOFTWARE_DECOMP as source authority.
- Treat the PRD hash mismatch in `_REFERENCES.md` as a warning only for this run, per dispatch.

## Steps

1. Identify the domain-engine surface under review.
   - Examples: UI result panel, operation proposal record, domain profile documentation, event record summary, protected artifact warning, fixture-profile example.

2. Classify the surface.
   - Mark it as one or more of: domain output, operation proposal, protected artifact, proposal/review aid, fixture profile, human acceptance gate, documentation example.

3. Apply the required notice pattern.
   - Use the standard notice for documentation and durable records.
   - Use the compact UI notice where space is constrained.
   - Use operation proposal, protected artifact, or fixture notices where the surface matches those categories.

4. Check for prohibited claims.
   - Reject or revise any wording that says or implies Chirality approves, validates, certifies, issues, signs, seals, externally validates, proves code compliance, decides professional adequacy, or owns solver truth.

5. Check ownership separation.
   - Confirm domain-engine outputs, deterministic checks, Chirality records/proposals, protected artifacts, and human acceptance are not conflated.

6. Check future-boundary posture.
   - If the copy references domain endpoints, adapters, OpenPipeStress, protected domain paths, operation application, or profile validation, ensure it is framed as future-boundary/gated scope unless an accepted amendment exists.

7. Mark unsupported details.
   - Use `TBD` for missing accepted facts.
   - Use `ASSUMPTION:` for best-effort inference.
   - Use `PROPOSAL:` for proposed copy or workflow wording.
   - Add or update a conflict table when source materials disagree or require human judgment.

8. Record review outcome.
   - Note pass/fail against the checklist in `Guidance.md`.
   - Record any human-ruling items.
   - Record the reviewed surface, reviewer, review date, source-warning status, closure verdict, unresolved human rulings, and carryforward items using the review output record fields below.
   - Do not create or update `Dependencies.csv` as part of this procedure.

## Verification

| Verification Item | Method |
|---|---|
| Notice present | Confirm every domain-engine surface has a boundary notice appropriate to its category. |
| Prohibited claims absent | Search/review for approve, validate, certify, issue, sign, seal, code compliance, external validation, professional adequacy, and solver truth ownership claims. |
| Human gate preserved | Confirm accepted domain state or reliance decisions require accountable human acceptance. |
| Protected paths preserved | Confirm protected domain artifacts are not described as directly agent-writable. |
| Future scope preserved | Confirm current-release implementation is not implied. |
| Unsupported facts labeled | Confirm unknowns are `TBD`, `ASSUMPTION`, `PROPOSAL`, or conflict-table items. |
| Closure evidence complete | Confirm the review output record includes reviewed surface, reviewer, date, checklist result, source-warning status, unresolved human rulings, and closure verdict. |
| PRD warning maintained | Confirm the PRD hash mismatch remains recorded with owner or resolution path until reconciled or formally waived. |

## Review Output Record

Use this minimum record shape for each boundary-notice review until a future product-native record is accepted:

| Field | Required Content |
|---|---|
| Reviewed surface | UI, documentation, event record, domain profile, operation proposal, protected artifact notice, fixture example, or other named surface. |
| Reviewed source | File/path, screen, mockup, record, or proposed copy location reviewed. |
| Reviewer | Accountable reviewer name or `TBD` if not yet assigned. |
| Review date | Calendar date or `TBD`. |
| Checklist result | Pass/fail for each `Guidance.md#Domain Review Checklist` row, or a reference to the completed checklist. |
| Notice pattern used | Standard, compact UI, operation proposal, protected artifact, fixture, or `TBD`. |
| Source-warning status | PRD hash warning open/closed/waived; closure evidence must cite the reconciliation or waiver record. |
| Human-ruling carryforward | Unresolved wording, profile-location, engine-specific, source-warning, or acceptance-authority questions. |
| Closure verdict | `PROPOSAL`, `BLOCKED`, `READY_FOR_HUMAN_RULING`, or `ACCEPTED_BY_HUMAN` with evidence. |

## Closure Evidence

A reviewed notice package is not complete merely because copy exists. Closure evidence must show:

- Required notice pattern or out-of-scope rationale for each selected future surface category.
- Completed checklist capture location, or `TBD` when no accepted storage location exists.
- OperationProposal schema citation status before operation-proposal notice examples are used as closure evidence.
- PRD source-warning owner or resolution path while `_REFERENCES.md` records a hash mismatch.
- Unresolved human-ruling items carried forward explicitly.

## Records

- Reviewed boundary notice copy.
- Completed domain review checklist from `Guidance.md`.
- Human-ruling list for unresolved wording, profile, or engine-specific questions.
- Source-warning note for PRD hash mismatch until reconciled, including owner or resolution path `TBD`.
- Review output record containing reviewed surface, reviewer, date, checklist result, source-warning status, closure verdict, and human-ruling carryforward.
- This deliverable's `_STATUS.md` lifecycle state.
