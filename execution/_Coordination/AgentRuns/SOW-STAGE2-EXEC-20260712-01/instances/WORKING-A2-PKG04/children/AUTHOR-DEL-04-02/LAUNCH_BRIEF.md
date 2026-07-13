# AUTHOR-DEL-04-02 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-04-02 and complete author evidence.
RequestedBy: WORKING-A2-PKG04
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A2-PKG04
ChildInstanceID: AUTHOR-DEL-04-02
PackageID: APP-PKG-04
ManifestPackageID: PKG-04
DeliverableID: DEL-04-02

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/AUTHOR-DEL-04-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/AUTHOR-DEL-04-02/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG04/DEL-04-02/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/AUTHOR-DEL-04-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-016, SOW-045, SOW-047, SOW-052
  PACKAGE_OBJECTIVE_REFS: OBJ-004, OBJ-005
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - synchronized main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa, evidence-only successor to exact row basis main@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  - accepted W-A2 preflight and exact DEL-04-02 row in snapshots/W_A2/preflight/A2_MANIFEST.tsv, including all hashes/refs/dependencies

Tasks:
  - Act strictly as Agent 2 TASK; load AGENT_TASK and the complete scope-of-work method pack; do not delegate or contact siblings.
  - Confirm the frozen row; seed the pre-created workspace with byte-equal legacy/control inputs; resolve exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, no live SOW.
  - Run converter first with PKG-04. Ground OUT-001/AC-001/VER-001 only in SOW-016, SOW-045, SOW-047, SOW-052; OBJ-004, OBJ-005; identity; and legacy source. Add no scope or semantic obligation.
  - Preserve markers; validate authorized MIGRATION_DUAL; map/parity; checklist twice; render twice; prove complete disposition, hash/target bindings, safety/stability and separate schema/content-authority/preservation/substrate verdicts.
  - Copy only exact ScopeOfWork.md to candidates/W_A2/APP-PKG04/DEL-04-02/ScopeOfWork.md. Write portable author evidence, terminal run record, RETURN.md, STATUS.json and self-excluding reproducible MANIFEST.tsv. Inventory exact preserved source literals; never normalize source/candidate/render bytes; stop before any evidence repair.
  - Fail on discrepancy. Never write project/Git/lifecycle surfaces.

ExpectedOutputs:
  - exact DEL-04-02 candidate; portable author evidence/manifest; terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; other candidates/package/sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
