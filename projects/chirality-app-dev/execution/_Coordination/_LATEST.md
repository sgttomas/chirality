# Latest Coordination Pointer

This pointer is for discovery only. It is not substitute authority.

Active coordination surfaces:

- `execution/_Coordination/_COORDINATION.md`
- `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- `execution/_Coordination/_DECISIONS/_REGISTER.md` (D-APP-18..D-APP-43 RULED; D-APP-19 ruled Option D custom — deliverable-inspection phase, issuance deferred; D-APP-38 ruled Option D — hybrid reference-integrity model; D-APP-39 released the autonomous development queue; D-APP-40/41/42/43 unblocked ADQ-05/08/10/11 follow-through; ADQ-05 consumed D-APP-40; ADQ-08 consumed D-APP-41; ADQ-09 completed the DEL-05-04 transcript/replay follow-through; ADQ-10 completed the DEL-05-05 D-APP-42 metadata/checksum/retention follow-through; ADQ-11 completed the PKG-06 permission/tool D-APP-43 closure follow-through; ADQ-12 completed the PKG-08 agent/subagent residuals).

Active development queue:

- **Active but exhausted: `plans/PLAN_2026-06-20_autonomous_development_queue.md`** (D-APP-39 — autonomous pull-and-execute on everything except the four hard fences, with autonomous commit+push; backlog source `plans/artifacts/insp05_development_roadmap_2026-06-21.md`). The agent pulls the highest-priority eligible item, executes/validates/commits/pushes, and stops only at a hard fence, a new decision, a validation failure, or an empty eligible queue. The **P0 governance cluster** was applied 2026-06-20 (commit `a5ccfc591`): D-APP-37 PKG-10 status-truth repair, D-APP-34/36 issue-readiness profiles (`docs/ISSUE_READINESS_PROFILES.md`), and the D-APP-38 reference-integrity model (authority-doc corpus `v1` reconciled via `execution/_Reconciliation/References/reconcile_authority_corpus.py`; 0 `HASH_MISMATCH`). ADQ-05 later bumped the authority corpus to `v2` after D-APP-40 PRD/SPEC/TYPES edits and reconciled 153 deliverable reference rows. ADQ-05, ADQ-08, ADQ-09, ADQ-10, ADQ-11, and ADQ-12 are done; all rows in the autonomous queue are now `DONE`, and no eligible `READY` item remains.
- Completed queue: `plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` (D-APP-19 Option D).
  Deliverable-INSPECTION phase: move all 53 deliverables `IN_PROGRESS -> CHECKING` and inspect each
  to form development evidence; issuance (`CHECKING -> ISSUED`) deferred. Tranche spine INSP-00 ->
  INSP-00b (both landed 2026-06-20) -> INSP-01a -> INSP-01 -> INSP-02 -> INSP-03 -> INSP-04 ->
  INSP-05 -> INSP-FINAL. `INSP-01a` executed 2026-06-20, found a status-history preservation
  blocker (`plans/artifacts/insp01a_status_preflight_2026-06-20.md`), and reran clean under the
  D-APP-33 semantic-history acceptance ruling
  (`plans/artifacts/insp01a_rerun_after_dapp33_2026-06-20.md`). `INSP-01` landed 2026-06-20 with
  owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`; all 53 deliverables are now
  `CHECKING`, 0 `IN_PROGRESS`, 0 `ISSUED`. Evidence:
  `plans/artifacts/insp01_owner_approval_sha_2026-06-20.md` and
  `plans/artifacts/insp01_status_transition_evidence_2026-06-20.md`. `INSP-02` landed 2026-06-20
  and aligned PKG-00 control-plane documents with accepted acyclic DepClosure snapshot
	  `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z`; evidence:
	  `plans/artifacts/insp02_control_plane_truth_fix_2026-06-20.md`. `INSP-03` waves 001-011 are
	  recorded: PKG-00 control-plane assessments DEL-00-01 and DEL-00-02, PKG-01 governance/reliance
	  assessments DEL-01-01 through DEL-01-04, PKG-02 baseline UI assessments DEL-02-01 through
	  DEL-02-05, PKG-03 runtime engine assessments DEL-03-01 through DEL-03-04, PKG-04 SDK adapter
	  / prompt / provider / settings assessments DEL-04-01 through DEL-04-05, PKG-05 session audit
	  / replay / tool-result assessments DEL-05-01 through DEL-05-05, and PKG-06 permissioned tools /
	  MCP / hooks assessments DEL-06-01 through DEL-06-06, and PKG-07 filesystem execution / lifecycle /
	  dependencies assessments DEL-07-01 through DEL-07-06, and PKG-08 agent suite / pipeline dispatch /
	  subagent governance assessments DEL-08-01 through DEL-08-05, and PKG-09 validation / packaging /
	  security / release assessments DEL-09-01 through DEL-09-06, and PKG-10 domain-engine future-boundary
	  assessments DEL-10-01 through DEL-10-05 are complete (53/53), 0 assessments remain
	  pending, reviewed SHA `0aea715f573cfd7759d7fe3f13ca03285b53ef98` is recorded for wave 011 as
	  inspected source-state evidence, and the coverage index is
	  `plans/artifacts/insp03_assessment_index_2026-06-20.md`. `INSP-04` gate-process evaluation is
	  complete at `plans/artifacts/insp04_gate_process_evaluation_2026-06-21.md`; D-APP-34 is now ruled
	  Option B for the post-INSP-03 issuance-gate model. `INSP-05` roadmap synthesis is
	  complete at `plans/artifacts/insp05_development_roadmap_2026-06-21.md`; D-APP-35 through
	  D-APP-37 were prepared and are now ruled. `INSP-FINAL` closeout is recorded at
	  `plans/artifacts/insp_final_closeout_2026-06-21.md`. D-APP-34 through D-APP-39 are ruled. The
	  inspection program is complete; the active queue is now the autonomous development queue (above),
	  whose backlog is sourced from the INSP-05 roadmap.

