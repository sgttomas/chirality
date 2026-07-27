# D-APP-49 Audit Fan-In Validation

## Verdict

`PASS_WITH_RECORDED_LIMITATIONS`

The single admitted child return is byte-identical to the report selected
through Gate F1. It is accepted into this derivative package without repair.

## Identity and basis

| Check | Result |
|---|---|
| Return SHA-256 equals `18e0ca3f...` | `PASS` |
| Audit commit `fb16e32...` resolves | `PASS` |
| Audit tree equals `65f1ca55...` | `PASS` |
| Runtime lockfile hash reproduces from audit commit | `PASS` |
| App lockfile hash reproduces from audit commit | `PASS` |
| Selected Revision 3 packet hash equals `c6d7b3...` | `PASS` |
| Selected packet's internal hash list verifies | `PASS` |
| Current basis is exactly `c487b7dd5...` | `PASS` |
| SCA-APP-005 ancestry and D-APP-48/49 subject stability | `PASS` |
| Broader packet premise drift | `ONE PATH — PIPING DECOMP REVISION FIELD ONLY` |
| Governed recheck 02 brief identity | `PASS — ed247711d...` |
| Governed recheck 02 terminal verdict | `PASS — PRE-TERMINAL POPULATION` |
| Recheck 01 normalization disposition | `PASS — ORIGINAL SHA PRESERVED` |

## Return coverage

| Required coverage | Result |
|---|---|
| Accepted commit and tree | `PASS — REPRODUCED` |
| Disposable checkout path and clean final state | `PRESENT_IN_RETURN — NOT_INDEPENDENTLY_REPRODUCED` |
| Node/npm versions | `PRESENT_IN_RETURN — NOT_INDEPENDENTLY_REPRODUCED` |
| Both lockfile identities | `PASS — REPRODUCED_FROM_GIT_BASIS` |
| Root implementation and App facade carrier inventory | `PASS` |
| Install, build, focused test, typecheck, lint, and import-probe commands with exit states | `PRESENT_IN_RETURN — NOT_INDEPENDENTLY_REPRODUCED` |
| Initial network failure and stated approved retry | `PRESENT_IN_RETURN — APPROVAL_RECORD_NOT_PRESENT` |
| Initial typecheck ordering failure and successful full-build retry | `PRESENT_IN_RETURN — NOT_INDEPENDENTLY_REPRODUCED` |
| Dependency-audit warning | `PRESENT_IN_RETURN — NOT_INDEPENDENTLY_REPRODUCED` |
| Claim-by-claim supported/not-current/not-tested distinctions | `PASS` |
| Explicit ownership, lifecycle, retirement, release, and implementation limits | `PASS` |

## Evidence anchors

Every accepted repository path cited as a carrier or governing instrument
exists at the stated basis or the current accepted basis appropriate to its
claim. D-APP-76 is separately frozen and hashed as a companion owner-ruling
candidate outside the accepted Git basis; it becomes durable only on scoped
integration.
The two recorded implementation SHA-256 values independently reproduce and
match the original D-APP-49 landing bytes; admission does not reinterpret
their ownership.

## Recorded limitations

1. The original audit's contemporaneous brief, run manifest, author/instance
   identity, and parentage are `NOT_PRESENT`; engine/provider/model are
   `UNKNOWN / UNKNOWN / UNKNOWN`. The report is admitted as evidence, not as
   proof of a fully governed Agent 2 dispatch.
2. The admission validator's trustworthy engine/provider/model surface is
   also unavailable and recorded as `UNKNOWN / UNKNOWN / UNKNOWN`.
3. Admission does not rerun npm installs, builds, typechecks, tests, or import
   probes. Those outcomes and the clean final state remain return-attested.
4. The stated network-retry approval record is not present in the admission
   inputs.
5. The audit is focused, not the complete App premerge suite.
6. UI, daemon, PEC, Piping, persistence, protected-path behavior, and live
   runtime consumption were not exercised.
7. One high-severity dependency audit notice remains unresolved.
8. Direct Node import emitted the recorded
   `MODULE_TYPELESS_PACKAGE_JSON` warning.
9. External consumers and facade migration-cycle completion remain unknown.
10. Recheck 02's engine/provider/model fields were not exposed and remain
    `UNKNOWN / UNKNOWN / UNKNOWN`.

These limitations constrain the admitted finding rather than invalidating
the basis-scoped continuity evidence.

## Fan-in boundary

Fan-in supports closure only of OD6-011's pinned executable-continuity
evidence gap at `fb16e32...`, effective when scoped Git closeout integrates
the exact package and companion ruling. It does not close D-APP-49's
lifecycle, accept a successor, complete the migration cycle, retire the
facade, reconcile D-APP-48, change a version, authorize implementation, or
make a release claim.
