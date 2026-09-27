# Review 01 of PR #971 (D-PEC-100 ruling), transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `dc93bde8a338dc082915225bd25fabc3b2ff6d4c` (base `origin/main` `d36c1a55f`). Repairs: `a45706f99`; this file is added after that.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `29967af5e74ea40e77c5254759f53767d678b9b73b6ef301a38558a2c47a584b`.

## Report (verbatim)

**Verdict: PASS WITH NOTES** for PR #971 at head `dc93bde8a338dc082915225bd25fabc3b2ff6d4c` (base `origin/main` `d36c1a55f`). Nothing is blocking. There are three non-blocking findings and some notes.

**My error: HEAD is detached. Please restore it.** While reviewing I ran a stray `git checkout -q origin/main --`. That detached the worktree's HEAD at `d36c1a55f` (origin/main). I tried to put it back and the permission classifier denied it, so I stopped there. Current state, checked read-only:
- The working tree is clean.
- `refs/heads/claude/pec-d100-ruling` still points at `dc93bde8a`, so no commits or files were lost.
- To restore: `git -C /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5 checkout claude/pec-d100-ruling`.

Every finding below comes from head content I read before the mistake, or from `git show dc93bde8a:…`.

## Checks

**1. Byte identity: PASS.**
- The published proposal `_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md` has SHA-256 `39c4331e083b28e34c1a9c0913247924e7a1cb4141a270e60c7dcd04dfcee25b`.
- The draft `PEC_SOW_REBUILD_S2_PREP_2026-09-26/DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md` on `origin/main` has the same hash, and `cmp` finds them identical.

**2. Ruling record `_DECISIONS/D-PEC-100_RULING_2026-09-26.md`: PASS, with notes.**
- **Quote (L9):** verbatim, "D-PEC-100: A; confirm B; M; defaults".
- **Q1 (L42):** A maps to option A. It says one run, seven contracts, no lifecycle change. Nothing is enlarged.
- **Q2 (L43):** matches proposal question 2 (proposal L281). The only change is that "the exhibit's" becomes "the `D-PEC-99` exhibit's", which clarifies without adding scope. The gates and the REM-002 condition are the same.
- **Q3 (L44):** matches add-on M (proposal L154–172 and L282). Files: six new `MEMORY.md` files (DEL-01-01, DEL-02-03..07) plus one row in DEL-01-06's existing file. Actor: WORKING_ITEMS. Timing: closeout, node M1. The DEL-01-06 `MEMORY.md` preimage `035ecb86…0a3f` matches at head.
- **Q4 (L45):** the model defaults match proposal L252.
- **Act script:** `apply_s2p.py` hashes to `42dc95532fdb39a308f59cf86e2bee73f8cf4f17808e403f42adcb308fc03d20`, on main and in the record (L30–32). All seven SOW preimages match at head.
- **Pinned files:** `PINNED` has exactly 23 entries (9 basis files, 7 `_STATUS.md`, 7 `Dependencies.csv`), and all 23 hashes match at head.
- **D-PEC-101 claim (L49) is true.**
  - I extracted all 161 paths from the D-PEC-101 proposal's grant tables on main (129 K4 plus 32 K1). None of them is among the 23 pins.
  - K1's `Dependencies.csv` writes are DEL-04-03, DEL-08-03, DEL-09-06 and DEL-10-03, plus two created files. Its `_STATUS.md` writes are only the two new folders.
  - Cross-check: the live `claude/pec-d101-act` branch (`b56dad37d`) changes 245 paths. None is a pin and none is a `ScopeOfWork.md`.
  - The D-PEC-101 generators do not reference `ScopeOfWork`, so "either act may land first" holds in both directions.

**3. Register row D-PEC-100 (`_REGISTER.md` L117): PASS.**
- It has 6 cells, like its neighbours. The proposal and script hashes are correct.
- PR #969 merged as `f392294b5`.
- The verdicts match the files: in-run verdicts 01 PASS WITH NOTES, 02 FAIL (blocker repaired), 03 and 04 PASS WITH NOTES; PR reviews 01 and 02 PASS WITH NOTES.
- The options list (A / A + M / amend / defer) and the grant and limits text match the proposal.

**4. Work graph and STATUS: PASS, with non-blocking findings 1 and 2.**
- No merge before merge is claimed: "the act is dispatched after the ruling PR merges" and "the act follows".
- The evidence line (graph L177) matches the brief.
- The STATUS line (L249) is true.
- Nothing prompts about CHECKING. The only mentions are exclusions (ruling L53).

