# Brief — AUDIT_DECOMP post-setup re-audit (D-PEC-93, SCA-005 A4 + B3)

The WORKING_ITEMS manager of node C5 dispatched this run. C5 belongs to
HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`. The run is the post-setup
re-audit that the D-PEC-93 proposal requires after the option-A PROJECT_SETUP
act (SCA-005 Lane A4 with Lane B3). It went to a Type 2 TASK instance
executing `chirality-root:bundled:workflow:audit-decomp`. Type 2 does not
delegate. The model steer was `claude-opus-5-5` at high reasoning. The host
reports the model as Opus 5.5 (`claude-opus-5-5`). This report records that
identity as the runtime exposes it and does not treat the steer as evidence of
the model used.

## Parameter source

The parameters come from the D-PEC-93 proposal, section "Re-audit and audit
pointer", and are not enlarged:

- proposal `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-93_project_setup_sca005_a4_b3_proposal_2026-09-25.md`,
  SHA-256 `46470575625522398fa47d0a39aa09d2b4d252dd89c083ba317f9e577f489422`
  (verified);
- owner ruling `…/_DECISIONS/D-PEC-93_RULING_2026-09-25.md`, SHA-256
  `ffb0b58293d868e1d7ddf61d2958a6b18ca73fa0c36da077f5309a8782153709`
  ("D-PEC-93: A.", recorded by HELP_HUMAN; option A without O and without B1).

## Parameters (as supplied, normalized)

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, revision 1.5, `status: current_basis`. Expected SHA-256 `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` (live bytes match) |
| Companion registers (live) | `ScopeLedger.csv` `83152a94…fd9df`; `Deliverables.csv` `b8628fc4…3d65a`; `ContextBudgetQA.csv` `2a194105…eb0df`; `Companion_Inventory.csv` `7c8a24a8…6ef8` (all equal the accepted revision-1.5 values) |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `SCA005_POSTSETUP` |
| Output folder | `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`, created by `bash tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV SCA005_POSTSETUP` from the worktree root |
| `REQUESTED_BY` | WORKING_ITEMS (node C5, HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`) |
| `PRIOR_RUN_LABEL` | `COV_SCA005_POSTCHANGE_2026-09-25_1344`. Its `coverage_summary.json` hashes to `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` (verified; equals the SCA-005 `Post_Change_Coverage.json`) |
| `EXPECTED_SOURCE_SNAPSHOT` | Decomposition revision 1.5 `current_basis` (`dc2b8479…9660`), SCA-005 closed for scope change only (`_ScopeChange/SCA-005_2026-09-23_2139/`, `CLOSED_FOR_SCOPE_CHANGE_ONLY`), plus the D-PEC-93 poststate: commit `995af4f368d0d8cc0b3134eef484b4b9618aa8ac` on `origin/main` `04e04da00f620a1a5786ee744b167490cc90531c`, run root `projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/` |
| `EXPECTED_HANDOFF_PHASE` | D-PEC-93 post-setup re-audit, after the product writes and before publication |

## Expected results, as briefed (a prediction to test, not a result to reproduce)

- **Cleared:** COV-001/002 (BLOCKER), COV-070/071 (WARNING), COV-068/069
  (INFO), COV-079/080/081 (pre-B3 INFO rows). Forward production-unit
  coverage 100 %.
- **Unchanged:** the three `PRE-EXISTING` v2-artifact-location warnings
  (COV-006/008/042) and COV-077/078 (B1 open).
- **New:** the closure tool's six isolated units (DEL-00-03, DEL-01-05,
  DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05), reported as expected.
- **Carried:** COV-072 may be carried or marked resolved by the SCA-005
  `RUN_SUMMARY.md` correction.
- **Expected verdict:** 0 blockers; overall status WARN.
- **Known disclosed residual, not a defect of the act:** 19 ACTIVE
  EXECUTION rows cite an `EvidenceQuote` that is no longer verbatim
  (proposal finding 1; the owner ruled it carried as a residual). It may be
  recorded at the severity the method assigns, but not as caused by the act.

These IDs are the prior run's (`COV_SCA005_POSTCHANGE_2026-09-25_1344`). This
snapshot numbers its own findings sequentially; `PrePost_Comparison.md` maps
every prior ID to its disposition and its new ID.

## Classification used in this run

Every finding carries one classification in its description:

- `EXPECTED_CONSEQUENCE`: stems from a named decision (the decision clause is
  given in `Decomp_Coverage_Report.md`).
- `PRE-EXISTING`: the condition was present at the prior audited state
  (`COV_SCA005_POSTCHANGE`), whether or not that audit measured it.
- `DEFECT`: anything else. This run found none.

The per-finding delta (`CARRIED`, `CHANGED`, `NEW`, `RESOLVED`) is recorded
separately in `PrePost_Comparison.md`.

## Sealed boundary

- Write only inside this folder; its contents are the method's eight files
  plus `PrePost_Comparison.md`, and nothing else.
- Do not update `_Evaluation/DecompCoverage/_LATEST.md`. The brief overrides
  the method's pointer step: the manager decides the pointer.
- Do not modify any deliverable, register, `_Decomposition/**`,
  `_ScopeChange/**`, the D-PEC-93 run root, docs or any other path.
- No git write (add, commit, stash, checkout, reset, push). Read-only git
  only.
- Deterministic tools run with `PYTHONDONTWRITEBYTECODE=1`; tool output and
  scratch work go to the session scratchpad outside the repository.
- Run the PEC reliance-hold preflight before writing. The result was `ALLOW`
  (`QA_Report.md`).
- Nothing here claims CHECKING, ISSUED, acceptance, readiness or reliance, or
  recommends a lifecycle step. This snapshot is derivative evidence. It
  accepts nothing and authorizes nothing.

## Instruction and method basis (SHA-256, verified before loading)

| File | SHA-256 | Brief value |
|---|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | — |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` | — |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` | — |
| `workflows/audit-decomp/WORKFLOW.md` | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` | match |
| `workflows/audit-decomp/resources/contract.md` | `70a5abebc8ff34826415e1566715373a322baded2939325b5b73828d78401a0c` | match (`70a5abeb…401a0c`) |
| `workflows/audit-decomp/resources/method.md` | `97df84022ccbec434aea9745296b93b6e549ef840acc0ca9df0a215e634d79c2` | match (`97df8402…d79c2`) |
| `tools/scaffolding/create_snapshot_folder.sh` | `2a01157959d7ac8fe55cd621c43ef61118b83370778f3f24cf54a4641fd1c361` | match |

No other role instructions were consulted, and no other workflow or skill
body was loaded. Every other source this run relied on is listed with its
hash in `Decision_Log.md`.
