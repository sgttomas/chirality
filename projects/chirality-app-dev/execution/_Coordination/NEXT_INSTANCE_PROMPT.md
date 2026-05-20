# NEXT INSTANCE PROMPT - Chirality App vNext

Adopt ORCHESTRATOR when initializing or scanning the workspace.

## Startup Read List

1. `execution/_Coordination/_COORDINATION.md`
2. `execution/_Coordination/NEXT_INSTANCE_STATE.md`
3. `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
4. `docs/PLAN.md`
5. Relevant deliverable-local `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md`

## Operating Invariants

- v3.2 SOFTWARE_DECOMP is the active decomposition authority until a later human ruling replaces it.
- Packages are flat work domains, not phases.
- Deliverables are the bounded execution units.
- Coordination mode is FULL_GRAPH with `SEMANTIC_READY` as the dependency satisfaction threshold.
- Dependency blockers are advisory and must be computed only from accepted dependency registers.
- R0/R1 runtime deliverables precede R2+ capability expansion.
- Read tools and read MCP exposure precede write/edit/bash.
- Domain engine execution, remote MCP, plugins, shipped bypass, non-macOS packaging, and retired PKG-08 hardening scope require governed amendment before implementation.

## Control Loop

1. ORCHESTRATOR scans lifecycle state and dependency-register readiness.
2. TASK executes one deliverable at a time with the selected skill and sealed write scope.
3. For setup, run `four-documents` P1/P2, `semantic-matrix-build`, `lens-register`, then `four-documents` P3.
4. After P3 enrichment reaches `SEMANTIC_READY`, run `dependency-extract`.
5. Validate touched artifacts before computing graph state.
6. Hand coherent work to CHANGE only after human approval gates are satisfied.

## TASK Dispatch Defaults

- `DECOMP_VARIANT=SOFTWARE`
- `DECOMPOSITION_REF=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `ALLOW_OVERWRITE_STATES=OPEN,INITIALIZED,SEMANTIC_READY`
- one deliverable folder per TASK invocation

## Starter Prompt

Read `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and `execution/_Coordination/NEXT_INSTANCE_STATE.md`, adopt ORCHESTRATOR, scan the filesystem-grounded state, and propose the next gated action without inventing dependency blockers.
