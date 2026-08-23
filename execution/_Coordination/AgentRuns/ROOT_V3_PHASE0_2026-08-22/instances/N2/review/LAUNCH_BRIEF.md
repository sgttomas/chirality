# Fresh Review Brief — N2 DEL-02-03 M2 Preparation

RunID: `ROOT_V3_PHASE0_2026-08-22`

Review construction: independent bounded ephemeral-generalist Agent 2.

Parent: `HELP_HUMAN`.

Basis: local branch `codex/root-v3-phase0-2026-08-22` at the unchanged authorized
execution basis `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776` (the remote has
advanced, but no sync is authorized and no review conclusion may rely on the
new remote bytes).

## Objective

Freshly review N2's preparation package and control return against the owner
steer, the Root instruction doctrine, the DEL-02-03 SOW, and the repository
manifest validator. This is a review-only run. Do not repair files.

## Read set

- `AGENTS.md`
- `agents/AGENT_HELP_HUMAN.md`
- `execution/_Coordination/LOOP_INIT.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/ORCHESTRATION_PLAN.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N2/LAUNCH_BRIEF.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N2/RETURN.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N2/STATUS.json`
- all files under `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-PREP-001/`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/ScopeOfWork.md`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_STATUS.md`
- the accepted N1 proposal folder and N1 cycle-3 review
- the user steer and attached G0 record in `plans/steers/`
- repository validators needed to reproduce the stated checks

## Review gates

1. Confirm the package is preparation only, with no lifecycle, instruction,
   status, notice-routing, pointer, hold, pin, project, plan, tool, or live
   manifest-corpus mutation.
2. Confirm the draft manifest basis is exactly
   `13201dfe7dc3b97c9aa36f6305cae604b48ef80f` and that `git cat-file -t`
   resolves it as `commit`.
3. Confirm the exact AGENTS delta is referenced only by N1 patch SHA-256
   `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee`,
   with no duplicated patch bytes.
4. Confirm the App and Piping notices are drafts inside the sealed run folder,
   correctly name intended coordination surfaces and loop-owned follow-ons,
   and remain unrouted pending D-GOV-35 ruling/application authority.
5. Confirm the application validator list is complete for the owner steer and
   includes downstream derivative/concordance obligations.
6. Confirm `HANDOFF_STATE.md` says exactly
   `PREPARED — BLOCKED ON D-GOV-35 RULING` and identifies accepted basis,
   derivative state, reruns, blockers, and next owner.
7. Directly invoke `validate_manifest` on the draft path; CI-only validation of
   the live corpus is not sufficient. Reproduce the SOW SHA-256
   `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f`
   and prove `_STATUS.md` untouched.
8. Recompute every package hash in N2 RETURN, verify JSON/YAML parseability,
   path containment, `git diff --check`, and candidate whitespace.
9. Treat upstream `origin/main` drift as a closeout authorization blocker, not
   as an N2 content failure, unless N2 improperly relied on the new bytes.

## Write set

Only:
`execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N2/review/REVIEW.md`

## Return contract

Write a verdict of `PASS — ZERO ACTIONABLE FINDINGS` or
`FAIL — ACTIONABLE FINDINGS`. For every finding give the exact file/evidence,
governing requirement, severity, and bounded repair. Record all reproduced
commands/results and the REVIEW.md SHA-256. Do not commit, push, sync, route,
apply, adopt, or merge.
