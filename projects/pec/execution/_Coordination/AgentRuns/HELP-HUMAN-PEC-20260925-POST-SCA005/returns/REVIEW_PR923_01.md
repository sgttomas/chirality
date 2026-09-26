# Review 01 of PR #923 (D-PEC-95 ruling record and work-graph update), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `df8acf4f555cd889a173851da57ee125f3507de6`.
- **SHA-256 of the report text below (UTF-8):** `57856217d8092492a76acdade8042a50ffbba4cccd7898143ccff663a6108fe6`.

## Report (verbatim)

## Review of PR #923 (D-PEC-95 ruling record, register row, work graph, STATUS/README)

**Verdict: PASS.** There are no blocking findings and eight non-blocking findings. I recommend fixing finding 1 before merge. It is a one-line change, and the pinned T1 script will otherwise write a cross-reference that points at the wrong question.

**Basis:**
- Head `df8acf4f555cd889a173851da57ee125f3507de6`, confirmed with `gh pr view 923`. Base `origin/main` `b1145955e`.
- I did not modify the checkout: `git status` is clean and HEAD is unchanged.
- Prototypes ran on a `git archive` export of `b1145955e` in my session scratchpad, which I have since deleted.
- Local date is 2026-09-25, so I did not need `--reproduction`.

### Blocking findings
None.

### Non-blocking findings (ranked)

**1. The ruling's question numbers do not match the proposal's, and the pinned T1 note cites the proposal's number.**
- **Where:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-95_RULING_2026-09-25.md` L14–23 and L37–46. The table heading is "Resolution of the proposal's owner questions".
- **Evidence:**
  - The proposal (L447–453) has five questions: 1 option, 2 T1, 3 re-audit, 4 Notes line, 5 models.
  - The ruling uses the six-question numbering of HELP_HUMAN's chat message, which inserts DEP-10-05-004 as question 2.
  - The pinned `t1_tm_pec_023.py` (`0e0cd6f9…7bec`) L36 writes into the Task Management row: "confirmed in the D-PEC-95 ruling (question 2)". In this ruling, question 2 is DEP-10-05-004; TM-PEC-023 is question 3.
  - Reading "include" as the Notes line and "defaults" as models is correct in substance. They are the proposal's questions 4 and 5.
- **Fix:**
  - Retitle the table as the presentation's questions.
  - Add one line mapping them to the proposal: presentation 1→1, 3→2, 4→3, 5→4, 6→5, and presentation 2 is the review-01 finding 1 choice.
  - State that the T1 note's "(question 2)" means proposal question 2.

**2. The work graph's S4 row contradicts itself on DEL-04-03.**
- **Where:** `WORK_GRAPH.md` L64.
- **Evidence:** the new sentence correctly mirrors `Impact_Assessment.md` §7.1 (L325–331):
  - proposed S4 is DEL-04-01, 04-02, 08-01, 08-03, 08-04 and 04-03;
  - DEL-03-04, 10-03 and 00-03 are at review level;
  - DEL-01-01, 01-05, 02-03 and 01-06 are NOT_AFFECTED.

  But the retained parenthetical still says DEL-04-03 is "expected NOT_AFFECTED". §7.1 L298 classes it AFFECTED (scope growth).
- **Fix:** drop DEL-04-03 from that parenthetical, or mark the parenthetical as the pre-R1 expectation.

**3. The graph misstates where the helpers are hashed.**
- **Where:** `WORK_GRAPH.md` L104: "its scratch helpers are hashed in the SCA-006 `Handoff_State.md`".
- **Evidence:** `Handoff_State.md` L88–100 only names `gen_actions.py`, `check_csv.py` and `showlines.py`. It says they are in the manager's scratchpad and not in the repository, and gives no hashes. The B4 return does not hash them either.
- **Fix:** replace "hashed" with "named (not hashed; not in the repository)".

**4. The register row still leads with 121 paths.**
- **Where:** `_REGISTER.md` L112.
- **Evidence:**
  - The row says "Opens exactly the 121 product paths … under option A (119 under P …)", but the ruled option opens 119.
  - There is a punctuation slip: "nodes N1–N3 and T1.; owner".
  - The Decision cell still says N1 brings "the SCA-005 handoff records" current. Under P those files stay byte-identical, though the notes column does say "SCA-005 snapshot files untouched".
- **What is correct:** 6 columns, the same as every other row (checked mechanically); the status format matches D-PEC-93; both hashes are correct.
- **Fix:** lead with "Opens exactly 119 product paths (option P: the grant table's 121 less the two SCA-005 snapshot files; add-on R changes 4 postimages)".

**5. "register-content" in the limits could be misread.**
- **Where:** ruling L102–104 and the register notes.
- **Evidence:** "no … decomposition-text, register-content … change" can be read as barring any register content change. N3 does change `Dependencies.csv` cells. The proposal's limit (L434) means `_Decomposition` register content.
- **Why it is only minor:** the ruling says "All D-PEC-95 limits apply unchanged", so the proposal still governs.
- **Fix:** write "decomposition text or decomposition-register content".

**6. Some graph text is stale under P + R.**
- **L36** (deliverable-scope row): N1 still lists the "SCA-005 handoff".
- **L54** (N2):
  - it says "semantic fields untouched", but R rewrites the "covers" bullet in 4 files. Its own state cell says so.
  - "generator re-prepared against the current tree" is done.
- **L54–55:** N2 and N3 still name "(TASK under HELP_HUMAN)" as owner. N1, U1 and the proposal's administrative grant (L408) name WORKING_ITEMS.

**7. One STATUS sentence implies an act that will never happen.**
- **Where:** `docs/STATUS.md` L210–214, in the same present-current paragraph.
- **Evidence:** it says the SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` "still describe the pre-setup audit state … updating them needs its own act". Under the P ruling those two files stay byte-identical permanently. `_COORDINATION.md` item 14 records them as superseded; I checked this in the rendered postimage.
- **Fix:** under D-PEC-88, qualify the sentence.

