# HANDOFF — SCA-004 metadata-alignment dispatch (routed instrument)

**Status:** FINALIZED / ROUTED IN THE 2026-08-03 CLOSEOUT TRANCHE — owner
activation ruling 2026-08-03 (deferral review: TM-PEC-023 ACTIVATABLE,
activation authorized). Prepared by TASK_MANAGEMENT; the TM session executes
no alignment work itself. This handoff routes to the named owning
instruments (PROJECT_SETUP / WORKING_ITEMS); the work session is a
separately scheduled owner act. This file is coordination, never authority:
it performs no lifecycle, acceptance, release, or reliance act.

**Register carriers:** TM-PEC-012 (primary), TM-PEC-023 (rider),
TM-PEC-017 and TM-PEC-015 (currency sweep) — all four rows cite this file
as carrier.

**Named instrument:** PROJECT_SETUP and WORKING_ITEMS — the "next owning
workflows" named by
`projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Handoff_State.md`
(SHA-256 `919d40bba285ebdab987c17c4443d9583528f845fde0681c460788f5701dbc1c`;
`MetadataAlignmentState: NOT_STARTED`) for separately authorized
regeneration/re-pin work.

## One dispatch, three register concerns (owner cross-relation)

Per the owner's 2026-08-03 promotion ruling, the eventual currency sweep is
one dispatch, not three. Scope units:

1. **TM-PEC-012 (OPEN, primary)** — SCA-004 metadata and dependency-anchor
   alignment: the remaining 63 deliverable `_CONTEXT.md` provenance blocks;
   all 64 deliverable `_REFERENCES.md` packets; the DEL-01-06
   `Dependencies.csv` non-gating SOW-077 anchor refresh.
2. **TM-PEC-023 (DEFERRED rider; trigger = this dispatch)** — COV-062..070:
   SupportsObjectives mapping for DEL-00-02, DEL-03-05, DEL-05-01,
   DEL-07-02..05, DEL-08-05, DEL-10-08 (accepted revision-1.4 residue;
   source `.../COV_SCA004_POSTCHANGE_2026-08-03_1442/Decomp_Coverage_IssueLog.csv`,
   SHA-256 `8be2c2b512b83a1cd8b2c2f24630261fa0a14c219a7abdca6b76c0659d4de4b1`).
3. **TM-PEC-017 + TM-PEC-015 (currency sweep)** — the orientation-map and
   handoff-prose currency set: `projects/pec/README.md`,
   `projects/pec/docs/STATUS.md`,
   `projects/pec/execution/_Coordination/_COORDINATION.md`,
   `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`
   (TM-PEC-015), and the seven stale handoff files listed in TM-PEC-017's
   SourceRef. **Owner constraint (TM-PEC-017 Notes):** committed handoff
   files are point-in-time records — prefer supersession annotations or
   pointer corrections over editing historical evidence; the dispatched
   repair decides per file class.

## Boundaries the dispatch must honor

- Write scope: the named pec surfaces only; never a Task Management
  register (children never write registers), never a foreign loop surface.
- SCA-004's `CLOSED_FOR_SCOPE_CHANGE_ONLY` state and
  `ReadyForNextPhase: REGEN_ONLY` govern: regeneration/re-pin only, no new
  scope decisions.
- Related but excluded: TM-PEC-011 (DEL-01-06 `ScopeOfWork.md`
  `STALE_REBUILD_REQUIRED`, RF-002) is contract-repair work under its own
  review path, not metadata alignment; TM-PEC-013/014 (downstream SOW and
  SPEC currency) are `STALE_REVIEW_REQUIRED` items for their owning review
  instruments. The dispatch reports adjacency, performs neither.
- Closure evidence lands in the owning instruments' surfaces; the register
  records disposition and evidence after owner ruling (K-TM-3).
