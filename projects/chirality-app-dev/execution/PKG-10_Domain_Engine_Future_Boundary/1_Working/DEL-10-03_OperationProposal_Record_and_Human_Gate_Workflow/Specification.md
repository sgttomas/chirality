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
| REQ-10-03-009 | Human acceptance evidence MUST remain a named `TBD` implementation blocker until the accepted artifact format, actor/authority field, timestamp rule, and proposal identifier binding are defined. | `docs/PRD.md` Section 8.17 FR-113; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3; `_SEMANTIC_LENSING.md` A-001/X-001 | Review checklist blocks application when the acceptance evidence artifact or `requiredHumanGate` value is unresolved. |
| REQ-10-03-010 | Deterministic check evidence MUST remain a named `TBD` implementation blocker until the result payload, pass/fail semantics, adapter/profile reference, and provenance location are defined. | `docs/PRD.md` Section 8.17 FR-112; `docs/TYPES.md` Section 11.2; `_SEMANTIC_LENSING.md` F-001/D-001 | Review checklist blocks review closure when deterministic check result records or adapter apply results are unresolved. |
| REQ-10-03-011 | Review sufficiency evidence MUST identify a future review-checklist artifact that records schema completeness, boundary-language review, protected-path posture, human-gate status, and unresolved `TBD` blockers. | `docs/PRD.md` Section 8.17 FR-110 through FR-115; `docs/CONTRACT.md` Section 1.10; `_SEMANTIC_LENSING.md` X-002 | Review closure requires a checklist result artifact or explicit `TBD` blocker. |

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
| Acceptance evidence | Verify the acceptance/rejection artifact format, actor/authority, timestamp, and proposal binding are defined or explicitly blocked as `TBD`. | PASS/TBD |
| Deterministic result evidence | Verify deterministic check result payload and adapter validation/apply result schema are defined or explicitly blocked as `TBD`. | PASS/TBD |
| Review sufficiency evidence | Verify a review-checklist result artifact records boundary-language, protected-path, human-gate, and unresolved-blocker findings. | PASS/TBD |

## Documentation

Required artifacts for this deliverable:

- Proposal record shape.
- Gate workflow notes.
- Review checklist.

Additional documentation needed before implementation:

- TBD: exact proposal ID generation semantics.
- TBD: human acceptance evidence format, including actor/authority field, timestamp rule, proposal identifier binding, and accepted/rejected value pattern.
- TBD: exact `requiredHumanGate` value vocabulary and relationship to the human acceptance evidence artifact.
- TBD: deterministic check result schema, including check name, adapter/profile reference, pass/fail result, evidence path, and failure reason field.
- TBD: adapter validation/apply result schema, including operation identifier, accepted proposal reference, output references, and failure/rollback note.
- TBD: review checklist result artifact that substantiates protected-path posture, boundary-language review, human-gate readiness, deterministic check readiness, and unresolved blockers.
- TBD: relationship between `requiredHumanGate` and broader lifecycle approval SHA semantics.
