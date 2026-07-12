# Assessment INSP-03: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-04-03 |
| Package | PKG-04 SDK Adapter, Prompt, Provider, and Settings |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `ce0ab70933c6cc32f9eea62a563e512fc738a575` |
| Spec source | `Specification.md` lines 5-76 |

## Scope

DEL-04-03 owns translation from SDK/provider stream inputs into stable browser `UIEvent`s and provider-neutral persisted `HarnessEvent`s. It must keep SDK vocabulary behind adapter metadata while preserving route/SSE compatibility.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-04-03-REQ001 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 633-907; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-153. Focused validation passed. | SDK input message names are translated before reaching browser event names. |
| DEL-04-03-REQ002 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 341-351 and 633-907; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-153. Focused validation passed. | Persisted events use Chirality-owned `HarnessEvent` categories. |
| DEL-04-03-REQ003 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 330-351 and 633-907; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 155-720. Focused validation passed. | Session IDs, tool evidence, permission data, and mirror errors are redacted or retained as adapter metadata. |
| DEL-04-03-REQ004 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 633-837; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-153. Focused validation passed. | Browser-facing output preserves stable `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, and `process:exit` compatibility. |
| DEL-04-03-REQ005 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 3-59; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 341-351; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-153. Focused validation passed. | Runtime outputs are versioned `HarnessEvent` records. |
| DEL-04-03-REQ006 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 633-837; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-153 and 646-720. Focused validation passed. | Initial session, model, turn, failure, completion, and child-run categories are mapped where source inputs are present. |
| DEL-04-03-REQ007 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 839-907 and 909 onward; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 112-153 and 558-644. Focused validation passed. | Tool, permission, hook, compaction, subagent, and mirror-error categories have explicit mappings/tests rather than being hidden. |
| DEL-04-03-REQ008 | PARTIAL | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-720. Focused validation passed. | Ordered fixture tests exist, but no explicit same-input repeated-run golden assertion was found during this wave. |
| DEL-04-03-REQ009 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 909 onward; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 155-644. Focused validation passed. | SDK model/tool loop activity is mirrored into Chirality tool, permission, hook, status, and subagent events where present. |
| DEL-04-03-REQ010 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 330-351 and 881-907; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 409-556. Focused validation passed. | SDK transcript/storage artifacts are redacted metadata and never replace canonical `HarnessEvent` output. |
| DEL-04-03-REQ011 | PARTIAL | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-153; `frontend/src/__tests__/api/harness/routes.test.ts`; `frontend/scripts/validate-harness-section9.mjs` lines 35-36. Focused validation passed. | Route/SSE compatibility is tested, but the Section 9 validator names `section9.adapter_message_mapper` instead of the spec's `section9.sdk_message_mapper`. |
| DEL-04-03-REQ012 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 19 and 330-351; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 409-556; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 225-260. Focused validation passed. | Redaction fixtures cover overflow artifacts, tool evidence, SDK errors, and configured key variants. |
| DEL-04-03-REQ013 | PARTIAL | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 750-879; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 66-153; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 160-253. Focused validation passed. | Mapper-owned terminal translation exists, but lock cleanup, cancellation-source classification, and durable terminal ownership remain shared with PKG-03/PKG-05. |
| DEL-04-03-REQ014 | PARTIAL | `Specification.md` lines 41 and 62; `Evidence_CODEV-001_SDK_Probe_Record.md` lines 32-38. | The current mapper covers many categories, but exact payload-field fixture provenance should be refreshed from the first-adapter probe/adoption record. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Section 9 validation ID does not match the deliverable specification. | Medium | `Specification.md` lines 52 and 76; `frontend/scripts/validate-harness-section9.mjs` lines 35-36. | Reconcile the validator ID or add an alias so both `section9.sdk_message_mapper` and current coverage are traceable. |
| Determinism is covered by fixture behavior but not an explicit repeated-input golden assertion. | Low | `Specification.md` lines 35 and 60; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-720. | Add one same-sequence repeated-run assertion or record why current golden fixtures satisfy the requirement. |
| Terminal outcome ownership is intentionally split. | Medium | `Specification.md` lines 40 and 65; PKG-03 assessments. | Preserve the split: mapper translates; `TurnEngine`/event store own cleanup and durability. |
| Exact SDK payload provenance remains tied to DEL-04-01. | Medium | `Specification.md` lines 21 and 41. | Refresh the first-adapter probe record before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for REF-006, first-adapter probe fixture provenance, Section 9 validation naming, and downstream event-store/terminal durability evidence.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Reconcile Section 9 mapper validation ID naming. | reconcile | S | FIT | Keep current mapper tests green. |
| Add an explicit repeated-input determinism fixture for mapper output ordering. | test | S | FIT | No provider expansion; use local fixtures only. |
| Cross-link terminal outcome responsibilities to PKG-03 and PKG-05 rather than broadening mapper ownership. | doc | S | FIT | Complete PKG-05 wave. |

## Issuance-Gate-Process Observations

DEL-04-03 is close to issuance-ready on implementation evidence, but issuance should not hide the Section 9 naming drift or the remaining first-adapter-probe provenance gap.

## D-APP-56 R5 P43 annotation (2026-07-12)

The REQ011 `PARTIAL` conclusion and Gap 1 naming mismatch above are preserved
historical evidence at the Reviewed SHA. ADQ-04 subsequently reconciled the
kit and validator on `section9.adapter_message_mapper`; route/SSE
compatibility remains test-covered. The old naming mismatch is no longer
current. This annotation makes no assessment-verdict or lifecycle change.
