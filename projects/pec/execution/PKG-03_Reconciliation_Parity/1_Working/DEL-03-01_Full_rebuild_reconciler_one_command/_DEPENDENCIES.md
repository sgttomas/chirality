# _DEPENDENCIES — DEL-03-01

Seeded deterministically under `D-PEC-62` (2026-07-25) from the
owner-accepted DAG exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1). `Dependencies.csv` (v3.1)
is the structured register; this file is the human-readable view.
Register storage is deliverable-local by owner ruling (no central register).

## Upstream (this deliverable depends on)

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-01-04 (Self-observability logging) | PROPOSAL | CONSUMES |  | E-N14 |
| DEL-01-01 (Record-tier schema & entity model) | PROPOSAL | CONSUMES |  | E-P10 |
| DEL-01-03 (Store bootstrap & content-minimal guard) | PROPOSAL | CONSUMES |  | E-P15 |
| DEL-01-06 (Loop registry (local config default)) | PROPOSAL | CONSUMES |  | E-P18 |
| DEL-02-01 (`_STATUS.md` parser) | PROPOSAL | CONSUMES |  | E-P19 |
| DEL-02-02 (Decision register/packet parser) | PROPOSAL | CONSUMES |  | E-P20 |
| DEL-02-03 (Receipts ledger parser (per-loop grammars)) | PROPOSAL | CONSUMES |  | E-P21 |
| DEL-02-04 (Run-evidence JSON parser) | PROPOSAL | CONSUMES |  | E-P22 |
| DEL-02-05 (Dependency register parser) | PROPOSAL | CONSUMES |  | E-P23 |
| DEL-02-06 (Workplan/LOOP_INIT parser) | PROPOSAL | CONSUMES |  | E-P24 |
| DEL-02-07 (`adapter.yaml` feed-manifest consumer) | PROPOSAL | CONSUMES |  | E-P25 |

## Downstream (informational; consumers of this deliverable)

- DEL-09-07 (Explain-shaped pressure rules) — CONSUMES [E-N05]
- DEL-03-02 (Incremental reconcile on Git delta) — CONSUMES [E-P26]
- DEL-03-03 (Drift classification) — CONSUMES [E-P27]
- DEL-03-04 (Practitioner-harness parity diff) — CONSUMES [E-P28]
- DEL-03-05 (Stream-loss recovery guarantee) — CONSUMES [E-P29]
- DEL-03-06 (Rebuild performance bounds) — TESTS [E-P30]
- DEL-04-01 (Loop orientation return) — CONSUMES [E-P32]
- DEL-05-01 (Gate precondition evaluators (Explain-shaped)) — CONSUMES [E-P37]
- DEL-05-02 (Cross-loop decision slate) — CONSUMES [E-P38]
- DEL-09-02 (Lifecycle census dashboard) — CONSUMES [E-P61]
- DEL-09-03 (Register views) — CONSUMES [E-P63]
- DEL-10-02 (Kill test (standing release gate)) — TESTS [E-P72]
- DEL-10-10 (Directed bootstrap self-ingest validation) — CONSUMES [E-P74]

## Non-gating constraints and register-wide rules

- **C-03 (PACKAGE_LEVEL)** — Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively
- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Blocker semantics

Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).
Blocker output is advisory visibility only — never work assignment.
