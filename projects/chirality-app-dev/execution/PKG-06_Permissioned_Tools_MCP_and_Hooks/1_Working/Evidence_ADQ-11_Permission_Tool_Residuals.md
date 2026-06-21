# Evidence - ADQ-11 Permission/Tool Residuals

Date: 2026-06-21

## Scope

This evidence records ADQ-11 implementation and closure work for bounded PKG-06 residuals from the
autonomous development queue:

- boot/version fingerprint for the runtime tool surface;
- explicit missing-register fallback for dependency reads;
- hook-side exact-edit stale-precondition checks;
- same-directory atomic-rename writes for Chirality-owned controlled status/dependency mutations;
- interrupted Bash/tool result classification;
- PreCompact/Stop lifecycle closure through adapter message/status/result mapping.

This evidence does not perform lifecycle transitions, issue deliverables, change provider policy,
expand provider/network scope, implement R7, or make release, professional, certification, sealing,
authentication, release-readiness, or code-compliance claims.

## Ruling Basis

| Decision | Effect |
|---|---|
| D-APP-40 Option B | Explicit user interruption terminates as `turn.interrupted`; `turn.cancelled` remains reserved for non-user cancellation. |
| D-APP-42 Option A | Tool-result artifacts include SHA-256 for exact stored bytes, `toolName`, optional `turnId`, and `session-lifetime` retention. |
| D-APP-43 1B/2B/3B | `interrupted: true` tool results are non-success outcomes; PreCompact/Stop closure is satisfied by adapter lifecycle mapping; strict workspace/tool behavior is preferred over compatibility inference. |

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
| Interrupted tool-result classification | `frontend/src/lib/harness/tool-evidence.ts` |
| Interrupted Bash adapter fixture | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` |
| PreCompact/Stop adapter lifecycle fixture | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` |

## Closure Semantics

ADQ-11 treats interrupted SDK Bash/tool results as non-success tool outcomes. Deterministic
adapter-level proof is the default validation bar: a `Bash` tool result with `interrupted: true` maps
to `tool.failed`, preserves safe stdout/stderr byte metadata, and does not store raw stdout/stderr in
event data.

ADQ-11 does not add synthetic SDK hook callbacks for PreCompact or Stop. Closure is based on the
accepted adapter lifecycle surface:

- `context.compaction.started` from adapter status `compacting`;
- `context.compacted` from compact-boundary or compact-success messages;
- `context.compaction.failed` from compact-failure messages;
- `turn.completed` and `turn.failed` from terminal SDK result messages;
- `turn.interrupted` from the D-APP-40 interruption paths.

Missing dependency-register state remains explicit and non-inferential. `_DEPENDENCIES.md` may be
reported as a secondary summary when present, but structured dependency rows are not synthesized from
prose. Exact-edit hooks deny missing, unreadable, or stale `old_string` preconditions before SDK
execution. Chirality-owned controlled status/dependency writers use same-directory temp-file rename and
clean up temp files on failed rename.

## Validation

| Command | Result |
|---|---|
| `npm run test -- src/__tests__/lib/tool-evidence.test.ts src/__tests__/lib/sdk-message-mapper.test.ts --testTimeout=30000` | PASS: 2 files / 18 tests |
| `npm run test -- src/__tests__/lib/atomic-write.test.ts src/__tests__/api/working-root/deliverable-contracts.test.ts src/__tests__/api/harness/routes.test.ts src/__tests__/lib/chirality-hooks.test.ts src/__tests__/lib/workspace-deliverable-api.test.ts src/__tests__/lib/tool-evidence.test.ts src/__tests__/lib/sdk-message-mapper.test.ts --testTimeout=30000` | PASS: 7 files / 91 tests |
| `npm run typecheck` | PASS |
| `npm run test -- --testTimeout=30000` | PASS: 78 files / 537 tests |
| `npm run harness:validate:section9` | PASS: 14 checks |
| `npm run build` | PASS |
| `npm run harness:validate:premerge` | PASS after starting local Next dev server: Section 8 8 checks; Section 9 report-only 14 checks |
| Modified PKG-06 dependency CSV parse check | PASS |
| `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` | PASS: corpus `v2`, no drift |
| `git diff --check -- projects/chirality-app-dev` | PASS |

## Residuals

No ADQ-11 code/test/docs residual remains open under D-APP-43. Historical run records may still mention
earlier HASH_MISMATCH or blocked/deferred states; those records are archival. Active assessment,
memory, dependency, and queue surfaces are updated by the ADQ-11 closeout tranche.
