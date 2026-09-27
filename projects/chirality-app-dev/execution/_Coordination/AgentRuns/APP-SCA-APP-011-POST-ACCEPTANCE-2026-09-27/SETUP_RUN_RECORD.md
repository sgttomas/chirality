# Setup run record — `project-setup` INCREMENTAL for SCA-APP-011

Function 5 run record (method Phase 5.7). The run is WORKING_ITEMS (workflow:
project-setup), from the bundled `workflows/project-setup/`
(`resources/method.md` Function 5; `resources/contract.md`).

## Gates (owner confirmations)

- **Owner act.** Typed in chat on 2026-09-27 (verbatim;
  `CHAT_TRANSCRIPTION.md`):

  > Confirm baseline SCA-APP-010 (accepted up to 2026-09-07) and the SCA-APP-011 incremental plan under FULL_GRAPH; HGD-2: retire DEP-02-01-008; APP-R058: option 1.

- **Phase 5.0 (baseline).** Confirmed. `_Coordination/SETUP_LOG.md` was
  created with its one `BASELINE` line: amendments accepted up to 2026-09-07,
  latest SCA-APP-010 with its DEL-02-05 carrier addendum.
- **Phase 5.1 (plan).** Confirmed. The plan is `INCREMENTAL_SETUP_PROPOSAL.md`
  §B:
  - accepted snapshot
    `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`;
  - register `Amendment_Actions.csv`, resolved through the group-2
    `ACCEPTED_MANIFEST.csv`, SHA-256
    `416097312beffa47143b2993bfe17721e5c312630789a1101e6cbda688edbc22`
    (verified);
  - 0 to scaffold, 0 retired, 9 modified, 16 neighbours, FULL_GRAPH.

## Stages, briefs and returns

| Phase | Stage | Brief (effective settings) | Return |
|---|---|---|---|
| 5.2–5.3 | Scaffold and initialize added entities | — | Nothing to do: no ADD |
| 5.4 | Record retirements | — | Nothing to do: no REMOVE |
| 5.5 | `scope-of-work` `MODE=VERIFY` for DEL-02-02, DEL-02-03, DEL-03-03, DEL-07-01, DEL-07-02, DEL-07-04, DEL-07-05, DEL-08-03, DEL-09-03 | `SOW_V1` at `IN_PROGRESS`; the group-2 write boundary (W-a) named each `ScopeOfWork.md`, so VERIFY only; `STATUS_POLICY: NO_STATUS_TOUCH` | PASS for all nine. Valid, 0 issues; checklists deterministic; contracts and `_STATUS.md` unchanged; nothing changes scope or lifecycle (`setup_verify/`) |
| 5.6 | `dependency-extract` for the 9 plus the 16 neighbours | `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; decomposition SHA-256 `cf6e56eb…1876`; one deliverable per pass; run directly by WORKING_ITEMS | 25 registers and indexes written. 311 rows re-seen, 7 retired, 6 restated, 1 kept with a note, 1 added, 12 held (ESR-1). HGD-2 closed. Function 5 checks pass (`DEPENDENCY_EXTRACT_RESULTS.md`, `dep_extract/`) |
| 5.6 | `audit-dep-closure` over the accepted inventory | SCOPE ALL rules with exemptions DEL-00-01, DEL-00-02 (CONTROL) and DEL-09-07 (RETIRED); `UPDATE_LATEST_POINTER=false` | 51 current units PASS, 107 edges, 0 SCC. No SCC to route (`_Evaluation/DepClosure/CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656/`) |
| 5.6 | `project-dag` currency audit | — | Not applicable: no accepted project DAG (`_DAG/_LATEST.md` absent) |
| 5.7 | Scan and report (Phase 3.1/3.2) | FULL_GRAPH advisory from the recorded register | 53 IN_PROGRESS and 1 OPEN (retired DEL-09-07). 53 unblocked, 0 blocked, 0 held for a cycle (`setup_report/SCAN_REPORT.md`) |

## Paths written

- **Setup records.**
  - `execution/_Coordination/SETUP_LOG.md`, created: the `BASELINE` line and
    the `INCREMENTAL` line.
  - This run's `CHAT_TRANSCRIPTION.md`, `SETUP_RUN_RECORD.md`,
    `DEPENDENCY_EXTRACT_RESULTS.md`, `setup_verify/`, `dep_extract/` and
    `setup_report/`.
- **Registers.** `Dependencies.csv` and `_DEPENDENCIES.md` of the 25
  deliverables named above.
- **Closure evidence.**
  `execution/_Evaluation/DepClosure/CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656/`.
- **Skipped, with nothing to do:** scaffolding, retirement records, and
  `_STATUS.md` history lines.
- **Not written:**
  - any `ScopeOfWork.md`, `_CONTEXT.md` or `_STATUS.md`;
  - `_COORDINATION.md`, which is human-owned and only read;
  - the decomposition;
  - the accepted amendment snapshot;
  - any pointer.

## Report to human (Phase 5.7)

Incremental setup for SCA-APP-011:
- **Scaffolding and retirements:** 0 scaffolded; 0 retirements recorded.
- **Modified:** 9 routed to `scope-of-work` `MODE=VERIFY`, all PASS.
- **Held for the human:** 0 (none at `CHECKING` or `ISSUED`).
- **Dependency refresh:** FULL_GRAPH.
  - `dependency-extract` ran for 25 deliverables.
  - `audit-dep-closure` result: PASS, 107 edges, 0 SCC.
- **`DAG pending`:** none, because there is no accepted project DAG.
- **Stale derivatives:** the `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` of the
  9 modified deliverables. Their owner is the semantic-lensing pipeline (Phase
  2.3–2.4). They are rerun only if the owner selects it.
- **Decisions pending:**
  - ESR-1: 12 held dependency rows whose evidence source was retired on
    2026-09-23;
  - HGD-1;
  - HGD-3, whose premise has changed;
  - the manager's call on the DepClosure and DecompCoverage observation
    pointers.
- **Closure check:** `audit-scope-closure` dispatched after this line (see
  `RECEIPT.md`).

The accepted amendment snapshot stays immutable.
