# DEL-10-01 Final Acceptance Ruling

**Decision:** D-PEC-72 final DEL-10-01 Gate 5 and AC-008 ruling
**Status:** RULED
**Owner:** Ryan Tufts
**Date:** 2026-08-01

## Owner ruling (verbatim)

> APPROVE:
>
> 1. DEL-10-01 Gate 5 — APPROVE.
>
> Advance DEL-10-01 from INITIALIZED to CHECKING under the
> previously recorded review-from-INITIALIZED owner override.
>
> The final SELF_CHECK populated all eight deterministic criteria,
> RF-001 is REVISE / RESOLVED, and no finding remains open.
>
> This is a lifecycle act only. It does not accept the method or
> baseline artifacts, satisfy AC-008, close C-05, or authorize P1.
>
> 2. DEL-10-01 AC-008 — ACCEPT.
>
> I accept artifacts/STEP0_COST_BASELINE_METHOD.md at SHA-256
> 5756d6cf1b7293a7db8dcf1ce968d443dcb7214867216f5013ee018a493a0c59
> and artifacts/STEP0_COST_BASELINE.md at SHA-256
> 0aa5dd22d397026d88dfd8af1613163dd2de01ef3264024438034e54a1f5d02d
> as fit for DEL-10-01.
>
> I confirm that the captured exact baseline is fit to serve as the
> “before” leg of PRD §11 metric 1 and that the PRE_P1_OBLIGATION
> was satisfied before any P1 node started.
>
> The bound telemetry evidence remains SHA-256
> baa80859d40845cc1c2448342befcacc83fd3519dd34e9e9b00dceb6764f7f89.
>
> This accepts these artifact bytes and satisfies AC-008 only.
> It does not independently change lifecycle state, close C-05,
> or authorize P1.

## Recorded effects and fences

1. Gate 5 is approved. `DEL-10-01` advances from `INITIALIZED` to
   `CHECKING` under the previously recorded review-from-`INITIALIZED` owner
   override. This is a lifecycle act only.
2. AC-008 accepts only these exact artifact bytes as the PRD §11 metric 1
   “before” leg:
   - `artifacts/STEP0_COST_BASELINE_METHOD.md` —
     `sha256:5756d6cf1b7293a7db8dcf1ce968d443dcb7214867216f5013ee018a493a0c59`
   - `artifacts/STEP0_COST_BASELINE.md` —
     `sha256:0aa5dd22d397026d88dfd8af1613163dd2de01ef3264024438034e54a1f5d02d`
3. The owner confirms that `PRE_P1_OBLIGATION` was satisfied before any P1
   node started. The bound telemetry evidence remains
   `sha256:baa80859d40845cc1c2448342befcacc83fd3519dd34e9e9b00dceb6764f7f89`.
4. The AC-008 acceptance does not independently change lifecycle state.
   Neither act closes C-05 or authorizes P1.