**8. Minor traceability gaps.**
- **Completed-work table:** unlike the PR #919 row, it does not record that REVIEW_PR921_01 findings 3, 4, 5 and 7 are repaired in this third PR. The repairs are present:
  - no PROPOSED state remains;
  - L76 uses the latest-list rule;
  - the register has "(119 under P)";
  - L87 notes the "40" count.
- **Unverifiable:** the review-01 disposition said finding 8 (changed basis records) would go to the owner. The ruling's summary of the chat presentation does not mention it. I cannot see the chat.
- **Ambiguous wording:** ruling L100–101 ("run … from the run root") could be read as the working directory. The proposal (L339–342) says the generator is copied into the run root and run from the repository root with `--repo`.

### What I verified

**1. Ruling record**
- **Quote:** the owner's words are byte-identical in the ruling (L9), the register and the graph (L117). The apostrophe is ASCII, with no U+2019.
- **Hashes (shasum -a 256):**
  - proposal `9137d387…4b22`, generator `0e9ede50…be78` and T1 script `0e0cd6f9…7bec` match;
  - SCA-005 `Handoff_State.md` `a86ae910…328a` and `RUN_SUMMARY.md` `e9a0224e…e518` match the hashes the P postimage writes into item 14;
  - SCA-006 `Impact_Assessment.md` is `93253b7d…b691`, as the graph cites.
- **P + R is within the proposal:**
  - the command line allows `[--retired-covers] [--option P]`;
  - `verify_d95.py` accepts `--option P --retired-covers`;
  - the limits cover R's four bullets.
- **P + R run:** `git diff 13df8b795 b1145955e` touches none of the 124 pinned files. On the `b1145955e` export, `gen_d95.py --option P --retired-covers --check-only --act-date 2026-09-25` gave:
  - exit 0, `AGGREGATE option=P+R files=119`, `CHECK active_execution_quotes_verbatim 111 111`;
  - a path set equal to `genP.tsv`'s;
  - 115 postimages equal to `evidence/genP.tsv` and 4 equal to `evidence/genAR.tsv` (the retired DEL-06-04, 07-02, 07-04 and 07-05 `_REFERENCES.md`), with none untabled;
  - preimages equal to P's.
