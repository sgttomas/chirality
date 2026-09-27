# Brief S1A — D-PEC-104 act: S1 Scope of Work currency, twelve exact replacements (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S1 (the act).

Role: WORKING_ITEMS (Type 1), with `Workflow: chirality-root:bundled:workflow:scope-of-work`. The workflow supplies the authoring discipline (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`) and the independent `MODE=VERIFY`; the ruling is the authority for the replacements. Record the SHA-256 of each method file you load.

Model steer: `claude-opus-5-5` at high reasoning, for you and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-104_RULING_2026-09-27.md`. The owner's words: "D-PEC-104: A; confirm Part B; correction-only; confirm 4; M; defaults."
- **Proposal:** `_DECISIONS/D-PEC-104_s1_sow_currency_proposal_2026-09-26.md`, SHA-256 `35301840d56f9972b0d7ca3c85dae0ee80ffdf5509c44586f219a47ff6545f51`. It is your specification: the exact grant, add-on M, the generation method, the finite verification, the administrative grant, rollback and limits. Do not enlarge it.
- **Preparation evidence:** `projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/`. It holds:
  - `apply_s1p.py` (`26b677a70d5d51041f0d49dd34e9a09685120f136071e906d7ff702719f1625f`; 12 targets, 35 pins including the landed S4 postimages of DEL-04-01 and DEL-04-03);
  - the twelve candidates;
  - the quote and state-claim verifiers, `run_s1p_checks.sh`, the negative controls and the tests;
  - `SHA256SUMS`, which you verify in full with `shasum -a 256 -c`.
- **Precedent act:** the `D-PEC-102` act, PR #998. See its run root `SOW_CURRENCY_S4_2026-09-26/`, its brief `briefs/S4A_D102_SOW_ACT.md` and HELP_HUMAN's reviews `returns/REVIEW_PR998_0*.md`.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and the register row `D-PEC-104` `RULED A …` (PR #1005, merged as `16010b4ca`).
- `apply_s1p.py --check-only` passes, with all 12 preimages and all 35 pins as tabled. On any mismatch, stop and return: no re-pin is authorized.
  - Since `b0a9a52b6`, main has gained the S1 prep folder (PR #986), this ruling (PR #1005) and Piping changes. None is an S1 target or pin; the check confirms it.
- `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) returns ALLOW on each of the 12 targets:
  - `dispatch-for-production` before dispatch;
  - `rely-for-production` before fan-in.

  Record both runs with a timestamp line, such as `date -u` output, so the order is evident.
- Work in an isolated worktree on branch `claude/pec-d104-s1-sow-act`, cut from fresh `origin/main`. On any failure, discard it and return. Do not repair outside the proposal.
- **Parallel work.** The D1 (`D-PEC-105`) and X1 (`D-PEC-106`) acts may run at the same time once ruled. D1 writes DEL-00-01 and DEL-00-03 files; X1 writes `v2/tests/parsers/**`, `software-workflow.json` and, with its add-on L, the `_STATUS.md` of DEL-02-03, DEL-02-08 and DEL-02-09. None is an S1 target or pin.
  - If `origin/main` moves before your PR merges, re-fetch it, merge it without a rebase, and rerun `--check-only` plus the quote and state-claim verifiers.
  - If a pinned file or quoted locus changed, stop and report.

## Act

1. **Run root.** Create `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_{D}/`, where `{D}` is the act date.
   - Copy in `apply_s1p.py`, `candidates/`, `quotes/`, `claims/` and the check aids, and check each hash.
   - Before running, read `apply_s1p.py`'s write-set inventory rule. Decide from it where output may be written during a run: beside the script in its own directory, if the script excludes that directory, or outside `projects/pec` (for example your session scratchpad), copied in after the script exits. Record the decision in `MANIFEST.md`.
2. **A.** Run `apply_s1p.py --check-only`, then run it once for real from the repository root.
3. **Verify.** Run the proposal's "Finite verification" table. Save each command, its exit code and its output. It includes:
   - the validator, `PASS format=SOW_V1` ×12;
   - the checklists: rerun byte-identical and equal to the prepared hashes;
   - the boundary owners;
   - quotes 884/884, state claims 905/905 and qualified IDs 44/44;
   - the S4 overlay (a no-op);
   - dependency-quote currency (127/127, identical);
   - no `_STATUS.md` or `_REVIEW.md` change;
   - strict registers, harness, receipts and closure, each identical before and after (at the current basis: exit 1, 0 errors, 26 `XRG-013`, D-GOV-48 deferred);
   - containment;
   - `git diff --check`.
4. **Verifier.** Dispatch one fresh read-only `pec-reviewer` (opus) for the proposal's `MODE=VERIFY` independent verification of all twelve contracts as written, including:
   - the Part B landings verbatim with gates binding (DEL-03-02, DEL-03-03, DEL-03-06 correction-only, DEL-04-05);
   - DEL-01-03 and DEL-01-05: every REQ, AC and VER line byte-identical to the preimage;
   - DEL-04-05's statements matching the landed S4 text.

   Save `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you. Run it in the foreground, or wait for it inside your turn; do not end your turn to wait.
5. **Add-on M** is written at the undertaking's closeout (node M1), not now. Do not create any `MEMORY.md`.
6. **Records.** Write `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` and a run-root `SHA256SUMS`.

## Write boundary

You may write only:
- the twelve `ScopeOfWork.md` targets, through `apply_s1p.py`;
- the run root;
- this brief, copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1A_D104_SOW_ACT.md`;
- your return, at `…/returns/S1A_D104_SOW_ACT.md`.

Write nothing else. That excludes `_STATUS.md`, `_REVIEW.md`, `MEMORY.md`, registers, `Dependencies.csv`, `_DEPENDENCIES.md`, `_CONTEXT.md`, `_REFERENCES.md`, the decomposition, `v2/**`, the PRD, `_DomainEngines/**`, `docs/**`, `README.md`, `_DECISIONS/**`, the work graph and any other deliverable or foreign path. HELP_HUMAN adds the graph and STATUS records to your PR.

Commit work in progress and push early. Commit your return before you hand back.

## Publication

- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Open a PR against `main`; do not merge it.
- If CI reports "Update the PR base", merge `origin/main` without a rebase, rerun the affected checks and push.
- If an unrelated check fails, rerun it once and report it; do not claim that a rerun repairs anything.

## Return

- The PR URL and head SHA.
- The act report.
- The written paths with hashes.
- The check results.
- The verifier verdicts.
- Containment.
- Anything unresolved.

## Limits

- No lifecycle change. Nothing accepts, re-verifies or changes the produced DEL-01-03 or DEL-01-05 artifacts. No S4 target is written.
- No `CON` item resolved, and no dependency edge.
- No tool declared or invoked.
- No CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or reliance claim. Do not ask the owner about CHECKING.
