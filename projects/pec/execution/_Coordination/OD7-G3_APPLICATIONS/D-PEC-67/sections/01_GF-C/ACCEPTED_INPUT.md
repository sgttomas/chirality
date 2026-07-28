# OD7-G3 GF-C — Global Event Feed Deferral Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED
**Candidate gate:** `OD7-G3-GF-C`
**Provisional PEC carrier:** `D-PEC-67`

## Exact candidate disposition

Defer selection and implementation of a daemon-wide global event feed. Keep
existing per-session SSE and file-native reconciliation. Keep PEC
`SOW-076` / `OI-002` open and non-reliance; P0–P2 remain unblocked as the
accepted PRD records.

This deferral expires at the earliest of:

1. activation of the P4 streams tranche that needs cross-session freshness;
2. accepted evidence that per-session consumption cannot satisfy `SOW-035`
   performance or coverage criteria; or
3. a proposed external client requiring daemon-wide observation.

At expiry, the owning loop must prepare a new exact decision candidate. This
deferral creates no endpoint, schema, storage, authorization, filtering,
replay, retention, cadence, or implementation requirement.

## Conditional write surfaces

- PEC decision record and register
- PEC open-item/coordination status surfaces that already carry
  `SOW-076` / `OI-002`
- a non-binding notice to Root only if the accepted record would otherwise
  leave Root expecting a generic-feed decision

No PRD, decomposition, ScopeOfWork, Root runtime, or implementation surface is
authorized by this candidate.
