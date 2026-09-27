# Setup run record — `project-setup` INCREMENTAL for SCA-APP-012

Function 5 run record (method Phase 5.7). The run is WORKING_ITEMS (workflow:
project-setup), from the bundled `workflows/project-setup/`
(`resources/method.md` Function 5; `resources/contract.md`).

## Gates (owner confirmations)

- **Owner act.** Typed in chat on 2026-09-27 (verbatim;
  `CHAT_TRANSCRIPTION.md`):

  > I Confirm the SCA-APP-012 incremental plan under FULL_GRAPH; DEP-02-03-008: retire; TM-APP-051: option 1.

- **Phase 5.0 (baseline).** Not run. `_Coordination/SETUP_LOG.md` already holds
  its one `BASELINE` line (amendments accepted up to 2026-09-07, latest
  SCA-APP-010), and the method runs Phase 5.0 only when that line is absent.
- **Phase 5.1 (plan).** Confirmed. The plan is `INCREMENTAL_SETUP_PROPOSAL.md`
  §B:
  - accepted snapshot
    `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/`;
  - register `Amendment_Actions.csv`, resolved through the group-2
    `ACCEPTED_MANIFEST.csv`, SHA-256
    `a9ff78f2be8356b7727d7bb853bd758a55cb6a976b42dc2fc8dc1d1365e114ad`
    (verified);
  - 0 to scaffold, 0 retired, 8 modified (0 held at `CHECKING` or `ISSUED`),
    16 neighbours, FULL_GRAPH.
- **FULL_GRAPH.** The owner named the mode for this plan. `_COORDINATION.md`
  still records no mode and is not edited: this function reads it and does not
  write it, and the owner did not ask for a standing record.
- **Where the gate is recorded.** The contract's `SETUP_LOG.md` holds the
  `BASELINE` line and one line per incremental run; it has no plan-gate line.
  The Phase 5.1 confirmation is recorded here and in `CHAT_TRANSCRIPTION.md`,
  and the run's `INCREMENTAL` line is appended at Phase 5.7.

## Stages, briefs and returns

| Phase | Stage | Brief (effective settings) | Return |
|---|---|---|---|
| 5.2–5.3 | Scaffold and initialize added entities | — | Nothing to do: no ADD of a deliverable (the one ADD row is the DEC-027 decision-log row) |
| 5.4 | Record retirements | — | Nothing to do: no REMOVE |
| 5.5 | `scope-of-work` `MODE=VERIFY` for DEL-02-01, DEL-02-02, DEL-02-03, DEL-06-03, DEL-07-02, DEL-07-03, DEL-08-02, DEL-08-03 | `SOW_V1` at `IN_PROGRESS`; the group-2 write boundary (T-a) named each `ScopeOfWork.md`, so VERIFY only; `STATUS_POLICY: NO_STATUS_TOUCH` | PASS for all eight. Valid, 0 issues; checklists deterministic; contracts and `_STATUS.md` unchanged; nothing changes scope or lifecycle (`setup_verify/`) |
| 5.6 | `dependency-extract` for the 8 plus the 16 neighbours | `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; decomposition SHA-256 `6ac78118…a577`; one deliverable per pass, straight through; run directly by WORKING_ITEMS | 24 registers and indexes written. 310 rows re-seen, 2 retired (DEP-02-03-009 DX-01, DEP-02-03-008 DX-07), 2 re-evidenced (DEP-02-03-004 DX-02, DEP-02-03-007 DX-06), 1 restated (DEP-08-03-007 DX-03), 0 added. Function 5 checks pass (`DEPENDENCY_EXTRACT_RESULTS.md`, `dep_extract/`) |
| 5.6 | `audit-dep-closure` over the accepted inventory | SCOPE ALL rules with exemptions DEL-00-01, DEL-00-02 (CONTROL) and DEL-09-07 (RETIRED); `UPDATE_LATEST_POINTER=false` | 51 current units PASS, 102 edges, 0 SCC; census 54 nodes, 102 edges, 0 SCC, no new isolate. No SCC to route (`_Evaluation/DepClosure/CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234/`) |
| 5.6 | `project-dag` currency audit | — | Not applicable: no accepted project DAG (`_DAG/_LATEST.md` absent) |
| 5.7 | Scan and report (Phase 3.1/3.2) | FULL_GRAPH advisory from the recorded register | 53 IN_PROGRESS and 1 OPEN (retired DEL-09-07). 53 unblocked, 0 blocked, 0 held for a cycle (`setup_report/SCAN_REPORT.md`) |

## Paths written

- **Setup records.**
  - `execution/_Coordination/SETUP_LOG.md`: one `INCREMENTAL` line appended.
  - This run's `CHAT_TRANSCRIPTION.md`, `SETUP_RUN_RECORD.md`,
    `DEPENDENCY_EXTRACT_RESULTS.md`, `setup_verify/`, `dep_extract/` and
    `setup_report/`.
- **Registers.** `Dependencies.csv` and `_DEPENDENCIES.md` of the 24
  deliverables named above (18 `Dependencies.csv` byte-identical, since their
  rows already carried `LastSeen=2026-09-27`).
- **Closure evidence.**
  `execution/_Evaluation/DepClosure/CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234/`.
- **Skipped, with nothing to do:** scaffolding, retirement records, and
  `_STATUS.md` history lines.
- **Not written:**
  - any `ScopeOfWork.md`, `_CONTEXT.md` or `_STATUS.md`;
  - `_COORDINATION.md`, which is human-owned and only read;
  - the decomposition;
  - the accepted amendment snapshot;
  - any pointer.

## Report to human (Phase 5.7)

Incremental setup for SCA-APP-012:
- **Scaffolding and retirements:** 0 scaffolded; 0 retirements recorded.
- **Modified:** 8 routed to `scope-of-work` `MODE=VERIFY`, all PASS.
- **Held for the human:** 0 (none at `CHECKING` or `ISSUED`).
- **Dependency refresh:** FULL_GRAPH.
  - `dependency-extract` ran for 24 deliverables; DX-01 to DX-07 as expected
    (DX-04 does not apply).
  - `audit-dep-closure` result: PASS, 102 edges, 0 SCC.
- **`DAG pending`:** none, because there is no accepted project DAG.
- **Stale derivatives:** the `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` of the
  8 modified deliverables. Their owner is the semantic-lensing pipeline (Phase
  2.3–2.4). They are rerun only if the owner selects it; the owner did not.
- **Observation for the register owner:** DEL-09-04's 2026-09-23 clause
  APP-R078 names DEL-02-01; the relationship is already recorded as
  DEP-02-01-013, so no row is emitted (noted in the DEL-09-04 index).
- **Decisions pending:** none from this plan. The DepClosure and DecompCoverage
  observation pointers stay where they are (the manager's call).
- **Closure check:** `audit-scope-closure` dispatched after this line (see
  `RECEIPT.md`).

The accepted amendment snapshot stays immutable.

## Why COMPLETE stands

- **Every planned stage ran.** The plan the owner confirmed (Phase 5.1) had no
  scaffold and no retirement. It had eight VERIFY routes, dependency
  extraction and closure for 24 deliverables under FULL_GRAPH, and the scan and
  report. Each of these ran to its end.
- **No stage waits on an owner decision.** DX-07 was confirmed with the plan,
  and no other row needed a ruling.
- **TM-APP-051** is a Task Management handoff of the amendment, not a setup
  stage. The owner chose option 1 in the same act, and it is recorded in
  `_TaskManagement/ROW_MAINTENANCE_TM-APP-051_SCA-APP-012_DISPOSITION_2026-09-27.md`.
