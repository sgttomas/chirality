# Brief H9 — draft D-PEC-95: revision-1.5 currency packet (read-only TASK)

Parent: HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`. Work graph: `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` (on branch `claude/pec-post-sca005-graph`, PR #919), nodes N1–N3 and T1. Role: TASK (Type 2). No delegation. Model steer: `claude-opus-5-5`, high.

## Why

After SCA-005 and D-PEC-93, several derivative surfaces still describe earlier states. Under `projects/pec/AGENTS.md` §"Write Scopes And Fences", the fenced parts need an owner-ruled packet. Draft `D-PEC-95` in the D-PEC-93 format, including a deterministic generator with fail-closed checks, so the owner can rule on one bounded currency act.

## Basis (read; record SHA-256)

- **Checkout:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5`. Use `origin/main` `13df8b795e47ab2284018eeefc9d5473d00c232d` as the preimage commit. Read it with `git show` or `git archive`. The local checkout is on a different branch; do not change it.
- **Precedent:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-93_project_setup_sca005_a4_b3_proposal_2026-09-25.md`, its ruling, and its preparation folder `_Coordination/PROJECT_SETUP_SCA005_A4_B3_PREP_2026-09-25/`. That folder includes `gen_d93_b1.py`, the B1 re-pin generator prepared against the pre-D-PEC-93 tree. Re-derive it; do not reuse its bytes.
- **The run root and re-audit of D-PEC-93:**
  - `_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/` (the `HANDOFF_STATE.md` residuals);
  - `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/` (COV-072 names the 19 stale evidence quotes; COV-068/069 the context and reference revisions; COV-073 the stale records).
- **SCA-005 records:** `_ScopeChange/SCA-005_2026-09-23_2139/` (`Handoff_State.md`, `RUN_SUMMARY.md`, `Propagation_Plan.md` §B1 and §B8), `_ScopeChange/_LATEST.md`, `_Decomposition/_LATEST.md`, `execution/_Coordination/_COORDINATION.md`.
- **Task Management:** `execution/_Coordination/_TaskManagement/REGISTER.csv` (row TM-PEC-023) and `workflows/task-management/` for the disposition method.

## Task

Draft `D-PEC-95` with exact acts for:

- **N1.** Present-current text only. The currency surfaces are:
  - `_Decomposition/_LATEST.md` and `_ScopeChange/_LATEST.md` (the post-setup audit reading and derivative state after D-PEC-93);
  - the SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` (a dated outcome note that the re-audit and A4/B3 were done under D-PEC-93, with no rewrite of history);
  - `_COORDINATION.md` (its revision-1.4 `current_basis` and any other false present-tense lines).

  For each file, say whether it is fenced. `_COORDINATION.md` is under default-writable `execution/_Coordination/**`.
- **N2.** Re-pin the 42 `_CONTEXT.md` files still at revision 1.4 and the 64 `_REFERENCES.md` files still at revision 1.4 to revision 1.5. Leave semantic fields untouched. Use a deterministic generator against the current tree, with exact anchors and a fail-closed population check. Name every path.
- **N3.** Refresh the 19 stale `EvidenceQuote` cells in their `Dependencies.csv` files. Each new quote must be verbatim in its cited file at revision 1.5 / PRD v2.3. Include before and after text per row, `LastSeen` handling, and the `Notes` convention. Keep every other cell and every row identity unchanged.
- **T1.** Draft the TM-PEC-023 disposition to `RESOLVED_BY_DECISION`, citing SCA-005 checkpoint acceptance and D-PEC-92. State whether the task-management method lets this be applied as a record of existing owner decisions, or needs a new owner act. If it needs one, make it an owner question in the packet.

Also include:
- **Verification:**
  - strict registers 0/0;
  - `analyze_dep_closure.py` unchanged (111 edges, 0 SCCs);
  - every `EvidenceQuote` verbatim;
  - every context and reference names revision 1.5;
  - the receipts validator unaffected;
  - a re-audit, if proportionate: recommend or not. If you recommend one, whether it moves the audit pointer.
- Options: recommended, narrower, amend, defer.
- An exact product grant with a preimage SHA-256 for every existing file touched.
- Rollback: a revert PR.
- Limits: no SOW, `v2/**`, PRD, decomposition-register content or lifecycle change; no CHECKING, ISSUED or acceptance.
- The owner questions.

Prototype on a `git archive` export in your own `mktemp -d` directory, and report exit codes and counts. Run `pec_reliance_hold.py` with `exact-correction-preparation` on the targets.

## Limits

Read-only on the repository. Write only to `<scratchpad>/h9/` (the draft `D-PEC-95_DRAFT.md`, generators and small evidence, with `SHA256SUMS`) and to your own temporary directory. Delete large exports. Status line: `PROPOSAL / AWAITING_RULING`, prepared by TASK under HELP_HUMAN.

## Return

- draft path and SHA-256;
- the recommended option;
- counts per item;
- prototype results;
- owner questions;
- anything unresolved.
