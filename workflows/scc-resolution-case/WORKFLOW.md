---
name: scc-resolution-case
description: Create or update an SCC resolution case, under `_DAG/cases/<CASE-ID>/` or a project's legacy PKG-00 control deliverable, that accumulates
  bounded TASK findings, evidence, human rulings, candidate remedies, and owner-workflow handoffs until DepClosure can verify closure.
---

# WORKFLOW — scc-resolution-case

## Purpose

Create or update one **SCC Resolution Case** in the project's case home. The case is a living receptacle for repeated bounded TASK work across affected deliverables, human rulings, candidate remedies, owner-workflow handoffs, and eventual DepClosure evidence.

This workflow does not resolve an SCC by itself. It records and organizes the evidence needed for the owning workflows to act.

## Case Home

- **Default:** `{EXECUTION_ROOT}/_DAG/cases/<CASE-ID>/`, in the `_DAG/` tool root registered in `docs/SPEC.md` §1.2 (D-GOV-49). Every project uses this home from D-GOV-49 onward.
- **Legacy:** a project whose cases are already held in a PKG-00 control deliverable (for example `PKG-00_DAG_Closure_and_Project_Control/.../scc-cases/`) may keep using it. Existing cases stay where they are and are not migrated.
- Each project uses one home for its cases; do not split them. Retiring the legacy PKG-00 home is a later decision, once no active project uses it.
- A case under `_DAG/cases/` is a working record, updated in place under this workflow's brief, with Git history as its revision record (`docs/CONTRACT.md` K-SNAP-1; `docs/SPEC.md` §1.2, §11.1). It is not a snapshot folder.

## Case Identity

`audit-dep-closure` numbers SCCs by position within each run (`SCC-001`, `SCC-002`, ...), so an SCC ID names a component only within its closure snapshot. A case is therefore identified by its own `CASE_ID`:

- **Scheme.** A new case takes `SCC-CASE-NNN`: the next unused three-digit number in the project's case home, assigned when the case opens and never reused. A withdrawn or merged case keeps its number and records why. Under `_DAG/cases/`, the folder name is the `CASE_ID`: `_DAG/cases/SCC-CASE-001/`. In a legacy PKG-00 home, existing case IDs and folders are unchanged.
- **Origin.** `Case_Datasheet.md` records the originating closure snapshot, the SCC ID in that snapshot, and the member node set.
- **Matching.** A later closure snapshot's SCC is matched to an existing case by member node set, not by SCC ID. The same set is the same case; if that case is already closed, it is reopened with the new snapshot recorded rather than duplicated. A set that gains or loses members while overlapping one open case stays in that case: record the snapshot, its SCC ID, and the membership change in `Case_Datasheet.md`; do not open a new folder unless the human rules it a different cycle. A set overlapping no case opens a new case. A set overlapping more than one case, or a case whose members split across several SCCs, is recorded as a proposed match for the human to rule on.

## Suitable Shell

- `TASK` in generic shell mode with `ScopePath` set to the case folder, to `{EXECUTION_ROOT}/_DAG/cases/` (for opening a case), or, for the legacy home, to the PKG-00 control deliverable folder.

## Required Inputs

- `ScopePath` — the case folder, `{EXECUTION_ROOT}/_DAG/cases/`, or the legacy PKG-00 control deliverable folder.
- `RuntimeOverrides.CASE_ID` — the stable case ID (see Case Identity), for example `SCC-CASE-001`; for an existing legacy case, its recorded ID.
- `RuntimeOverrides.CASE_PATH` — absolute output folder: `{EXECUTION_ROOT}/_DAG/cases/<CASE-ID>/` by default, or inside `{control-deliverable}/scc-cases/` for the legacy home.
- `RuntimeOverrides.CASE_TITLE` — human-readable case title.
- `RuntimeOverrides.SCC_ID` — SCC identifier in `DEPCLOSURE_SNAPSHOT`; positional within that snapshot, not the case identity.
- `RuntimeOverrides.DEPCLOSURE_SNAPSHOT` — accepted upstream DepClosure snapshot.
- `RuntimeOverrides.AFFECTED_DELIVERABLES` — semicolon-separated deliverable IDs.
- `RuntimeOverrides.CASE_STATE` — one canonical case lifecycle state.

