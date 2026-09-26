# Review 01 of PR #954 (SCA-006 checkpoint-3 acceptance with A6; D-PEC-98 and D-PEC-99 rulings), transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `4ddea329370e9f34815673314944ab170994de83` (base `origin/main` `c61a540ea`). Repairs: `b823aac16`, then merge of `origin/main` `0583e36ff` (`b37ca82fa`); this file is added after that.
- **SHA-256 of the report text below (UTF-8):** `e0d8d42773e1733ac27fcd1bc3bca9bf3a7391afed4a2783c5936fcf55c80e00`.

## Report (verbatim)

**PR #954 review (head 4ddea3293, base c61a540ea): PASS WITH NOTES.** There are no BLOCKING findings. Five NON-BLOCKING findings are stale present-current statements, all in records. Four of them are false only because this PR moves the pointers. I recommend fixing them before merge.

I reviewed read-only. I read files with `git show` and ran the validators in the checkout (clean at the PR head) and in `git archive` exports in my scratchpad. I modified nothing.

## What I verified (all pass)

**1. Fidelity**
- **Owner quotes:** all three are verbatim everywhere they appear in the diff, with the period only on the CP3 string, as given.
- **CP3:** the DECISION.md interpretation maps Q-CP3-A, Q-CP3-1 (a) and Q-CP3-2 (a) to exactly RUN_SUMMARY §9's recommendations. It claims no owner inspection.
- **D-PEC-98 ruling:** questions 1–6 map to the proposal's recommendations (A, S, M, question-4 re-pin, CON-005 open, defaults).
  - Proposal hash `92b6f1a2…3e40`, `apply_d98.py` `19c2ecb6…419e` and candidates `03cce13f…`/`aafb54fd…` all recompute.
  - The re-pin text matches proposal question 4: three places move; only `TARGETS` and the four register/PRD entries of `PINNED` change; a second `PIN` is added to `verify_d98_state_claims.py`; a quote failure voids the re-pin.
  - The grant and limits are subsets of the proposal. The CON-005 wording matches candidate CON-005, which "extracts no node reference from prose".
- **D-PEC-99 ruling:**
  - It selects option A, question 1 (a) with `--q1 s1`, and {N}=D-PEC-99. `gen_d99.py` defaults to `--decision D-PEC-99` and `--q1 s1`.
  - Generator `1fad0239…7237`, `verify_d99.py` `c1d50dfd…1865`, census `b0e25361…`, account `b240b38d…` and the `AGENTS.md` pin `4400c4e9…` (the live file at base and head) all recompute.
  - The counts (71 / 12 = 4+4+4 / 9; 62 paths) match the draft.
  - Verdict 03 is PASS WITH NOTES with 0 BLOCKING. The draft is identical at the verified head 0729769be and at the PR #951 head.
- **Supporting claims:** REVIEW_PR944_02 is PASS for both contracts and contains N1/N2 as described. The PR states cited are correct: #943, #944, #946, #950 and #951 are all MERGED at the stated merge commits, and every cited commit is an ancestor of c61a540ea.

**2. A6**
- Live `SOFTWARE_DECOMP.md` hashes `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1` (head blob and working tree).
- Against origin/main (`3ef0412a…`) the diff is exactly the `status:` and `accepted:` lines. The `accepted:` line equals the CP2_CANDIDATE form with the date slot set to 2026-09-26. `date:`, L574 and L700 already carry 2026-09-26.
- `_Decomposition/_LATEST.md` counts match the registers: 100 items, 74/18/8, 11 packages, 68 rows (64 active, 4 retired), 10 open / 3 resolved issues. Its register and PRD hashes match, and the DEL-08-06/DEL-10-13 folders are absent.
- The audit counts (0 / 3 / 71 / 12) match `Decomp_Coverage_IssueLog.csv`. `coverage_summary.json` `b9a068c0…` matches.
- `_ScopeChange/_LATEST.md` and `DecompCoverage/_LATEST.md` are truthful.

