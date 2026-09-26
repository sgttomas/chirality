# Review 01 of PR #925 (D-PEC-95 act recorded complete), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `0401c6bc1b8fa9fc6f0415c536873d923ef3f340`. This file is the only addition after that head.
- **SHA-256 of the report text below (UTF-8):** `5b7b6c431c0f1645ae41f75c2907c5644f569b7b1c971728fc2012a1c2a54cb6`.

## Report (verbatim)

## Review of PR #925 (`claude/pec-graph-u1-complete`, head `0401c6bc1b8fa9fc6f0415c536873d923ef3f340`)

**Verdict: PASS.** I found no blocking findings. Every factual claim in the PR matches `origin/main` `abfd0897b`. The findings below are non-blocking.

I confirmed the PR with `gh pr view 925`: head `0401c6bc1…` (OPEN), base `main`, merge-base `abfd0897b`, 5 files changed. I read the trees from `git archive` exports into my scratchpad, `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/r925.M4cl/{main,head}`. I made no edits to the checkout, and `git status` is clean.

### Blocking findings
None.

### Non-blocking findings (most important first)

1. **A false present-tense statement in `projects/pec/docs/STATUS.md` L63–65, outside the edited paragraphs.** This PR did not introduce it: it dates from commit `9d4d19205`.
   - It reads "The objective fields and the SOW-037 / DEL-07-04 status change only when SCA-005 applies; today SOW-037 is still `IN` and DEL-07-04 still `OPEN`."
   - SCA-005 has applied. `ScopeLedger.csv` L38 has SOW-037 as `OUT`. `Deliverables.csv` L42 and the DEL-07-04 `_STATUS.md` both have DEL-07-04 as `RETIRED`.
   - It sits in the Current-state "Implementation" paragraph, which is under D-PEC-88 maintenance.
   - Fix: rewrite it in past tense (the fields changed when SCA-005 applied; SOW-037 is `OUT` and DEL-07-04 is `RETIRED`), here or in the next PR, and add it to the D-PEC-88 trace.

2. **`projects/pec/README.md` L38–42 reads as self-contradictory.** It says "Current SCA-004 derivative state is recorded in …HANDOFF_STATE.md: incomplete only for TM-PEC-023, which was closed `RESOLVED_BY_DECISION` under `D-PEC-95`…"
   - The record's text is quoted accurately. But "Current … incomplete" next to "which was closed" invites a wrong reading.
   - Suggest: "The SCA-004 closeout (…HANDOFF_STATE.md) recorded derivative state as incomplete only for TM-PEC-023, which was closed … on 2026-09-25 under `D-PEC-95`."

3. **The WORK_GRAPH "Deliverable scope" table still shows the state before the act.**
   - L36 says "The pointers still carry the pre-setup audit reading; `_COORDINATION.md` names revision 1.4".
   - L37 says the contexts and references are "Pinned to revision 1.4".
   - L44 has TM-PEC-023 as "OPEN".
   - This can be read as the baseline at graph construction. But the graph is the one current account, and the Work table now says COMPLETE. Suggest relabelling the column as the baseline, or updating it.

4. **Small inconsistencies in how G1 READY is justified.** All nodes use only the six template states, and the graph is acyclic. G1 has no unmet predecessor node, so READY for read-only packet preparation is defensible. However:
   - The Approach prose at L14–15 ("Then SOW currency … Then the registry source packet") still orders G1 after SOW currency. The Order section (L76, L79) puts G1 first ("Ready now", and "After G1: DEL-01-06 in S2").
   - The G1 note at L65 cites "SCA-006 checkpoint 1 classes DEL-01-06 NOT_AFFECTED". That matches Impact_Assessment L304/L331, but the package is unaccepted (R1 is BLOCKED). "Proposes … (unaccepted)" would be more exact.
   - S2's Needs cell (L62) does not name R1, but the Order section (L78) gates S2 on R1. S1 and S3 do name R1. This was already the case before this PR, but it matters more now that U1 is done.

