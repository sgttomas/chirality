# _DEPENDENCIES — DEL-06-04

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| ~~DEL-01-02 (Presence-tier schema & entity model)~~ | PROPOSAL | CONSUMES |  | ~~E-N09~~ |
| ~~DEL-06-01 (Session presence records)~~ | PROPOSAL | CONSUMES |  | ~~E-N10~~ |
| ~~DEL-07-02 (Daemon SSE subscriber bridge)~~ | DERIVED | CONSUMES |  | ~~E-P46~~ |
| ~~DEL-07-03 (Hooks CLI bridge)~~ | DERIVED | CONSUMES |  | ~~E-P47~~ |

**RETIRED 2026-09-25 under SCA-005 (D-PEC-93):** DEL-06-04 is retired (A-34; SOW-029 OUT).
Every row of `Dependencies.csv` is kept with `Status=RETIRED` — tree anchors
`DEP-06-04-001`/`002` and execution rows `DEP-06-04-003`..`006`; the struck edges above no longer gate or feed any deliverable.

## Downstream (informational; consumers of this deliverable)

- ~~DEL-09-05 (Presence board) — CONSUMES [E-N02]~~ — **RETIRED 2026-09-25 under SCA-005 (D-PEC-93)**: DEL-06-04 retired (A-34, A-38); register row `DEP-09-05-005` kept with `Status=RETIRED`

## Non-gating constraints and register-wide rules

- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