**3. `ACCEPTED_MANIFEST.csv`:** I recomputed all 15 hashes.
- Accepted rows equal the head: SOFTWARE_DECOMP at 9374c21f, and the other nine accepted rows (registers, PRD, `AGENTS.md`, tranche manifest, audit summary, hunk, Supersession_Map, Post_Change_Coverage) are unchanged from main.
- The three "at presentation" rows equal origin/main: RUN_SUMMARY `690b4923`, Decision_Log `96cc5602`, Handoff_State `89af74b8`.

**4. Published D-PEC-99 proposal:** byte-identical to the draft, `29e2ff5704d45f0da31f41fd80bf822003743fbf9effdda4ebbc2806306d5c79`.

**5. SCA-006 package records**
- Decision_Log changes in place only the front matter and the CP3 row; the rest is appended.
- Handoff_State changes in place only the front matter and the Decision_Log hash row; the rest is appended.
- RUN_SUMMARY is append-only.
- The quoted Decision_Log hash `46530f08…` equals the head blob.

**6. Register:** rows D-PEC-97, -98 and -99 have 6 columns, and their hashes and text are accurate.

**8. Containment:** all 18 paths are under `projects/pec/**` and inside the stated grants. There is no lifecycle, SOW, `v2/**`, PRD or `AGENTS.md` change.

**9. CHECKING:** nothing prompts the owner about CHECKING.

**Checks run**
- Harness self-check exits 0.
- `validate_pec_loop_receipts.py --repo-root .` reports VALID, exit 0.
- `validate_decomposition_registers.py --strict` exits 1 with 0 errors and 28 warnings, byte-identical at base and head.
- `git diff --check` is clean.
- CI was still running (harness IN_PROGRESS, Harness pre-merge QUEUED) when I looked.

## NON-BLOCKING

1. **`projects/pec/docs/STATUS.md:168-169`** says SCA-005 is closed "and `_ScopeChange/_LATEST.md` names it". It is now false, because this PR moves the pointer to SCA-006.
2. **`projects/pec/docs/STATUS.md:222-224`** says `COV_SCA005_POSTSETUP_2026-09-25_1606` is "now named by `_Evaluation/DecompCoverage/_LATEST.md`". It is now false after the Q-CP3-2 (a) move. Line 228–229 ("`_LATEST.md` … describe the post-setup state") is stale in the same way.
3. **`projects/pec/README.md:126`** says `execution/_ScopeChange/` has "the active scope-change pointer (SCA-005)" and "SCA-001 to SCA-005 … SCA-005 checkpoint-group snapshots". This was true at base and is false at head.
4. **POST-SCA005 `WORK_GRAPH.md:62`** (S2 row state) still says "DEL-01-06 waits for G1", but G1 is COMPLETE in this PR. The Order section (L80) already says S2 includes DEL-01-06.
5. **`projects/pec/execution/_Coordination/_COORDINATION.md:16-18`** (not touched by the PR, default-writable) still states revision 1.5 is `current_basis`. It becomes false on merge. The SCA-005 precedent left the same kind of line for a later currency packet, so this could be routed rather than fixed here.

## NOTE

