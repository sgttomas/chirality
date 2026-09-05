# INIT-TASK Brief — DEL-09-07

**State:** `GATE4_REVISION_5_DRAFT_NOT_DISPATCHED`
**Dispatcher:** PROJECT_SETUP
**Executor:** PREPARATION, Task C
**Authority prerequisite:** the exact Gate-4 revision-5 package has passed independent review and been owner-authorized for revised Gate-5 execution. This Task-C brief is executed before the candidate post-change audit; SCA-APP-009 is not yet current and `_ScopeChange/_LATEST.md` must not move.
**Basis prerequisite:** exact accepted post-amendment decomposition identifies DEL-09-07 as `Two-Job Runtime-Control Installer Migration and Rollback`, under PKG-09, Type `MIGRATION_SCRIPT`, Context Envelope `M`, Responsible Party `TBD`, covering SOW-080 and OBJ-008.

## Objective

Create the canonical metadata scaffold for exactly one new deliverable:

`projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/`

This is structural initialization only within the pre-pointer Gate-5 transaction. First create and validate the five files in the disposable candidate mirror before its post-change audit. If and only if that audit and independent review pass the revised Gate-5 criteria, the same five reviewed bytes may be materialized by PREPARATION in the actual Gate-5 worktree before the pointer sub-gate. Do not produce installer code, tests, scripts, signing/notarization material, release artifacts, release-readiness claims, working-item prose, dependency conclusions, or any other deliverable/package.

## Required context

Read completely before acting:

1. root `AGENTS.md` and `agents/AGENT_PREPARATION.md`;
2. `projects/chirality-app-dev/AGENTS.md`;
3. the candidate SCA-APP-009 `Brief.md`, `Amendment_Actions.csv`, revised `Propagation_Plan.md`, and revised `Decision_Log.md`; final `Handoff_State.md` and `RUN_SUMMARY.md` do not yet exist and must not be required or inferred;
4. the accepted post-amendment rows for PKG-09, DEL-09-07, SOW-080, OBJ-008, OI-003, and OI-007;
5. the nearest current PKG-09 deliverable scaffolds for layout only.

Do not treat existing deliverable-local MEMORY as authority. If a status is read and a sibling `_MEMORY.md`/`MEMORY.md` is present, read both and record any material caveat as operational evidence.

## Complete PREPARATION Task-C input from PROJECT_SETUP

```yaml
TASK_TYPE: C
DEL_ID: DEL-09-07
DEL_NAME: Two-Job Runtime-Control Installer Migration and Rollback
PKG_ID: PKG-09
PKG_NAME: Validation, Packaging, Security, and Release
DISCIPLINE: NOT_PRESENT_IN_ACCEPTED_DECOMPOSITION
TYPE: MIGRATION_SCRIPT
RESPONSIBLE: TBD
DESCRIPTION: Provide the App-side installer transaction for two Root-owned launchd jobs through Root-owned runtime-control IPC, with staging, effective-state inspection, rollback, upgrade/uninstall, and cleanup evidence.
ANTICIPATED_ARTIFACTS: Two-job installer/migration script; transaction journal; effective-state inspector; rollback, upgrade, uninstall, and cleanup fixtures and evidence
DECOMPOSITION_REF: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md
COORDINATION_MODE: NOT_TRACKED
DECLARED_UPSTREAM_DEPENDENCIES: NONE
DECLARED_DOWNSTREAM_DEPENDENCIES: NONE
```

The accepted decomposition has no `DISCIPLINE` field for SOFTWARE deliverables. `NOT_PRESENT_IN_ACCEPTED_DECOMPOSITION` is the truthful source state, not an invented discipline. If PREPARATION or its deterministic schema cannot accept that value, PROJECT_SETUP must stop and obtain an explicit human/schema direction; it must not substitute, infer, or assign a discipline.

Exact reference materials supplied by PROJECT_SETUP:

