# _DEPENDENCIES — DEL-02-07

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-01-06 (Loop registry (local config default)) | PROPOSAL | CONSUMES |  | E-N16 |

## Downstream (informational; consumers of this deliverable)

- ~~DEL-03-01 (Full-rebuild reconciler (one command)) — CONSUMES [E-P25]~~ — **RETIRED 2026-09-25 under SCA-005 (D-PEC-93)**: `_harness/adapter.yaml` is a parity-peer input, not the feed manifest (A-07, A-18); register row `DEP-03-01-014` kept with `Status=RETIRED`

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
