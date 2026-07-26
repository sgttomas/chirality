# _DEPENDENCIES — DEL-08-01

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream

**no upstream predecessors (root node)** — expected and valid (D-PEC-62 §3.2).

## Downstream (informational; consumers of this deliverable)

- DEL-09-06 (Universal drill-down to cited source) — CONSUMES [E-N06]
- DEL-10-12 (Poll-adoption measurement) — MEASURES [E-N08]
- DEL-08-04 (Orientation latency budget (p95 ≤ 100 ms)) — TESTS [E-P52]
- DEL-10-03 (No-ruling-write verification) — TESTS [E-P54]
- DEL-08-05 (SSE delta/presence subscription) — CONSUMES [E-P58]

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
