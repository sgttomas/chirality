# _DEPENDENCIES — DEL-07-01

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-00-02 (Event-contract schema v1) | DECLARED | CONSUMES |  | E-A01 |
| DEL-01-04 (Self-observability logging) | PROPOSAL | CONSUMES |  | E-N15 |
| DEL-01-03 (Store bootstrap & content-minimal guard) | PROPOSAL | CONSUMES |  | E-P16 |

## Downstream (informational; consumers of this deliverable)

- DEL-07-02 (Daemon SSE subscriber bridge) — CONSUMES [E-P48]
- DEL-07-03 (Hooks CLI bridge) — CONSUMES [E-P49]
- DEL-07-04 (cmux socket adapter (optional)) — CONSUMES [E-P50]
- DEL-10-08 (Stream-loss recovery demonstration) — TESTS [E-P78]

## Non-gating constraints and register-wide rules

- **C-01 (CO_LANDING)** — DEL-07-01 may not be accepted/live without DEL-03-05; simultaneity permitted
- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
