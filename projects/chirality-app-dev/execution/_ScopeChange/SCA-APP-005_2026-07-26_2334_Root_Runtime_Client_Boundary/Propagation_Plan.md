# SCA-APP-005 Propagation Plan — Revision 2

**Gate:** 4
**Status:** `APPROVED_AND_APPLIED`
**Date:** 2026-07-27

## Direct writes

1. Authoritative decomposition:
   `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
2. Twenty-five `_CONTEXT.md` metadata files under PKG-03, PKG-04, PKG-05,
   PKG-06, and PKG-08.
3. This immutable SCA snapshot and
   `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md`.
4. One immutable post-change AUDIT_DECOMP package and the App
   DecompCoverage `_LATEST.md`.
5. Three factual coordination notices: Root, Tier-0, and PEC.

## Explicitly unchanged

- ScopeOfWork contracts, statuses, dependencies, accepted-basis pins, and
  repins.
- App and Root PRDs, authority corpora, D-APP-48/49, APP-HOLD-1, and
  compatibility-retirement state.
- Runtime, daemon, client, frontend, adapter, credential, event-store,
  packaging, test, and semantic-parity implementation.
- Piping state or notice.
- Every stable ID, mapping, type, context envelope, lifecycle state,
  dependency fact, estimate, and schedule.

## Notice semantics

Root, Tier-0, and PEC notices are coordination only. They confer no authority,
require receiving-loop disposition under that loop's own instruments, and do
not make acknowledgment a condition of App SCA closure.

## Downstream state

Contract/basis repair, D-APP-48/49 evidence, population repinning,
implementation, method reform, and semantic parity remain separately governed
and frozen. SCA-APP-005 closes scope change only.

## Rollback

Before Git closeout, rollback is the exact inverse of the enumerated
decomposition/context/pointer/notice changes. After Git closeout, CHANGE and
Git history own any reversal. No hidden compatibility or migration operation
is part of this amendment.
