# Assessment INSP-03: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-04-05 |
| Package | PKG-04 SDK Adapter, Prompt, Provider, and Settings |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `ce0ab70933c6cc32f9eea62a563e512fc738a575` |
| Spec source | `Specification.md` lines 5-96 |

## Scope

DEL-04-05 covers API-key precedence, safeStorage persistence, active-turn SDK key handoff, Anthropic base URL validation, renderer/Node network policy, provider error classification, and redacted adapter metadata.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-04-05-RQ-001 | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 258-277; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 46-70; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 1114-1194. Focused validation passed. | UI key wins, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. |
| DEL-04-05-RQ-002 | PARTIAL | `frontend/electron/api-key-storage.ts` lines 26-48; `frontend/src/__tests__/electron/api-key-storage.test.ts` lines 66-114; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 572-935. Focused validation passed. | Storage and provider error paths are redacted, but broader logs/tool-artifact assertions are shared with PKG-05 and release validation. |
| DEL-04-05-RQ-003 | PASS | `frontend/electron/api-key-storage.ts` lines 26-48; `frontend/src/__tests__/electron/api-key-storage.test.ts` lines 66-73 and 108-114. Focused validation passed. | UI key material is encrypted with safeStorage under `app.getPath('userData')/credentials/api-key.enc`. |
| DEL-04-05-RQ-004 | PASS | `frontend/electron/api-key-ipc.ts` lines 13-17 and 51-69; `frontend/src/__tests__/electron/api-key-ipc.test.ts` lines 97-122. Focused validation passed. | Status exposes only `ui`, `env`, or `none`, not key values. |
| DEL-04-05-RQ-005 | PASS | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 46-70 and 202-220; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 225-260; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 816-840. Focused validation passed. | Claude Agent SDK env key is installed only around active turn execution and restored; direct Anthropic client receives in-memory config. |
| DEL-04-05-RQ-006 | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 166-255; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 295-526. Focused validation passed. | Base URL accepts only `https://api.anthropic.com` with no credentials and empty/443 port. |
| DEL-04-05-RQ-007 | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 174-247; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 295-505. Focused validation passed. | Invalid host/scheme/credentials/port fail closed with typed errors before network execution. |
| DEL-04-05-RQ-008 | PASS | `frontend/electron/main.ts` lines 105-127; `frontend/src/__tests__/scripts/build-network-policy.test.ts` lines 36-49. Focused validation passed. | Renderer egress is intercepted and fail-closed for non-loopback/non-Anthropic targets, with metadata-only diagnostics. |
| DEL-04-05-RQ-009 | PASS | `frontend/src/__tests__/scripts/build-network-policy.test.ts` lines 51-60; `frontend/scripts/run-network-policy-proof.mjs`; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 836-840. Focused validation passed. | Scripted network proof and provider base URL validation avoid silent broadening of Node/SDK egress scope. |
| DEL-04-05-RQ-010 | PASS | `docs/SPEC.md` Section 16.3; `frontend/src/lib/harness/tool-descriptor.ts`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 117-192. Focused validation passed. | Remote MCP, plugins, and non-Anthropic provider/network tools remain out of scope. |
| DEL-04-05-RQ-011 | PARTIAL | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 523-668 and 933-947; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 528-724 and 937-1112. Focused validation passed. | Auth, rate limit, API, network, invalid base URL, policy violation, and timeout categories exist; timeout has source coverage but limited explicit test visibility in this wave. |
| DEL-04-05-RQ-012 | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 594-668 and 933-956; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 572-935. Focused validation passed. | Classified provider failures become typed `SDK_FAILURE` with configured key variants redacted. |
| DEL-04-05-RQ-013 | PASS | `frontend/src/app/api/harness/turn/route.ts` lines 9-45; `frontend/src/lib/harness/runtime.ts` lines 74-89; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 670-970. Focused validation passed. | Provider integration remains behind runtime managers; HTTP route delegates rather than owning provider semantics. |
| DEL-04-05-RQ-014 | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 675-693 and 949-956; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 162-246 and 572-935. Focused validation passed. | Provider-specific data stays in adapter metadata and redacted lifecycle events. |
| DEL-04-05-RQ-015 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 22-37 and 147-149; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 194-213. Focused validation passed. | Provider behavior does not depend on ambient user/local Claude settings. |
| DEL-04-05-RQ-016 | PASS | `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 225-260; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 126-1194; `frontend/src/__tests__/electron/api-key-storage.test.ts` lines 66-114; `frontend/src/__tests__/electron/api-key-ipc.test.ts` lines 77-122; `frontend/src/__tests__/scripts/build-network-policy.test.ts` lines 36-60. Focused validation passed. | Key handoff, base URL/network, and redaction fixtures/tests exist. |
| DEL-04-05-RQ-017 | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 675-693 and 949-956; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 202-217; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 572-935. Focused validation passed. | Wrapper exposes redacted metadata to events and assertions. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Broad no-key-in-any-log/tool-artifact proof is shared with PKG-05/release validation. | Medium | `Specification.md` lines 28 and 60; DEL-05 pending assessment wave. | Carry the residual into PKG-05 and release-quality checks rather than treating provider tests as whole-product proof. |
| Timeout classification exists but needs explicit test traceability before issuance. | Low | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 933-947; `Specification.md` lines 37 and 63. | Add or cross-link a timeout fixture in the provider manager tests. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12; `Specification.md` lines 94-96. | Retain warning-limited PRD-derived provider-policy rows until source-state ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for REF-006, release-quality/redaction breadth, network-policy evidence, and downstream PKG-05 run-log/tool-artifact ownership.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add explicit timeout classification test traceability for the Anthropic provider manager. | test | S | FIT | Keep current provider tests green. |
| Cross-link no-secret-in-logs/tool-artifacts proof to PKG-05 event/run-log assessments and release gates. | reconcile | S | FIT | Complete PKG-05 wave. |
| Keep remote MCP/plugins/non-Anthropic provider expansion out of scope unless a future ruling opens a bounded tranche. | governance | S | FIT | Fresh human ruling. |

## Issuance-Gate-Process Observations

DEL-04-05 has strong provider-boundary tests. Issuance should focus on whole-product redaction/logging breadth, timeout traceability, and REF-006 rather than expanding provider scope.

## D-APP-56 R5 P44 pointer annotation (2026-07-12)

The RQ-010 evidence citation above preserves the `frontend/src/lib/harness/tool-descriptor.ts` path inspected at assessment time. D-APP-46/D-APP-48 subsequently relocated that contract to `frontend/packages/harness-contract/src/tool-descriptor.ts`. The PASS conclusion is unchanged; this is an evidence-pointer annotation only.
