# D-GOV-16 Stage-2 Census Refresh

Status: `PASS — SYNCHRONIZED-MAIN CENSUS UNCHANGED`
Observed date: 2026-07-12
Observed basis: `main@c9af689118e4e87f329e1ab4c6e71fea331b2674`

## Basis synchronization

The planning branch was created directly from the synchronized basis. Read-only
inspection returned the same object for all four required identities:

| Identity | Commit |
|---|---|
| planning `HEAD` | `c9af689118e4e87f329e1ab4c6e71fea331b2674` |
| local `main` | `c9af689118e4e87f329e1ab4c6e71fea331b2674` |
| local `origin/main` | `c9af689118e4e87f329e1ab4c6e71fea331b2674` |
| remote `refs/heads/main` | `c9af689118e4e87f329e1ab4c6e71fea331b2674` |

The remote value was obtained with `git ls-remote origin refs/heads/main`.
D-GOV-16 ruling commit `7584718aa32b112e415331736d1a8e68c12ac176`
is an ancestor of the observed basis. Proposal commit
`31e5efd985db4cc7b25543e11a65933979e07e4f` and the ruling commit both resolve
as Git commits.

The ruled artifact checks also pass:

| Artifact/check | Observed result |
|---|---|
| successor standard | SHA-256 `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` |
| `TYPES.proposed.patch` | SHA-256 `9614166c7db8340532d838768be2de52567862757fe0d5add3d3a90edea9d4b4`; `git apply --unidiff-zero --check` PASS |
| `SPEC.proposed.patch` | SHA-256 `543200af8a617e2f5673db110eef2b0a5cf742c54e70ccda8bce0cad870d4b2e`; `git apply --unidiff-zero --check` PASS |
| Stage-2 evidence index | SHA-256 `8a6e48ac8247fe5147afb4208d3e7c0b4f48cb1071b1e086b4f24a2ceeded806` |

## Reproduction procedure

The census uses the D-GOV-15 tracked-tree membership rule, not unrestricted
filesystem discovery:

```sh
git ls-files \
  'projects/chirality-app-dev/execution/**/1_Working/DEL-*/Datasheet.md' \
  'projects/chirality-piping/execution/**/1_Working/DEL-*/Datasheet.md' \
  | sed 's#/Datasheet.md$##' | LC_ALL=C sort
```

Hash the exact newline-terminated output above with `sha256sum`. For every
selected directory, check `Specification.md`, `Guidance.md`, `Procedure.md`,
and `_STATUS.md`. Read the first `**Current State:**` assertion from the
tracked `_STATUS.md`. Pilot membership is the exact App Dev PKG-07 and Piping
PKG-13 prefixes ruled in D-GOV-15. No working-tree-only path participates.

## Result

| Project | Deliverables | Datasheet | Specification | Guidance | Procedure | `ScopeOfWork.md` | Lifecycle |
|---|---:|---:|---:|---:|---:|---:|---|
| `chirality-app-dev` | 53 | 53 | 53 | 53 | 53 | 0 | 53 `IN_PROGRESS` |
| `chirality-piping` | 101 | 101 | 101 | 101 | 101 | 0 | 100 `IN_PROGRESS`; 1 `ISSUED` |
| **Total** | **154** | **154** | **154** | **154** | **154** | **0** | **153 `IN_PROGRESS`; 1 `ISSUED`** |

All 154 selected directories have all four production files and `_STATUS.md`;
`missing_companions=0`. The sorted directory-list SHA-256 remains:

```text
b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31
```

This exactly matches D-GOV-16 item 5. There is no membership or lifecycle
population delta and no accepted dual-format state on synchronized `main`.

The sole `ISSUED` member remains:

```text
projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-01_Project governance baseline
```

## Package topology and wave sizing

| Project/package | Members | Pilot | Ordinary remaining | ISSUED isolated |
|---|---:|---:|---:|---:|
| App PKG-00 | 2 | 0 | 2 | 0 |
| App PKG-01 | 4 | 0 | 4 | 0 |
| App PKG-02 | 5 | 0 | 5 | 0 |
| App PKG-03 | 4 | 0 | 4 | 0 |
| App PKG-04 | 5 | 0 | 5 | 0 |
| App PKG-05 | 5 | 0 | 5 | 0 |
| App PKG-06 | 6 | 0 | 6 | 0 |
| App PKG-07 | 6 | 6 | 0 | 0 |
| App PKG-08 | 5 | 0 | 5 | 0 |
| App PKG-09 | 6 | 0 | 6 | 0 |
| App PKG-10 | 5 | 0 | 5 | 0 |
| Piping PKG-00 | 8 | 0 | 8 | 0 |
| Piping PKG-01 | 4 | 0 | 3 | 1 |
| Piping PKG-02 | 5 | 0 | 5 | 0 |
| Piping PKG-03 | 8 | 0 | 8 | 0 |
| Piping PKG-04 | 6 | 0 | 6 | 0 |
| Piping PKG-05 | 5 | 0 | 5 | 0 |
| Piping PKG-06 | 5 | 0 | 5 | 0 |
| Piping PKG-07 | 8 | 0 | 8 | 0 |
| Piping PKG-08 | 6 | 0 | 6 | 0 |
| Piping PKG-09 | 5 | 0 | 5 | 0 |
| Piping PKG-10 | 5 | 0 | 5 | 0 |
| Piping PKG-11 | 5 | 0 | 5 | 0 |
| Piping PKG-12 | 5 | 0 | 5 | 0 |
| Piping PKG-13 | 4 | 4 | 0 | 0 |
| Piping PKG-14 | 5 | 0 | 5 | 0 |
| Piping PKG-15 | 4 | 0 | 4 | 0 |
| Piping PKG-16 | 4 | 0 | 4 | 0 |
| Piping PKG-17 | 9 | 0 | 9 | 0 |
| **Total** | **154** | **10** | **143** | **1** |

Thus the ruled arithmetic is unchanged: ten verified pilots plus 144
remaining members, of which 143 are ordinary `IN_PROGRESS` conversions and one
is the separately governed `ISSUED` representation replacement.

## Pilot membership

The exact pilot members remain App `DEL-07-01` through `DEL-07-06` and Piping
`DEL-13-01` through `DEL-13-04`. Their derivative Stage-1 sources remain:

- App candidate commit `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`;
- Piping candidate commit `31c35ea9798c29cd0af16b7089186f3942dcfcb1`;
- inventory
  `execution/_Coordination/AgentRuns/SOW-STAGE1-20260712/instances/RECON-FANIN/evidence/DELIVERABLE_INVENTORY.json`.

The candidates are evidence inputs only. Their dual-format branches must not
be merged.

## Execution-time rerun rule

Before the first Stage-2 child dispatch, ORCHESTRATOR must reproduce this
census from the then-synchronized execution basis and freeze a manifest with
path, project, package, deliverable ID, four source hashes, `_STATUS.md` hash,
lifecycle, pilot flag, and ISSUED flag. Any membership, lifecycle-population,
companion, candidate-hash, or active-caller delta is a decision request. It is
not authority to expand or silently reclassify scope.