5. **The SCA-006 baseline caveat (WORK_GRAPH L96) is accurate, with two nuances.**
   - Verified:
     - `Pre_Change_Coverage.json` is byte-identical to the POSTSETUP `coverage_summary.json` (`b7b432a2…128d`).
     - It still carries context pins 1.5:24 / 1.4:42, references 1.4:64 / 1.5:2, and 19 non-verbatim quotes.
     - COV-068/069/072/073 are in the POSTSETUP `Decomp_Coverage_IssueLog.csv` at L69/70/73/74.
   - Nuance 1: Impact_Assessment §2.1 (L96–101) claims the audited state is "the current pre-change state byte for byte". Since D-PEC-95 changed 116 `execution/PKG-*` files, that is no longer true. The caveat implies this without saying it; R2 should say it explicitly.
   - Nuance 2: most of these findings will be *resolved* at R3 rather than re-reported. The real risk is attributing their resolution, and the context/reference/quote diffs, to SCA-006. COV-073-type stale-handoff findings may reappear, because under P the SCA-005 handoff files stay stale.
   - It may be worth mentioning the §2.1 drift to the owner alongside the pending R1 decision.

6. **WORK_GRAPH L102, "It was presented 2026-09-25", cannot be checked from the repository.** It refers to a chat act. Consider pointing to a record or labelling it as HELP_HUMAN's account.

7. **Brief `U1_D95_CURRENCY_ACT.md` L74, "No … register-content … change", is looser than the ruling.**
   - The ruling (L120) and the register row say "decomposition-register-content".
   - Read literally, the brief's wording conflicts with N3 (19 `Dependencies.csv` rows) and T1 (the Task Management registers).
   - The brief's bytes are pinned as supplied (hash matches), so it should not be edited. A one-line note in the graph or the return would clear it up.

8. **Nit: inconsistent follow-through on historical paragraphs.** README L105–106 appends the TM-PEC-023 closure to its historical paragraph. The matching STATUS sentence at L188–189 ("TM-PEC-023 is carried into SCA-005 intake as described above") was not annotated. It is not false, because "above" now leads to the closure.

### What I verified

