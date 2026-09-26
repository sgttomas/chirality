# Review 01 of PR #921 (D-PEC-95 publication and work-graph update), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `2e6767e2f26069dec1bfcea1d0ebe5291159aed9`. This file is the only addition after that head.
- **SHA-256 of the report text below (UTF-8):** `47fdbe4466be6ca26132dba761311be9c9d16f05e15e1989798c49cf0e521f74`.

## Report (verbatim)

## Review of PR #921: D-PEC-95 proposal and work-graph update

**Verdict: PASS.** I found no blocking findings. There are ten non-blocking findings. The first two bear on the owner's ruling and should reach the owner when the packet is presented.

**What I reviewed:**
- PR head `2e6767e2f26069dec1bfcea1d0ebe5291159aed9`, confirmed with `gh pr view 921`. Base `bec8bdd65`.
- The checkout is unmodified: `git status` is clean and HEAD is unchanged. I worked in my own scratchpad, using `git archive` exports of `bec8bdd65`, `13df8b795` and HEAD plus two `--shared` scratch clones. That scratch has since been deleted.
- The proposal's basis is `13df8b795`. `git diff 13df8b795 bec8bdd65` touches none of the 121 targets, none of the 3 basis files, and neither Task Management register, so every preimage in the grant still holds on current main.

## Blocking findings
None.

## Non-blocking findings (ranked)

**1. DEP-10-05-004 conflicts with the packet's own verifier criterion.**
- **Where:** `D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md` L400 (verifier item 4: "at least as well as the old one (note DEP-10-05-004)"), against finding 2 at L168 and the table row at L120.
- **Evidence:** the `Deliverables.csv` DEL-10-05 Description at base reads in full: "Owner use or non-use logging … falsification evidence; manual Step 0 remains available and no PEC read/write duty is created. Split from DEL-10-12…". It never names orientation.
  - The new quote is verbatim, but it does not support the row's Statement ("Orientation reads are a logged consultation surface") or its DEL-04-01 target.
  - The recommended A + R therefore knowingly includes a row that fails the verifier's literal test. "(note …)" does not say how the verifier should treat it.
  - The refreshed `Notes` prefix ("SCA-003 revision 1.3: DEL-10-05 description re-expressed…") does not record that the warrant is weaker, so a later reader sees a row that looks freshly verified.
- **Fix:** do not edit the hash-bound proposal. In the owner presentation, name DEP-10-05-004 explicitly as a choice:
  - accept it as prepared, and the ruling states that verifier item 4 records the row but does not fail it; or
  - take the "amend" path and move its evidence to SOW-085.

  The graph's carry-forward note (WORK_GRAPH L84–86) already records it; that part is fine.

**2. RUN_SUMMARY.md is not an "accumulating" record under the checkpoint-3 manifest.**
- **Where:** proposal L41.
- **Evidence:** group-3 `ACCEPTED_MANIFEST.csv` gives `Handoff_State.md` the boundary "Context; updated additively by this act", but gives `RUN_SUMMARY.md` "Context at presentation" (at `e3480b78…`).
- **What does hold:** HELP_HUMAN did already append a checkpoint-3 outcome section to `RUN_SUMMARY.md` (now `e9a0224e…`), so appending has precedent.
- **Why it matters:** it bears on question 1 (A versus P).
- **Fix:** tell the owner in the presentation.

**3. Work-graph node states use a word the template does not have.**
- **Where:** `WORK_GRAPH.md` L53–55 and L68.
- **Evidence:** N1–N3 and T1 are marked `PROPOSED`. `workflows/construct-local-work-graph/resources/work-graph-template.md` L36 allows only PLANNED, READY, ACTIVE, BLOCKED, UNCERTAIN and COMPLETE.
- **Fix:** `BLOCKED — awaiting owner ruling on D-PEC-95` (T1: on question 2).

**4. The graph's Order list still uses the old membership rule.**
- **Where:** `WORK_GRAPH.md` L76: "Their membership excludes the R1 affected set."
- **Evidence:** the repaired S1 and S2 rows (review-02 NB2) now use "the latest SCA-006 affected-SOW list (R1's, replaced by R2's…)".
- **Fix:** align L76.

**5. The register row names only option A's path set.**
- **Where:** `_REGISTER.md` L112: "Opens exactly the 121 product paths … (option A; …)".
- **Fix:** add "(119 under P)". Otherwise the row matches the D-PEC-93 precedent format and its hashes are correct.

**6. Self-descriptions inside the hash-bound files disagree with the packet.** Disclose these; do not fix them, because the bytes are pinned.
- `gen_d95.py` L35 calls add-on R "not recommended by default", while the proposal recommends A + R.
- The `verify_d95.py` usage docstring (L4) omits `--retired-covers`.
- `t1_tm_pec_023.py` has no local-date check on `--act-date`, unlike the generator.

