# Procedure: DEL-07-04 Status Transition API and MCP Tool

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
| Implementation module location | TBD. |

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
   - Apply the PRD Section 8.9 FR-054 acceptance detail: 7-64 character hex SHA-like token. PRD hash mismatch warning applies.

6. Implement the status API surface.
   - Provide `GET /api/working-root/deliverable/status` for read-only status snapshots.
   - Provide `POST /api/working-root/deliverable/status/transition` for allowed lifecycle transitions.
   - Return structured success and denial outcomes. Exact response schema is `TBD`.

7. Implement the Chirality MCP status tools.
   - Provide `mcp__chirality__status_read` for reading `_STATUS.md`.
   - Provide `mcp__chirality__status_transition` for write-gated status transitions.
   - Route MCP execution through the same permission, hook, path, redaction, and event logging policy as SDK built-ins.

8. Add tests for the deliverable acceptance surface.
   - Parser tests for valid and malformed `_STATUS.md`.
   - Transition tests for valid forward moves, invalid states, backward moves, unauthorized actors, missing approval SHA, and invalid SHA-like token.
   - API route tests for read and transition.
   - MCP tool tests for naming, schema, read/write mode, denial, and success.
   - Permission/path/hook tests for gated writes.

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

## Records

Expected records and artifacts:

- Status parser implementation.
- Transition validator implementation.
- Status API route or service tests.
- Chirality MCP status tool definitions and tests.
- Approval SHA test fixtures.
- Denial/success fixtures for actor authorization and forward-only lifecycle behavior.
- Runtime/event logging evidence for write-gated status transitions when the implementation surface supports it.

TBD records:

- Exact implementation file paths.
- Exact request/response schemas.
- Exact actor identity mapping.

## Source Warning

`docs/PRD.md` is listed as `HASH_MISMATCH` in `_REFERENCES.md`; reconcile the source hash before final acceptance of PRD-derived acceptance details.
