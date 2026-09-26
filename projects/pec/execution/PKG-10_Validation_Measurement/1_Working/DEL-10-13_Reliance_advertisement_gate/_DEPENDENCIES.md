# Dependencies: DEL-10-13 Reliance-advertisement gate

## Dependency Tracking Mode
- **Mode:** FULL_GRAPH
- **Register:** the declared sections of this file together with Dependencies.csv (schema v3.1) when present (docs/SPEC.md §5.3)
- **Notes:** `execution/_Coordination/_COORDINATION.md` (coordination representation FULL_GRAPH; RequiredMaturity threshold `INITIALIZED`, owner-ruled Phase 1.3). Register storage is deliverable-local by owner ruling (no central register). Blocker output is advisory visibility only — never work assignment.

---

## Declared Upstream (I need these before I can proceed)
- None declared at setup. The upstream edges in the Extracted Dependency Register below are extracted-stratum rows seeded under `D-PEC-101`; none is a human declaration.

## Declared Downstream (These need me)
- None declared at setup.

---

## Extracted Dependency Register
- **Status:** SEEDED 2026-09-26 under `D-PEC-101` from accepted decomposition revision 1.6 (SCA-006, A-29) and PRD v2.4, outside the `dependency-extract` lifecycle by packet ruling (the D-PEC-62 §3.2 and D-PEC-93 precedent). A later `dependency-extract` run refreshes this section.
- **Rows:** `Dependencies.csv` — 2 ANCHOR (`DEP-10-13-001` → PKG-10, `DEP-10-13-002` → SOW-100) and 12 EXECUTION (`DEP-10-13-003`..`-014`).

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-03-04 (Practitioner-harness parity diff) | DERIVED | TESTS |  | E-P88 |
| DEL-04-03 (Citation & freshness stamping) | DERIVED | TESTS |  | E-P89 |
| DEL-04-05 (Measurement-limitation honesty) | DERIVED | TESTS |  | E-P90 |
| DEL-10-02 (Kill test (standing release gate)) | DERIVED | TESTS |  | E-P91 |
| DEL-02-01 (`_STATUS.md` parser) | PROPOSAL | TESTS |  | E-P92 |
| DEL-02-02 (Decision register/packet parser) | PROPOSAL | TESTS |  | E-P93 |
| DEL-02-03 (Receipts ledger parser (per-loop grammars)) | PROPOSAL | TESTS |  | E-P94 |
| DEL-02-04 (Run-evidence JSON parser) | PROPOSAL | TESTS |  | E-P95 |
| DEL-02-05 (Dependency register parser) | PROPOSAL | TESTS |  | E-P96 |
| DEL-02-06 (Workplan/LOOP_INIT parser) | PROPOSAL | TESTS |  | E-P97 |
| DEL-02-08 (Work-graph parser) | PROPOSAL | TESTS |  | E-P98 |
| DEL-02-09 (MEMORY run-index parser) | PROPOSAL | TESTS |  | E-P99 |

No deliverable depends on this one at setup.

---

## Lifecycle Summary
- (placeholder)

---

## Run Notes
- Register-wide rules carried from the D-PEC-62 exhibit (non-gating):
  - **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
  - **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority
- The accepted register row says the gate is "re-proved at each such release" and consumes no internals "(as DEL-10-02)". Whether DEL-10-13 is a C-08 standing node, like DEL-10-02 and DEL-03-04, is an owner classification that `D-PEC-101` does not make.

## Run History
- 2026-09-26 — seeded under `D-PEC-101` (WORKING_ITEMS with `project-setup`; `preparation` skill scaffold; rows and this file written by the bound generator `gen_d101_k1.py`).
