# HANDOFF — TM-PEC-013 SCA-004 ScopeOfWork currency

**Status:** FINALIZED / ROUTED
**Prepared by:** TASK_MANAGEMENT
**Receiving instrument:** WORKING_ITEMS, with one separate REVIEW cycle for
each successor ScopeOfWork
**Execution status:** NOT STARTED — separately scheduled owner act

This is a routed coordination instrument, not execution authority. It records
the owner's routing act and the bounded work surface; it does not amend or
accept a production contract, open a REVIEW, alter lifecycle state, or close
TM-PEC-013.

## Owner ruling of record

> AUTHORIZE TASK_MANAGEMENT to route TM-PEC-013 to WORKING_ITEMS with one
> REVIEW cycle per DEL-02-07, DEL-03-01, and DEL-04-01 successor SOW; route
> TM-PEC-014 to the DEL-00-03 owning workflow with REVIEW/owner exact-byte
> acceptance of the corrected SPEC. Set both priorities LOW. Preserve
> lifecycle, source, dependencies, and historical artifacts. Prepare routed
> handoffs only; execution remains separately scheduled.
>
> Hold on TM-PEC-023.

## Accepted basis and current preimages

- SCA-004 Gate 5 handoff:
  `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Handoff_State.md`,
  SHA-256 `919d40bba285ebdab987c17c4443d9583528f845fde0681c460788f5701dbc1c`.
- SCA-004 decision log:
  `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Decision_Log.md`,
  SHA-256 `c377d7f094b46ede1b0ec8f108e7c52e61dada9565227820415b47301a87cd3c`.
  `SCA004-G1` records OI-003 resolved by D-PEC-78 O-A and `SCA004-G5`
  records revision 1.4 executed without downstream repair.
- Authoritative SOFTWARE_DECOMP revision 1.4:
  `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, SHA-256
  `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`.
- Current SOW preimages:
  - DEL-02-07: SHA-256
    `ddc837ca8b87ad8af52cfc4ec8b06c8fef883bbc3eeca9eea9949fb6280b007b`.
  - DEL-03-01: SHA-256
    `756c5f2af726272645a3cee491862cf3ca1fb751becad39f82ff310128d5ba19`.
  - DEL-04-01: SHA-256
    `0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f`.

The preimages are discovery evidence, not accepted successor hashes. Each
later production cycle must reproduce its preimage before editing and bind
its own candidate, checklist, review, and acceptance evidence to the exact
successor bytes it produces.

## Nine-domain completeness scan

| Domain | Routed resolution surface |
|---|---|
| Action Item | TM-PEC-013 remains `OPEN`. Three current SOWs retain a present-tense OI-003-undecided/open premise after D-PEC-78 O-A and SCA-004 resolved OI-003. No HOLD or closure is inferred. |
| Assignment | `R=WORKING_ITEMS`; `S=REVIEW`, once per deliverable; `C=TASK_MANAGEMENT`; `I=HELP_HUMAN`. Accountability and every acceptance act remain human-only; no agent is A. |
| Prioritization | `LOW`, by owner ruling 2026-08-04. Execution is separately scheduled; this route creates no urgency or queue. |
| Deliverables | Exactly the current `ScopeOfWork.md` for DEL-02-07, DEL-03-01, and DEL-04-01. Each successor is a separate deliverable-local product and review basis. |
| Work | Replace only the stale OI-003-undecided/open premise with revision-1.4 currency and its D-PEC-78 O-A / SCA-004 citation. Preserve every unaffected requirement, criterion, verification method, boundary, and unknown. Exact per-deliverable fences are below. |
| Planning | Three independent one-deliverable cycles: reproduce preimage → produce one successor SOW → validate and derive its deterministic checklist → run one REVIEW against that exact successor → return for the required human artifact ruling. Do not batch a review across deliverables. REVIEW_TYPE remains owner-selected at each Gate 1. |
| Approval | This handoff authorizes routing only. WORKING_ITEMS production, REVIEW entry, and human acceptance of each exact successor are later acts. No lifecycle transition is requested or authorized. |
| Checking | Per successor: SOW_V1 validation; exact checklist derivation; source-hash and cited-basis reproduction; semantic-diff inspection; lifecycle/dependency/source/history preservation; immutable one-deliverable REVIEW snapshot; repository whitespace and containment checks. |
| Decisions | D-PEC-78 O-A and SCA004-G1/G5 supply the resolved premise. The 2026-08-04 owner ruling supplies assignment, LOW priority, routing, and preservation fences. No new product or lifecycle decision is made here. |

## Exact per-deliverable work fences

### DEL-02-07

Target:
`projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md`.

- Replace the current `CON-001` premise that the loop-registry home and shape
  remain an undecided `SOW-077` / `OI-003` owner question, plus any directly
  dependent present-tense phrasing, with a citation-bound statement that the
  question was resolved by D-PEC-78 O-A and SCA-004.
- Preserve the in-process interface boundary: the consumer still must not
  depend on registry path, filename, or serialization. Do not turn the resolved
  upstream choice into a local filesystem binding or expand the deliverable.
- Preserve all current dependency rows and lifecycle bytes.

### DEL-03-01

Target:
`projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md`.

- Replace the OI-003-awaiting-ruling premise in `CON-002`, `AX-012`, and any
  directly dependent present-tense phrasing with the accepted D-PEC-78 O-A /
  SCA-004 result.
- Preserve `TBD-005`: loop-to-project resolution for the per-project manifest
  remains separately unresolved. Do not collapse that unknown into the now
  resolved registry-home question.
- Preserve the stable in-process interface boundary and every dependency edge;
  add, remove, or reclassify no edge.

### DEL-04-01

Target:
`projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md`.

- Replace the stale OI-003-open premise in `TBD-003`, `AX-012`, and any
  directly dependent present-tense phrasing with the accepted D-PEC-78 O-A /
  SCA-004 result.
- Preserve the current statement that DEL-04-01 has no local execution edge to
  DEL-01-06 and obtains loop identity from the record tier. Do not invent a
  DEL-01-06 dependency or change the three-edge upstream set.
- Preserve every other unknown, boundary, dependency row, and lifecycle byte.

## Review and return contract

For each deliverable, WORKING_ITEMS must hand REVIEW exactly one validated
successor SOW. REVIEW must consume a checklist emitted by
`tools/scope_of_work/derive_review_checklist.py` whose source SHA matches that
successor and bind any finding and immutable snapshot to those exact bytes.
`REVIEW_TYPE` remains unselected here and must be selected by the owner at each
deliverable's Gate 1. A review may recommend acceptance or HOLD; it must not
modify the SOW or lifecycle state. The owner rules artifact acceptance
separately. If the minimal currency repair cannot be completed without a scope,
dependency, lifecycle, or unrelated contract change, stop and return the
conflict rather than widen this route.

## Preservation and closure boundary

This route preserves all source, dependency, decomposition, SCA, historical
handoff/reconciliation/review, foreign-loop, and lifecycle bytes. It authorizes
no implementation, issuance, release, reliance, schedule, or professional
claim. TM-PEC-013 remains `OPEN` with blank disposition and closure evidence;
later TASK_MANAGEMENT may propose closure only after all three exact successors
are human-accepted and their evidence is committed.
