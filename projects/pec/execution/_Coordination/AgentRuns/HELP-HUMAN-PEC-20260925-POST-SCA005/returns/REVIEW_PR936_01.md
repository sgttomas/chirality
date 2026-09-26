# Review 01 of PR #936 (SCA-006 checkpoint-2 acceptance record; graph update), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `89cf8c7fe0c57fc799b0366527104de4ada21b98`.
- **SHA-256 of the report text below (UTF-8):** `103cc8c4ac7db4adb18535f94541efec0da4d91fde095a8f56140acb8ded939d`.

## Report (verbatim)

## Review of PR #936 (`claude/pec-graph-cp2-d96`, head `89cf8c7fe0c57fc799b0366527104de4ada21b98`, base `origin/main` `971ca68a1`)

**Verdict: FAIL.** There are four blocking findings, and each is a short text fix. The core of the acceptance record is sound:
- the owner quote is verbatim everywhere it appears;
- all 16 manifest hashes match `origin/main`;
- the Lane A path list is exact, and Lane B is excluded;
- nothing is applied, and the validators pass.

The four blockers are one misstatement about slot dates in the packet itself, and three places where a record is no longer true now that checkpoint 2 is accepted. Two of them are the same kinds of problem that failed PR #926.

`gh pr view 936` confirms head `89cf8c7fe…` (OPEN, base `main`). The merge base equals `origin/main` `971ca68a1`. The diff has 10 files. I made no edits to the checkout, and `git status --porcelain` is empty.

### Blocking findings

**B1. `DECISION.md` says the `AGENTS.md` hash stands as listed, but that file's date slot is an application-date slot.**
- **Where:** `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md` L37, the Q-CP2-A row: "…so the adopted PRD and `AGENTS.md` hashes stand as listed."
- **What is right:** the PRD slots S1–S4 bind to "date of the owner's checkpoint-group-2 acceptance" (`PRD_V2_4_SUCCESSOR_DIFF.md` §6). So the PRD hash `ae49b806…` and the folder token do stand. This matches the SCA-005 wording.
- **What is wrong:** `AGENTS_MD_CANDIDATE_DIFF.md` §9 (L893–910) and §3.3 define the `AGENTS.candidate.md` L6 `amended:` token differently. It is an "application-date slot: the date the tranche is applied at checkpoint 3". The manifest-draft date, the tranche ID and the notice-name slots are also application-date slots.
- **Consequence:** the act was at about 23:20 on 2026-09-25, so the tranche will almost certainly be applied on a later date. `49ce993a…` will then not stand as listed.
- **Why it blocks:** this file is the owner-ruled D-PEC packet (with `D-PEC-97`) and is fixed once merged. As written, it invites either a backdated `amended:` line or a false C1 mismatch.
- **Fix:** say that the PRD hash and every group-2 folder token stand as listed. Say that the `AGENTS.md` `amended:` line and the manifest and notice date slots take the checkpoint-3 application date under `AGENTS_MD_CANDIDATE_DIFF.md` §9. Optionally, align the `AGENTS.candidate.md` row of `ACCEPTED_MANIFEST.csv` ("Selected; applied at A4…") to match.

**B2. The package `Handoff_State.md` still asserts checkpoint-2 state that is now false.** This is the PR #926 B2 pattern.
- **Where:** `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md`:
  - L129: "The checkpoint-group-2 package is prepared and awaits the owner."
  - L150, the Closure verdict note: "checkpoints 2 and 3 are open".
  - L185–189, Next owning actor: "1. The owner decides the checkpoint-2 question set".
- **Problem:** the appended section (L204–206) says "The state fields above are otherwise unchanged". That re-asserts the L150 note that checkpoint 2 is open.
- **Precedent:** the group-1 repair stated explicitly which rows describe the pre-acceptance state.
- **Fix:**
  - State that L129, the L150 note and the L185–189 list describe the pre-acceptance state.
  - Give the post-acceptance values: checkpoint 2 accepted, checkpoint 3 open, next actor WORKING_ITEMS.
  - Keep `ReadyForNextPhase` `NO` (it is correct).

**B3. The Decision_Log "Non-decisions" section contradicts the accepted plan on when the notices go out.** This is the PR #926 B1 pattern.
- **Where:** `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Decision_Log.md` L74–75: "notices are graph node R4, after checkpoint 3."
- **What the accepted plan says:** `Propagation_Plan.md` §A4.3 has HELP_HUMAN write the three notices in the checkpoint-3 PR, during checkpoint-3 preparation. That PR merges before the owner's checkpoint-3 acceptance, as SCA-005's `bbee14b03` did before `c9e5cd87d`. "After checkpoint-3 acceptance" was only the non-selected alternative, with `disposition: pending`.
- **What the PR itself says:** `DECISION.md` L41 and graph R4 ("The notice content rides the checkpoint-3 PR") agree with the plan, not with L74–75.
- **Also missing:** the section says nothing about what checkpoint 2 added: the group-2 snapshot, the pointer `../SCA-006_GROUP-2_AUTHORIZED.md` and register row `D-PEC-97`. The group-1 repair added the equivalent line.
- **Fix:**
  - Reword L74–75 to say the notices go with the checkpoint-3 instruction tranche PR (A4) and none has been sent yet.
  - Add a bullet naming the group-2 snapshot, its pointer and `D-PEC-97`.
  - L65–67 and L70 remain true.

**B4. Work graph node R3 is marked READY while it waits on an owner decision.**
- **Where:** `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`:
  - L59: R3 is "READY — … Open owner choice before dispatch: the scope-change method edition".
  - L82: "Ready now: R3 (after the method-edition choice)".
  - L123: "The owner's choice of scope-change method edition … then dispatch R3".
- **The rule it breaks:** the template (`workflows/construct-local-work-graph/resources/work-graph-template.md` L36–37) says "A node awaiting a human decision is BLOCKED and names that decision."
- **The same update adopts that rule:** L99 says "This graph applies that from this update (G1, R2)". R2 is COMPLETE, so that parenthesis should read G1 and R3.
- **Fix, either one:**
  - Set R3 to `BLOCKED — owner's choice of scope-change method edition`, and fix L82 and L99.
  - Or cite `projects/pec/AGENTS.md` ("In-flight method bases retain their own authority until explicitly transitioned"), make the pinned edition the default, and stop gating dispatch on the choice.

### Non-blocking findings (most important first)

1. **Lane B3 (EvidenceQuote refresh) has no node.** Plan §B3 names DEP-09-06-003 (DEL-09-06) and DEP-10-03-003 (DEL-10-03). K1 (L69) covers only the new deliverables' `Dependencies.csv` rows, and no other node owns these two.
   - The other Lane B items all map:
     - B1+B2 → K1;
     - B4 → S4, D1 and K2;
     - B5 → D1;
     - B6 → K3;
     - B7 → K4.
   - Add B3 to K1's scope, or add a new node.
2. **K3 is missing a dependency on K2.** Plan §B6 says the profile act comes "After DEL-08-06's first Scope of Work fixes the tool's shape". K3 (L71) and the Order line (L85) put it after R3 only. Add K2 to K3's needs.
3. **The group-2 `Handoff_State.md` gives the notices to the wrong writer.** Its L14 lists "write the A4 tranche manifest and the three notices" under WORKING_ITEMS. Plan §A4.3 says HELP_HUMAN writes the notices. This snapshot also does not mention the open method-edition choice.
4. **The package `Handoff_State.md` hash table is stale.** L53 still shows `Decision_Log.md` `4968fe9d…`. The live value is `404c5960…6856`, and the pre-act value is `dc6e89fe…170e`. The SCA-005 checkpoint-2 act updated its table in place (`162d3ac40`).
5. **Decision_Log smaller items:**
   - The SCA006-CP2 row (L28) records `ACCEPTED` but not the Q-CP2-1 (a) selection; the SCA-005 precedent listed the selections in the status cell.
   - L91 still says "every checkpoint-2 question is `AWAITING_OWNER`", in the present tense. The SCA-005 precedent left the same wording, but a one-clause "(pre-acceptance)" would help.
6. **"Foreign-path" wording.** `DECISION.md` L39 opens the Root path `docs/governance_harness/tranche_manifests/PEC-SCA006-…yaml`, but L41 and L50 say the three notices are the only foreign-path writes. This is inherited from the plan. Clarify that the manifest is the tranche's Root instruction record.
7. **Notice triage is slightly overstated.** It says "Each has a home in this graph", but the CHANGE_CONCERNS notice also records that SCA-005's hand-written RETIRED states would trip `adapter_project.py` if PEC adopted the practitioner harness. Nothing in the graph carries that.
   - Also, if SCA-006 stays on the pinned scope-change edition, the R3 audit would use the revised `audit-decomp` (`EXPECTED_CONSEQUENCE`, from SETUP_DEPS). That mix of editions is worth stating in the owner's edition question.
