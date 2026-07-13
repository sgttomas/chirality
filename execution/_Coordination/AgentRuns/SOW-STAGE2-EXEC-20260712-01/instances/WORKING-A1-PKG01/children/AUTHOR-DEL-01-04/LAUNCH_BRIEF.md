# AUTHOR-DEL-01-04 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-01-04 and complete author evidence.
RequestedBy: WORKING-A1-PKG01
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG01
ChildInstanceID: AUTHOR-DEL-01-04
PackageID: APP-PKG-01
DeliverableID: DEL-01-04

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-04/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-04/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A1/APP-PKG01/DEL-01-04/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-04/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-065, SOW-076, SOW-077, SOW-078
  PACKAGE_OBJECTIVE_REFS: OBJ-009
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@34b87ec77010035eeaa76f0fa65981ec57e78933, evidence-only successor to exact row basis main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  - accepted W-A1 A1-B0 preflight and exact DEL-01-04 manifest row
  - Datasheet c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd
  - Specification 2c62f5727c02f036097d1d1ce1361cbbe0b10fe6594fa21d0ffbfacc87cedc66
  - Guidance 631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c
  - Procedure d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca
  - _STATUS 93b04e3b03d2f47ca0105e05a138ac5765d6c841305daef9020a579c6ec3699a
  - _CONTEXT eaa0ee8ccb5a52cfca6bdcff64d2ef236a6dce1a26231b020d2a16b4e5cf8323
  - _REFERENCES 8690002970f937ec20cde7cb5437f9d051ccdd81e8e49203260292465357c216
  - _DEPENDENCIES 33f481ccc3ba05772f5f39ab5be65081b5777fc575e4f07097d06417c98a80e4
  - Dependencies.csv 5a190cab5b55d89537d92d148038f0877226b0d5bca994e699c45b131fed6727

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate or contact siblings.
  - Confirm seeded workspace equals exact live sources and status/control inputs and preserve them byte-for-byte.
  - Resolve exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, no live ScopeOfWork.md.
  - Invoke converter first with exact manifest package-id PKG-01, never APP-PKG-01. Seed OUT-001 only as the source-grounded scope-boundary/retired-scope register and amendment-trigger record; AC-001 only as preservation/traceability to SOW-065, SOW-076, SOW-077, SOW-078, and OBJ-009; VER-001 only as deterministic validation, mapping, parity, checklist/render checks, and human review. Add no scope, reliance claim, lifecycle meaning, or obligation.
  - Preserve markers; validate MIGRATION_DUAL; map/parity; checklist twice; render twice; prove line/marker/checklist/render and four verdict classes.
  - Copy only exact ScopeOfWork.md to candidates/W_A1/APP-PKG01/DEL-01-04/ScopeOfWork.md.
  - Write portable evidence and terminal run record/return/status. Fail on discrepancy; no project or Git/lifecycle writes.

ExpectedOutputs:
  - exact candidate candidates/W_A1/APP-PKG01/DEL-01-04/ScopeOfWork.md
  - author run record and evidence under this child instance
  - terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - other candidates, package instances, sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation
