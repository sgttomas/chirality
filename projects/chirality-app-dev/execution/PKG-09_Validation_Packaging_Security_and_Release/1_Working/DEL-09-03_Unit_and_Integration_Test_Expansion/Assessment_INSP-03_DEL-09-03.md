# Assessment INSP-03: DEL-09-03 Unit and Integration Test Expansion

Deliverable: DEL-09-03
Package: PKG-09 Validation, Packaging, Security, and Release
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `d0766e0f24b923f7925c711fe05e0cf5d28fd1fb`
Spec source: `Specification.md`

## Scope

This assessment inspected the unit and integration test expansion for runtime, SSE, replay, attachments, lifecycle, dependency registers, interrupt/cancel, denied actions, and provider-neutral events. It did not add tests or change runtime code.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ001 - Test `TurnEngine.runTurn` without HTTP. | PASS | `frontend/src/lib/harness/turn-engine.ts` exposes and runs `runTurn` at lines 186-305; `frontend/src/__tests__/lib/turn-engine.test.ts` covers no-HTTP turn execution at lines 160-205. | Direct runtime tests exist. |
| REQ002 - Test `/api/harness/turn` SSE route compatibility and browser event names. | PASS | `frontend/src/app/api/harness/turn/route.ts` streams TurnEngine events at lines 9-46; `frontend/src/__tests__/api/harness/routes.test.ts` covers stable SSE names at lines 520-547. | Route compatibility is covered. |
| REQ003 - Persist accepted input before SDK/model execution. | PASS | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` appends `turn.accepted` before SDK query at lines 203-221; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` emits `turn.accepted` before client use at lines 756-840. | Evidence confirms accepted lifecycle precedes provider execution. |
| REQ004 - Every accepted turn reaches terminal success/failure/cancel/interruption event. | PASS | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` emits terminal success/cancel/failure paths at lines 279-360; route tests cover failure and interrupt terminal outcomes at lines 731-787 and 971-1040. | Terminal taxonomy remains an INSP finding elsewhere, but tests cover required terminal behavior. |
| REQ005 - Append-only HarnessEvent JSONL replay with malformed tail. | PASS | `frontend/src/lib/harness/session-events.ts` appends events at lines 14-22 and replays with malformed-line counting at lines 50-84; session-event tests cover append/replay and malformed tails. | Replay behavior is directly tested. |
| REQ006 - Attachment resolver validates paths, file type, symlinks, readability, and size limits. | PASS | `frontend/src/lib/harness/attachment-resolver.ts` defines limits/extensions at lines 6-22 and validates path/readability/symlink/regular-file/file-size/total-size at lines 47-141; attachment resolver tests cover allowed, unsupported, symlink, per-file, and total-budget cases. | Attachment validation is broad and server-side. |
| REQ007 - Status parsing and forward lifecycle with approval SHA. | PASS | `frontend/src/lib/lifecycle/transition.ts`, status parser/writer, and working-root deliverable contract tests cover lifecycle/approval SHA behavior; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` covers lifecycle transitions at lines 130-288. | All deliverables are currently CHECKING; no issuance was attempted. |
| REQ008 - Dependencies.csv v3.1 parsing/validation/writing/provenance/host consistency/retirement/legacy normalization. | PASS | `frontend/src/lib/dependencies/schema.ts` defines v3.1 columns/enums and legacy normalization at lines 1-223; register reader/writer enforce normalization, provenance, targets, satisfaction, and serialization; dependency contract tests cover invalid anchors, provenance, duplicates, satisfaction, and legacy normalization. | Dependency CSV mechanics are covered. |
| REQ009 - Denied actions do not execute and emit events when support exists. | PASS | `frontend/src/lib/harness/permission-overlay.ts` denies action classes at lines 111-265 and enforces canUseTool decisions at lines 338-447; route tests cover denied governance/subagent/tool paths at lines 549-729. | Denials are enforced before execution. |
| REQ010 - Public APIs/canonical events stay provider-neutral; SDK appears only in adapter metadata. | PASS | `frontend/src/lib/harness/session-events.ts` and SDK mapper tests maintain HarnessEvent/UIEvent separation; adapter-specific metadata is emitted in provider manager lifecycle events. | Provider-specific details are bounded to adapter metadata. |
| REQ011 - At least one implemented or deferred test per behavior group. | PASS | The focused PKG-09 test set covers runtime, SSE, replay, attachments, lifecycle, dependencies, denied actions, packaging policy, network policy, and key/security surfaces. | No unrepresented behavior group was found in source review. |
| REQ012 - Preserve stable `npm run test` evidence. | PARTIAL | The test script exists in `frontend/package.json` line 14 and focused tests were selected for this inspection. | A full `npm run test` was not rerun solely for this assessment wave. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| Full-suite test evidence not refreshed by this wave | Medium | Focused validation is appropriate for assessment-only work, but issuance should have a fresh complete `npm run test` result. | Validation tranche |
| Terminal taxonomy still spans multiple owners | Medium | Terminal behavior is tested, but taxonomy reconciliation remains visible across runtime assessments. | Runtime reconciliation tranche |
| Dependency tests cover mechanics, not closure satisfaction | Low | Register mechanics pass, but this assessment does not satisfy any deliverable dependency rows. | Dependency workflow |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-09-03 still has 13 active dependency rows with `SatisfactionStatus: TBD`; closure remains open.

## Forward Development Recommendation

1. Before issuance, run and archive a full `npm run test` result plus the focused release/security subset. Type: validation evidence. Size: S. Strategic fit: ON-STRATEGY.
2. Add a short test manifest mapping each behavior group to concrete test files and any intentionally deferred cases. Type: docs/test. Size: S. Strategic fit: ON-STRATEGY.
3. Reconcile terminal lifecycle naming across runtime, route, and assessment surfaces. Type: docs/code reconciliation. Size: M. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

This deliverable demonstrates why an issuance gate should require both source-mapped coverage and a fresh command result. Static/source evidence is strong, but it should not replace a current full-suite test artifact.
