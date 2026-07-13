# AUTHOR-DEL-01-03 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-01-03 and complete author evidence.
RequestedBy: WORKING-A1-PKG01
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG01
ChildInstanceID: AUTHOR-DEL-01-03
PackageID: APP-PKG-01
DeliverableID: DEL-01-03

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-03/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A1/APP-PKG01/DEL-01-03/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-071, SOW-074
  PACKAGE_OBJECTIVE_REFS: OBJ-009, OBJ-010
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@34b87ec77010035eeaa76f0fa65981ec57e78933, evidence-only successor to exact row basis main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  - accepted W-A1 A1-B0 preflight and exact DEL-01-03 manifest row
  - Datasheet ff00ec279937b42d6a86999dca8968c6488d019b67f63ec1ca1bbda0c9b813dd
  - Specification 87a13c0e49921facf88abc160a0367b65ffbfcf874107fdb26d7faaadb32d5ee
  - Guidance 7ce122014f08590d159aa070aa2ec5e211a3153e888f5bfc6445c3e8dcfba5fb
  - Procedure ccb9ae343c16cc927cc0a1827f3a909f0c73241502c0a1c6cf9c25b49b0adad7
  - _STATUS 2f0454fad0f3f9b6fd8719b4c7701c10bfbacdd192e02ec900364106d4a0ce01
  - _CONTEXT f03cc198eda6b5cc84325f9550baea53105d7da707ac577b23227f3d97a828e9
  - _REFERENCES 045cc70a94a4128486e60e6ced5499ac8659fee1cbcb1fc64ff629e9c0579ea9
  - _DEPENDENCIES 093b1b267a5054d7d56aed6103d7cc6b5f277daed911469e737090b20fbeef4b
  - Dependencies.csv bd44beecaf3b916f4e9ed9f97bf796e483a357c6ae6adf6f3f371e4b53f4b22b

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate or contact siblings.
  - Confirm seeded workspace equals exact live sources and status/control inputs and preserve them byte-for-byte.
  - Resolve exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, no live ScopeOfWork.md.
  - Invoke converter first with exact manifest package-id PKG-01, never APP-PKG-01. Seed OUT-001 only as the source-grounded product-identity and professional-boundary copy guidance/review record; AC-001 only as preservation/traceability to SOW-071, SOW-074, OBJ-009, and OBJ-010; VER-001 only as deterministic validation, mapping, parity, checklist/render checks, and human review. Add no scope, reliance claim, lifecycle meaning, or obligation.
  - Preserve markers; validate MIGRATION_DUAL; map/parity; checklist twice; render twice; prove line/marker/checklist/render and four verdict classes.
  - Copy only exact ScopeOfWork.md to candidates/W_A1/APP-PKG01/DEL-01-03/ScopeOfWork.md.
  - Write portable evidence and terminal run record/return/status. Fail on discrepancy; no project or Git/lifecycle writes.

ExpectedOutputs:
  - exact candidate candidates/W_A1/APP-PKG01/DEL-01-03/ScopeOfWork.md
  - author run record and evidence under this child instance
  - terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - other candidates, package instances, sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation
