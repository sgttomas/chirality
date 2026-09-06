# Status: DEL-08-04

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-05
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- Per-attempt subagent decision-replay packet prepared under D-APP-103:
  `execution/_Coordination/_DECISIONS/D-APP-117_PACKET_PER_ATTEMPT_DECISION_REPLAY_2026-09-05.md`.
  Implementation remains (`gated: owner ruling on D-APP-117`); packet is
  PROPOSAL / AWAITING_RULING, with capture/handoff, persistence and consumer
  ownership kept distinct. Packet preparation does not authorize implementation.

- **DEL-08-04-V3-01** (`NOT_SELECTABLE_UNTIL: Root WP-03/WP-05 fixtures (accepted DEL-02-07 supervisor and DEL-02-10 API v2 returns routed to App); G-ROLE/G-APPR/G-SBX/G-SENT/G-PROT/G-ENV/G4 for claims`) — class-aware managed/native delegation bridge for v3.
  Trace: OUT-002, REQ-001 through REQ-005, AC-002, VER-002; CLM-033.
  Plan: WP-06; G-ROLE, G-APPR, G-SBX, G-SENT, G-PROT, G-ENV, G4; AT-026 through AT-031 and AT-045 App portions. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Root DEL-02-07 and DEL-02-10 accepted returns (routed notices); DEP-08-04-009/010/011; the accepted D-GOV-35 class notice; the D-APP-103 packet item below stays separate. The `managed-delegation.ts:480-496` sibling-overlap fail-close remains a required invariant.
  Write locus: `frontend/src/lib/harness/subagent-governance.ts` (class-aware change at lines 205-213 only under the accepted native ruling), `managed-delegation.ts`, related tests/fixtures, and deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Role/native-origin fixtures, sealed-brief, containment, approval, cancellation, and cleanup conformance evidence with `role not mechanically enforced` and `instruction-asserted` labels proved whenever G-ROLE proof is absent; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the class-aware bridge lands with the named gate evidence.

