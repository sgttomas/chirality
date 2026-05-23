# Procedure: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Purpose

Define the future workflow for producing and reviewing `OperationProposal` records while preserving protected-path, human-gate, and professional-boundary constraints. This procedure is a design procedure for the future workflow; it does not activate domain-engine operation execution.

## Prerequisites

- Accepted future amendment authorizing domain-engine operation workflow implementation: TBD.
- Accepted `DomainEngineProfile` for the target engine: TBD.
- Protected path and proposal path policy: TBD, sibling deliverable DEL-10-02.
- Deterministic adapter or validation tool for the operation: TBD.
- Explicit human gate definition and acceptance evidence format: TBD.
- Declared upstream dependencies: TBD, no accepted dependency edges extracted yet.

## Steps

1. Confirm future-boundary authorization.
   - Verify that the work remains proposal/workflow design unless a governed amendment authorizes implementation.
   - Source: `_CONTEXT.md`; `docs/PRD.md` Section 8.17.

2. Create a draft `OperationProposal` record.
   - Populate each required field from `docs/TYPES.md` Section 11.2.
   - Use `TBD` for unavailable values.
   - Keep `ResponsibleParty` outside the proposal workflow as `TBD` until human assignment.

3. Identify inputs and intended changes.
   - Fill `inputRefs` with the future domain artifacts or proposal inputs to be reviewed.
   - Fill `intendedChanges` with proposed changes.
   - Do not write directly to protected domain-engine model truth.

4. Define deterministic checks.
   - Populate `deterministicChecks` with the checks expected before review.
   - Mark exact check payloads, pass/fail schema, adapter/profile reference, evidence path, and failure reason field as `TBD` until an adapter/profile contract is accepted.

5. Identify expected outputs and risks.
   - Populate `expectedOutputRefs` with proposal/review artifacts or approved future adapter outputs.
   - Populate `risks`; use `TBD` for risks requiring domain expert review.

6. Set the required human gate.
   - Populate `requiredHumanGate` with the required gate name or mark it `TBD`.
   - Keep the acceptance/rejection artifact format, actor/authority field, timestamp rule, and proposal identifier binding as `TBD` until accepted by human ruling.
   - Do not move to application without explicit human acceptance.

7. Review protected-path and professional-boundary posture.
   - Confirm agents write proposals, summaries, and review aids only.
   - Confirm proposal text does not claim professional approval, code compliance, external validation, or Chirality-owned solver truth.

8. Transition proposal status.
   - `draft`: initial incomplete or working proposal.
   - `ready_for_review`: ASSUMPTION: proposal has required fields populated or explicitly marked `TBD`, deterministic checks are prepared for review, and unresolved blockers are visible in the review checklist.
   - `accepted`: ASSUMPTION: explicit human acceptance has been recorded in a future acceptance evidence artifact bound to the proposal identifier.
   - `rejected`: ASSUMPTION: human reviewer or policy rejects the proposal and records the rejection reason in the same evidence family as acceptance.
   - `applied`: ASSUMPTION: approved future adapter applies the operation after human acceptance and records adapter validation/apply results.
   - Human ruling is needed before these transition semantics become implementation requirements.

## Verification

| Verification Item | Pass Condition |
|---|---|
| Field completeness | Every `OperationProposal` field from `docs/TYPES.md` Section 11.2 is populated or marked `TBD`. |
| Human gate | `requiredHumanGate` is present, and unresolved acceptance evidence is marked `TBD`. |
| Deterministic checks | `deterministicChecks` are listed or marked `TBD`; no prompt-only safety claim is made. |
| Protected path safety | No step instructs agents to write protected domain-engine model truth. |
| Boundary notice | No step or record represents Chirality as professional approver, code-compliance verifier, external validator, or solver truth owner. |
| Future-boundary posture | Procedure does not activate current-release domain operation execution. |
| Acceptance/rejection evidence | Future acceptance/rejection artifact format, actor/authority, timestamp, and proposal binding are defined or explicitly marked `TBD`. |
| Adapter result evidence | Future deterministic validation/apply result payload and storage location are defined or explicitly marked `TBD`. |
| Review sufficiency evidence | Future review checklist result records field completeness, protected-path posture, boundary-language review, gate readiness, deterministic-check readiness, and unresolved blockers or marks the result artifact as `TBD`. |

## Records

- Draft `OperationProposal` record.
- Deterministic check plan or `TBD` placeholder.
- Deterministic check result record: TBD future schema including check name, adapter/profile reference, pass/fail result, evidence path, and failure reason.
- Human gate acceptance/rejection record: TBD future schema including actor/authority, timestamp, proposal identifier binding, accepted/rejected value, and rejection reason when applicable.
- Review checklist result: TBD future artifact recording schema completeness, protected-path posture, boundary-language review, human-gate readiness, deterministic-check readiness, and unresolved blockers.
- Boundary notice review result.
- Adapter validation/apply result: TBD future implementation artifact including operation identifier, accepted proposal reference, output references, and failure/rollback note.
