# Brief K14A — D-PEC-101 act: K1 then K4 with add-on C, then add-on V (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph nodes K1 and K4. Role: WORKING_ITEMS (Type 1) under `chirality-root:bundled:workflow:project-setup` (record identity and hashes). Model steer: `claude-opus-5-5`, high reasoning, for you and every child. The owner said "defaults".

## Authority and specification

- **Ruling.** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_RULING_2026-09-26.md`. The owner's words: "D-PEC-101: K4 with C; K1; V; Notes a; defaults".
- **Proposal.** `_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md`, SHA-256 `7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25`. It is your specification: exact product grant (161 paths), generation method, finite verification (including the combined-tree K4 verifier expectation: original export as before-state, exactly one containment FAIL listing K1's 20 paths), add-on V, independent verifier, administrative grant, rollback and limits. Do not enlarge it.
- **Bound generators** in `projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/`:
  - `k1/gen_d101_k1.py` `4892c6a3c7fab4ba405b1ca201b7cab423c8c59644dee5f1d675d2e5f692cecb` — `--act-date {D}`, default actor `TASK+preparation`, no `--reproduction`;
  - `k4/gen_d101_k4.py` `075036f0a8c214a156aec151aaa52f6d1b78c2694f4306d410579ffcef9f0e73` — `--covers`.
  Copy both and the verify scripts (`k1/verify_d101_k1.py`, `k4/verify_d101_k4.py`) byte for byte into the run root and check hashes.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and register row `D-PEC-101` `RULED K4+C / K1 / V` (PR #969).
- `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) ALLOW for every target with `dispatch-for-production`, and `rely-for-production` before fan-in.
- Isolated worktree on branch `claude/pec-d101-act` from fresh `origin/main`. Any generator or check failure: discard the worktree and return (the K1 folder-creation step can leave untracked files; discarding removes them). Do not repair outside the proposal.

## Act (order: K1, then K4 with C, then V)

1. Run root `projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_{D}/` with a `.gitattributes` exempting its generator reports and closure outputs from whitespace checks (as the prep folder's `k1/` and `k4/` do). Record pre-act baselines: strict registers, closure, harness self-check, receipts validator.
2. **K1.** One bounded `pec-task` (the eligible `preparation` actor) runs `gen_d101_k1.py --check-only`, then the act, from the repository root. Capture generator output outside `projects/pec` if the generator inventories the tree, then copy it into the run root. Verify the 32 postimages against the proposal's table (at `{D}` = 2026-09-26; otherwise the slot rule).
3. **K4 with C.** You or that TASK run `gen_d101_k4.py --covers --check-only`, then the act. Verify the 129 postimages (A+C table).
4. Run the proposal's whole "Finite verification" table and save each command, exit code and output: strict registers (with K1: exit 1, 0 ERROR, the same 26 XRG-013, 0 DRB-008, 68 registers, 285 rows); closure (127 edges, 0 SCCs, …); quote currency 127/127; COV-080 anchor coverage; `verify_d101_k1.py base <repo> --allow-k4` PASS; `verify_d101_k4.py base <repo> --covers --allow-k1` against the ORIGINAL export giving exactly the one containment FAIL (149 vs 129) and every other check PASS; schema VALID ×6; minimum fileset PASS ×2; harness and receipts identical before/after; byte identity; containment; whitespace (product paths).
5. **Independent verifier.** One fresh read-only `pec-reviewer` (opus) applies the proposal's "Independent verifier" section, including reproduction on a fresh export. Save `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you. Tell HELP_HUMAN (in a pushed commit message and your return) when the verifier has passed K1: HELP_HUMAN then applies the owner-authorized Notes (a) replacement of `_COORDINATION.md` L225–227 in this PR; you do not touch `_COORDINATION.md`.
6. **Add-on V.** After the product writes are verified, one `pec-task` runs `audit-decomp` exactly as the proposal's "Add-on V" states into a folder from `tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV D101_POSTSETUP`. Only on 0 BLOCKERs do you move the pointer with `tools/scaffolding/update_latest_pointer.sh` (preimage `f8469f88…a9dea`); otherwise leave it and report the findings.
7. Write `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` (PROJECT_SETUP closeout format; record the SCA-006 Lane B1/B2/B3/B7 closeout there) in the run root.

## Write boundary

Only: the 161 granted paths (via the generators); the run root; with V, the new `COV_D101_POSTSETUP_*` folder and `_Evaluation/DecompCoverage/_LATEST.md` (0 BLOCKERs only); this brief copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K14A_D101_ACT.md`; your return at `…/returns/K14A_D101_ACT.md`. Nothing else: no SOW, MEMORY, other `_STATUS.md`, decomposition, `_ScopeChange/**`, `checkpoint_snapshots/**`, PRD, `v2/**`, `AGENTS.md`, `_COORDINATION.md`, `_DECISIONS/**`, work graph, `docs/**`, README or foreign path.

Commit and push after each step so a forced handback loses nothing. Commit your return before you hand back.

## Publication

Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Open a PR against `main`; do not merge. If CI reports "Update the PR base", report it; do not repair it.

## Return

PR URL and head; generator reports; written paths with hashes (or the aggregates); check results; verifier verdicts; the audit verdict and whether the pointer moved; containment; anything unresolved.

## Limits

No lifecycle change beyond the two new `OPEN` files; no action on the D-GOV-48 warnings; no `project-setup` `INCREMENTAL` run, `SETUP_LOG.md` or `project-dag` adoption; no tier-0 profile act; no CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
