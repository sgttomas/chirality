# OD7-G3 K11-A — PEC-K-11 Interface Classification Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED
**Candidate gate:** `OD7-G3-K11-A`
**Provisional PEC carrier:** `D-PEC-67`
**Exact PRD candidate:** `../candidate_tree/K11-A/projects/pec/docs/PRD.md`
**Exact PRD diff:** `../diffs/K11-A_PEC_PRD.diff`

## Exact candidate interpretation

Classify PEC-K-11 as a PEC-owned interface requirement, not an external
harness obligation:

1. PEC supports scope and mode parameters and never forces contact.
2. Pipeline and unscoped-conversation modes support testable zero-contact
   operation.
3. An explicitly opted-in consumer owns its own mode mapping and contact
   cadence unless that receiving owner separately adopts an exact duty.
4. PEC output remains non-authoritative and verify-before-rely.
5. Degraded operation uses file-native truth and starts no hidden execution
   loop.

This interpretation creates no external scope. Lack of consumer adoption is a
product uptake or falsification signal, not external nonconformance.

## Required propagation if accepted

The current accepted PEC-K-11 literally states that consumption follows the
modes ladder. K11-A materially narrows that text into a capability offered by
PEC with consumer-owned use. Therefore acceptance requires:

1. an exact PEC PRD amendment using the accompanying candidate row;
2. after PRD adoption, PEC SCOPE_CHANGE over constraint C15 and every mapped
   scope/deliverable/ScopeOfWork surface whose accepted meaning changes; and
3. non-binding notices to likely consumers.

Conditional write surfaces are the PEC PRD adoption record and exact PRD row,
then only the surfaces accepted through that later SCOPE_CHANGE.

No receiving loop is bound, and no consumer-mode implementation is
authorized.
