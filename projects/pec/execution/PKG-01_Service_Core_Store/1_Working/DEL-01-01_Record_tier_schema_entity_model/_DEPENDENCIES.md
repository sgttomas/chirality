# _DEPENDENCIES — DEL-01-01

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-00-01 (v2 first ADRs (core isolation + carried postures)) | PROPOSAL | CONSUMES |  | E-P01 |

## Downstream (informational; consumers of this deliverable)

- DEL-02-01 (`_STATUS.md` parser) — CONSUMES [E-P03]
- DEL-02-02 (Decision register/packet parser) — CONSUMES [E-P04]
- DEL-02-03 (Receipts ledger parser (per-loop grammars)) — CONSUMES [E-P05]
- DEL-02-04 (Run-evidence JSON parser) — CONSUMES [E-P06]
- DEL-02-05 (Dependency register parser) — CONSUMES [E-P07]
- DEL-02-06 (Workplan/LOOP_INIT parser) — CONSUMES [E-P08]
- DEL-03-01 (Full-rebuild reconciler (one command)) — CONSUMES [E-P10]
- DEL-04-01 (Loop orientation return) — CONSUMES [E-P11]
- DEL-05-01 (Gate precondition evaluators (Explain-shaped)) — CONSUMES [E-P12]
- DEL-05-02 (Cross-loop decision slate) — CONSUMES [E-P13]
- DEL-07-05 (Shared-runtime client seam (v2)) — CONSUMES [E-P14]

## Non-gating constraints and register-wide rules

- **C-03 (PACKAGE_LEVEL)** — Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively
- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
