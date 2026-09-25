# Run record — HELP-HUMAN-PEC-20260923-SCA005

Purpose: execute the owner's 2026-09-23 direction recorded in
`_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md`: open
SCA-005 and prepare its checkpoint-group-1 package; run the three DEL-01-03
read-only evidence inquiries; triage the three 2026-09-23 notices; refresh
STATUS/README present-current prose; independent review; PR.

Supplied basis and hashes: `SUPPLIED_BASIS.json`. Briefs: `briefs/`. Returns:
`returns/`. Receipts: `projects/pec/loop/LOOP_RECEIPTS.md` (Receipt 179+).

## Work graph

| Node | Role / agent type | Depends | Write locus (under projects/pec/) | State |
|---|---|---|---|---|
| A1 sister-loop file-truth survey | TASK / general-purpose opus (high requested) | none | `execution/_Coordination/SCA-005_PREP_2026-09-23/SURVEY_*` | COMPLETE — `returns/A1_SURVEY.md`; DR-01..DR-18 |
| A2 PEC basis impact inventory | TASK / general-purpose opus (high requested) | none | `.../SCA-005_PREP_2026-09-23/IMPACT_INVENTORY_*` | COMPLETE — `returns/A2_IMPACT_INVENTORY.md`; 201 rows |
| A4 feed-model v2 design note | HELPS_HUMANS / general-purpose opus (high requested; no children) | none | `.../SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md` | COMPLETE — `returns/A4_FEED_MODEL_DESIGN.md`; recommends O-B2 + P-β; Q1–Q10 |
| C1 DEL-01-03 REM-001..003 inquiries | WORKING_ITEMS / general-purpose opus → 3 authors + 1 read-only verifier (all opus) | none | DEL-01-03 `_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/**`, `MEMORY.md` append | COMPLETE — `returns/C1_DEL0103_INQUIRIES.md`; verifier PASS; no Remaining item closed; O-2-2 flagged |
| D1 notice triage | TASK / general-purpose opus (task-management workflow) | none | `_TaskManagement/NOTICE_TRIAGE_2026-09-23.md` only (no rows warranted) | COMPLETE — `returns/D1_TM_NOTICE_TRIAGE.md` |
| B1 SCA-005 checkpoint-1 package | WORKING_ITEMS / general-purpose opus (scope-change) → audit-decomp child | A1, A2, A4 | `execution/_ScopeChange/SCA-005_2026-09-23_2139/`, `_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139/` | COMPLETE — `returns/B1_SCA005_CHECKPOINT1.md`; Impact_Assessment.md SHA-256 `0bcbe9bd…39bf`; 76 PROPOSED actions; AWAITING_OWNER |
| E1 STATUS/README currency | TASK / general-purpose opus | B1, C1 | `docs/STATUS.md`, `README.md` | COMPLETE — `returns/E1_STATUS_README_CURRENCY.md` |
| F1 independent review | TASK / general-purpose opus (read-only by instruction) | B1, C1, D1, E1 | none (read-only) | COMPLETE — `returns/F1_INDEPENDENT_REVIEW.md`; PASS WITH MINOR; minors repaired/recorded |
| G1 receipts, PR, CI, merge | HELP_HUMAN | F1 (+ B1 repair) | `loop/LOOP_RECEIPTS.md` | in progress |

Integration owner for all shared writes: HELP_HUMAN. Concurrent nodes have
disjoint write loci. Owner checkpoints are not inferred from any node's
completion.


Dispatch note: the host's agent roster is fixed at session start, so the gitignored `.claude/agents/` definitions (`pec-manager`, `pec-task`, `pec-reviewer`; `model: opus`, `effort: high`) were not selectable; every node ran as `general-purpose` with `model: opus` and high effort requested in its brief. See `SUPPLIED_BASIS.json`.

## Continuation 2026-09-24 (owner: "Have you tried answering those matters yourself?")

| Node | Role / agent type | Depends | Write locus | State |
|---|---|---|---|---|
| H1 checkpoint-1 resolutions from the repository | HELP_HUMAN | merged PR #882 | `returns/CHECKPOINT1_RESOLUTION_NOTE.md` (moved from the snapshot after review); pointer lines in `Decision_Log.md`, `Handoff_State.md`, `docs/STATUS.md` | COMPLETE |
| H2 DEL-01-03 obligations triage | TASK / general-purpose opus (high requested) | none | `returns/OBLIGATION_TRIAGE_DEL-01-03.md` | COMPLETE — 6 A / 9 B / 13 C (8 repairs) / 4 D (2 choices) |
| H3 D-PEC-87 correction-packet proposal | same TASK, resumed | H2 | `_DECISIONS/D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md` | COMPLETE — SHA-256 `ba3d3e64…` (after escape/fixture and triage-hash fixes); register row AWAITING_RULING |
| G2 receipt 180, register row, PR, CI, merge | HELP_HUMAN | H3 | `loop/LOOP_RECEIPTS.md`, `_DECISIONS/_REGISTER.md` | COMPLETE — PR #884 merged `f7e8b467cb2db244f11fe49cede636140031b387` after review PASS WITH MINOR (`returns/F2_REVIEW_PR884.md`) |

## Continuation 2026-09-24 (owner: "I accept checkpoint 1 and the Impact Assessment. …")