Completed / superseded queues (history, non-governing):

- `plans/PLAN_2026-06-19_loop_first_pivot.md` (D-APP-28 full loop-first pivot; 28a-28e LANDED).
- `plans/PLAN_2026-06-18_deliverable_issuance_and_evidence_consolidation.md` (issuance program;
  materials transposed into the inspection plan; issuance spine retained as eventual follow-on).
- `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` (active design: Agent-Orchestration UI &
  Information Architecture redesign; Phases 1-5 COMPLETE).

Closed validation-loop follow-up:

- `plans/PLAN_2026-06-19_validation_server_build_isolation.md` (CLOSED — sequencing rule codified
  in `docs/BUILD_AND_RELEASE.md` §4 and `docs/VALIDATION_STRATEGY.md` §3: stop the local dev
  server before build/package/premerge unless the command owns server lifecycle).

Completed planning and history surfaces:

- `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md` (Live Packaged
  `agentSdk` Read-Tool Proof plan; D-APP-17 `sonnet` proof passed; closed history).
- `plans/artifacts/lp02_live_packaged_agentsdk_read_tool_procedure.md` (LP-03 command,
  package path, key supply, artifact directory, stop conditions, and redaction checks).
- `plans/artifacts/lp03_live_packaged_agentsdk_read_tool_evidence_2026-06-18.md`
  (LP-03 failed-proof evidence and redaction disposition).
- `plans/artifacts/dapp17_live_packaged_agentsdk_read_tool_success_2026-06-18.md`
  (successful app-directory packaged live read-tool proof evidence).
- `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` (R6 Extensibility & MCP Boundary Maturity program, R6-01..R6-05; accepted by `execution/_Coordination/_DECISIONS/D-APP-14_RULING_2026-06-17.md`, closed by R6-05; R6-04 deferred as optional organization work).
- `plans/PLAN_2026-06-16_runtime_stabilization.md` (Runtime Stabilization program, STAB-00..STAB-06; accepted by `execution/_Coordination/_DECISIONS/D-APP-11_RULING_2026-06-16.md`, closed by STAB-06).
- `plans/PLAN_2026-06-16_six_node_scc_resolution.md` (closed; no longer the active queue)
- `plans/PLAN_COMPLETION_LOG.md`

Retired planning/history surfaces:

- `plans/PLAN_2026-06-13_runtime_completion.md` is retired runtime completion history.

Active scope-change surfaces:

- `execution/_ScopeChange/_LATEST.md`

Dependency discovery surfaces:

- `execution/_Reconciliation/DepClosure/_LATEST.md`

Bootstrap prompt:

- `init/init-prompt.md`

Retired surface:

- `execution/_Coordination/NEXT_INSTANCE_STATE.md` is retired. Do not use it as app state, update it, or recreate it.
