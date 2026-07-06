# D-PEC-09 - PROPOSAL: CSV formula-injection neutralization in exports

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-09
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Owner ruling that opened this row

Owner ruling of record (verbatim, 2026-07-05, in-session, Ryan Tufts):

> S-4 (register rows): affirmed. Because I adopt the brief this session, open D-PEC-08
> scoped to the remaining gate only — the source-tranche authorization for the upload-agent
> implementation — AWAITING_RULING. Open D-PEC-09 for the CSV formula-injection repair,
> AWAITING_RULING and design-only; it authorizes no source change.

## Finding

The D-PEC-07 artifact review recorded RV-24: CSV formula-injection neutralization
is absent from exported CSV escaping. The finding was discovered during review
of D-PEC-07 artifacts but is a pre-existing application behavior, not a defect
of the ruled D-PEC-07 packet, runbook, or brief.

## Decision to rule

Whether to authorize a future repair tranche that neutralizes spreadsheet
formula vectors in exported CSV fields that begin with `=`, `+`, `-`, or `@`
after import/export round trips.

## Scope boundary

This packet is design-only and AWAITING_RULING. It authorizes no source change,
no test change, no import/export behavior change, and no mutation of PEC data.

Structure precedent: this packet follows the PEC-local residual-work row
convention in `_REGISTER.md` and the narrow-repair decision pattern used by
D-PEC-06.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Authorize a narrow CSV export-neutralization repair. | A later branch may change only the ruled CSV escaping/export scope and tests. |
| O-B | Defer. | Current CSV export behavior remains unchanged; the finding stays parked. |

## Recommendation (non-binding)

O-A in a later narrow PR, after owner ruling. The repair should be scoped to CSV
export neutralization and regression tests, with no unrelated import or data
model changes.
