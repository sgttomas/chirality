# _DEPENDENCIES — DEL-07-03

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-00-02 (Event-contract schema v1) | DECLARED | CONSUMES |  | E-A02 |
| DEL-07-01 (Idempotent event ingest + durable message store) | PROPOSAL | CONSUMES |  | E-P49 |

## Downstream (informational; consumers of this deliverable)

- DEL-06-01 (Session presence records) — CONSUMES [E-P45]
- DEL-06-04 (Live hierarchy edges) — CONSUMES [E-P47]
- DEL-10-12 (Poll-adoption measurement) — MEASURES [E-P77]

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
