# Source Pack: Skill pack: scope-change-packet

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/scope-change-packet/BRIEF_SCHEMA.md

### BRIEF SCHEMA — scope-change-packet

Use this skill when WORKING_ITEMS needs one PKG-00 control deliverable to produce a SCOPE_CHANGE-consumable packet.

#### Required Fields

```yaml
PURPOSE: Produce one Scope Change Consumable Packet.
RequestedBy: WORKING_ITEMS
ScopePath: /abs/path/to/DEL-00-XX_...
TaskSkill: scope-change-packet
ApplyEdits: true
AllowedWriteTargets:
  - /abs/path/to/DEL-00-XX_.../scope-change-packets/<packet-folder>/
  - /abs/path/to/DEL-00-XX_.../_run_records/
RuntimeOverrides:
  PACKET_ID: PKG00-SCA-PACKET-001
  PACKET_PATH: /abs/path/to/DEL-00-XX_.../scope-change-packets/<packet-folder>
  PACKET_TITLE: SCC-002 PKG-10 Policy Proposal
  SCC_ID: SCC-002
  DECOMP_VARIANT: SOFTWARE
  DECOMPOSITION_PATH: /abs/path/to/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md
  DEPCLOSURE_SNAPSHOT: /abs/path/to/execution/_Reconciliation/DepClosure/CLOSURE_...
  AFFECTED_DELIVERABLES: DEL-10-02;DEL-10-03
  FOCUS_ROWS: DEP-10-02-004;DEP-10-03-006
ExpectedOutputs:
  - Packet_Contract.md
  - Packet_Datasheet.md
  - Packet_Specification.md
  - Packet_Procedure.md
  - Packet_Rationale.md
  - SCOPE_CHANGE_INIT.md
  - Proposed_SCA_Actions.csv
  - Affected_Surfaces.csv
  - Evidence_Index.csv
  - Packet_QA.md
```

#### Optional Runtime Overrides

- `BIDIRECTIONAL_PAIRS` — semicolon-separated pair labels for SCC-001 packet subsets.
- `PACKET_SCOPE_NOTE` — extra bounded framing.
- `MAX_ACTIONS` — soft cap on proposed actions.

#### Required Custom Instructions

- Treat packet outputs as proposals and evidence only.
- Do not edit product deliverables, dependency registers, decomposition files, `_ScopeChange/`, or `_Reconciliation/`.
- Do not report SCC closure or project-wide blocked/unblocked status.
- Keep `SCOPE_CHANGE_INIT.md` human-initiated and gate-controlled.


## Component: skills/scope-change-packet/QA_CHECKS.md

### QA CHECKS — scope-change-packet

#### Required Checks

- Required ten packet files exist.
- Required CSV columns are present.
- Every `Proposed_SCA_Actions.csv` row has non-empty `EvidenceRefs`.
- Every affected deliverable ID exists in the current decomposition authority or is explicitly marked `TBD`.
- Packet text does not claim:
  - dependency rows were changed;
  - SCC closure was achieved;
  - SCOPE_CHANGE was initiated;
  - project-wide blocked/unblocked state is reportable.
- PKG-00 contains no `Dependencies.csv`.
- `SCOPE_CHANGE_INIT.md` states that human initiation is required.

#### Readiness Verdict

Use one of:

- `READY_FOR_HUMAN_REVIEW`
- `SELECTED_FOR_SCOPE_CHANGE_INTAKE`
- `BLOCKED_TBD`

`READY_FOR_HUMAN_REVIEW` requires all required files, evidence-backed proposed actions, and no blocking validator failures. It means the packet is structurally complete enough for review.

`SELECTED_FOR_SCOPE_CHANGE_INTAKE` is not a TASK-authored default. Use it only after a human explicitly selects the packet as a SCOPE_CHANGE seed. It does not bypass SCOPE_CHANGE gates.

## Component: skills/scope-change-packet/SKILL.md

---
name: scope-change-packet
description: Produce a bounded PKG-00 Scope Change Consumable Packet for later human-initiated SCOPE_CHANGE intake; use scc-resolution-case for active SCC resolution receptacles.
compatibility: Chirality TASK in generic shell mode; dispatched by WORKING_ITEMS for PKG-00 control deliverables.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — scope-change-packet

#### Purpose

Produce one **Scope Change Consumable Packet** under a PKG-00 control deliverable. The packet prepares evidence, proposed actions, affected-surface inventories, and a human-readable SCOPE_CHANGE seed request.

The packet is not an amendment, not a dependency ruling, and not a DepClosure result. It is a bounded staging artifact for a later human-initiated SCOPE_CHANGE workflow.

For active SCC resolution work, use `TASK + scc-resolution-case`. Existing scope-change packets may be retained as seed evidence inside an SCC Resolution Case.

#### Suitable Shell

- `TASK` in generic shell mode with `ScopePath` set to one PKG-00 control deliverable folder.

#### Required Inputs

- `ScopePath` — one PKG-00 control deliverable folder.
- `RuntimeOverrides.PACKET_ID` — local packet ID, for example `PKG00-SCA-PACKET-001`.
- `RuntimeOverrides.PACKET_PATH` — absolute output folder inside `{ScopePath}/scope-change-packets/`.
- `RuntimeOverrides.PACKET_TITLE` — human-readable packet title.
- `RuntimeOverrides.SCC_ID` — `SCC-001` or `SCC-002`.
- `RuntimeOverrides.DECOMP_VARIANT` — `SOFTWARE`.
- `RuntimeOverrides.DECOMPOSITION_PATH` — current decomposition authority.
- `RuntimeOverrides.DEPCLOSURE_SNAPSHOT` — accepted upstream DepClosure snapshot.
- `RuntimeOverrides.AFFECTED_DELIVERABLES` — semicolon-separated deliverable IDs.
- `RuntimeOverrides.FOCUS_ROWS` — semicolon-separated dependency row IDs or `TBD`.