**7. The B1 quote hides a wrong count.**
- **Where:** proposal L14.
- **Evidence:** the quoted plan text reads "Re-pin … the … `_CONTEXT.md` files". The elided word is "40" (Propagation_Plan L802). The correct figure is 42 (checkpoint-3 audit COV-072, the plan-count defect).
- **Why it is only minor:** the proposal uses 42 everywhere, and finding 4 names the defect.

**8. Two basis records have changed since the proposal's basis commit.** The proposal labels both as read "at 13df8b795", so this is historical, not false, but the owner reads the proposal on current main.
- **D-PEC-94:** the proposal cites `eb9793aa…5e81` (L12, L509). At base it is `b6814e90…`, because PR #919 appended to it.
- **PR #919:** the proposal (L3, L12) describes it as not yet on `origin/main`. It is now merged.
- The H9 transcription (return L11–13) covers only the generator's preimages.
- **Fix:** mention this in the owner presentation.

**9. The published SHA256SUMS does not fully verify in its folder.**
- **Where:** `SHA256SUMS` line 1 lists `./D-PEC-95_DRAFT.md`, which is not in the folder. In the folder, `shasum -c` gives 40 OK and 1 missing.
- **Why it is only minor:** this is disclosed at return L10. The draft's hash equals the published proposal's.
- **Also in the transcribed report:** L24 says the draft is "522 lines"; the file is 524. The transcription is verbatim, so this is the preparer's own miscount.

**10. The B4 brief record is incomplete.**
- **Where:** `briefs/B4_SCA006_CHECKPOINT1.md`. Its bytes are correct and its hash `87612aca…` matches review 02.
- **Gap:** the two SendMessage addenda to the SCA-006 manager are not recorded anywhere in the repository: the 01:12:47Z message, and the S4/DEL-04-01 correction per the review-02 disposition. Both are part of R1's supplied basis.
- **Fix:** record them next to the brief, or in the graph.

## What I verified, and how

**1. Truthfulness.**
- **Populations, recounted at base:**
  - 66 contexts. Exactly 42 carry the revision-1.4 tail; 24 already name 1.5 (22 A2 mirrors plus DEL-02-08/09).
  - 64 of 66 references name 1.4.
  - Registers: 66 registers, 263 rows (ANCHOR 140 = 132 active + 8 retired; EXECUTION 123 = 111 active + 12 retired).
  - ACTIVE EXECUTION quotes verbatim: 92/111. The 19 misses equal COV-072's list exactly. RETIRED EXECUTION: 7 non-verbatim.
- **Lifecycle counts, from each `_STATUS.md`:**
  - The 64 touched folders: 28 OPEN, 26 INITIALIZED, 4 CHECKING (00-01, 00-03, 08-02, 10-01), 2 IN_PROGRESS (01-03, 01-05), 4 RETIRED.
  - The 42 contexts: 20 / 16 / 4 / 2.
- **Pointer and handoff staleness:** confirmed at base in `_Decomposition/_LATEST.md` (BLOCKERS 2/6/74), `_ScopeChange/_LATEST.md` (FROZEN / IN_PROGRESS / BLOCKED), `_COORDINATION.md` L15–21 and L182–184, and items 12 and 13. The D-PEC-93 run root now holds MANIFEST.md, VALIDATION.md and HANDOFF_STATE.md.
- **Owner quotes:** verbatim, including the double space in "accept your  read" (checked with `od -c`), "CP2: …", "CP3: accept; Q1 a", "D-PEC-93: A." and the D-PEC-94 sentence.
- **Hashes:** I recomputed every cited basis hash at `13df8b795`. All match, including the work graph at `87f6bfe30` (`f669ebe5…`).
- **SCA-005 cause IDs:** A-02, 12, 16, 33, 37, 38 and 75 exist in `Amendment_Actions_CP2.csv` (`7bb3bada…`). The two "stale before SCA-005" causes are confirmed against `f22cfcc76` (PEC-API-002) and `42e291db1` (DEL-10-05).

**2. Generator.**
- **Runs on my export of `bec8bdd65`:**
  - A, A + R and P each exited 0.
  - The reports are byte-identical to `evidence/genA.tsv`, `genAR.tsv` and `genP.tsv`, including the aggregates (A `946646dd…`, A + R `282450fc…`, P `f0b9f726…`) and `CHECK active_execution_quotes_verbatim 111 111`.
  - All 121 grant-table postimages match, as do the P `_COORDINATION.md` hash and the four A + R hashes.
  - The git diff from my scratch clone is byte-identical to `evidence/optionA_vs_13df8b795.diff`, and containment equals `G_changed.txt`.
