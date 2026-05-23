# Specification: DEL-09-03 Unit and Integration Test Expansion

## Scope

DEL-09-03 shall define and implement focused unit, API, and integration test expansion for TurnEngine, SSE compatibility, event replay, attachment validation, status lifecycle behavior, dependency register behavior, interrupts/cancellation, and denied actions.

This deliverable excludes feature implementation except test fixtures and packaging glue, and it shall not create or populate `Dependencies.csv` during this four-document initialization run. Source: `_CONTEXT.md` Package Scope and Deliverable Scope; decomposition row for DEL-09-03.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| DEL-09-03-REQ-001 | Tests shall cover `TurnEngine.runTurn()` as a product-owned lifecycle boundary, separate from HTTP route ownership. | Unit tests instantiate or exercise TurnEngine without HTTP; assertions cover accepted-turn persistence, event yield, terminal outcomes, and adapter boundary behavior. Source: `docs/SPEC.md` Section 10; `docs/PRD.md` FR-070 and Section 12.5. |
| DEL-09-03-REQ-002 | Tests shall preserve `/api/harness/turn` SSE route compatibility, including stable browser event names. | API/integration tests assert `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, and `process:exit` behavior as applicable. Source: `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3. |
| DEL-09-03-REQ-003 | Tests shall verify that accepted user input is persisted before SDK/model execution begins. | Integration or unit tests assert `turn.accepted` precedes model/request execution records. Source: `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` Sections 8.12 and 12.6. |
| DEL-09-03-REQ-004 | Tests shall verify every accepted turn reaches a durable terminal success, failure, cancellation, or interruption event. | Tests assert terminal event persistence for success, failure, interrupt, and cancellation paths. Source: `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-073 and Section 12.6. |
| DEL-09-03-REQ-005 | Tests shall cover append-only `HarnessEvent` JSONL replay, including malformed trailing line tolerance and preservation of valid prior events. | Unit tests write valid events plus malformed tail and assert replay diagnostics without loss of valid prior events. Source: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5. |
| DEL-09-03-REQ-006 | Tests shall verify attachment resolver enforcement for path validation, regular-file status, symlink rejection, extension allowlist, readability, per-file 10 MB limit, total raw-byte 18 MB limit, partial failure, and all-failure empty-text rejection. | Attachment resolver unit/API tests use fixtures for allowed file types, symlink/path failures, budget failures, partial failure, and `ATTACHMENT_FAILURE`. Source: `docs/SPEC.md` Section 16.1; `docs/CONTRACT.md` K-ATTACH-1. |
| DEL-09-03-REQ-007 | Tests shall verify `_STATUS.md` parsing and forward-only lifecycle transition enforcement, including approval SHA requirements for `CHECKING` and `ISSUED`. | Status parser/API tests cover valid states, invalid/backward transitions, unauthorized actors, and SHA-like token requirements. Source: `docs/SPEC.md` Section 4; `docs/PRD.md` FR-052 through FR-054. |
| DEL-09-03-REQ-008 | Tests shall verify `Dependencies.csv` v3.1 parsing, validation, writing, provenance preservation, host deliverable consistency, row retirement, and legacy normalization. | Dependency parser/writer/linter tests assert required headers, enums, `FromDeliverableID` consistency, active extracted-row evidence fields, and retired-not-deleted behavior. Source: `docs/SPEC.md` Section 6; `docs/PRD.md` FR-055 through FR-057. |
| DEL-09-03-REQ-009 | Tests shall verify denied actions do not execute and, where runtime event support exists, emit permission/runtime events. | Permission tests cover deny-over-allow, `dontAsk`, `readOnly`, unknown tool names, denied writes, denied Bash, hook failure, and structured decisions. Source: `docs/SPEC.md` Sections 14-15; `docs/CONTRACT.md` K-PERM-1 through K-PERM-5 and K-BASH-1. |
| DEL-09-03-REQ-010 | Tests shall keep public APIs and canonical events provider-neutral, with SDK-specific names and IDs only as adapter metadata. | Conformance tests reject SDK-shaped leakage in public APIs and canonical `HarnessEvent` fields except explicit adapter metadata. Source: `docs/SPEC.md` Section 10.3; `docs/PRD.md` FR-122 and FR-123. |

## Standards

| Standard / Source | Applicability |
|---|---|
| `docs/CONTRACT.md` | Binding invariants for event audit, permissions, lifecycle, dependencies, attachments, validation, and no-invention behavior. |
| `docs/SPEC.md` | Physical file/API/runtime contracts for `_STATUS.md`, `Dependencies.csv`, `HarnessEvent`, TurnEngine, SSE, tools, permissions, and attachments. |
| `docs/TYPES.md` | Vocabulary and canonical terms for runtime, session, permission, validation, and dependency concepts. |
| `docs/PRD.md` | Product requirements for validation/test coverage and runtime behavior; hash mismatch is a source warning only for this run. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Accepted decomposition routing, DEL-09-03 scope, SOW mapping, and objective mapping. |

## Verification

| Verification Item | Required Evidence |
|---|---|
| Unit tests | Jest or equivalent unit tests for TurnEngine, event replay, attachment resolver, status parser, dependency parser/writer/linter, permission overlay, and hook behavior. |
| API tests | `/api/harness/turn`, `/api/harness/interrupt`, `/api/working-root/deliverable/status`, and `/api/working-root/deliverable/dependencies` route tests where implemented. |
| Integration tests | Accepted-turn-before-execution, interrupt cancellation, SSE compatibility, denied write under `dontAsk`, denied Bash, and governed allowed-write paths when those phases are available. |
| Regression fixtures | Files and runtime records for malformed JSONL, symlinks, budget-sized attachments, invalid dependency rows, invalid status transitions, unknown tools, and denied permission cases. |
| Command gate | `npm run test` from `frontend/` remains passing when dependencies and required instruction-root assets are present. Source: `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1. |

## Documentation

- Test names or descriptions should cite the governing contract section or FR where practical.
- Any unsupported implementation target remains `TBD` rather than being converted into a false requirement.
- Test fixtures should be documented enough to distinguish source-derived requirements from assumptions.
- ResponsibleParty remains TBD until assigned by a human.
