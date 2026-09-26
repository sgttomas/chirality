# Child brief T_K1_ACT — D-PEC-101 Part K1 generator run (TASK, `preparation` actor)

Parent: WORKING_ITEMS (Type 1), brief K14A (`K14A_D101_ACT.md`, SHA-256
`b253797178dfb4b117491d5d056120a23e2b2538485fa83119c5e4851961d2ec`), undertaking
`HELP-HUMAN-PEC-20260925-POST-SCA005`, nodes K1/K4. Role: TASK (Type 2), acting as
the eligible `preparation` actor recorded `TASK+preparation`. You do not delegate.
Model: `claude-opus-5-5`, high reasoning.

## Authority (read, do not edit)

- Ruling `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_RULING_2026-09-26.md`
  (`baa4fc09525aaef89cdb519b934b00c90e699a2111a5c604f906fc5ed2edba28`).
- Proposal `…/_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md`
  (`7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25`), sections
  "Generation method (binding)", "K1 bound options", "K1 slot rule".
- Skill `.agents/skills/preparation/SKILL.md` (expected
  `0662dc88b5c1deff27280480395d355e5b073a3eb5eb9887f1459861ced96d38`): read it and record
  its hash; the generator performs its deliverable-fileset operation through
  `tools/scaffolding/write_status.sh` and `scaffold_deliverable.sh`.
- Read `AGENTS.md`, `projects/pec/AGENTS.md` and `agents/AGENT_TASK.md`; record their hashes.

## Setup facts

- Repository root (worktree): `{W}` =
  `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act`, branch
  `claude/pec-d101-act`. Run root `{RR}` =
  `projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26`.
- Scratch `{S}` =
  `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d101act/k1task`
  (create it).
- The manager has already run the reliance-hold preflight (`dispatch-for-production`,
  164/164 ALLOW, `{RR}/checks/01_preflight_dispatch-for-production.out`) and verified
  161/161 preimages (`{RR}/checks/06_pre_preimages.out`).

## Steps (exactly these; stop at the first failure)

1. Confirm `shasum -a 256 {W}/{RR}/gen_d101_k1.py` is
   `4892c6a3c7fab4ba405b1ca201b7cab423c8c59644dee5f1d675d2e5f692cecb`, `git -C {W} status --short`
   shows only nothing or run-root paths, and `date +%F` prints `2026-09-26`. If any fails, stop.
2. From `{W}` run (pass the literal repository path for `--repo`; it equals
   `git rev-parse --show-toplevel`):
   `PYTHONDONTWRITEBYTECODE=1 python3 {RR}/gen_d101_k1.py --repo {W} --act-date 2026-09-26 --check-only > {S}/gen_d101_k1_checkonly.tsv 2> {S}/gen_d101_k1_checkonly_stderr.txt`
   and record the exit code. Required: exit 0, and `git -C {W} status --short` unchanged
   (check-only writes nothing). Otherwise stop.
3. From `{W}` run the act, once:
   `PYTHONDONTWRITEBYTECODE=1 python3 {RR}/gen_d101_k1.py --repo {W} --act-date 2026-09-26 > {S}/gen_d101_k1_report.tsv 2> {S}/gen_d101_k1_stderr.txt`
   Record the exit code, the local timestamp (`date '+%F %T %Z'`) before and after, and
   `git -C {W} status --short` afterwards. Do not rerun the act for any reason. Default
   actor, no `--reproduction`, no other option.
4. Copy the four `{S}` files byte for byte into `{W}/{RR}/` under the same names, and
   `cmp` each copy with its source.
5. Report: exit codes; line counts by kind (first column) of each report; the `CHECK`
   lines verbatim (for example `active_execution_quotes_verbatim`, fileset); whether
   `{W}/{RR}/gen_d101_k1_report.tsv` is byte-identical to
   `projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/k1/evidence/genK1.tsv`
   (`cmp`; if not, `diff` and describe); the post-act `git status --short` list (expect
   20 modified product paths, two new untracked folders and the four new run-root files).

## Write boundary

Only: the 32 K1 product paths, written solely by the generator (and the tools it
calls); the four report copies in `{RR}/`; files under `{S}`. Nothing else. No `git add`,
commit, push or branch operation (the manager commits). No edits to any product file by
hand, no repair, no second act run. If anything fails, stop and return exactly what
happened; the manager decides.

## Return

A plain report to the manager: the hashes of the instruction files you read, the steps
with commands, exit codes, timestamps, the report summaries and comparisons above, and
anything unexpected.
