# _DEPENDENCIES — DEL-10-03

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-08-01 (Unix-socket server + token-scoped access) | PROPOSAL | TESTS |  | E-P54 |
| DEL-08-02 (Versioned additive API schema) | PROPOSAL | TESTS |  | E-P55 |

## Standing obligation (constraint C-08)

This deliverable is a STANDING node: it gates releases, not successors,
and is excluded from one-shot COMPLETE/UNBLOCKED arithmetic (owner-confirmed at D-PEC-62 ruling).

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-08 (STANDING_NODES)** — Standing obligations: excluded from one-shot COMPLETE/UNBLOCKED arithmetic; they gate releases not successors
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