**1. Truth against `origin/main` `abfd0897b`.**
- **Merge chain:** `abfd0897b` has parents `590ec52c1` and `cbfa14ee9` (PR #924). `590ec52c1` is PR #923 and `b1145955e` is PR #922.
- **Revision 1.5 re-pin:** 66 `_CONTEXT.md` and 66 `_REFERENCES.md` files.
  - All 132 contain "revision 1.5".
  - The last revision named in every context is 1.5.
  - Every reference names "(revision 1.5, accepted `current_basis`; SCA-005 successor)".
- **Evidence quotes:** my own scan finds 111/111 ACTIVE EXECUTION quotes verbatim, using the same rule as `gen_d95.py` L795–809.
  - Row counts: ANCHOR/ACTIVE 132, EXECUTION/RETIRED 12, ANCHOR/RETIRED 8.
  - The closure recompute gives `closure_summary.json` `bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a`, which matches.
- **Task Management:** the live register has 9 rows (8 `OPEN`, 1 `DEFERRED`) and the archive 16 `CLOSED`. TM-PEC-023 is in `REGISTER_CLOSED.csv` as `CLOSED` / `RESOLVED_BY_DECISION`, closed 2026-09-25. `taskmgmt validate` passes on both registers (9 and 16 rows).
- **Pointers and `_COORDINATION.md`:**
  - `_Decomposition/_LATEST.md` and `_ScopeChange/_LATEST.md` both describe the post-setup state (`COV_SCA005_POSTSETUP`, D-PEC-95 re-pin, MetadataAlignment `COMPLETE`).
  - `_COORDINATION.md` item 14 (L173–197) and its Notes line are current.
- **SCA-005 handoff files:** `Handoff_State.md` is `a86ae910…328a` and `RUN_SUMMARY.md` is `e9a0224e…e518`. Both equal the hashes item 14 records, and `git diff 590ec52c1 abfd0897b` over the SCA-005 folder is empty.
- **Run root and verdicts:**
  - `CURRENCY_REV15_D95_2026-09-25/` exists.
  - `VERIFIER_VERDICT_01.md` and `_02.md` both conclude "PASS WITH NOTES" with no blocking finding.
  - Commits after verdict 02 (`5caaf4b94..cbfa14ee9`) touched only the run root and the return.
- **Postimages:** my recompute confirms 115 files equal `genP.tsv` postimages, 4 equal `genAR.tsv`, and 0 mismatch.
- **Containment of PR #924:** 116 `PKG-*` files (42 contexts, 64 references, 10 `Dependencies.csv`), plus 2 `_LATEST.md` and `_COORDINATION.md`, is 119. Add 2 Task Management registers, 66 run-root files and 1 return: 188 in total, with nothing outside `projects/pec`.
- **Pinned hashes:** proposal `9137d387…4b22`, ruling `51dceb71…4beb`, and `gen_d95.py`, `verify_d95.py` and `t1_tm_pec_023.py` (in both the prep folder and the run root) all match what the text names.

**2. Graph.**
- The six template states are used as defined (`workflows/construct-local-work-graph/resources/work-graph-template.md` L36).
- Edges from Order and Needs (U1/R1 → S1–S3, G1 → S2, R1 → R2 → R3 → R4, R3 → S4/D1/I1, S2/S3 → X1, then C1 → M1 → F1) contain no cycle.
- Order (L75–82) and Current state (L100–110) agree.
- "Fourth PR" is correct: the graph's earlier PRs are #919, #921 and #923.
- The D-PEC-88 trace (L129) covers both STATUS hunks and all three README hunks.

**3. STATUS and README.** I checked the edited paragraphs line by line (STATUS L163–169 and L205–239; README L23–60 and L91–106). Apart from findings 1, 2 and 8, the statements are true.
- Lifecycle census 30/26/4/2/4 matches `lifecycle_distribution`.
- The Open list matches graph nodes S1–S4, D1, G1, X1, I1 and R1–R3.
- The nested-list Markdown is well formed.

**4. Brief hash.** `shasum -a 256` gives `6cdf4c63cdc8c993319dd069db6938c701b4d619da5985a8918811a03986553e`, as expected. It also matches the hash in the U1 return (L146).

**5. Register row.** The D-PEC-95 row (L112) has 6 columns (8 `|`-separated fields). Status stays `RULED P + R / EFFECTIVE ON MERGE`, as the D-PEC-93 precedent does. The appended facts are accurate, and the relative run-root path resolves. The only other row with an odd column count is D-PEC-22, which this PR does not touch.

**6. Containment and limits.**
- Diff paths: 3 files under `_Coordination/**`, plus `docs/STATUS.md` and `README.md` under D-PEC-88. No product, `v2/**`, SOW or register-content path is written.
- CHECKING appears only in the brief's prohibition ("Do not ask the owner about CHECKING") and in the graph's statement that nothing prompts for it.
- The reliance-hold preflight (`candidate-validation`) returns ALLOW for all 5 changed files.

**7. Hygiene** (run in the checkout with `PYTHONDONTWRITEBYTECODE=1`).
- `git diff --check origin/main...HEAD`: exit 0, no output.
- `validate_pec_loop_receipts.py --repo-root .`: exit 0, "frozen through Receipt-166; versioned receipt contract satisfied".
- `validate_decomposition_registers.py --strict projects/pec/execution`: exit 0, 0 errors / 0 warnings.
- `harness.py self-check`: exit 0.

### Relevant paths
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/README.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/U1_D95_CURRENCY_ACT.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Impact_Assessment.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/

## HELP_HUMAN disposition

PASS, with no blocking findings. The PR merges at the reviewed content with this file added.

- **Findings 1, 2, 3, 4, 6 and 8** are corrected in the graph's next update, which gets its own review:
  - finding 1: the STATUS SOW-037 / DEL-07-04 sentence;
  - finding 2: the README SCA-004 sentence;
  - finding 3: the deliverable-scope column, labelled as the baseline or updated;
  - finding 4: the G1 approach prose, "proposes (unaccepted)", and R1 in S2's needs;
  - finding 6: the presentation labelled as HELP_HUMAN's account;
  - finding 8: the STATUS historical annotation.
- **Finding 5:** the SCA-006 §2.1 drift is recorded for R2. HELP_HUMAN tells the owner alongside the pending checkpoint-1 decision.
- **Finding 7:** the brief's bytes stay pinned. Its "register-content" means decomposition-register content, as the ruling and register row state. N3's 19 `Dependencies.csv` rows and T1's registers are within the ruling's grant.
