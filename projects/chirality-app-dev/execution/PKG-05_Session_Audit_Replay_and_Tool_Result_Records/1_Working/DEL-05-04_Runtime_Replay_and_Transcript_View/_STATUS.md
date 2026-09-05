# Status: DEL-05-04

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-04
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- Prior scope note (closed 2026-08-17; see History): the daemon/client
  vertical-slice residual was closed by the accepted canonical replay/restart
  integration proof; no pre-v3 residual remains. The v3 items follow.

- **DEL-05-04-V3-01** (`NOT_SELECTABLE_UNTIL: accepted Root restart/resume and storage semantics routed to App (Root DEL-02-11) and DEL-05-01-V3-02 landed`) — present restart/resume continuity truthfully in the read-only replay lens.
  Trace: OUT-001, AC-001, VER-001; DEL-05-04-REQ-014/016/018/019; applied decomposition row L325 (live versus replayed state and primary versus observational authority remain explicit).
  Plan: WP-08; AT-036 presentation portion; G5 fan-in. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Root DEL-02-11 accepted semantics (routed notice); DEL-05-01-V3-02; DEL-03-03-V3-01; DEP-05-04-005/006.
  Write locus: `frontend/src/**` replay/projection surfaces and tests plus deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Fixtures proving a stored thread is presented as resumable only on exact root/account/policy match, otherwise fresh, and that read-only replay never implies in-flight re-attach; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the truthful presentation lands with G5 evidence.

- **DEL-05-04-V3-02** (`NOT_SELECTABLE_UNTIL: DEL-02-03-V3-01 landed`) — Session view: the replay lens mounted in the right panel with a read-only banner and a parent link (T3 part).
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L339 (selected-session read-only replay lens); SOW-006 L176 (the Session view is read-only, never takes the centre, and is distinct from the mounted primary).
  Plan: T3 part; SR-08. Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: DEL-02-03-V3-01 (the view switcher); DEL-02-02-V3-03 (replay beside a visible primary); the existing `selected-session-replay-lens.tsx`.
  Write locus: `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx` mount and the right-panel Session view, tests; deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: the Session view renders in the right panel with a read-only banner and a parent link, never takes the centre, and never transfers the primary dialogue's draft, attachments, or context; live versus replayed state stays explicit; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS; restart/resume continuity remains DEL-05-04-V3-01.

## History
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P44 docs applied UPD-098; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
- 2026-07-23 - SCA-APP-004 Gate-5 propagation reconciled DEL-05-04 to the
  Woven Dialogue replay/projection contract; existing daemon/client replay
  residue was preserved, new implementation/validation work was added, and
  lifecycle remained IN_PROGRESS.
- 2026-07-24 - Woven Dialogue visual redesign and IA consolidation tranche
  recorded in `_run_records/R1_WOVEN_REDESIGN_2026-07-24.md`; the SCA-APP-004
  replay-lens Remaining item was rewritten to its residual of unevidenced
  transcript-item rendering against a real daemon session, and the gated
  daemon/client vertical-slice item was retained verbatim. State remains
  IN_PROGRESS; accepted historical evidence and Checking Approval SHA are
  preserved.
- 2026-07-25 - Daemon-service tranche recorded in
  `_run_records/R2_DAEMON_SERVICE_2026-07-25.md`. No replay or transcript code
  changed; the transcript-item Remaining entry is amended only to record that
  daemon unavailability no longer blocks it and to point at the packaged
  evidence that a real daemon-owned session is producible. Both Remaining items
  stay open. State remains IN_PROGRESS; accepted historical evidence and
  Checking Approval SHA are preserved.
- 2026-08-03 - D-APP-86 Option A integrated parity evidence closed only the
  real-daemon transcript-item-rendering residual: one admitted
  `WORKING_ITEMS` / `agent1` session rendered one read-only replay transcript
  item from two events, ending at the recorded terminal event. No parent/child
  attribution existed and none was inferred. Evidence is pointed from
  `_run_records/R3_DAPP86_REAL_DAEMON_REPLAY_2026-08-03.md`. The separate
  Desktop/CLI restart-and-migration item remains gated and unchanged. State
  remains IN_PROGRESS; Authorization Basis, Directive, and Checking Approval
  SHA are preserved. Any later accepted D-APP-88 distinct-helper
  implementation remains a non-blocking parity-rerun trigger.
- 2026-08-17 - The live daemon/client vertical-slice gate was confirmed
  satisfied. A dedicated App integration case proved the authenticated Desktop
  port and Root `runCli session replay --json` façade decode structurally equal
  canonical manager/child sessions after
  non-destructive lazy legacy migration and again after a fresh daemon/service
  restart. Recorded `agent1`/`agent2` roles, exact `parentSessionId`, ordered
  events, and engine/provider/model attribution survive. Focused Vitest and
  worktree-correct typecheck passed. An integrated review identified and then
  accepted remediation of record wording that had overstated structural
  equality as byte equivalence. Evidence is recorded in
  `_run_records/CANONICAL_REPLAY_RESTART_2026-08-17.md`. The sole Remaining
  item is closed; lifecycle remains IN_PROGRESS and no release claim is made.
  Integrated CLI-boundary review then required the actual Root `runCli` façade
  rather than a second runtime client and raw-buffer comparisons for legacy
  byte preservation. Final focused test/typecheck and independent backcheck
  passed at blob `310e0c9539dbac6af89159bd312b2a93a082689b`; closure remains accepted.
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; v3 Remaining items seeded (1, of which 0 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-09-04 - SCA-APP-010 shell-redesign seating (D-APP-108; owner adopted the seating list as presented): Remaining items seeded DEL-05-04-V3-02 (SELECTABLE: none) with gate, dependency, write-locus, check, and return contracts; ruled questions cited by item. Outside the thirteen SCA-APP-010 carriers: seating only, no Scope of Work, context, or reference change. Run evidence `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
