# _DEPENDENCIES — DEL-04-03

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-04-01 (Loop orientation return) | PROPOSAL | CONSUMES |  | E-P34 |

## Downstream (informational; consumers of this deliverable)

- DEL-10-04 (Orientation defect-rate spot-check) — MEASURES [E-A21]
- DEL-09-07 (Explain-shaped pressure rules) — CONSUMES [E-N04]
- DEL-04-05 (Measurement-limitation honesty) — CONSUMES [E-N17]
- DEL-08-03 (Compact citation-bearing response format) — CONSUMES [E-P53]
- DEL-09-06 (Universal drill-down to cited source) — CONSUMES [E-P70]

## Non-gating constraints and register-wide rules

- **C-02 (CO_OBLIGATION)** — One PEC-K-05/C4 enforcement obligation split across two write scopes; direction not declared
- **C-03 (PACKAGE_LEVEL)** — Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively
- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
