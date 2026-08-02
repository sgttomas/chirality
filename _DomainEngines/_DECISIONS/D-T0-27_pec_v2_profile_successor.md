# D-T0-27 — PEC v2 Domain Engine Profile successor

**Status:** `AWAITING_RULING / CANDIDATE VALIDATED / LIVE PROFILE UNCHANGED`

**Date presented:** 2026-08-02

**Decision ID:** D-T0-27

**Candidate packet:**
`../bridge/PEC_V2_PROFILE_SUCCESSOR_D-T0-27_2026-08-02/PACKET.md`

**Exact candidate profile SHA-256:**
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`

## Named precedents

- `_DomainEngines/_DECISIONS/D-T0-12_pec_profile_lifecycle.md` owns the
  validator-evidence-to-owner-Gate-2 lifecycle for PEC profile adoption.
- D-PEC-11 in
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` is the
  project-local pointer-row precedent and creates no second adoption ruling.
- `_DomainEngines/_DECISIONS/D-T0-26_pec_profile_stale_demotion.md` is the live
  demotion and separately adopted PEC v2 successor requirement this row
  discharges only if ruled and effectively applied.

## Question

Adopt the exact newly authored PEC v2 profile at `READ_ONLY` as the separately
adopted successor required by D-T0-26, or keep the current frozen-v0.4 profile
`STALE / DENY_ALL`?

## Options

- **O-A — adopt now (recommended).** Owner Gate 2 approves the exact candidate
  and its application plan, effective only after exact application merge;
  D-PEC-76 is the local pointer row and no second ruling.
- **O-B — defer.** Keep the exact candidate as validated preparation; leave
  the live profile unchanged; keep both D-PEC-75 executable options held
  before source activation while allowing only separately owner-ruled bounded
  SOW-currency work.

## Recommendation

Recommend O-A. Accepted PEC v2 contract bytes support a narrow read-only
profile now. It declares no runtime or mutating operation, and adopting it
before adapter code avoids a deadline-driven boundary decision.

## Current authority fence

Until the owner rules and the application becomes effective, the live profile
remains SHA-256
`0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6`,
`STALE / MANUAL_BRIDGE / DENY_ALL_PROFILE_MEDIATED_INVOCATIONS`.

This presentation creates no adoption, live-profile edit, profile-mediated
invocation, PEC project/source/SOW/status/Task-Management change, lifecycle
act, release, professional reliance, or cross-loop mandate.

## Owner ruling

`TBD`