#### Read Boundary

Read only:

- the PKG-00 control deliverable in `ScopePath`;
- PKG-00 package-level control files;
- the cited decomposition document;
- the cited DepClosure snapshot and evidence files;
- affected product deliverable `_CONTEXT.md`, `_STATUS.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and four-doc kit files.

Do not scan unrelated packages except as needed to resolve explicitly listed affected deliverables.

#### Write Boundary

Write only:

- `{PACKET_PATH}/Packet_Contract.md`
- `{PACKET_PATH}/Packet_Datasheet.md`
- `{PACKET_PATH}/Packet_Specification.md`
- `{PACKET_PATH}/Packet_Procedure.md`
- `{PACKET_PATH}/Packet_Rationale.md`
- `{PACKET_PATH}/SCOPE_CHANGE_INIT.md`
- `{PACKET_PATH}/Proposed_SCA_Actions.csv`
- `{PACKET_PATH}/Affected_Surfaces.csv`
- `{PACKET_PATH}/Evidence_Index.csv`
- `{PACKET_PATH}/Packet_QA.md`
- `{ScopePath}/_run_records/TASK_RUN_*.md`

Never write:

- product package files;
- any `Dependencies.csv`;
- `_ScopeChange/`;
- `_Reconciliation/`;
- decomposition files.

#### Output Contract

Each packet must contain the fixed ten-file set named above.

`Packet_Contract.md` defines consumption rules, authority limits, SCOPE_CHANGE gate mapping, and non-goals.

`Packet_Datasheet.md` records identity, SCC baseline, affected deliverables, affected rows, and evidence inventory.

`Packet_Specification.md` records proposed amendment requirements, action candidates, acceptance criteria, and invariant checks.

`Packet_Procedure.md` gives SCOPE_CHANGE intake and gate-by-gate use instructions.

`Packet_Rationale.md` records source-grounded reasoning, why dependency-edge treatment is insufficient, risks, and alternatives rejected.

`SCOPE_CHANGE_INIT.md` is a seed request. It must say it is not valid until the human explicitly initiates SCOPE_CHANGE.

`Proposed_SCA_Actions.csv` uses columns:

```csv
PacketID,ActionSeq,ActionType,EntityType,EntityID,Description,AffectedDeliverables,AffectedFiles,EvidenceRefs,SCOPE_CHANGE_Gate,Status
```

`Affected_Surfaces.csv` uses columns:

```csv
PacketID,SurfaceType,SurfacePath,PackageRole,ChangeClass,OwnerWorkflow,RequiredAction,EvidenceRefs,Status
```

`Evidence_Index.csv` uses columns:

```csv
EvidenceID,SourcePath,SourceRef,EvidenceType,Supports,Notes
```

`Packet_QA.md` records checklist results, unresolved TBDs, and packet readiness verdict. The verdict must distinguish structural packet validity from SCOPE_CHANGE intake acceptance.

#### Method

1. Load `AGENT_TASK.md`, this skill, and companion files.
2. Resolve `PACKET_PATH` and confirm it is inside `ScopePath`.
3. Read PKG-00 control files and deliverable-local packet context.
4. Read the cited DepClosure evidence for the target SCC.
5. Read only explicitly affected product deliverables and dependency registers.
6. Produce the packet file set using evidence-grounded statements.
7. Keep proposed SCOPE_CHANGE actions conservative:
   - use `MODIFY` for decomposition text, package/deliverable metadata, or scope-ledger clarification;
   - use `RECLASSIFY`, `MERGE`, `SPLIT`, `ADD`, or `REMOVE` only when the evidence clearly requires structural amendment framing;
   - use `TBD` where the action requires human or SCOPE_CHANGE ruling.
8. Write a TASK run record with outputs, evidence read, and validation notes.

#### Non-Negotiable Constraints

- Do not claim any dependency row was changed.
- Do not claim any SCC was closed.
- Do not claim SCOPE_CHANGE was initiated.
- Do not claim project-wide blocker status.
- Unknowns remain `TBD`.
- Every proposed action must cite at least one evidence row in `Evidence_Index.csv`.
- Packet readiness means the packet is structurally complete enough for human review. It is not SCOPE_CHANGE intake acceptance unless a human explicitly selects the packet for SCOPE_CHANGE.

## Component: skills/scope-change-packet/TOOL_POLICY.md

### TOOL POLICY — scope-change-packet

#### Tool Posture

Reasoning-first packet production. No deterministic helper is required to author a packet.

#### Preferred Validation

After packet creation, run:

```sh
python3 tools/validation/validate_scope_change_packet.py <packet-folder>
```

Do not claim validator PASS unless it actually ran and passed.

#### Disallowed Tool Effects

- No writes outside `PACKET_PATH` and `_run_records/`.
- No mutation of product deliverables.
- No mutation of `Dependencies.csv`.
- No mutation of `_ScopeChange/`, `_Reconciliation/`, or decomposition authority.
