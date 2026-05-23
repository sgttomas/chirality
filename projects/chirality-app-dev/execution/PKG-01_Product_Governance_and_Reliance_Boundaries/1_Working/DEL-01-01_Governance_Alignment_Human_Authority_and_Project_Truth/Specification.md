# Specification: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

## Scope

This deliverable covers the governance-alignment work needed to keep `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and the active SOFTWARE_DECOMP v3.2 working surface mutually consistent as the runtime evolves.

The scope is bounded to preserving human authority, filesystem project truth, accepted git history, runtime-audit boundaries, product identity, professional-boundary posture, and reliance-boundary ownership. Runtime implementation details are excluded except where they are necessary to define or check a governance boundary.

ResponsibleParty remains `TBD` until assigned by a human.

## Requirements

| ReqID | Requirement | Source basis | Verification |
|---|---|---|---|
| DEL-01-01-REQ-001 | Governance alignment work must preserve the authority order: DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, PRD, then agent instructions and accepted execution records for concrete operations. | `docs/DIRECTIVE.md` Section 0. | Governance consistency notes identify any lower-authority conflict and proposed correction path. |
| DEL-01-01-REQ-002 | Human approval, professional acceptance, issue/release actions, residual-risk acceptance, and judgment conflict rulings must remain human-only. | `docs/DIRECTIVE.md` Sections 2.4 and 3; `docs/CONTRACT.md` K-AUTH/K-GATE/K-PROF. | Human-authority checklist confirms no automated approval claim is introduced. |
| DEL-01-01-REQ-003 | Agent, SDK, runtime, validator, deterministic tool, domain adapter, and runtime-event outputs must be described as drafts, evidence, diagnostics, or decision support unless accepted by a governed human process. | `docs/DIRECTIVE.md` Sections 2.3 and 3.1; `docs/CONTRACT.md` K-BIND-1. | Checklist reviews copy and document changes for binding/non-binding separation. |
| DEL-01-01-REQ-004 | Project truth must remain in versioned project files under the working root and accepted git history; hidden app state, chat, SDK transcripts, runtime logs, caches, model context, API keys, and provider transcripts must not be treated as project truth unless imported through governance. | `docs/DIRECTIVE.md` Sections 2.1, 2.2, 2.6; `docs/TYPES.md` Project Truth. | Project-truth checklist verifies claims and storage locations. |
| DEL-01-01-REQ-005 | Runtime events must support audit and replay without approving or issuing deliverables. | `docs/DIRECTIVE.md` Section 2.3; `docs/SPEC.md` Sections 8-10; `docs/PRD.md` session/audit requirements. | Runtime-audit checklist confirms `.chirality/sessions/<sessionId>/events.jsonl` is canonical and SDK transcripts are secondary unless imported. |
| DEL-01-01-REQ-006 | Product-critical reliance boundaries must be Chirality-owned or verified at explicit enforcement surfaces; prompt text and opaque SDK defaults are not sufficient for P0 boundaries. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1/K-RELIANCE-2; `docs/PLAN.md` R0/R1. | Acceptance checklist verifies each P0 reliance boundary has a documented non-prompt-only enforcement plan or an open gap. |
| DEL-01-01-REQ-007 | SDK adoption must remain privileged but replaceable; SDK APIs, transcript shape, tool names, and vendor defaults must not define Chirality public semantics or product identity. | `docs/DIRECTIVE.md` Sections 2.8-2.11; `docs/CONTRACT.md` K-ENGINE/K-SDK; `docs/PLAN.md` Controlling Runtime Direction. | Diff checklist verifies product-owned contracts and Chirality terminology remain intact. |
| DEL-01-01-REQ-008 | Unknown, unsupported, or conflicting facts must be represented as `TBD`, `ASSUMPTION`, `PROPOSAL`, source warning, or human-ruling-needed. | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1/K-CONFLICT-1; `AGENT_SOFTWARE_DECOMP.md`. | Review checks the four-document kit and later governance notes for unsupported claims. |
| DEL-01-01-REQ-009 | Lifecycle state must only transition according to SPEC; `OPEN -> INITIALIZED` is allowed after four required documents are written and non-empty. | `docs/SPEC.md` Section 4. | `_STATUS.md` updated only after `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
| DEL-01-01-REQ-010 | Dependency extraction remains deferred for this run and `Dependencies.csv` must not be created. | Dispatch assignment; `_DEPENDENCIES.md` initial population rule. | Absence of deliverable-local `Dependencies.csv`. |

## Standards

| Standard / governing source | Status |
|---|---|
| `docs/DIRECTIVE.md` | Accessible; hash match. |
| `docs/CONTRACT.md` | Accessible; hash match. |
| `docs/SPEC.md` | Accessible; hash match. |
| `docs/TYPES.md` | Accessible; hash match. |
| `docs/PLAN.md` | Accessible; hash match. |
| `docs/PRD.md` | Accessible; hash mismatch observed and treated as source warning, not blocker, by dispatch instruction. |
| Active decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Accessible. |
| `AGENT_SOFTWARE_DECOMP.md` | Accessible; hash match. |

## Verification

| Verification item | Method | Acceptance |
|---|---|---|
| Four-document kit exists | File check | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
| Human-authority preservation | Checklist review | No automated actor is represented as able to approve, issue, certify, sign, seal, externally validate, or make professional work reliable. |
| Project-truth preservation | Checklist review | Reliance-relevant facts are represented in project files and git evidence, not only runtime state or hidden memory. |
| Runtime-audit boundary | Checklist review | Runtime audit is evidence/replay support only; it does not replace approval records. |
| Cross-document consistency | Diff checklist | PRD, DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and decomposition remain aligned or conflicts are surfaced. |
| Source warning handling | Conflict/source-warning table | PRD hash mismatch and dispatch-path mismatch are visible pending human ruling. |
| Source-warning acceptance | Reference-row or human-ruling check | Clean reliance on a source-warning item requires the exact affected reference row, accepted hash update, or explicit human bypass decision to be recorded before the warning is treated as resolved. |
| Dependency deferral | Scope check | P3 does not create or update dependency records. |

## Documentation

The expected documentation artifacts are:

- Governance consistency notes.
- Human-authority checklist.
- Project-truth checklist.
- Runtime-audit boundary checklist.
- Document diff checklist.
- Acceptance checklist.
- Conflict/source-warning table for human rulings where source records disagree or source hashes are not accepted.

`TBD`: final artifact filenames and destination locations for the above checklists are not specified by the available sources. This includes the governance consistency notes, human-authority checklist, project-truth checklist, runtime-audit checklist, document diff checklist, acceptance checklist, and conflict/source-warning table.
