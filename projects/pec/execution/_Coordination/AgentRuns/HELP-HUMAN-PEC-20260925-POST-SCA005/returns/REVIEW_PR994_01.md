# Review 01 of PR #994, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `33050cef3f466e90ec940f36aeb98739d4749039`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `ba1e8851a9dea950858d0c1d6f94f6c5f9b669c67cba1474a8599edf2d6909eb`.

## Report (verbatim)

## PR #994 review: head `33050cef3f466e90ec940f36aeb98739d4749039`, branch `claude/pec-d102-ruling`

**Verdict: PASS WITH NOTES.** Nothing blocks. There are 3 NON-BLOCKING findings and 5 NOTES. The first three findings are graph-record fixes of the same kind that earlier reviews repaired.

I read everything with `git archive` exports under my own scratchpad directories and deleted them afterwards. I made no edits, no git writes and no checkout.

### What I verified
- **Byte identity.** The published proposal and the prep-folder draft both hash to `baf178125e37ea8d82735f0bd4c0913531188ca9daffd95309339eb82fffcfdd`; `cmp` shows them identical. The draft on `origin/main` has the same hash.
- **Act script and prep folder.**
  - `apply_s4p.py` hashes to `2b6792fe…4869`.
  - `shasum -a 256 -c SHA256SUMS`: all 107 entries OK.
- **Verdict counts.**
  - In-run verdicts: 01 and 02 FAIL, 03 to 07 PASS WITH NOTES.
  - `REVIEW_PR990_01` and `_02` are PASS WITH NOTES; `_03` is PASS.
  - `REVIEW_PR992_01` and `_02` are PASS WITH NOTES; `_03` is PASS.
  - The ruling, the register row and the graph all state these correctly.
- **PR facts.**
  - PR #990 merged as `5a305bc04`.
  - PR #992 merged as `6c6cc1b00`.
  - The D-PEC-102 reservation came from PR #989. It is correct.
