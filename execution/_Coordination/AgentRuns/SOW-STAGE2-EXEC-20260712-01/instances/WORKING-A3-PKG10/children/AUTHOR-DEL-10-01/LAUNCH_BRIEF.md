# AUTHOR-DEL-10-01 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-10-01 and complete author evidence.
RequestedBy: WORKING-A3-PKG10
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG10
ChildInstanceID: AUTHOR-DEL-10-01
PackageID: APP-PKG-10
ManifestPackageID: PKG-10
DeliverableID: DEL-10-01

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/AUTHOR-DEL-10-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/AUTHOR-DEL-10-01/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A3/APP-PKG10/DEL-10-01/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/AUTHOR-DEL-10-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-066, SOW-067
  PACKAGE_OBJECTIVE_REFS: OBJ-010
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1, evidence-only successor to exact row basis main@ff59428ff27d929bc1172e6c049a5e274d487fc0
  - accepted W-A3 preflight and exact DEL-10-01 row in snapshots/W_A3/preflight/A3_MANIFEST.tsv
  - source hashes e2ff9bf41bfb974d5c8bbc1f697065839f049f941213853a75d6df5b4c1fda35, f08fca5f98d8a1ab373148134d29a91b26405841d82f25bbc5e868d338f6e8a9, 350b3312a290fd83d9620fbd83ed2fa3550fad1472e3553e88a4767de4429799, 53b10c6fef07d1493fd20404de54caa3272052a7c99a749234ffe9f42e7bda59; status a891a8e388b47f09e40dcc72eccf33f380035cf5bbfa6b0bfda481c741960fbe

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and every scope-of-work method file; do not delegate or contact siblings.
  - Confirm the exact manifest row, then seed the pre-created workspace from the live path with byte-equal Datasheet.md, Specification.md, Guidance.md, Procedure.md, _STATUS.md, _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, and Dependencies.csv. Keep seeded inputs byte-identical.
  - Resolve live state as exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, with no live ScopeOfWork.md.
  - Invoke deterministic converter first using exact manifest package-id PKG-10. Ground OUT-001, AC-001, and VER-001 only in SOW-066, SOW-067; OBJ-010; deliverable identity; and exact legacy source. Add no domain-engine implementation, solver reliance, protected-path write, approval, lifecycle meaning, or semantic obligation beyond the accepted source.
  - Preserve every source marker; validate authorized MIGRATION_DUAL; emit map/parity; derive checklist twice; render twice; run fail-closed negative fixtures.
  - Prove complete line disposition, marker/hash/target bindings, checklist exactness, stable script-free render, and separate schema/content-authority/preservation/substrate verdicts.
  - Copy only exact ScopeOfWork.md to candidates/W_A3/APP-PKG10/DEL-10-01/ScopeOfWork.md.
  - Write only portable generated evidence and terminal TASK run record, RETURN.md, STATUS.json, and reproducible self-excluding MANIFEST.tsv. Preserve and inventory machine-specific strings embedded in accepted source/control or marker-bound candidate/render bytes as PRESERVED_SOURCE_LITERAL; never normalize source/candidate/render bytes. Generated metadata must be portable. Stop before any after-the-fact evidence repair.
  - Any discrepancy fails with rerun requirements. Never write project or Git/lifecycle surfaces.

ExpectedOutputs:
  - exact candidate, author evidence, preserved-literal inventory, reproducible MANIFEST.tsv, terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; other candidates/package/sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
