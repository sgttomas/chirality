# D-APP-80 — OD6-G4 Complete Contract Concordance and One-Time Repin

Status: `RULED — GIT_CLOSEOUT_PENDING`

DecisionID: `D-APP-80`

Date: 2026-07-28

Owner: Ryan Tufts

Owning loop: Chirality App Dev

Source basis: `main@deb01644e324af2b39cff7b52abae43784cd071b`

EffectiveCommit: `PENDING_GIT_CLOSEOUT`

## Question

Whether to apply the complete 53-contract concordance recommended after
D-APP-78 and D-APP-79: one-time repin of the 51 decomposition-derived
contracts, preservation of the two PKG-00 controls and six unknown historical
relations, exact reconciliation of the seven SCA-APP-006 downstream
contracts, and validation while every current hold remains active.

## Recommendation

Approve the exact candidate identified by live-surface manifest SHA-256
`6507828512e247f4cd96c1b2ae84cf72c7b1c1973bd2b69dfb21ef32206c7218`.
It performs the complete contract repair once, retains the post-repin
validation interval, and grants neither hold release nor another repin.

## Owner direction and selection

The owner directed verbatim:

> "Finish out your plan now (attaining your goal) with self merge of PRs and auto approve for owners rulings, which should still be recorded in the usual manner with your recommendation standing as what I approved."

Under that direction, the recommendation above stands as the approved owner
selection.

## Ruling

1. The execution-time population scan governs and must resolve exactly 53
   contracts at application.
2. The exact 51 decomposition-derived contracts identified in
   `CONTRACT_CONCORDANCE.csv` are repinned once to
   `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca`.
3. `DEL-00-01` and `DEL-00-02` remain PKG-00 controls on their existing
   README basis.
4. The seven named SCA-APP-006 downstream contracts are reconciled to their
   accepted `_CONTEXT.md` scope relations and recorded boundary meanings.
5. The six missing historical relations remain
   `HISTORICAL_RELATION_UNKNOWN`. Their prospective current basis is repaired
   without claiming or reconstructing the missing historical object.
6. The six targets remain `REPAIR_VALIDATION_PENDING` and blocked for
   reliance, dispatch, `CHECKING` promotion, and accepted-dependency
   consumption through every entry path.
7. The APP-HOLD guard must fail closed if any of those six repair-pending
   register rows disappears after current-basis resolution. Scan-authoritative
   discovery of any additional unresolvable contract remains in force.
8. D-APP-80 is a one-time exact repin authority for the 56-surface manifest.
   The final six register rows retain `NO_REPIN`, and no further repin or
   exception is authorized.
9. Hold release remains a later, separate exact owner act after this
   application's validation and durable Git closeout.

## Exact accepted candidate

- candidate:
  `execution/_Coordination/_PROPOSALS/OD6-G4_APP_CONTRACT_CONCORDANCE_2026-07-28/CANDIDATE.md`
- live-surface manifest:
  `execution/_Coordination/_PROPOSALS/OD6-G4_APP_CONTRACT_CONCORDANCE_2026-07-28/LIVE_SURFACE_MANIFEST.csv`
- accepted manifest SHA-256:
  `6507828512e247f4cd96c1b2ae84cf72c7b1c1973bd2b69dfb21ef32206c7218`

## Non-effects

This ruling does not:

- release, weaken, or bypass APP-HOLD-1;
- infer historical provenance;
- change the App PRD, decomposition, invariant register, stable IDs,
  packages, deliverables, objectives, or lifecycle state;
- repin either PKG-00 control;
- authorize implementation, runtime, dependency, estimate, schedule,
  identity, version, compatibility, facade retirement, issuance, release, or
  professional reliance; or
- approve a later hold transition or any other OD6 gate.
