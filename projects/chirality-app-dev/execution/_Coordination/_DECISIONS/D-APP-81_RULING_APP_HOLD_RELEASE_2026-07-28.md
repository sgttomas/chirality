# D-APP-81 — APP-HOLD-1 Exact Release

Status: `RULED — GIT_CLOSEOUT_PENDING`

DecisionID: `D-APP-81`

Date: 2026-07-28

Owner: Ryan Tufts

Owning loop: Chirality App Dev

Source basis: `main@b0b673dc3d65a4cfff9a045fda6c1fefa060645c`

EffectiveCommit: `PENDING_GIT_CLOSEOUT`

## Question

Whether the six APP-HOLD-1 targets may leave
`REPAIR_VALIDATION_PENDING` after the accepted D-APP-80 repair is durable and
the required post-merge population, basis, schema, historical-relation, and
guard proofs pass.

## Recommendation

Approve the exact five-surface release candidate identified by live-surface
manifest SHA-256
`5d0dacdf790d63bb44a579382b56acd776547cbf46cac401adce9e585b92613d`.
The repair is complete, every current basis resolves, and the six historical
UNKNOWN records remain preserved. Continuing to block the repaired
contracts would no longer protect an unresolved current reliance basis.

## Owner direction and selection

The owner directed verbatim:

> "Finish out your plan now (attaining your goal) with self merge of PRs and auto approve for owners rulings, which should still be recorded in the usual manner with your recommendation standing as what I approved."

Under that direction, the recommendation above stands as the approved owner
selection.

## Ruling

1. Release exactly `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-05-04`,
   `DEL-08-02`, and `DEL-08-03` from APP-HOLD-1.
2. The canonical released representation is absence from the active hold
   register. `APP_HOLD_REGISTER.csv` becomes header-only.
3. The guard records those six identities as released and rejects active
   register reinsertion unless a later separately accepted authority-and-tool
   change supersedes this ruling.
4. The six targets are allowed for reliance, dispatch, `CHECKING` promotion,
   and accepted-dependency consumption through every entry path, subject to
   all other ordinary project gates.
5. Scan-authoritative discovery remains active. Any future unresolvable
   current contract basis missing from the active register fails closed.
6. The six historical relations remain
   `HISTORICAL_RELATION_UNKNOWN`; release and prospective basis resolution do
   not reconstruct the missing historical object.
7. The D-APP-80 historical-evidence package remains unchanged.

## Exact accepted candidate

- candidate:
  `execution/_Coordination/_PROPOSALS/OD6-G5_APP_HOLD_RELEASE_2026-07-28/CANDIDATE.md`
- live-surface manifest:
  `execution/_Coordination/_PROPOSALS/OD6-G5_APP_HOLD_RELEASE_2026-07-28/LIVE_SURFACE_MANIFEST.csv`
- accepted manifest SHA-256:
  `5d0dacdf790d63bb44a579382b56acd776547cbf46cac401adce9e585b92613d`

## Non-effects

This ruling does not:

- infer historical provenance;
- edit or repin any contract;
- change App scope, decomposition, invariant coverage, topology, lifecycle,
  implementation, runtime, identity, version, compatibility, facade
  retirement, issuance, release, or professional reliance; or
- authorize a generic hold bypass, future reactivation, or another OD6 gate.