- **Applied run:** a real P + R run on a clone, followed by `verify_d95.py … --option P --retired-covers`, exited 0 with every check PASS, and both SCA-005 files were unchanged.
- **Postimage content:** `_COORDINATION.md` item 14 and the Notes line render as the ruling states.
- **Question readings:**
  - "P+R (don't append)": correct;
  - DEP-10-05-004: matches review-01 finding 1's offered choice;
  - TM-PEC-023: matches K-TM-3;
  - "no re-audit", "include" and "defaults": match proposal questions 3, 4 and 5 (see finding 1).
- **Grant and limits:** nothing is enlarged; the proposal is incorporated "without enlargement".
- **Format:** follows `D-PEC-93_RULING_2026-09-25.md`, including the status line and all sections.

**2. Register row:** 6 columns, the same as the header and rows D-PEC-90..94.

**3. Work graph**
- **States:** only READY, BLOCKED and PLANNED are used. READY for N1–N3, U1 and T1 becomes true at merge, since the ruling lands together with the graph.
- **Acyclic:** the dependency chain is U1/R1 → S1–S3, R3 → S4, D1, I1 and X1, G1 → S2(DEL-01-06), then C1 → M1 → F1.
- **Checked against the diff and Git history:**
  - PR #921 merged as `325629882` and PR #922 as `b1145955e`;
  - the SCA-006 package is unchanged from verdict-03's candidate `0aa65beef` to `b1145955e`;
  - verdict 03 is PASS, with 54 actions ("54 PROPOSED" in `Decision_Log.md`) and 32 SOWs, 9 AFFECTED (§7.1 L317);
  - the D-PEC-88 trace names both STATUS hunks and the README hunk.

**4. STATUS and README:** the changed lines are true. The SCA-006 checkpoint-1 decision is `AWAITING_OWNER`, and the act has not run. The one stale sentence is finding 7.

**5. Containment:** the diff touches only `execution/_Coordination/**` (default-writable), plus `docs/STATUS.md` and `README.md` under D-PEC-88. No product path is written. The only CHECKING mentions are disclaimers or pre-existing text, and no grant is enlarged.

**6. Hygiene**
- `git diff --check origin/main...HEAD`: clean.
- `validate_pec_loop_receipts.py --repo-root .`: VALID, exit 0.
- `validate_decomposition_registers.py --strict projects/pec/execution`: 0 errors / 0 warnings, exit 0.
- `harness.py self-check`: exit 0.
- PR #923 CI: harness, pec, Harness pre-merge, Desktop E2E and the three Select coverage jobs pass; the rest are skipped.

### Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-95_RULING_2026-09-25.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/README.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_CURRENCY_D95_PREP_2026-09-25/t1_tm_pec_023.py
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Impact_Assessment.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md

## HELP_HUMAN disposition

The verdict is PASS, with no blocking findings. All eight non-blocking findings are repaired in commit `145c93622`, and the reviewer re-checks that commit.

| Finding | Repair |
|---|---|
| 1 | The ruling's table is retitled for the presentation's questions and maps them to the proposal's numbering. It states that the T1 note's "(question 2)" means proposal question 2. |
| 2 | The S4 parenthetical now says checkpoint 1 classes DEL-04-03 AFFECTED for scope growth. |
| 3 | The helpers are "named … (not hashed, and not in the repository)". |
| 4 | The register row leads with 119 paths as ruled, the punctuation is fixed, and the N1 Decision wording is qualified for option A. |
| 5 | The limits say "decomposition-register-content", and the ruling notes that N3's 19 rows are within the grant. |
| 6 | The graph's deliverable-scope N1 row and the N2/N3 rows are current under P + R, with WORKING_ITEMS as owner. |
| 7 | The STATUS sentence is qualified under D-PEC-88 and traced in the graph. |
| 8 | The completed-work row records the review-01 repairs. The ruling records the presentation's basis note (finding 8), and its grant states how the generator is run. |
