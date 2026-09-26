# Review 02 of PR #940 (repair re-review), transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 01 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `a07f62190fbb57971e5ed732533885755cb78428`.
- **SHA-256 of the report text below (UTF-8):** `a4b97ff650706f1a2076c58d3dd1a58d092ca7eec8cb0d4864bbb883fe4cef70`.

## Report (verbatim)

## Re-review of PR #940 at head `a07f62190fbb57971e5ed732533885755cb78428`

**Verdict: CHANGES REQUESTED, on one missed line.** B1, B2 (apart from that line) and B3 are properly repaired. The transcription is faithful and hygiene passes. The one blocking item is a single stale phrase in the work graph's R3 row that repeats the B2 defect.

`gh pr view 940` gives head `a07f62190…`. It is one commit after `c0a668181` and touches 11 files (+437/−23). I read the files from a fresh `git archive` in `/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T/tmp.xGKNZcyOGE`. I made no edits. Note that someone else moved the checkout's HEAD to `a07f62190`; I did not. It is clean.

### Blocking finding

**R1. The R3 row still says "shown".** In `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` L59, R3's state ends "…and its exact hunk is shown to the owner before the application PR merges".
- The amendment now says "The owner's explicit approval of the exact hunk text is required… Display alone is not enough" (`SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md` L20).
- The other five records agree with the amendment: L131 of the same graph, the Decision_Log row SCA006-G2-A1, the D-PEC-97 register row, `SCA-006_GROUP-2_AUTHORIZED.md` and `Handoff_State.md`. Brief B6 at L62, L150 and L159 does too.
- R3 is the node that dispatches checkpoint 3, so its wording should match.
- **Fix:** replace "is shown to the owner" with "needs the owner's explicit approval".

### Non-blocking findings

1. **The D-GOV-47 triage overstates.** Graph L81 says "the OUT and TBD rows are unchanged". In the candidate `ScopeLedger.csv`, SOW-080 (TBD) changes its `ScopeItemStatement` and `DecisionRef`. The convention itself holds: 74 IN, 18 OUT and 8 TBD; every IN row has a package, every OUT and TBD row has a blank `PackageID`, and SOW-097 to SOW-100 are IN with PKG-04, PKG-08, PKG-08 and PKG-10. Suggest "the OUT and TBD rows keep a blank `PackageID`".
2. **The review/CHECKING notice triage (L82) leaves out one PEC-specific item.** The notice says `DEL-08-02` entered CHECKING under the D-PEC-74 override with no frozen SHA or checking basis. It also says a later review will surface that.
   - The triage also misses how the notice meets D1. D1 amends the DEL-00-03 SPEC while DEL-00-03 is in CHECKING, and the new rule checks that frozen claim surfaces are unchanged since the frozen SHA.
   - Record both as consequences held for D1 or a later review, with no owner prompt. The present text correctly makes no CHECKING prompt.
3. **"PEC does not read them" sits oddly beside "each item's gate markers still bind".** This appears in amendment L20, brief B6 L57–58 and the amend record L29.
   - If "PEC" means agents working in the project, the two statements conflict. If it means the coordination-plane product or its feed profiles, they don't.
   - The owner's "no need to scan for them" was about the registry profile. The hunk should say which is meant, for example "no PEC feed profile reads them".
   - The explicit-approval gate covers this, so it is not blocking.
4. **The STATUS correction lands in the application PR but is outside its containment list.** The amendment's "Known consequence outside A4" has HELP_HUMAN correct `docs/STATUS.md` under D-PEC-88 in the same PR. Brief B6's C1 allowlist does not include STATUS, and its verifier is not told to expect that file. Tell the verifier, or C1 will flag it.
5. **Brief B6 moves the notice writes to the checkpoint-3 manager.** Brief B6 A4.5 delegates the notice-file writes from HELP_HUMAN to WORKING_ITEMS, while plan §A4.3 assigns them to HELP_HUMAN.
   - HELP_HUMAN still reviews them, so this is arguably an ordinary method choice within the grant.
   - It is a change of actor from the accepted plan and should be named as such, for example in the Decision_Log or the graph.
6. **The S3 brief's basis is stale.**
   - It fixes the number ("The number is `D-PEC-98`.", L13) where the graph labels it provisional.
   - It points the drafter at `D-PEC-96` revision 3 (L24), which includes `remaining-items` and `remaining-loop`, both dropped by the owner's direction.
   - On receipt, reconcile the draft with revision 4. Also check that its PRD §7.1 "remaining items" reading carries no Remaining-reading dependency.
7. **One minor gap in the graph.** G1's revision-4 preparer has no committed brief of its own; it runs from the G1 brief plus the direction record. That is disclosed at L139, so this is acceptable.

### What I verified

**B1: repaired.**
- RS1 (L74) is "Owner decision: open a separate undertaking…?". It is a decision record only, and its completion check is "Decision recorded; if opened, the new undertaking's graph is named". It is BLOCKED and names the decision.
- L21 now matches it, and so does AGENTS.md L249–250.
- RS1 has no edges, and the graph stays acyclic.

**B2: repaired apart from R1.** The amendment L20:
- names the paragraph at candidate L261–270 (live L241–250) and "no other line";
- keeps the status quo: the sections stay in place, gate markers bind, and they are updated only under a packet;
- keeps the separate-undertaking sentence and uses "adds no new … sections or entries";
- requires explicit approval, saying "Display alone is not enough".

Its §"Verification rule" is sound:
- It amends plan §A4 step 1 and C1 item 2 for `AGENTS.md` only.
- The applied file must equal `49ce993a…` with slots filled, except the one hunk.
- The manifest (draft `852b1d5b…`) and the three notices each gain only a named addition.

The folder-shape sentence was added. The pointer, Decision_Log row, D-PEC-97 register row, package handoff and brief B6 are consistent with it:
- B6 A4.2, C1, the verifier, the owner question, Publication ("Do not merge") and Limits all match;
- B6 preconditions require amendment 1 on `origin/main`;
- B6's pinned hashes match Git (`4453a719…`, `34187e83…`, `58f5d1d5…`, unchanged since `9b005c23a`/`4d5f7b911`).

**B3: repaired.**
- The S3 row is ACTIVE, with the brief and "provisional".
- The Order section lists Active G1 and S3, Ready R3 and S1–S2, and Blocked RS1.
- "Active operations" lists the G1 revision-4 preparer and the S3 TASK, and they agree with the node states.
- In the graph, `D-PEC-98` appears only as provisional. It has no register row.
- Brief hashes: `S3_FIRST_SOWS_PROPOSAL.md` is `ef12b740…a537a` and `B6_SCA006_CHECKPOINT3.md` is `52d98c5e…e366`, both as stated.

**Earlier non-blocking findings 1–8.**
- The stale lines are fixed: L103, L106 and L146, and the old L124 was removed.
- The checked basis is `8f9bd314c`, which is correct.
- The D-GOV-46 triage matches its notice: new files use the amended schema, which applies to K1.
- STATUS lists RS1.
- The Decision_Log rows are reordered.
- The amend record adds Question 4.

**STATUS** (L229–250) is true.

**Transcription.** The block between "## Report (verbatim)" and "## HELP_HUMAN disposition", stripped, is 13,123 characters. Its SHA-256 is `e0b51505…c30e`, equal to the recorded value, and it matches my report as I sent it. Each disposition row describes what the commit did, and none overclaims.

**Quotes.** Both are still verbatim, with the double spaces. Q1 appears in 5 files and Q2 in 6, now including brief B6 and the review file.

**Tables.** The Decision_Log has 14 rows, all 5 cells, with an EOF newline. The register rows all have 6 cells. The graph's Work table has 5 cells throughout. Every changed file ends with a newline.

**Hygiene.**
- `git diff --check origin/main...a07f62190`: exit 0.
- `harness.py self-check`: exit 0, with the same 4 pre-existing REVIEW findings and none on a changed path.
- `validate_pec_loop_receipts.py --repo-root .`: exit 0 (VALID).
- The reliance-hold preflight (`candidate-validation`) returns ALLOW for all 11 changed paths.
- No `AGENTS.md`, PRD, decomposition, `_STATUS.md`, SOW or `v2/**` byte changed.
- Nothing prompts about CHECKING, and B6 and S3 both forbid it.

### Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md (L59, L81, L82)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/B6_SCA006_CHECKPOINT3.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S3_FIRST_SOWS_PROPOSAL.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR940_01.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/_Decomposition/ScopeLedger.csv (SOW-080)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md

## HELP_HUMAN disposition

The verdict was CHANGES REQUESTED on R1. It is repaired in the next commit, with the non-blocking findings.

- **R1:** R3's state now reads "needs the owner's explicit approval".
- **Finding 1:** the D-GOV-47 triage now says "keeps a blank `PackageID`", and notes the SOW-080 change.
- **Finding 2:** the review-notice triage records the DEL-08-02 and D1/DEL-00-03 points as consequences held for D1 or a later review, with no owner prompt.
- **Finding 3:** "PEC does not read them" becomes "no PEC feed profile reads them, so the coordination plane does not scan them", in the amendment, the amend record and brief B6.
- **Finding 4:** brief B6's C1 now tells the manager that HELP_HUMAN may add a STATUS commit and notice edits after its verification.
- **Finding 5:** the graph names the notice-write actor change.
- **Finding 6:** the S3 drafter was told that the number is provisional and to reconcile with D-PEC-96 revision 4.
- **Finding 7:** no change.

Brief B6 is re-committed at `8bdc7181…df4`.
