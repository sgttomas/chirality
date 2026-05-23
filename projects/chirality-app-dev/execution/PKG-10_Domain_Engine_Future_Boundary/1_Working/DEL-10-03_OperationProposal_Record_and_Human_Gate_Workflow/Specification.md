# Specification: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Scope

This deliverable defines a future-boundary data model and review workflow for `OperationProposal` records. It covers the proposal record shape, required human-gate posture, and review checklist for future domain-engine operations.

This deliverable excludes current-release domain operation execution, domain adapter implementation, protected-path enforcement implementation, and any claim that Chirality owns solver truth. Those items remain future amendment or sibling-deliverable scope.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-10-03-001 | The future operation proposal record MUST include the fields defined for `OperationProposal`: `proposalId`, `profileId`, `operationName`, `createdAt`, `createdBy`, `inputRefs`, `intendedChanges`, `deterministicChecks`, `expectedOutputRefs`, `risks`, `requiredHumanGate`, and `status`. | `docs/TYPES.md` Section 11.2 | Compare proposed schema/checklist against the field list. |
| REQ-10-03-002 | The future operation proposal status values MUST remain `draft`, `ready_for_review`, `accepted`, `rejected`, and `applied` unless amended through governed change. | `docs/TYPES.md` Section 11.2 | Confirm status enum values in proposal record documentation. |
| REQ-10-03-003 | Domain operations MUST be represented as `OperationProposal` records before application. | `docs/PRD.md` Section 8.17 FR-112; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Review workflow has a proposal-record step before any apply step. |
| REQ-10-03-004 | Applying a domain operation MUST require explicit human acceptance. | `docs/PRD.md` Section 8.17 FR-113; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Review checklist requires a human gate before application. |
| REQ-10-03-005 | Proposal records MUST identify inputs, intended changes, deterministic checks, expected outputs, risks, and required human gates. | `docs/PRD.md` Section 8.17 FR-112; `docs/TYPES.md` Section 11.2 | Required fields are present and non-empty or marked `TBD` before review. |
| REQ-10-03-006 | Agents MUST write proposals, summaries, and review aids, not protected domain-engine model truth. | `docs/PRD.md` Section 8.17 FR-111; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 | Review checklist confirms proposed outputs target proposal/review paths, not protected paths. |
| REQ-10-03-007 | Domain-engine outputs MUST NOT be represented as professional approval, code compliance, external validation, or solver truth owned by Chirality. | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 | Review checklist includes professional-boundary copy check. |
| REQ-10-03-008 | ASSUMPTION: A proposal should not reach `applied` status without a successful deterministic adapter/application workflow and recorded human acceptance. | `docs/PRD.md` Section 8.17; `docs/SPEC.md` future domain endpoints note | Human ruling required before treating this as accepted lifecycle semantics. |

## Standards

| Standard or Source | Applicability |
|---|---|
| `docs/TYPES.md` Section 11.2 | Authoritative local vocabulary and target shape for `OperationProposal`. |
| `docs/PRD.md` Section 8.17 | Product requirements for future domain-engine compatibility. Source warning: hash mismatch recorded in `_REFERENCES.md`; invocation permits use as warning-only. |
| `docs/CONTRACT.md` Section 1.10 | Binding invariants for domain-engine future scope. |
| `docs/SPEC.md` domain endpoint list and future profile note | Future API surface context; endpoint behavior details are TBD. |

## Verification

| Check | Method | Result Target |
|---|---|---|
| Schema completeness | Verify every `OperationProposal` field from `docs/TYPES.md` Section 11.2 appears in the record shape or checklist. | PASS/TBD |
| Status integrity | Verify status values match the enum in `docs/TYPES.md`. | PASS/TBD |
| Human gate | Verify every apply path requires explicit human acceptance. | PASS/TBD |
| Protected path posture | Verify proposal outputs do not directly modify protected domain-engine paths. | PASS/TBD |
| Boundary language | Verify no text claims Chirality approves, validates, or owns solver truth. | PASS/TBD |
| Future-boundary constraint | Verify implementation activation is excluded until governed amendment. | PASS/TBD |

## Documentation

Required artifacts for this deliverable:

- Proposal record shape.
- Gate workflow notes.
- Review checklist.

Additional documentation needed before implementation:

- TBD: exact proposal ID generation semantics.
- TBD: human acceptance evidence format.
- TBD: deterministic check result schema.
- TBD: adapter apply result schema.
- TBD: relationship between `requiredHumanGate` and broader lifecycle approval SHA semantics.
