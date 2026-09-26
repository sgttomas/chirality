# Review 01 of PR #926 (SCA-006 checkpoint-1 acceptance record), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `4398370947b728ea07801479640285269734d2ee`.
- **SHA-256 of the report text below (UTF-8):** `cc03e970474ee2bab6d566140c7d1eeb1fd3fd3c6e8ae919e826abc6c8370111`.

## Report (verbatim)

## Review of PR #926 (`claude/pec-sca006-cp1-accept`, head `4398370947b728ea07801479640285269734d2ee`, base `origin/main` `3245f9acd`)

**Verdict: FAIL.** There are two blocking findings. Both are wrong or contradictory statements in the SCA-006 package files, and both are quick to fix. The acceptance record itself holds up: the owner quote is verbatim, every hash matches, and the interpretation neither enlarges the owner's act nor departs from the Impact Assessment.

`gh pr view 926` shows head `4398370947b7…` (OPEN), base `main`. I did not modify the checkout, and `git status --porcelain` is empty.

### Blocking findings

**B1. The Decision_Log "Non-decisions" section is now false.** Location: `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Decision_Log.md` L65–67 and L72–73.
- **L65–67 say:** "No PRD, `projects/pec/AGENTS.md`, decomposition, register, pointer, `checkpoint_snapshots/`, Scope of Work, … byte has changed."
- **This PR contradicts that three ways:**
  - it creates `checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`;
  - it creates the pointer `_ScopeChange/SCA-006_GROUP-1_AUTHORIZED.md`;
  - it edits the decision register row for D-PEC-90.
- **L72–73 are also stale.** They still say, in the future tense, that the checkpoint-1 snapshot "will be written … only after the owner's acceptance".
- **Precedent:** the SCA-005 review F3 (`returns/F3_REVIEW_CP1_ACCEPTANCE.md`, cycle 1) raised this same kind of problem as MAJOR. The repair commit `6edd921fd` reworded the SCA-005 bullet to "No decomposition, decomposition register, SOW, …" and added "`_LATEST.md` still names SCA-004 (the amendment-qualified … pointer is new)". F3 also flagged the ambiguous word "register" as a NOTE.
- **Fix:**
  - Reword L65–67 to cover what did change: "decomposition register" instead of "register"; say the group-1 snapshot and the amendment-qualified pointer are new and `_LATEST.md` still names SCA-005; say the decision-register D-PEC-90 row gained a pointer.
  - Replace L72–73 with a past-tense line naming the snapshot.

**B2. The package handoff now uses a `ReadyForNextPhase` value the contract does not allow, and contradicts itself.** Location: `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md` L114–116, against L38 and L17/L23–25.
- **L114 says:** "`ReadyForNextPhase` for checkpoint-2 preparation is `YES`."
  - The contract allows only `NO` / `REGEN_ONLY` / `PHASE7_REVIEW` / `PUBLICATION_GATED` (`workflows/scope-change/resources/contract.md`, state-fields table).
  - The same file's table still says `NO` (L38).
  - The SCA-005 precedent kept "`ReadyForNextPhase = NO` until checkpoint 3" (`6edd921fd`, the third amendment of the SCA-005 `Handoff_State.md`).
- **L115–116 then say "All other state fields above are unchanged."** That implicitly re-asserts rows that are now false:
  - L17 "owner acceptance **not** given";
  - L23 "Group-1 decision snapshot | not created";
  - L24 "Next owning actor | the owner";
  - L25 "the owner's checkpoint-1 decision is the only blocker".
  - The SCA-005 precedent said explicitly that its "not created" and "Stage reached" rows describe the pre-acceptance state.
- **Fix:**
  - Replace the `YES` bullet with: checkpoint-2 preparation is authorized; `ReadyForNextPhase` stays `NO` until checkpoint 3.
  - State that the Stage-reached, Group-1-snapshot, Next-owning-actor and Blockers rows describe the pre-acceptance state.

### Non-blocking findings (most important first)

