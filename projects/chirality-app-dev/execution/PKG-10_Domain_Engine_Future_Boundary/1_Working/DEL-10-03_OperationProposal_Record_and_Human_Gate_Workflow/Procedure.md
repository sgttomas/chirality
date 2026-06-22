# Procedure: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Purpose

Define the future workflow for producing and reviewing `OperationProposal` records while preserving protected-path, human-gate, result-schema, and professional-boundary constraints. This procedure is a design procedure for the future workflow; it does not activate domain-engine operation execution.

## Prerequisites

- Framework canon source: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`.
- Accepted future amendment authorizing domain-engine operation workflow implementation: TBD.
- Accepted `DomainEngineProfile` for the target engine: TBD.
- Protected path and proposal path policy: TBD, sibling deliverable DEL-10-02.
- Deterministic adapter or validation tool for the operation: TBD.
- Concrete `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema refs: TBD.
- Operation store and review-checklist result artifact path/schema: TBD.
- Declared upstream dependencies: TBD, no accepted dependency edges extracted yet.

## Steps

1. Confirm future-boundary authorization.
   - Verify that the work remains proposal/workflow design unless a governed amendment authorizes implementation.
   - Source: `_CONTEXT.md`; `docs/PLAN.md` R7; D-APP-39 F3.

2. Create a draft `OperationProposal` record.
   - Populate each canonical field from REF-008 / `docs/TYPES.md` Section 11.2.
   - Set `status` to `proposal_only`.
   - Set `lifecycle` to `draft`.
   - Use `TBD` for unavailable implementation values.
   - Keep `ResponsibleParty` outside the proposal workflow as `TBD` until human assignment.

3. Identify baseline, inputs, and intended changes.
   - Fill `base_state` with the accepted baseline or mark it `TBD`.
   - Fill `input_refs` with the future domain artifacts or proposal inputs to be reviewed.
   - Fill `intended_changes` with proposed changes.
   - Do not write directly to protected domain-engine model truth.

4. Define deterministic checks.
   - Populate `deterministic_checks` with the checks expected before review.
   - Tie checks to profile-level `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema hooks.
   - Mark exact payloads, pass/fail schema, adapter/profile reference, evidence path, and failure reason field as `TBD` until an adapter/profile contract is accepted.

5. Identify expected outputs, risks, assumptions, and blockers.
   - Populate `expected_output_refs` with proposal/review artifacts or approved future adapter outputs.
   - Populate `risks`, `assumptions`, and `blockers`; use `TBD` for items requiring domain expert review.
   - Record `operation_risk_class` and provenance for judgment values.

6. Set the required human gate.
   - Populate `required_human_gate` with the required gate name or mark it `TBD`.
   - Do not move to `accepted` or `applied` without explicit human approval bound to git SHA per K-AUTH-2.
   - Do not move to `applied` without domain-engine-controlled apply or external terminal acceptance record.

7. Review protected-path and professional-boundary posture.
   - Confirm agents write proposals, summaries, and review aids only.
   - Confirm proposal text does not claim professional approval, code compliance, certification, sealing, authentication, external validation, or Chirality-owned solver truth.

8. Maintain lifecycle semantics.
   - `draft`: initial incomplete or working proposal.
   - `ready_for_review`: proposal has required fields populated or explicitly marked `TBD`, deterministic checks are identified, and unresolved blockers are visible in the review checklist.
   - `accepted`: explicit human approval has been recorded and bound to git SHA per K-AUTH-2.
   - `rejected`: human reviewer or policy rejects the proposal and records the rejection reason in the same evidence family as acceptance.
   - `applied`: accepted proposal is applied by domain-engine-controlled apply or external terminal acceptance record, with result evidence stored according to the accepted profile/workflow.

## Verification

| Verification Item | Pass Condition |
|---|---|
| Field completeness | Every canonical `OperationProposal` field is populated or marked `TBD`. |
| Status/lifecycle | `status` is `proposal_only`; lifecycle values match REF-008. |
| Human gate | Accepted/applied states require K-AUTH-2-bound human approval. |
| Deterministic checks | Checks are listed or marked `TBD`; no prompt-only safety claim is made. |
| Result schema hooks | Validation/apply/check result schema hooks are present; concrete refs may remain `TBD`. |
| Protected path safety | No step instructs agents to write protected domain-engine model truth. |
| Boundary notice | No step or record represents Chirality as professional approver, code-compliance verifier, certifier, sealer, authenticator, external validator, or solver truth owner. |
| Future-boundary posture | Procedure does not activate current-release domain operation execution. |
| Review sufficiency evidence | Future review checklist result records field completeness, protected-path posture, boundary-language review, gate readiness, deterministic-check readiness, and unresolved implementation blockers or marks the result artifact as `TBD`. |

## Records

- Draft `OperationProposal` record.
- Deterministic check plan or `TBD` placeholder.
- Deterministic check result record: TBD future schema including check name, adapter/profile reference, pass/fail result, evidence path, and failure reason.
- Human gate acceptance/rejection record: TBD future artifact carrying K-AUTH-2-bound approval/rejection evidence.
- Review checklist result: TBD future artifact recording schema completeness, protected-path posture, boundary-language review, human-gate readiness, deterministic-check readiness, and unresolved implementation blockers.
- Boundary notice review result.
- Adapter validation/apply result: TBD future implementation artifact including operation identifier, accepted proposal reference, output references, and failure/rollback note.
