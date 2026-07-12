# Assessment INSP-03: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-04-02 |
| Package | PKG-04 SDK Adapter, Prompt, Provider, and Settings |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `ce0ab70933c6cc32f9eea62a563e512fc738a575` |
| Spec source | `Specification.md` lines 5-81 |

## Scope

DEL-04-02 owns deterministic construction of Claude Agent SDK options from Chirality runtime state and policy, including settings isolation, registered tool mapping, safe metadata, max-turn propagation, and adjacent-contract inputs.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-04-02-REQ-001 | PASS | `frontend/src/lib/harness/options.ts` lines 13-107; `frontend/src/__tests__/lib/harness-options.test.ts` lines 68-221 and 266-288. Focused validation passed. | Model, tools, max turns, mode, and persona fallback chains are deterministic. |
| DEL-04-02-REQ-002 | PASS | `frontend/src/lib/harness/options.ts` lines 71-85; `frontend/src/__tests__/lib/harness-options.test.ts` lines 241-264. Focused validation passed. | Unknown option keys warn and do not mutate resolved behavior. |
| DEL-04-02-REQ-003 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 22-37 and 147-149; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87. Focused validation passed. | Shipped default is `settingSources: []`. |
| DEL-04-02-REQ-004 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 22-37; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 194-213. Focused validation passed. | Only exact `project` is accepted; user/local/mixed settings fall back to `[]`. |
| DEL-04-02-REQ-005 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 186-229; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 233-253; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 117-192. Focused validation passed. | Unknown requested agentSdk tools are rejected before adapter streaming; remaining exact structured-error ownership is shared with runtime/tool-descriptor surfaces. |
| DEL-04-02-REQ-006 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-157; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 89-192 and 266-288. Focused validation passed. | Tool ordering, naming, MCP IDs, allow/deny lists, and options are deterministic for a fixed input. |
| DEL-04-02-REQ-007 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 39-54 and 100-138; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 255-562. Focused validation passed. | `allowedTools` is accompanied by disallowed tools, permission mode mapping, hooks, and `canUseTool`; bypass requires explicit env opt-in. |
| DEL-04-02-REQ-008 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` line 111; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87; `frontend/src/__tests__/lib/harness-options.test.ts` lines 68-159. Focused validation passed. | `maxTurns` is propagated into SDK options; terminal max-turn event ownership remains outside this builder. |
| DEL-04-02-REQ-009 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 106-157; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 202-220; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-720. Focused validation passed. | SDK-specific details stay behind adapter/options metadata and mapper translation. |
| DEL-04-02-REQ-010 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 202-217; `frontend/src/lib/harness/persona-manager.ts` lines 149-189; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 74-155. Focused validation passed. | Safe visible posture is present for tool/mode/policy and accepted-turn metadata; transcript/store linkage remains downstream PKG-05 evidence. |
| DEL-04-02-REQ-011 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 81-157; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-562; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 225-260. Focused validation passed. | Builder output does not include API key material; the manager injects and restores active-turn key state separately. |
| DEL-04-02-REQ-012 | PARTIAL | `frontend/src/lib/harness/sdk-options-builder.ts` line 1; `frontend/package.json` lines 29-31; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 18-21. Focused validation passed. | Current TypeScript API imports compile against the pinned SDK, but final probe/adoption evidence still carries subprocess/version TBDs. |
| DEL-04-02-REQ-013 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 81-157; `frontend/src/lib/harness/types.ts` lines 23-252; `frontend/src/lib/harness/persona-manager.ts` lines 210-285. Focused validation passed. | Session, persona output, MCP, hooks, resume, settings, and subagent policy inputs are imported from adjacent runtime contracts. |
| DEL-04-02-REQ-014 | PARTIAL | `frontend/src/lib/harness/sdk-options-builder.ts` lines 81-157; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 117-562; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 233-253. Focused validation passed. | Policy inputs fail closed for unknown tools and restricted capabilities, but broader unresolved-adjacent-input closure remains shared with PKG-06/PKG-08. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Exact structured-error ownership for unknown tools is split across `TurnEngine`, tool descriptors, and options builder tests. | Medium | `Specification.md` lines 32 and 57-64; `frontend/src/lib/harness/turn-engine.ts` lines 186-229. | Reconcile the deliverable doc to name the runtime-owned validation point and the builder-owned deterministic mapping point. |
| Safe visible metadata is broad but transcript/store linkage remains outside PKG-04. | Medium | `Specification.md` line 37; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 202-217. | Carry transcript/store metadata closure into PKG-05 rather than inventing it in options builder. |
| First-adapter probe still owns exact SDK-version/adoption confirmation. | Low | `Specification.md` lines 39 and 64; DEL-04-01 evidence record lines 18-21 and 37-38. | Update DEL-04-01 first, then close any remaining DEL-04-02 SDK-shape TBDs. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for REF-006, first-adapter probe confirmation, Section 9 validation linkage, and adjacent permission/subagent/session ownership.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Document the current options-builder integration boundary: builder maps deterministic SDK options; `TurnEngine` rejects unknown tools before streaming. | doc | S | FIT | Keep focused PKG-04 tests green. |
| Add or cross-link a safe metadata fixture that distinguishes builder-owned metadata from PKG-05 transcript/store linkage. | evidence | S | FIT | Complete PKG-05 assessment wave. |
| Close SDK option-shape TBDs after the DEL-04-01 adoption record is refreshed. | reconcile | S | FIT | DEL-04-01 superseding probe note exists. |

## Issuance-Gate-Process Observations

DEL-04-02 has strong runnable source/test coverage. Issuance should focus on reconciling split ownership and remaining upstream probe/reference warnings, not on rewriting the options implementation.

## D-APP-56 R5 P40 annotation (2026-07-12)

The source-state caveat above is preserved as historical assessment evidence. REF-006 now records `docs/PRD.md` expected and actual SHA-256 as `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` (`MATCH`) under D-APP-38; it is not a current warning or blocker. No assessment verdict or lifecycle state changes here.
