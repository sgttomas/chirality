# Status: DEL-02-02

**Current State:** IN_PROGRESS
**P06 Record:** 2026-07-12 — D-APP-56 R4-P06 authority/kit transcription applied; state remains IN_PROGRESS; generic concordance Remaining stays open for R6.
**Last Updated:** 2026-09-05
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

The Work/Agents projections (PR #323 merge `403f228f4`), the Workbench and
Pipeline re-host, the Artifacts fold into a Workbench Documents block, and the
coordination/activity presentation are implemented and evidenced, with the
semantic-owner boundaries independently re-proven (2026-07-24 redesign tranche;
see `_run_records/R6_WOVEN_REDESIGN_2026-07-24.md` and
`execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/`). The
owner accepted the current "All sessions (N)" presentation as final under
D-APP-96; no presentation residual remains.

Mandatory non-blocking rerun trigger: if a later accepted D-APP-88
distinct-helper implementation lands, rerun the D-APP-86 packaged parity
instrument against that changed package identity.

- **DEL-02-02-V3-01** (`NOT_SELECTABLE_UNTIL: DEL-08-05-V3-01 landed (recorded managed/native descendant records exist to present)`) — Work/Agents presentation of managed and native descendant records with source, authority-class, responsible-reference, currency, and evidence provenance labels from recorded evidence.
  Trace: OUT-001 (Work/Agents coordination presentation; provenance labels; stale/empty-state tests), AC-001, VER-001; applied decomposition row L294 (present explicitly recorded agent/session selections with source, authority class, responsible reference, currency, and evidence; DEL-08-05 retains child records, DEL-05-04 retains projection semantics).
  Plan: WP-07; AT-028 presentation portion; G4 for any Preview-boundary claim; no live-account claim. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: DEL-08-05-V3-01 (the descendant record classes and attribution vocabulary this presentation labels). Row L294 was not amended at Gate 5: the Codex Agent 0/1/2 role-entry offer and the `role not mechanically enforced` / `Opt-in Preview` posture labels are not DEL-02-02 scope and are unseated here (`SCOPE_AMENDMENT_REQUIRED` S-7 in the seating packet MAPPING); they are seated on DEL-02-05 (row L297) and DEL-08-04 (row L357).
  Write locus: `frontend/src/**` presentation components, fixtures, and tests for the Work/Agents/Workbench surfaces plus this deliverable's `_STATUS.md`/`MEMORY.md`/`_run_records/**`; no harness, IPC, or Root write.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Fixture bytes, component tests, and D-APP-36 render evidence proving descendant/status presentation from recorded evidence with provenance labels and no inferred parentage or role; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the presentation lands with review PASS; live wiring is DEL-02-02-V3-02.
- **DEL-02-02-V3-02** (`NOT_SELECTABLE_UNTIL: Root API v2 and event schema v2 acceptance routed to App (Root DEL-02-10) and DEL-08-04-V3-01 landed`) — live descendant/status presentation.
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L294.
  Plan: WP-07; G4 (owner accepts Preview boundary); AT-028 live presentation portion; live success claims wait for G3/G-WIRE. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Root DEL-02-10 accepted API/event schema v2 (routed notice); DEL-08-04-V3-01; DEL-08-05-V3-01; DEL-02-02-V3-01; owner G4 acceptance for any Preview-boundary claim.
  Write locus: `frontend/src/**` presentation surfaces and tests plus deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Live-path presentation evidence bound to the accepted schema identity and to recorded descendant evidence; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: live presentation lands under G4 evidence.

- **DEL-02-02-V3-03** (`SELECTABLE`) — retire Workbench and Pipeline from the woven route and make the primary dialogue invariant (T1).
  Implementation status (2026-09-05): implemented and validated on the run branch in `APP_LOOP_SHELL_2026-09-05` (12-file source freeze, fresh review PASS, focused 29 tests PASS, revised D-APP-36 browser/render PASS). No product residual is known for this T1 slice. Item and its removal condition remain until owner merge; local premerge failed in the documented absent-daemon-bindings class and requires PR CI, not a local PASS claim. See `_run_records/TASK_RUN_2026-09-05_T1_SHELL_RETIREMENT.md`.
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L308 (Workbench and Pipeline retired from the active shell with code, routes, and tests retained; the Work projection unmounted until an explicitly recorded plan/task source exists); SOW-001 L171 (the centre dialogue is never hidden, unmounted, or replaced; retired routes reachable but unmounted); SOW-007 L177 (presentation half retired by owner ruling, DEL-08-03 remains semantic owner); DEC-025 L634.
  Plan: T1; SR-01, SR-06, SR-08; Q3 ruled D-APP-108 (the retired `/workbench` and `/pipeline` routes stay reachable by URL and unlisted; no 404). Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: none (first tranche); DEL-08-03 dispatch semantics are consumed by nothing in the active shell and are not touched; no Root dependency.
  Write locus: `frontend/src/components/woven-dialogue/**` (route, shell, viewport, navigator, replay-lens mount; `work-projection.tsx` unmount with its empty-source disclosure test retained), `frontend/src/__tests__/components/woven-dialogue-*.test.tsx`, D-APP-36 render fixtures; `frontend/src/app/workbench/**` and `frontend/src/app/pipeline/**` untouched (retained routes); deliverable-local `_STATUS.md`/`MEMORY.md`/`_run_records/**`. No harness, IPC, or Root write.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: the woven route renders with no focused-surface mode and no Workbench or Pipeline mount; a test proves the primary dialogue is never hidden, unmounted, or replaced under replay selection, panel resize, and expand; replay opens beside a visible primary; the Work projection is unmounted; `/workbench` and `/pipeline` remain reachable by URL with their existing tests green and no navigation entry; D-APP-36 render evidence and browser evidence; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS and browser evidence recorded; the Workflows view and proposal card are DEL-02-02-V3-04.
- **DEL-02-02-V3-04** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed; DEL-07-03-V3-01 landed`) — Workflows view, roadmap, New workflow form, library and bind, the derived rung with its two forms, the proposal card, and the workflow file read/write route (T3 part).
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L308 (Workflows view, roadmap, New workflow form, library, and bind actions over governed workflow files; the transcript proposal card rendered from `proposal.*` events); SOW-081 L251; SOW-082 L252 (card actions are human acts applied by the app; one proposal per chat per trigger); OI-008 L602.
  Plan: T3 part; SR-23, SR-24, SR-26; Q10 to Q14 ruled 2026-09-04 (SR-24; G2-CONFIRM); Q15 ruled D-APP-108 (a read-only currency line in the Workflows view comparing the file's `roadmapSource` hash against the current protocol or template); Q16 ruled D-APP-108 (position advances only at human gates, the file records who advanced it, concurrent editing documented as unsupported until the thesis §9.4.6 work). `03_TARGET_SPEC.md` (SHA-256 `d1643e3cf8156b7084b370aa8624bd5e87a75bfb4c0cd7b3a2552a4cbef82b45`) §4.3 and §5.10 for meaning. Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: DEL-07-03-V3-01 (the front matter, roadmap grammar, gate markers, and bind copy semantics this view reads and writes); DEL-02-03-V3-01 (the right-panel view switcher hosts the Workflows view, which cannot mount before it); DEL-02-04-V3-01 (chat rung and declined-trigger convenience fields); the card's live `proposal.*` path is DEL-05-02-V3-02 after Root DEL-02-10 acceptance, so this item ships the card over fixtures for the four candidate event types and makes no live-event claim.
  Write locus: `frontend/src/components/woven-dialogue/**` (Workflows view, roadmap, New workflow and bind forms, rung forms, proposal card), a new K-PATH-2-contained read/write route under `frontend/src/app/api/working-root/workflow/**` limited to `.chirality/workflows/`, consumers of the DEL-02-04-owned additive state, fixtures and tests; deliverable-local state. No harness, MCP, instruction-root, or Root write.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched; workflow-file writes prove K-PATH-2 containment and refuse a file with role, folder, or delegation policy unset.
  Return: Workflows view lists, opens, follows, pauses, creates, and binds from the library with provenance (`roadmapSource` and hash) and the Q15 currency line; New workflow refuses role, folder, or delegation policy unset; position advances only at human-gate markers and records who advanced it (Q16); the proposal card renders Accept, Adjust, and Not now as human acts over the four fixture event types with once-per-chat-per-trigger enforcement visible; nothing is promoted silently; the file steers and never records status, approvals, or evidence; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS; live `proposal.*` consumption remains DEL-05-02-V3-02.

## History
- 2026-09-05 - DEL-02-02-V3-03 T1 implemented on the run branch: primary dialogue stays visible and mounted, replay is in interim Session panel, Work/Workbench/Pipeline mounts retired, legacy URLs retained. Initial browser review found narrow metadata wrapping; scoped repair and fresh full review passed, then revised browser proof passed. Remaining item retained pending owner merge; Current State and Checking Approval SHA unchanged. See `_run_records/TASK_RUN_2026-09-05_T1_SHELL_RETIREMENT.md`.
- 2026-09-05 - D-APP-109 (owner direction 2026-09-05): dependency register re-extracted against the applied decomposition row L308 with the held edge proposals emitted as cycle-participating, non-gating rows (run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`); `_CONTEXT.md` Traceability, Anticipated Artifacts, and Source Authority aligned to the applied row. No Remaining, lifecycle, Checking Approval SHA, product, or release change.
- 2026-09-04 - SCA-APP-010 shell-redesign seating (D-APP-108; owner adopted the seating list as presented): Remaining items seeded DEL-02-02-V3-03, DEL-02-02-V3-04 (SELECTABLE: DEL-02-02-V3-03) with gate, dependency, write-locus, check, and return contracts; ruled questions cited by item. `ScopeOfWork.md` re-pinned to the applied decomposition at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` with a SCA-APP-010 Gate-5 Current Contract section; `_CONTEXT.md` and `_REFERENCES.md` aligned (WI-006, WI-007, WI-008, WI-009, WI-010). Display name is now `Right-Panel Coordination, Workflows, and Proposal UX`; existing DEL-02-02-V3-01 and V3-02 are read under the applied row (the Who is working view) without text change. Run evidence `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; v3 Remaining items seeded (2, of which 0 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-08-17 - D-APP-96 accepted the current "All sessions (N)" presentation
  as final: N counts all recorded sessions per Working Root, including
  unattributed ones. The owner-reserved presentation item was removed from
  Remaining; TM-APP-037 is resolved for later TASK_MANAGEMENT maintenance. No
  product bytes, lifecycle state, dependencies, or Checking Approval SHA
  changed.
- 2026-08-03 - D-APP-86 Option A packaged Desktop evidence proved the
  re-hosted Workbench and Pipeline observations on one frozen unsigned/adhoc
  package: Workbench rendered the live 53-deliverable governed boundary,
  Pipeline rendered the DECOMP/PREP/TASK/AUDIT intent, each preserved the
  mounted primary Dialogue, and each returned without observed route or state
  corruption. The packaged Workbench/Pipeline evidence residual was removed;
  the owner-reserved "All sessions (N)" presentation question remains. A later
  accepted D-APP-88 distinct-helper implementation is a mandatory non-blocking
  parity rerun trigger. State remains IN_PROGRESS; lifecycle, dependencies,
  authorization basis, directive, and Checking Approval SHA are unchanged.
  See `_run_records/R8_DAPP86_PACKAGED_WORKBENCH_PIPELINE_2026-08-03.md`.
- 2026-08-02 - Navigator UI compatibility repair added fixed-record-year
  session timestamps and an inverse `Recent sessions` expanded label, with a
  real component state-transition proof from the four-item scoped recent list
  to all eight fixture records (including the unattributed record) and back.
  The owner-reserved total-per-Working-Root versus per-group count question and
  packaged Desktop smoke remain open. State remains IN_PROGRESS; lifecycle,
  dependencies, authorization basis, directive, and Checking Approval SHA are
  unchanged. See `_run_records/R7_UI_COMPAT_NAVIGATOR_2026-08-02.md`.
- 2026-07-24 - Woven Dialogue visual redesign and IA consolidation tranche recorded in `_run_records/R6_WOVEN_REDESIGN_2026-07-24.md`; the four SCA-APP-004 Remaining items were rewritten to their true residuals (recorded-session presentation notes for "All sessions (N)", label inversion and session year, plus packaged Desktop smoke evidence). State remains IN_PROGRESS; accepted historical evidence and Checking Approval SHA are preserved.
- 2026-07-23 - SCA-APP-004 Gate-5 execution-record propagation added the owner-approved Work/Agents projection and contextual Workbench/Pipeline implementation tranche. State remains IN_PROGRESS; accepted historical evidence and Checking Approval SHA are preserved.
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-068; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 R5 P45 applied UPD-107; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
- 2026-07-19 - D-APP-56 R4-P28 PIPELINE lifecycle-transition component-render coverage added and validated at the D-APP-36 bar; the deliverable-local Remaining item was removed. State remains IN_PROGRESS; Checking Approval SHA preserved.
