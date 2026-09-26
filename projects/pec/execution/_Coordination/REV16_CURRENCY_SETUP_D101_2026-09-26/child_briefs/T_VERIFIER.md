# Child brief T_VERIFIER — independent verifier of the D-PEC-101 act (fresh read-only TASK)

Parent: WORKING_ITEMS (Type 1), brief K14A (`AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K14A_D101_ACT.md`,
SHA-256 `b253797178dfb4b117491d5d056120a23e2b2538485fa83119c5e4851961d2ec`). Role: TASK (Type 2), fresh
context, authored nothing in this act. You do not delegate and you do not repair. Model:
`claude-opus-5-5`, high reasoning. Method: `chirality-root:bundled:skill:software-code-review`
(`.agents/skills/software-code-review/SKILL.md`, expected `ee085d589c44f912d11a59eead8edac214f0343761d26b0d33e886a979888bca`),
adapted to governed metadata. Read root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`
and that skill; record their hashes.

## Candidate

- Worktree `{W}` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act`, branch
  `claude/pec-d101-act`, candidate commit given in your prompt. Base: merge-base with `origin/main`
  (`f392294b573dcc0b17fff8cd9b5a8c2cf4dd252d`, PR #969, which carries the ruling).
- Run root `{RR}` = `projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/`:
  generator copies, reports, `checks/` (see `checks/COMMANDS.txt`), `closure/`, `closure_pre/`,
  helper scripts `check_hashes.py`, `check_k4_extras.py`, `containment.py`, `run_holds.sh`,
  child brief/return records.

## Specification

The ruled proposal `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md`
(`7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25`) and ruling
`D-PEC-101_RULING_2026-09-26.md` (`baa4fc09525aaef89cdb519b934b00c90e699a2111a5c604f906fc5ed2edba28`).
Apply the proposal's section "Independent verifier" items 1-5 in full (Basis; Reproduction; the
fixed checks = the whole "Finite verification" table; Semantics; Containment). Selected: K1, K4 with
add-on C (`--covers`), add-on V (V has NOT run yet; at this candidate no `_Evaluation/**` path may
have changed). The act ran K1 first (TASK, `TASK+preparation`, act date 2026-09-26), then K4 `--covers`
(manager).

Manager method choices you should assess, not assume:
- The postimage verifiers were run on two `git archive` exports: pre = `f392294b5` `projects/pec`;
  post = the act commit `projects/pec` excluding the run root and the K14A brief copy (so the
  verifiers' whole-tree containment sees product paths only; the run root and brief are covered by
  `containment.py`). The proposal describes the K4 verifier's before-state as an export of
  `aca930622`; the manager used `f392294b5` (all 161 targets and basis files identical there; say
  whether that matters).
- The `rely-for-production` preflight ran after the K1 and K4 fan-in commits (disclosed).

## Reproduction (item 2)

Today is the act's local date if `date +%F` prints 2026-09-26: then rerun each generator from its
run-root copy on a fresh `git archive` export of `aca930622ba167689881416044ba0feaee3ef003` (export at
least `projects/pec` and `tools`; add what the generators need), K1 first with
`--act-date 2026-09-26` (no `--reproduction`), then K4 with `--covers`, and compare every one of the 161
product files and both reports byte for byte with the candidate. If the date has changed, use K1's
`--reproduction --act-date 2026-09-26` and say so. Write only under a scratch directory
`/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d101act/verifier/`
and delete your exports there when done (disk is limited). Never write in `{W}` or any checkout;
no git write operations.

## Verdict

Return a verdict document (the manager saves it verbatim as `{RR}/VERIFIER_VERDICT_NN.md`), with:
header (verifier, candidate commit, date/time, instruction hashes); verdict `PASS`, `PASS WITH NOTES`
or `FAIL`; a separate explicit line stating whether **K1 passes** (HELP_HUMAN's Notes (a) edit waits on
it); per-item results 1-5 with the commands you ran, exit codes and key outputs; the reproduction
method used; numbered findings, each marked BLOCKING or NON-BLOCKING with the exact path/line and
the repair you would expect. Do not soften or omit a defect.
