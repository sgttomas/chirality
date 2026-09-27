# Brief D1A — D-PEC-105 act: premise-only amendment of the DEL-00-01 ADRs and contract and the DEL-00-03 SPEC and contract (WORKING_ITEMS)

- **Parent:** HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node D1 (the act).
- **Role:** WORKING_ITEMS (Type 1). You follow the owning discipline the proposal records: the bounded candidate edit and its deterministic checks from the 2026-08-09 route, and `chirality-root:bundled:workflow:scope-of-work` `MODE=VERIFY` for the two contracts. The ruling is the authority for the replacements. Record the SHA-256 of each method file you load.
- **Model steer:** `claude-opus-5-5` at high reasoning, for you and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-105_RULING_2026-09-27.md`. The owner's words: "D-PEC-105: A; P; RR1; confirm 4a 4b; M; defaults".
- **Proposal:** `_DECISIONS/D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md`, SHA-256 `077610057791063e2308d932cf08a7ac44cd02793fe60925c744d969fd6ba89f`.
  - It is your specification: the exact grant, add-on P, add-on M, the generation method, finite verification (checks 1–12), the independent verifier, the administrative grant, rollback and limits. Do not enlarge it.
  - RR1 grants nothing to this act. The REVIEW-before-merge variant was **not** selected.
- **Preparation evidence:** `projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-26/`. It contains:
  - `apply_d1p.py` (`952a7512fd74e1b77f2f6b948d3cf46c876448ee1dee5370759f627236399d4d`), run with `--with-addon-p`;
  - `render_candidates.py`, `premise/`, `candidates/`, `quotes/`, `claims/` and `targets.json`;
  - `run_d1p_checks.sh`, `negative_controls.sh` and the tests;
  - `SHA256SUMS`. Verify all of it with `shasum -a 256 -c`.
- **Precedent act:** the `D-PEC-102` act, PR #998. See its run root `SOW_CURRENCY_S4_2026-09-26/`, its brief `briefs/S4A_D102_SOW_ACT.md` and HELP_HUMAN's reviews `returns/REVIEW_PR998_0*.md`.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and the register row `D-PEC-105` `RULED A + P …` (PR #1006, merged as `c5d852c4a`).
- `apply_d1p.py --with-addon-p --check-only` passes, with all 4 preimages and all pins as tabled. That includes both deliverables' `_STATUS.md`, `_REVIEW.md` and `Review_Findings.csv`. On any mismatch, stop and return: no re-pin is authorized.
- `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) returns ALLOW on each of the 4 targets, twice:
  - `dispatch-for-production` before dispatch;
  - `rely-for-production` before fan-in.

  Record each run with a `date -u` line.
- Work in an isolated worktree on branch `claude/pec-d105-d1-premise-act`, cut from fresh `origin/main`. On any failure, discard and return. Do not repair outside the proposal.
- **Parallel work.** Two other acts may run at the same time:
  - The `D-PEC-104` act (S1) writes only twelve other deliverables' `ScopeOfWork.md`.
  - The X1 act (`D-PEC-106`, if ruled) writes `v2/tests/parsers/**`, `software-workflow.json` and, with add-on L, three `_STATUS.md` files in PKG-02.

  None of these is a D1 target or pin. If `origin/main` moves before your PR merges:
  1. Re-fetch, and merge without a rebase.
  2. Rerun `--check-only` on an export of the new main, `run_d1p_checks.sh`, and the quote and state-claim verifiers.
  3. If a pinned file or quoted locus changed, stop and report.

## Act

1. **Run root.** Create `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_{D}/`, where `{D}` is the act date.
   - Copy in the bound files the proposal names, and check their hashes.
   - Read `apply_d1p.py`'s write-set inventory rule to decide where output may be written during a run: beside the script in its own directory if the script excludes it, otherwise outside `projects/pec` (copied in afterwards). Record the decision in `MANIFEST.md`.
   - Export `TMPDIR` to a scratch directory outside the repository in every shell.
2. **A + P.** Run `apply_d1p.py --with-addon-p --check-only`, then run it once for real from the repository root.
3. **Verify.** Run the proposal's finite verification, checks 1–12. Save each command, exit code and output. The checks include:
   - `render_candidates.py` equality;
   - validator ×2 on the contracts;
   - checklists equal to the prepared `a3bc80a0…21b1` and `6e99f93c…8cf9`, byte-identical on rerun;
   - boundary owners;
   - quotes 74/74 and state claims 126/126;
   - no `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv` or `REV_*` change;
   - strict registers, harness and receipts identical before and after (at the current basis: exit 1, 0 errors, 26 `XRG-013`);
   - quote currency 127/127;
   - stored-evidence whitespace 0;
   - containment of exactly the 4 targets plus the run root;
   - `git diff --check`.
4. **Verifier.** Dispatch one fresh read-only `pec-reviewer` (opus) for the proposal's independent verification. It checks:
   - `MODE=VERIFY` on both contracts;
   - premise-only discipline on every hunk;
   - the 4(a) rebind as ruled;
   - posture 3 and add-on P agreeing;
   - containment.

   Save `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you. Run it in the foreground, or wait for it inside your turn; do not end your turn to wait.
5. **Add-on M.** It is written at the undertaking's closeout (node M1), not now. Do not create any `MEMORY.md`.
6. **Records.** Write `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` and a run-root `SHA256SUMS`.

## Write boundary

You may write only:
- the four targets, through `apply_d1p.py --with-addon-p`;
- the run root;
- this brief, copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/D1A_D105_PREMISE_ACT.md`;
- your return, at `…/returns/D1A_D105_PREMISE_ACT.md`.

Write nothing else. That excludes `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `REV_*`, `MEMORY.md`, registers, `Dependencies.csv`, `_DEPENDENCIES.md`, `_CONTEXT.md`, `_REFERENCES.md`, the decomposition, `v2/**`, the PRD, `docs/**`, `README.md`, `_DECISIONS/**`, the work graph, and any other deliverable or foreign path. HELP_HUMAN adds the graph and STATUS records to your PR.

Commit work in progress and push early. Commit your return before you hand back.

## Publication

- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Open a PR against `main`, and do not merge it.
- If CI reports "Update the PR base", merge `origin/main` without a rebase, rerun the affected checks and push.

## Return

- PR URL and head SHA
- the act report
- the written paths with their hashes
- check results
- verifier verdicts
- containment
- anything unresolved

## Limits

- No lifecycle change. Both deliverables stay `CHECKING`, and you do not ask about it.
- No REVIEW act and no acceptance.
- No `CON` resolved and no dependency edge.
- No tool declared or invoked.
- No readiness, release or reliance claim.
