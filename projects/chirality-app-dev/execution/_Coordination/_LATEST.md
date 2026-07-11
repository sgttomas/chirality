# Latest Coordination Pointer

This pointer is for discovery only. It is not substitute authority. Per
`_COORDINATION.md` (record-keeping rule 5), it must not accumulate state
history: current status is always re-derived from the decision register, each
plan file's own rows/status, and `../../loop/LOOP_RECEIPTS.md`.

Session entry (current convention, owner direction of record 2026-07-04 —
`loop/LOOP_RECEIPTS.md` Receipt 0):

- `../../loop/LOOP_INIT.md` -> newest `loop/WORKPLAN_*.md` -> `loop/LOOP_RECEIPTS.md`

Active coordination surfaces:

- `execution/_Coordination/_COORDINATION.md`
- `execution/_Coordination/_DECISIONS/_REGISTER.md` — the register's own rows
  (not this pointer) are the owner-gated surface; check it every session for
  rulings and open rows.

Work discovery (owner-adopted 2026-07-10; queue convention retired):

- Deliverable-driven: `execution/PKG-*/1_Working/DEL-*/_STATUS.md`
  `## Remaining` sections are the work surface, selected per the newest
  `loop/WORKPLAN_*.md`. No successor queue plan will be authored. Which rehomed
  lanes are live is the owner's ruling — `D-APP-53` (RULED Option A 2026-07-10,
  `_DECISIONS/D-APP-53_RULING_2026-07-10.md`: the dependency-row reconciliation
  lane, executed the same day — see the packet's §7/§8 notes and the accepted
  DepClosure snapshot; Option C/D lanes were NOT unlocked); honor every
  `(gated: ...)` suffix.

Queue and plan history (non-governing; each plan's own status field and
`plans/PLAN_COMPLETION_LOG.md` govern):

- `plans/PLAN_2026-06-21_inspection_orphan_remediation.md` (CLOSED 2026-07-10)
- `plans/PLAN_2026-06-20_autonomous_development_queue.md` (exhausted/closed)
- `plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` (completed)
- `plans/PLAN_2026-06-19_loop_first_pivot.md`,
  `plans/PLAN_2026-06-19_validation_server_build_isolation.md`,
  `plans/DESIGN_2026-06-18_agent_orchestration_ui.md`,
  `plans/PLAN_2026-06-18_deliverable_issuance_and_evidence_consolidation.md`,
  `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`,
  `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`,
  `plans/PLAN_2026-06-16_runtime_stabilization.md`,
  `plans/PLAN_2026-06-16_six_node_scc_resolution.md`,
  `plans/PLAN_2026-06-13_runtime_completion.md` (completed/closed/retired history)

Cross-project (informational, not app-dev active work):

- `plans/artifacts/bridge_appdev_contribution_for_tier0_2026-06-21.md` — tier-0
  cross-check input (owner directive 2026-06-21); read order: facts first,
  app-dev recommendations last; precedence is the root agent's ruling.

Historical session entry:

- `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` — dated historical map from
  the pre-loop convention; never authority (`loop/LOOP_RECEIPTS.md` Receipt 0).

Active scope-change surfaces:

- `execution/_ScopeChange/_LATEST.md`

Dependency discovery surfaces:

- `execution/_Reconciliation/DepClosure/_LATEST.md`

Bootstrap prompt:

- `init/init-prompt.md` (thin launcher pointing at `loop/LOOP_INIT.md`)

Retired surface:

- `execution/_Coordination/NEXT_INSTANCE_STATE.md` is retired. Do not use it as
  app state, update it, or recreate it.
