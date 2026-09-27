# Brief X1A — D-PEC-106 act: P1 parser fixture suites, with add-on L (WORKING_ITEMS)

- **Parent:** HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node X1 (the act).
- **Role:** WORKING_ITEMS (Type 1). Record the SHA-256 of each method file you load.
- **Models:** `claude-opus-5-5` at high reasoning, for you and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-106_RULING_2026-09-27.md`. The owner's words were: "D-PEC-106: A; confirm FX-PEC-0; confirm thresholds; L; M; defaults".
- **Proposal:** `_DECISIONS/D-PEC-106_x1_parser_fixture_suites_proposal_2026-09-26.md`, SHA-256 `677b59f6b1ae19b911e6e07aecfa4df0f39a380fb3ab806903da87c8fa18d279`. It is your specification. Do not enlarge it. It covers:
  - the exact grant, including the single-run, rerun and exit-code rules;
  - add-on L and add-on M;
  - the generation method;
  - finite verification, including row 1 and the requirement to set `TMPDIR`;
  - the independent verifier, which applies `software-code-review`;
  - the administrative grant, rollback and limits.
- **Preparation evidence:** `projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/`. It contains:
  - `apply_x1p.py` (`452ff66af71b7d3de9814301a8e45ca070137d5e577b4e73c202b713d2102428`);
  - the candidates;
  - `run_x1p_checks.sh`, `run_fixture_suite.sh`, the negative controls and the tests;
  - `SHA256SUMS`. Verify it with `shasum -a 256 -c`.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and the register row `D-PEC-106` `RULED …` (PR #1006, merged as `c5d852c4a`).
- Finite-verification row 1 passes:
  - fresh preimage, pin and dependency checks;
  - `apply_x1p.py --check-only` with all pins as tabled;
  - `write_status.sh` hash `0bf835f5…ece3`, recomputed;
  - the three `_STATUS.md` preimages as tabled;
  - `pec_reliance_hold.py` `dispatch-for-production` ALLOW on every target, including add-on L's three `_STATUS.md`. Record it with a `date -u` line.

  Any mismatch or drift in a target or pin stops the act and routes to the owner; no re-pin is authorized. For the classes the grant calls fix-and-rerun, fix them without changing any bound byte.
- Use a full, non-shallow clone without a partial-clone filter, and a Git that honours `GIT_NO_LAZY_FETCH` (2.44 or later). Record the Git and Python versions.
- Work in an isolated worktree on branch `claude/pec-d106-x1-fixtures-act`, cut from fresh `origin/main`. Export `TMPDIR` to a scratch directory outside the repository in every shell.
- **Parallel work.** The `D-PEC-104` act (S1: twelve other deliverables' `ScopeOfWork.md`) and the `D-PEC-105` act (D1: DEL-00-01 and DEL-00-03 files) may run at the same time. Neither is an X1 target or pin.
  - If `origin/main` moves before your PR merges: re-fetch, merge without a rebase, and rerun row 1's pin checks, `run_x1p_checks.sh` and the fixture suite.
  - If a pinned file changed, stop and report.

## Act

1. **Run root.** Create `projects/pec/execution/_Coordination/X1_FIXTURES_{D}/`, where `{D}` is the act date. Copy in the bound files and check their hashes.
2. **Add-on L, at actual production start.**
   - Once row 1 has passed, run the proposal's three `write_status.sh … IN_PROGRESS "…X1_FIXTURES_{D}/"` commands from the repository root, with `{D}` equal to the act date.
   - Check each postimage against the proposal's slot rule. No other byte may change.
   - Commit the three `_STATUS.md` changes on the act branch **before** running the act script.
3. **A.** Run `apply_x1p.py --check-only`, then run it once for real from the repository root, under the grant's rules.
   - Exit 0 consumes the grant.
   - A rolled-back exit 1, or a preflight refusal, does not consume it. Record it, and rerun only as the grant allows, reusing this run root and `{D}`.
   - Exit 2 with `FAIL …; ROLLBACK INCOMPLETE` consumes the grant and stops for the owner.
4. **Verify.** Run the proposal's finite verification. Save each command, its exit code and its output. It includes:
   - containment: exactly the 34 creates, the one modify, and add-on L's three `_STATUS.md`;
   - all six affected registered checks at exit 0, including `v2-parsers` (10 tests);
   - bindings 442/442 and pins 19/19;
   - strict registers, harness and receipts identical before and after;
   - hygiene;
   - `git diff --check`, which must be clean.
5. **Verifier.** Dispatch one fresh read-only `pec-reviewer` (opus) for the proposal's independent verification. It applies `software-code-review` and checks:
   - the add-on L postimages;
   - the ordering: L committed before the act;
   - no parser code, and no scanning for retired sections.

   Save `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you. Run it in the foreground, or wait for it inside your turn; do not end your turn to wait.
6. **Add-on M.** Written at the undertaking's closeout (node M1), not now. Do not create or edit any `MEMORY.md`.
7. **Records.** Write `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` and a run-root `SHA256SUMS`.

## Write boundary

You may write only:
- the 34 new files and `software-workflow.json`, through `apply_x1p.py`;
- the three `_STATUS.md` of DEL-02-03, DEL-02-08 and DEL-02-09, through add-on L's `write_status.sh` commands only;
- the run root;
- this brief, copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/X1A_D106_FIXTURES_ACT.md`;
- your return, at `…/returns/X1A_D106_FIXTURES_ACT.md`.

Write nothing else. That excludes:
- parser code and `v2/src/**`;
- `MEMORY.md`, `ScopeOfWork.md`, registers, `Dependencies.csv`, `_DEPENDENCIES.md`, `_CONTEXT.md` and `_REFERENCES.md`;
- the decomposition, the PRD, `docs/**`, `README.md` and `_DECISIONS/**`;
- the work graph;
- any other deliverable or foreign path.

HELP_HUMAN adds the graph and STATUS records, including the lifecycle census, to your PR. Commit work in progress and push early. Commit your return before you hand back.

## Publication

- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Open a PR against `main`, and do not merge it.
- If CI reports "Update the PR base", merge `origin/main` without a rebase, rerun the affected checks and push.

## Return

- PR URL and head SHA;
- the act report and the add-on L result;
- written paths with their hashes;
- check results;
- verifier verdicts;
- containment;
- anything unresolved.

## Limits

- No lifecycle change other than add-on L's three `INITIALIZED → IN_PROGRESS`.
- No dependency `SatisfactionStatus` written.
- No `CON` resolved.
- No CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or reliance claim. Do not ask the owner about CHECKING.
