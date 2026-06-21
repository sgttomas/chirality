# Assessment INSP-03: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-04-01 |
| Package | PKG-04 SDK Adapter, Prompt, Provider, and Settings |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `ce0ab70933c6cc32f9eea62a563e512fc738a575` |
| Spec source | `Specification.md` lines 5-102 |

## Scope

DEL-04-01 defines the evidence needed to decide whether Chirality should adopt a version-pinned Claude Agent SDK runtime path for R1. This assessment inspects the current probe record, implementation, tests, package pins, and validation hooks without making an adoption verdict.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-04-01-REQ-001 | PARTIAL | `Evidence_CODEV-001_SDK_Probe_Record.md` lines 18-21; `frontend/package.json` lines 29-31; `frontend/package-lock.json` lines 11-12 and 54. Focused validation passed. | Package and peer versions are pinned, but the Claude Code subprocess version remains `BLOCKED_TBD`. |
| DEL-04-01-REQ-002 | PARTIAL | `frontend/package.json` lines 29-31; `frontend/package-lock.json` lines 11-12; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 37-38. Focused validation passed. | The version pin exists, but the deliverable-local record still lacks the final adoption decision and upgrade regression expectation. |
| DEL-04-01-REQ-003 | PARTIAL | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 633-907; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-720; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 32-33. Focused validation passed. | Mapping implementation is broad, but exact live SDK `query()` sequence capture remains tied to the probe/adoption evidence refresh. |
| DEL-04-01-REQ-004 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 330-351 and 633-907; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-720. Focused validation passed. | SDK names and IDs are retained as adapter metadata instead of public or canonical event names. |
| DEL-04-01-REQ-005 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 22-37 and 147-149; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-115 and 194-213. Focused validation passed. | Shipped posture resolves `settingSources: []`; exact `project` is the only accepted explicit development opt-in. |
| DEL-04-01-REQ-006 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 81-157; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 255-562. Focused validation passed. | Permission mode mapping, deny lists, `canUseTool`, hooks, bypass gating, and delegated-agent permissions are covered. |
| DEL-04-01-REQ-007 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 139-146; `frontend/src/__tests__/lib/agent-sdk-mcp-behavior-probe.test.ts`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 117-192. Focused validation passed. | In-process MCP is exposed through Chirality descriptors/policy, not treated as a bypass around permission, hooks, redaction, or logging. |
| DEL-04-01-REQ-008 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 323-340; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 188-220; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 34-36. Focused validation passed. | SDK session metadata and resume handoff exist, but live `SessionStore` / `CLAUDE_CONFIG_DIR` / transcript linkage remains not fully accepted in the DEL record. |
| DEL-04-01-REQ-009 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-21; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 202-217; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 225-260. Focused validation passed. | Chirality JSONL events remain the canonical audit mirror; SDK transcript details are metadata or residual-risk evidence only. |
| DEL-04-01-REQ-010 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 87-179 and 340-379; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 696-716 and 863-956; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 262-332. Focused validation passed. | Interrupt/cancel tests exist, but terminal taxonomy and client-disconnect ownership remain open across PKG-03/PKG-04/PKG-05. |
| DEL-04-01-REQ-011 | PARTIAL | `frontend/package.json` lines 19-22 and 53-60; `frontend/src/__tests__/scripts/verify-packaged-agent-sdk-runtime.test.ts`; `frontend/src/__tests__/scripts/run-live-packaged-agent-sdk-read-tool-proof.test.ts`; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 37-38. Focused validation passed. | Packaging scripts and `asarUnpack` exist, but the DEL record still says packaging and adoption verdict are `BLOCKED_TBD`. |
| DEL-04-01-REQ-012 | PASS | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 46-70 and 202-220; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 225-260; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 572-935. Focused validation passed. | Active-turn key handoff and redaction are tested for the Claude SDK manager and Anthropic provider surfaces. |
| DEL-04-01-REQ-013 | PARTIAL | `Specification.md` lines 38 and 46-55; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 37-38; D-APP-18 key-aware default is landed. | Fallback triggers are expressed as contract/gate expectations, but the adoption verdict itself remains unresolved. |
| DEL-04-01-REQ-014 | PASS | `frontend/src/__tests__/scripts/run-live-packaged-agent-sdk-read-tool-proof.test.ts`; `frontend/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-115. Focused validation passed. | Live/package proof paths keep the tool surface controlled and Read-focused; no broad local tool exposure is accepted. |
| DEL-04-01-REQ-015 | PARTIAL | `Specification.md` lines 40 and 86-102; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 34-38. | The spec names the residual risks, but the DEL-local adoption decision/residual-risk record has not been refreshed after the later SDK/runtime work. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| The DEL-local probe record is stale relative to D-APP-18 key-aware default behavior. | Medium | `Evidence_CODEV-001_SDK_Probe_Record.md` lines 8-9; `frontend/src/lib/harness/runtime.ts` lines 50-72. | Add a superseding probe note that distinguishes explicit provider selection history from the current key-aware default. |
| The subprocess version, packaging result, and adoption verdict remain unresolved in the probe record. | Medium | `Evidence_CODEV-001_SDK_Probe_Record.md` lines 21 and 37-38. | Refresh CODEV-001 or add a new decision record before issuance. |
| Live SDK session/transcript storage behavior remains only partially closed. | Medium | `Evidence_CODEV-001_SDK_Probe_Record.md` lines 34-36; `Specification.md` lines 33 and 77. | Carry this into the PKG-05 session/audit wave and avoid treating SDK transcript paths as project truth. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Retain warning-limited source status until project-wide ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for REF-006 source-state, first-adapter probe/adoption evidence, package/runtime proof evidence, and downstream PKG-05 session/audit ownership.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add a superseding SDK probe/adoption note that records the current package pins, subprocess-version disposition, packaging status, fallback triggers, and residual risks. | evidence | M | FIT | Keep provider scope limited to the Anthropic path already ruled by D-APP-18. |
| Cross-link session/transcript residual risks to PKG-05 assessment findings. | reconcile | S | FIT | Complete PKG-05 wave. |
| Record an explicit upgrade-regression expectation for future `@anthropic-ai/claude-agent-sdk` pin changes. | doc/test | S | FIT | Current focused PKG-04 tests remain green. |

## Issuance-Gate-Process Observations

DEL-04-01 is implementation-rich but evidence-record-stale. Issuance should require a refreshed adoption packet rather than relying on the May CODEV-001 record alone.
