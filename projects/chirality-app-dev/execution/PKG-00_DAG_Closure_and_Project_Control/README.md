# PKG-00 DAG Closure and Project Control

## Purpose

`PKG-00` is a meta/control package for project-level dependency closure. It exists to coordinate the agentic reconciliation workflow that turns SCC closure rulings into an acyclic project DAG.

## Boundary

`PKG-00` is not a decomposed product implementation package and is not part of the strict deliverable dependency graph.

It may contain `DEL-00-*` control deliverables for SCC closure. Those control deliverables intentionally have no deliverable-local `Dependencies.csv` registers. DepClosure and dependency extraction should continue to read product deliverable registers under `PKG-01` through `PKG-10`.

## Owned Records

- DAG/SCC closure workflow notes.
- Project-level reconciliation control records.
- Pointers to immutable DepClosure snapshots.
- Human-ruling queues for SCC and bidirectional-pair resolution.
- SCC closure control deliverables:
  - `DEL-00-01` for SCC-002 (`DEL-10-02`, `DEL-10-03`).
  - `DEL-00-02` for SCC-001 runtime/SDK/session/tooling.

## Current Readiness

Both SCC closure control deliverables are `SEMANTIC_READY` through bounded `TASK` run records. The earlier direct ORCHESTRATOR-authored semantic-ready state was explicitly invalidated in each deliverable history before the TASK pipeline regenerated the document kit, semantic lens, lensing register, and P3 enrichment.

This does not modify dependency edge state and does not make the strict product graph acyclic.

## Non-Goals

- Do not use this package to invent dependency edges.
- Do not use this package to bypass deliverable-local evidence requirements.
- Do not report strict project-wide `BLOCKED/UNBLOCKED` until DepClosure reports a strict acyclic FULL_GRAPH.
