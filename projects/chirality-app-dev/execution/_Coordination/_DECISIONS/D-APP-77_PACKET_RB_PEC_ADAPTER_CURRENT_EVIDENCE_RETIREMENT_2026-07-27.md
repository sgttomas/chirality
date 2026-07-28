# D-APP-77 Packet — RB-PEC-ADAPTER Current-Evidence Retirement

**Status:** PROPOSAL — exact application requires a later owner ruling
**Date:** 2026-07-27
**Decision ID:** D-APP-77
**Owner:** Ryan Tufts
**Owning loop:** Chirality App Dev
**Basis:** `9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2`
**Method:** DEL-01-02 maintenance through `WORKING_ITEMS`; no App `SCOPE_CHANGE`

## Question

Whether to apply the exact G4-A maintenance candidate that preserves the
stable `RB-PEC-ADAPTER` row as history while retiring its v0.4
adapter-service, RBAC, scratch/demo, and pilot content as current PEC v2
enforcement evidence.

## Prior owner selection

Provenance: Ryan Tufts, in-session owner direction, 2026-07-27.

> SELECT OD7-G4 G4-A.

This selection authorizes preparation of this exact candidate. It does not
authorize application, Git closeout, App or PEC scope change, implementation,
repinning, lifecycle transition, or release.

## Proposed exact effect

If separately approved by the owner, the application:

1. preserves `RB-PEC-ADAPTER` as a stable historical row;
2. marks its SCA-APP-003/v0.4 enforcement and pilot assertions retired for
   current PEC v2 reliance;
3. cites the one-daemon boundary to Root `D-GOV-20` and the surviving
   no-dual-loop and human-only-act restrictions to PEC PRD v2 §15;
4. states that PEC v2 adapter shape, enforcement mechanism, pilot, and closure
   evidence remain `UNKNOWN`;
5. requires a governed PEC `DEL-07-05` ScopeOfWork and accepted evidence before
   any new current-enforcement claim;
6. updates the existing DEL-01-02 test to reject recurrence of the obsolete
   wording;
7. aligns DEL-01-02 `Remaining` without changing its `IN_PROGRESS` lifecycle
   state; and
8. routes a coordination-only notice to PEC.

## Scope fence

This candidate does not:

- amend App or PEC PRD, decomposition, ScopeOfWork, dependency, or objective;
- assert a current PEC v2 adapter service, RBAC mechanism, pilot, or proof;
- change PEC optionality, authority, profile, or lifecycle;
- change App implementation or runtime behavior;
- repin any contract;
- grant generic runtime any PEC authority;
- authorize release, publication, issuance, or professional reliance; or
- authorize Git closeout.

## Validation implications

The application gate requires:

- exact candidate hash verification;
- one and only one `RB-PEC-ADAPTER` row;
- the row contains `RETIRED current-evidence row`, the no-current-enforcement
  statement, and `UNKNOWN`;
- the obsolete enforcement phrase is absent from that row;
- the D-GOV-20 and PEC PRD citations resolve at the accepted basis;
- the focused Vitest passes;
- the complete App frontend test suite is rerun or explicitly held for the
  separately governed application stage;
- `git diff --check` and exact write-containment pass; and
- PEC notice delivery is recorded, with acknowledgment tracked but not a
  condition of App closeout.

## Owner gate

Approval must identify the exact candidate-set manifest SHA-256. The later
ruling record must transcribe that approval verbatim. No application occurs
from this packet alone.