## Case Lifecycle States

- `OPEN_FOR_TASK_WORK`
- `EVIDENCE_ACCUMULATING`
- `HUMAN_RULINGS_PENDING`
- `REMEDY_CLASSIFIED`
- `READY_FOR_OWNER_WORKFLOWS`
- `DEP_CLOSURE_PENDING`
- `CLOSED_BY_DEPCLOSURE`
- `BLOCKED_TBD`

## Read Boundary

Read only:

- the project's case home in scope (`_DAG/cases/`, or the legacy PKG-00 control deliverable);
- existing case files under `CASE_PATH`;
- existing `case-seeds/` artifacts;
- cited DepClosure snapshot evidence;
- explicitly affected product deliverable evidence when needed for case indexing.

Do not scan unrelated packages except to resolve explicitly listed affected deliverables.

## Write Boundary

Write only:

- `{CASE_PATH}/Case_Contract.md`
- `{CASE_PATH}/Case_Datasheet.md`
- `{CASE_PATH}/Task_Findings.csv`
- `{CASE_PATH}/Evidence_Register.csv`
- `{CASE_PATH}/Candidate_Remedies.csv`
- `{CASE_PATH}/Ruling_Register.csv`
- `{CASE_PATH}/Open_Questions.md`
- `{CASE_PATH}/Owner_Workflow_Handoff.md`
- `{CASE_PATH}/Case_QA.md`
- `{CASE_PATH}/case-seeds/` only when preserving prior packet artifacts
- `{CASE_PATH}/_run_records/TASK_RUN_*.md`, or, for the legacy home with `ScopePath` at the PKG-00 control deliverable, `{ScopePath}/_run_records/TASK_RUN_*.md`. When `ScopePath` is `{EXECUTION_ROOT}/_DAG/cases/`, run records go under `CASE_PATH`, never `_DAG/cases/_run_records/`.

Never write:

- product package files;
- any `Dependencies.csv`;
- `_ScopeChange/`;
- `_Reconciliation/`;
- decomposition files.

## Output Contract

`Case_Contract.md` defines contribution rules, TASK deposit protocol, authority limits, and owner-workflow boundaries.

`Case_Datasheet.md` records the `CASE_ID`; the originating closure snapshot, its SCC ID there, and the member node set; each later snapshot matched to the case, with its SCC ID and any membership change; the latest DepClosure baseline; affected deliverables; current case state; and seed artifacts.

`Task_Findings.csv` indexes bounded TASK outputs contributed over time.

`Evidence_Register.csv` indexes all evidence citations used by the case.

`Candidate_Remedies.csv` records remedy candidates per issue/edge with owner workflow and evidence.

`Ruling_Register.csv` records human rulings and disposition state.

`Open_Questions.md` records active human-facing questions.

`Owner_Workflow_Handoff.md` records downstream handoffs by owning workflow.

`Case_QA.md` records validator status, case state, unresolved blockers, and closure boundary.

## Method

1. Load `agents/AGENT_TASK.md`, this workflow, and resources required for the current stage.
2. Resolve `CASE_PATH` and confirm it is in the project's one case home: under `{EXECUTION_ROOT}/_DAG/cases/`, or under the legacy PKG-00 control deliverable that already holds the project's cases. Match the SCC in `DEPCLOSURE_SNAPSHOT` to an existing case by member node set before opening a new one (see Case Identity).
3. Read existing packet seeds and case files when present.
4. Create or update the case receptacle files.
5. Preserve existing packet artifacts as seed evidence, not active WORKING_ITEMS (workflow: scope-change) intake.
6. Keep remedies candidate-level unless supported by human rulings and owner-workflow evidence.
7. Write a TASK run record with outputs and validation notes.

## Non-Negotiable Constraints

- Do not claim dependency rows were changed.
- Do not claim an SCC was closed unless a cited DepClosure snapshot proves it.
- Do not claim WORKING_ITEMS (workflow: scope-change) was initiated.
- Do not claim project-wide blocker status.
- Unknowns remain `TBD`.
- Every candidate remedy must cite evidence or carry a `TBD` reason.
- WORKING_ITEMS (workflow: scope-change) is one possible owner workflow, not the default remedy.
