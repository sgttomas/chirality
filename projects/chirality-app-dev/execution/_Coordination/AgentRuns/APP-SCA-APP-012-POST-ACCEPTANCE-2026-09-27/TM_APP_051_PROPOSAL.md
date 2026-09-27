# TM-APP-051 — disposition note after SCA-APP-012 (PROPOSAL, for the row's owner)

**Status: PROPOSAL. No Task Management record is edited.**

## What the records say is owed

- **The proposed note.** SCA-APP-012 `Propagation_Plan.md` §8 item 5 proposes
  a disposition note for TM-APP-051 and adds: "Proposed disposition note for
  the row's owner (this workflow does not edit Task Management)". The group-3
  decision lists "the TM-APP-051 note" among the handoffs.
- **The row.** `TM-APP-051` ("Assign scope scan and route consumers") is a live
  row of `execution/_Coordination/_TaskManagement/REGISTER.csv`:
  - `Status` = `DEFERRED`; `AssociatedWith` = `APP-R024;DEL-02-03;SCA-APP-010`;
  - `Assignment` = "TBD (owning human decision or direct receiving owner;
    A=human-only)", so the row's owner is the human owner, not this loop;
  - `Trigger`: "A bounded DEL-02-03/SCA-APP-010 consumer comparison names each
    required receiver or identifies the precise orphan; the accountable human
    records any missing App/Runtime owner before implementation."
  - `SourceRef` is the 2026-09-22 remaining-work census and `CandidateRef` is
    `APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv` APP-R024.
- **Federation.** A read-only preflight on 2026-09-27
  (`tools/taskmgmt/taskmgmt.py federation --register
  projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv`)
  returned `COMPLETE` over four registers with `register_writes: 0`. No finding
  names TM-APP-051. The generated `.candidates/federation.json` is gitignored
  and was not kept.

## The note (verbatim from `Propagation_Plan.md` §8 item 5)

| Consumer | After SCA-APP-012 |
|---|---|
| Route | Retired with DEL-02-03-REQ-009 (R-b) |
| Scope scan | `/api/project/deliverables`; `/api/working-root/scope` retired |
| Status | Restated read-only by DEL-02-03-REQ-010 from `/api/project/deliverables` |
| Summary widget | Still unimplemented; stays with DEL-02-03 |

"The row then stays open only for the summary/status widget; this amendment
does not close it."

## Options

The owner chooses one.

1. **Recommended: row maintenance that records the note and keeps the row
   `DEFERRED`.** The tighter precedent is
   `ROW_MAINTENANCE_TM-APP-032_RESCOPE_2026-08-21.md`, which maintained a live
   `REGISTER.csv` row (APP-R058 was a row of the closed finite account, so its
   record was only a closure echo).
   - **Record:** `ROW_MAINTENANCE_TM-APP-051_SCA-APP-012_DISPOSITION_2026-09-27.md`
     in `_Coordination/_TaskManagement/`, holding the federation preflight
     verdict, the owner's act verbatim with its date, the evidence hashes and
     the exact row delta.
   - **Row delta (TM-APP-051 only):**
     - `Status`: retained `DEFERRED`;
     - `ScaRef`: `NONE` → `SCA-APP-012`;
     - `LastReviewed`: `2026-09-23` → the date of the owner's act;
     - `Notes`: append "SCA-APP-012 (accepted 2026-09-27, checkpoint group 3;
       landed in PR #1020, `bc1ea504d`) disposes three of the four consumers:
       route retired with DEL-02-03-REQ-009 (R-b); scope scan is
       `/api/project/deliverables`, `/api/working-root/scope` retired; status
       restated read-only by DEL-02-03-REQ-010 from `/api/project/deliverables`.
       The summary widget is still unimplemented and stays with DEL-02-03; the
       row stays open for it only.";
     - every other field unchanged, including `Trigger`, `SourceRef`,
       `SourceSha`, `EvidenceRef`, `EvidenceSha` and `EvidenceQuote`.
   - **Variant 1b (not recommended here):** also narrow `Concern` and
     `Trigger` to the summary/status widget. That rewrites the row's scope and
     is the owner's call; the plan asks only for the note.
   - **Prerequisites:** rerun the federation preflight at write time and
     transcribe the owner's act verbatim.
2. **Record nothing now.** The accepted DEL-02-03 `ScopeOfWork.md` already
   carries the dispositions. The row keeps describing four unmapped consumers
   although three are disposed, and `audit-scope-closure` would carry the note
   as an open handoff (at best `CLOSED_WITH_OBSERVATIONS`).

**Observation, not proposed:** the row's `EvidenceSha`
(`4aba6a5c…33e1`) no longer matches DEL-02-03 `ScopeOfWork.md`
(now `ac34b8dc…cc91`, after SCA-APP-011 and SCA-APP-012). Option 1 leaves the
evidence fields as they are, as the TM-APP-032 precedent did; refreshing them
is a separate row-maintenance choice.

**Proposed owner answer:** "TM-APP-051: option 1."
