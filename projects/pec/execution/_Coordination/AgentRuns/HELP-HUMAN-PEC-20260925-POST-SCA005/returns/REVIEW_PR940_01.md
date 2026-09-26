# Review 01 of PR #940 (owner directions 2026-09-26), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `c0a668181592d2f149b8a9740730b6f25392b5c8`.
- **SHA-256 of the report text below (UTF-8):** `e0b51505775dc8c2ce747c1e172f7d5fba263666cecb51dd8206c6dc0cabc30e`.

## Report (verbatim)

## Review of PR #940 at head `c0a668181592d2f149b8a9740730b6f25392b5c8`

**Verdict: CHANGES REQUESTED.** There are 3 blocking findings, each cheap to fix. The quotes, hashes, line references, register and Decision_Log shape, and hygiene all check out. Nothing is applied and nothing prompts about CHECKING.

I confirmed the head with `gh pr view 940`: `headRefOid` is `c0a668181…`. The merge-base equals `origin/main` `8f9bd314c`. The PR is one commit touching 8 files (+112/−14). I read the files from a fresh `git archive` into `/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T/tmp.z47k8j62R3`. The checkout was not modified: `git status` is empty.

### Blocking findings

**B1. RS1 contradicts the graph's own scope statement and `projects/pec/AGENTS.md`.**
- **Where:** `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
  - L74 (the new RS1 node) against L21, which is unchanged. L21 lists "retiring the `## Remaining` sections" under "Left for later, not in this graph".
  - L10 says the graph completes only when every node is COMPLETE or removed by the owner.
- **Evidence:**
  - RS1's completion check is "Owner rules the retirement packet; sections retired with no open item lost". That makes the retirement itself part of this undertaking.
  - Live `projects/pec/AGENTS.md` L249–250 makes retiring the sections "a separate owner-directed undertaking". RS1's own "Needs" cell cites that.
  - As written, this undertaking cannot reach F1 until the Remaining sections are retired or the owner removes RS1. That quietly enlarges the undertaking.
- **Fix, either of:**
  - (a) Drop RS1 as a node. Record the open owner question in the Next work list and the Order section instead.
  - (b) Reframe RS1 as "Owner decision whether to open a separate retirement undertaking". Its completion check becomes "decision recorded (and, if opened, the new undertaking's graph named)". Update L21 to match.

**B2. The amendment's interpretation hands an owner-shaped choice to the drafter, and one sentence contradicts "not retired".**
- **Where:** `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md` L20.
- **Evidence:**
  - L20 says the replacement text "also states the status of the existing sections until any retirement, including whether their gate markers still bind". WORKING_ITEMS drafts that text.
  - Live AGENTS.md L245 says "A Remaining item's own gate markers still bind that item". Dropping or changing that changes a fence. Neither owner quote speaks to existing gate markers, and project AGENTS.md sends owner-shaped decisions to the owner.
  - The only safeguard is that the hunk is "shown to the owner". Per the accepted plan (§A4) and the SCA-005 precedent, the application PR merges during checkpoint-3 preparation, before the owner accepts checkpoint 3. So agent-drafted live instruction text could land with no owner approval, only display.
  - L20 also says "PEC keeps no `## Remaining` sections going forward". L21 of the same file, and the D-PEC-96 record L33, say the 57 sections are not retired. Those statements cannot both hold.
- **Fix:**
  - Bound the interim status to the status quo: existing sections and their gate markers still bind, and are updated only under a packet, until any retirement ruling. Alternatively, put the gate-marker question to the owner explicitly.
  - Say whether the hunk needs the owner's explicit approval before the application PR merges, or only display. Approval is recommended.
  - Change "keeps no `## Remaining` sections going forward" to "adds no new `## Remaining` sections or entries".

**B3. The graph's recovery section contradicts the node states.**
- **Where:** `WORK_GRAPH.md`
  - L65 (G1 is `ACTIVE`, "The preparer is revising the draft") against L135 ("G1: the preparer handed back revision 3, now merged; nothing is running").
  - L82 ("S3's `D-PEC-98` draft is active") and L127: the S3 row (L63) still reads plain "READY — packet preparation". "Active operations and ownership" (L132–136) lists no D-PEC-98 drafter.
- **Evidence:**
  - Either a G1 revision-4 preparer and a D-PEC-98 drafter are running, in which case the recovery section is false, or they are not, in which case `ACTIVE` and "active" are false.
  - No brief exists for either in `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/`.
  - `D-PEC-98` appears nowhere else in `projects/pec` (`git grep`). The number is used before any register row exists.
