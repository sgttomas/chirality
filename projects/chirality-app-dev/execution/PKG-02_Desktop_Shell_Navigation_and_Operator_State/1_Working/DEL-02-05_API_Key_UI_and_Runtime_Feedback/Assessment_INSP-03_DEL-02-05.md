# Assessment INSP-03: DEL-02-05 API Key UI and Runtime Feedback

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-02-05 |
| Package | PKG-02 Desktop Shell Navigation and Operator State |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `50b063f3ec4d9df900b4f2c465cf2f9ac79e91a0` |
| Spec source | `Specification.md` lines 5-78 |

## Scope

DEL-02-05 covers API-key settings/status UI, secure-storage feedback, typed runtime error display, retry-preserving local state, browser-facing SSE compatibility, and runtime/provider redaction boundaries.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-02-05-R01 | PASS | `frontend/src/components/settings/api-key-settings.tsx` lines 16-20 and 63-94; `frontend/electron/api-key-ipc.ts` lines 27-39; `frontend/electron/api-key-storage.ts` lines 26-48; `frontend/src/__tests__/electron/api-key-storage.test.ts` lines 65-73; `frontend/src/__tests__/electron/api-key-ipc.test.ts` lines 77-95. Focused validation passed. | UI calls Electron IPC; storage writes encrypted key material under Electron `userData`, not project root. |
| DEL-02-05-R02 | PASS | `frontend/src/components/settings/api-key-settings.tsx` lines 5-9 and 117-139; `frontend/electron/api-key-ipc.ts` lines 51-69; `frontend/src/__tests__/electron/api-key-ipc.test.ts` lines 97-122. Focused validation passed. | Status reports `ui`, `env`, or `none` without rendering key material. |
| DEL-02-05-R03 | PASS | `frontend/electron/api-key-ipc.ts` lines 51-69; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 258-270 and 816-840; `frontend/src/__tests__/electron/api-key-ipc.test.ts` lines 97-122; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 1114-1189; `frontend/src/__tests__/lib/harness-runtime.test.ts` lines 57-87. Focused validation passed. | UI status reports `ui > env > none`; runtime key selection is UI key, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. |
| DEL-02-05-R04 | PASS | `frontend/src/components/settings/api-key-settings.tsx` lines 63-90 and 124-139; `frontend/electron/api-key-storage.ts` lines 39-48 and 103-108; `frontend/src/__tests__/electron/api-key-storage.test.ts` lines 108-114. Focused validation passed. | Unavailable secure storage throws/fails closed and UI has explicit warning/error copy. |
| DEL-02-05-R05 | PASS | `frontend/src/lib/harness/error-display.ts` lines 4-62 and 138-166; `frontend/src/__tests__/lib/harness-error-display.test.ts` lines 6-106. Focused validation passed. | Typed client errors map to title, message, next-step, and code. |
| DEL-02-05-R06 | PASS | `frontend/src/lib/harness/chat-draft.ts` lines 32-57 and 111-130; `frontend/src/__tests__/lib/harness-chat-draft.test.ts` lines 12-45 and 143-180; `frontend/src/__tests__/lib/harness-ui-attachments.test.ts` lines 39-75. Focused validation passed. | Draft and attachment metadata persist locally and are sanitized independently of runtime error outcomes. |
| DEL-02-05-R07 | PASS | `frontend/src/lib/harness/client.ts` lines 84-134; `frontend/src/__tests__/lib/harness-client.test.ts` lines 180-245; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 760-900. Focused validation passed. | Browser-facing `turn:error` and terminal `process:exit` events remain parseable and named compatibly. |
| DEL-02-05-R08 | PASS | `frontend/electron/api-key-storage.ts` lines 1-10 and 39-48; `frontend/src/components/settings/api-key-settings.tsx` lines 117-139; `frontend/src/lib/harness/chat-draft.ts` lines 3-7 and 32-38; `frontend/src/__tests__/electron/api-key-storage.test.ts` lines 65-73. Focused validation passed. | Key material and UI state are local/runtime convenience state, not project truth files. |
| DEL-02-05-R09 | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 115-142, 506-520, and 594-620; `frontend/src/lib/harness/harness-ui-bridge.ts` lines 5-34; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 572-610; `frontend/src/__tests__/lib/harness-ui-bridge.test.ts` lines 49-62. Focused validation passed. | Provider/SDK error text and bridged harness events redact configured API keys, including encoded variants in the broader manager test suite. |
| DEL-02-05-R10 | PARTIAL | `Specification.md` lines 38 and 61-62; `frontend/src/lib/harness/error-display.ts` lines 11-62; `frontend/src/__tests__/lib/harness-error-display.test.ts` lines 6-106. Focused validation passed. | UI consumes current typed errors, but canonical taxonomy ownership remains cross-package and still needs architecture review before issuance. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Secure-storage code comment labels DEL-02-06, but this package has DEL-02-05. | Low | `frontend/electron/api-key-storage.ts` line 2; `frontend/src/lib/harness/api-key-store.ts` line 2. | Correct comments during a future docs/code hygiene pass. |
| Canonical runtime error taxonomy ownership remains unresolved. | Medium | `Specification.md` lines 38 and 61-62; `_DEPENDENCIES.md` lines 47-50 and 66-74. | Resolve with PKG-03/04/05 assessment synthesis before issuance. |
| Browser render evidence for the API key settings component is not present. | Medium | `Specification.md` lines 53-56. | Add component/browser tests if AMD-01 requires UI rendering evidence. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Retain warning-limited source status until project-wide ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-02-05 has 6 active rows, all `TBD` per `_DEPENDENCIES.md` lines 59-68, with runtime/API contract ownership unresolved.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Resolve typed runtime/provider error taxonomy ownership across PKG-03, PKG-04, and PKG-05. | governance/reconcile | M | FIT | Complete corresponding INSP-03 waves. |
| Add a render/integration test for API key settings status, secure-storage unavailable copy, and non-disclosure of key material if AMD-01 requires it. | test | S | FIT | AMD-01 ruling. |
| Fix stale DEL-02-06 comments in key-storage files. | doc/code hygiene | S | FIT | Scope a small cleanup tranche. |