1. **The G1 state is inconsistent within `WORK_GRAPH.md`.**
   - L65 has G1 as `READY`. But L76 says "Active: G1 packet preparation", and L111 lists a running read-only TASK for G1. The template's `ACTIVE` state fits.
   - L109 still opens with "None running", which contradicts L111.
   - The G1 brief `G1_REGISTRY_SOURCE_PROPOSAL.md` (`084eadd8…0fca1`) is not in the repository. It is not under `briefs/`, and no path is given, so its hash cannot be checked. `D-PEC-96` is not yet in the register.
   - Fix: set G1 to ACTIVE, reword "None running", and give the brief's location or commit it, as the earlier briefs were.

2. **The package `Handoff_State.md` hash table L53 still shows the pre-acceptance `Decision_Log.md` hash** (`8a01bd65…`). The live file is now `b36b58e7…a8cc`. SCA-005 review F3 raised the same issue as MINOR, and its repair updated the table in place, noting the pre-acceptance value.

3. **Decision_Log smaller issues.**
   - The L11–16 preamble ("Every other row is `AWAITING_OWNER` or `NOT_STARTED` … The owner accepts checkpoint group 1, if at all") is stale now that the CP2 row reads `PREPARATION AUTHORIZED`.
   - The L21 Authority cell cites `checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/` without `../`. L80 and the SCA-005 precedent use `../`.

4. **"Checkpoint 2 is in preparation" is ahead of the facts.** It appears in `docs/STATUS.md` L239 and `README.md` L90. The graph has R2 as READY, with the manager "dispatched after this graph update", so preparation has not started. D-PEC-88 requires "no assertion of acts that did not occur", and the SCA-005 precedent wrote "authorized and not started". Suggest "checkpoint-2 preparation is authorized".

5. **"None SCA-006 amends" is true only at text level.** `WORK_GRAPH.md` L96 says the D-PEC-95 act changed "119 derivative paths, none of which SCA-006 amends". `DECISION.md` L18 says "nothing SCA-006 amends".
   - At path level this is wrong. Three of the 119 paths are in SCA-006 `AffectedFiles`:
     - `DEL-04-03/_CONTEXT.md` (Seq 30);
     - `DEL-08-03/_CONTEXT.md` (Seq 32);
     - `DEL-10-12/Dependencies.csv` (Seq 54).
   - D-PEC-95 changed only the anchor lines at L30–31 and DEP-10-12-003. SCA-006 targets the description mirrors and DEP-10-12-004, which D-PEC-95 left alone. So the baseline note's wording at `DECISION.md` L77 ("no text SCA-006 amends changed") is accurate.
   - Fix: align L96 and L18 to the text-level wording.

6. **The CP1-DQ interpretation's Seq list is loose.** `DECISION.md` L41 says "(Seq 3, 7, 20, 26, 28, 31, 41 and the DQ-a advisories)".
   - It mixes agent-class-specific rows (3, 20, 31, 41) with rows that DQ-b also keeps (7, 26, 28).
   - It omits other direct-query rows (4, 9, 10, 15, 21, 34).
   - No enlargement results, because CP1-A confirms all 54. Consider "e.g." or a derivation from IA §13.1.

7. **The routing of DEL-03-04 and DEL-10-03 differs from the accepted IA §7.1.** The IA proposes "Review-level (S1 or D1): DEL-03-04, DEL-10-03 and DEL-00-03". The graph now keeps all 9 out of S1 (L61) and says the review-level three "also wait for R3" (L64). This is more conservative and within graph discretion, but R2 should note the deviation.

8. **Nits.**
   - `WORK_GRAPH.md` L65: "no predecessor. the accepted…" starts a sentence in lowercase.
   - L92–95 still say "(recommended set)" and "(recommended INS-a)" although these are now selected.
   - L126 "It was given after HELP_HUMAN explained…" is HELP_HUMAN's account but not labelled as such. This is the same kind of issue as PR #925 finding 6.
   - `STATUS.md` L254 "Checkpoint 2 carried a note…" means SCA-005's checkpoint 2, and now sits next to SCA-006 checkpoint text. That is ambiguous.
   - S3 lists "S2 context for parsers" among its needs while it is READY and S2 has not run.

