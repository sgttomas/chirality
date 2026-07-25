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
  revision **1.2** (`current_basis`, SCA-002 successor, accepted
  2026-07-25 under `D-PEC-64`; evidence
  `execution/_ScopeChange/SCA-002_2026-07-25_1042/`). Historical:
  revision 1.1 was the basis at this gate's ruling (SCA-001 evidence
  `execution/_ScopeChange/SCA-001_2026-07-24_2206/`); read
  `execution/_Decomposition/_LATEST.md` first, always.

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
6. **`D-PEC-64` RULED and SCA-002 closed 2026-07-25:** decomposition
   revision **1.2** accepted (`current_basis`) — deliverable→objective
   mapping completed for the O-A wave-minimum scope; all 32 Phase 2.2
   wave members now carry non-empty `SupportsObjectives`; residue 11 IN
   rows / 9 deliverables retained by design. Evidence:
   `execution/_ScopeChange/SCA-002_2026-07-25_1042/`, Receipt 109.
   Executed under owner-directed Agent 0 orchestration (managed
   SCOPE_CHANGE instance; control plane
   `AgentRuns/RUN_2026-07-25_sca002/`). Re-pins executed 2026-07-25
   (`6e558a2c0`). Next: the D-PEC-63 draft-v2 ruling.

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
