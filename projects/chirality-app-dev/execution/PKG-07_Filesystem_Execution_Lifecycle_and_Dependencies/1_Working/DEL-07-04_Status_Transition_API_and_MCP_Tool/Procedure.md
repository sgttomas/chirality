# Procedure: DEL-07-04 Status Transition API and MCP Tool

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

Define the working procedure to produce and verify the DEL-07-04 backend feature slice for status parsing, status transition enforcement, API exposure, and Chirality MCP tool exposure.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted scope entry for DEL-07-04 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`. |
| Authoritative lifecycle contract | Available in `docs/SPEC.md` Section 4 and `docs/CONTRACT.md` Section 1.7. |
| API/MCP contract references | Available in `docs/SPEC.md` Sections 13 and 14.2 and `docs/PRD.md` API inventory. |
| Permission/MCP boundary references | Available in `docs/CONTRACT.md` Section 1.6 and `docs/DIRECTIVE.md` design commitments. |
| Declared upstream dependencies | TBD; `_DEPENDENCIES.md` lists no accepted upstream edges yet. |
| Implementation module location | TBD; implementation owner must identify accepted module paths for working-root status APIs and Chirality MCP tools before implementation closeout. |
| Accepted schema fixtures | TBD; exact request/response fields remain unresolved until API and MCP schema fixtures are accepted. |

## Steps

1. Locate the implementation area for working-root deliverable APIs and Chirality MCP tools.
   - If no established location exists, record candidate module paths as `TBD` until accepted by the responsible implementer.

2. Implement or update the `_STATUS.md` parser.
   - Parse the SPEC Section 4.1 fields: title, `Current State`, `Last Updated`, and history.
   - Reject or report malformed files without inferring lifecycle state from other files.

3. Implement lifecycle state validation.
   - Recognize `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING`, and `ISSUED`.
   - Enforce the forward-only ordering from SPEC Section 4.2.
   - Include the TYPES Section 4.1 optional route from `INITIALIZED` to `IN_PROGRESS` when semantic lensing is skipped, subject to authorized actor rules.

4. Implement actor authorization.
   - Use the authorized actor table in SPEC Section 4.3 as the baseline.
   - Preserve `TBD` for exact runtime actor identity mapping until the implementation surface defines caller identities.

5. Implement human gate approval SHA checks.
   - Require approval SHA evidence for transitions to `CHECKING` or `ISSUED`.
   - Apply the PRD Section 8.9 FR-054 acceptance detail: 7-64 character hex SHA-like token. PRD hash status: MATCH status applies. (reconciled under D-APP-38).

6. Implement the status API surface.
   - Provide `GET /api/working-root/deliverable/status` for read-only status snapshots.
   - Provide `POST /api/working-root/deliverable/status/transition` for allowed lifecycle transitions.
   - Return structured success and denial outcomes. Exact response schema is `TBD`.
   - After schema acceptance, add fixtures for status snapshot responses, transition requests, transition success responses, and transition denial responses.

7. Implement the Chirality MCP status tools.
   - Provide `mcp__chirality__status_read` for reading `_STATUS.md`.
   - Provide `mcp__chirality__status_transition` for write-gated status transitions.
   - Route MCP execution through the same permission, hook, path, redaction, and event logging policy as SDK built-ins.
   - Record test evidence for permission decisions, path containment, hook outcomes, redaction behavior, and tool/runtime event logging for status operations.

8. Add tests for the deliverable acceptance surface.
   - Parser tests for valid and malformed `_STATUS.md`.
   - Transition tests for valid forward moves, invalid states, backward moves, unauthorized actors, missing approval SHA, and invalid SHA-like token.
   - API route tests for read and transition.
   - MCP tool tests for naming, schema, read/write mode, denial, and success.
   - Permission/path/hook tests for gated writes.
   - Denial payload tests for invalid state, backward transition, unauthorized actor, missing approval SHA, invalid approval SHA, path/policy denial, and malformed `_STATUS.md`.
   - Success payload tests once accepted field names exist.

9. Record unresolved implementation details.
   - Keep `TBD` for exact module paths, request/response schemas, and actor identity mapping until accepted by implementation owners or adjacent deliverables.

## Verification

| Check | Expected result |
|---|---|
| Parser fixture: valid `_STATUS.md` | Current state, last updated date, and history are returned. |
| Parser fixture: malformed `_STATUS.md` | Structured error is returned; no alternate file determines lifecycle state. |
| Transition fixture: forward authorized transition | Transition succeeds when policy/path checks pass. |
| Transition fixture: backward transition | Transition fails unless an explicit human amendment path exists. |
| Transition fixture: `CHECKING` or `ISSUED` without approval SHA | Transition fails. |
| Transition fixture: `CHECKING` or `ISSUED` with invalid SHA-like token | Transition fails under PRD FR-054 acceptance. |
| API tests | Status read and transition endpoints behave consistently with parser/validator. |
| MCP tests | `mcp__chirality__status_read` and `mcp__chirality__status_transition` expose deterministic Chirality operations and preserve policy overlays. |
| Boundary tests | Status transition does not imply human approval, professional validation, issue, or release. |
| Schema fixture tests | After schemas are accepted, exact request/response fixtures cover API and MCP read, transition success, and transition denial. |
| Audit overlay tests | Permission, hook, path-containment, redaction, and event logging evidence exists for MCP status operations. |

## Records

Expected records and artifacts:

- Status parser implementation.
- Transition validator implementation.
- Status API route or service tests.
- Chirality MCP status tool definitions and tests.
- Approval SHA test fixtures.
- Denial/success fixtures for actor authorization and forward-only lifecycle behavior.
- Runtime/event logging evidence for write-gated status transitions when the implementation surface supports it.
- Permission decision, hook outcome, path-containment, redaction, and event logging evidence for MCP status operations.
- PRD hash reconciliation or approved bypass evidence before final PRD-derived acceptance claims.

TBD records:

- Exact implementation file paths.
- Exact request/response schemas.
- Exact actor identity mapping.
- Exact success and denial payload fields.

## Pass 3 Disposition Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| D-001 | Converted to an explicit prerequisite and closeout blocker: accepted implementation module paths remain `TBD`. | `_DEPENDENCIES.md` DEP-07-04-008; decomposition DEL-07-04 anticipated artifacts. |
| F-002 | Incorporated as post-schema fixture verification for API/MCP request and response schemas. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` FR-079. |
| X-002 | Incorporated as audit evidence expectations for permission, hook, path, redaction, and event logging policy on MCP status operations. | `docs/CONTRACT.md` K-MCP-1/K-PERM-1; `docs/PRD.md` FR-092, FR-093, FR-104. |
| E-002 | Converted to explicit `TBD` success/denial payload fields until schema acceptance. | `docs/SPEC.md` API inventory; `docs/PRD.md` FR-079 and NFR-009. |

## Source Status

`docs/PRD.md` is listed as `MATCH` in `_REFERENCES.md`; reconcile the source hash before final acceptance of PRD-derived acceptance details. (reconciled under D-APP-38).

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-132 names the landed status-transition and MCP modules while leaving ResponsibleParty assignment human-owned.
