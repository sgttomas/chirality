# Runtime Capability Matrix

**Tranche:** STAB-00 Baseline Reconciliation & ID Canonicalization
**Status:** STAB-00 artifact
**Generated:** 2026-06-16T19:30:18Z
**Working root:** `projects/chirality-app-dev/`

This artifact publishes the Runtime Stabilization plan's current-state matrix as a
regenerable evidence surface. It is derivative planning evidence only. It does not
replace product requirements, decomposition truth, source, tests, decision records,
lifecycle approvals, release readiness, professional approval, certification, sealing,
authentication, or code-compliance acceptance.

Evidence basis:

- Active queue: `plans/PLAN_2026-06-16_runtime_stabilization.md`
- Runtime contract baseline: `frontend/docs/harness/runtime_engine_contract.md`
- Provider selection truth: `frontend/src/lib/harness/runtime.ts`
- Persona gap truth: `frontend/src/lib/harness/persona-manager.ts`
- Accepted dependency closure discovery: `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/`
- Static status scan: 53 deliverable `_STATUS.md` files, all with `**Current State:** SEMANTIC_READY`

Paths below are relative to `projects/chirality-app-dev/`.

## Matrix

| # | Capability | Primary source evidence | Test or validation evidence | Deliverable | STAB-00 status |
|---:|---|---|---|---|---|
| 1 | AgentEnginePort + engine conformance evaluator | `frontend/src/lib/harness/agent-engine-port.ts`; `frontend/src/lib/harness/engine-conformance.ts` | `frontend/src/__tests__/lib/engine-conformance.test.ts`; `frontend/src/__tests__/lib/agent-engine-port.test.ts` | DEL-03-01 | LANDED |
| 2 | Thin TurnEngine + same-session active-turn locking | `frontend/src/lib/harness/turn-engine.ts` | `frontend/src/__tests__/lib/turn-engine.test.ts` | DEL-03-02 | LANDED |
| 3 | Harness API + SSE compatibility adapter | `frontend/src/app/api/harness/turn/route.ts`; `frontend/src/app/api/harness/interrupt/route.ts`; `frontend/src/app/api/harness/session/` | `frontend/src/__tests__/api/harness/routes.test.ts` | DEL-03-03 | LANDED |
| 4 | Interrupt / cancel / terminal outcomes | `frontend/src/lib/harness/claude-agent-sdk-manager.ts`; `frontend/src/lib/harness/turn-engine.ts` | `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts`; `frontend/src/__tests__/lib/engine-conformance.test.ts`; `frontend/src/__tests__/api/harness/routes.test.ts` | DEL-03-04 | LANDED |
| 5 | HarnessEvent schema + append-only JSONL | `frontend/src/lib/harness/event-schema.ts`; `frontend/src/lib/harness/session-events.ts` | `frontend/src/__tests__/lib/session-events.test.ts` | DEL-05-02 | LANDED |
| 6 | Redacted RunLogger / secret hygiene | `frontend/src/lib/harness/run-logger.ts`; `frontend/src/lib/harness/sdk-message-mapper.ts` | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` | DEL-05-03 | LANDED |
| 7 | SdkMessageMapper provider-neutral translation | `frontend/src/lib/harness/sdk-message-mapper.ts` | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` | DEL-04-03 | LANDED |
| 8 | SdkOptionsBuilder + `settingSources: []` isolation | `frontend/src/lib/harness/sdk-options-builder.ts` | `frontend/src/__tests__/lib/sdk-options-builder.test.ts`; `frontend/src/__tests__/lib/harness-options.test.ts` | DEL-04-02 | LANDED |
| 9 | Permission overlay + explicit hard-deny precedence | `frontend/src/lib/harness/permission-overlay.ts` | `frontend/src/__tests__/lib/permission-overlay.test.ts` | DEL-06-01 | LANDED |
| 10 | SDK read tool surface + unknown-tool rejection | `frontend/src/lib/harness/tool-descriptor.ts`; `frontend/src/lib/harness/turn-engine.ts` | `frontend/src/__tests__/lib/tool-descriptor.test.ts`; `frontend/src/__tests__/lib/turn-engine.test.ts` | DEL-06-02 | LANDED |
| 11 | Chirality MCP read tools | `frontend/src/lib/harness/mcp/read-tools.ts`; `frontend/src/lib/harness/mcp/tool-names.ts` | `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` | DEL-06-03 | LANDED |
| 12 | Write/Edit + path hooks | `frontend/src/lib/harness/chirality-hooks.ts`; `frontend/src/lib/harness/tool-path-policy.ts`; `frontend/src/lib/harness/instruction-root.ts` | `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `frontend/src/__tests__/lib/harness-instruction-root.test.ts` | DEL-06-04; DEL-07-01 | LANDED |
| 13 | Bash governance + timeout / no-network policy | `frontend/src/lib/harness/tool-shell-policy.ts`; `frontend/src/lib/harness/chirality-hooks.ts` | `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `frontend/src/__tests__/lib/permission-overlay.test.ts` | DEL-06-05 | LANDED |
| 14 | Hook lifecycle + compaction mirror | `frontend/src/lib/harness/chirality-hooks.ts`; `frontend/src/lib/harness/sdk-message-mapper.ts` | `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`; `frontend/src/__tests__/lib/session-events.test.ts` | DEL-06-06 | LANDED |
| 15 | Tool result budgets + overflow artifact spill | `frontend/src/lib/harness/tool-evidence.ts`; `frontend/src/lib/harness/tool-result-artifacts.ts`; `frontend/src/lib/harness/chirality-hooks.ts` | Indirect: `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` | DEL-05-05 | PARTIAL - Bash/hook-path spill only; non-Bash mapper path and direct tests remain STAB-03 scope. |
| 16 | Runtime replay | `frontend/src/lib/harness/session-events.ts` | `frontend/src/__tests__/lib/session-events.test.ts` | DEL-05-04 | PARTIAL - append/replay and malformed-line count exist; full event-class coverage and surfaced replay summary remain STAB-03 scope. |
| 17 | Type 2 subagent governance bridge | `frontend/src/lib/harness/subagent-bridge.ts`; `frontend/src/lib/harness/subagent-governance.ts`; `frontend/src/lib/harness/agent-runtime-contract.ts` | `frontend/src/__tests__/lib/subagent-bridge.test.ts`; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts`; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` | DEL-08-04 | LANDED |
| 18 | Subagent child-run records | `frontend/src/lib/harness/agent-runtime-contract.ts` | Contract-only: `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` | DEL-08-05 | PARTIAL - `createAdapterObservedChildRunRecord` exists and is contract-tested, but the factory has no adapter caller yet. |
| 19 | Status transition engine | `frontend/src/lib/lifecycle/transition.ts`; `frontend/src/lib/lifecycle/status-parser.ts` | `frontend/src/__tests__/lib/lifecycle-status.test.ts` | DEL-07-04 | LANDED - engine and route exist; mutating MCP exposure remains row 28. |
| 20 | Dependencies.csv v3.1 reader/writer/linter engine | `frontend/src/lib/dependencies/register-writer.ts`; `frontend/src/lib/dependencies/schema.ts`; `frontend/src/lib/workspace/deliverable-contracts.ts` | `frontend/src/__tests__/lib/dependencies-register-contract.test.ts`; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` | DEL-07-05 | LANDED - engine exists; mutating MCP exposure remains row 28. |
| 21 | Provider selection | `frontend/src/lib/harness/runtime.ts`; `frontend/src/lib/harness/agent-sdk-manager.ts`; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` | `frontend/src/__tests__/lib/harness-runtime.test.ts` | DEL-04-01 | LANDED - default remains `stub`; `agentSdk` is opt-in. |
| 22 | API key supply to SDK for the active turn | `frontend/src/lib/harness/turn-engine.ts`; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` | No active-turn env-injection test found | DEL-04-05 | GAP - key presence is checked before delegation, but `ANTHROPIC_API_KEY` is not set/restored around SDK `query()` yet. |
| 23 | PersonaComposer from instruction root | `frontend/src/lib/harness/persona-manager.ts`; `frontend/src/lib/harness/runtime.ts` | No persona-composer tests found | DEL-04-04 | GAP - `StubPersonaManager` validates persona existence and returns a short synthetic prompt. |
| 24 | Section 8 running-app validation + stable premerge artifact | `frontend/scripts/validate-harness-section8.mjs`; `frontend/scripts/validate-harness-premerge.mjs` | `frontend/src/__tests__/api/harness/routes.test.ts`; `frontend/docs/harness/TRACEABILITY.md`; Section 8 script check IDs in `frontend/scripts/validate-harness-section8.mjs` | DEL-09-01 | LANDED |
| 25 | Section 9 runtime validation IDs aggregator | `docs/SPEC.md` Section 19.3; `docs/PRD.md` Section 12.4 | No `frontend/scripts/validate-harness-section9.mjs` found | DEL-09-02 | GAP - STAB-01 owns the aggregator. |
| 26 | macOS DMG packaging + SDK subprocess probe | `frontend/package.json`; `frontend/scripts/verify-instruction-root-integrity.mjs` | `frontend/src/__tests__/scripts/dmg-packaging-policy.test.ts`; `frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts` | DEL-09-04 | PARTIAL - packaging path exists; SDK subprocess package proof and `asarUnpack` remain STAB-02(d) scope. |
| 27 | Network policy proof | `frontend/scripts/run-network-policy-proof.mjs`; Electron network policy surfaces under `frontend/` | `frontend/src/__tests__/scripts/build-network-policy.test.ts` | DEL-09-06 | LANDED for default/`anthropic`; `agentSdk` outbound proof remains STAB-02(c). |
| 28 | Mutating Chirality MCP tools (`status_transition`, `deps_write`) | Descriptor reservation in `frontend/src/lib/harness/tool-descriptor.ts` | No mutating MCP tests found | DEL-07-04; DEL-07-05 | METADATA-ONLY - exposure requires STAB-04 and D-APP-13. |

## Deliverable Status Reconciliation Note

The live decomposition deliverable status surface is not a runtime-completion surface.
A static scan found 53 deliverable `_STATUS.md` files and every one reports
`**Current State:** SEMANTIC_READY`.

STAB-00 records this as a reconciliation note only:

- `SEMANTIC_READY` is a decomposition-process state from the semantic/lensing workflow.
- The v3.2 decomposition remains topology authority.
- The matrix above is the runtime-implementation view for the stabilization program.
- No `_STATUS.md` files were bulk-edited; forward lifecycle transitions remain
  actor-authorized and approval-SHA-gated where applicable.

## Human Ruling Posture

Current human-gated decisions from `execution/_Coordination/_DECISIONS/_REGISTER.md`:

| ID | State | Blocks |
|---|---|---|
| D-APP-12 | AWAITING_RULING | Default-provider cutover to `agentSdk`; any governance text declaring SDK as active default. |
| D-APP-13 | NOT_PREPARED | Mutating Chirality MCP exposure (`status_transition`, `deps_write`). |

STAB-05 persona-composer implementation and STAB-00/STAB-01 evidence work require no new
ruling beyond accepted program ruling D-APP-11, provided they stay within the active plan.
