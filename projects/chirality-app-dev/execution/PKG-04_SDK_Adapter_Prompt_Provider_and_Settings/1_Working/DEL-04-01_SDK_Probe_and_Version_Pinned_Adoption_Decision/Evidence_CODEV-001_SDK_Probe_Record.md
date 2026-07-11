# Evidence - CODEV-001 SDK Probe Record

Date: 2026-05-24

## ADQ-04 / ADQ-15 Superseding Note - refreshed 2026-07-10

This CODEV-001 probe record remains historical evidence for first-adapter package pins and
initial SDK isolation. It is superseded for current default-provider posture, Section 9
validation naming, packaged proof status, and REF-006 source-state posture by
`docs/harness/runtime_evidence_reconciliation.md`,
`frontend/docs/harness/runtime_engine_contract.md`, and
`execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`.

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
- ADQ-15 produced fresh unsigned local package/DMG evidence and passing scripted no-live
  packaged Agent SDK subprocess proofs for both the build-directory and mounted-DMG
  layouts. That evidence proves packaged resolver discovery, executable posture, and
  controlled `CLAUDE_CONFIG_DIR` / `HOME` propagation; it is not a live provider turn or
  a release-readiness claim.
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

## Current Option-Shape And Payload-Provenance Crosswalk

| Evidence Area | Current proof | Remaining limit |
|---|---|---|
| Deterministic SDK option shape | `frontend/src/lib/harness/sdk-options-builder.ts`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` prove settings-source isolation, tool allow/deny construction, permission mode, hooks, `canUseTool`, MCP server attachment, resume, and delegated-agent option shaping. | These deterministic fixtures do not identify the exact bundled Claude subprocess version. |
| Provider selection | `frontend/src/lib/harness/runtime.ts`; `frontend/src/__tests__/lib/harness-runtime.test.ts`; D-APP-18; and `docs/harness/runtime_evidence_reconciliation.md` prove the current key-aware default and explicit-override precedence. | No provider expansion or new default semantics are authorized here. |
| SDK payload-to-product-event mapping | `frontend/src/lib/harness/sdk-message-mapper.ts`; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` provide the current raw SDK fixture provenance for stable `UIEvent` and persisted `HarnessEvent` mappings. | Exact live `query()` payload-sequence capture remains separate from deterministic fixture provenance. |
| Packaged subprocess integration | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`; `frontend/src/__tests__/scripts/verify-packaged-agent-sdk-runtime.test.ts`. | ADQ-15 is scripted no-live proof. It does not prove a live packaged provider turn, mounted-DMG live workflow parity, or the exact subprocess version reported by a live SDK init event. |
| Session/transcript linkage | `docs/harness/runtime_evidence_reconciliation.md`; `frontend/docs/harness/runtime_engine_contract.md`. | Exact live SDK session capture, transcript placement/acceptance, and downstream dependency closure remain outside this refresh. |

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
| Current key-aware provider selection | PASS | `frontend/src/lib/harness/runtime.ts`; `frontend/src/__tests__/lib/harness-runtime.test.ts`; D-APP-18; `docs/harness/runtime_evidence_reconciliation.md` |
| SDK `settingSources` isolation | PASS | `frontend/src/lib/harness/sdk-options-builder.ts`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` |
| `user` / `local` setting source exclusion | PASS | `frontend/src/__tests__/lib/sdk-options-builder.test.ts` |
| Current governed SDK option shape | PASS | `frontend/src/lib/harness/sdk-options-builder.ts`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` |
| SDK message to stable `UIEvent` mapping | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts`; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` |
| SDK message to `HarnessEvent` evidence mapping | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts`; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` |
| SDK session ID linkage metadata | PARTIAL | `SessionRecord.sdkSessionId`; route save path for `agentSdk`; live SDK session ID capture remains to be proven. |
| API key redaction helper | PASS | `frontend/src/lib/harness/run-logger.ts`; JSONL append path uses redaction. |
| Interrupt/cancel terminal behavior | PARTIAL | `ClaudeAgentSdkManager.interrupt()` calls SDK `interrupt()` and closes active query; live subprocess behavior remains `BLOCKED_TBD`. |
| Unsigned local Electron packaging and scripted packaged subprocess integration | PASS | ADQ-15 packaging/instruction-root evidence; build-directory and mounted-DMG scripted no-live proofs. Signing, notarization, publication, distribution, and release-readiness remain excluded. |
| Default-provider implementation disposition | RULED / LANDED | D-APP-18 Option A approved the bounded key-aware default-provider implementation; ADQ-04 reconciles the landed posture. This evidence refresh makes no new adoption ruling. |
| Exact live subprocess, payload-sequence, and session/transcript evidence | PARTIAL / TBD | Deterministic option/mapper fixtures and scripted packaged integration are current; exact subprocess version, live `query()` payload sequence, live packaged workflow parity, and accepted session/transcript placement remain separate residuals. |

## Source-State Caveat

Historical note: this section recorded the 2026-05-24 REF-006 `HASH_MISMATCH` state.
D-APP-38 later established authority corpus `v1`, and current reconciliation status reports
REF-006 as `MATCH`. This historical caveat no longer describes current ADQ-04 evidence
posture, but it is retained to preserve the original run record.

## Dependency Closure Note

This record does not mark any `Dependencies.csv` row satisfied, waived, retired, or not
applicable. Dependency-row mutation and hard closure are excluded from this evidence refresh.
Follow-up dependency closure remains required through its owning governed workflow.
