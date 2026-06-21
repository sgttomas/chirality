# Runtime Evidence Reconciliation

**Date:** 2026-06-21
**Queue item:** ADQ-04
**Scope:** PKG-03 runtime engine contract and PKG-04 SDK adapter / provider settings evidence.

This record refreshes evidence and spec-to-implementation crosswalks only. It does not
change runtime code, provider/network scope, release/distribution posture, lifecycle state,
dependency rows, professional approval, certification, sealing, authentication, or
code-compliance acceptance.

G5 naming and taxonomy questions remain queued for ADQ-05: `runTurn` / `startTurn`
terminology, public event ownership wording, interruption terminal taxonomy, and child-run
ID alignment.

## Current Implementation Snapshot

| Surface | Current implementation truth | Evidence |
|---|---|---|
| First adapter / provider default | Claude Agent SDK / Anthropic is the first concrete adapter. With no explicit `CHIRALITY_HARNESS_PROVIDER`, `resolveHarnessProviderMode` selects `agentSdk` when an Anthropic API key is configured by environment or UI Settings; otherwise it selects `stub`. Explicit `stub`, `anthropic`, and `agentSdk` still win. | D-APP-18 ruling; `frontend/src/lib/harness/runtime.ts`; `frontend/src/__tests__/lib/harness-runtime.test.ts` |
| Package pins | `@anthropic-ai/claude-agent-sdk@0.3.150` and `@anthropic-ai/sdk@0.93.0` remain the first-adapter package pins. | `frontend/package.json`; `frontend/package-lock.json` |
| Product-owned adapter boundary | `AgentEnginePort.startTurn(input)` is the adapter port method; `TurnEngine.runTurn(request)` is the route-independent lifecycle method. The older `runTurn` wording for the adapter boundary is a naming residual, not a code gap. | `frontend/src/lib/harness/agent-engine-port.ts`; `frontend/src/lib/harness/turn-engine.ts` |
| Public browser event names | `PUBLIC_UI_EVENT_NAMES` includes `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and `harness:event`. `harness:event` carries redacted provider-neutral `HarnessEvent` records and does not rename product events to SDK/provider names. | `frontend/src/lib/harness/agent-engine-port.ts`; `frontend/src/lib/harness/types.ts`; `frontend/src/lib/harness/harness-ui-bridge.ts` |
| Persisted runtime evidence | Browser `UIEvent` and persisted `HarnessEvent` remain separate contracts. `HARNESS_EVENT_TYPES` is the versioned persisted runtime vocabulary. | `frontend/src/lib/harness/event-schema.ts`; `frontend/src/lib/harness/session-events.ts`; `frontend/docs/harness/runtime_engine_contract.md` |
| Section 9 validation IDs | Current deterministic IDs use `section9.adapter_*` naming, including `section9.adapter_turn_engine_event_log` and `section9.adapter_message_mapper`. Legacy `section9.sdk_*` names are not the active IDs. | `frontend/scripts/validate-harness-section9.mjs`; `frontend/docs/harness/TRACEABILITY.md` |
| Authority source state | REF-006 is no longer a local hash-mismatch blocker for this evidence refresh. The D-APP-38 authority corpus is `v1` and current `status` validation reports no drift when no authority docs are edited. | `execution/_Reconciliation/References/AUTHORITY_CORPUS.json`; `execution/_Reconciliation/References/reconcile_authority_corpus.py status` |

## PKG-03 Crosswalk

| Deliverable | Reconciled posture | Residual |
|---|---|---|
| DEL-03-01 AgentEnginePort and conformance | The May CODEV-001 evidence remains historical. It is superseded for current default-provider, Section 9, and REF-006 posture by this ADQ-04 record and by the refreshed runtime contract. `harness:event` is part of the current public event list. | Adapter method naming (`startTurn` vs older `runTurn`) is deferred to ADQ-05. |
| DEL-03-02 TurnEngine and locking | `TurnEngine.runTurn` owns route-independent lifecycle, same-session locking, preflight, option resolution, attachment shaping, persona validation, subagent governance, adapter streaming, and mid-stream error mapping. It currently depends on `IAgentSdkManager`; a broader port-name refactor is not part of ADQ-04. | Accepted-event persistence ownership and durable disconnect/cancel evidence remain downstream runtime/session residuals. |
| DEL-03-03 API and SSE adapter | The route remains a transport adapter over `TurnEngine`; the public SSE stream uses stable `UIEvent` names, including the current redacted `harness:event` passthrough. | Route/SSE fixture capture and disconnect persistence strengthening remain future evidence work. |
| DEL-03-04 interrupt/cancel/terminal outcomes | Current source exposes adapter interruption and terminal UI evidence; Section 9 exercises runtime event-log and engine-conformance paths. | Interruption terminal taxonomy and client-disconnect durable cancellation remain ADQ-05 / downstream residuals. |

## PKG-04 Crosswalk

| Deliverable | Reconciled posture | Residual |
|---|---|---|
| DEL-04-01 SDK probe and adoption | D-APP-17 recorded a bounded packaged live read-tool proof, and D-APP-18 approved the bounded key-aware default-provider implementation. The original CODEV-001 probe record is superseded for default/adoption posture but remains historical package-pin evidence. | Mounted-DMG live parity, broad packaged workflow proof, and release/distribution claims remain out of scope. Exact Claude Code subprocess version capture remains separate from the package pins. |
| DEL-04-02 options/settings isolation | `sdk-options-builder` keeps `settingSources: []` by default, accepts only the explicit `project` override, and routes unknown tool validation through the current runtime/tool descriptor path. | Ownership wording for structured unknown-tool errors can be tightened during ADQ-05 or a later runtime cleanup; no source behavior changes here. |
| DEL-04-03 provider-neutral mapping | The current active Section 9 ID is `section9.adapter_message_mapper`, and mapper tests cover SDK-to-UI and SDK-to-`HarnessEvent` translation without adopting provider event names as product names. | Repeated-input golden assertions and terminal outcome ownership can be expanded in a later test tranche if required. |
| DEL-04-04 persona composer | Persona/system prompt composition is resolved before adapter invocation; boot-fingerprint and alias evidence stays tied to the current composer and route/runtime tests. | Instruction-root packaging proof is outside this evidence refresh. |
| DEL-04-05 key/base URL/network bridge | D-APP-18 keeps provider scope bounded to Anthropic / Claude Agent SDK. Existing tests cover key-aware default selection, API-key preflight, redaction, and network-error redaction surfaces. ADQ-16 adds current `npm run proof:secret-scan` evidence and a scripted `agentSdk` network proof artifact. | Provider/network expansion remains fenced; future release-significant reviews must rerun current secret/network evidence. |

## Validation Routing

ADQ-04 uses docs/governance validation plus the runtime validation index referenced by the
crosswalk:

- `git diff --check` over affected docs, frontend docs, execution evidence, and plans.
- `node -e JSON.parse(...)` for `docs/MANIFEST.json` after index updates.
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`.
- `npm run harness:validate:section9` from `frontend/` for the current Section 9 runtime IDs.

The generated Section 9 summary is intentionally under `frontend/artifacts/harness/section9/latest/`
and is regenerated per validation run rather than committed.
