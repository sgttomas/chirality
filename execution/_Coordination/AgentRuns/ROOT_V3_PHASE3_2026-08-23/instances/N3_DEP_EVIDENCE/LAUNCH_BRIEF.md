# Sealed brief — N3 dependency graph and closure evidence

You are a bounded Agent 2 specialist executing graph re-derivation and `AUDIT_DEP_CLOSURE` semantics. Role entry is instruction-asserted. Do not delegate.

## Basis and dependency

- Repository root: `/Users/ryan/.codex/worktrees/0b6e/chirality`
- Basis: Phase 3 branch after validated N1 and N2 commits.
- Do not begin until HELP_HUMAN confirms N2 terminal PASS.
- Read root `AGENTS.md`, `agents/AGENT_AUDIT_DEP_CLOSURE.md`, `docs/CYCLE_DRIVEN_RESOLUTION.md`, the Phase 3 steer, revision-1.3 live decomposition/register, R7, N1/N2 returns, and prior Phase-1 graph/audit evidence.

## Objective and write scope

Write only:

- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/DEP_GRAPH_POST_PHASE3/`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DEP_CLOSURE_POST_PHASE3/`
- this instance's `RETURN.md` and `STATUS.json`.

## Required result

- Re-derive the objective-relative graph from 53 live deliverable nodes plus six package nodes and the N2 grounded dependencies. Emit `WORK_GRAPH.json`, `DAG.md`, and an SCC report.
- Never silently linearize a cycle. A required cut/merge is human-gated: preserve the evidence, mark cycle edges non-gating, return `BLOCKED`, and stop that affected step.
- Run a fresh dependency-closure audit. Record 53 deliverables, closure violations, and whether the Phase-1 initialized-empty warning is cleared or explained.
- Cite accepted SCA-004/revision-1.3 snapshot, R7, and N1/N2 outputs. State rerun after estimates/schedule or any dependency change.
- Preserve all earlier evidence.
- Fresh-review for exact node set, citations, SCC handling, and write containment.

## Return contract

Report file hashes, node/edge/SCC counts, SCC dispositions, closure verdict/reasons, audit findings, rerun trigger, protected-path checks, and review findings. Terminal status is `COMPLETE` or `BLOCKED`.
