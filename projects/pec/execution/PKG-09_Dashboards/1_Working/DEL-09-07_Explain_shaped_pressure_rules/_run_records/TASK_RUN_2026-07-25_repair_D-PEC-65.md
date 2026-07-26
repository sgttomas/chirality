# TASK RUN — D-PEC-65 register evidence repair (DEL-09-07)

- **Date:** 2026-07-25
- **Instrument:** `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED §7)
- **Agent:** sealed ephemeral Agent 2 repair dispatch (file-tool-only), package `PKG-09_Dashboards`
- **File touched:** `Dependencies.csv` (EXECUTION rows only; ANCHOR rows read-only)

## Rows dispositioned

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-09-07-003 | DUP (EVQ-001) | REPAIRED (+ Statement edit) | `execution/_Decomposition/Deliverables.csv` |
| DEP-09-07-004 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-09-07-005 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-09-07-006 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-09-07-007 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-09-07-008 | DUP (EVQ-001) | REPAIRED (+ Statement edit) | `execution/_Decomposition/ScopeLedger.csv` |

Counts: 6 EXECUTION rows inspected, 6 repaired, 0 waived, 0 already-clean,
0 blocked. 2 ANCHOR rows untouched.

## Cells changed

All six rows: `EvidenceFile` re-pointed off the frozen D-PEC-62 PLAN exhibit;
quote-free register-row locus in `SourceRef`; verbatim single-line span in
`EvidenceQuote`. Rows 004–008 are grounded on the ScopeLedger row of the
*producing* deliverable, each of which names the exact input the pressure rule
consumes.

- DEP-09-07-003 — locus `Deliverables.csv row DEL-09-06`; shared-component quote.
- DEP-09-07-004 — locus `ScopeLedger.csv row SOW-006` (covered by DEL-04-03);
  examined-through SHA + per-feed freshness are the staleness-rule input.
- DEP-09-07-005 — locus `ScopeLedger.csv row SOW-010` (covered by DEL-03-01);
  the record tier the stuck-in-state age is read from.
- DEP-09-07-006 — locus `ScopeLedger.csv row SOW-019` (covered by DEL-03-03);
  drift classification output feeds the drift-density rule.
- DEP-09-07-007 — locus `ScopeLedger.csv row SOW-023` (covered by DEL-05-01);
  Explain-shaped gate verdicts feed the gate-blocked rule.
- DEP-09-07-008 — locus `ScopeLedger.csv row SOW-031` (covered by DEL-06-06);
  advisory overlap detection feeds the collision-risk rule.

## Statement edits flagged

**2 edits.**

1. **DEP-09-07-003**
   - Before: `Literal resolution of 'the other six views'; refuters recommend dropping; owner ruling requested`
   - After: `DEL-09-07 counted among the six views consuming the shared drill-down component; refuters recommend dropping; owner ruling requested`
   - Reason: the seeded text described the basis dispute and asserted no
     dependency claim at all. The rewrite states the claim the row makes and
     preserves the refuters' recommendation and the pending owner ruling; the
     row's `Flag=AMBIGUOUS_BASIS` in Notes is untouched.

2. **DEP-09-07-008**
   - Before: `P3 producer for a P2 consumer; staged rule set vs soft edge — owner classification requested`
   - After: `Collision-risk rule consumes DEL-06-06 overlap detection; P3 producer for a P2 consumer — owner classification requested`
   - Reason: the seeded text was a pure phase-tension provenance note stating
     no dependency claim. The rewrite states the claim and preserves the open
     classification question; `Flag=PHASE_TENSION` in Notes is untouched.

## Waivers declared

None. No `Dependencies_EvidenceWaivers.csv` created.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MIN-4** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-09-07-008` | `Statement` | `Collision-risk rule consumes DEL-06-06 overlap detection; P3 producer for a P2 consumer — owner classification requested` | `Collision-risk rule consumes DEL-06-06 overlap detection; P3 producer for a P2 consumer — owner classification requested; staged rule set vs soft edge` |

`EvidenceFile`, `SourceRef`, and `EvidenceQuote` are untouched; the evidence
repair recorded above stands unchanged. `DEP-09-07-003`'s `Statement` edit is not
in the finding set and is untouched.

Why: the earlier flagged `Statement` rewrite dropped the seeded qualifier naming
the two dispositions the owner is being asked to choose between (staged rule set
vs soft edge). The disposition restores it inline by append, so the dependency
claim, the phase tension, and the offered resolutions now stand together.
`Flag=PHASE_TENSION` in `Notes` is untouched.

**Integrity:** the appended text introduces no comma, so the cell remains a valid
unquoted CSV field. Row re-read post-edit: 29 columns intact.
