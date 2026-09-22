# Status: DEL-06-03

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-22
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- **DEL-06-03-V3-01** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected`) — the `propose` tool: schema, roster and policy validation, plan-reference resolution, once-per-chat enforcement, and `proposal.offered` emission.
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L348 (in-process deterministic `propose` specification-ladder tool; DEL-06-02 retains catalog validation and collision prevention); SOW-082 L252.
  Plan: T3 part; SR-24, SR-26; Q11 and Q12 ruled 2026-09-04 (the specification tuple is folder, agent, delegation policy, roadmap, and permission mode); Q13 ruled 2026-09-04 (`proposal.offered` is an additive harness event type). Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: DEL-02-02-V3-04 (card and rung forms that consume `proposal.offered`); DEL-08-01-V3-01 (clauses naming the triggers); DEL-06-02 catalog validation; roster and policy values read from the instruction root.
  Write locus: `frontend/src/lib/harness/mcp/**` (`mcp__chirality__propose` definition, schema, validation, once-per-chat state), wrapper metadata, in-process extension-boundary notes, tests; deliverable-local state. No remote MCP, plugin, provider, or network change.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); D-APP-127 requires repeating checks whose evidence is invalidated by affected source, configuration or packaging changes.
  Return: a deterministic in-process tool that validates the five-item tuple against roster and policy values, resolves plan references from Agent 1 procedures, refuses a trigger already declined in the chat, and emits only `proposal.offered`; F-APP-1 untouched; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS.

- **DEL-06-03-R5-RESIDUALS** — Complete the remaining claim-level reconciliation and owning implementation/evidence follow-through: 13 authority application, 17 implementation or evidence, 16 record repair. Exact source keys, required work and individual gates: `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R5/RESIDUALS/DEL-06-03.csv` (D-APP-131). Apply existing decisions without asking for them again; preserve specifically reserved owner decisions, unknown off-code results, scope/instruction boundaries and human lifecycle acts. Select a bounded subset from this item, revalidate its current source/evidence, and close only the independently backchecked keys. The CSV is supporting evidence for this Remaining item, not a second work-selection surface.

## History
- 2026-09-22 — D-APP-131 R5/R6: completed the D-APP-128 bootstrap, recorded exact residual keys and applied any named carrier repairs. D-APP-127 affected-check rule replaces obsolete A1 re-stage wording in live Remaining only. Historical results, lifecycle and Checking Approval SHA are unchanged.
- 2026-09-21 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-128 packet; no state change.
- 2026-09-05 - D-APP-109 (owner direction 2026-09-05): dependency register re-extracted against the applied decomposition row L348 with the held edge proposals emitted as cycle-participating, non-gating rows (run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`); `_CONTEXT.md` Traceability, Anticipated Artifacts, and Source Authority aligned to the applied row. No Remaining, lifecycle, Checking Approval SHA, product, or release change.
- 2026-09-04 - SCA-APP-010 shell-redesign seating (D-APP-108; owner adopted the seating list as presented): Remaining items seeded DEL-06-03-V3-01 (SELECTABLE: none) with gate, dependency, write-locus, check, and return contracts; ruled questions cited by item. `ScopeOfWork.md` re-pinned to the applied decomposition at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` with a SCA-APP-010 Gate-5 Current Contract section; `_CONTEXT.md` and `_REFERENCES.md` aligned (WI-036, WI-037, WI-038, WI-039, WI-040). Run evidence `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-07-22 - D-APP-72 neutral tool bridge completed with separate Claude/Pi binders and exactly one governed `read_file` tool for the bounded Pi child; containment, permission, redaction, and evidence tests pass. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-21 - SCA-APP-002 added the bounded neutral read-tool bridge to Remaining; state remains IN_PROGRESS.
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-071; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 R5 P45 applied UPD-128; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
- 2026-07-19 - D-APP-68 item 3 in-process coordination-tool composition ownership recorded; no lifecycle, Approval SHA, or Remaining change; state remains IN_PROGRESS.
