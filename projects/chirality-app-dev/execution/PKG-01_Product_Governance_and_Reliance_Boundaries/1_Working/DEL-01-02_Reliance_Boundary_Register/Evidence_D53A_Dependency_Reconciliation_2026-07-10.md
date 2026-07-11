# Evidence D53A - Dependency Reconciliation - DEL-01-02 Reliance Boundary Register

**Date:** 2026-07-10
**Queue row:** DRQ-01 of `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`
**Authority:** D-APP-53 ruling (Option A, 2026-07-10), `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`

## Epistemic status

This is derivative dependency-reconciliation evidence. It does not replace decomposition truth,
source/test evidence, decision records, or human lifecycle approvals. It authorizes no issuance, no
`CHECKING -> ISSUED` transition, no release act, and no scope change. Every closure below cites live
evidence re-verified in the working tree on 2026-07-10; satisfaction of a dependency row is register
bookkeeping, not deliverable acceptance.

## Per-row reconciliation

All paths relative to `projects/chirality-app-dev/` unless rooted. "Register" below means the DEL-01-02
deliverable artifact `docs/harness/reliance_boundary_register.md` (live in-tree). Section 9 IDs were
confirmed implemented in `frontend/scripts/validate-harness-section9.mjs`.

| DependencyID | Prior | New | Basis / evidence pointer |
|---|---|---|---|
| DEP-01-02-001 | TBD | SATISFIED | PKG-01 present in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §7 Packages; DEL-01-02 deliverable row (§8) lists PKG-01. |
| DEP-01-02-002 | TBD | SATISFIED | Decomposition §9 Scope Item Ledger row SOW-037 lists DEL-01-02. |
| DEP-01-02-003 | TBD | SATISFIED | Decomposition §9 row SOW-045 lists DEL-01-02. |
| DEP-01-02-004 | TBD | SATISFIED | Decomposition §9 row SOW-054 lists DEL-01-02. |
| DEP-01-02-005 | TBD | SATISFIED | Decomposition §9 row SOW-057 lists DEL-01-02. |
| DEP-01-02-006 | TBD | SATISFIED | Decomposition §9 row SOW-074 lists DEL-01-02. |
| DEP-01-02-007 | TBD | SATISFIED | `docs/DIRECTIVE.md` present; `_REFERENCES.md` REF-001 MATCH re-verified by live SHA-256 recompute (`14c77480…`). |
| DEP-01-02-008 | TBD | SATISFIED | `docs/CONTRACT.md` present; REF-002 MATCH re-verified live (`2f52a24c…`). |
| DEP-01-02-009 | TBD | SATISFIED | `docs/SPEC.md` present; REF-003 MATCH re-verified live (`2a63277a…`). |
| DEP-01-02-010 | TBD | SATISFIED | `docs/TYPES.md` present; REF-004 MATCH re-verified live (`aed33a0f…`). |
| DEP-01-02-011 | TBD | SATISFIED | `docs/PLAN.md` present; REF-005 MATCH re-verified live (`6f0baacc…`). |
| DEP-01-02-012 | TBD | SATISFIED | `docs/PRD.md` present; REF-006 MATCH under D-APP-38 corpus v1 re-verified live (`ac35fba4…`). |
| DEP-01-02-013 | TBD | SATISFIED | `agents/AGENT_SOFTWARE_DECOMP.md` present at the recorded absolute path; REF-007 MATCH re-verified live (`4f2c0a66…`). |
| DEP-01-02-014 | TBD | SATISFIED | Target `DEL-03-01` dir exists; register RB-ENGINE names DEL-03-01 as downstream closure owner; live surfaces `frontend/packages/harness-contract/src/agent-engine-port.ts`, `frontend/src/__tests__/lib/engine-conformance.test.ts`; `section9.runtime_engine_contract` implemented; reciprocal target-register row DEP-03-01-007 cross-references this register. |
| DEP-01-02-015 | TBD | SATISFIED | Target `DEL-03-02` dir exists; register RB-ENGINE names DEL-03-02; `frontend/src/lib/harness/turn-engine.ts` implements the per-turn lock (`releaseTurnLock`). |
| DEP-01-02-016 | TBD | SATISFIED | Target `DEL-04-02` dir exists; register RB-SETTINGS names DEL-04-02; `frontend/src/lib/harness/sdk-options-builder.ts` defaults `settingSources` to `[]`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` asserts it; `section9.settingsources_isolation` implemented. |
| DEP-01-02-017 | TBD | SATISFIED | Target `DEL-05-01` dir exists; register RB-TRANSCRIPT names DEL-05-01; canonical `.chirality/sessions` root in `frontend/src/lib/harness/session-manager.ts`; `section9.sdk_session_link_resume` implemented. |
| DEP-01-02-018 | TBD | SATISFIED | Target `DEL-05-02` dir exists; register RB-AUDIT names DEL-05-02; `appendHarnessEvent` writes `events.jsonl` in `frontend/src/lib/harness/session-events.ts` with schema `frontend/packages/harness-contract/src/event-schema.ts`; `section9.adapter_turn_engine_event_log` implemented. TargetLocation literal corrected (see hygiene). |
| DEP-01-02-019 | TBD | SATISFIED | Target `DEL-05-04` dir exists; register RB-AUDIT/RB-TRANSCRIPT name DEL-05-04; `replayHarnessEvents` in `frontend/src/lib/harness/session-events.ts`, `frontend/src/components/shell/transcript-stream-view.tsx`, `frontend/src/__tests__/lib/transcript-replay.test.ts`; `section9.session_event_replay` implemented. |
| DEP-01-02-020 | TBD | SATISFIED | Target `DEL-06-01` dir exists; register RB-PERMISSION names DEL-06-01; `frontend/src/lib/harness/permission-overlay.ts` present; `section9.permission_overlay_hard_deny_precedence` implemented. |
| DEP-01-02-021 | TBD | SATISFIED | Target `DEL-06-04` dir exists; register RB-FILESYSTEM/RB-HOOKS name DEL-06-04; `frontend/src/lib/harness/tool-path-policy.ts` and `frontend/src/lib/harness/chirality-hooks.ts` present; `section9.path_containment_hook` and `section9.instruction_root_protection_hook` implemented. |
| DEP-01-02-022 | TBD | SATISFIED | Target `DEL-06-06` dir exists; register RB-HOOKS names DEL-06-06; `frontend/src/lib/harness/chirality-hooks.ts` present; `section9.context_compaction_boundary` implemented. |
| DEP-01-02-023 | TBD | SATISFIED | Target `DEL-08-04` dir exists; register RB-SUBAGENT names DEL-08-04; `frontend/src/lib/harness/subagent-governance.ts` and `subagent-bridge.ts` present; `section9.subagent_governance_hook` implemented. |
| DEP-01-02-024 | TBD | SATISFIED | Target `DEL-09-02` dir exists; register Test Index maps boundaries to implemented Section 9 IDs; `frontend/scripts/validate-harness-section9.mjs` implements the runtime validation IDs. |

Rows closed: 24. Rows left open: 0. For every closed row `ProposedMaturity` was set to the row's
`RequiredMaturity` (`SEMANTIC_READY`) and `LastSeen` bumped to 2026-07-10.

## Hygiene: summary/pointer repairs

- `DEP-01-02-018` `TargetLocation` corrected from
  `…/DEL-05-02_HarnessEvent_Schema_and_Append-Only_JSONL` to
  `…/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL` to match the real directory name
  (DRQ-01 extra scope).
- `_DEPENDENCIES.md`: SatisfactionStatus lifecycle table updated (`TBD 24` -> `SATISFIED 24`); dated
  run note and Run History row appended; dated correction note added for the now-stale 2026-05-20
  `OPEN_BLOCKERS` warning (original text retained as history).
- Observation only (no edit made; outside this deliverable's write scope): the register file
  `docs/harness/reliance_boundary_register.md` cites `frontend/src/lib/harness/agent-engine-port.ts`
  and `frontend/src/lib/harness/event-schema.ts`, which now live at
  `frontend/packages/harness-contract/src/agent-engine-port.ts` and
  `frontend/packages/harness-contract/src/event-schema.ts`. The symbols (`AgentEnginePort`,
  `HarnessEvent`) are live; the pointer drift is recorded here for a future register refresh.

## Validation

`python3 execution/_Scripts/validate_dependencies.py <this deliverable>/Dependencies.csv` -> PASS,
24 rows, 0 errors, 0 warnings (2026-07-10).
