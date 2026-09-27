# Brief S2A — D-PEC-100 act: seven Scope of Work replacements (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S2 (the act). Role: WORKING_ITEMS (Type 1), with `Workflow: chirality-root:bundled:workflow:scope-of-work` supplying the authoring discipline already applied and the independent `MODE=VERIFY` (record identity and hashes). Model steer: `claude-opus-5-5`, high reasoning, for you and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling.** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-100_RULING_2026-09-26.md`. The owner's words: "D-PEC-100: A; confirm B; M; defaults".
- **Proposal.** `_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md`, SHA-256 `39c4331e083b28e34c1a9c0913247924e7a1cb4141a270e60c7dcd04dfcee25b`. It is your specification: exact product grant (7 paths, pre/postimages, 23 pinned files), generation method, finite verification, independent verifier, administrative grant, rollback and limits. Do not enlarge it.
- **Bound act script** `projects/pec/execution/_Coordination/PEC_SOW_REBUILD_S2_PREP_2026-09-26/apply_s2p.py`, SHA-256 `42dc95532fdb39a308f59cf86e2bee73f8cf4f17808e403f42adcb308fc03d20`, with the seven candidates under that prep folder's `candidates/` and the check aids (`verify_s2p_quotes.py`, `verify_s2p_state_claims.py`, `check_sibling_ids.py`, `scan_external_quotes.py`, `test_apply_s2p.py`, `run_s2p_checks.sh`, `quotes/`, `claims/`).

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and register row `D-PEC-100` `RULED A / B CONFIRMED / M` (PR #971).
- `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) ALLOW on each target with `dispatch-for-production` before the act, and `rely-for-production` before fan-in — run the latter BEFORE committing the act's writes.
- Isolated worktree on branch `claude/pec-d100-act` from fresh `origin/main`. On any failure, discard and return.
- **Parallel act.** The `D-PEC-101` act (branch `claude/pec-d101-act`) runs concurrently; it writes none of this act's 7 targets or 23 pins. If it merges before your PR, re-fetch `origin/main`, confirm your pins still hold, and rerun the quote, state-claim and sibling-ID checks on the updated base (its K4 changes these deliverables' `_CONTEXT.md`/`_REFERENCES.md`, which the candidates describe as naming revision 1.5 at their observation commit — true as observations).

## Act

1. Run root `projects/pec/execution/_Coordination/SOW_REBUILD_S2_{D}/` with the exact script copy, `candidates/`, `quotes/`, `claims/` and check aids (hashes checked), plus a `.gitattributes` exempting raw outputs from whitespace checks if needed.
2. Run the script `--check-only`, then once for real, from the repository root. The script inventories `projects/pec`: capture its output outside `projects/pec` (session scratchpad) and copy it into the run root after it exits.
3. Run the proposal's whole "Finite verification" table and save each command, exit code and output (validator `PASS format=SOW_V1` ×7; checklists; boundary owners; quotes; state claims; sibling IDs; strict registers identical before/after; harness and receipts identical; containment exactly the 7 contracts plus the run root and your brief/return; `git diff --check`).
4. One fresh read-only `pec-reviewer` (opus) performs the proposal's independent verifier (the method's `MODE=VERIFY` on all seven postimages, plus basis, byte identity, Part B fidelity, containment). Save `VERIFIER_VERDICT_NN.md` in the run root; defects come back to you. Wait for its verdict in the foreground if the host allows; commit and push before waiting.
5. Add-on M is written at the undertaking's closeout (node M1), not now.
6. Write `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the run root.

## Write boundary

Only: the 7 `ScopeOfWork.md` targets (via the script); the run root; this brief copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S2A_D100_SOW_ACT.md`; your return at `…/returns/S2A_D100_SOW_ACT.md`. Nothing else: no `MEMORY.md`, `_STATUS.md`, register, dependency, context, reference, decomposition, `v2/**`, PRD, `docs/**`, README, `_DECISIONS/**`, work graph or foreign path.

Commit and push after each step. Commit your return before you hand back.

## Publication

Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Open a PR against `main`; do not merge. If CI reports "Update the PR base", report it; do not repair it.

## Return

PR URL and head; act report; written paths with hashes; check results; verifier verdicts; containment; anything unresolved.

## Limits

No lifecycle change; no CON item resolved; no DEL-02-07 production act; no edit to the 15 downstream contracts; no CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
