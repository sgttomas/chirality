# Brief K2A — D-PEC-103 act: first Scope of Work contracts for DEL-08-06 and DEL-10-13, with add-ons C8 and S (WORKING_ITEMS)

- **Parent:** HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node K2 (the act).
- **Role:** WORKING_ITEMS (Type 1), with `Workflow: chirality-root:bundled:workflow:scope-of-work` (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`). Record the SHA-256 of the method files you load.
- **Model steer:** `claude-opus-5-5` at high reasoning, for you, the status TASK and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-103_RULING_2026-09-26.md`. The owner's words: "D-PEC-103: A; S; M; C8; defaults".
- **Proposal:** `_DECISIONS/D-PEC-103_first_sows_del_08_06_10_13_proposal_2026-09-26.md`, SHA-256 `cfc2e65d5ae91f0d62d4ef993bc22a91d2bb4716969d083ae98f0fc948eb5417`.
  - It is your specification: exact grant, add-ons S, M and C8, generation method, finite verification, administrative grant, rollback and limits. Do not enlarge it.
  - The ruling fixes the order: A → C8 → verifier → S, one step after another, never concurrently.
- **Preparation evidence:** `projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/`.
  - `apply_k2.py` `b10461fa…257a` and `apply_k2_c8.py` `093130c8…84e9`; the full hashes are in `SHA256SUMS`, and you verify them all with `shasum -a 256 -c`.
  - Candidates DEL-08-06 `aecc513161c1e8a5a984dc2f7878b79783170adc1042fb91e816dc649ef50826` and DEL-10-13 `c7743ee2ab7d795577d08c57d748fa704d3cc58ad55df7eea77bc95fb1b56633`.
  - C8's postimage `609aa807710feef11bf8506324cb2a79996f3d6ce5a6eb623ec9516e3ac65693`.
  - The quote and state-claim verifiers, `run_k2_checks.sh`, and the tests.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and register row `D-PEC-103` `RULED A + S + M + C8` (PR #989, merged as `d385b6a19`).
- `apply_k2.py --check-only` passes, with every pin as tabled. On any pin mismatch, stop and return: no re-pin is authorized.
- `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) gives ALLOW on each target: `dispatch-for-production` before dispatch, and `rely-for-production` before fan-in.
- The act runs in an isolated worktree on branch `claude/pec-d103-first-sows-act`, cut from fresh `origin/main`. On any failure, discard and return. Do not repair outside the proposal.
- **Parallel work:** the S4 and S1 packet preparations run at the same time. They write only under their own prep folders on their own branches, and they touch neither DEL-08-06 nor DEL-10-13. If `origin/main` moves before your PR merges, re-fetch it and rerun the quote and state-claim verifiers on the updated base. If a pinned file or quoted locus changed, stop and report.

## Act

1. **Run root:** `projects/pec/execution/_Coordination/SOW_INIT_K2_{D}/` (`{D}` = the act date, 2026-09-26 if it runs today).
   - Copy in `apply_k2.py`, `apply_k2_c8.py`, `candidates/`, `addons/`, `quotes/`, `claims/` and the check aids, and check their hashes.
   - `apply_k2.py` inventories every file under `projects/pec` except its own directory. Output written beside it in the run root is therefore admitted. Capture any other output outside `projects/pec`, for example in your session scratchpad, and copy it in after the script exits.
2. **A:** run `apply_k2.py --check-only`, then run it once for real from the repository root.
3. **C8:** run `apply_k2_c8.py --check-only`, then run it once. Its write set must be exactly DEL-10-13 `_DEPENDENCIES.md`, and the file must equal the tabled postimage. The number is final (`D-PEC-103`), so nothing is rebuilt.
4. **Verify.** Run the proposal's "Finite verification" table. Save each command, its exit code and its output. Required results:
   - validator `PASS format=SOW_V1` ×2;
   - checklists of 17 and 19 items, equal to the prepared `2227dbeb…9641` and `8e07ff3e…ba30` and byte-identical on rerun;
   - boundary owners;
   - quotes `RESULT PASS 137/137`;
   - state claims `RESULT PASS 482/482`;
   - cited IDs and old S2 text;
   - no `_STATUS.md` change yet;
   - strict registers **identical before A, after A and after C8** (at the current basis: exit 1, 0 errors, 26 `XRG-013`, D-GOV-48 deferred);
   - harness self-check, `validate_pec_loop_receipts.py` and `analyze_dep_closure.py` identical at the same three points;
   - containment;
   - `git diff --check`.
5. **Verifier.** Dispatch one fresh read-only `pec-reviewer` (opus) for the proposal's `MODE=VERIFY` independent verification of both contracts as written, and of C8's one-line change. Save `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you. Run the verifier in the foreground, or **wait for it inside your turn**; do not end your turn to wait.
6. **Add-on S.** Only after the verifier passes and each validator prints `PASS format=SOW_V1`, dispatch one separate generic-shell TASK (`pec-task`, opus, no workflow selected).
   - Its only write targets are the two `_STATUS.md` paths.
   - It runs the proposal's two `write_status.sh … INITIALIZED "TASK+status-advance"` commands from the repository root.
   - Check the postimages against the proposal's table at `{D}` = 2026-09-26, or against its slot rule on another date. Save the TASK's return in the run root.
   - `write_status.sh` was `0bf835f5…` at preparation and at HELP_HUMAN's review. Record its current hash. If the postimages differ from the table, explain the difference by the slot rule or stop.
7. **Add-on M** is written at the undertaking's closeout (node M1), not now. Do not create the `MEMORY.md` files.
8. Write `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the run root.

## Write boundary

You may write only:
- the two `ScopeOfWork.md` targets, through `apply_k2.py`;
- DEL-10-13 `_DEPENDENCIES.md`, through `apply_k2_c8.py`;
- the two `_STATUS.md` files, through the S TASK only;
- the run root;
- this brief, copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2A_D103_SOW_ACT.md`;
- your return, at `…/returns/K2A_D103_SOW_ACT.md`.

Nothing else. That rules out `MEMORY.md`, registers, `Dependencies.csv`, other `_DEPENDENCIES.md` bytes, `_CONTEXT.md`, `_REFERENCES.md`, the decomposition, `v2/**`, the PRD, `_DomainEngines/**`, `docs/**`, `README.md`, `_DECISIONS/**`, the work graph and any foreign path. HELP_HUMAN adds the graph and STATUS records to your PR.

Commit work in progress and push early, because host-forced handbacks happen. Commit your return before you hand back.

## Publication

- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Open a PR against `main`, and do not merge it.
- If CI reports "Update the PR base", merge `origin/main` into your branch (no rebase or force-push), rerun the affected checks and push.

## Return

- PR URL and head SHA;
- the act report;
- written paths with their hashes;
- check results;
- verifier verdicts;
- the S TASK's result;
- containment;
- anything unresolved.

## Limits

- No lifecycle change other than add-on S's single `OPEN → INITIALIZED` per deliverable.
- No `CON` item resolved, other than the C-08 classification C8 records. No dependency amend.
- No tool declared, registered or invoked, and no tier-0 profile act (K3 is its own act).
- No CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or reliance claim. Do not ask the owner about CHECKING.
