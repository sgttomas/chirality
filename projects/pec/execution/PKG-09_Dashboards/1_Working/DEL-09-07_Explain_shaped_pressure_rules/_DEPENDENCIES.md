# _DEPENDENCIES — DEL-09-07

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-09-06 (Universal drill-down to cited source) | PROPOSAL | CONSUMES | AMBIGUOUS_BASIS | E-A11 |
| DEL-04-03 (Citation & freshness stamping) | DERIVED | CONSUMES |  | E-N04 |
| DEL-03-01 (Full-rebuild reconciler (one command)) | PROPOSAL | CONSUMES |  | E-N05 |
| DEL-03-03 (Drift classification) | DERIVED | CONSUMES |  | E-P67 |
| DEL-05-01 (Gate precondition evaluators (Explain-shaped)) | DERIVED | CONSUMES |  | E-P68 |
| DEL-06-06 (Advisory overlap detection) | DERIVED | CONSUMES | PHASE_TENSION | E-P69 |

## Downstream (informational; consumers of this deliverable)

- DEL-09-01 (Overview dashboard) — CONSUMES [E-A12]
- DEL-09-02 (Lifecycle census dashboard) — CONSUMES [E-A13]
- DEL-09-03 (Register views) — CONSUMES [E-A14]
- DEL-09-04 (Decision-slate view ("waiting on you")) — CONSUMES [E-A15]
- DEL-09-05 (Presence board) — CONSUMES [E-A16]

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
