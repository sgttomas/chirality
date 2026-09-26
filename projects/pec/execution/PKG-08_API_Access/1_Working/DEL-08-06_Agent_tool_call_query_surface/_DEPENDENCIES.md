# Dependencies: DEL-08-06 Agent tool-call query surface

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
- **Status:** SEEDED 2026-09-26 under `D-PEC-101` from accepted decomposition revision 1.6 (SCA-006, A-28) and PRD v2.4, outside the `dependency-extract` lifecycle by packet ruling (the D-PEC-62 §3.2 and D-PEC-93 precedent). A later `dependency-extract` run refreshes this section.
- **Rows:** `Dependencies.csv` — 2 ANCHOR (`DEP-08-06-001` → PKG-08, `DEP-08-06-002` → SOW-099) and 4 EXECUTION (`DEP-08-06-003`..`-006`).

| Predecessor | Stratum | Kind | Flag | EdgeID |
|---|---|---|---|---|
| DEL-08-01 (Unix-socket server + token-scoped access) | DERIVED | CONSUMES |  | E-P84 |
| DEL-08-02 (Versioned additive API schema) | DERIVED | CONSUMES |  | E-P85 |
| DEL-08-03 (Compact citation-bearing response format) | DERIVED | CONSUMES |  | E-P86 |
| DEL-04-01 (Loop orientation return) | PROPOSAL | CONSUMES |  | E-P87 |

No deliverable depends on this one at setup.

---

## Lifecycle Summary
- (placeholder)

---

## Run Notes
- Register-wide rules carried from the D-PEC-62 exhibit (non-gating):
  - **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling
  - **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority

## Run History
- 2026-09-26 — seeded under `D-PEC-101` (WORKING_ITEMS with `project-setup`; `preparation` skill scaffold; rows and this file written by the bound generator `gen_d101_k1.py`).