8. **Stale graph text:**
   - L28 says notices go to "Root and App"; Runtime is now also routed.
   - The "Carried from SCA-006 checkpoint-1 preparation (for R2)" items (L110–116) are now settled at K1–K3 and R4.
   - Order has two "Done" bullets (L79–80).
   - L120 says the Root wave-2A tranches came "in between". But #935 (FORMATION, `971ca68a1`) merged after #934.
   - K4 names no owner (the plan names PROJECT_SETUP).
9. **The act's time zone is not recorded.** `DECISION.md` does not give the act's time or zone. The act was about 23:20 MDT, which is 2026-09-26 05:20 UTC, and the Root wave-2A records from the same evening are dated 2026-09-26. The slot values depend on the act date, so recording "local date" would help replay.
10. **STATUS gaps (not false):** the "Agent reliance" paragraph in `STATUS.md` mentions only checkpoint 1. The owner-gates list does not list the method-edition choice.

### What I verified

1. **Owner act.** `SCA-006 CP2: accept; Q1 a; Q2 a` is byte-identical in:
   - `DECISION.md` L31 (and L27, as HELP_HUMAN's suggested form);
   - `Decision_Log.md` L114;
   - the package `Handoff_State.md` L198;
   - register row D-PEC-97 (curly quotes, as in earlier rows);
   - `WORK_GRAPH.md` L58 and L150.

   No variant form appears anywhere.
2. **Interpretation.**
   - **Q-CP2-A:** PRD adoption and the S4 fix match plan §"Checkpoint-2 owner question set". PRD slots bind to the act date, so the PRD part is correct; B1 covers `AGENTS.md`.
   - **Q-CP2-1 (a):** matches plan L544.
   - **Q-CP2-2 (a):** A1, A2 (Seq 30/31/32), A4 (`AGENTS.md`, manifest, 3 notices), A5, A6 after checkpoint 3 and the C4 folder exactly equal plan L545 and C1. Lane B1–B7 are excluded.
   - **Lineage note:** matches plan L232.
   - **Notices basis:** matches plan §"Foreign-surface notices". Runtime `SOURCE_PINS.json` S4–S6 pin `projects/pec/AGENTS.md`, `Deliverables.csv` and `ScopeLedger.csv`.
   - **Limits:** nothing is enlarged, and the limits cover Lane B, `v2/**`, `software-workflow.json`, SOW, SPEC, `_REFERENCES`/`_DEPENDENCIES`, tier-0, pointers, foreign writes, lifecycle, access classes, consumers, release, CHECKING and ISSUED.
3. **Method edition.**
   - Root `09c299ac0` changed `workflows/scope-change/resources/contract.md` from `4453a719` to `0bd3533d` and `method.md` from `34187e83` to `22e2b43c`.
   - Follow-ups `0d7d5da61` and `4dcc2c6a8` in the same tranche give the final `74793f04` / `fd3fe525`, which equal `origin/main`. So "the tranche revised both to 74793f04… and fd3fe525…" is accurate.
   - The pinned edition `4453a719…` / `34187e83…` is the one recorded in `returns/B5_SCA006_CHECKPOINT2.md` L16–17.
   - `09c299ac0` is not an ancestor of `4d5f7b911` or `7f33b4dd5`, so the package was prepared on the pinned edition.
4. **`ACCEPTED_MANIFEST.csv`:**
   - It has 17 lines, all with 4 fields, and a trailing newline.
   - All 16 SHA-256 values equal `git show origin/main:<path> | shasum -a 256`.
   - Only `Decision_Log.md` and `Handoff_State.md` in the package folder change at HEAD.
   - The pre-act hashes `dc6e89fe…` and `0043e9b1…` are correct.
5. **Decision_Log:**
   - The table has 10 rows of 5 columns.
   - CP2 is `ACCEPTED` and CP3 is `PREPARATION AUTHORIZED`.
   - The frontmatter (group 3, `checkpoint_2_accepted_checkpoint_3_preparation_authorized`) follows the SCA-005 pattern at its checkpoint-1 acceptance.
   - The Non-decisions problems are B3.
6. **Pointer and register:**
   - The pointer follows the SCA-005 group-2 structure.
   - `_ScopeChange/_LATEST.md` still names SCA-005 (`e92b3b16…`).
   - D-PEC-97 has 6 columns, its relative paths resolve, and its state vocabulary matches D-PEC-92.
7. **Work graph:**
   - The dependencies are acyclic.
   - G1 is correctly BLOCKED on `D-PEC-96`. The proposal hash `2f7d9875…afc4` matches, and PR #928 merged as `6721457be` with reviews FAIL/FAIL/PASS.
   - PR #934 merged as `a558f5a40`; B5 verdicts were PASS WITH MINOR, PASS WITH MINOR, PASS.
   - The S4 set equals plan §B4.
   - EXECUTION triage claims check out against D-PEC-96 L46 and L607 and `AGENTS.candidate.md` L122.
   - The D-PEC-88 seventh-PR trace covers both the STATUS and README hunks.
8. **STATUS and README:** the changed lines are true.
9. **Hygiene:**
   - `git diff --check origin/main...HEAD`: exit 0.
   - `harness.py self-check`: exit 0. The 4 REVIEW findings are pre-existing and are in `_DomainEngines`.
   - `validate_pec_loop_receipts.py --repo-root .`: exit 0, VALID.
   - `validate_decomposition_registers.py --strict`: exit 0, 0 errors / 0 warnings.
   - The reliance-hold preflight (`candidate-validation`) returns ALLOW for all 10 paths.
   - No live decomposition, PRD, `AGENTS.md` or `_LATEST.md` byte changed; the checkpoint-3 preimages all hold at HEAD.
   - Nothing prompts about CHECKING.

**Side effect you should know about.** I extracted `git archive` trees into `scratchpad/head/` and `scratchpad/base/` in the shared session scratchpad. `head/` already existed from an earlier run (created 18:57, a full-repo archive), and its `projects/pec/**` files are now overwritten with `89cf8c7fe` bytes. `base/projects` may also have existed before (created 23:12); it now holds `origin/main` bytes. I also wrote `/tmp/claude-501/hsc.txt`, the harness output. Nothing in the repository was touched.

### Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/Handoff_State.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/ACCEPTED_MANIFEST.csv
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Decision_Log.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/AGENTS_MD_CANDIDATE_DIFF.md (§9, the source for B1)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Propagation_Plan.md (§A4, §B3, §B6)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/workflows/construct-local-work-graph/resources/work-graph-template.md

## HELP_HUMAN disposition

FAIL with four blocking findings. All are repaired in the next commit, and the reviewer re-checks the repair.

| Finding | Repair |
|---|---|
| B1 | `DECISION.md` says that the PRD hash and the group-2 folder tokens stand as listed. It also says the `AGENTS.md` `amended:` line and the tranche, manifest and notice date slots take the checkpoint-3 application date, under `AGENTS_MD_CANDIDATE_DIFF.md` §9. It records the act's local date, time zone and UTC time. The manifest row is aligned to match. |
| B2 | The package `Handoff_State.md` names the lines that describe the pre-acceptance state, and gives their post-acceptance values. `ReadyForNextPhase` stays `NO`. |
| B3 | The Decision_Log Non-decisions section says HELP_HUMAN writes the notices in the checkpoint-3 instruction-tranche PR (plan §A4.3). A new bullet names the group-2 snapshot, the pointer and `D-PEC-97`. |
| B4 | R3 is BLOCKED on the owner's choice of scope-change method edition. The Order section and the triage parenthesis are fixed. |
| 1, 2 | K1 now includes the plan B3 EvidenceQuote refresh (DEP-09-06-003, DEP-10-03-003). K3 now needs K2. |
| 3 | The group-2 `Handoff_State.md` gives the notices to HELP_HUMAN and names the open edition choice. |
| 4 | The package hash table carries the current `Decision_Log.md` hash, with its pre-act values. |
| 5 | The CP2 row records the Q-CP2-1 and Q-CP2-2 selections. The preparation note is marked as pre-acceptance. |
| 6 | `DECISION.md` says the manifest is the tranche's Root instruction record, not a notice. |
| 7 | The triage records the RETIRED/`adapter_project.py` item and the mixed-edition audit disclosure. |
| 8 | Graph L28 names Runtime, the carried items are marked as settled, the Order section is merged into one "Done" bullet, the basis line is corrected, and K4 names its owner. |
| 9 | Recorded under B1. |
| 10 | The STATUS reliance paragraph records checkpoint 2, and the owner-gates entry names the method-edition choice. |