- **DEL-08-04-V3-02** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected`) — per-session delegation policy honoured by the managed delegation bridge, `none` by default (SOW-083).
  Trace: OUT-001, OUT-002, AC-001, AC-002, VER-001, VER-002; applied decomposition row L371 (honour the per-chat delegation policy carried with the session as a narrowing input to managed delegation); SOW-083 L253 (only narrows what SCA-APP-008's carrier text allows; adds no delegation class).
  Plan: T3 and T6 harness part; SR-24. Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: DEL-03-02-V3-01 (the binding; selected together); DEL-08-04-V3-01 where the class-aware paths exist, otherwise the current managed bridge; the `managed-delegation.ts` sibling-overlap fail-close remains a required invariant.
  Write locus: `frontend/src/lib/harness/managed-delegation.ts` and `subagent-governance.ts` (policy check before admission), fixtures, tests; deliverable-local state. No daemon or Root write.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: the bridge applies the session policy: `none` refuses `delegate_agent`; ask-per-brief routes an approval; approve-brief-writes requires write approval; bounded-briefs admits only sealed briefs within declared tools; `none` is proven as the default; no new class; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS.

## History
- 2026-09-05 - Prepared D-APP-117 under D-APP-103 (APP_LOOP_SHELL_2026-09-05 / pkg08_packet). At most three options and recommendation; no implementation, dependency acceptance, lifecycle or Checking Approval SHA change. Packet awaits owner ruling; governing review and closeout evidence remain in the supervising run.
- 2026-09-05 - Remaining marker normalized under D-APP-114 (`SELECTABLE` packet preparation; no scope change).
- 2026-09-05 - D-APP-109 (owner direction 2026-09-05): dependency register re-extracted against the applied decomposition row L371 with the held edge proposals emitted as cycle-participating, non-gating rows (run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`); `_CONTEXT.md` Traceability, Anticipated Artifacts, and Source Authority aligned to the applied row. No Remaining, lifecycle, Checking Approval SHA, product, or release change.
- 2026-09-04 - SCA-APP-010 shell-redesign seating (D-APP-108; owner adopted the seating list as presented): Remaining items seeded DEL-08-04-V3-02 (SELECTABLE: none) with gate, dependency, write-locus, check, and return contracts; ruled questions cited by item. `ScopeOfWork.md` re-pinned to the applied decomposition at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` with a SCA-APP-010 Gate-5 Current Contract section; `_CONTEXT.md` and `_REFERENCES.md` aligned (WI-061, WI-062, WI-063, WI-064, WI-065). Run evidence `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; decomposition-conformant v3 outputs/requirements (OUT-002, REQ-*, AC-002, VER-002) added from the Gate-5 row text only; v3 Remaining items seeded (1, of which 0 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-08-21 - Completed the post-Root cross-surface integration check on
  accepted basis `1b375af4f1219ecfc00fc2755854aa7fd4220901` against the
  unchanged Receipt 172 App harness implementation at
  `ac2cd801a06a0679bc86830c627218ccca78b658`. The live configured Agent 0
  route admits allowlisted canonical `TASK` Agent 2 and explicitly opted-in
  ephemeral generalist Agent 2, while unsupported named Agent 2, unresolved,
  missing-opt-in, noncanonical TASK-class, and Agent-2-parent routes remain
  fail-closed. Root validator 34/0/0, Root tests 19/19, App focused tests
  19/19 and 11/11, and combined App backcheck 30/30 passed. The App loop
  acknowledges the routed TM-ROOT-125 notice as `INCORPORATED` through this
  deliverable record; no Root or product-source write occurred. The unrelated
  D-APP-103 packet item remains. State stays IN_PROGRESS; lifecycle and
  Checking Approval SHA are unchanged.
- 2026-08-21 - Owner rehomed the TM-APP-044 residual to DEL-08-04. The
  App-side harness code and tests already landed at
  `ac2cd801a06a0679bc86830c627218ccca78b658` and were integrated under
  Receipt 172; the only added Remaining work is post-root cross-surface
  validation/integration after the Root-owned `TM-ROOT-125` alignment lands.
  No duplicate App implementation, Root write, lifecycle change, or Checking
  Approval SHA change is authorized.
- 2026-08-17 - D-APP-103 authorized one bounded planning node to prepare the
  per-attempt subagent decision-replay packet with at most three options and a
  recommendation. Implementation remains gated on a later ruling; lifecycle
  and Checking Approval SHA are unchanged.
- 2026-08-16 - Repaired the App harness type rules so an Agent 0 with configured authority may dispatch allowlisted canonical `TASK` Agent 2 children and explicitly opted-in ephemeral generalists while unsupported routes remain fail-closed. Integrated review found that managed launch also needed canonical `AGENT_CLASS: TASK`; the guard and missing/non-TASK rejection tests were added, focused tests passed 30/30, and fresh corrected-diff review returned PASS with zero findings. The coordinated root metadata/validator alignment remains external to this node, and the unrelated D-APP-53-gated decision-replay item remains open. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-22 - D-APP-72 governed optional Agent 2 `EngineSelection` completed through Chirality `delegate_agent`; Pi-native delegation remains prohibited and managed-delegation tests pass. The unrelated D-APP-53-gated decision-replay item remains open. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-21 - SCA-APP-002 added bounded Pi-child engine selection to Remaining; state remains IN_PROGRESS.
- 2026-05-20 - State set to INITIALIZED (TASK + four-documents P1/P2)
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-10 - Remaining section added: open scope rehomed from the D-APP-53 candidate enumeration per owner-adopted consolidation (loop Receipt 5); no state change.
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P45 applied UPD-135, UPD-136, UPD-137; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.

- 2026-07-12 - D-APP-56 R4-P46 reaffirmed the D-APP-53 Option-C-gated per-attempt decision-replay artifact as open and unselectable; no gate was unlocked and no state change occurred.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
- 2026-07-19 - D-APP-68 dispositions 3-4 refreshed managed-delegation admission, parent-relative hierarchy, and DEL-08-05 handoff ownership; the gated decision-replay Remaining item is unchanged; state remains IN_PROGRESS and Checking Approval SHA is preserved.
