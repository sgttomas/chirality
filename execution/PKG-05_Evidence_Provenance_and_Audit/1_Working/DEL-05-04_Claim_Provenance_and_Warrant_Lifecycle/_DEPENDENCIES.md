# Dependencies: DEL-05-04 Claim Provenance and Warrant Lifecycle

Deliverable-local dependency truth (K-DEP-1). This file and `Dependencies.csv`
are authoritative for this deliverable's dependencies; there is no central
dependency graph.

## Coordination (human-owned)

- **Mode:** DECLARED
- **Notes:** `execution/_harness/work_graph.yaml` is the accepted root work
  graph. It declares six package nodes, all `pending`, with **no** `depends_on`
  or `serialized_after` edges — the accepted decomposition §8 partitions six
  flat work-domain packages ("No nesting, no phases, no overlap, no gaps") and
  its §14 Downstream Execution Notes declare no inter-package ordering.

## Upstream (I need these before I can proceed) — human-owned declarations

- None declared. The accepted decomposition declares no inter-package or
  inter-deliverable ordering, and none is inferred here (K-INVENT-1).

## Downstream (These need me) — human-owned declarations

- None declared. See above.

## Extracted Dependency Register (populated by TASK+dependency-extract)

- **Status:** NOT_RUN_YET
- **Dependencies.csv:** TBD
- **Summary:** TBD

## Run Notes & History (populated by TASK+dependency-extract)

- 2026-07-25 — Container created by PROJECT_SETUP at step-9 materialization
  (D-GOV-25). No edges declared or extracted.

## Lifecycle Summary (populated by TASK+dependency-extract)

- (placeholder)

## Consumer Handoff Notes (optional)

- (placeholder)
