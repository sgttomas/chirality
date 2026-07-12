# Procedure: DEL-09-03 Unit and Integration Test Expansion

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

This procedure describes how to produce and verify the DEL-09-03 test expansion artifacts while preserving the bounded scope, source-grounded requirements, and deferred dependency workflow.

## Prerequisites

| Prerequisite | Status / Note | Source |
|---|---|---|
| Accepted DEL-09-03 scope | Available in `_CONTEXT.md` and decomposition v3.2. | `_CONTEXT.md`; decomposition row DEL-09-03 |
| Authoritative source corpus | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; TASK dispatch — reconciled under D-APP-38 |
| Upstream dependencies | `Dependencies.csv` exists with 13 ACTIVE extracted rows and all satisfaction statuses remain `TBD`; final release-readiness review must either satisfy, waive, or explicitly defer applicable dependency evidence. | `_DEPENDENCIES.md`; `Dependencies.csv`; `_run_records/TASK_RUN_2026-05-20_2102.md` |
| Responsible party | TBD until human assignment. | `_CONTEXT.md` Source Authority |
| Implementation paths | TBD; exact frontend test directories/files must be identified during implementation work. | ASSUMPTION based on anticipated artifacts and `docs/PRD.md` Section 12.2 |

## Steps

1. Confirm the current source state.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the DEL-09-03 decomposition row.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

2. Build the test inventory.
   - Map each test candidate to at least one source requirement or invariant.
   - Required behavior groups: TurnEngine, SSE compatibility, event replay, attachments, status lifecycle, dependencies, interrupts/cancellation, denied actions.
   - For closure, record at least one implemented test case, explicit deferral, or blocker for each required behavior group.
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
   - Replace fixture path `TBD`s only when actual fixture files exist; otherwise record the planned fixture class and the blocking implementation-path decision.
   - Avoid storing secrets, API keys, or source paths that violate project-root containment.

6. Run local validation.
   - From `frontend/`, run `npm run test`.
   - Run `npm run typecheck` if touched test code requires TypeScript confidence or if source policy requires it for the change.
   - Run `npm run harness:validate:premerge` only when the change affects validation surfaces or route behavior.

7. Record evidence.
   - Capture passing command output or stable artifacts in the implementation run record or PR notes.
   - Record final test source files, fixture files, behavior-group coverage decisions, and validation commands before closure.
   - Do not regenerate `Dependencies.csv` from this procedure; consume the existing dependency register as review context unless a separate dependency workflow is dispatched.

## Verification

| Check | Pass Condition |
|---|---|
| Scope check | Tests map to DEL-09-03 behaviors and do not implement unrelated features. |
| Source check | Non-trivial assertions cite or trace to `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PRD.md`, or decomposition v3.2. |
| Event check | Accepted-turn, terminal, replay, and redaction tests align with product-owned `HarnessEvent` contracts. |
| API check | SSE route tests preserve browser event names and route shape. |
| Lifecycle check | `_STATUS.md` and `Dependencies.csv` tests follow SPEC sections 4 and 6. |
| Permission check | Explicit hard-deny precedence is tested as an enforcement boundary, not as prompt text. |
| Fixture check | Fixtures are deterministic, small, and free of secrets. |
| Command check | `npm run test` passes when dependencies and required instruction-root assets are present. |
| Closure evidence check | Test source paths, fixture paths, behavior-group coverage decisions, and command evidence are recorded, or explicitly remain `TBD` with a blocker. |

## Records

- Test source files: TBD until implementation work identifies exact paths.
- Fixtures: TBD until implementation work identifies exact paths.
- Command evidence: TBD until implementation work runs validation.
- Behavior-group closure: TBD until implementation work records implemented tests, explicit deferrals, or blockers for TurnEngine, SSE compatibility, event replay, attachments, status lifecycle, dependencies, interrupts/cancellation, and denied actions.
- Dependency review evidence: existing `Dependencies.csv` contains 13 ACTIVE rows with satisfaction `TBD`; final release-readiness review must resolve or explicitly defer applicable dependency evidence.
- Four-document initialization run record: `_run_records/TASK_RUN_2026-05-20_1619.md`.

## Pass 3 Semantic Lensing Disposition

| ItemID | Disposition | Evidence / Reread |
|---|---|---|
| A-001 | Incorporated. | Added DEL-09-03-REQ-011 requiring one implemented or explicitly deferred test decision per required behavior group. Reread: `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Sections 12.5-12.6; decomposition DEL-09-03 row. |
| B-001 | Incorporated as closure evidence. | Records now require final test source files, fixture files, behavior-group coverage decisions, and command evidence, or explicit `TBD` blockers. Reread: Procedure Records; `docs/PRD.md` Section 12.2. |
| C-001 | Incorporated as prerequisite and fixture guard. | Procedure keeps implementation paths `TBD` until selected and Step 5 now blocks fixture path replacement until actual files exist. Reread: Procedure Prerequisites and Steps; `docs/PRD.md` Section 12.2. |
| F-001 | Incorporated. | Added DEL-09-03-REQ-012 and closure-evidence verification for stable `npm run test` evidence. Reread: `docs/CONTRACT.md` K-VALIDATE-1; `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1. |
| D-001 | Already covered and preserved. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| X-001 | Incorporated as closure evidence. | Records now require test source paths, fixture paths, behavior-group coverage decisions, and command evidence before determination closure, with blockers if still `TBD`. Reread: Procedure Records and Verification. |
| E-001 | Incorporated as fixture-path guard. | Step 5 now requires actual fixture files before replacing fixture path `TBD`s for symlink, budget, malformed JSONL, dependency, status, and denied-tool cases. Reread: `docs/SPEC.md` Sections 9.2 and 16.1; `docs/PRD.md` Sections 12.5-12.6. |
| E-002 | Incorporated with current dependency state. | Prerequisites and Records now note existing `Dependencies.csv`, 13 ACTIVE rows, and satisfaction `TBD`; final release-readiness review must resolve or explicitly defer applicable dependency evidence. Reread: `_DEPENDENCIES.md`, `Dependencies.csv`, and `_run_records/TASK_RUN_2026-05-20_2102.md`. |