### What I verified

1. **Owner act.**
   - The exact string `SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded` appears byte-identically in:
     - `DECISION.md` L32;
     - `Decision_Log.md` L77;
     - `_REGISTER.md` (D-PEC-90 row);
     - `WORK_GRAPH.md` L126;
     - the package `Handoff_State.md` L104–105 (line-wrapped inside quotation marks; identical after whitespace normalization).
   - `STATUS.md` and `README.md` paraphrase it ("DQ a, ENV a, …") and do not present it as a quote. That is acceptable.
   - It matches IA §15's one-line form except for the final period, and matches the owner's words as the brief gives them.

2. **Interpretation.**
   - CP1-A: 54 actions, 12 ADD / 42 MODIFY, matching the CSV count.
   - ENV-a: PEC-ORI-007 → SOW-097 → DEL-04-03.
   - BUD-a: PEC-API-006 → SOW-098 → DEL-08-03, with numbers set at P1.
   - GATE-a: SOW-100 and DEL-10-13, P1 row not edited (IA §13.4).
   - INS-a: IA §13.5.
   - R-C: IA §13.6.
   - The DQ-b explanation matches IA §13.1 (49 actions, 7 AFFECTED).
   - Nothing is enlarged. The acceptance authorizes checkpoint-2 preparation only, and the limits cover the PRD, AGENTS.md, decomposition and registers, pointers, SOWs, SPEC, `_CONTEXT.md`, `_STATUS.md`, `v2/**`, `software-workflow.json`, the tier-0 profile, foreign surfaces, access classes, consumers, reliance holds, release, CHECKING and ISSUED.
   - The Runtime notice is correctly left for the checkpoint-2 plan to justify.
   - The baseline note is accurate:
     - PR #924 (`abfd0897b`) changed 119 non-run-root product paths: 2 `_LATEST.md`, `_COORDINATION.md`, 42 contexts, 64 references and 10 `Dependencies.csv`.
     - IA §2.1's byte-identity claim is quoted correctly.
     - COV-068/069/072/073 are present in the POSTSETUP audit.

3. **Hashes.** I recomputed all six `ACCEPTED_MANIFEST.csv` SHA-256 values with `shasum -a 256` on `git show 3245f9acd:…`, and all match:
   - Impact_Assessment `93253b7d…b691`;
   - Amendment_Actions `c5f90801…4891`;
   - Brief `205a46c0…1831`;
   - Pre_Change_Coverage `b7b432a2…128d`;
   - Decision_Log `8a01bd65…547a`;
   - Handoff_State `4526797c…f9df`.

   Other checks:
   - The IA, actions, Brief and coverage files are byte-unchanged at HEAD.
   - The manifest has 7 rows of 4 fields each.
   - The PRD is `fff27a66…dc32` and `SOFTWARE_DECOMP.md` is `dc2b8479…9660`, as `DECISION.md` states.
   - `b1145955e` is PR #922.

4. **Decision_Log.**
   - The table has 10 rows, each with 5 columns.
   - The statuses are appropriate and follow the SCA-005 pattern.
   - The frontmatter matches the SCA-005 post-acceptance values exactly. The contract defines no Decision_Log frontmatter vocabulary, so there is nothing to conflict with.
   - The Non-decisions section is false (B1).

5. **Pointer and scope.**
   - The pointer follows the SCA-005 structure (snapshot, scope, next, amendment-qualified limits).
   - `_ScopeChange/_LATEST.md` is untouched and names SCA-005.
   - The diff has 10 files: 3 under `_ScopeChange` package or snapshot paths, 2 under `_Coordination/**`, `STATUS.md`, `README.md`, and 3 new snapshot/pointer files. No decomposition, PRD, instruction, SOW, `_STATUS.md` or `v2/**` byte changed.

