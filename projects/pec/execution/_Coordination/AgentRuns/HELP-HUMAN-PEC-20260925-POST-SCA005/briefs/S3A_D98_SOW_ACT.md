# Brief S3A — D-PEC-98 act: first Scope of Work contracts for DEL-02-08 and DEL-02-09, re-pinned to revision 1.6 (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S3 (the act). Role: WORKING_ITEMS (Type 1), with `Workflow: chirality-root:bundled:workflow:scope-of-work` (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`). Record the SHA-256 of the method files you load. Model steer: `claude-opus-5-5`, high reasoning, for you, the status TASK and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling.** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-98_RULING_2026-09-26.md`. The owner's words: "D-PEC-98: A; S; M; re-pin yes; CON-005 open; defaults".
- **Proposal.** `_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md`, revision 2, SHA-256 `92b6f1a223f5cb6fffc399f16e5e4e63cf5d8aa8f391981d3afcb9f4027a3e40`. It is your specification, including question 4 (the re-pin procedure), add-on S, add-on M, finite verification, independent verifier, rollback and limits. Do not enlarge it.
- **Preparation evidence** `projects/pec/execution/_Coordination/PEC_FIRST_SOWS_D98_PREP_2026-09-26/`: `apply_d98.py` `19c2ecb6bd40082c2397956dee2e0efb48b7a2aef5ec56e7498d4ed5e2fc419e`; candidates DEL-02-08 `03cce13f484a9b595b5162bd662af42bcd67aae37a8843304bf03cfbb3badc0a`, DEL-02-09 `aafb54fd6457f09da8304ead444686703d5f8d2c28f4c94ec4eab4d2737b188b`; the check aids (`verify_d98_quotes.py`, `verify_d98_state_claims.py`, `test_apply_d98.py`, `run_d98_checks.sh`).
- **The acceptance commit** (the re-pin target): `189f205ff02df4111b33c20be441ce06e65ada7a`, the `origin/main` merge commit of PR #954, which carries the SCA-006 group-3 record and A6. At it, `SOFTWARE_DECOMP.md` is `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`, `Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`, `ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`, `docs/PRD.md` `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`. Verify these yourself.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and register row `D-PEC-98` `RULED A + S + M` (PR #954).
- `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) ALLOW on each target with `dispatch-for-production`, and `rely-for-production` before fan-in.
- Isolated worktree on branch `claude/pec-d98-first-sows-act`, cut from fresh `origin/main`. On any failure, discard and return. Do not repair outside the proposal.

- **Parallel act.** The `D-PEC-99` Remaining retirement act (brief RR3) runs at the same time. It changes `projects/pec/AGENTS.md` and 57 other deliverables' `_STATUS.md`, not DEL-02-08/09. If it merges before your PR, re-fetch `origin/main` and rerun `verify_d98_quotes.py` and `verify_d98_state_claims.py` on the updated base; if a quoted locus changed, stop and report.

## Act

1. **Re-pin (question 4).** In the run root `projects/pec/execution/_Coordination/SOW_INIT_D98_{D}/`, copy the candidates, `apply_d98.py` and the check aids, and check their hashes. Then, in the copies only:
   - in each candidate, move exactly the three places question 4 names: the front-matter `decomposition_basis` commit → `189f205ff02df4111b33c20be441ce06e65ada7a`; the Purpose paragraph beginning "The accepted basis is …", restated for revision 1.6 (revision, accepting act and date 2026-09-26, pin commit `189f205ff02df4111b33c20be441ce06e65ada7a`, the three register and PRD hashes at `189f205ff02df4111b33c20be441ce06e65ada7a`); and the "**Observation commit.**" clause, which now says the registers and PRD at `53145aaeb` differ from the pin and names the quoted loci re-verified. No other byte moves;
   - rerun `verify_d98_quotes.py` against the current tree. If any check fails, the re-pin is void: stop and return, and the packet goes back to the owner;
   - generate the re-bound `apply_d98.py` by changing only `TARGETS` (the two new candidate hashes) and the four `PINNED` entries for `SOFTWARE_DECOMP.md`, `Deliverables.csv`, `ScopeLedger.csv` and `docs/PRD.md` (their hashes at `189f205ff02df4111b33c20be441ce06e65ada7a`). The four deliverable-file pins stay;
   - add `189f205ff02df4111b33c20be441ce06e65ada7a` as a second `PIN` in `verify_d98_state_claims.py`, keeping every existing check; rerun it;
   - record the new hashes and a word diff (old candidate → new candidate, old script → new script) in the run root as `REPIN.md`.
2. **Write.** Run the re-bound script `--check-only`, then once for real, from the repository root. `apply_d98.py` requires the change under `projects/pec` to be exactly the two targets, and the run root is under `projects/pec`: **capture its output outside `projects/pec`** (for example in your session scratchpad) and copy it into the run root after the script exits (review 02 note N2). Commit the run-root files only after the script has exited.
3. **Verify.** Run the proposal's "Finite verification" table and save each command, exit code and output: validator `PASS format=SOW_V1` ×2; checklists (21 and 17 items, bound to the new postimage hashes; they will differ from the prepared checklist hashes only through the re-pin, which you record); boundary owners with the QA 21 hand resolution; quotes; state claims; lifecycle preserved (no `_STATUS.md` change yet); strict registers **identical before and after** (exit 1, 0 errors, 28 warnings at current `origin/main`, D-GOV-48); harness self-check and `validate_pec_loop_receipts.py` identical before and after; containment; `git diff --check`.
4. **Verifier.** Dispatch one fresh read-only `pec-reviewer` (opus) for the proposal's `MODE=VERIFY` independent verification, plus the ruling's re-pin checks: the word diff touches only the three places; `TARGETS` and `PINNED` equal recomputed hashes; the state-claims check passes at both pins. Save `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you.
5. **Add-on S.** Only after the verifier passes the act and each validator prints `PASS format=SOW_V1`: dispatch one separate generic-shell TASK (`pec-task`, opus, no workflow selected) whose only write targets are the two `_STATUS.md` paths, to run the proposal's two `write_status.sh … INITIALIZED "TASK+status-advance"` commands from the repository root. Check the postimages against the proposal's table (at `{D}` = 2026-09-26) or its slot rule, and save the TASK's return in the run root.
6. **Add-on M** is written at the undertaking's closeout (node M1), not now. Do not create the `MEMORY.md` files.
7. Write `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the run root.

## Write boundary

You may write only: the two `ScopeOfWork.md` targets (via the script); the two `_STATUS.md` files (via the S TASK only); the run root; this brief copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S3A_D98_SOW_ACT.md`; your return at `…/returns/S3A_D98_SOW_ACT.md`. Nothing else: no `MEMORY.md`, register, dependency, `_CONTEXT.md`, `_REFERENCES.md`, decomposition, `v2/**`, PRD, `docs/**`, `README.md`, `_DECISIONS/**`, work graph or foreign path.

Commit work in progress and push early. Commit your return before you hand back.

## Publication

Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Open a PR against `main`; do not merge. If CI reports "Update the PR base", report it; do not repair it.

## Return

PR URL and head SHA; `REPIN.md` summary with new hashes; act report; written paths with hashes; check results; verifier verdicts; the S TASK result; containment; anything unresolved.

## Limits

No lifecycle change other than add-on S's single `OPEN → INITIALIZED` per deliverable; no `CON` item resolved (CON-005 stays open); no registry act; no CHECKING, ISSUED, REVIEW gate or acceptance. Do not ask the owner about CHECKING.
