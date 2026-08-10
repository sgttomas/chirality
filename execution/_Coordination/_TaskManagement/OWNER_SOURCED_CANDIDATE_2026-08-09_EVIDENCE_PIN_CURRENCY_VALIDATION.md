# Owner-Sourced Candidate — Evidence-Pin Currency Validation Gap

Date: 2026-08-09

Status: **PREPARATION ONLY — NOT PROMOTED — NOT DISPOSED**

Source: accountable-human direction
`OWNER_DIRECTION_2026-08-09_ROOT_EVIDENCE_PIN_CLASS_CLOSURE.md`, SHA-256
`7a78ee04d1dc53dccc7dff9695e1d3a92478a0bb985d06e7bf665c8e32feffa3`.

This owner-sourced candidate arrived after acceptance of the Step-2 harvest.
It is not a harvest product and does not amend
`CANDIDATE_HARVEST_2026-08-09_GENERATIONAL_PASS.md`.

## Candidate

Proposed title: **Root register validation does not check evidence-pin
currency**

Concern: `taskmgmt validate` passed both Root registers while archived rows
`TM-ROOT-109` and `TM-ROOT-121` pinned bytes that had changed after closure.
The validator checks schema and referential form but does not compare an exact
64-hex `EvidenceSha` against the current committed bytes of an exact-path
`EvidenceRef`. The bounded class sweep in
`EVIDENCE_PIN_CLASS_CLOSURE_2026-08-09.md` found 11 mechanically eligible
rows, of which exactly two were stale before the owner-ruled repair.

Suggested lenses: `Checking;Work;Decisions`.

No candidate ID, assignment, priority, status, or disposition is inferred.

## Owner-gate disposition options

1. **New row.** Promote this validator-currency concern as a distinct Root
   action item, preserving its evidence-pin-specific scope and explicit
   handling of composite/unpinnable references.
2. **Fold into validator-quality genus.** Fold the concern into one or both
   of `TM-ROOT-113` and `TM-ROOT-115` at the owner gate, with an explicit
   Notes citation and a bounded validator/test target. This preparation does
   not choose which survivor or imply that either existing row already covers
   evidence currency.

The candidate is to be presented with the next owner slate. Until the owner
rules, no register row changes and no validator implementation are authorized.