6. **WORK_GRAPH.**
   - Only template states are used.
   - The edges are acyclic: U1/R1 → S1–S3; G1 → S2 (for DEL-01-06); R1 → R2 → R3 → R4/S4/D1/I1; S2/S3 → X1; then C1 → M1 → F1.
   - R2 and S1–S3 READY are justified once this PR merges.
   - PR #925 review findings 1, 2, 3, 4 (all three parts), 6 (the line was removed) and 8 are addressed. Finding 5 is carried as the baseline note.
   - The D-PEC-88 trace for the fifth PR covers all 4 STATUS hunks and both README hunks.
   - "Fifth PR" is correct (#919, #921, #923, #925, #926).

7. **STATUS and README.**
   - SOW-037 is `OUT` (`ScopeLedger.csv` L38).
   - DEL-07-04 is `[RETIRED — SCA-005]` in `Deliverables.csv` L42, and its `_STATUS.md` reads "Current State: RETIRED".
   - The README SCA-004 rephrase and the TM-PEC-023 annotation are accurate.
   - The remaining issues are non-blocking finding 4 and the finding 8 nits.

8. **Register.** The D-PEC-90 row has 6 columns. The appended text is accurate and its relative paths resolve.

9. **Limits and hygiene.**
   - Nothing prompts about CHECKING; the only added mention is the prohibition at `DECISION.md` L63.
   - `git diff --check origin/main...HEAD`: exit 0.
   - `validate_pec_loop_receipts.py --repo-root .`: exit 0, VALID.
   - `validate_decomposition_registers.py --strict projects/pec/execution`: exit 0, 0 errors / 0 warnings.
   - `harness.py self-check`: exit 0.
   - The reliance-hold preflight (`candidate-validation`) returns ALLOW for all 10 changed paths.
   - `validate_scope_change_packet.py` does not fit a checkpoint snapshot: exit 1, missing `Packet_Contract.md` and the other packet files, as recorded for SCA-005 and SCA-006. `validate_domain_decomposition_integrity.py` is DOMAIN-only, so no scope-change validator applies.

### Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Decision_Log.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/ACCEPTED_MANIFEST.csv
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-006_GROUP-1_AUTHORIZED.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/README.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/workflows/scope-change/resources/contract.md

## HELP_HUMAN disposition

FAIL with two blocking findings. Both are repaired in the next commit, and the reviewer re-checks the repair.

| Finding | Repair |
|---|---|
| B1 | The Decision_Log "Non-decisions" section now says "decomposition-register", names the new snapshot and pointer, says `_LATEST.md` still names SCA-005, and notes the D-PEC-90 register pointer. The snapshot line is in the past tense, and the preamble is current. |
| B2 | The package handoff says checkpoint-2 preparation is authorized and `ReadyForNextPhase` stays `NO` until checkpoint 3. The four Position rows are stated to describe the pre-acceptance state, and their post-acceptance values are given. |
| 1 | G1 is set to ACTIVE, since the draft has returned and publication is next. The "None running" wording is corrected, and the G1 brief is committed to `briefs/`. |
| 2 | The hash table's `Decision_Log.md` row carries the post-acceptance hash and notes the pre-acceptance value. |
| 3 | The Decision_Log preamble is current, and the snapshot path uses `../`. |
| 4 | STATUS and README say "checkpoint-2 preparation is authorized". |
| 5 | The graph states that three `D-PEC-95` paths overlap SCA-006 `AffectedFiles` with no amended text changed. `DECISION.md` says "no text that SCA-006 amends". |
| 6 | The CP1-DQ row distinguishes the rows specific to the agent class from the direct-query rows shared by DQ-a and DQ-b, which DQ-c drops or changes (IA §13.1). The first repair wrote "kept under every DQ option"; re-review R1 corrected it. |
| 7 | The graph records that it holds DEL-03-04, DEL-10-03 and DEL-00-03 until R3, which is more conservative than IA §7.1's "S1 or D1", and that R2 records this. |
| 8 | The G1 row is rewritten. "Recommended" is changed to "selected" where the owner has selected. The owner-evidence account is labelled as HELP_HUMAN's. The STATUS sentence now says SCA-005's checkpoint 2. S3's needs no longer imply a block on S2. |