| Node | Role / agent type | Depends | Write locus | State |
|---|---|---|---|---|
| G3 record checkpoint-1 acceptance | HELP_HUMAN | merged PR #884 | `_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/{DECISION.md,ACCEPTED_MANIFEST.csv,Handoff_State.md}` (new); `SCA-005_2026-09-23_2139/Decision_Log.md` rows + `Handoff_State.md` amendment; `_REGISTER.md` D-PEC-86 status; `docs/STATUS.md`, `README.md`; `loop/LOOP_RECEIPTS.md` Receipt 181 | COMPLETE — PR #888 head `0d7435ec4` merged as `3c3adae355739b2ad24acdb33d3b5422bb36db95`; cycle-2 review of `6edd921fd` PASS WITH MINOR, minors applied in `0d7435ec4`, cycle-3 confirmation of `0d7435ec4` PASS (`returns/F3_REVIEW_CP1_ACCEPTANCE.md`) |
| G4 explain remaining owner decisions (D-PEC-87 C-A/C-B + L-1/L-2; seven TM-PEC-023 rows) | HELP_HUMAN | none | chat only | COMPLETE |
| F3 independent review of the G3 candidate | TASK / host agent type `pec-reviewer` (read-only) | G3 | none (return transcribed to `returns/F3_REVIEW_CP1_ACCEPTANCE.md` by HELP_HUMAN) | cycle 1 FAIL (5 MAJOR: four record-currency, one substantive Seq 75/Q10 contradiction) → repaired; cycle 2 PASS WITH MINOR → minors applied; cycle 3 confirmation of `0d7435ec4` PASS (transcribed late, during G5); verdicts in `returns/F3_REVIEW_CP1_ACCEPTANCE.md` |
| B2 checkpoint-2 package preparation | WORKING_ITEMS (`pec-manager`, scope-change) | G3 merged | `_ScopeChange/SCA-005_2026-09-23_2139/` checkpoint-2 artifacts | NOT_STARTED — next run; carries whichever TM-PEC-023 selections exist by then |


Authority note for G3 (HELP_HUMAN): D-PEC-86 §4 names WORKING_ITEMS (scope-change) as owner of the `_ScopeChange` package and holds `checkpoint_snapshots/` "untouched until owner acceptance". The acceptance occurred 2026-09-24. HELP_HUMAN wrote the group-1 snapshot and the amendment-qualified pointer itself rather than dispatching a manager, because the act is a transcription of the owner's ruling (K-AUTH-1 places that duty on the role that received it) and the snapshot binds existing bytes only; no scope-change judgment was exercised. The second `docs/STATUS.md`/`README.md` refresh is the same present-current maintenance I-5 named, made necessary by the acceptance; it asserts no acceptance that did not occur. If the owner reads I-5 as a single refresh only, the STATUS/README hunks of PR #888 revert cleanly. Warrant for the pointer path: D-PEC-86 §3 I-1 opened SCA-005 under the scope-change workflow, whose method finalizes "the group-1 decision snapshot and pointer" after acceptance; §4's post-acceptance `checkpoint_snapshots/` clause is read to include that companion pointer. It is a new file and reverts cleanly; `_LATEST.md` is not touched.

## Continuation 2026-09-24 (owner: "1. C-A. / 2. L-1a, L-2a but no need to ask me about declaring CHECKING status … / 3. … let's discuss 3 more.")

HELP_HUMAN is served by `claude-opus-5-5` from this continuation (owner switched the session model); earlier nodes were served by `claude-fable-5-1`.

| Node | Role / agent type | Depends | Write locus | State |
|---|---|---|---|---|
| G5 record D-PEC-87 ruling | HELP_HUMAN | merged PR #888 | `_DECISIONS/D-PEC-87_RULING_2026-09-24.md` (new); `_REGISTER.md` D-PEC-87 row; `docs/STATUS.md`, `README.md` (present-current maintenance, not owner-approved); `loop/LOOP_RECEIPTS.md` Receipt 182; `returns/F3_…` cycle-3 transcription; `returns/F4_REVIEW_D87_RULING.md` | COMPLETE — PR #890 merged `6b4a0f59d292ed9f5f0ca222986ca95bc01bb0b6`; review cycle 1 FAIL (two record-accuracy MAJORs) → repaired; cycle 2 PASS; cycle 3 PASS WITH MINOR → transcription-only append (`returns/F4_REVIEW_D87_RULING.md`) |
| C2 D-PEC-87 C-A correction slice | WORKING_ITEMS (`pec-manager`) → one TASK author (`pec-task`, software-bounded-implementation) → one fresh read-only verifier (`pec-reviewer`, software-code-review) | G5 merged and observed on `origin/main` | the seven granted paths; DEL-01-03 `_run_records/P1_STORE_GUARD_02/**`, `MEMORY.md`, and the single L-1a `_STATUS.md` edit (L-1a lets WORKING_ITEMS tick the REM rows independently of the slice's completion; bundling that edit into C2 is a work-organization choice) | in progress — dispatched after the #890 merge as host `subagent_type: pec-manager` (`model: opus`) in an isolated worktree, brief `briefs/C2_D87_CORRECTION_SLICE.md` (method path corrected after dispatch; manager notified) |
| G6 TM-PEC-023 per-row context for the owner | HELP_HUMAN (+ read-only research) | none | chat | COMPLETE — owner accepted the per-row reads except row 6, and deferred cmux |
| G7 record TM-PEC-023 selections and cmux deferral | HELP_HUMAN | G6; stacked on PR #890 | `_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/**` (new); `SCA-005_2026-09-23_2139/Decision_Log.md` rows + `Handoff_State.md` amendment; `SCA-005_GROUP-1_AUTHORIZED.md`; `docs/STATUS.md`, `README.md` (present-current maintenance); `briefs/C2_D87_CORRECTION_SLICE.md`; Receipt 183 | in progress — PR, independent review, CI, merge |
