# _DEPENDENCIES — DEL-00-02

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-00-01 (v2 first ADRs (core isolation + carried postures)) | PROPOSAL | CONSUMES | LOW_CONFIDENCE | E-N18 |

## Downstream (informational; consumers of this deliverable)

- DEL-07-01 (Idempotent event ingest + durable message store) — CONSUMES [E-A01]
- DEL-07-03 (Hooks CLI bridge) — CONSUMES [E-A02]
- DEL-07-02 (Daemon SSE subscriber bridge) — CONSUMES [E-A03]
- DEL-07-04 (cmux socket adapter (optional)) — CONSUMES [E-A04]
- DEL-07-05 (Shared-runtime client seam (v2)) — CONSUMES [E-N01]

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
