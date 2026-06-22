# Guidance: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Purpose

This deliverable preserves future compatibility for domain-engine operation workflows without turning Chirality into a domain solver. It defines how future domain operations should be represented as proposed, reviewable, human-gated records before any protected domain state can be changed.

Primary canon: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`.

## Principles

- Treat `OperationProposal` as a future proposal and audit record, not as permission to execute a domain operation by itself.
- Keep authoritative domain truth in the domain engine. Chirality governs interaction, proposals, records, review aids, and human gates.
- Keep protected domain paths separate from profile-approved agent-writable proposal paths.
- Preserve `status = proposal_only`; use `lifecycle` for `draft`, `ready_for_review`, `accepted`, `rejected`, and `applied`.
- Require deterministic checks and profile-declared result-schema hooks before a future operation can be considered implementation-ready.
- Require explicit human approval bound to git SHA per K-AUTH-2 before accepted/applied lifecycle states.
- Preserve professional-boundary language: Chirality must not claim professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth ownership.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Future scope | Draft record/workflow surfaces only; do not activate domain-engine implementation in this package. | `_CONTEXT.md`; `docs/PRD.md` Section 8.17; D-APP-39 F3 |
| Proposal fields | Use the REF-008 field table as the minimum record shape. | REF-008; `docs/TYPES.md` Section 11.2 |
| Base state | Include `base_state` so review can compare proposed changes against a named accepted state or artifact baseline. | REF-008 |
| Deterministic checks | Define check names and expected outcomes before review; concrete result payloads and schema refs remain true implementation TBDs. | REF-008; `docs/PRD.md` Section 8.17 FR-112 |
| Human gate | Accepted/applied states require explicit human approval bound to git SHA per K-AUTH-2. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
| Applied state | Applied state additionally requires domain-engine-controlled apply or external terminal acceptance record. | REF-008 |
| Protected paths | Proposal outputs should be written to proposal/review locations, not protected model truth. | `docs/PRD.md` Section 8.17 FR-110/FR-111 |
| Professional boundary | Review copy and event records should avoid language that makes Chirality the approving professional, code-compliance verifier, external validator, certifier, sealer, authenticator, or solver owner. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |

The former "7 TBD blockers" around required-human-gate semantics and result-schema hooks are resolved by framework canon. Do not re-derive them locally. Preserve only concrete implementation TBDs: profile instances, concrete schema refs, adapters, operation stores, apply tooling, review-checklist artifact path/schema, and concrete proposal records.

## Terminology Map

| Term | Meaning in this deliverable | Current disposition |
|---|---|---|
| `status` | Canonical proposal-only posture. | Required value: `proposal_only`. |
| `lifecycle` | Proposal progression: `draft`, `ready_for_review`, `accepted`, `rejected`, `applied`. | Canonical values; implementation artifacts remain future-gated. |
| Human gate | The workflow point that prevents accepted/applied lifecycle states without accountable human action. | Required by REF-008 and K-DOMAIN-3. |
| Explicit human approval | K-AUTH-2-bound human approval evidence for accepted/applied lifecycle states. | Canonical requirement; concrete evidence artifact remains implementation `TBD`. |
| `required_human_gate` | The `OperationProposal` field naming the required gate. | Required field; concrete value vocabulary may be profile/workflow-specific. |
| Deterministic result schema | Schema hooks used by validation/apply/check results. | Canonical hooks required; concrete schema refs may be `TBD`. |
| Review checklist result | Future artifact recording schema completeness, protected-path posture, boundary-language review, gate readiness, deterministic-check readiness, and unresolved implementation blockers. | Implementation `TBD` until artifact path/schema is accepted. |

## Example Minimal Proposal Shape

```json
{
  "proposal_id": "TBD",
  "profile_id": "TBD",
  "base_state": "TBD",
  "operation_name": "TBD",
  "status": "proposal_only",
  "lifecycle": "draft",
  "created_at": "TBD",
  "created_by": "TBD",
  "input_refs": [],
  "intended_changes": [],
  "deterministic_checks": [],
  "expected_output_refs": [],
  "risks": [],
  "assumptions": [],
  "blockers": [],
  "boundary_notice": "TBD",
  "required_human_gate": "TBD",
  "operation_risk_class": "engine_checkable",
  "provenance_on_judgment_values": "TBD",
  "storage_path": "TBD"
}
```

Values are `TBD` because no accepted engine profile, adapter, operation store, or operation instance exists in this future-boundary deliverable.

## Review Checklist

| Check | Question |
|---|---|
| Base state | Is `base_state` identified and reviewable? |
| Inputs | Are all `input_refs` identified and reviewable? |
| Intended changes | Are `intended_changes` specific enough for review? |
| Deterministic checks | Are checks named, tied to profile schema hooks, and ready to produce deterministic evidence? |
| Expected outputs | Are `expected_output_refs` proposal/review artifacts or approved adapter outputs, not direct protected-path writes by agents? |
| Risks/assumptions/blockers | Are known risks, assumptions, and blockers explicit? |
| Human gate | Is `required_human_gate` explicit, and is accepted/applied blocked until K-AUTH-2-bound approval exists? |
| Lifecycle | Does `status` remain `proposal_only`, with lifecycle carrying progression? |
| Review evidence | Does a future checklist result artifact record boundary-language, protected-path, human-gate, deterministic-check, and unresolved implementation-blocker findings or mark the artifact as `TBD`? |
| Boundary notice | Does the proposal avoid claims of professional approval, code compliance, certification, sealing, authentication, external validation, or Chirality-owned solver truth? |
