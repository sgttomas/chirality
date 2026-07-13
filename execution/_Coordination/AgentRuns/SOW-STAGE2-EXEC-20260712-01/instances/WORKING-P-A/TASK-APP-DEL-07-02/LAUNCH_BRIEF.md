# TASK-APP-DEL-07-02 Sealed Brief — v2

PURPOSE: Independently verify the exact App DEL-07-02 Stage-2 pilot replacement candidate without repair.
RequestedBy: WORKING-P-A
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-P-A
ChildInstanceID: TASK-APP-DEL-07-02
PackageID: APP-PKG-07
DeliverableID: DEL-07-02

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/workspace/target_state
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-02_Execution_Root_Scaffolding_from_Decomposition
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/workspace/target_state
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0d260eb024d8b8dada0df477b70ac880a6906ffa
  PROJECT_SCOPE_REFS: projects/chirality-app-dev/docs/PRD.md; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-02_Execution_Root_Scaffolding_from_Decomposition/_CONTEXT.md
  PACKAGE_OBJECTIVE_REFS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md PKG-07; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-02_Execution_Root_Scaffolding_from_Decomposition/_CONTEXT.md
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@0d260eb024d8b8dada0df477b70ac880a6906ffa
  - P3_MANIFEST B1/G3 PASS exact row for DEL-07-02
  - Stage-1 App evidence commit fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26
  - PILOT-VALIDATION-001 active cross-lane correction
  - candidate SHA-256 80fbd86600af8516d75d2d11ccf53d304ec36426069728fbe30a8fceb846d952
  - Datasheet 73076f5533d9e7fef29e6428f9fffeca88c1400a7dfd1e72f0a46524238a5078
  - Specification f68633966fee53f7e14233dbb0399c534bd67b930b3ffa428b7331e2bb47cee9
  - Guidance 2d8fce727eace8649b6d8158e5a08a4ed07d68425b2fde3f9fa23e53c3aa2e0a
  - Procedure 2e4bc6207923fd97c83fd02bae60cc0e8e6c831d04e1412059221529cd259752
  - _STATUS 65a15cff6be7500523b3c1097d2432fa60279288256287aca9b90d96e870b98d

Tasks:
  - Read complete agents/AGENT_TASK.md and all live skills/scope-of-work method files before acting. Do not delegate.
  - Read exactly the named P3 DEL-07-02 row, the named live four sources and _STATUS/control references, the extracted candidate under candidates/P4_PILOTS/APP-PKG07/DEL-07-02/, active SOW tools, Stage-1 inventory, and Stage-1 evidence/DEL-07 evidence.
  - Confirm `target_state/legacy_source` is byte-equal to the live four sources/_STATUS and `target_state/ScopeOfWork.md` is byte-equal to the extracted candidate; do not edit those seeded truth copies.
  - Under PILOT-VALIDATION-001, validate the current live/P3-bound legacy-only state as `LEGACY_FOUR_DOC` with no SOW, and validate `target_state` as target-only `SOW_V1` with no legacy production files at its root. Do not invoke isolated-dual validation.
  - Reproduce the remaining full pilot gate: exact hashes/current-base equality; claim map and every target resolution; parity and source-line preservation; deterministic checklist twice; HTML render twice with byte stability/script/external-resource safety; lifecycle/control containment; Stage-1 evidence identity; separate schema/content, preservation, and substrate verdicts.
  - Emit an exact five-path future replacement manifest: ADD ScopeOfWork.md at candidate hash and DELETE the four legacy production paths at their P3 hashes. This is evidence only; do not modify the live project.
  - Write detailed evidence and terminal RETURN.md/STATUS.json only in this child instance. Any discrepancy returns FAIL; never repair.
  - Do not insert a D-GOV-16 marker, invoke conversion, overlay the legacy and target formats, treat the D-GOV-15 provenance marker as migration authority, or modify the candidate.

ExpectedOutputs:
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/workspace/target_state/_run_records/TASK_RUN_*.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/workspace/target_state/evidence/**
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/RETURN.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/STATUS.json
  - evidence includes SOURCE_HASHES.tsv, validation/map/parity/checklist/render artifacts, REPLACEMENT_MANIFEST.tsv, and CHECKS.md

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/chirality-app-dev/** write
  - candidate edits or regeneration
  - Git/index/ref/branch/PR writes
  - lifecycle/control/receipt/release/H1/H2/retirement writes
  - delegation