| Ref | Exact path/source | Accepted identity/use |
| --- | --- | --- |
| TASKC-REF-001 | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Accepted Gate-3 post-image SHA-256 `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`; PKG-09 line 275, SOW-080 lines 242/471, DEL-09-07 line 372, DEC-024 line 616. |
| TASKC-REF-002 | `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-009_2026-09-04_0944_App_V3_Pathway_Seating/Brief.md` | Candidate SCA initiation/boundary record; not evidence that `_LATEST.md` has moved. |
| TASKC-REF-003 | `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-009_2026-09-04_0944_App_V3_Pathway_Seating/Amendment_Actions.csv` | Exact 16-row ledger SHA-256 `46273d39b991551326688fac9d5f4f8381b181503bdf38aced4a94d46223c2b6`; actions 7-8. |
| TASKC-REF-004 | revised Gate-4 `Propagation_Plan.md` and `Decision_Log.md` | Exact pre-pointer PREPARATION authority, retained exclusions, and current gate state. |
| TASKC-REF-005 | `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Carrier_Map.md` | Immutable proposed-history evidence SHA-256 `72a1b55b5307b6df5131011e30581e323737e95f3bcf85471121481ded25b619`; WP-03 is evidence, not current decomposition authority. |
| TASKC-REF-006 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/MAPPING.md` | Seating-gap evidence SHA-256 `99ba8fb24a40a0eaafc37465a8f5c47b84d57cdc21eac3faa7280ba890b076c8`; MAPPING S-2. |

The accepted decomposition's REF-001 through REF-007 table remains the governing source-corpus reference list for `_REFERENCES.md`. PREPARATION must extract those exact rows from the accepted decomposition at dispatch; a mismatch is reported to PROJECT_SETUP and is not silently reconciled.

## Exact allowed write targets

- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/_CONTEXT.md`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/_REFERENCES.md`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/_DEPENDENCIES.md`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/_SEMANTIC.md`

No other path may change. A pre-existing target folder or any extra required file is a collision/blocker, not permission to expand scope.

## Required initialization

- Use the governed PREPARATION/scaffolding method, idempotently, for one deliverable.
- `_STATUS.md` initial lifecycle is exactly `OPEN`. Do not set a checking/approval SHA, add a `Remaining` item, or claim acceptance/readiness.
- `_CONTEXT.md` must copy the complete Task-C input exactly, including `Responsible: TBD`, Type `MIGRATION_SCRIPT`, Context Envelope `M`, and the truthful `Discipline: NOT_PRESENT_IN_ACCEPTED_DECOMPOSITION`; cite the exact accepted decomposition and candidate SCA-APP-009; preserve Root DEL-02-07/DEL-02-11 control/storage boundaries, the DEL-02-06 implementation act, F-APP-2, D-APP-97, and the G5/G6 release gates.
- `_DEPENDENCIES.md` is a `NOT_TRACKED` initialization stub with declared upstream and downstream dependencies both `NONE`, pending downstream TASK + `dependency-extract`; do not infer or hand-invent any edge.
- `_REFERENCES.md` contains only the accepted authority pointers supplied in this brief or extracted byte-faithfully from REF-001 through REF-007 in the accepted decomposition.
- `_SEMANTIC.md` remains the empty standard placeholder created by the scaffold tool (zero bytes); do not generate semantic content or matrices.

## Acceptance checks

1. Exact folder name and exactly the five authorized files exist; `ScopeOfWork.md`, `MEMORY.md`, and `Dependencies.csv` are absent.
2. No other path changed.
3. `_STATUS.md` is `OPEN` and contains no approval/readiness assertion.
4. DEL-09-07 identity is PKG-09 / `MIGRATION_SCRIPT` / `M` / `ResponsibleParty: TBD` / SOW-080 / OBJ-008; description and anticipated artifacts are byte-faithful to candidate line 372.
5. Root/App authority boundaries and F-APP-2/D-APP-97 are not weakened.
6. Dependency content is explicitly `NOT_TRACKED`, declares no edges, and remains pending the owning extraction workflow.
7. `_SEMANTIC.md` is the empty standard placeholder.
8. `git diff --check` passes and the project scaffolding/status validation applicable to PREPARATION passes.

## Return contract

Return the exact changed-file list, per-file SHA-256, commands/results, collision status, and candidate-mirror validation result to SCOPE_CHANGE. Freeze the five candidate bytes for exact later actual-worktree parity. Stop. Do not hand off to WORKING_ITEMS, create `ScopeOfWork.md`, `MEMORY.md`, or `Dependencies.csv`, move `_LATEST.md`, commit, push, enter production, or dispatch another agent.
