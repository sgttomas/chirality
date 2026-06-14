# Source Pack: Skill pack: scc-resolution-case

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/scc-resolution-case/BRIEF_SCHEMA.md

### BRIEF SCHEMA — scc-resolution-case

Use this skill when WORKING_ITEMS needs to create or update a PKG-00 SCC case file.

#### Required Fields

```yaml
PURPOSE: Create or update one SCC resolution case.
RequestedBy: WORKING_ITEMS
ScopePath: /abs/path/to/DEL-00-XX_...
TaskSkill: scc-resolution-case
ApplyEdits: true
AllowedWriteTargets:
  - /abs/path/to/DEL-00-XX_.../scc-cases/<case-folder>/
  - /abs/path/to/DEL-00-XX_.../_run_records/
RuntimeOverrides:
  CASE_ID: CASE-SCC-002
  CASE_PATH: /abs/path/to/DEL-00-XX_.../scc-cases/<case-folder>
  CASE_TITLE: SCC-002 PKG-10 Policy Proposal
  SCC_ID: SCC-002
  DEPCLOSURE_SNAPSHOT: /abs/path/to/execution/_Reconciliation/DepClosure/CLOSURE_...
  AFFECTED_DELIVERABLES: DEL-10-02;DEL-10-03
  CASE_STATE: OPEN_FOR_TASK_WORK
ExpectedOutputs:
  - Case_Contract.md
  - Case_Datasheet.md
  - Task_Findings.csv
  - Evidence_Register.csv
  - Candidate_Remedies.csv
  - Ruling_Register.csv
  - Open_Questions.md
  - Owner_Workflow_Handoff.md
  - Case_QA.md
```

#### Optional Runtime Overrides

- `SEED_PACKET_PATHS` — semicolon-separated paths to prior packets to preserve under `case-seeds/`.
- `SCC_NODE_SET` — semicolon-separated SCC node set.
- `FOCUS_PAIRS` — semicolon-separated bidirectional pairs.

#### Required Custom Instructions

- Treat existing scope-change packets as seed evidence, not active SCOPE_CHANGE intake.
- Do not edit product deliverables, dependency registers, decomposition files, `_ScopeChange/`, or `_Reconciliation/`.
- Do not report SCC closure or project-wide blocked/unblocked status.


## Component: skills/scc-resolution-case/QA_CHECKS.md

### QA CHECKS — scc-resolution-case

#### Required Checks

- Required case files exist.
- Required CSV columns are present.
- `CaseState` is one of the canonical lifecycle states.
- Every candidate remedy has evidence or a `TBD` reason.
- Every owner handoff names an owning workflow.
- Case text does not claim SCC closure unless cited DepClosure evidence proves it.
- PKG-00 contains no `Dependencies.csv`.
- Seed packets, when present, are labeled seed evidence and not active SCOPE_CHANGE intake.

#### Closure Boundary

`CLOSED_BY_DEPCLOSURE` is valid only when `Case_QA.md` cites a follow-up DepClosure snapshot proving the SCC is absent or otherwise formally accepted by the owning reconciliation workflow.


## Component: skills/scc-resolution-case/SKILL.md

---
name: scc-resolution-case
description: Create or update a PKG-00 SCC resolution case that accumulates bounded TASK findings, evidence, human rulings, candidate remedies, and owner-workflow handoffs until DepClosure can verify closure.
compatibility: Chirality TASK in generic shell mode; dispatched by WORKING_ITEMS for PKG-00 SCC case coordination.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — scc-resolution-case

#### Purpose

Create or update one **SCC Resolution Case** under a PKG-00 control deliverable. The case is a living receptacle for repeated bounded TASK work across affected deliverables, human rulings, candidate remedies, owner-workflow handoffs, and eventual DepClosure evidence.

This skill does not resolve an SCC by itself. It records and organizes the evidence needed for the owning workflows to act.

#### Suitable Shell

- `TASK` in generic shell mode with `ScopePath` set to a PKG-00 control deliverable folder or to the case folder itself.

#### Required Inputs

