# OD6-G5 — APP-HOLD-1 Exact Release

Status: `AUTO-APPROVED AND APPLIED — GIT_CLOSEOUT_PENDING`

Prepared and applied: 2026-07-28

Decision record: `D-APP-81`

Source basis: `main@b0b673dc3d65a4cfff9a045fda6c1fefa060645c`

## Recommendation

Release the six APP-HOLD-1 targets now. The required post-merge proof passes:

- all 53 App contracts validate;
- all 51 decomposition-derived contracts declare the accepted terminal
  decomposition basis;
- both PKG-00 controls retain their existing README basis;
- every current contract basis resolves;
- all six formerly missing historical relations remain explicitly
  `HISTORICAL_RELATION_UNKNOWN`; and
- D-APP-80 is durable at PR #397 merge
  `b0b673dc3d65a4cfff9a045fda6c1fefa060645c`.

The canonical released representation is a header-only active hold register.
The live guard should preserve scan-authoritative detection of any future
unresolvable current basis, allow every released target through each formerly
prohibited operation and entry path, and reject any attempt to reactivate a
released target by register insertion alone.

## Exact candidate identity

- live-surface manifest: `LIVE_SURFACE_MANIFEST.csv`
- live-surface manifest SHA-256:
  `5d0dacdf790d63bb44a579382b56acd776547cbf46cac401adce9e585b92613d`
- exact release surfaces: 5
- released targets: 6
- active hold rows after application: 0

`POST_MERGE_PROOF.json` records the population proof.
`RELEASED_TARGETS.csv` carries the six historical-UNKNOWN records forward
without reconstruction. `CLOSEOUT_IDENTITY.csv` proves the D-APP-78,
D-APP-79, and D-APP-80 application/merge identities used by their additive
effective-state closeouts. The runnable `validate_hold_release.py` reproduces
all four artifacts.

## Canonical release behavior

1. Remove the six active rows from `APP_HOLD_REGISTER.csv`; retain the exact
   header as the canonical no-active-hold representation.
2. Preserve the six identities as a released set in the guard, so adding any
   one back to the active register without a later guard-and-authority change
   fails closed.
3. Preserve scan-authoritative discovery: a future scan-derived
   unresolvable target missing from the active register blocks.
4. Prove every released target is allowed for all four formerly prohibited
   operations across every tested entry path.
5. Preserve the absence of a generic exception or bypass argument.
6. Preserve the D-APP-80 historical evidence package byte-for-byte.

## Non-effects

This release does not:

- declare the six historical relations knowable;
- repin or edit any `ScopeOfWork.md`;
- change the App PRD, decomposition, invariant register, stable IDs,
  packages, deliverables, objectives, or lifecycle state;
- alter implementation, runtime, dependency, estimate, schedule, identity,
  version, compatibility, facade retirement, issuance, release, or
  professional-reliance state; or
- disable future scan-authoritative protection or authorize future
  reactivation.
