# D-APP-79 — OD6-G3-H0-A Repair-Validation Hold

Status: `RULED — GIT_CLOSEOUT_PENDING`

DecisionID: `D-APP-79`

Date: 2026-07-28

Owner: Ryan Tufts

Owning loop: Chirality App Dev

Source basis: `main@23b3b07d1122ae065affe69346c53bac78289a2e`

EffectiveCommit: `PENDING_GIT_CLOSEOUT`

## Question

Whether the six APP-HOLD-1 contracts remain blocked through the later
full-population contract repair and validation, with release requiring a
separate owner act, or whether repair and release occur atomically.

## Recommendation

Select H0-A. Install `REPAIR_VALIDATION_PENDING` before any contract edit or
repin. Keep every currently prohibited operation blocked through later basis
repair and validation. Release only through a separate exact owner act after
the repaired population passes its required concordance and validation.

This preserves an observable post-repin validation interval and avoids
equating a resolvable new basis with permission to rely on the repaired
contract.

## Owner direction and selection

The owner directed verbatim:

> "Finish out your plan now (attaining your goal) with self merge of PRs and auto approve for owners rulings, which should still be recorded in the usual manner with your recommendation standing as what I approved."

Under that direction, the recommendation above stands as the approved owner
selection: **H0-A**.

## Ruling

1. The six existing APP-HOLD-1 rows move from scan-derived `HELD` to
   `REPAIR_VALIDATION_PENDING`.
2. `REPAIR_VALIDATION_PENDING` is an active hold state. It blocks reliance,
   dispatch, `CHECKING` promotion, and accepted-dependency consumption for
   every entry path even when the contract's declared basis later resolves.
3. The execution-time scan remains authoritative for discovering additional
   unresolvable contracts. Every scan-derived held contract must appear in
   the active register; omission or register drift blocks the operation.
4. The six named rows retain `entry_path_scope=ANY` and the complete four-act
   prohibited-operation set.
5. The six rows retain `repin_posture=NO_REPIN` in this tranche. A later exact
   OD6 contract-repair candidate may propose the bounded repin posture, but
   only through a separately accepted App-loop amendment tied to that exact
   candidate.
6. A successful later repin or resolvable basis does not release any row.
   Release requires a separate exact owner act after repair validation.
7. D-APP-75 remains the founding APP-HOLD-1 authority. D-APP-79 is the
   prospective repair-state extension and authority basis for these six
   `REPAIR_VALIDATION_PENDING` rows.
8. The six missing historical relations remain
   `HISTORICAL_RELATION_UNKNOWN`. Prospective repair never reconstructs the
   missing historical object.
9. `DEL-00-01` and `DEL-00-02` remain PKG-00 controls outside the later
   decomposition repin population.

## Exact affected targets

- `DEL-02-01`
- `DEL-02-02`
- `DEL-02-04`
- `DEL-05-04`
- `DEL-08-02`
- `DEL-08-03`

## Validation contract

The live guard must prove:

- all six targets block every prohibited operation through every entry path;
- a registered `REPAIR_VALIDATION_PENDING` target still blocks when a
  simulated post-repin scan reports `CLEAR`;
- an unaffected clear target remains allowed;
- a scan-derived held target missing from the register blocks as drift;
- a stale scan-derived `HELD` row may not survive after its basis resolves;
- no generic owner, manager, session, agent, or workflow bypass exists; and
- the register, receipt, paths, and staged bytes pass their deterministic
  checks.

## Non-effects

This ruling does not:

- edit or repin any `ScopeOfWork.md`;
- authorize the later contract-repair candidate;
- release, weaken, or bypass APP-HOLD-1;
- infer historical provenance;
- change the terminal decomposition basis adopted by D-APP-78;
- change either PKG-00 control basis;
- amend the App PRD, decomposition, invariant register, or lifecycle state;
- authorize implementation, dependency, estimate, schedule, runtime,
  release, issuance, or professional reliance; or
- approve any later OD6 gate except the H0-A posture stated here.
