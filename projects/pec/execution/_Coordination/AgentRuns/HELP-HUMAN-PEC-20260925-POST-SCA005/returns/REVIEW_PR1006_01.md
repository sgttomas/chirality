# Review 01 of PR #1006, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `b23d0276b7168f35dc879b8fcf7ef4e2b7be71f2`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `ccc603ea0b1887f0c276030f3b4ecd2a9d591f85b73d28d531365eee3eae259f`.

## Report (verbatim)

**PR #1006 review, head `b23d0276b7168f35dc879b8fcf7ef4e2b7be71f2` (covers both commits: `63a40f6ed` for D-PEC-105 and `b23d0276b` for D-PEC-106). Verdict: PASS WITH NOTES.** Nothing blocks. There are four NON-BLOCKING findings, all stale or loose wording that is easy to fix before merge, and eight NOTEs. I made no edits and no git writes, and ran no checkout or switch. I exported with `git archive` into my own mktemp directory under the scratchpad, with TMPDIR set to it, and deleted it afterwards. The worktree is clean.

## Verified (no finding)

**Containment**
- `63a40f6ed` against base `16010b4ca` changes exactly the five briefed paths.
- `b23d0276b` adds exactly the two D-PEC-106 files, `D-PEC-106_RULING_2026-09-27.md` and `D-PEC-106_x1_parser_fixture_suites_proposal_2026-09-26.md`. It also edits the shared register, graph and STATUS. Seven paths in total.
- `git diff --check 16010b4ca b23d0276b` is clean.

**Proposals published unchanged**
- D-PEC-105: `077610057791063e2308d932cf08a7ac44cd02793fe60925c744d969fd6ba89f`. It equals the prep-folder draft at both the PR head and origin/main.
- D-PEC-106: `677b59f6b1ae19b911e6e07aecfa4df0f39a380fb3ab806903da87c8fa18d279`. It equals the draft and its `SHA256SUMS` entry.

**Act scripts and merges**
- `apply_d1p.py` is `952a7512…9d4d`, matching `SHA256SUMS`.
- `apply_x1p.py` is `452ff66af71b…2428`, matching `SHA256SUMS`.
- PR #997 merged as `cfe753dc7`; PR #996 merged as `b0a9a52b6`.

**Verdict counts**
- D1: in-run verdicts 01–03 FAIL and 04–06 PASS WITH NOTES. `REVIEW_PR997_01`–`03` are all PASS WITH NOTES.
- X1: in-run verdicts 01, 04 and 07 FAIL; 02, 03, 05, 06 and 08 PASS WITH NOTES. `REVIEW_PR996_01` and `_02` are PASS WITH NOTES; `_03` is PASS.
- The ruling records and register rows state these correctly.

**Pins are live (check-only runs on exports of the head)**
- `apply_d1p.py --with-addon-p --check-only` exits 0: "CHECK preflight passed; mode A+P; 4 modifies".
- `apply_x1p.py --check-only` exits 0: "34 creates, 1 modifies".
- The three X1 `_STATUS.md` files still hash to their tabled preimages (`6f94c04f…`, `4341d6b2…`, `e67be587…`). `write_status.sh` is still `0bf835f5…`.