- **Base drift paragraph** (ruling L65–70) is true.
  - Since `d385b6a19`, only four things touched the repo: Piping (PRs #983, #991, #993), PR #990 (prep folder, one brief and returns only), and PR #992.
  - PR #992 wrote DEL-08-06 and DEL-10-13 files, the `SOW_INIT_K2` run root and AgentRuns records. It also changed `README.md` and `docs/STATUS.md`, which count as HELP_HUMAN's D-PEC-88 records.
  - I ran `apply_s4p.py --check-only` from a copy against exports of `origin/main` `4087a4f8c` and of the PR head. Both print "CHECK preflight passed; planned write set 8 modifies". So no S4 target or pin has moved.
- **Faithfulness.**
  - Q1 (A), 3a/3b, M and the default models match the proposal's question text (L187–200) and add-on M (L37–58), with nothing added.
  - The Grant repeats the proposal's grant (one run, VERIFY TASK, M at M1, no re-pin).
  - The Limits section is an "including" subset of the proposal's limits.
  - The status line and table follow the D-PEC-100 and D-PEC-103 format.
- **D-PEC-100 notice facts.**
  - DEL-02-07's `_REVIEW.md` records `ACCEPT_EXACT_BYTES` for `d044499a…2559`.
  - DEL-01-06's `_REVIEW.md` records an accepted successor `5fdcfd96…2fa8`.
  - Both hashes are the D-PEC-100 preimages (proposal L119, L124).
  - The D-PEC-100 proposal says nothing about acceptance or `_REVIEW`.
  - Verdict 06 L42 is the source of the DEL-02-07 point.
- **Register row** (`_REGISTER.md:119`) replaces the reservation row in place. The row order and the house style are right.
- **Branches.**
  - `claude/pec-d1-premise-proposal` (`73e47d956`, brief D1P, provisional D-PEC-105) is on origin.
  - `claude/pec-x1-fixtures-proposal` (`3f41666bb`, brief X1P, provisional D-PEC-106) is on origin.
  - `claude/pec-s1-sow-currency-proposal` is on origin and has PR #986 open.
- **Containment.** Exactly the five named paths changed. `git diff --check origin/main...33050cef3` is clean, and the merge-base is current `origin/main` `4087a4f8c`.
- **CI** on the head: `pec`, `harness`, `Harness pre-merge`, `Select source/PEC/App coverage` and `Desktop E2E (source mode)` passed; the others were skipped. `mergeStateStatus` is CLEAN.
- **Local checks** on a full export of the head:
  - `validate_pec_loop_receipts.py`: VALID, exit 0.
  - `validate_decomposition_registers.py --strict`: 0 errors, 26 warnings.
  - `harness.py self-check` could not run on the export, because it needs a git work tree. CI covers it.

### NON-BLOCKING
1. **The K3 hold cites the wrong item, and the row contradicts itself** (`WORK_GRAPH.md:71`; the PR body repeats the citation).
   - The new text says the profile entry needs the tool's exact shape, "which DEL-08-06's production defines (its TBD-007)".
   - DEL-08-06 TBD-007 says the opposite: "The content of the tier-0 profile entry … is the K3 act's (CLM-013)."
   - The items that leave the shape to production or other owners are TBD-003 (tool-definition representation), TBD-004 (exact operations and parameters, fixed by the API schema owners) and TBD-006 (fallback-signal representation). They do support the hold.
   - The same row's Inputs cell still says K3 "follows DEL-08-06's first Scope of Work, which fixes the tool's shape (plan §B6)". That contradicts the new status cell.
   - SCA-006 `Propagation_Plan.md` §B6 "When" sets a window: after the first Scope of Work fixes the shape, and before any tool is declared. Holding K3 later stays inside that window, but it is HELP_HUMAN's sequencing choice, not a §B6 requirement. The row should say so and cite TBD-003/004/006.
   - The hold does not decide CON-002. CON-002 itself allows the question to be settled "at the K3 act or in the production packet".
2. **The M1 row does not list D-PEC-102 add-on M** (`WORK_GRAPH.md:76`).
   - The row lists add-on M for D-PEC-98, D-PEC-100 and D-PEC-103, but not the eight S4 `MEMORY.md` files that ruling L47 assigns to M1. Only the S4 row mentions them ("Add-on M at M1").
   - Reviews repaired the same omission twice before: PR #971 review 01 (`a45706f99`) and PR #989 review 01 (`5f184fb24`).
3. **The Order section is stale** (`WORK_GRAPH.md:87`).
   - "Ready now: packet preparation for S1, S4 and D1" no longer holds: the S4 packet is merged and ruled, and S4 is ACTIVE with the act next.
   - There is no Order bullet for "S4 ruled; act next; add-on M at M1".
   - The PR edited line 85 next to it. The same "graph Order lines" repair was made at PR #989.

### NOTES
1. **Q1 lapse wording** (ruling L44). "Lapses on its own terms" is accurate, since the review record says any byte change invalidates the acceptance. The lapse actually takes effect when the act lands (proposal L97), and "when the act lands" would make that explicit. The register row matches Q1's own wording ("lets … lapse").
2. **Q2 wording** (ruling L45). The ruling drops Q2's "as tabled". "Exact documentary wording … at their named loci only" still keeps the limit, so this is not an enlargement.
3. **Register row compresses the Part B gates.** "Part B items for DEL-04-01/02/03 carried verbatim with gates" combines two states. The DEL-04-01 gates still bind. The DEL-04-02 and DEL-04-03 documentary-correction gates are met by this ruling, for the tabled texts only (proposal L186). The phrase is literally true, because the gate lines are quoted in AX-014 and AX-013.
4. **D-PEC-100 notice framing is accurate and non-enlarging** (ruling L18, L50–55).
   - It is labelled "a record, not a new owner act" and grants nothing. It does not change the status line, and the graph's owner-direction line labels it as part of the presentation.
   - "Any new review … is left to when those deliverables' production is taken up" is HELP_HUMAN's stated disposition, as the notice put it. It is not an owner decision, and it opens or closes no review.
5. **The central-receipt record is still to come** (`WORK_GRAPH.md:158`). The graph says the lapse "is recorded here and in the central receipt", but no receipt exists yet. Carry it into the receipt at M1.

### Relevant paths (at the PR head)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-102_RULING_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-102_s4_sow_currency_proposal_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (L119)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` (L71, L76, L85–88, L154–162)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md` (L261–265)
- Basis for finding 1:
  - `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Propagation_Plan.md` (§B6, L321–339)
  - `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md` (TBD-003/004/006/007 at L133–137; CON-002 at L181)

These paths are as they read at the PR head. The worktree itself is checked out on the S1 branch.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (K3 hold cites TBD-007; the row contradicts itself): repaired.**
  - The K3 row's Inputs cell now states the plan §B6 window: after the first Scope of Work fixes the shape, and before any tool surface is declared or invoked.
  - The status cell cites DEL-08-06 TBD-003, TBD-004 and TBD-006 as what leaves the exact shape to production and other owners.
  - It labels the hold as HELP_HUMAN's sequencing choice within that window, not a §B6 requirement.
  - It says TBD-007 (the profile content) belongs to the K3 act, and that the hold decides neither TBD-007 nor CON-002.
  - The PR body is corrected to match.
- **NB-2 (M1 row missing D-PEC-102 add-on M): repaired.** M1 now names the eight S4 `MEMORY.md` files. It also says the receipt records the `D-PEC-100` and `D-PEC-102` acceptance lapses and DEL-10-13's C-08 classification, which covers Note 5.
- **NB-3 (Order section stale): repaired.** The Order section now records the S4 packet as done and ruled, with its act next and M at M1. It lists S1 (presented after the S4 act), D1 and X1 as in preparation. The stale X1 "Ready now" line is removed.
- **Note 1: repaired.** Question 1's resolution now says the DEL-04-01 acceptance lapses "when the act lands".
- **Notes 2, 3 and 4: no change.** The reviewer found them accurate and non-enlarging.
- **Note 5: carried to M1**, as NB-2 records.

The repair head needs a fresh review before merge.
