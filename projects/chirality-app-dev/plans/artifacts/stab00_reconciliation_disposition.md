# STAB-00 Reconciliation Disposition

**Tranche:** STAB-00 Baseline Reconciliation & ID Canonicalization
**Status:** STAB-00 artifact
**Generated:** 2026-06-16T19:30:18Z
**Working root:** `projects/chirality-app-dev/`

This artifact records the stale-governance disposition list, Section 9 ID
canonicalization, and ruling posture required by STAB-00. It is derivative planning
evidence only.

## Stale-Governance Disposition List

| ID | Doc + anchor | Stale or at-risk claim | Contradicting or qualifying source | Disposition |
|---|---|---|---|---|
| STAB00-DISP-001 | `docs/PRD.md` FR-027 | `CHIRALITY_HARNESS_PROVIDER=anthropic` resolves to the SDK-backed `TurnEngine` after R1 cutover. | `frontend/src/lib/harness/runtime.ts` maps `anthropic` to `AnthropicAgentSdkManager` and maps only `agentSdk` aliases to `ClaudeAgentSdkManager`; `frontend/docs/harness/runtime_engine_contract.md` says `agentSdk` is opt-in and default remains unchanged. | UPDATE IN PLACE in STAB-06: correct provider-mode wording to `agentSdk` for the SDK probe; do not declare a default-provider cutover without D-APP-12. |
| STAB00-DISP-002 | `docs/PRD.md` FR-070 | `TurnEngine.runTurn()` delegates SDK execution to `query()` after R1. | `frontend/src/lib/harness/turn-engine.ts` delegates through `IAgentSdkManager`; `frontend/src/lib/harness/runtime.ts` chooses direct Anthropic, SDK probe, or stub by provider mode. | UPDATE IN PLACE in STAB-06: make acceptance provider-adapter neutral and describe `query()` as the `agentSdk` path detail. |
| STAB00-DISP-003 | `docs/PLAN.md` R1 implementation target | Wire `CHIRALITY_HARNESS_PROVIDER=anthropic` to SDK-backed path. | Same provider-mode source as STAB00-DISP-001. | UPDATE IN PLACE in STAB-06: correct to opt-in `agentSdk` and preserve current default until D-APP-12. |
| STAB00-DISP-004 | `docs/SPEC.md` Section 19.4 | First-adapter SDK-backed turn can start in packaged app after R1. | `plans/PLAN_2026-06-16_runtime_stabilization.md` row 26 records packaged SDK subprocess proof as `BLOCKED_TBD`; `frontend/docs/harness/runtime_engine_contract.md` keeps `agentSdk` in first-adapter probe posture. | UPDATE IN PLACE in STAB-06: mark packaged SDK turn proof as STAB-02(d) evidence, not an R1-complete fact. |
| STAB00-DISP-005 | `docs/PRD.md` Section 2 current implementation assessment | Harness lacks real tool surface, permission model is partly simulated, there is no append-only per-turn Chirality transcript, and the route owns too much runtime lifecycle. | `frontend/docs/harness/runtime_engine_contract.md`; `frontend/src/lib/harness/turn-engine.ts`; `frontend/src/lib/harness/event-schema.ts`; `frontend/src/lib/harness/session-events.ts`; `frontend/src/lib/harness/tool-descriptor.ts`; `frontend/src/lib/harness/permission-overlay.ts`. | SUPERSEDE WITH DATED NOTE in STAB-06: runtime primitives have landed, with residual gaps tracked in `plans/artifacts/runtime_capability_matrix.md`. |
| STAB00-DISP-006 | `docs/PRD.md` KG-004 | Append-only transcript/event log is a gap. | `frontend/src/lib/harness/event-schema.ts`; `frontend/src/lib/harness/session-events.ts`; `frontend/src/__tests__/lib/session-events.test.ts`. | SUPERSEDE WITH DATED NOTE in STAB-06: append-only event log exists; replay hardening remains STAB-03. |
| STAB00-DISP-007 | `docs/PRD.md` KG-005 | Tool runtime is a gap. | `frontend/src/lib/harness/tool-descriptor.ts`; `frontend/src/lib/harness/mcp/read-tools.ts`; `frontend/src/lib/harness/chirality-hooks.ts`; `frontend/src/__tests__/lib/tool-descriptor.test.ts`; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts`; `frontend/src/__tests__/lib/chirality-hooks.test.ts`. | SUPERSEDE WITH DATED NOTE in STAB-06: read, Write/Edit, and Bash surfaces have landed behind policy; mutating MCP and result-artifact hardening remain explicit future scope. |
| STAB00-DISP-008 | `docs/PRD.md` KG-006 | Generic adapter/Chirality permission overlay is a gap. | `frontend/src/lib/harness/permission-overlay.ts`; `frontend/src/__tests__/lib/permission-overlay.test.ts`; `frontend/src/lib/harness/sdk-options-builder.ts`. | SUPERSEDE WITH DATED NOTE in STAB-06: overlay and hard-deny precedence exist; STAB-04 governs mutating MCP exposure. |
| STAB00-DISP-009 | `docs/PRD.md` KG-010 | Subagent execution has no SDK `agents` integration or child runtime records. | `frontend/src/lib/harness/subagent-bridge.ts`; `frontend/src/lib/harness/subagent-governance.ts`; `frontend/docs/harness/runtime_engine_contract.md` Agent/Subagent Runtime Contract; `frontend/src/lib/harness/agent-runtime-contract.ts`. | SUPERSEDE WITH DATED NOTE in STAB-06, qualified: governed executable subagent path has landed, while adapter-observed child-run record wiring remains STAB-03. |
| STAB00-DISP-010 | `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` K-ENGINE-3; `docs/SPEC.md` Sections 10.3 and 12.1 | Claude Agent SDK / Anthropic is described as the current shipped path. | `frontend/src/lib/harness/runtime.ts` and `frontend/docs/harness/runtime_engine_contract.md` show `agentSdk` is opt-in and default provider is unchanged pending D-APP-12. | SUPERSEDE WITH DATED CLARIFICATION in STAB-06: retain first-adapter strategy, but avoid wording that implies default-provider cutover or broader provider/network approval. |
| STAB00-DISP-011 | `docs/PLAN.md` and `docs/PRD.md` R2-R5 roadmap sections | Forward roadmap text presents phases that have since partially or fully landed. | `frontend/docs/harness/runtime_engine_contract.md`; `plans/PLAN_COMPLETION_LOG.md`; `plans/artifacts/runtime_capability_matrix.md`. | SUPERSEDE WITH DATED NOTE in STAB-06: keep roadmap as history, route active work through Runtime Stabilization. |
| STAB00-DISP-012 | `docs/PRD.md` Section 2 persona clause; `docs/PRD.md` KG-002 | Persona composer remains unimplemented. | `frontend/src/lib/harness/persona-manager.ts` still instantiates `StubPersonaManager`; `frontend/src/lib/harness/runtime.ts` wires that stub. | KEEP AS CURRENT: STAB-05 owns implementation. Do not mark resolved in STAB-06 unless STAB-05 lands. |
| STAB00-DISP-013 | `docs/SPEC.md` Section 19.3 | Section 9 IDs are specified, but no Section 9 running artifact exists. | No `frontend/scripts/validate-harness-section9.mjs` exists; `plans/PLAN_2026-06-16_runtime_stabilization.md` assigns this to STAB-01. | KEEP / DEFER: STAB-01 builds the aggregator. No authority-doc edit in STAB-00. |
| STAB00-DISP-014 | `execution/PKG-01.../DEL-01-02_*` and `execution/PKG-09.../DEL-09-02_*` live deliverable kits | Older `section9.sdk_turn_engine_event_log` and `section9.sdk_message_mapper` aliases remain in live deliverable-local artifacts. | `docs/SPEC.md` Section 19.3 and `docs/PRD.md` Section 12.4 use canonical `section9.adapter_turn_engine_event_log` and `section9.adapter_message_mapper`. | CANONICALIZE FOR NEW WORK: STAB-01 must use canonical `adapter_*` IDs. STAB-00 does not bulk-edit deliverable kits; STAB-06 may add dated supersession notes if it touches the affected docs. |

## Section 9 ID Canonicalization

Authority: `docs/SPEC.md` Section 19.3 and `docs/PRD.md` Section 12.4.

Canonical IDs for STAB-01:

| Canonical ID | Superseded alias posture |
|---|---|
| `section9.runtime_engine_contract` | No alias observed. |
| `section9.adapter_turn_engine_event_log` | Supersedes older `section9.sdk_turn_engine_event_log` in live deliverable-local kits. |
| `section9.adapter_message_mapper` | Supersedes older `section9.sdk_message_mapper` in live deliverable-local kits. |
| `section9.session_event_replay` | No alias observed. |
| `section9.reliance_boundary_register` | Deferred from STAB-01 first cut unless deterministic evidence lands. |
| `section9.settingsources_isolation` | No alias observed. |
| `section9.sdk_session_link_resume` | Canonical as written; this remains SDK-session-linkage specific adapter metadata. |
| `section9.permission_overlay_hard_deny_precedence` | Canonical spelling; supersedes any older `permission_overlay_deny_first` wording if encountered. |
| `section9.tool_runtime_read_file` | No alias observed. |
| `section9.chirality_mcp_status_dependencies` | No alias observed. |
| `section9.path_containment_hook` | No alias observed. |
| `section9.instruction_root_protection_hook` | No alias observed. |
| `section9.tool_result_budget` | No alias observed. |
| `section9.context_compaction_boundary` | Included in STAB-01 first cut because runtime evidence is landed and tested. |
| `section9.subagent_governance_hook` | No alias observed. |
| `section9.domain_profile_validation` | Deferred until governed domain-profile amendment enters scope. |

STAB-00 corrects one guidance assumption from the active plan: the older `sdk_*` aliases
are not confined to `.archive`; they also appear in live deliverable-local kits. This
artifact records that discrepancy and binds future STAB-01 work to the canonical SPEC/PRD
IDs without bulk-editing deliverable-local lifecycle artifacts.

## Required Human Rulings

| ID | State in register | Required before |
|---|---|---|
| D-APP-12 | AWAITING_RULING | Any default-provider cutover to `agentSdk`; any governance text declaring the SDK path the active default. |
| D-APP-13 | NOT_PREPARED | Any mutating Chirality MCP exposure from metadata-only to `workspaceWrite`-gated. |

STAB-05 persona-composer work is implementation scope accepted by D-APP-11 and the active
Runtime Stabilization plan. It does not need a separate ruling unless it changes provider,
network, release, professional-boundary, or lifecycle policy.
