# Brief D1P-V — independent verification of the D1 premise packet (TASK, read-only)

Parent: WORKING_ITEMS manager of `briefs/D1P_PREMISE_PROPOSAL.md` (SHA-256 `d1cdf4e3104d38a08e8bef8c3641070d942ec9ad2744bddeb9cadfb482cbc1f1`), undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node D1 (provisional `D-PEC-105`). Role: TASK (Type 2), a fresh reviewer who authored nothing in this packet. Model: `claude-opus-5-5`, high reasoning. You do not delegate and you do not repair: defects go back to the manager.

## Boundary

- **Read-only.** Write nothing in any checkout; never check out a branch; read-only git only (`show`, `log`, `diff`, `grep`, `archive`, `rev-parse`, `merge-base`).
- Scratch: `X=$(mktemp -d /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d1pv.XXXXXX)`; `export TMPDIR=$X`. Create and delete files only inside directories you created with `mktemp -d`. Never delete anything else in the shared scratchpad.
- Run tools only on your own `git archive` export (`git -C REPO archive 6c6cc1b00 | tar -x -C $X/e`), with candidates copied in where needed.

## Inputs

- `REPO` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d1-premise-proposal` (branch `claude/pec-d1-premise-proposal`, PR #997; `origin/main` `6c6cc1b00` plus the prep folder). `PREP` = `REPO/projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-26/`.
- In `PREP`: `DRAFT_D-PEC-105_d1_premise_amendment_proposal.md`, `DRAFTER_BRIEF.md` (the premise rule), `targets.json`, `premise/`, `quotes/`, `claims/`, `candidates/`, the bound `apply_d1p.py` and the check aids, `evidence/`.
- The brief and its `COMMON.md` (read both): `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/acts2/D1P.md` and `…/acts2/COMMON.md` (`51b70e46…b311`).
- Instructions: root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`. Method: `workflows/scope-of-work/WORKFLOW.md` and `resources/checks.md` (for `MODE=VERIFY`), `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`; `workflows/review/` (the owning deliverables' REVIEW method).
- Scope-binding sources: SCA-005 `Propagation_Plan.md` §B4/§B5 and INV rows (see `DRAFTER_BRIEF.md`); SCA-006 `Propagation_Plan.md` §B4/§B5; PRD v2.4; decomposition revision 1.6 (pin `189f205ff`); Root `docs/DIRECTIVE.md` (D-GOV-43), `docs/CONTRACT.md` K-RUNTIME-1; the deliverables' `_REVIEW.md`, `_STATUS.md`, `_run_records/`.

## Verdict

Return a verdict: `PASS`, `PASS WITH NOTES` or `FAIL`, then numbered findings, each with severity **BLOCKING** or **NON-BLOCKING**, evidence (file:line, commit, command output), and the concrete repair you would expect. BLOCKING means the packet should not go to the owner as is: a false statement, a quotation that is not verbatim, a change that is not a premise (or not its minimal consequence) under the rule, a premise made false by SCA-005/SCA-006 that the amendment leaves in place in a named or checked locus, a broken check, a grant or script defect, a lifecycle/acceptance/CHECKING claim or prompt, or a missing item the brief requires. List what you checked and how, the commands and exit codes, and the sources with hashes.
