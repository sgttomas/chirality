# D-T0-14 - PROPOSAL: PEC data residency and instance-content visibility

**Status:** PROPOSAL / awaiting owner ruling.  
**Date prepared:** 2026-07-04  
**Decision ID:** D-T0-14  
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Decision to rule

Decide whether and under what conditions agents may view or capture PEC
instance content, including pilot DB content, register exports, reports, and
visibility-filtered logs.

## Verified facts

| Fact | Source |
|---|---|
| PEC log visibility is role-filtered and title/detail-bearing rows are redacted outside the actor's visible logs. | `projects/pec/docs/SPEC.md:80-85`, `projects/pec/docs/SPEC.md:468-471` |
| Register, report, import/export, plan, schedule, and lookahead routes expose project data through API/read surfaces. | `projects/pec/docs/SPEC.md:355-372`, `projects/pec/docs/SPEC.md:513-533` |
| Real pilot work remains human and may involve real MDL/RAIL/decision/risk data. | `projects/pec/docs/STATUS.md:82-87` |
| The server and backup tools use configurable database and backup paths. | `projects/pec/server/src/index.ts:16-22`, `projects/pec/tools/backup.ts:18-32` |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | CLOSED/TBD for now: agents read committed repo files only; no instance-content capture or egress unless separately authorized. | Gate-safe default and no privacy surprise. |
| O-B | Owner-approved exported artifacts only, with an actor/visibility basis and immutable capture manifest. | Enables bounded L1/L2 evidence while preserving traceability. |
| O-C | Open residency for PEC instance content. | Broadest access; requires explicit owner comfort with real project-controls data exposure. |
| O-D | Custom residency rule. | Owner supplies provider/location/visibility constraints. |

## Recommendation

Frame only. If deferred, use O-A as the gate-safe default. For any future
capture of instance data, require a declared actor/visibility basis and write a
manifest with source refs, command refs, output paths, and limitations.

## Human ruling

HumanRuling: OPEN - awaiting owner ruling.

