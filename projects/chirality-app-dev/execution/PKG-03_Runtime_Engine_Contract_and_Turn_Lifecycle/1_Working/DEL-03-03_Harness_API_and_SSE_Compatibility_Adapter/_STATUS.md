# Status: DEL-03-03

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-12
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- **DEL-03-03-V3-01** (`NOT_SELECTABLE_UNTIL: the D-GOV-43 spike lands the transport repair on the production path`) — harness API and SSE adapter retained and repaired (topology A2, D-APP-127): keep the `/api/harness/*` routes and the loopback HTTP/SSE channel through the in-process Next server as the renderer channel; add SSE comment keepalives, remove the idle timeout that ends a turn, and make a renderer disconnect unsubscribe without interrupting the turn (the Runtime owns the active turn; explicit Stop is the interrupt endpoint; reopening recovers current state, missed activity and outstanding decisions without re-sending the prompt); carry the extensible event representation (upstream method names, identifiers and payloads preserved; normalized views for known items; unfamiliar notifications inspectable, never dropped) in place of the closed schema v2 and the eight-name `UIEvent` set.
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L305 (keep `/api/harness/*` shapes and browser SSE event names stable while runtime policy moves behind services).
  Plan: WP-05/WP-08; G-WIRE; AT-024 App-hop raw-event rejection portion. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: the Runtime service transport repair of the same tranche (SSE writer keepalives and close handler in `runtime-daemon.ts`; stream timeout in `packages/client`); DEP-03-03-006/007/010 read with D-GOV-43. Relaunch resumes threads through `thread/resume` (D-GOV-43 item 5; Root DEL-02-11's continuity gate is retired); DEL-05-04 owns truthful presentation.
  Write locus: `frontend/src/app/api/harness/**`, route adapter tests, SSE fixtures, and deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Route adapter tests and SSE fixtures proving stable route shapes, keepalives, no idle-timeout interruption, disconnect without interrupt, and generic inspectable rendering of unfamiliar notifications at the App boundary; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the repaired transport lands with the S-2 and renderer-disconnect continuity evidence.

## History
- 2026-09-12 - D-GOV-43 application (`execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`): DEL-03-03 is "retained and repaired" under topology A2 (the A2 supplement re-expresses IMPACT.md's "replace with the IPC channel"); V3-01 revised from closed-schema-v2 consumption to the transport repair and the extensible event representation. `RouteAdapterTestIndex.md` and `SSE_Compatibility_Fixture_README.md` are preserved as history. No lifecycle, Checking Approval SHA or product change.
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; v3 Remaining items seeded (1, of which 0 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-07-20 - D-APP-70 Option A mapped the CQ-F1 working-root content route to DEL-07-03 as physical route-contract owner while retaining DEL-07-01 containment and DEL-02-03 consumption; the CQ-F1 Remaining entry was closed; no source, lifecycle, Approval SHA, SOW, or dependency change.
- 2026-07-18 - D-APP-65 disposition 4 unlocked the R4-P48 documentation-production deferral; the route-adapter test index and SSE compatibility fixture README were produced in the deliverable folder. Content is agent findings; no acceptance or issuance is rendered. The CQ-F1 route-affinity item remains open for the next concordance pass. No state or lifecycle change.
- 2026-07-12 - R6 backcheck corrected the omitted UPD-045/P30 authority half: the three live routes are now cataloged in SPEC §17.1 through the D-APP-56 P06/D-APP-38 corpus procedure; the landed Remaining item was removed. State remains IN_PROGRESS.
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P44 docs applied UPD-099 pointer-only repair; P48 residual unchanged; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 R5 P45 applied UPD-116; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
