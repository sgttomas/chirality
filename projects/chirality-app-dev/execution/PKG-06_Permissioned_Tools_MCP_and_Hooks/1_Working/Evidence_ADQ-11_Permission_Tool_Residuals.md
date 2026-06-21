# Evidence - ADQ-11 Permission/Tool Residuals

Date: 2026-06-21

## Scope

This evidence records the ADQ-11 implementation work for bounded PKG-06 residuals from the
autonomous development queue:

- boot/version fingerprint for the runtime tool surface;
- explicit missing-register fallback for dependency reads;
- hook-side exact-edit stale-precondition checks;
- same-directory atomic-rename writes for Chirality-owned controlled status/dependency mutations.

This evidence does not perform lifecycle transitions, satisfy dependency rows, issue deliverables,
change provider policy, expand provider/network scope, implement R7, or make release, professional,
certification, sealing, authentication, release-readiness, or code-compliance claims.

## Implemented Evidence

| Evidence Area | Artifact |
|---|---|
| Runtime fingerprint schema | `frontend/src/lib/harness/runtime-fingerprint.ts` |
| SDK package version constant | `frontend/src/lib/harness/sdk-version.ts` |
| MCP server version constant | `frontend/src/lib/harness/mcp/tool-names.ts` |
| Boot metadata persistence | `frontend/src/app/api/harness/session/boot/route.ts`; `frontend/src/lib/harness/types.ts` |
| Shared SDK-version usage | `frontend/src/lib/harness/claude-agent-sdk-manager.ts`; `frontend/src/lib/harness/turn-engine.ts` |
| Boot fingerprint route assertions | `frontend/src/__tests__/api/harness/routes.test.ts` |
| Missing `Dependencies.csv` fallback | `frontend/src/lib/workspace/deliverable-contracts.ts` |
| Dependency fallback route coverage | `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` |
| API client snapshot shape | `frontend/src/lib/workspace/deliverable-api.ts`; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` |
| Exact-edit hook precondition | `frontend/src/lib/harness/chirality-hooks.ts` |
| Exact-edit hook evidence tests | `frontend/src/__tests__/lib/chirality-hooks.test.ts` |
| Atomic controlled text writes | `frontend/src/lib/atomic-write.ts`; `frontend/src/lib/lifecycle/transition.ts`; `frontend/src/lib/workspace/deliverable-contracts.ts` |
| Atomic-write coverage | `frontend/src/__tests__/lib/atomic-write.test.ts` |

## Validation

| Command | Result |
|---|---|
| `npm run typecheck` | PASS |
| `npm run test -- src/__tests__/lib/atomic-write.test.ts src/__tests__/api/working-root/deliverable-contracts.test.ts src/__tests__/api/harness/routes.test.ts src/__tests__/lib/chirality-hooks.test.ts src/__tests__/lib/workspace-deliverable-api.test.ts --testTimeout=15000` | PASS: 5 files / 73 tests |
| `npm run test -- src/__tests__/api/harness/routes.test.ts -t "supports session create/list/get/delete happy path" --testTimeout=20000` | PASS: isolated route timeout check |
| `npm run test -- src/__tests__/api/harness/routes.test.ts --testTimeout=15000` | PASS: 35 route tests after deterministic route-module preload |
| `npm run test -- --testTimeout=15000` | PASS: 73 files / 512 tests after deterministic route-module preload |
| `git diff --check` | PASS |
| `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` | PASS: no drift |

## Residuals

- Real Bash process interruption proof remains blocked/deferred. Current implementation has timeout,
  denial, metadata, artifact, and hook-failure evidence, but no end-to-end real-process cancellation
  fixture. The remaining work depends on the runtime terminal/interruption taxonomy boundary tracked
  by D-APP-40 and shared tool-result metadata policy tracked by D-APP-42.
- Dedicated PreCompact/Stop callback semantics remain blocked/deferred. Current implementation keeps
  the adapter-message compaction mirror and terminal status mapping, but does not add a new SDK hook
  callback path or declare the mirror sufficient. That acceptance needs the D-APP-40 terminal taxonomy
  ruling or explicit SDK lifecycle support.
