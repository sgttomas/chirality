---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
phase: R4
status: owner_approved_by_standing_direction
authority: D-PEC-69
population: 11
claim_repairs: 56
---

# R4 — owner-approved exact repair disposition

## Recommendation

Apply the smallest whole-contract semantic repairs supported by the accepted
W1 claim ledgers and independent population verification:

| Deliverable | Repair-candidate local IDs |
|---|---|
| `DEL-00-01` | `OUT-002`, `CLM-002`, `REQ-005`, `AC-003`, `VER-002`, `AX-002`, `AX-004`, `AX-006` |
| `DEL-03-06` | `CLM-016`, `CLM-020`, `AX-012` |
| `DEL-04-01` | `CLM-016`, `CLM-018`, `REQ-010`, `AX-007`, `AX-012`, `AX-013` |
| `DEL-04-02` | `CLM-016`, `CLM-017`, `REQ-013`, `AX-013` |
| `DEL-04-03` | `CLM-016`, `CLM-017`, `AX-011` |
| `DEL-08-01` | `CLM-003`, `CLM-004`, `AX-004`, `AX-006` |
| `DEL-08-03` | `CLM-011`, `REQ-005`, `CON-001`, `CON-003`, `AX-006`, `AX-010` |
| `DEL-08-04` | `CLM-002`, `CLM-008`, `CLM-010`, `CLM-014`, `CON-005`, `AX-012` |
| `DEL-10-01` | `CLM-004`, `CLM-007`, `AX-005`, `AX-007` |
| `DEL-10-10` | `CLM-001`, `CLM-002`, `CLM-004`, `CLM-005`, `CLM-020`, `AX-011` |
| `DEL-10-11` | `CLM-003`, `CLM-015`, `CLM-017`, `CON-003`, `AC-015`, `AX-009` |

Whole-contract bookkeeping is repaired with the same tranche: current
decomposition basis is revision 1.3 at SCA-003 merge `11a494e9a`; earlier
revision-1.1/-1.2 and stale `_REFERENCES.md` statements remain explicitly
historical; quotation records are refreshed; embedded lifecycle prose is
corrected to the authoritative `INITIALIZED` value without editing
`_STATUS.md`.

## Preserved boundaries

- Retain every stable local ID, heading order, objective/scope mapping,
  output/acceptance/verification matrix, dependency, topology fact, and
  unaffected semantic claim.
- Retain all twenty-two explicit W1 `UNKNOWN` records; infer no answer.
- Create no product scope, receiving-loop duty, polling event, cadence,
  injection requirement, consumer conformance criterion, implementation,
  runtime, lifecycle transition, release, dependency, estimate, or schedule.
- Preserve `PEC-HOLD-001` as active.

## Ruling

D-PEC-69 records the owner's standing approval of RECONCILIATION
recommendations R0–R6 and specifically approves the smallest exact
whole-contract repairs once discovery and fan-in establish them. This
recommendation therefore stands as the owner-approved R4 ruling.

W1 deterministic fan-in reports 794 definitions / 794 ledger rows,
56 repair candidates, zero authority conflicts, and no semantic blocker.
Independent population verification confirms eleven selected contracts and
twenty-one controls. Repair may proceed under the D-PEC-69 exact write fence.