- **Fix:**
  - List the actual running operations under L132–136, with their briefs and actors, or correct the states.
  - Align the S3 row with L82.
  - Avoid fixing a D-PEC number before its proposal and register row exist, or label it provisional.

### Non-blocking findings

1. **The Lane C verification rule is only implied.** The accepted plan's C1 item 2 asserts that each written file equals its planned postimage, and A4 step 1 writes the selected candidate (`49ce993a…`). The amendment changes that postimage but amends neither step explicitly. It relies on "Every other byte of the accepted candidate stays as accepted" and "The verifier checks it" (DECISION.md L20).
   - "Opens only the correction above" (L24) also sits awkwardly beside L26, where the manifest and notices "record the correction". Those texts are fixed drafts: manifest draft `852b1d5b…` and notices §6.3.
   - Suggest stating the rule outright: applied AGENTS.md equals `49ce993a…` with slots filled, except the one approved hunk, plus the named additions to the manifest and notices.
2. **"Any sentence that directly restates it" is an open bound** (DECISION.md L20). Name the lines. Candidate L330 ("Item D's selection only from deliverable `## Remaining` surfaces…") is not a restatement. Also note that `docs/STATUS.md` L132–133 ("the sections remain as records") will go stale after application and is outside A4.
3. **Stale graph lines:**
   - L103 still says adopting the revision "is an open choice for the owner".
   - L124 still reads "The owner's `D-PEC-96` ruling (presented 2026-09-25/26…)". It is superseded by L126.
   - L146's unresolved consequence still reads "Owner ruling" on revision 3.
   - L106 mixes tenses: "It is put to the owner before R3 is dispatched" followed by "The owner chose…".
