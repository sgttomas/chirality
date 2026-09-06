# Status: DEL-02-04

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-04
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

The versioned `chirality.woven-workspace/v1` state store, its non-destructive
rollback-safe migration, the additive v1 fields added by the 2026-07-24
redesign tranche (`theme`; bounded `sessionSurfaces` map;
`navigatorExpandedSurfaces`), and the isolation, storage-failure,
malformed-record, keyboard/focus, and reduced-motion evidence are implemented
and evidenced (PR #323 merge `403f228f4`; redesign tranche 2026-07-24). See
`_run_records/R6_WOVEN_REDESIGN_2026-07-24.md` and
`execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/`. What
remains:

- Keep the schema-version discipline for any future workspace-state field: new
  fields stay additive and optional-with-default under the unchanged
  `chirality.woven-workspace/v1` schema string, or a versioned read branch must
  land in the same tranche. Bumping the schema constant without that branch
  silently discards all stored state.

- **DEL-02-04-V3-01** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed`) — activity strip and Activity view; retire the resizable shelf; additive v1 workspace-state fields (T5).
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L310 (per-view right-panel widths, expand state, chat annotations, known folders, chat rung and declined proposal triggers as additive v1 fields; the one-line activity strip in place of the resizable shelf); SOW-004 L174; SOW-008 L178.
  Plan: T5; SR-07 (strip), SR-02 and SR-05 (per-view widths, expand), SR-03 and SR-24 (additive fields). Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: DEL-02-02-V3-03; the Activity view mounts in the right-panel view switcher from DEL-02-03-V3-01 and cannot land before it, while the strip and the additive fields can; DEL-02-01-V3-02, DEL-02-01-V3-03, DEL-02-02-V3-04, and DEL-02-03-V3-01 consume the additive fields.
  Write locus: `frontend/src/lib/woven-dialogue/woven-workspace-state.ts` (additive v1 fields under the existing schema string with rollback-safe migration), `frontend/src/components/woven-dialogue/activity-shelf.tsx` retirement and the strip and Activity view components, migration guards and tests; deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: a one-line activity strip in place of the resizable shelf; the Activity view in the right panel; additive fields (per-view widths, expand state, chat annotations, known folders, chat rung, declined proposal triggers) with migration tests proving prior state is preserved for rollback; convenience state never transfers session authority and never stands in for the workflow file; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS.

## History
- 2026-09-05 - Additive-state partial closeout: final full-diff reviewPASS; full1636testsPASS/4skipped, typecheck/build/Section9/selfcheck/350pytest/holdPASS. Actual local premergeFAIL HTTP503 ENGINE_UNAVAILABLE missing daemon binding; source-bound branchCI owed. Parent integration/governed review/CHANGE pending; Activity strip/view and full Remaining/merge condition retained. See `_run_records/TASK_RUN_2026-09-05_ADDITIVE_STATE_PARTIAL.md`.
- 2026-09-05 - Additive-state source fan-in: focused32testsPASS; full revised-diff review PASS after parent source challenge and independent P2 confirmation/repair retaining cross-root titles/rung hints. Global gates pending; partial obligation only. Prior records preserved in iteration3 instances/pkg02_fields.
- 2026-09-05 - DEL-02-04-V3-01 partial additive-state implementation under APP_LOOP_SHELL_2026-09-05 iteration3: state module/library tests only; focused31testsPASS; source frozen for fresh review and parent global gates. See `_run_records/TASK_RUN_2026-09-05_ADDITIVE_STATE_PARTIAL.md`. Activity strip/view and consumer integration remain; full Remaining/merge condition and lifecycle unchanged. Frontend mutation requires A1 restage and fresh owner proof.
- 2026-09-05 - D-APP-109 (owner direction 2026-09-05): dependency register re-extracted against the applied decomposition row L310 with the held edge proposals emitted as cycle-participating, non-gating rows (run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`); `_CONTEXT.md` Traceability, Anticipated Artifacts, and Source Authority aligned to the applied row. No Remaining, lifecycle, Checking Approval SHA, product, or release change.
- 2026-09-04 - SCA-APP-010 shell-redesign seating (D-APP-108; owner adopted the seating list as presented): Remaining items seeded DEL-02-04-V3-01 (SELECTABLE: none) with gate, dependency, write-locus, check, and return contracts; ruled questions cited by item. `ScopeOfWork.md` re-pinned to the applied decomposition at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` with a SCA-APP-010 Gate-5 Current Contract section; `_CONTEXT.md` and `_REFERENCES.md` aligned (WI-011, WI-012, WI-013, WI-014, WI-015). Run evidence `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-07-24 - Woven Dialogue visual redesign and IA consolidation tranche recorded in `_run_records/R6_WOVEN_REDESIGN_2026-07-24.md`; the four SCA-APP-004 Remaining items were rewritten to the single residual of keeping schema-version discipline for future additive v1 workspace-state fields. State remains IN_PROGRESS; accepted historical evidence and Checking Approval SHA are preserved.
- 2026-07-23 - SCA-APP-004 Gate-5 execution-record propagation added the owner-approved versioned workspace-state, explicit-context, focus, isolation, and rollback tranche. State remains IN_PROGRESS; accepted historical evidence and Checking Approval SHA are preserved.
- 2026-07-12 - D-APP-56 final code tranche implemented UPD-110 AppShell keyboard-resize interaction coverage; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 consolidated R5 decision application recorded; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-079; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 R5 P45 applied UPD-109, UPD-111; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
