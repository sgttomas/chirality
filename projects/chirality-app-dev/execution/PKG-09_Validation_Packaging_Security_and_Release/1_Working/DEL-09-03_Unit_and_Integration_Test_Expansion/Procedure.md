# Procedure: DEL-09-03 Unit and Integration Test Expansion

## Purpose

This procedure describes how to produce and verify the DEL-09-03 test expansion artifacts while preserving the bounded scope, source-grounded requirements, and deferred dependency workflow.

## Prerequisites

| Prerequisite | Status / Note | Source |
|---|---|---|
| Accepted DEL-09-03 scope | Available in `_CONTEXT.md` and decomposition v3.2. | `_CONTEXT.md`; decomposition row DEL-09-03 |
| Authoritative source corpus | Available; REF-006 PRD has known hash mismatch treated as warning only. | `_REFERENCES.md`; TASK dispatch |
| Upstream dependencies | TBD; no accepted dependency edges have been extracted. | `_DEPENDENCIES.md` |
| Responsible party | TBD until human assignment. | `_CONTEXT.md` Source Authority |
| Implementation paths | TBD; exact frontend test directories/files must be identified during implementation work. | ASSUMPTION based on anticipated artifacts and `docs/PRD.md` Section 12.2 |

## Steps

1. Confirm the current source state.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the DEL-09-03 decomposition row.
   - Record the PRD hash mismatch as a warning, not a blocker, for this dispatched run.

2. Build the test inventory.
   - Map each test candidate to at least one source requirement or invariant.
   - Required behavior groups: TurnEngine, SSE compatibility, event replay, attachments, status lifecycle, dependencies, interrupts/cancellation, denied actions.
   - Mark unavailable or phase-dependent implementation surfaces as `TBD`.

3. Create or update unit tests.
   - Add TurnEngine lifecycle tests for `runTurn()` without HTTP.
   - Add event replay tests for append-only JSONL, malformed trailing line tolerance, event schema shape, and terminal outcome records.
   - Add parser/validator tests for `_STATUS.md` lifecycle and `Dependencies.csv` v3.1.
   - Add attachment resolver and permission overlay tests using fixtures.

4. Create or update API/integration tests.
   - Add `/api/harness/turn` SSE compatibility tests.
   - Add `/api/harness/interrupt` cancellation cleanup tests where implementation exists.
   - Add workspace status and dependency route tests where implementation exists.
   - Add denied-action integration tests for `dontAsk`, read-only posture, denied writes, denied Bash, and unknown tools where implementation exists.

5. Create fixtures and regression cases.
   - Use small named fixtures for symlink attachments, unsupported extensions, budget excess, malformed JSONL tail, invalid dependency rows, invalid status transitions, and denied tool requests.
   - Avoid storing secrets, API keys, or source paths that violate project-root containment.

6. Run local validation.
   - From `frontend/`, run `npm run test`.
   - Run `npm run typecheck` if touched test code requires TypeScript confidence or if source policy requires it for the change.
   - Run `npm run harness:validate:premerge` only when the change affects validation surfaces or route behavior.

7. Record evidence.
   - Capture passing command output or stable artifacts in the implementation run record or PR notes.
   - Do not create `Dependencies.csv` from this procedure; dependency extraction is a later workflow per `_DEPENDENCIES.md`.

## Verification

| Check | Pass Condition |
|---|---|
| Scope check | Tests map to DEL-09-03 behaviors and do not implement unrelated features. |
| Source check | Non-trivial assertions cite or trace to `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PRD.md`, or decomposition v3.2. |
| Event check | Accepted-turn, terminal, replay, and redaction tests align with product-owned `HarnessEvent` contracts. |
| API check | SSE route tests preserve browser event names and route shape. |
| Lifecycle check | `_STATUS.md` and `Dependencies.csv` tests follow SPEC sections 4 and 6. |
| Permission check | Deny-first behavior is tested as an enforcement boundary, not as prompt text. |
| Fixture check | Fixtures are deterministic, small, and free of secrets. |
| Command check | `npm run test` passes when dependencies and required instruction-root assets are present. |

## Records

- Test source files: TBD until implementation work identifies exact paths.
- Fixtures: TBD until implementation work identifies exact paths.
- Command evidence: TBD until implementation work runs validation.
- Four-document initialization run record: `_run_records/TASK_RUN_2026-05-20_1619.md`.