4. **The checked basis is stale** (L122, `971ca68a1`). `origin/main` is now `8f9bd314c` (PRs #936–#939). Three PEC notices merged since then and are not triaged: `execution/_Coordination/NOTICE_2026-09-26_DECOMP_RULINGS_D-GOV-47.md`, `…_DEPENDENCY_SCHEMA_D-GOV-46.md` and `…_REVIEW_SPEC34_REVERSAL.md`. D-GOV-46 bears on K1, and the review/CHECKING notice bears on R3's review. The triage at L97 claims completeness for five notices only.
5. **STATUS owner gates** (`docs/STATUS.md` L229–246) do not list the new RS1 owner question, if RS1 stays as an owner gate.
6. **Decision_Log row order** (L29–31): CP3-EDITION (3), then G2-A1 ("2 (amendment)"), then CP3. This is cosmetic.
7. **Amendment folder shape:** the folder has only `DECISION.md`, while the SCA-005 group-1 amendments also carry `ACCEPTED_MANIFEST.csv` and `Handoff_State.md`. That is acceptable because no new bytes are accepted and the package `Handoff_State.md` is appended instead, but worth a sentence.
8. **The D-PEC-96 register row** (L113) keeps its revision-3 Decision text (`remaining-loop`, `remaining-items`) with the amend note appended. That is acceptable as history. The amend record's effect table covers Q2 and Q3; the direction also effectively answers Q4 (a smaller vocabulary), which could be noted.
9. **Reading of "those":** HELP_HUMAN reads the first quote's "those" as the Remaining sections, where the literal antecedent is `remaining-items`. The second act's "yes, ride checkpoint 3" endorses the recommendation, so the reading is supported. It rests on HELP_HUMAN's account of the chat, which the record labels correctly.

### What I verified

**Quotes.** Both are verbatim, with the double spaces, checked with `grep -F` on the exact strings:
- Q1 appears in 4 files: the D-PEC-96 amend record, the amendment `DECISION.md`, `Decision_Log.md` and `WORK_GRAPH.md`.
- Q2 appears in 5 files: those 4 plus `_REGISTER.md`.
- The partial quotes ("SCA-006 pinned", "yes, ride checkpoint 3") are exact substrings.

**Interpretation.**
- **Amend direction, no ruling claimed.** The amend record explicitly says it is not a ruling. The register row stays `PROPOSAL / AWAITING_RULING`.
- **Revision 3 is on main.** `D-PEC-96` revision 3 on `origin/main` hashes `2f7d9875…afc4`.
- **Pinned-edition hashes:**
  - `contract.md` `4453a719…4d02` and `method.md` `34187e83…67f5` are the blob at `9b005c23a` (2026-09-09) and at `4d5f7b911`. Both were revised at `09c299ac0`/`0d7d5da61`/`4dcc2c6a8`, and HEAD has `74793f04…`/`fd3fe525…`.
  - `WORKFLOW.md` `58f5d1d5…7a90` is unchanged since `9b005c23a`.
  - All three match SCA-006 `Brief.md` L152–154.
- **The 57 sections are not retired.** 57 live `PKG-*/1_Working/DEL-*/_STATUS.md` files carry `## Remaining`. No `_STATUS.md` is in the diff, and live AGENTS.md is unchanged.
- **AGENTS.md hashes and lines:**
  - Live AGENTS.md is `c9d3b44d…197a` at both HEAD and `origin/main`, and its paragraph is exactly L241–250.
  - The candidate `CP2_CANDIDATE/AGENTS.candidate.md` hashes `49ce993a…070d`, matching `ACCEPTED_MANIFEST.csv`, and its paragraph is exactly L261–270.
- **Group-2 snapshot untouched.** `SCA-006_GROUP-2_2026-09-25/` is not in the diff.

**Decision_Log.**
- The 2 new rows have 5 cells each. The table has 14 rows, all 5 cells.
- The file ends with a newline, and the new section is appended.
- The front-matter status is still true.

**Pointer, handoff and register rows.**
- `Handoff_State.md` and `SCA-006_GROUP-2_AUTHORIZED.md` change by additions only.
- In `_REGISTER.md`, rows D-PEC-90 to D-PEC-97 all have 6 cells, and the header has 6. D-PEC-96 is still `PROPOSAL / AWAITING_RULING`. D-PEC-97's Opens column is unchanged.

**WORK_GRAPH.md.**
- **Vocabulary:** all states come from the template's vocabulary (`workflows/construct-local-work-graph/resources/work-graph-template.md` L36–37).
- **RS1:** it is `BLOCKED` and names its decision, and its premise matches AGENTS.md L249–250. The scope conflict is B1.
- **Acyclic:** the dependencies are acyclic, and RS1 has no edges.
- **Review-02 nits:** nit 1 is addressed (K1 check, L69). Nit 2 is reworded (L106), with the residual tense issue in non-blocking 3.
- **D-PEC-88 trace:** the "Eighth PR" entry (L171) names the STATUS change, and `README.md` is not touched.
- **Tables:** the Work table is 5 cells throughout.

**STATUS.** It is accurate on the pinned edition and the revision-4 direction, provided the PR merges.

**Hygiene and checks.**
- `git diff --check origin/main...HEAD`: exit 0.
- `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check`: exit 0. The only REVIEW findings are the same 4 pre-existing ones in `_DomainEngines`, and none of its findings touches a changed path.
- `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .`: exit 0 (VALID).
- The reliance-hold preflight (`candidate-validation`) returns ALLOW for all 8 changed paths.
- No `v2/**`, PRD, decomposition, `_STATUS.md`, SOW or live AGENTS.md byte changed.

### Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-96_AMEND_DIRECTION_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Decision_Log.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_GROUP-2_AUTHORIZED.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/AGENTS.md (live, L241–250)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/AGENTS.candidate.md (L261–270)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Propagation_Plan.md (§A4 L218–234, §C1 L380–390)

## HELP_HUMAN disposition

The verdict was CHANGES REQUESTED, with three blocking findings. All are repaired in the next commit, and the reviewer re-checks the repair.

| Finding | Repair |
|---|---|
| B1 | Option (b): RS1 is now only the owner's decision whether to open a separate retirement undertaking. Its completion check is "decision recorded; if opened, the new undertaking's graph is named". The "left for later" line says the same. |
| B2 | The amendment bounds the replacement to candidate L261–270. The existing sections keep their status quo: they stay in place, their gate markers still bind, and they are updated only under a packet, until any retirement ruling. The owner's **explicit approval** of the exact hunk is required before the application PR merges. "Keeps no" becomes "adds no new … sections or entries". The pointer, Decision_Log row, register row, package handoff and brief B6 match. |
| B3 | "Active operations and ownership" lists the G1 revision-4 preparer and the S3 drafter with their briefs. The S3 row is ACTIVE. `D-PEC-98` is labelled provisional. The S3 brief is committed. |
| 1, 2 | The amendment gains a §"Verification rule" for `AGENTS.md`, the manifest and the notices. The replaced lines are named. The `docs/STATUS.md` consequence is noted. |
| 3 | The stale graph lines are fixed. |
| 4 | The basis is `8f9bd314c`. The three later Root notices (D-GOV-46, D-GOV-47, and the review/SPEC §3.4 reversal) are triaged. |
| 5 | The STATUS owner-gates list names the RS1 decision. |
| 6 | The Decision_Log rows are reordered: G2-A1, CP3-EDITION, CP3. |
| 7 | The amendment has a sentence on its folder shape. |
| 8 | The amend record notes that the direction answers question 4's vocabulary part. |
| 9 | No change. The reading rests on HELP_HUMAN's labelled account. |
