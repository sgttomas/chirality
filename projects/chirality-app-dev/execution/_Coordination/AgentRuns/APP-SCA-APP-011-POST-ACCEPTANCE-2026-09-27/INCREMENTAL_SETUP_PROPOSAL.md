# SCA-APP-011 — `project-setup` INCREMENTAL: baseline and incremental plan (PROPOSAL, awaiting the owner)

**Status: PROPOSAL. Nothing in this proposal is written.**

`project-setup` Function 5 (bundled `workflows/project-setup/`,
`resources/method.md` Phases 5.0–5.1) needs two owner confirmations before any
setup write:
- the adoption baseline, once for this project;
- the incremental plan.

`_Coordination/SETUP_LOG.md` does not exist yet. `_COORDINATION.md` is not
edited.

## A. Phase 5.0 — adopt incremental setup (baseline)

The App has no `SETUP_LOG.md`, so it has not adopted incremental setup. The
accepted amendments under `execution/_ScopeChange/`:

| Amendment | Accepted | Hands setup to `project-setup` INCREMENTAL? |
|---|---|---|
| SCA-APP-001 (v2; the 1755 v1 folder was never accepted) and SCA-APP-002 … SCA-APP-007 | 2026-06-13 … 2026-08-01 | No; accepted before incremental setup existed |
| SCA-APP-008 | Not accepted (`AWAITING_OWNER_ACCEPTANCE`) | Not an input: a candidate is never set up |
| SCA-APP-009 | 2026-09-04 (pointer moved in `87f2d2a75`) | No |
| SCA-APP-010 | 2026-09-04 (pointer G5-POINTER, `91402dcda`) | No |
| SCA-APP-010 DEL-02-05 carrier addendum | 2026-09-07 (`_ScopeChange/ACCEPTANCE_SCA_APP010_DEL05_PROPAGATION_2026-09-07/OWNER_ACCEPTANCE.md`, "Accept both exact poststates") | No |
| SCA-APP-011 | 2026-09-27 (`checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`) | Yes (`Handoff_State.md`, next owning workflows 1) |

**Proposed baseline:** SCA-APP-010, accepted up to 2026-09-07. SCA-APP-010
itself was accepted on 2026-09-04, and its DEL-02-05 carrier addendum on
2026-09-07.
- It covers SCA-APP-010, its addendum and every accepted amendment before
  them. None of them is reprocessed.
- SCA-APP-011 is never covered, because it hands setup to INCREMENTAL, so it
  stays in the queue.

**Gate question (Phase 5.0):**

> Adopt incremental setup with baseline SCA-APP-010 (accepted up to 2026-09-07, including its DEL-02-05 carrier addendum):
> 10 earlier accepted amendments (SCA-APP-001 v2, SCA-APP-002 to 007, 009, 010 and the
> DEL-02-05 addendum) are treated as already set up and not reprocessed; 1
> amendment that hands setup to INCREMENTAL (SCA-APP-011) stays in the queue.
> Confirm?

**On confirmation:** create `_Coordination/SETUP_LOG.md` from the
`project-setup` contract template and append its one `BASELINE` line in the
contract form: amendments accepted up to 2026-09-07 (latest SCA-APP-010,
with its DEL-02-05 carrier addendum) are already set up and are not
reprocessed; confirmed by the owner.

## B. Phase 5.1 — the incremental plan for SCA-APP-011

**Inputs**
- Accepted snapshot:
  `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`,
  named by `_ScopeChange/_LATEST.md`.
- Register `Amendment_Actions.csv`, resolved through
  `checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/ACCEPTED_MANIFEST.csv`.
  SHA-256 `416097312beffa47143b2993bfe17721e5c312630789a1101e6cbda688edbc22`,
  verified. It has 29 rows: 28 MODIFY and 1 ADD. The ADD is the DEC-026
  decision-log row, not a deliverable.
- `Propagation_Plan.md` §7–§8 and `Handoff_State.md` (ACCEPTED,
  `OPEN_PENDING_DERIVATIVE_CLOSURE`).

**Coordination record.**
- `_COORDINATION.md` does not record a representation or a dependency
  tracking mode.
- All 53 deliverable `_DEPENDENCIES.md` files record `ProjectMode = FULL_GRAPH`.
- There is no accepted project DAG (`execution/_DAG/` is absent; D-GOV-49),
  so there is no `project-dag` currency audit and nothing is `DAG pending`.
- **Proposed:** confirm FULL_GRAPH as the recorded mode for this run. The
  human-owned `_COORDINATION.md` is not written.

| Treatment | Entities | Route |
|---|---|---|
| Scaffold (Phase 5.2–5.3) | None: no deliverable ADD | — |
| Retirements (Phase 5.4) | None: no REMOVE | — |
| Modified (Phase 5.5) | 9 deliverables, all `SOW_V1` at `IN_PROGRESS`: DEL-02-02, DEL-02-03, DEL-03-03, DEL-07-01, DEL-07-02, DEL-07-04, DEL-07-05, DEL-08-03, DEL-09-03 | The accepted group-2 write boundary named each `ScopeOfWork.md` (W-a), so the amendment already changed it. `scope-of-work` `MODE=VERIFY` only (no REVISE). None is at `CHECKING` or `ISSUED`, so nothing is held and no reopening is needed |
| Dependency refresh (Phase 5.6, FULL_GRAPH) | The 9 affected deliverables and 16 neighbours, each with an ACTIVE edge to or from an affected deliverable: DEL-02-01, DEL-02-04, DEL-02-05, DEL-03-02, DEL-03-04, DEL-04-04, DEL-05-02, DEL-05-04, DEL-06-03, DEL-06-04, DEL-07-03, DEL-08-01, DEL-08-02, DEL-08-04, DEL-08-05, DEL-09-02. DEL-04-03 is left out: its only recorded edge is the RETIRED row DEP-03-03-009. The earlier draft counted it (17), and including it would be a harmless over-inclusion | `dependency-extract` (`MODE: UPDATE`, one deliverable per brief), then `audit-dep-closure` over the accepted inventory (SCOPE ALL). The expected outcomes are in `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`; the post-extraction `audit-scope-closure` checks them |
| Stale derivatives | `_SEMANTIC.md` / `_SEMANTIC_LENSING.md` of the 9 modified deliverables (the project uses semantic lensing) | Reported stale. Rerun only if the owner selects it |
| Decisions reserved for the owner | HGD-2 for DEP-02-01-008 only. Retiring DEP-02-01-007 was accepted at groups 1 and 2 | See `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md` |

There are no estimates, schedules or hypergraph for the App (`_Estimates`,
`_Schedule` and `_Aggregation` are absent).

**Gate question (Phase 5.1):**

> Accepted amendment SCA-APP-011 (register hash 41609731…c22): 0 to
> scaffold, 0 retired, 9 modified (0 held at `CHECKING` or `ISSUED`), 16
> neighbours for dependency refresh under FULL_GRAPH. Confirm this
> incremental plan?

**After confirmation:**
1. Phase 5.5 VERIFY runs.
2. Phase 5.6 extraction and closure run straight through. The extraction
   derives rows from the source text and applies the owner's HGD-2 ruling on
   DEP-02-01-008.
3. Phase 5.7 writes the run record and one `SETUP_LOG.md` line (`COMPLETE`,
   `PARTIAL` or `BLOCKED`).
4. `audit-scope-closure` is rerun.