- `ScopePath` — PKG-00 control deliverable folder or case folder.
- `RuntimeOverrides.CASE_ID` — local case ID, for example `CASE-SCC-002`.
- `RuntimeOverrides.CASE_PATH` — absolute output folder inside `{control-deliverable}/scc-cases/`.
- `RuntimeOverrides.CASE_TITLE` — human-readable case title.
- `RuntimeOverrides.SCC_ID` — SCC identifier from DepClosure.
- `RuntimeOverrides.DEPCLOSURE_SNAPSHOT` — accepted upstream DepClosure snapshot.
- `RuntimeOverrides.AFFECTED_DELIVERABLES` — semicolon-separated deliverable IDs.
- `RuntimeOverrides.CASE_STATE` — one canonical case lifecycle state.

#### Case Lifecycle States

- `OPEN_FOR_TASK_WORK`
- `EVIDENCE_ACCUMULATING`
- `HUMAN_RULINGS_PENDING`
- `REMEDY_CLASSIFIED`
- `READY_FOR_OWNER_WORKFLOWS`
- `DEP_CLOSURE_PENDING`
- `CLOSED_BY_DEPCLOSURE`
- `BLOCKED_TBD`

#### Read Boundary

Read only:

- the PKG-00 control deliverable in scope;
- existing case files under `CASE_PATH`;
- existing `case-seeds/` artifacts;
- cited DepClosure snapshot evidence;
- explicitly affected product deliverable evidence when needed for case indexing.

Do not scan unrelated packages except to resolve explicitly listed affected deliverables.

#### Write Boundary

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
- `{ScopePath}/_run_records/TASK_RUN_*.md` or `{CASE_PATH}/_run_records/TASK_RUN_*.md`

Never write:

- product package files;
- any `Dependencies.csv`;
- `_ScopeChange/`;
- `_Reconciliation/`;
- decomposition files.

#### Output Contract

`Case_Contract.md` defines contribution rules, TASK deposit protocol, authority limits, and owner-workflow boundaries.

`Case_Datasheet.md` records SCC identity, node set, latest DepClosure baseline, affected deliverables, current case state, and seed artifacts.

`Task_Findings.csv` indexes bounded TASK outputs contributed over time.

`Evidence_Register.csv` indexes all evidence citations used by the case.

`Candidate_Remedies.csv` records remedy candidates per issue/edge with owner workflow and evidence.

`Ruling_Register.csv` records human rulings and disposition state.

`Open_Questions.md` records active human-facing questions.

`Owner_Workflow_Handoff.md` records downstream handoffs by owning workflow.

`Case_QA.md` records validator status, case state, unresolved blockers, and closure boundary.

#### Method

1. Load `AGENT_TASK.md`, this skill, and companion files.
2. Resolve `CASE_PATH` and confirm it is under a PKG-00 control deliverable.
3. Read existing packet seeds and case files when present.
4. Create or update the case receptacle files.
5. Preserve existing packet artifacts as seed evidence, not active SCOPE_CHANGE intake.
6. Keep remedies candidate-level unless supported by human rulings and owner-workflow evidence.
7. Write a TASK run record with outputs and validation notes.

#### Non-Negotiable Constraints

- Do not claim dependency rows were changed.
- Do not claim an SCC was closed unless a cited DepClosure snapshot proves it.
- Do not claim SCOPE_CHANGE was initiated.
- Do not claim project-wide blocker status.
- Unknowns remain `TBD`.
- Every candidate remedy must cite evidence or carry a `TBD` reason.
- SCOPE_CHANGE is one possible owner workflow, not the default remedy.


## Component: skills/scc-resolution-case/TOOL_POLICY.md

### TOOL POLICY — scc-resolution-case

#### Tool Posture

Reasoning-first case organization. No deterministic helper is required to author case files.

#### Preferred Validation

After case creation or update, run:

```sh
python3 tools/validation/validate_scc_resolution_case.py <case-folder>
```

Do not claim validator PASS unless it actually ran and passed.

#### Disallowed Tool Effects

- No writes outside `CASE_PATH` and scoped `_run_records/`.
- No mutation of product deliverables.
- No mutation of `Dependencies.csv`.
- No mutation of `_ScopeChange/`, `_Reconciliation/`, or decomposition authority.
