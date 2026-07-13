# AUTHOR-DEL-01-01 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-01-01 and complete author evidence.
RequestedBy: WORKING-A1-PKG01
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG01
ChildInstanceID: AUTHOR-DEL-01-01
PackageID: APP-PKG-01
DeliverableID: DEL-01-01

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-01/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A1/APP-PKG01/DEL-01-01/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-074, SOW-075
  PACKAGE_OBJECTIVE_REFS: OBJ-009
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@34b87ec77010035eeaa76f0fa65981ec57e78933, evidence-only successor to exact row basis main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  - accepted W-A1 A1-B0 preflight and exact DEL-01-01 manifest row
  - Datasheet 0cf37c2b83e3d2295390a6f89d0e0b54e653499c28e4d88dd1a1dedfc34cf870
  - Specification 4d16fa3bc902adf148004a8fc7e092e7d51a3777571644c789809aad661a90fb
  - Guidance 8f9dc09fdbf475f0e1db5ac2936b71a62e514bd2c8fa0717e281f0bb7cd9c9b4
  - Procedure 4af013257eb301ed18528b5faf7326280648b0ae14cffe8940c52a4fd9217071
  - _STATUS 110367613b5307f4af98972c57b5065d712d8a3d8753f36522fa75e07d35c1ce
  - _CONTEXT 863d309662517a2eca0e9a52b065c6fd92818cd32e9be8f7778a7102ed369cdd
  - _REFERENCES 506299e1d0538fecf3df4095798ad0c99938f561c1d9461569d3950935ef8530
  - _DEPENDENCIES 499402cf984773b25042d77af139138ed7c0c98dff1c835e0dad9a1795817dfa
  - Dependencies.csv 978f9b2fe779feac2b8fecc0d53c62c80382c00a315d553cea40f2cf84e290ea

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate or contact siblings.
  - Confirm the manager-seeded workspace is byte-equal to the exact live four sources and _STATUS/control inputs. Keep all seeded inputs byte-identical.
  - Resolve live state as exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, with no live ScopeOfWork.md.
  - Invoke the deterministic converter first using exact manifest package-id PKG-01, never APP-PKG-01. Seed OUT-001 only as the source-grounded governance-alignment record and human-authority/project-truth/runtime-audit checklists; AC-001 only as preservation and traceability to SOW-074, SOW-075, and OBJ-009; VER-001 only as deterministic validation, mapping, parity, checklist/render checks, and human review against the accepted legacy basis. Add no scope, reliance claim, lifecycle meaning, or semantic obligation.
  - Preserve every source marker; validate MIGRATION_DUAL; emit map/parity; derive checklist twice; render twice under exact authority.
  - Prove complete line disposition, marker/hash/target bindings, checklist exactness, stable script-free render, and separate schema/content-authority/preservation/substrate verdicts.
  - Copy only exact ScopeOfWork.md to candidates/W_A1/APP-PKG01/DEL-01-01/ScopeOfWork.md.
  - Write portable evidence and terminal TASK run record, RETURN.md, and STATUS.json. Any discrepancy fails with rerun requirements. Never write project or Git/lifecycle surfaces.

ExpectedOutputs:
  - exact candidate candidates/W_A1/APP-PKG01/DEL-01-01/ScopeOfWork.md
  - author run record and evidence under this child instance
  - terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - other candidates, package instances, sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation
