# Specification: DEL-07-04 Status Transition API and MCP Tool

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Scope

This deliverable specifies the backend slice that parses deliverable-local `_STATUS.md`, exposes status read/transition access through the working-root API and Chirality MCP tooling, and enforces lifecycle rules for state movement. The slice covers SOW-028 and supports OBJ-006 as recorded in `_CONTEXT.md` and the accepted SOFTWARE_DECOMP v3.2 entry for DEL-07-04.

In scope:

- `_STATUS.md` parser behavior for current state, last updated date, and history.
- Lifecycle transition validation for valid state sequence, forward-only movement, authorized actors, and approval SHA evidence for human gates.
- Status read and transition API contracts.
- `mcp__chirality__status_read` and `mcp__chirality__status_transition` tool behavior.
- Tests for parser, transition, actor authorization, approval SHA, and MCP/API exposure.

Out of scope:

- Dependency CSV parser/writer behavior except where status/dependency APIs share a contract surface.
- UI presentation beyond consuming the API/tool result.
- Remote MCP servers, plugin marketplaces, remote execution, or custom generic MCP transport.
- Autonomous approval, issue, release, certification, or professional validation.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-07-04-REQ-001 | The status parser SHALL read `_STATUS.md` as the canonical human-readable lifecycle file for a deliverable. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1; `docs/SPEC.md` Section 4.3 |
| DEL-07-04-REQ-002 | The parser SHALL extract `Current State`, `Last Updated`, and history entries from the `_STATUS.md` format. | `docs/SPEC.md` Section 4.1; `docs/PRD.md` Section 8.9 FR-052 |
| DEL-07-04-REQ-003 | The validator SHALL recognize the lifecycle order `OPEN -> INITIALIZED -> SEMANTIC_READY -> IN_PROGRESS -> CHECKING -> ISSUED`. | `docs/SPEC.md` Section 4.2; `docs/TYPES.md` Section 4.1 |
| DEL-07-04-REQ-004 | The validator SHALL reject backward transitions unless a human explicitly amends the record. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-053 |
| DEL-07-04-REQ-005 | The validator SHALL enforce actor authorization for lifecycle transitions according to SPEC Section 4.3. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-053 |
| DEL-07-04-REQ-006 | Transitions to `CHECKING` or `ISSUED` SHALL require approval SHA evidence; the PRD acceptance criterion is a 7-64 character hex SHA-like token. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-054 |
| DEL-07-04-REQ-007 | The implementation SHALL expose a status read API at `GET /api/working-root/deliverable/status`. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
| DEL-07-04-REQ-008 | The implementation SHALL expose a status transition API at `POST /api/working-root/deliverable/status/transition`. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
| DEL-07-04-REQ-009 | The implementation SHALL expose `mcp__chirality__status_read` and `mcp__chirality__status_transition` as Chirality MCP tool names. | `docs/SPEC.md` Section 14.2; `docs/TYPES.md` Section 8.4 |
| DEL-07-04-REQ-010 | `mcp__chirality__status_transition` SHALL be write-gated and SHALL apply authorized lifecycle transitions with approval SHA where required. | `docs/SPEC.md` Section 14.2; `docs/CONTRACT.md` Section 1.7 K-STATUS-2 |
| DEL-07-04-REQ-011 | Chirality MCP status tools SHALL pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/PRD.md` Section 8.13 FR-119 |
| DEL-07-04-REQ-012 | Deny-first behavior SHALL be preserved for status transitions; denial from policy, path check, hook, governance, SDK deny rule, or human gate blocks execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1; `docs/DIRECTIVE.md` Design commitments |
| DEL-07-04-REQ-013 | Status transition behavior SHALL NOT create or imply binding approval records by an agent, SDK, tool, runtime event, validator, or domain adapter. | `docs/CONTRACT.md` Section 1.2 K-AUTH-1/K-BIND-1; `docs/DIRECTIVE.md` Human authority |
| DEL-07-04-REQ-014 | Approval evidence SHALL bind to specific content, normally a git SHA or equivalent immutable evidence; content changes after approval void approval until review. | `docs/DIRECTIVE.md` Human authority; `docs/CONTRACT.md` Section 1.2 K-AUTH-2 |
| DEL-07-04-REQ-015 | Tests SHALL cover parser success/failure, invalid state handling, unauthorized actor rejection, backward transition rejection, approval SHA enforcement, and API/MCP routing. | `docs/PRD.md` Section 8.9 FR-052 through FR-054; decomposition DEL-07-04 anticipated artifacts |
| DEL-07-04-REQ-016 | Request and response payload schemas for status read, status transition, and MCP equivalents SHALL be captured as accepted schema fixtures before implementation acceptance; until accepted, exact fields remain `TBD`. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` API inventory; `docs/PRD.md` FR-079 |
| DEL-07-04-REQ-017 | Runtime actor identity mapping SHALL be explicit and fail closed for unmapped actors before transition authorization is treated as complete. The accepted human-gate string aliases are exactly `HUMAN`, `USER`, and `OPERATOR`; arbitrary `HUMAN*` prefixes are unmapped and MUST fail with `UNAUTHORIZED_ACTOR`. | `docs/SPEC.md` Section 4.3; `docs/CONTRACT.md` K-STATUS-2; D-APP-56 R4-P19 |
| DEL-07-04-REQ-018 | PRD-derived approval-SHA acceptance criteria SHALL NOT be treated as final implementation acceptance authority until the `docs/PRD.md` hash status: MATCH is reconciled or a human-approved bypass record is accepted. | `_REFERENCES.md` REF-006; `docs/SPEC.md` Section 3.1 file inventory for `HASH_VERIFICATION_BYPASS.jsonl`; `docs/SPEC.md` Section 7 reference hash behavior — reconciled under D-APP-38 |

## Standards

| Standard or source | Applicability |
|---|---|
| `docs/SPEC.md` Section 4 | Governs `_STATUS.md` format, lifecycle states, and transition rules. |
| `docs/SPEC.md` Sections 13 and 14.2 | Governs status API and Chirality MCP tool names. |
| `docs/CONTRACT.md` K-STATUS-1/K-STATUS-2 | Binding invariants for canonical status state and transition enforcement. |
| `docs/CONTRACT.md` K-MCP-1/K-PERM-1 | Binding invariants for MCP wrapper and deny-first behavior. |
| `docs/PRD.md` Section 8.9 | Product requirements for lifecycle and dependency contracts; MATCH status applies. — reconciled under D-APP-38 |
| `docs/TYPES.md` Section 4.1 | Defines lifecycle vocabulary and optional `INITIALIZED -> IN_PROGRESS` route when semantic lensing is skipped. |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-001, REQ-002 | Unit tests parse representative `_STATUS.md` files and return current state, last updated date, and history. |
| REQ-003, REQ-004 | Unit tests accept forward movement and reject backward or unknown-state transitions. |
| REQ-005, REQ-006 | Unit/API tests check authorized actors and require valid SHA-like approval evidence for `CHECKING` and `ISSUED`. |
| REQ-007, REQ-008 | API route tests verify request validation, status snapshot response, transition success, and transition denial results. |
| REQ-009, REQ-010 | MCP tool tests verify names, schemas, read/write mode, and gated transition behavior. |
| REQ-011, REQ-012 | Integration tests verify permission overlay, hook/path denials, and event logging behavior for MCP status operations. |
| REQ-013, REQ-014 | Tests or review checks verify output copy and event records do not present tool or agent actions as human approval. |
| REQ-015 | Test suite includes the anticipated artifacts from decomposition: status parser tests, transition API/tool tests, and approval SHA tests. |
| REQ-016 | Schema fixture tests cover status snapshot response, transition request, transition success response, transition denial response, and MCP input/output schemas after the accepted schemas exist. |
| REQ-017 | Actor authorization tests cover every SPEC Section 4.3 authorized transition plus unmapped/unsupported actor denial. |
| REQ-018 | Acceptance checklist verifies the PRD hash status: MATCH has been reconciled or explicitly bypassed before relying on PRD-specific SHA-token criteria as final. — reconciled under D-APP-38 |
| REQ-004, REQ-005, REQ-006, REQ-011, REQ-012 | Denial fixtures assert typed reasons for invalid state, backward transition, unauthorized actor, missing approval SHA, invalid approval SHA, policy/path denial, and malformed `_STATUS.md`. |

## Documentation

Required artifacts:

- Status parser.
- Transition API/tool.
- Approval SHA tests.
- MCP tool contract notes or schema fixtures.
- API contract tests for status read/transition.
- Permission/hook/path policy tests for write-gated transition behavior.
- PRD hash reconciliation or approved hash-bypass evidence before final PRD-derived acceptance claims.

TBD:

- Implementation module paths.
- Exact request/response payload schemas for the status API and MCP tools.
- Exact actor identity enum or policy mapping used by runtime callers.
- Exact success and denial payload field names until schema fixtures are accepted.

## Pass 3 Disposition Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| B-001 | Converted to explicit `TBD` schema-fixture requirement rather than invented payload fields. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` FR-079. |
| B-002 | Converted to explicit `TBD` actor-mapping requirement with fail-closed behavior. | `docs/SPEC.md` Section 4.3; `docs/CONTRACT.md` K-STATUS-2. |
| F-001 | Incorporated as a PRD hash reconciliation acceptance check. | `_REFERENCES.md` REF-006; `docs/SPEC.md` Section 3.1 and reference-hash behavior. |
| F-002 | Incorporated as schema fixture verification after schemas are accepted. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` FR-079. |
| X-001 | Incorporated as denial-reason fixture coverage. | `docs/CONTRACT.md` K-PERM-1/K-MCP-1/K-STATUS-2; `docs/SPEC.md` Sections 4.1-4.3. |

## Source Status

`docs/PRD.md` is listed as `MATCH` in `_REFERENCES.md`. Requirements using PRD clauses are retained because the source is locally accessible and explicitly listed, but the MATCH should be reconciled before treating PRD-derived acceptance details as final implementation authority. (reconciled under D-APP-38).