- **Acceptance commit (`D-PEC-98_RULING_2026-09-26.md:59-63`).** The ruling defines it as the origin/main merge commit of this PR. The SCA-005 precedent pin `c9e5cd87d`, which the candidates call "the checkpoint-3 acceptance commit", is the branch commit, not the merge commit. Proposal question 4 does not fix which is meant. The merge-commit reading is consistent with it and is more robust to squash merges or added repair commits. At that commit the four `PINNED` register/PRD files will equal the manifest values (9374c21f, 94ee5d18, 1d24a4b8, ae49b806). No enlargement.
- **POST-SCA005 `WORK_GRAPH.md:133`** says the RR1 manager's return is under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/`. It is actually at `AgentRuns/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/returns/RR1_REMAINING_RETIREMENT_ACCOUNT.md`. The brief is under POST-SCA005.
- **Register D-PEC-98 row, "Blocks" column (`_REGISTER.md:115`).** It still lists only the SOW and MEMORY paths and says "no lifecycle change unless add-on S is ruled". Now that S is ruled, the two `_STATUS.md` paths are opened by the ruling but not named in that cell. The ruling record governs.
- **`Decision_Log.md:31`** cites RUN_SUMMARY `690b4923…9b62` without saying "at presentation". RUN_SUMMARY now hashes `6c627456…`.
- **`ACCEPTED_MANIFEST.csv:12-13`** say "updated additively by this act". Both files also had front matter changed in place (and one hash row in Handoff_State). The wording copies the c9e5cd87d precedent.
- **origin/main has moved** to 0583e36ff (PR #949, D-GOV-49). It adds `projects/pec/execution/_Coordination/NOTICE_2026-09-26_PROJECT_DAG_D-GOV-49.md`. It does not overlap this PR's paths. The graphs' "Checked basis c61a540ea" does not reflect the new notice; triage it in a later graph update.
- **Pre-existing staleness, not introduced here:** `README.md:128` and the STATUS "P1 source … slices" sentence list only D-PEC-74/75/77/84/85, omitting later slices (87, 89, 91, the 96 act).
- **Wording nit:** `DECISION.md:31-32` records the offered reply without the final period that the owner used.

## Key paths
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-98_RULING_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_RULING_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/README.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_COORDINATION.md`

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| NON-BLOCKING 1 (`docs/STATUS.md` SCA-005 sentence) | Repaired in `b823aac16`: the sentence now says the pointer named SCA-005 until the SCA-006 acceptance and now names SCA-006 |
| NON-BLOCKING 2 (`docs/STATUS.md` audit-pointer and "describe the post-setup state" lines) | Repaired: both lines are past tense, naming the move to `COV_SCA006_POSTCHANGE_2026-09-26_0051` and the revision-1.6 pointers |
| NON-BLOCKING 3 (`README.md` `_ScopeChange/` row) | Repaired: SCA-001 to SCA-006 evidence, SCA-005 and SCA-006 snapshots, active pointer SCA-006 |
| NON-BLOCKING 4 (graph S2 state) | Repaired: DEL-01-06 is in S2's packet preparation (G1 COMPLETE) |
| NON-BLOCKING 5 (`_COORDINATION.md` basis lines) | Repaired in this PR: the accepted-basis line (L16–19, default-writable body) names revision 1.6, and a dated item 15 records the SCA-006 acceptance. `b823aac16` also rewrote the derivative-package parenthetical in the human-owned Notes section; review 02 blocked that, and it is restored to its base bytes (`REVIEW_PR954_02.md`) |
| NOTE acceptance commit | No change: the merge-commit reading is the ruling's stated definition and consistent with question 4 |
| NOTE graph return path for RR1 | Repaired |
| NOTE register D-PEC-98 "Blocks" cell | Repaired: the cell records that add-on S opens the two `_STATUS.md` paths |
| NOTE `Decision_Log.md` RUN_SUMMARY hash | Repaired: "at presentation" added; `Handoff_State.md`'s quoted Decision_Log hash updated to match |
| NOTE `ACCEPTED_MANIFEST.csv` "additively" wording | No change: the rows follow the SCA-005 precedent, and `Handoff_State.md` records the in-place front-matter and hash-row changes |
| NOTE `origin/main` moved (D-GOV-49 notice) | Merged `origin/main` `0583e36ff`; the notice is triaged in the graph's notice list (owner defers; no node) and the checked basis updated |
| NOTE pre-existing P1-slice lists | No change here; left for a later STATUS/README currency pass |
| NOTE offered reply without period | No change: the record quotes HELP_HUMAN's offered reply as offered; the owner's act is quoted with its period |
