# Evidence - CODEV-001 SDK Probe Record

Date: 2026-05-24

## ADQ-04 Superseding Note - 2026-06-21

This CODEV-001 probe record remains historical evidence for first-adapter package pins and
initial SDK isolation. It is superseded for current default-provider/adoption posture,
Section 9 validation naming, packaged live proof status, and REF-006 source-state posture
by `docs/harness/runtime_evidence_reconciliation.md` and the refreshed
`frontend/docs/harness/runtime_engine_contract.md`.

Current posture:

- The package pins remain `@anthropic-ai/claude-agent-sdk@0.3.150` and
  `@anthropic-ai/sdk@0.93.0`.
- D-APP-17 recorded a bounded packaged live `agentSdk` read-tool proof; D-APP-18 Option A
  approved the bounded key-aware default-provider implementation.
- The default is now key-aware: `agentSdk` when an Anthropic key is configured and no
  explicit provider override is set, otherwise `stub`. Explicit `stub`, `anthropic`, and
  `agentSdk` provider selections still win.
- The active Section 9 mapper ID is `section9.adapter_message_mapper`, not the older
  `section9.sdk_message_mapper` wording.
- D-APP-38 authority corpus `v1` resolves the earlier REF-006 hash-mismatch caveat for
  this evidence refresh.

This note does not authorize provider expansion, remote MCP/plugins/tool search, release or
distribution posture, lifecycle issuance, dependency-row closure, professional approval,
certification, sealing, authentication, or code-compliance acceptance.

## Probe Posture

This record covers the first CODEV-001 SDK probe implementation for DEL-04-01.
Historical posture at the time of this record: the SDK-backed runtime path was present only
behind explicit provider selection: `CHIRALITY_HARNESS_PROVIDER=agentSdk`. D-APP-18 later
superseded that default-selection posture with the key-aware default described above.

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

Historical note: this section recorded the 2026-05-24 REF-006 `HASH_MISMATCH` state.
D-APP-38 later established authority corpus `v1`, and current reconciliation status reports
REF-006 as `MATCH`. This historical caveat no longer describes current ADQ-04 evidence
posture, but it is retained to preserve the original run record.

## Dependency Closure Note

This record does not mark any `Dependencies.csv` row satisfied, waived, retired, or not
applicable. Follow-up dependency closure remains required after tranche evidence review.
