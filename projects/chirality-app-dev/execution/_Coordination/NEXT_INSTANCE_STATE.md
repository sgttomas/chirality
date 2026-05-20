# NEXT INSTANCE STATE - Chirality App vNext

**Last Updated:** 2026-05-20
**Updated By:** ORCHESTRATOR

## Current Pointers

| Artifact | Path |
|---|---|
| Coordination policy | `execution/_Coordination/_COORDINATION.md` |
| Stable startup prompt | `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` |
| Decomposition authority | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Source corpus | `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md` |

## Current Program State

| Metric | Value |
|---|---:|
| Packages scaffolded | 10 |
| Deliverables scaffolded | 51 |
| OPEN | 51 |
| INITIALIZED | 0 |
| SEMANTIC_READY | 0 |
| IN_PROGRESS | 0 |
| CHECKING | 0 |
| ISSUED | 0 |

## Data-Quality Notes

REF-006 docs/PRD.md=HASH_MISMATCH

## Package Folders

| PackageID | Name | Path |
|---|---|---|
| PKG-01 | Product Governance and Reliance Boundaries | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries` |
| PKG-02 | Desktop Shell, Navigation, and Operator State | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State` |
| PKG-03 | Runtime Engine Contract and Turn Lifecycle | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle` |
| PKG-04 | SDK Adapter, Prompt, Provider, and Settings | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings` |
| PKG-05 | Session Audit, Replay, and Tool Result Records | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records` |
| PKG-06 | Permissioned Tools, MCP, and Hooks | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks` |
| PKG-07 | Filesystem Execution, Lifecycle, and Dependencies | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies` |
| PKG-08 | Agent Suite, Pipeline Dispatch, and Subagent Governance | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance` |
| PKG-09 | Validation, Packaging, Security, and Release | `execution/PKG-09_Validation_Packaging_Security_and_Release` |
| PKG-10 | Domain Engine Future Boundary | `execution/PKG-10_Domain_Engine_Future_Boundary` |

## Active Human Rulings

- Decomposition authority: v3.2 SOFTWARE_DECOMP.
- Coordination representation: FULL_GRAPH.
- Dependency satisfaction threshold: SEMANTIC_READY.
- Dependency extraction is post-enrichment, not pre-scaffold.

## Immediate Next Actions

1. Run TASK + `four-documents` with `RUN_PASSES=P1_P2` for selected deliverables.
2. Validate generated four-document kits before semantic matrix generation.
3. Run TASK + `semantic-matrix-build`, then `lens-register`, then `four-documents` P3.
4. Run TASK + `dependency-extract` only after enrichment is complete.

## Handoff Payload

- Stable invariant instructions: `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- Mutable state and queue: this file
- Deliverable-local continuity: `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- Dependency state: pending post-enrichment extraction

## Update Protocol

WORKING_ITEMS or TASK handoff should update this file when lifecycle distribution, active blockers, or immediate next actions change. ORCHESTRATOR should update it only when explicitly performing a scan or setup-state refresh.
