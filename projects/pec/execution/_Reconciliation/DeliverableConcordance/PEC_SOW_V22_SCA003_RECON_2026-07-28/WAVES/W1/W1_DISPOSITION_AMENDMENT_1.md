---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
amendment: 1
status: accepted
authority: D-PEC-69 R2/R4/R6 and owner standing completion direction
verifier_source: W1_LEDGER_VERIFICATION.md
---

# W1 disposition amendment 1

The independent ledger verifier rejected the initial 56-row candidate fan-in
for one omitted semantic mismatch:

| Field | Corrected value |
|---|---|
| ClaimRowID | `DEL-10-11-CR-002` |
| DeliverableID | `DEL-10-11` |
| LocalID | `CLM-002` |
| Prior disposition | `ALIGNED`; `RepairNeeded=NO` |
| Corrected disposition | `DOCUMENTED_DIFFERENTLY`; `RepairNeeded=YES` |
| Exact repair | Preserve the parity metric statement and every recorded unknown; replace only the stale §11 heading quotation “measured in system behavior, not human behavior” with PRD v2.2 “measured in observable system and use behavior.” Create no receiving-loop duty or conformance condition. |

The original worker ledger remains immutable as discovery evidence. This
versioned amendment is the effective disposition for fan-in. The effective
repair set is 57 claims across the same eleven contracts. Definition/ledger
coverage remains 794/794; the amendment adds no row and resolves no `UNKNOWN`.

No further repair may proceed to W2 acceptance until a fresh independent
verification passes over the original ledgers plus this amendment.
