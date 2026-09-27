# SCA-APP-012 — `project-setup` INCREMENTAL: incremental plan (PROPOSAL, awaiting the owner)

> **2026-09-27 — decided and executed.** The owner confirmed this plan under FULL_GRAPH (`CHAT_TRANSCRIPTION.md`). Setup ran and is COMPLETE (`SETUP_RUN_RECORD.md`). The text below is the proposal as reviewed and is kept unchanged.

**Status: PROPOSAL. Nothing in this proposal is written.**

`project-setup` Function 5 (bundled `workflows/project-setup/`,
`resources/method.md` Phases 5.0–5.1) needs owner confirmation before any
setup write. This time only one gate applies:
- **Phase 5.0 (baseline): not needed.** `_Coordination/SETUP_LOG.md` already
  holds its `BASELINE` line (adopted 2026-09-27, amendments accepted up to
  2026-09-07, latest SCA-APP-010). The method runs Phase 5.0 only "when
  `SETUP_LOG.md` has no `BASELINE` line".
- **Phase 5.1 (plan): needs the owner.** "Do not write before the human
  confirms the plan."

`_COORDINATION.md` is read, not edited.

## A. The Function 5 queue

| Amendment | Accepted | Covered by the baseline? | `SETUP_LOG.md` | In this plan? |
|---|---|---|---|---|
| SCA-APP-001 … SCA-APP-010 (with the DEL-02-05 carrier addendum) | 2026-06-13 … 2026-09-07 | Yes | `BASELINE` line | No; never reprocessed |
| SCA-APP-008 | Not accepted | — | — | No; a candidate is never set up |
| SCA-APP-011 | 2026-09-27 | No (hands setup to INCREMENTAL) | `INCREMENTAL SCA-APP-011 setup COMPLETE` | No; already complete |
| SCA-APP-012 | 2026-09-27 (`checkpoint_snapshots/SCA-APP-012_GROUP-3_2026-09-27/`) | No (`Handoff_State.md`, next owning workflows 1) | none | **Yes** |

No other accepted amendment waits, so the plan covers SCA-APP-012 alone and
no later amendment acts on the same entities.

## B. Phase 5.1 — the incremental plan for SCA-APP-012

**Inputs**
- Accepted snapshot:
  `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/`,
  named by `_ScopeChange/_LATEST.md`.
- Register `Amendment_Actions.csv`, resolved through
  `checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/ACCEPTED_MANIFEST.csv`.
  SHA-256 `a9ff78f2be8356b7727d7bb853bd758a55cb6a976b42dc2fc8dc1d1365e114ad`,
  verified. It has 24 rows: 23 MODIFY and 1 ADD. The ADD is the DEC-027
  decision-log row, not a deliverable. Ten MODIFY rows name a deliverable.
  The other 13 MODIFY rows name decomposition, PRD, SPEC or PLAN text
  (`EntityType` OTHER), which the amendment already applied; they need no
  setup action.
- `Propagation_Plan.md` §7–§8 and `Handoff_State.md` (ACCEPTED,
  `OPEN_PENDING_DERIVATIVE_CLOSURE`).
- Amended decomposition SHA-256
  `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577`, equal to
  the post-acceptance validation record.

**Coordination record.**
- `_COORDINATION.md` still records no representation or dependency tracking
  mode.
- 53 deliverable `_DEPENDENCIES.md` files record `ProjectMode = FULL_GRAPH`.
  The 54th, retired DEL-09-07, records none.
- The owner confirmed FULL_GRAPH for the SCA-APP-011 run. Because
  `_COORDINATION.md` still does not record it, the mode is named again in this
  gate question rather than assumed.
- There is no accepted project DAG (`execution/_DAG/` is absent; D-GOV-49), so
  there is no `project-dag` currency audit and nothing is `DAG pending`.

| Treatment | Entities | Route |
|---|---|---|
| Scaffold (Phase 5.2–5.3) | None: no deliverable ADD | — |
| Retirements (Phase 5.4) | None: no REMOVE | — |
| Modified (Phase 5.5) | 8 deliverables, all `SOW_V1` at `IN_PROGRESS`: DEL-02-01, DEL-02-02, DEL-02-03, DEL-06-03, DEL-07-02, DEL-07-03, DEL-08-02, DEL-08-03 (register rows 1–6, 19, 20, 22, 23) | The accepted group-2 write boundary (`Propagation_Plan.md` §2, T-a) named each `ScopeOfWork.md`, so the amendment already changed it. `scope-of-work` `MODE=VERIFY` only (no REVISE). None is at `CHECKING` or `ISSUED`, so nothing is held and no reopening is needed |
| Dependency refresh (Phase 5.6, FULL_GRAPH) | The 8 affected deliverables and 16 neighbours, each with an ACTIVE `Dependencies.csv` edge to or from an affected deliverable: DEL-02-04, DEL-02-05, DEL-04-04, DEL-05-02, DEL-05-03, DEL-05-04, DEL-06-01, DEL-06-02, DEL-07-01, DEL-07-04, DEL-07-05, DEL-08-01, DEL-08-04, DEL-08-05, DEL-09-02, DEL-09-04. DEL-01-03 is left out: its only recorded edge is the RETIRED row DEP-02-01-014. The declared sections of `_DEPENDENCIES.md` add no neighbour (they point to the registers), and the impact assessment names none for dependency review | `dependency-extract` (`MODE: UPDATE`, one deliverable per brief), then `audit-dep-closure` over the accepted inventory (SCOPE ALL, exemptions DEL-00-01, DEL-00-02 and retired DEL-09-07). The expected outcomes are in `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`; the post-setup `audit-scope-closure` checks them |
| Stale derivatives | `_SEMANTIC.md` / `_SEMANTIC_LENSING.md` of the 8 modified deliverables (all eight carry both) | Reported stale. Rerun only if the owner selects it (as for SCA-APP-011, where it was not selected) |
| Decisions reserved for the owner | None beyond this gate. DX-01 (retire DEP-02-03-009) was accepted at group 1 (R-b) | See `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md` |

There are no estimates, schedules or hypergraph for the App (`_Estimates`,
`_Schedule` and `_Aggregation` are absent).

**The extraction set is wider than `Propagation_Plan.md` §8 item 2.** That
item names DEL-02-03 and DEL-08-03, the two registers where changes are
expected. Phase 5.6 under FULL_GRAPH dispatches every affected deliverable and
its neighbours, as the SCA-APP-011 run did (25 registers). This plan follows
the workflow. The six other modified registers and the 16 neighbours are
expected to change only in `LastSeen`: a quote screen finds every ACTIVE quote
in them in its cited source.

**Gate question (Phase 5.1):**

> Accepted amendment SCA-APP-012 (register hash a9ff78f2…14ad): 0 to
> scaffold, 0 retired, 8 modified (0 held at `CHECKING` or `ISSUED`), 16
> neighbours for dependency refresh under FULL_GRAPH. Confirm this
> incremental plan?

**After confirmation:**
1. Phase 5.5 VERIFY runs over the eight modified contracts.
2. Phase 5.6 extraction and closure run straight through. The extraction
   derives rows from the source text; DX-01 to DX-07 are checked afterwards.
3. Phase 5.7 writes the run record and one `SETUP_LOG.md` line (`COMPLETE`,
   `PARTIAL` or `BLOCKED`).
4. `audit-scope-closure` is run against SCA-APP-012.
