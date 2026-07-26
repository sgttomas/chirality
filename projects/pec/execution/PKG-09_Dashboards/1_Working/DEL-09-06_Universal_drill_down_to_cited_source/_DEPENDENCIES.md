# _DEPENDENCIES — DEL-09-06

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-08-01 (Unix-socket server + token-scoped access) | PROPOSAL | CONSUMES |  | E-N06 |
| DEL-08-03 (Compact citation-bearing response format) | PROPOSAL | CONSUMES |  | E-N07 |
| DEL-04-03 (Citation & freshness stamping) | PROPOSAL | CONSUMES |  | E-P70 |

## Downstream (informational; consumers of this deliverable)

- DEL-09-01 (Overview dashboard) — CONSUMES [E-A06]
- DEL-09-02 (Lifecycle census dashboard) — CONSUMES [E-A07]
- DEL-09-03 (Register views) — CONSUMES [E-A08]
- DEL-09-04 (Decision-slate view ("waiting on you")) — CONSUMES [E-A09]
- DEL-09-05 (Presence board) — CONSUMES [E-A10]
- DEL-09-07 (Explain-shaped pressure rules) — CONSUMES [E-A11]

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