- **Edits confined:**
  - each context changes 1 line into 2;
  - each reference changes 2 lines; the 4 retired ones change 3 under R;
  - registers change 19 rows, in `EvidenceQuote`, `LastSeen` and `Notes` only.
- **Fails closed:**
  - a rerun exits 1 for A, A + R and P ("preimage mismatch");
  - a wrong date exits 1 and writes nothing (the tree matched base afterwards);
  - a malformed date exits 1;
  - `--reproduction` at 2026-09-26 gives 15 differing files, and only `Handoff_State.md` still differs after swapping the date (the derived hash).
- **Rebuild:** `build_gen_d95.py` rebuilds `gen_d95.py` byte for byte from the template on the base export (`0e9ede50…`).
- **Validators on base, A, A + R and P:**
  - strict registers: exit 0, 0 errors / 0 warnings, identical output, equal to `evidence/base_strict.out`;
  - closure: `closure_summary.json` is `bd73806c…` in all four (111 edges, 66 nodes, 0 SCCs, 6 isolated);
  - schema validator: VALID ×10;
  - `verify_d95.py`: A, A + R and P exit 0 with output identical to the evidence; self-comparison exits 1, and a mismatched R flag exits 1.
- **Reliance holds:** `pec_reliance_hold.py … exact-correction-preparation` returned ALLOW on all 123 targets.
- **Harness:** `harness.py self-check` output is identical at base, after option A and at head.

**3. N3.**
- The proposal's before/after table equals the base and post cells exactly for all 19 rows.
- Each new quote is a substring of its cited locus (PRD PEC-RCN-002 and PEC-API-002 rows; `Deliverables.csv` and `ScopeLedger.csv` cells).
- Each `Notes` value equals the stated prefix plus the old Notes. `LastSeen` went from 2026-07-25 to the act date; every other field is unchanged.
- No `_DEPENDENCIES.md` mirrors the old quotes.
- 18 rows keep their warrant. DEP-10-05-004 is weaker; see finding 1.

**4. Add-on R.**
- The DEL-06-04, 07-02, 07-04 and 07-05 `CoversScopeItems` cells are blank, SOW-029/035/037/087 are `OUT` ("**Deferred**"), and the A2 contexts say "(none — retired under SCA-005)". R is accurate.
- The other 62 references' "covers" lines match the register, so R is complete.
- It is correctly presented as beyond the brief (proposal finding 1, question 1, and "A alone stays inside it").

**5. T1.**
- `task-management` contract L11 ("Promotion and disposition are human acts. WORKING_ITEMS applies the exact recorded decision…") and K-TM-3 ("the owner triage session is the sole disposition authority") are correctly applied. Question 2 is the right owner question.
- The objective selections at base match amendment 1 (rows 1, 2, 3, 5, 8, 9; rows 4, 6, 7 moot).
- On my scratch clone:
  - `t1_tm_pec_023.py` produced `62f897ab…`;
  - `taskmgmt validate` passed on both registers (10/15), then `archive` ran, then validate passed again (9/16);
  - final hashes `634641f0…` and `3c1349ba…`;
  - a rerun exited 1;
  - the diff is byte-identical to `evidence/T1_vs_13df8b795.diff`.

**6. Grant, rollback and limits.** They are complete and exact.
- There is no grant for a lifecycle, SOW, PRD, `v2/**` or `_Decomposition` register change.
- The revert PR restores 121 or 119 preimages, plus both registers if T1 rode along.
- Every CHECKING mention in the added text is a disclaimer or a count; none prompts the owner.

**7. Owner questions.**
- Questions 1–4 are genuinely the owner's, and the A + R recommendation is well-founded, subject to findings 1 and 2.
- Question 5 (model steer) is optional; agents could decide it.

**8. Publication.**
- The proposal SHA-256 is `9137d387…4b22`. It is byte-identical (`cmp`) to the preparer's surviving `scratchpad/h9/D-PEC-95_DRAFT.md`, and `diff -r` shows the published folder equals `h9/` except the draft and the added `.gitattributes`.
- `.gitattributes` is the only added file beyond the preparer's set.
- The H9 transcription hash `78a55321…` reproduces over return lines 19–119, UTF-8, without the final newline.
- The brief hash is `02fb7370…`.

**9. Work graph and STATUS.**
- **Review-02 fixes:** NB1–NB7 are applied: the S4 §8 list, the membership rule, DEL-04-01 as a fixed member, R1's path basis (D-PEC-90 grant item 3 quote verified), "Candidate" basis for T1, the D-PEC-95 number reserved, S3/X1 dependencies, and the STATUS wrap. L76 lags; see finding 4.
- **S4 list:** my grep of all 32 `ScopeOfWork.md` files found:
  - PEC-K-03: DEL-04-01, 04-02, 08-01, 08-03;
  - verify-before-rely: DEL-04-01, 04-02, 08-01;
  - genuine PRD §8: DEL-01-05 (L66), 04-02, 08-01, 08-03 (L229), 08-04;
  - SOFTWARE_DECOMP §8 only: DEL-01-01, 02-03, 04-03.

  This equals the corrected S4 text.
