# Brief B2 — SCA-005 checkpoint-group-2 package (WORKING_ITEMS, scope-change workflow)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node B2. Role: WORKING_ITEMS (Type 1). Model steer: `claude-opus-5-5`, high reasoning, for you and your children (D-PEC-86 I-8).

Authority: the owner accepted checkpoint group 1 on 2026-09-24, which authorizes checkpoint-2 preparation. On 2026-09-25 the owner directed "Proceed towards checkpoint 2 as indicated." Stage covered: **checkpoint group 2 preparation only** (method parts A and B). Produce one complete reviewable package, have it independently verified, and stop. Do not apply anything.

## Method

`Workflow: chirality-root:bundled:workflow:scope-change`. Load `workflows/scope-change/WORKFLOW.md`, `resources/contract.md` and `resources/method.md`, and record their SHA-256. Settings:
- Variant: `SOFTWARE`.
- `CONTEXT_ROOT = projects/pec/execution/`.
- `DECOMPOSITION_PATH = projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.4).
- `SCOPE_CHANGE_ROOT = projects/pec/execution/_ScopeChange/`.
- `AMENDMENT_ID = SCA-005`.
- `ALLOW_RENUMBERING = false`.

Where the method is silent on form, mirror SCA-004 (`_ScopeChange/SCA-004_2026-08-02_2325/`: `Amendment_Preview.md`, `Propagation_Plan.md`, `Supersession_Map.csv`).

## Accepted basis (read first; verify hashes; stop and report on any mismatch)

1. **Group-1 authority pointer.** `projects/pec/execution/_ScopeChange/SCA-005_GROUP-1_AUTHORIZED.md`.
2. **Checkpoint snapshots, all files.** Read these together:
   - `checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/`;
   - `checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/`, including `Amendment_Actions_Addendum.csv` and the §"Impact delta against the accepted group-1 evidence";
   - `checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-2_2026-09-24/`.
3. **The SCA-005 package** `_ScopeChange/SCA-005_2026-09-23_2139/`:
   - `Impact_Assessment.md` (accepted, SHA-256 `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf`);
   - `Amendment_Actions.csv` (accepted intake, `5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2`);
   - `Brief.md`, `Pre_Change_Coverage.json`;
   - `Decision_Log.md`, including row SCA005-D90-NOTE;
   - `Handoff_State.md`.
4. **Checkpoint-1 resolution note.** `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/CHECKPOINT1_RESOLUTION_NOTE.md` (`af4e46d0dba2fb71c8f4aceca69098d81806b9add1ac960f074aa8fe949b0ad2`). It holds the selected Q1–Q10 and CP1-* options.
5. **Evidence behind the Impact Assessment.**
   - `execution/_Coordination/SCA-005_PREP_2026-09-23/`: survey, impact inventory and `FEED_MODEL_V2_DESIGN_NOTE.md`.
   - `execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/` (D-PEC-79, adopted, not applied).
   - `execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/`.
6. **Live canonical package.**
   - `execution/_Decomposition/` (`SOFTWARE_DECOMP.md` `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`), its four registers, and `_LATEST.md`.
   - `docs/PRD.md` v2.2 (`6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`).
   - `_ScopeChange/_LATEST.md` (names SCA-004) and the SCA-004 snapshot.
   - `docs/DECOMPOSITION_STANDARD.md`.
   - `projects/pec/AGENTS.md`, for fences F-PEC-1..4.
7. **`execution/_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md`.** It carries the preparation note: DEL-04-01 and the PRD §8 refresh are not to be designed around verify-before-rely. Checkpoint 2 still quotes the in-force v2.2 text, and PEC-K-03 is not amended by SCA-005. A later scope change amends it.

## What the package must contain

These owner selections are already made and are not re-asked. Apply them exactly as recorded in the snapshots:
- the checkpoint-1 options (Q1 O-B2 … CP1-O);
- the TM-PEC-023 values (amendment 1: rows 1, 2, 3, 5, 8 and 9 mapped; rows 4, 6 and 7 moot or dropped);
- the cmux deferral (Seq 77 and 78; Seq 43 narrowed; Seq 75 extended; Seq 68 dropped);
- the SOW-033 mapping (Seq 79, `OBJ-003`);
- Seq 72 dropped (Q9);
- Seq 75 narrowed (Q10 (a)).

**Part A — exact amendment.** `Amendment_Preview.md` is a diff-style preview across the method's semantic sections: Change Register, Packages, Deliverables, Scope Ledger (including objective mappings), Vocabulary Map, and coverage/telemetry/open issues. It must also contain the full child-closure set and ledger remaps for every partition change, and the retired-row representation.

Also produce candidate postimage bytes, not applied, under `SCA-005_2026-09-23_2139/CP2_CANDIDATE/`:
- `_Decomposition/SOFTWARE_DECOMP.md` as revision 1.5;
- every affected register.

Record each postimage's SHA-256 and each preimage's SHA-256.

**PRD v2.3 successor candidate** (CP1-D79 (b)), under `CP2_CANDIDATE/docs/PRD.md`, with a section-by-section diff against v2.2 in `PRD_V2_3_SUCCESSOR_DIFF.md`. It carries:
- the six D-PEC-79 hunks;
- the Annex B rows of the Impact Assessment as accepted;
- Seq 75 as narrowed and extended.

Where D-PEC-90 bears on §8 or orientation text, keep the v2.2 meaning (verify-before-rely stands), and add no reliance text.

**Part B — propagation plan.** `Propagation_Plan.md`, limited to the write scope the amendment needs:
- per-action propagation: ADD via the preparation skill and project-setup; REMOVE via `RETIRED` status with no deletion; MODIFY as `_CONTEXT.md` edits per deliverable;
- the downstream rerun advisory: dependency extraction, PROJECT_SETUP metadata re-pin, SOW currency per deliverable (including the two housekeeping fixes and the DEL-01-06 v2-schema obligation as a later D-PEC packet), DEL-00-03 SPEC, and the P1 fixture strategy;
- the package-role classification of every touched surface;
- derivative status per package;
- the closure validation lane, which separates direct writes after checkpoint 2, downstream reruns not executed by WORKING_ITEMS, and closure validation;
- the foreign-surface notices, which PEC does not write.

**Other outputs.**
- **`Amendment_Actions_CP2.csv`:** the exact final action register. Use the contract columns plus `SupersessionBindingPresent`. Every row cites the intake Seq and the snapshot that shaped it.
- **`Supersession_Delta.csv`:** a binding for every action that supersedes an admitted authority fact, including the PRD rows and the SOW supersessions the Impact Assessment flags.

Resolve or explicitly carry the group-1 blockers:
- the RETIRED-row representation against XRG-003/005/007/008, tested by running the validators on a scratch copy of the candidate postimage;
- whether `audit-decomp` flags a zero-coverage retired row;
- the post-change dependency topology (plan it; mark UNKNOWN only what genuinely needs the re-extraction);
- which SCA-004 downstream repairs happened since 2026-08-03 (verify against the files).

Refresh the accepted evidence that the amendment-1 impact delta names.

Since checkpoint 1, `v2/**` changed under D-PEC-87, 89 and 91, and DEL-01-03 received new run records. Confirm that none of this changes any SCA-005 action, or report which one it changes.

**Checkpoint-2 owner question set**, at the end of `Propagation_Plan.md`:
- accept the exact amendment and propagation plan together, citing the exact SHA-256 of `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`, the PRD candidate and the postimages;
- only genuinely open choices besides that, each with a recommendation.

Do not re-ask settled selections.

## Write boundary (only)

In your isolated worktree, on a branch `claude/pec-sca005-cp2-package` from fresh `origin/main`, write only these inside `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/`:
- new files: `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`, `PRD_V2_3_SUCCESSOR_DIFF.md`, and `CP2_CANDIDATE/**`;
- additive updates to `Decision_Log.md`: the SCA005-CP2 row goes to `PREPARED / AWAITING_OWNER`, with the package hashes;
- additive updates to `Handoff_State.md`: a dated amendment line and state fields per the contract (`DecompositionTruthState` `INCOMPLETE`; `ReadyForNextPhase` `NO`).

Also write `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/B2_SCA005_CHECKPOINT2.md` (your return, plus your verifier's verdict files beside it as `B2_VERIFIER_VERDICT_NN.md`).

Do NOT modify:
- `Impact_Assessment.md`, `Amendment_Actions.csv`, `Brief.md` or `Pre_Change_Coverage.json` (accepted bytes);
- `checkpoint_snapshots/**`, `SCA-005_GROUP-1_AUTHORIZED.md` or `_ScopeChange/_LATEST.md`;
- the live decomposition or registers, `docs/PRD.md`, any SOW, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` or `_DEPENDENCIES.md`;
- `v2/**`, `software-workflow.json`, `loop/**`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**`, the HELP_HUMAN `RUN.md`, or any Root, sister or foreign path.

HELP_HUMAN records the receipt, STATUS/README and the decision snapshot after the owner acts.

## Checks

Run each of these and record the command, cwd, interpreter and exit code in `Handoff_State.md` and your return:
- `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` on the live tree (unchanged, exit 0), and the same validator on a scratch copy with the candidate postimages in place;
- the preimage hash checks above;
- `python3 tools/validation/validate_scope_change_packet.py`, if its schema fits (report if it does not);
- a parse check of both action CSVs against the contract columns and enums;
- the PEC reliance-hold preflight (`projects/pec/execution/_Scripts/pec_reliance_hold.py`, operation `exact-correction-preparation`) for the decomposition, the registers and `docs/PRD.md`;
- `git diff --check`;
- a containment check of `git diff --name-only origin/main` against the write boundary.

## Delegation

You may dispatch bounded TASK children (`subagent_type: pec-task`, `model: opus`, no further delegation) for drafting in disjoint files, for example the PRD candidate or the register postimages. You integrate the results and own the package.

Before returning, dispatch one fresh read-only verifier (`subagent_type: pec-reviewer`, `model: opus`). It checks the package against the snapshots, the accepted Impact Assessment and the method:
- every selection applied exactly and nothing unselected added;
- child closure;
- stable IDs;
- invariants, including the union rule `Deliverables.SupportsObjectives = union(ScopeLedger.ObjectiveIDs)`;
- supersession bindings;
- the PRD candidate against D-PEC-79 and Annex B;
- the write boundary.

Defects go back to the drafter; repeat until the verifier finds nothing blocking. Save each verdict.

If child completion notices reach HELP_HUMAN instead of you, HELP_HUMAN relays them verbatim.

## Publication

Commit (end each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`), push, and open a PR against `main`. End the PR body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Do not merge. The PR publishes a candidate for the owner. It applies nothing.

## Return

- PR URL and head SHA;
- the package file list with SHA-256;
- action counts by type (intake versus CP2 final, with the delta explained);
- the counts that change;
- blocker resolutions;
- the checkpoint-2 owner question set;
- check results;
- verifier verdicts and cycles;
- containment output;
- anything unresolved or routed;
- the delegation record.

## Limits

No decomposition, PRD, SOW or pointer application. No CHECKING, ISSUED or acceptance; do not ask the owner about CHECKING. No `v2/**` or foreign write. No reliance-text amendment (D-PEC-90 H6 is later).