## Issuance-Gate-Process Observations

DEL-02-05 is one of the stronger PKG-02 deliverables in runnable evidence. The remaining gate question is whether cross-package taxonomy ownership and render-level API-key UI evidence must be closed before issuance, or can be accepted as later hardening.

## 2026-08-20 R03 Calibration

The dated 2026-06-20 R03 row above overreached: its cited IPC test asserted
`ui > env > none` but returned `env` whenever an environment key coexisted with
the safeStorage/UI key, and the runtime resolver still preferred the
compatibility alias over the canonical environment key. That historical
assessment is preserved; it is superseded for R03 by this calibration.

Current R03 status is **PASS** for the repaired product candidate. The daemon
credential store is the sole resolver and reports a non-secret
`source: ui | env | none` from the accepted order UI safeStorage,
`ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. Electron IPC validates
and projects that source without reading environment variables itself. Direct
tests cover UI plus both environment variables (`ui`), canonical-only and
compatibility-alias-only (`env`), no credential (`none`), malformed or
inconsistent daemon replies (fail closed), provider isolation, and
non-disclosure.

Evidence: `frontend/electron/api-key-storage.ts`,
`frontend/electron/api-key-ipc.ts`, their focused tests, and
`_run_records/TASK_RUN_2026-08-20_1004.md`. Focused Vitest passed 3 files / 47
tests; the registered frontend suite passed 150 files / 1,174 tests with one
file / four tests skipped; typecheck, build, 350 harness tests, harness
self-check, APP-HOLD, scope, and whitespace checks passed. This calibration does not change any
other requirement row, dependency, lifecycle state, Remaining item, or the
Checking Approval SHA.
