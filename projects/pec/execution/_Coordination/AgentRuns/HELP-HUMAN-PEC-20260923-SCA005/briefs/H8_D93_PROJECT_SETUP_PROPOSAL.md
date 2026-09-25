# Brief H8 — draft D-PEC-93: PROJECT_SETUP packet for SCA-005 A4 and B3 (read-only TASK)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node H8. Role: TASK (Type 2). You do not delegate. Model steer: `claude-opus-5-5`, high reasoning.

## Why

On 2026-09-25 the owner accepted SCA-005 checkpoint 2 with Lane A4 deferred: "Q4 a with A4 deferred". A4 covers the DEL-02-08 and DEL-02-09 folders and their `Dependencies.csv` ANCHOR rows. It goes to PROJECT_SETUP under its own packet, together with Lane B3, the dependency rerun. SCA-005 then closed for scope change only on checkpoint 3. The owner has now directed: "go ahead with the PROJECT_SETUP packet".

`projects/pec/AGENTS.md` §"Write Scopes And Fences" requires an owner-ruled D-PEC packet for this. The packet must name exact paths, acts, verification and rollback. Your job is to draft it so the owner can rule on it.

## Basis (read; record SHA-256)

- Checkout `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5`, detached at `origin/main` `6dac281c679e779e9e8507add693554f102242d2`. Do not change it. Report `git rev-parse HEAD`.
- `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md`: §A4, §B3, §C2, §C4, §B7, the "40 vs 42" note and §"Failure and rollback". Also `Amendment_Preview.md` for the accepted DEL-02-08/09 register rows. Read the plan's A4 and B3 as intent. The exact bytes are yours to specify.
- The group-2 and group-3 decision records under `_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-{2,3}_2026-09-25/`, register rows `D-PEC-92` and `D-PEC-86`, and SCA-005 `RUN_SUMMARY.md` §"Recommended downstream reruns".
- The accepted decomposition revision 1.5 and its registers under `projects/pec/execution/_Decomposition/`, plus `docs/PRD.md` v2.3.
- Methods:
  - `workflows/project-setup/`
  - the `preparation` skill: resolve its effective descriptor as the plan's A4 says, and record `source` and `sourceRootId`
  - `workflows/dependency-extract/`
  - `workflows/audit-decomp/`
  - `workflows/audit-dep-closure/` if relevant
  - `tools/validation/validate_decomposition_registers.py`
  - `tools/validation/validate_dependencies_schema.py`, if present
  - `tools/coordination/analyze_dep_closure.py`
- Precedent format: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_del_01_03_count_domain_encoding_residual_proposal_2026-09-25.md` and its ruling; the SCA-004 PROJECT_SETUP closeout `execution/_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/`.
- The latest audit, `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`.

## Task

Draft `D-PEC-93` in the D-PEC-91 format. It must let the owner rule on one bounded PROJECT_SETUP act with these parts.

1. **A4, exact.**
   - Resolve the DEL-02-08 and DEL-02-09 folder names by the PROJECT_SETUP naming rule from the accepted names. Show the rule and its output.
   - List every file to create, with exact bytes or a byte-exact generation method that you prototype: `_CONTEXT.md` at revision 1.5, `_STATUS.md` `OPEN`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and anything else the preparation skill requires.
   - Say how the `_STATUS.md` creation is done. Is there a tool that writes `OPEN`?
2. **B3, exact.** For every `Dependencies.csv` row to retire, add or refresh, give the owning file path, the row ID, and the before and after values. Apply the plan's retirement representation: keep the row, `Status=RETIRED`, `LastSeen`, and a `Notes` prefix. Rows are never deleted.
   - Resolve the plan's PLANNED new edges into exact rows. Say whether `dependency-extract` must produce them, or whether its method allows a specified exact write. Either way, the packet must bind exact bytes or a deterministic procedure plus an acceptance check.
   - Decide on the optional DEL-04-01 → DEL-02-08 edge and recommend.
   - Give the exact `_DEPENDENCIES.md` mirror edits for the consumers the plan names.
   - Keep the `[E-P25]` replacement as the plan specifies: retire `DEP-03-01-014` and refresh the evidence of `DEP-03-01-007`.
3. **Verification.**
   - `validate_decomposition_registers.py --strict` must reach 0 errors / 0 warnings.
   - `analyze_dep_closure.py` must show 0 SCCs and 0 bidirectional pairs, with the exact expected edge count and isolated nodes.
   - Run a re-audit with `audit-decomp`, full SOFTWARE scope, into a new `COV_SCA005_POSTSETUP_<date>_<time>/` folder. Compare it with `COV_SCA005_POSTCHANGE_2026-09-25_1344`. Expect COV-001/002/070/071 to clear.
   - State whether moving `_Evaluation/DecompCoverage/_LATEST.md` to the new audit belongs in this packet. Recommend it, since D-PEC-92 did not open it.
   - Say what an independent verifier checks.
4. **Options.**
   - A (recommended): A4 + B3 + re-audit + audit pointer.
   - A narrower option, if one makes sense.
   - An optional add-on for B1: re-pin the 42 `_CONTEXT.md` and 64 `_REFERENCES.md` files to revision 1.5. Give its exact scope and cost. Do not recommend bundling it unless it is clearly proportionate.
   - Amend or defer.
5. Include a product grant (exact paths opened, with preimage SHA-256 for every existing file touched), an administrative grant (run root and records), rollback with preimages, and limits. The limits are: no SOW, `v2/**`, PRD, decomposition-register or lifecycle change beyond creating the two `OPEN` statuses; no CHECKING, ISSUED or acceptance; and CHECKING is not an owner gate.
6. Add the owner questions.

**Prototype.**
- Apply A and B3 to a scratch copy exported with `git archive` into your own `mktemp -d` directory. Never apply them to the checkout.
- Run the validators and `analyze_dep_closure.py` there, and report exits and counts.
- Delete large exports when done; keep the small evidence under the scratchpad path below.
- Run `projects/pec/execution/_Scripts/pec_reliance_hold.py` with operation `exact-correction-preparation` on the targets and record the result.

## Limits

You are read-only on the repository: no edits in the checkout, no state-changing git, no PRs.

You may write only:
- the draft, to `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/h8/D-PEC-93_DRAFT.md`;
- small evidence, under that `h8/` folder;
- prototypes, in your own temporary directory.

The draft's status line is `PROPOSAL / AWAITING_RULING`, prepared by TASK under HELP_HUMAN node H8.

## Return

A short return with:
- the draft path and SHA-256;
- the recommended option in a few lines;
- the resolved folder names;
- exact row counts by kind;
- prototype check results;
- the owner questions;
- anything unresolved.
