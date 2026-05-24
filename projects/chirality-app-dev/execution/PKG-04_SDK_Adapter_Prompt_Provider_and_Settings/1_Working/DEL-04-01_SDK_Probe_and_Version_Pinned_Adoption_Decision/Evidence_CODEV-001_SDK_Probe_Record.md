# Evidence - CODEV-001 SDK Probe Record

Date: 2026-05-24

## Probe Posture

This record covers the first CODEV-001 SDK probe implementation for DEL-04-01.
The SDK-backed runtime path is present only behind explicit provider selection:
`CHIRALITY_HARNESS_PROVIDER=agentSdk`.

No new user-visible read, write, bash, MCP, remote, plugin, or subagent tool capability is
enabled by this tranche.

## Version Evidence

| Item | Value | Evidence |
|---|---|---|
| Claude Agent SDK package | `@anthropic-ai/claude-agent-sdk@0.3.150` | `frontend/package.json`; `frontend/package-lock.json` |
| Anthropic SDK peer package | `@anthropic-ai/sdk@0.93.0` | `frontend/package.json`; `frontend/package-lock.json` |
| Peer dependency reason | Claude Agent SDK `0.3.150` requires `@anthropic-ai/sdk >=0.93.0` | npm install resolution |
| Claude Code subprocess version | BLOCKED_TBD | Requires live SDK query/init event from controlled environment. |

## Probe Evidence Matrix

| Evidence Area | Status | Evidence |
|---|---|---|
| Package pin and lockfile | PASS | `frontend/package.json`; `frontend/package-lock.json` |
| SDK provider isolated behind explicit mode | PASS | `frontend/src/lib/harness/runtime.ts`; `harness-runtime.test.ts` |
| SDK `settingSources` isolation | PASS | `frontend/src/lib/harness/sdk-options-builder.ts`; `sdk-options-builder.test.ts` |
| `user` / `local` setting source exclusion | PASS | `sdk-options-builder.test.ts` |
| Built-in tools disabled for tranche | PASS | `sdk-options-builder.test.ts` |
| SDK message to stable `UIEvent` mapping | PASS | `sdk-message-mapper.test.ts` |
| SDK message to `HarnessEvent` evidence mapping | PASS | `sdk-message-mapper.test.ts`; `claude-agent-sdk-manager.test.ts` |
| SDK session ID linkage metadata | PARTIAL | `SessionRecord.sdkSessionId`; route save path for `agentSdk`; live SDK session ID capture remains to be proven. |
| API key redaction helper | PASS | `frontend/src/lib/harness/run-logger.ts`; JSONL append path uses redaction. |
| Interrupt/cancel terminal behavior | PARTIAL | `ClaudeAgentSdkManager.interrupt()` calls SDK `interrupt()` and closes active query; live subprocess behavior remains `BLOCKED_TBD`. |
| Electron packaging | BLOCKED_TBD | Not executed in this tranche. |
| Adoption verdict | BLOCKED_TBD | No `ADOPT`, `ADOPT_WITH_RESIDUAL_RISK`, or `FALLBACK` decision is made by this tranche. |

## Source-State Caveat

REF-006 `docs/PRD.md` remains `HASH_MISMATCH` in `_REFERENCES.md`. PRD-derived runtime
direction remains visible but closure requires source-state confirmation or a human ruling.

## Dependency Closure Note

This record does not mark any `Dependencies.csv` row satisfied, waived, retired, or not
applicable. Follow-up dependency closure remains required after tranche evidence review.
