# Decision log — graph re-derivation

## DG-001 — Objective and edge semantics

The objective is post-SCA-004 Root sequencing readiness. Only declared
dependencies can create strict edges. Package-to-deliverable relationships are
recorded separately as non-gating structural membership edges.

## DG-002 — No inferred dependencies

All 46 pre-existing `_DEPENDENCIES.md` containers say extraction is
`NOT_RUN_YET` and declare no upstream/downstream edge. All seven N1 containers
explicitly say no dependency is declared or inferred and defer extraction.
Accordingly, the strict dependency edge set is empty; objectives, shared scope
items, prose resemblance, and package co-membership were not converted into
ordering edges.

## DG-003 — Cycle resolution

Deterministic SCC analysis over the declared dependency layer yields 59
singletons and no cycle. No decompose, invert, merge, or cut move is required.
No human-gated cut/merge decision was made.

## DG-004 — Derivative boundary

This run writes only the steer-authorized SCA evidence folder, overriding the
dedicated audit agent's default `_Evaluation/DepClosure` output location.
The graph must be regenerated after accepted SOWs and dependency extraction.
