# AUTHOR-DEL-01-02 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-01-02 and complete author evidence.
RequestedBy: WORKING-A1-PKG01
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG01
ChildInstanceID: AUTHOR-DEL-01-02
PackageID: APP-PKG-01
DeliverableID: DEL-01-02

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-02/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A1/APP-PKG01/DEL-01-02/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-037, SOW-045, SOW-054, SOW-057, SOW-074
  PACKAGE_OBJECTIVE_REFS: OBJ-002, OBJ-005, OBJ-009
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@34b87ec77010035eeaa76f0fa65981ec57e78933, evidence-only successor to exact row basis main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  - accepted W-A1 A1-B0 preflight and exact DEL-01-02 manifest row
  - Datasheet ad72196a3fa5282b0b37581913321f9950a1bc3004444d5a821ab8de1dd749ee
  - Specification c538ec54d671bd8fbc2189f34b53155a7fc47d80efa515b179d15f1e1a1ac107
  - Guidance 8ad3bb5959055a99810bb8cb6d02e354aa94e00ed207ea95259a1a3a59ec3b6d
  - Procedure 2182d71e2becd966b7f85a135fc0c8fa3927a9eaa3b335a615ab9ecd858a7ba3
  - _STATUS 213041b3886a728effd826e81822cc987efa8d84ee12fa32723f16484485add9
  - _CONTEXT d462de712c34240df0a153f92d39bf974483ac3fa3007e75fd85381e7cf0c9d6
  - _REFERENCES 9948487c5ff7859181289b51b62602d51ee147568962da61abde1096ec05ee10
  - _DEPENDENCIES 8d9f23443125d6043d34e46dfd0e7db77e4523bf7e7fbc3d5f0bbd120dda644f
  - Dependencies.csv 89a6d3babc70b87da98dcbe0f240f06171136f124f64c489cee818f6b774f294

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate or contact siblings.
  - Confirm seeded workspace equals exact live sources and status/control inputs and preserve them byte-for-byte.
  - Resolve exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, no live ScopeOfWork.md.
  - Invoke converter first with exact manifest package-id PKG-01, never APP-PKG-01. Seed OUT-001 only as the source-grounded reliance-boundary register, enforcement matrix, and test index; AC-001 only as preservation/traceability to the frozen SOW/OBJ refs; VER-001 only as deterministic validation, mapping, parity, checklist/render checks, and human review. Add no scope, reliance claim, lifecycle meaning, or obligation.
  - Preserve markers; validate MIGRATION_DUAL; map/parity; checklist twice; render twice; prove line/marker/checklist/render and four verdict classes.
  - Copy only exact ScopeOfWork.md to candidates/W_A1/APP-PKG01/DEL-01-02/ScopeOfWork.md.
  - Write portable evidence and terminal run record/return/status. Fail on discrepancy; no project or Git/lifecycle writes.

ExpectedOutputs:
  - exact candidate candidates/W_A1/APP-PKG01/DEL-01-02/ScopeOfWork.md
  - author run record and evidence under this child instance
  - terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - other candidates, package instances, sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation
