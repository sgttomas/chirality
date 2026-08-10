# TM-PEC-013 revision 02 exact repair map

Only the following review-cited claim locations changed from the reviewed
preimages named in `PREIMAGE_AND_AUTHORITY.md`.

| Deliverable / finding | Claim location | Exact repair |
|---|---|---|
| DEL-02-07 RF-001 | CLM-006 | Replaced the stale DEP-02-07-003 `Statement`, `SourceRef`, and `EvidenceQuote` assertions with the live row values; retained the edge count, target, maturity, confidence, origin, notes, and two-anchor description. |
| DEL-02-07 RF-002 | CLM-010 | Replaced lifecycle `OPEN` with governed `INITIALIZED`; retained the no-implementation and future-contract qualification exactly. |
| DEL-03-01 RF-001 | CLM-010 | Removed the false shared `EvidenceFile` assertion, added `EvidenceFile` to the fields that differ, and replaced the stale evidence narrative with the live source-specific loci for DEP-03-01-004 through DEP-03-01-014. The eleven targets, statements, notes, count, topology, maturity, satisfaction, and common fields are unchanged. |
| DEL-03-01 RF-002 | CLM-022; AX-013 | Replaced lifecycle `OPEN` with governed `INITIALIZED` in both cited claims; retained all surrounding no-implementation, lifecycle-neutrality, and future-contract language. |
| DEL-04-01 RF-001 | CLM-008 | Removed the false shared historical-exhibit `EvidenceFile` assertion and recorded the live row values in order: `ScopeLedger.csv`, `Deliverables.csv`, and `docs/PRD.md`; retained the separate historical-exhibit quotation and all topology, target, statement, maturity, stratum, and notes claims. |
| DEL-04-01 RF-002 | CLM-009 | Replaced the all-`INITIALIZED`/no-baseline-artifact assertion with live state: DEL-10-01 `CHECKING`, DEL-01-01 and DEL-03-01 `INITIALIZED`, and both DEL-10-01 baseline artifacts present. Retained the contract-as-boundary-input posture and added no reliance or acceptance claim for those artifacts. |

No other revision-02 claim location was edited. The earlier SCA-004/OI-003
producer edits remain the unchanged reviewed basis for this repair.