**Base drift**
- Since `f0a6159c9` (the D1 and X1 rendering basis), the only change to `projects/pec` outside the `_Coordination` prep folders, rulings, register and graph is `docs/STATUS.md`. The other merges are packets (#996, #997, #986), a ruling (#1005) and Piping PRs.
- Since the observation commit `6c6cc1b00`, the only other product files that changed are the eight S4 contracts. No D1 or X1 target or pin moved.
- The S1 act exists as local branch `claude/pec-d104-s1-sow-act` (worktree `.claude/worktrees/pec-d104-act`, commit `053ca4e22`). It is not pushed to origin.
  - That commit holds only the run root and the brief `briefs/S1A_D104_SOW_ACT.md`.
  - `apply_s1p.py` targets the twelve S1 contracts. It does pin some files, but none is a DEL-00-01 or DEL-00-03 file, a DEL-02-03/08/09 file or `software-workflow.json`, so it pins no D1 or X1 target.

**RV1 and the other graph tables**
- The RV1 row has 5 cells, like every node row.
- The notice it cites, `projects/pec/execution/_Coordination/NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md`, exists and hashes to `30aab470…4168`, as the proposal pins.
- Its needs match the proposal's RR1 text: a separately authorized REVIEW that names its review type and method basis, granting nothing.
- The D1, M1 (both D-PEC-105 and D-PEC-106 add-on M entries), Order, next-work and owner-line entries agree with each other.
- The X1 residuals listed under next work match `returns/X1P_FIXTURES_PROPOSAL.md` L192–197 and `REVIEW_PR996_01` item 9.

**Faithfulness (K-AUTH-1)**
- Each resolution in D-PEC-105 matches the owner's string and the proposal's question text.
  - The three lapse statements match the "Acceptance-lapse account": DEL-00-03 SOW and SPEC "on the record's own terms"; the DEL-00-01 AC-007 acceptance of `f63ecc27…5db5` "hash-bound".
  - RR1 is recorded as intent, granting nothing, in the ruling, the register row and the graph.
  - Readings 4(a) and 4(b), P with `--with-addon-p`, and M all match.
- "The owner did not select the REVIEW-before-merge variant" is fair. It was offered only under Amend, the presentation reported it, and the owner said "A".
- Each resolution in D-PEC-106 also matches. Questions 1–6 track the question text; the thresholds follow question 3's own wording. L follows the `D-PEC-85` pattern, commits before the act, and holds the rollback carve-out. The grant's single-run and rerun rules are kept ("apply as written").
- The ruling discloses that the packet left L to the owner and that HELP_HUMAN recommended it.
- Neither record prompts about CHECKING. D-PEC-105 makes no lifecycle change. D-PEC-106's only lifecycle change is the owner-ruled L on three INITIALIZED deliverables.

**CI on `b23d0276b`:** pec, harness, Harness pre-merge, Desktop E2E (source mode) and the Select App, PEC and source coverage jobs pass; the rest skip. `mergeStateStatus` CLEAN; review decision empty.

## NON-BLOCKING

1. **Graph scope contradicts RV1.** `WORK_GRAPH.md:20` still says "CHECKING, ISSUED and acceptance acts, which are the owner's own" are "Left for later, not in this graph". RV1 (`:67`) now holds the owner's `ACCEPT_EXACT_BYTES`.
   - Because Completion (`:10`) needs every node COMPLETE or removed, F1 now waits on a REVIEW authorization and an acceptance the owner has not given.
   - It is also unclear whether RV1 gates C1: Order `:93` puts it after the D1 act, and C1's needs say only "All substantive PRs merged".
   - Suggested fix: either amend `:20` and state RV1's place relative to C1, or record RV1 as carried beyond this undertaking.
2. **Stale notice-triage line.** `WORK_GRAPH.md:120` still says the undertaking "makes no CHECKING, ISSUED or review lifecycle act (its only lifecycle act is `D-PEC-98` add-on S …)" and that "D1 accounts for it when it is prepared". After this PR, D-PEC-106 add-on L is a second lifecycle act, RV1 is a planned REVIEW, and D1 has been prepared and ruled.
3. **D-PEC-106 "Base drift" misplaces two items.** `D-PEC-106_RULING_2026-09-27.md:63–67` says `origin/main` "has gained … the S1 and D1 packets and rulings, and the S1 act now running".
   - The D1 ruling is in this same PR, not on origin/main.
   - The S1 act is a local, unpushed branch.
   - "a X1" should read "an X1".
   - The underlying safety claim is true (no X1 target or pin moved; check-only passes).
4. **S1 state is inconsistent.** The recovery lines now say the S1 act is running (`WORK_GRAPH.md` next work, `:168`, `:169`). The S1 row (`:61`, "the act is next"), Order `:88` ("Next: its act") and `docs/STATUS.md:273` ("its act is next") still say it is next.

## NOTE

1. `D-PEC-105_RULING_2026-09-27.md:44` says AC-011 and AC-007 are unsatisfied "until the RR1 owner act". The proposal says "until a later owner act". RR1 is only intent, so the proposal's wording is safer.
2. The D-PEC-105 ruling's 4(a) summary (`:47`) lists the changed IDs but not the re-resolution of AC-002, AC-004, VER-002 and VER-004. It also omits the correction of the basis note, which has been stale since SCA-004. Both are incorporated by reference, so nothing is enlarged.
3. With P selected, the proposal's lapse account adds that DEL-00-01's SELF_CHECK SOW basis will describe superseded bytes. Neither the ruling nor the M1 receipt list (`WORK_GRAPH.md:77`) carries this.
4. The D-PEC-105 register row (`_REGISTER.md:122`) lists options "A / A + P / amend (incl. REVIEW-before-merge) / defer" and omits the proposal's "A (+ P) + M".
5. "34 fixture files" (`D-PEC-106_RULING_2026-09-27.md:14`, `docs/STATUS.md:278`) counts the test module as a fixture. The register row's breakdown is exact.
6. `docs/STATUS.md:276` says "with a later REVIEW and owner re-acceptance (RR1)". Adding that RR1 is intent only and needs its own authorization would match the ruling.
7. When the D1 act lands, RV1 should change from PLANNED to BLOCKED, naming the owner's REVIEW authorization. The graph adopted that rule at `:107`.
8. `WORK_GRAPH.md:168` names the S1A branch, which exists only locally, not on origin.

Relevant files:
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-105_RULING_2026-09-27.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-106_RULING_2026-09-27.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md

These paths are in the reviewed branch at `b23d0276b`, not in this worktree's checkout.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (RV1 against the graph's scope and completion): repaired.** RV1 now reads CARRIED. It sits beyond this undertaking and does not gate C1, because it needs a separate owner REVIEW authorization and the owner's own acceptance act, which the scope line leaves outside this graph. The scope line and the completion line now name RV1 and the CARRIED state. The central receipt will name RV1's next home, and there it waits BLOCKED on that authorization (note 7). The Order and next-work lines match.
- **NB-2 (stale notice-triage line): repaired.** It now lists this undertaking's lifecycle acts (`D-PEC-98` and `D-PEC-103` add-on S, and `D-PEC-106` add-on L), says the RV1 REVIEW is carried, and records that `D-PEC-105` discloses the frozen-surface consequence.
- **NB-3 (D-PEC-106 base-drift paragraph): repaired.** It now separates what is on `origin/main` from the D1 ruling in this PR and the unpushed S1 act, and it reads "an X1".
- **NB-4 (S1 state): repaired.** The S1 row, the Order line and STATUS now say its act is in progress.
- **Note 1: repaired.** "Until a later owner act (RR1 records the intended route)."
- **Note 2: no change.** The re-resolution and the basis-note correction are incorporated by reference.
- **Note 3: repaired.** The D-PEC-105 ruling and the M1 receipt list now record that, with P, DEL-00-01's SELF_CHECK SOW basis describes superseded bytes.
- **Note 4: repaired.** The register row now lists "A (+ P) + M".
- **Note 5: repaired.** The D-PEC-106 ruling states what "34 fixture files" counts.
- **Note 6: repaired.** STATUS now says RR1 is intent only and needs its own authorization.
- **Note 7: adopted.** See NB-1.
- **Note 8: repaired.** The unmerged-work line says the S1 act is on a local, unpushed branch.

The repair head needs a fresh review before merge.