**5. Containment: PASS.**
- Exactly 5 files change: the two new `_DECISIONS/` files, `_REGISTER.md`, the POST-SCA005 `WORK_GRAPH.md` and `docs/STATUS.md` (under D-PEC-88).
- `git diff --check origin/main...HEAD` is clean (exit 0).
- `harness.py self-check` exits 0, with no finding on the changed files.
- `validate_pec_loop_receipts.py` returns VALID.
- On PR CI, the pec, Harness pre-merge, Desktop E2E and Select App coverage checks pass; the rest skip.

## NON-BLOCKING

1. **Graph L82 contradicts L83.** L82 was left unchanged and still says "Ready after the ruling PR merges: the `D-PEC-101` act …". The D-PEC-101 ruling PR (#969) has merged, and the new L83 says that act "is in progress on branch `claude/pec-d101-act`". Suggest updating L82 to "in progress" and merging it with L83.

2. **The ordering line (graph L84) goes beyond the proposal and conflicts with L85.**
   - L84: "S2 lands before the S1 and S4 packets are drafted, because 15 other contracts quote the old S2 text."
   - The proposal (L97) recommends only to "rule S2 before the S1 and S4 packets are finalized". Two of the fifteen (DEL-02-08/09) belong to a later DEL-02-08/09 revision, not to S1 or S4.
   - L85 still says "Ready now: packet preparation for S1, S4 and D1".
   - Suggest aligning L84 with the proposal's wording, for example: "S2 is ruled, and lands before the S1/S4 packets are finalized, so they absorb the stale quotations".

3. **Ruling L53 narrows the proposal's disposition of the 15 downstream contracts.** Its parenthetical says "they are revised by the S1 and S4 packets under their own rulings". The proposal (L97) says they belong to "S1, S4 or a later DEL-02-08/09 revision". This grants nothing extra, but it misstates the source. Suggest quoting the proposal's phrase.

## NOTE

- **Ruling L13, "two HELP_HUMAN PR reviews":** the reviews were run by a fresh `pec-reviewer` TASK that HELP_HUMAN dispatched (`REVIEW_PR964_01.md` L3). "HELP_HUMAN-dispatched" would be more exact. "Nothing blocking" describes the final state; verdict 02 did fail, and the register records it correctly.
- **The number moved straight from NOT_PREPARED to RULED.** Proposal L3 says the number becomes final when HELP_HUMAN publishes the packet "and moves that row to `AWAITING_RULING`". The row skipped that state. The ruling (L26) says the number is final anyway. This is harmless, since the proposal's status line is descriptive.
- **The M1 row (graph L76) names only `D-PEC-98` add-on M.** Its generic wording covers D-PEC-100 M, and the S2 row says "Add-on M is written at M1". Naming D-PEC-100 M there, including the rule that DEL-01-06's row goes after the D-PEC-96 row, would make M1 self-contained.
- **The record's status line (L19) and the register differ in wording.** The record says "EFFECTIVE ON SHARED-MAIN PUBLICATION" and the register says "EFFECTIVE ON MERGE". This matches the D-PEC-101 precedent.

## Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-100_RULING_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md (used for the pin cross-check)

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| Reviewer's detached HEAD | HELP_HUMAN restored the checkout to `claude/pec-d100-ruling` (`dc93bde8a`); no file or commit was lost |
| NON-BLOCKING 1 (graph L82 vs L83) | Repaired in `a45706f99`: the D-PEC-101 act is "in progress" in one line |
| NON-BLOCKING 2 (ordering wording) | Repaired: "S2 is ruled and lands before the S1 and S4 packets are finalized", with the DEL-02-08/09 remainder named, merged into the "Ready now" line |
| NON-BLOCKING 3 (ruling's downstream wording) | Repaired: quotes the proposal's "S1, S4 or a later DEL-02-08/09 revision" |
| NOTE (PR reviews "HELP_HUMAN") | Repaired: "HELP_HUMAN-dispatched" |
| NOTE (NOT_PREPARED straight to RULED) | Recorded: publication and ruling happened in the same PR; the ruling states the number is final |
| NOTE (M1 names only D-PEC-98 M) | Repaired: M1 names D-PEC-100 add-on M, including the DEL-01-06 row placement |
| NOTE (status wording) | No change: follows the D-PEC-101 precedent |
