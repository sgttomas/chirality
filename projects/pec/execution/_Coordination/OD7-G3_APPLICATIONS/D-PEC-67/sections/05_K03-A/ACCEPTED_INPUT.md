# OD7-G3 K03-A — PEC-K-03 Interface Classification Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED
**Candidate gate:** `OD7-G3-K03-A`
**Provisional PEC carrier:** `D-PEC-67`
**Exact PRD candidate:** `../candidate_tree/K03-A/projects/pec/docs/PRD.md`
**Exact PRD diff:** `../diffs/K03-A_PEC_PRD.diff`

## Exact candidate interpretation

Classify PEC-K-03 as a PEC-owned interface requirement, not an external
harness obligation:

1. PEC provides a pull-oriented, labeled, non-authoritative orientation
   interface.
2. PEC never self-polls, schedules a consumer, injects into an agent, or
   claims an external polling cadence.
3. An explicitly opted-in consumer decides under its own authority whether
   and when to consume.
4. If a consumer injects PEC data, verify-before-rely is an interface
   precondition; it does not require injection.
5. PEC absence and zero-contact operation remain supported through
   file-native truth.

This interpretation creates no external scope. Lack of consumer adoption is a
product uptake or falsification signal, not external nonconformance.

## Required propagation if accepted

The current accepted PEC-K-03 literally assigns polling and injection to
harnesses. K03-A materially narrows that text. Therefore acceptance requires:

1. an exact PEC PRD amendment using the accompanying candidate row;
2. after PRD adoption, PEC SCOPE_CHANGE over constraint C3 and every mapped
   scope/deliverable/ScopeOfWork surface whose accepted meaning changes; and
3. non-binding notices to likely consumers.

Conditional write surfaces are the PEC PRD adoption record and exact PRD row,
then only the surfaces accepted through that later SCOPE_CHANGE.

No receiving loop is bound, and no polling or injection implementation is
authorized.
