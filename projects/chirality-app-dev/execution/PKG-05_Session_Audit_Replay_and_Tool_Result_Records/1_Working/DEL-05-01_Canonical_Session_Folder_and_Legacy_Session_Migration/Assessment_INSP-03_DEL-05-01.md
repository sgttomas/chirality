# Assessment INSP-03: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-05-01 |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed source state | ADQ-08 working tree based on `86e934f39d602e5c25986b4d3fea7cbfc0ac1628` |
| Spec source | `Specification.md` |

## Scope

DEL-05-01 covers canonical `.chirality/sessions/<sessionId>/` layout, eager legacy flat-session conversion, normalized session CRUD, SDK linkage metadata, duplicate folder/flat resolution, and session-root override behavior.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-01-R001 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 84-95 and 167-183; `frontend/src/__tests__/lib/session-manager.test.ts` lines 57-71. | New session records are written to `{sessionRoot}/{sessionId}/session.json`. |
| DEL-05-01-R002 | PARTIAL | `frontend/src/lib/harness/session-manager.ts` lines 133-139; `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/lib/harness/tool-result-artifacts.ts`. | `session.json`, `events.jsonl`, and artifacts use the folder shape. Explicit `turns/` and `sdk/` directory materialization remains demand-driven/downstream. |
| DEL-05-01-R003 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 142-164; `frontend/src/__tests__/lib/session-manager.test.ts` lines 73-105. | Legacy flat records are canonicalized on resume/read. |
| DEL-05-01-R004 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 210-238; `frontend/src/__tests__/lib/session-manager.test.ts` lines 160-178. | Legacy records are discovered by list, returned once, converted, and removed as flat files. |
| DEL-05-01-R005 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 23-67 and 210-238. | CRUD remains bound to accessible normalized project roots. |
| DEL-05-01-R006 | PASS | `frontend/src/lib/harness/types.ts` lines 23-42; `frontend/src/lib/harness/session-manager.ts` lines 195-207. | Stable session metadata and SDK linkage fields persist through `session.json`. |
| DEL-05-01-R007 | PASS | `frontend/src/lib/harness/types.ts` lines 30-38; `frontend/src/__tests__/lib/session-manager.test.ts` lines 107-158. | SDK and legacy provider identifiers remain metadata; `sessionId` remains the Chirality identity. |
| DEL-05-01-R008 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/__tests__/lib/session-events.test.ts`. | Runtime audit events append to canonical per-session `events.jsonl`. |
| DEL-05-01-R009 | PARTIAL | `frontend/src/lib/harness/types.ts` lines 33-35; R1/OI-002 handoff remains active. | Transcript path/store-key fields exist, but final SDK transcript placement remains out of scope for DEL-05-01. |
| DEL-05-01-R010 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 111-164; `frontend/src/__tests__/lib/session-manager.test.ts` lines 107-158. | Duplicate folder/flat records merge with canonical precedence, preserve legacy-only fields, write canonical, and remove flat. |
| DEL-05-01-R011 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 70-95, 167-183, and 241-247. | Session IDs are stable path keys and are generated once at create. |
| DEL-05-01-R012 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 111-164 and 195-207. | Path-changing migration preserves the stable `sessionId` in the canonical record. |
| DEL-05-01-R013 | PARTIAL | `frontend/src/lib/harness/run-logger.ts`; `frontend/src/lib/harness/session-events.ts` lines 14-22. | Event/artifact redaction remains covered by DEL-05-03 and release gates; ADQ-08 did not add secret persistence. |
| DEL-05-01-R014 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 15-17; `frontend/src/__tests__/lib/session-manager.test.ts` lines 41-47. | `CHIRALITY_SESSION_ROOT` override is honored by the session manager. |
| DEL-05-01-R015 | PASS | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/Evidence_ADQ-08_Canonical_Session_Migration.md`. | Implementation paths, helper behavior, and validation commands are recorded. |
| DEL-05-01-R016 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 167-183; `frontend/src/__tests__/lib/session-manager.test.ts` lines 57-71. | New sessions do not write flat legacy files. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| SDK transcript/store placement is metadata-only and not replay-closed. | Medium | `frontend/src/lib/harness/types.ts` lines 33-35; DEL-04-01/DEL-05-04 dependency handoffs. | Carry transcript placement into DEL-05-04/R1 and keep SDK transcripts non-canonical unless imported into `HarnessEvent` form. |
| `turns/` and `sdk/` folders are not eagerly materialized. | Low | `frontend/src/lib/harness/session-manager.ts` lines 133-139. | Keep demand-driven creation unless a later replay/transcript tranche requires placeholder directories. |

## Source-State Caveat

D-APP-38 corpus v2 is current for this deliverable. `_REFERENCES.md` reports MATCH for PRD, SPEC, TYPES, CONTRACT, and PLAN. No `_STATUS.md` lifecycle state was changed.

## Dependency Closure Note

ADQ-08 satisfies the implementation prerequisite for current session storage paths, the duplicate folder/flat semantics constraint under D-APP-41, and the duplicate delete fixture requirement. R1/OI-002 SDK transcript placement remains open and is not closed by this tranche.

## Validation Snapshot

Validation passed:

- `npm run test -- src/__tests__/lib/session-manager.test.ts --testTimeout=15000`
- `npm run test -- src/__tests__/api/harness/routes.test.ts src/__tests__/lib/session-events.test.ts src/__tests__/lib/turn-engine.test.ts --testTimeout=15000`
- `npm run typecheck`
- `npm run harness:validate:section8`
- `npm run harness:validate:section9`
- `npm run test -- --testTimeout=15000`
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`
- `git diff --check`

Closeout validation details are recorded in `Evidence_ADQ-08_Canonical_Session_Migration.md`.
