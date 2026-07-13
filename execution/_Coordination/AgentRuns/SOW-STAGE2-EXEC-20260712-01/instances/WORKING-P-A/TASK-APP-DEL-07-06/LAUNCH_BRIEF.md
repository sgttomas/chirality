# TASK-APP-DEL-07-06 Sealed Brief — v2

PURPOSE: Independently verify the exact App DEL-07-06 Stage-2 pilot replacement candidate without repair.
RequestedBy: WORKING-P-A
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-P-A
ChildInstanceID: TASK-APP-DEL-07-06
PackageID: APP-PKG-07
DeliverableID: DEL-07-06

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/workspace/target_state
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/workspace/target_state
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0d260eb024d8b8dada0df477b70ac880a6906ffa
  PROJECT_SCOPE_REFS: projects/chirality-app-dev/docs/PRD.md; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/_CONTEXT.md
  PACKAGE_OBJECTIVE_REFS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md PKG-07; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/_CONTEXT.md
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@0d260eb024d8b8dada0df477b70ac880a6906ffa
  - P3_MANIFEST B1/G3 PASS exact row for DEL-07-06
  - Stage-1 App evidence commit fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26
  - PILOT-VALIDATION-001 active cross-lane correction
  - candidate SHA-256 6de59e2a9d6806fb620c673b1da4822337b4c531a41de3186c9f0fde8e10b93e
  - Datasheet 86b4c8ae102e9d3389b9b67023109be337e2ec2b5144d651edc9c557ce622e39
  - Specification 52a779316bf5f3b47bdd0939e70c444050769501e1eaddfcd5474e73d00fe687
  - Guidance ddd66ac8848f045f8d78c0b70ca30a5cad0b0be7182aacce5509054cc657e7e8
  - Procedure f0cfc4030fbea25e741e8f5fb59a8c32e58003351e3184b85eb1292c7e052a48
  - _STATUS ebc272daa5e7ddafb5dcc4e76b8ed0b676f7b0bd90c63ff8f4fc42d6bd30dbe1

Tasks:
  - Read complete agents/AGENT_TASK.md and all live skills/scope-of-work method files before acting. Do not delegate.
  - Read exactly the named P3 DEL-07-06 row, the named live four sources and _STATUS/control references, the extracted candidate under candidates/P4_PILOTS/APP-PKG07/DEL-07-06/, active SOW tools, Stage-1 inventory, and Stage-1 evidence/DEL-07 evidence.
  - Confirm `target_state/legacy_source` is byte-equal to the live four sources/_STATUS and `target_state/ScopeOfWork.md` is byte-equal to the extracted candidate; do not edit those seeded truth copies.
  - Under PILOT-VALIDATION-001, validate the current live/P3-bound legacy-only state as `LEGACY_FOUR_DOC` with no SOW, and validate `target_state` as target-only `SOW_V1` with no legacy production files at its root. Do not invoke isolated-dual validation.
  - Reproduce the remaining full pilot gate: exact hashes/current-base equality; claim map and every target resolution; parity and source-line preservation; deterministic checklist twice; HTML render twice with byte stability/script/external-resource safety; lifecycle/control containment; Stage-1 evidence identity; separate schema/content, preservation, and substrate verdicts.
  - Emit an exact five-path future replacement manifest: ADD ScopeOfWork.md at candidate hash and DELETE the four legacy production paths at their P3 hashes. This is evidence only; do not modify the live project.
  - Write detailed evidence and terminal RETURN.md/STATUS.json only in this child instance. Any discrepancy returns FAIL; never repair.
  - Do not insert a D-GOV-16 marker, invoke conversion, overlay the legacy and target formats, treat the D-GOV-15 provenance marker as migration authority, or modify the candidate.

ExpectedOutputs:
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/workspace/target_state/_run_records/TASK_RUN_*.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/workspace/target_state/evidence/**
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/RETURN.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/STATUS.json
  - evidence includes SOURCE_HASHES.tsv, validation/map/parity/checklist/render artifacts, REPLACEMENT_MANIFEST.tsv, and CHECKS.md

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/chirality-app-dev/** write
  - candidate edits or regeneration
  - Git/index/ref/branch/PR writes
  - lifecycle/control/receipt/release/H1/H2/retirement writes
  - delegation
