# P3_MANIFEST B1 Basis

Status: `CANDIDATE — AWAITING RECON-B1`
Observed: `2026-07-13` (America/Edmonton)
Source basis: `main@9349594530dc19e55baf9c2ef0b7eb4716f48a17`

## Accepted upstreams

- D-GOV-16 ruling `7584718aa32b112e415331736d1a8e68c12ac176`.
- Accepted Stage-2 plan and B1 node contract.
- `P0_BASIS` accepted derivative census/caller freeze.
- `P2_CONSUMERS` C2F-R2 PASS and C2G postmerge handoff.
- Synchronized local `main`, `origin/main`, and remote main at the source basis.
- H1 and H2 remain unapproved.

## Reproduced basis

Local main, `origin/main`, and remote `refs/heads/main` are equal with divergence
`0/0`. The tracked deliverable census is exactly 154 members: App 53 and Piping
101. Every member has the four legacy sources and `_STATUS.md`; no member has
`ScopeOfWork.md`. Lifecycle truth is 153 `IN_PROGRESS` plus the sole `ISSUED`
Piping `DEL-01-01`. The accepted ten-pilot/144-remaining partition and sorted
path digest `b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31`
reproduce exactly.

`EXECUTION_MANIFEST.tsv` is a fresh hash census. `ROW_COMPARISON.tsv` compares
all twelve fields for all 154 rows and reports no delta. This package is
derivative evidence; it does not replace canon, decomposition truth,
deliverable truth, lifecycle truth, or human acceptance.
