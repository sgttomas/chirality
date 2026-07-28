---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
phase: R4
amendment: 1
status: owner_approved
authority: owner standing completion direction relayed by Agent 0
population: 11
effective_claim_repairs: 57
---

# R4 amendment 1 — verifier-found DEL-10-11 correction

## Trigger

Independent W1 ledger verification found that `DEL-10-11/CLM-002` still quotes
the superseded PRD §11 heading “measured in system behavior, not human
behavior.” PRD v2.2 uses “measured in observable system and use behavior.”
This was the sole reason for the verifier's `FAIL`.

## Amended recommendation

Add `DEL-10-11/CLM-002` to the R4 repair set. Preserve the claim's parity
metric statement, denominator, silences, and explicit unknowns; replace only
the heading quotation. Do not derive a polling, contact, cadence, injection,
consumer-use, or receiving-loop-conformance duty.

The effective R4 set is now 57 claim repairs across the same eleven contracts.
All boundaries in `R4_OWNER_APPROVED_REPAIR.md` remain unchanged.

## Owner ruling

Agent 0 relayed the owner's standing completion direction and confirmed:

> Proceed with the versioned R4 amendment and fresh independent verification.
> The scan-governed DEL-10-11/CLM-002 correction is accepted under the
> standing completion direction; preserve the hold until the full 11-contract
> fan-in passes.

The amendment is therefore owner-approved. The initial failed verification is
preserved; a fresh independent verification is mandatory before W2 acceptance.
