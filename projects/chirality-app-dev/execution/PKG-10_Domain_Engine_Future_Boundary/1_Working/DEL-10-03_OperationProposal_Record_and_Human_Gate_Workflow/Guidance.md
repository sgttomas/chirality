# Guidance: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Purpose

This deliverable preserves future compatibility for domain-engine operation workflows without turning Chirality into a domain solver. It defines how future domain operations should be represented as proposed, reviewable, human-gated records before any protected domain state can be changed.

## Principles

- Treat `OperationProposal` as a future proposal and audit record, not as permission to execute a domain operation by itself.
- Keep authoritative domain truth in the domain engine. Chirality governs interaction, proposals, records, review aids, and human gates.
- Keep protected domain paths separate from agent-writable proposal paths.
- Require deterministic checks before a future operation can be considered review-ready.
- Require explicit human acceptance before a future operation is applied.
- Preserve professional-boundary language: Chirality must not claim professional approval, code compliance, external validation, or solver truth ownership.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Future scope | Draft record/workflow surfaces only; do not activate domain-engine implementation in this package. | `_CONTEXT.md`; `docs/PRD.md` Section 8.17 |
| Proposal fields | Use the `OperationProposal` field list as the minimum record shape. | `docs/TYPES.md` Section 11.2 |
| Deterministic checks | Define check names and expected outcomes before review; exact result payload is TBD. | `docs/PRD.md` Section 8.17 FR-112 |
| Human gate | A proposal can support review, but application requires explicit human acceptance. | `docs/PRD.md` Section 8.17 FR-113 |
| Protected paths | Proposal outputs should be written to proposal/review locations, not protected model truth. | `docs/PRD.md` Section 8.17 FR-110/FR-111 |
| Professional boundary | Review copy and event records should avoid language that makes Chirality the approving professional or solver. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |
| Evidence blockers | Human acceptance evidence, deterministic check result payloads, adapter apply results, and review-checklist result artifacts are required future evidence slots but remain `TBD` until accepted by governed amendment. | `docs/PRD.md` Section 8.17 FR-112/FR-113; `docs/SPEC.md` domain endpoints note |
| Status transitions | Treat `ready_for_review`, `accepted`, `rejected`, and `applied` semantics as assumptions until human ruling defines the implementation lifecycle. | `docs/TYPES.md` Section 11.2; `_SEMANTIC_LENSING.md` F-002/E-001 |

## Terminology Map

| Term | Meaning in this deliverable | Current disposition |
|---|---|---|
| Human gate | The workflow point that prevents domain operation application without accountable human action. | Required by `docs/PRD.md` Section 8.17 FR-113 and `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3. |
| Explicit human acceptance | The required human action before application. | Required; concrete evidence format remains `TBD`. |
| `requiredHumanGate` | The `OperationProposal` field that names the required gate. | Required field; accepted value vocabulary remains `TBD`. |
| Acceptance evidence format | The future artifact proving acceptance or rejection for a specific proposal. | `TBD` blocker until actor/authority, timestamp, proposal binding, and accepted/rejected value pattern are defined. |
| Review checklist result | The future artifact recording schema completeness, protected-path posture, boundary-language review, gate readiness, deterministic check readiness, and unresolved blockers. | `TBD` blocker until implementation artifact location and schema are accepted. |

## Trade-offs

| Trade-off | Directional Decision |
|---|---|
| Rich proposal schema vs. early compatibility | Use the current `OperationProposal` fields as the stable minimum and leave unresolved implementation details as `TBD`. |
| Automated checks vs. human authority | Deterministic checks may support review, but they do not replace the required human acceptance gate. |
| Future domain support vs. current runtime focus | Preserve interfaces and documentation now; defer execution semantics until governed amendment. |
| Core runtime simplicity vs. domain-specific behavior | Keep engine-specific assumptions in future profiles/adapters, not in Chirality core. |
| Status clarity vs. premature implementation | Use the enum from `docs/TYPES.md` now, but keep transition thresholds as assumptions until a future workflow owner accepts lifecycle semantics. |

## Examples

### Minimal Proposal Shape

```json
{
  "proposalId": "TBD",
  "profileId": "TBD",
  "operationName": "TBD",
  "createdAt": "TBD",
  "createdBy": "TBD",
  "inputRefs": [],
  "intendedChanges": [],
  "deterministicChecks": [],
  "expectedOutputRefs": [],
  "risks": [],
  "requiredHumanGate": "TBD",
  "status": "draft"
}
```

Source: `docs/TYPES.md` Section 11.2. Values are `TBD` because no accepted engine profile, adapter, or operation instance exists in this future-boundary deliverable.

### Review Checklist

| Check | Question |
|---|---|
| Inputs | Are all `inputRefs` identified and reviewable? |
| Intended changes | Are `intendedChanges` specific enough for review? |
| Deterministic checks | Are required checks named, executable by an approved future adapter, and recorded? |
| Expected outputs | Are `expectedOutputRefs` proposal/review artifacts or approved adapter outputs, not direct protected-path writes by agents? |
| Risks | Are known risks listed, with `TBD` where evidence is missing? |
| Human gate | Is `requiredHumanGate` explicit and unresolved gate evidence marked `TBD`? |
| Acceptance evidence | Is the acceptance/rejection artifact format, actor/authority, timestamp, and proposal binding defined or explicitly blocked as `TBD`? |
| Review evidence | Does a review-checklist result artifact record boundary-language, protected-path, human-gate, deterministic-check, and unresolved-blocker findings or mark the artifact as `TBD`? |
| Boundary notice | Does the proposal avoid claims of professional approval, code compliance, external validation, or Chirality-owned solver truth? |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-10-03-001 | `_REFERENCES.md` records a PRD hash mismatch, while the invocation directs treating it as a source warning only. | `_REFERENCES.md` REF-006 | Assignment runtime instruction | All PRD-grounded sections | Use PRD Section 8.17 as accessible source with warning noted. | TBD |
| CT-10-03-002 | Exact `requiredHumanGate` value format and acceptance evidence are not defined in the accessible slices. | `docs/TYPES.md` Section 11.2 | `docs/PRD.md` Section 8.17 | Specification Documentation; Procedure Records | Keep fields mandatory but mark concrete evidence format `TBD`. | TBD |
| CT-10-03-003 | Proposal status values are defined, but transition thresholds and rationale are not accepted implementation requirements. | `docs/TYPES.md` Section 11.2 | Procedure Step 8 assumptions | Procedure Steps; Guidance Considerations | Keep enum values authoritative and transition rationale as `ASSUMPTION` pending human ruling. | TBD |