- **Graph:** acyclic. Other states are truthful: PR #919 merged as `7562c4434`, PR #920 touched no `projects/pec` path, and the SCA-006 worktree is on `claude/pec-sca006-cp1-package`.
- **D-PEC-88 trace:** complete. Both STATUS hunks are named, and README is unchanged.
- **STATUS:** the new text is true.

**10. Hygiene** (scratch clone at head, `PYTHONDONTWRITEBYTECODE=1`).
- `git diff --check bec8bdd65...HEAD`: clean.
- `validate_pec_loop_receipts.py --repo-root .`: VALID, exit 0.
- `validate_decomposition_registers.py --strict projects/pec/execution`: 0 / 0, exit 0.
- PR #921 CI: harness, pec, Harness pre-merge, Desktop E2E and the three Select coverage jobs pass; the rest are skipped.

## Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_CURRENCY_D95_PREP_2026-09-25/ (gen_d95.py, verify_d95.py, t1_tm_pec_023.py, SHA256SUMS, evidence/)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/H9_D95_CURRENCY_PROPOSAL.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/B4_SCA006_CHECKPOINT1.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md

## HELP_HUMAN disposition

The verdict is PASS, with no blocking findings, so the PR merges at the reviewed content with this file added.

- **Findings 1, 2 and 8** go to the owner with the `D-PEC-95` presentation:
  - finding 1: DEP-10-05-004 as an explicit choice;
  - finding 2: `RUN_SUMMARY.md`'s checkpoint-3 boundary, which bears on option A versus P;
  - finding 8: basis records that changed after `13df8b795`.
- **Findings 3, 4, 5 and 7** are fixed in the next graph update, which gets its own review:
  - node states become `BLOCKED — awaiting owner ruling`;
  - the Order line uses the latest-list membership rule;
  - the register row gains "(119 under P)";
  - the B1 plan count is noted.
- **Findings 6 and 9** are disclosed and not fixed. The generator, verifier and T1 script bytes are pinned by the proposal, and `SHA256SUMS` is the preparer's list.
- **Finding 10** is recorded here. These are the two addenda HELP_HUMAN sent to the SCA-006 checkpoint-1 manager, which are part of R1's supplied basis. Both were sent through the host's SendMessage on 2026-09-25 (session date). Verbatim:

### B4 addendum 1

This is a brief addendum from HELP_HUMAN to B4 (SCA-006 CP1). The Impact_Assessment must enumerate the affected Scope of Work population explicitly, deliverable by deliverable, instead of saying "where affected". The work graph now gates its SOW batch S4 on exactly that set.

Evidence (grep at `13df8b795`/`5570fd095`):
- SOWs quoting PEC-K-03 or verify-before-rely:
  - DEL-04-01;
  - DEL-04-02 (CLM-016, L225);
  - DEL-08-01 (CLM-004, L92, which also paraphrases the PRD §8 access classes);
  - DEL-08-03 (REQ-005, L256).
- SOWs citing PRD §8 in some form: DEL-01-01, DEL-01-05, DEL-02-03, DEL-04-02, DEL-04-03, DEL-08-01, DEL-08-04.
- DEL-01-06's SOW quotes neither K-03 nor §8. Classify it on its own evidence.

For each candidate, classify it `AFFECTED` or `NOT_AFFECTED`, citing the SOW line and the PRD text SCA-006 would change. Read-only within your existing write boundary; nothing else in your brief changes.

### B4 addendum 2

This corrects part of the PRD §8 candidate list in HELP_HUMAN's earlier addendum to B4 (SCA-006 CP1). A re-review found that three of the "citing PRD §8" hits cite `SOFTWARE_DECOMP.md` §8 (Context Budget QA), not PRD §8:
- DEL-01-01 `ScopeOfWork.md` L90 (CLM-007);
- DEL-02-03 L104 (CLM-007);
- DEL-04-03 L146 (CLM-006).

Classify them on their actual text; they are expected to be NOT_AFFECTED.

The genuine PRD §8 references are:
- DEL-01-05 L66;
- DEL-04-02 L363;
- DEL-08-01 (CLM-004 L92);
- DEL-08-03 L229 (CLM-009);
- DEL-08-04 L274.

The K-03 / verify-before-rely set is unchanged: DEL-04-01, DEL-04-02, DEL-08-01 and DEL-08-03.

DEL-04-01 is a fixed member of the affected set: the D-PEC-90 proposal L64 names its CLM-016/AX-007 as a locus, and D-PEC-90 grant item 1 forbids rebuilding it around verify-before-rely.

Nothing else in your brief changes.
