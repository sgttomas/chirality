# SOFTWARE Decomposition Coverage Report

- Run: `SCA_APP_011_POST_ACCEPTANCE`
- Timestamp: `2026-09-27T05:03:19+00:00`
- Scope: `ALL`

Result: **WARNINGS**; blockers: **0**.

## Basis and boundary

Full structural audit of the App SOFTWARE decomposition after SCA-APP-011 was accepted and applied (active snapshot `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`). Decomposition SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876`; companion register `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944`; `_LATEST.md` `904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637`; basis commit `78e74f590d6010a52565d250288290b3305a2942`. It checks structure and records; it is not product verification and asserts no owner acceptance. Incremental setup and dependency re-extraction for SCA-APP-011 have not run.

## Core checks

| Check | Result | Evidence |
|---|---|---|
| 1 — Forward coverage: packages | **PASS** | 10 declared; 10 with folders |
| 2 — Forward coverage: deliverables | **PASS** | 52 declared; 52 with folders |
| 3 — Reverse coverage: folders | **WARNING** | undeclared package folders ['PKG-00']; undeclared deliverable folders ['DEL-00-01', 'DEL-00-02'] (control-only surfaces) |
| 4 — ID consistency | **PASS** | 0 findings |
| 5 — Context fidelity | **WARNING** | {'MATCH': 51, 'PARTIAL': 1} across 52 declared deliverables; retired ['DEL-09-07'] |
| 6 — Artifact presence | **WARNING** | path/filename screen 18/194 anticipated artifact descriptions over active declared units; 50 IN_PROGRESS deliverables with incomplete matches. Structural screen, not product acceptance |
| 7 — Objective mapping | **PASS** | 10 ledger objectives; 0 without active support; Objectives/ledger mismatches [] |
| 8 — Ledger integrity | **PASS** | 84 rows {'IN': 78, 'OUT': 5, 'TBD': 1}; 0 dangling references; 0 reverse-view mismatches |
| 9 — Derivative package parity | **SKIPPED** | Not variant-owned for SOFTWARE (method Step 9); other derivative observations in the issue log |
| 9b — Package-shape conformance | **PASS** | companion register labeled authoritative in the main document |
| 10 — Active snapshot and handoff state | **PASS** | active snapshot ['SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement'] |
| 11 — Lifecycle distribution | **PASS** | {'IN_PROGRESS': 53, 'OPEN': 1} |

## Scope of Work validation

`validate_scope_of_work.py` on every physical deliverable folder: **54/54** pass.

## Comparison with the prior full audit

Prior: `projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_RECORD_RECON_2026-09-22_2026-09-22_1513/` (WARNINGS; issues {'WARNING': 55, 'INFO': 1}). Now: WARNINGS; issues {'WARNING': 57}. Topology prior {'packages': 10, 'deliverables': 52, 'objectives': 10, 'scope_items': 84, 'ledger_rows': 84}, now {'packages': 10, 'deliverables': 52, 'objectives': 10, 'ledger_rows': 84}; ledger prior {'IN': 78, 'OUT': 5, 'TBD': 1}, now {'IN': 78, 'OUT': 5, 'TBD': 1}. The artifact screen here is this run's path/filename heuristic (Step 6); its counts are not directly comparable with the prior run's filename-token screen.

## Closure readiness

**FAIL**: the active SCA-APP-011 snapshot remains `OPEN_PENDING_DERIVATIVE_CLOSURE` (incremental setup, dependency re-extraction and `audit-scope-closure` pending).
