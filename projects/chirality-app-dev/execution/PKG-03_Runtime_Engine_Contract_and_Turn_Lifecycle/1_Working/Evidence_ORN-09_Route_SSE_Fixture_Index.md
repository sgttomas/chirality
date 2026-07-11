# ORN-09 Route / SSE Fixture Index

**Scope:** DEL-03-03 and DEL-03-04 implementation evidence only. This index does not issue either deliverable or change lifecycle, dependency, release, or approval status.

**Baseline basis:** branch `codex/app-dev-orn-remediation`, starting commit `dc9c50ca6b7216f200cceeaf745bcd42f2c0d27b`. ORN-09 changes were validated in the working tree and were not committed by the bounded TASK run.

## Route and terminal-path fixtures

| Path | Exact fixture | Assertion surface |
|---|---|---|
| Pre-stream missing session | `frontend/src/__tests__/api/harness/routes.test.ts:521` | HTTP `404`, typed `SESSION_NOT_FOUND`, provider not started. |
| Normal SSE success | `frontend/src/__tests__/api/harness/routes.test.ts:551` | Ordered compact events ending in `process:exit`. |
| Mid-stream runtime failure | `frontend/src/__tests__/api/harness/routes.test.ts:825` | Typed `turn:error` and failing `process:exit` metadata. |
| Pre-stream missing key | `frontend/src/__tests__/api/harness/routes.test.ts:852` | HTTP `503`, typed `MISSING_API_KEY`. |
| Same-session exclusion and recovery | `frontend/src/__tests__/api/harness/routes.test.ts:1065` | `TURN_IN_PROGRESS` during overlap; lock is reusable after terminal completion. |
| Explicit user interrupt | `frontend/src/__tests__/api/harness/routes.test.ts:1133` | D-APP-40 `turn.interrupted` plus `process:exit.interrupted=true`. |
| Client disconnect / reader cancellation | `frontend/src/__tests__/api/harness/routes.test.ts:1185` | `ReadableStreamDefaultReader.cancel()` persists `turn.cancelled`, never interruption events, releases the lock, preserves the shared turn ID, and recovers redacted `message.accepted` despite malformed trailing JSONL. |
| Cross-bundle interrupt coherence | `frontend/src/__tests__/api/harness/routes.test.ts:1250` | Explicit interruption survives route/runtime module boundary reset. |
| General malformed JSONL replay | `frontend/src/__tests__/api/harness/routes.test.ts:1406` | Valid records survive and malformed-line count remains honest. |
| Route-independent lock/cancel dispatch | `frontend/src/__tests__/lib/turn-engine.test.ts:211` | Optional provider `cancel()` is used; `interrupt()` is not used for non-user cancellation. |

## Implementation pointers

- Accepted raw user input is persisted before provider iteration at `frontend/src/lib/harness/turn-engine.ts:295` and shares its generated turn ID with adapter lifecycle dispatch at `frontend/src/lib/harness/turn-engine.ts:375`.
- Disconnect cancellation is persisted once and releases the session lock at `frontend/src/lib/harness/turn-engine.ts:327`.
- Claude provider cancellation is distinct from explicit interruption at `frontend/src/lib/harness/claude-agent-sdk-manager.ts:90` and `frontend/src/lib/harness/claude-agent-sdk-manager.ts:112`.
- Anthropic provider cancellation is distinct from explicit interruption at `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts:700` and `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts:722`.

## Validation

- `npx vitest run src/__tests__/lib/turn-engine.test.ts src/__tests__/lib/claude-agent-sdk-manager.test.ts src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts src/__tests__/api/harness/routes.test.ts` — PASS, 126/126 tests.
- `npx tsc --noEmit` — PASS.
