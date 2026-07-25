# Coordination Record

**Representation:** Full dependency graph (DAG)
**Dependency tracking mode:** FULL_GRAPH
**External schedule / coordination artifact:** N/A
**Default maturity threshold (if computing blockers):** `INITIALIZED` — owner-ruled 2026-07-25 (Phase 1.3 gate)

## Provenance

- Representation and mode are **owner-selected**, not agent-chosen: `D-PEC-61`
  ruled behavior 2 ("`FULL_GRAPH` is the owner-selected coordination
  representation for PEC Project Setup") and the SCA-001 closure released
  PROJECT_SETUP with `FULL_GRAPH` already selected
  (`execution/_Decomposition/_LATEST.md`, `execution/_ScopeChange/_LATEST.md`).
- Accepted upstream basis: `execution/_Decomposition/SOFTWARE_DECOMP.md`
  revision 1.1 (`current_basis`), immutable amendment evidence at
  `execution/_ScopeChange/SCA-001_2026-07-24_2206/`.

## Phase 1.3 owner rulings (2026-07-25 gate)

1. Maturity threshold: **`INITIALIZED`**.
2. Register storage: **deliverable-local `Dependencies.csv` (v3.1) +
   `_DEPENDENCIES.md`**, seeded at scaffolding; full accounting
   reconstructed on demand (`tools/coordination/analyze_dep_closure.py`);
   **no standing central register** — owner declined the central-aggregate
   pattern as "another surface for authority."
3. DAG candidate v0.2 **accepted, all strata as presented** (120 edges,
   10 constraints, 5 STANDING nodes) — exhibit in
   `PLAN_2026-07-25_project_setup_dag_gate.md`.
4. Phase-precedence and PHASE_TENSION items remain recorded flags/erratum
   candidates (PLAN §7); they do not alter threshold-based blocker
   arithmetic.
5. **`D-PEC-62` RULED and executed 2026-07-25:** scaffolding + local-register
   seeding authorized and landed — 11 packages / 64 deliverables (`OPEN`),
   64 deliverable-local `Dependencies.csv` (v3.1) + `_DEPENDENCIES.md`
   seeded from the frozen gate exhibit (evidence:
   `SEED_D-PEC-62/RUN_LOG.md`, Receipt 108). Blocker computation is active
   in advisory-reporting form from deliverable-local registers only.

## Notes (human-owned)

- Scaffolding and local-register seeding were authorized by `D-PEC-62`
  (RULED 2026-07-25) and executed the same day; further build tranches
  (the P1 slice) still require their own owner-ruled `D-PEC` packets per
  `docs/STATUS.md`.
- The owner-accepted dependency-DAG exhibit is embedded in
  `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` and
  is now **frozen gate provenance**: the deliverable-local
  `Dependencies.csv` registers are the sole live dependency basis. Both
  are derivative packages citing the accepted revision 1.1 snapshot and
  are never a substitute for decomposition truth.
