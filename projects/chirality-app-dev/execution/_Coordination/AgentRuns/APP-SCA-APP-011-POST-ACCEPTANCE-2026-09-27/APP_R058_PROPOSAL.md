# APP-R058 — disposition after SCA-APP-011 (PROPOSAL, for the row's owner)

**Status: PROPOSAL. No Task Management record is edited.**

## What the records say is owed

- SCA-APP-011 `Propagation_Plan.md` §8 item 6 proposes the disposition note
  "closed by removal under SCA-APP-011 (DEL-07-02 SCA-APP-011 section)". It
  adds: "The row's owner records it; this workflow does not edit Task
  Management."
- The row is `APP-R058` in the finite retirement account
  `execution/_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv`.
  - `HumanDecision` = `OWNER_FINAL_RETIREMENT_2026-09-23`;
    `RiskFlag` = `DEFER_WITH_HOLD`.
  - `AffectedActUntilResolved`: "No scaffold live-operation acceptance while
    ProjectScaffoldPort/501 composition is absent."
  - The owner of the row is therefore the human owner, not this loop.

## What is already true in the accepted scope text

- **The clause is closed.** The DEL-07-02 `ScopeOfWork.md` retired-status
  clause for APP-R058 (line 477) ends: "Closed by SCA-APP-011: the App
  scaffold route is retired, so no App live scaffold operation remains to
  repair."
- **The controlling section says the same.** The DEL-07-02 SCA-APP-011
  controlling section (line 24) states: "APP-R058 is closed by removal."
- **The hold's premise is gone.** Nothing is left to accept: the App route no
  longer exists, and the Runtime's own scaffold API is the Runtime loop's
  decision (notice sent 2026-09-27).

## Proposal

The owner chooses one of these.

1. **Recommended — append a dated row-maintenance record** in
   `_Coordination/_TaskManagement/`, following the precedent
   `ROW_MAINTENANCE_TM-APP-032_RESCOPE_2026-08-21.md`. It would be named
   `ROW_MAINTENANCE_APP-R058_SCA-APP-011_CLOSURE_2026-09-27.md` and record
   that APP-R058 is closed by removal under SCA-APP-011:
   - accepted group 3, `checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`;
   - landed in PR #995, `78e74f590`;
   - DEL-07-02 SOW line 477 and its SCA-APP-011 section.

   It would also record that the `DEFER_WITH_HOLD` hold is released. The
   bytes of `ROWS.csv`, the immutable finite account, stay unchanged.
2. **Record nothing further.** The DEL-07-02 SOW already carries the closure,
   and the account stays as dated history.

**Proposed owner answer:** "APP-R058: option 1."
