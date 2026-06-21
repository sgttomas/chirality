# Assessment INSP-03: DEL-02-04 Toolkit Options and Local UI State

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-02-04 |
| Package | PKG-02 Desktop Shell Navigation and Operator State |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `50b063f3ec4d9df900b4f2c465cf2f9ac79e91a0` |
| Spec source | `Specification.md` lines 5-81 |

## Scope

DEL-02-04 covers shell pane layout state, Toolkit option controls and presets, chat draft and attachment local persistence, and the non-authoritative boundary for local UI state.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-02-04-REQ-001 | PARTIAL | `frontend/src/components/shell/app-shell.tsx` lines 115-160 and 290-385; `frontend/src/lib/shell/layout-state.ts` lines 1-24 and 157-205; `frontend/src/__tests__/lib/layout-state.test.ts` lines 50-128. Focused validation passed. | File Tree/workspace sidebar and Chat panes are resizable/collapsible. Toolkit is now a sidebar tab, not a dedicated resizable pane, due the loop-first pivot. |
| DEL-02-04-REQ-002 | PASS | `frontend/src/components/shell/app-shell.tsx` lines 81-93, 163-234, 236-287, and 294-311; `frontend/src/__tests__/lib/layout-state.test.ts` lines 22-48 and 110-140. Focused validation passed. | Layout state is persisted locally; pointer drag and keyboard Arrow/Home/End controls are implemented. |
| DEL-02-04-REQ-003 | PARTIAL | `frontend/src/components/shell/operator-toolkit-panel.tsx` lines 64-143; `frontend/src/lib/harness/toolkit.ts` lines 1-146; `frontend/src/__tests__/lib/harness-toolkit.test.ts` lines 15-50. Focused validation passed. | Toolkit exposes model, tools, max turns, and governance metadata. Mode/persona are runtime options but are not exposed as Toolkit controls here. |
| DEL-02-04-REQ-004 | PASS | `frontend/src/components/workspace/toolkit-provider.tsx` lines 45-92 and 136-195; `frontend/src/components/shell/operator-toolkit-panel.tsx` lines 152-207; `frontend/src/__tests__/lib/harness-toolkit.test.ts` lines 53-115. Focused validation passed. | Toolkit values and presets persist in local storage and sanitize stale preset IDs. |
| DEL-02-04-REQ-005 | PASS | `frontend/src/components/shell/operator-toolkit-panel.tsx` lines 49-52; `frontend/src/lib/harness/toolkit.ts` lines 106-146; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 255-319. Focused validation passed. | Presets only produce `opts`; SDK permission posture and tool exposure remain enforced downstream. |
| DEL-02-04-REQ-006 | PASS | `frontend/src/lib/harness/chat-draft.ts` lines 32-38 and 111-130; `frontend/src/__tests__/lib/harness-chat-draft.test.ts` lines 12-16 and 143-180. Focused validation passed. | Draft keys are scoped by root/persona/mode and persist draft plus attachment metadata. |
| DEL-02-04-REQ-007 | PASS | `frontend/src/lib/harness/chat-draft.ts` lines 47-57 and 87-108; `frontend/src/lib/harness/ui-attachments.ts` lines 92-119; `frontend/src/__tests__/lib/harness-chat-draft.test.ts` lines 18-45 and 84-140; `frontend/src/__tests__/lib/harness-ui-attachments.test.ts` lines 39-75. Focused validation passed. | Malformed draft and attachment records are dropped or reset with warnings. |
| DEL-02-04-REQ-008 | PASS | `frontend/src/components/workspace/toolkit-provider.tsx` lines 45-92; `frontend/src/lib/harness/chat-draft.ts` lines 63-130; `frontend/src/__tests__/lib/harness-chat-draft.test.ts` lines 103-140 and 181-208. Focused validation passed. | Local-storage read/write failures warn and fall back to in-memory behavior. |
| DEL-02-04-REQ-009 | PASS | `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 255-287. Focused validation passed. | Runtime mode mapping exists in SDK option builder: read-only, workspace-write, and gated bypass map to SDK permission posture. |
| DEL-02-04-REQ-010 | PASS | `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 290-319. Focused validation passed. | Write/Edit/Bash exposure changes by enforced runtime mode, not prompt hint text. |
| DEL-02-04-REQ-011 | PASS | `frontend/src/__tests__/lib/harness-options.test.ts` lines 65-137; `frontend/src/__tests__/lib/harness-toolkit.test.ts` lines 10-31. Focused validation passed. | Explicit Toolkit opts are deterministic; empty Toolkit values fall through to runtime fallback. |
| DEL-02-04-REQ-012 | PARTIAL | `frontend/src/lib/harness/toolkit.ts` lines 47-104; `frontend/src/__tests__/lib/harness-toolkit.test.ts` lines 53-90. Focused validation passed. | Unknown persisted Toolkit keys are ignored by sanitization, but warning behavior for unknown option keys is not visible in current tests. |
| DEL-02-04-REQ-013 | PASS | `frontend/src/components/shell/operator-toolkit-panel.tsx` lines 49-52 and 204-207; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 255-319. Focused validation passed. | Toolkit is explicitly local/non-authoritative and runtime permission/governance layers remain authoritative. |
| DEL-02-04-REQ-014 | TBD | `Specification.md` lines 56-62; `docs/ui/UI_POLISH_EXECUTION_PLAN.md` is absent. | The functional UI is dense and professional in code, but the referenced accepted polish checklist is not present and no browser visual review was performed in this assessment-only wave. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Toolkit pane wording is stale after the Toolkit folded into the sidebar. | Medium | `Specification.md` lines 9-12 and 27-28; `frontend/src/components/shell/app-shell.tsx` lines 36-49; `frontend/src/components/shell/workspace-sidebar.tsx` lines 35-43 and 208. | Reconcile dedicated Toolkit pane requirements to the right-sidebar Tool Kit tab. |
| Toolkit lacks explicit UI controls for mode and persona. | Medium | `Specification.md` line 29; `frontend/src/components/shell/operator-toolkit-panel.tsx` lines 64-143. | Add controls if still desired, or amend the requirement to state mode/persona are supplied by other runtime/UI surfaces. |
| Unknown-option warning behavior is not evidenced. | Low | `Specification.md` lines 60-61; `frontend/src/lib/harness/toolkit.ts` lines 47-104. | Add a test or runtime warning path for unknown option keys if required for issuance. |
| UI polish acceptance source is missing. | Medium | `Specification.md` line 62. | Resolve AMD-01 / polish-plan source before issuance. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Retain warning-limited source status until project-wide ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-02-04 has 14 active rows; `_DEPENDENCIES.md` lines 76-87 report 6 `NOT_APPLICABLE`, 6 `SATISFIED`, 1 `PENDING`, and 1 `TBD`, with REF-006 and adjacent runtime/policy contracts still open.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Reconcile Toolkit-pane wording to current sidebar Tool Kit tab behavior. | doc/reconcile | S | FIT | Loop-first pivot accepted as basis. |
| Decide whether Toolkit must expose mode/persona controls or whether those options belong in persona picker/session controls. | product/reconcile | S | FIT | Runtime option ownership review. |
| Add unknown-option warning evidence or amend the requirement to match sanitizer-only behavior. | test/doc | S | FIT | Runtime option contract owner input. |
| Run browser/component visual review if AMD-01 requires it. | test | S | FIT | AMD-01 ruling. |

## Issuance-Gate-Process Observations

DEL-02-04 exposes a common gate-process tension: implementation has evolved with the UI architecture, while some deliverable requirements still describe the older three-pane layout. Issuance should require reconciling that wording, not rebuilding obsolete layout.
