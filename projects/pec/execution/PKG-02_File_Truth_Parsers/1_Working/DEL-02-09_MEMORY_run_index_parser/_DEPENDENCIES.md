# _DEPENDENCIES — DEL-02-09

Seeded deterministically under `D-PEC-93` (2026-09-25) from accepted
decomposition revision 1.5 (SCA-005, A-20) and PRD v2.3; the D-PEC-62
DAG exhibit predates this deliverable. `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-01-01 (Record-tier schema & entity model) | PROPOSAL | CONSUMES |  | E-P80 |

## Downstream (informational; consumers of this deliverable)

- DEL-03-01 (Full-rebuild reconciler (one command)) — CONSUMES [E-P82]

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
