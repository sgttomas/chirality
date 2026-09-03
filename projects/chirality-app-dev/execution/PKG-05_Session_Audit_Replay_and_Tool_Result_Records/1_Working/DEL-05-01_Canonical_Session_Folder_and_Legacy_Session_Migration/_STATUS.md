# Status: DEL-05-01

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-03
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- **DEL-05-01-V3-01** (`SELECTABLE`) — v2 session-data lazy non-destructive access fixtures with typed failure.
  Trace: OUT-001 (canonical folder-backed store and first-touch legacy migration), AC-001, VER-001; DEL-05-01-R003/R004/R015; applied decomposition row L322 (lazy non-destructive access to and migration of legacy project-local session records while preserving list, resume, and delete behavior).
  Plan: WP-08; AT-035 v2-data portion (representative v2 data opens without destructive rewrite); AT-046 deletion portion; G5 fan-in later. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Existing `frontend/src/lib/harness/session-manager.ts` lazy conversion path (DEP-05-01-006, D-APP-41); representative current-release (2.0.0) session fixtures. No Root schema dependency: the target remains the existing canonical folder layout. Backup-before-write and rollback obligations named by the Carrier Map and plan WP-08 are not stated by row L322 or this Scope of Work and are unseated (`SCOPE_AMENDMENT_REQUIRED` S-4 in the seating packet MAPPING).
  Write locus: `frontend/src/lib/harness/session-manager.ts` and related tests/fixtures plus deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Fixtures for readable, malformed, and unsupported-version legacy project-local session records proving typed failure states, lazy non-destructive access (no destructive bulk rewrite), and preserved list, resume, and delete behavior; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the fixtures and typed failure states land with review PASS.
- **DEL-05-01-V3-02** (`NOT_SELECTABLE_UNTIL: accepted Root daemon session/storage schema routed to App (Root DEL-02-11) and the migration path frozen`) — migrate legacy session records to the accepted v3 daemon session shape preserving list/resume/delete.
  Trace: OUT-001, AC-001, VER-001; DEL-05-01-R003/R004/R011/R012; applied decomposition row L322 (daemon sessions remain Root-owned).
  Plan: WP-08; AT-035/AT-036/AT-046 App portions; G5 fan-in. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Root DEL-02-11 accepted storage/resume semantics (routed notice); DEL-05-01-V3-01; DEL-03-03-V3-01. Consent/root-home migration and account-change invalidation are unseated (`SCOPE_AMENDMENT_REQUIRED`, see the seating packet MAPPING).
  Write locus: `frontend/src/lib/harness/**` session client and tests plus deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Migration fixtures against the accepted schema identity with list/resume/delete preservation and fresh-thread/resume compatibility proofs; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the accepted-schema migration lands with G5 evidence.

## History
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; v3 Remaining items seeded (2, of which 1 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-07-22 - D-APP-72 provider-neutral selection and opaque adapter-session metadata completed with lazy legacy-Claude migration and Chirality-owned Pi session evidence; session/replay tests and G5 backcheck pass. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-21 - SCA-APP-002 added multi-adapter session compatibility to Remaining; state remains IN_PROGRESS.
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P44 assessment-pointer rider applied as a forward annotation; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
- 2026-07-19 - D-APP-56 R4-P31 dedicated unsafe/session-ID traversal guard coverage added and validated; the deliverable-local Remaining item was removed. State remains IN_PROGRESS; Checking Approval SHA preserved.
- 2026-07-19 - D-APP-68 ruling 3 managed-delegation `SessionRecord` ownership mapping recorded; state remains IN_PROGRESS and Checking Approval SHA is preserved.
