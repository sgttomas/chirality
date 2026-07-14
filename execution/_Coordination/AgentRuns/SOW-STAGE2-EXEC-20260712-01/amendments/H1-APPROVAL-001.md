# H1 Approval — Piping DEL-01-01 Representation Replacement

Decision ID: `H1-APPROVAL-001`
Decision date: `2026-07-14`
Decision owner: Human
State: `APPROVED — PENDING GIT BINDING`

## Exact human ruling

> I APPROVE H1 for the exact DEL-01-01 representation replacement bound at
> commit 054ef5dd2de62f0803569573e162d613258b1b40.

The human also confirmed agreement with the governed pause because the
deliverable was `ISSUED`, and directed the goal to resume.

## Bound evidence and effect

The cited commit contains the accepted H1 evidence package at
`snapshots/I0/H1_EVIDENCE/`, with normalized manifest SHA-256
`4c9a71df041a37755cd0c291f3013130245b7d44156cc0bb558370c701394df2`,
and the independent RECON snapshot at normalized manifest SHA-256
`802656d604adcaed53bdfd6789a79d852da77dc252382387954f369fe603bc74`.

This ruling authorizes CHANGE to perform only the exact atomic five-row
representation replacement after fresh drift and required checks:

- add `ScopeOfWork.md` with SHA-256
  `23d92ddeb0cc4e3fe37694b1c8b79284017799cd08caaaad9767c8a4f0121f21`;
- remove the four exact bound legacy documents;
- preserve `_STATUS.md` byte-for-byte at SHA-256
  `e63b1797b30c291b2a4510cd521951fd2736675025f0e2d07b810e64617b28a8`;
- preserve lifecycle exactly as `ISSUED`.

The ruling does not authorize candidate regeneration, semantic modification,
reissue, reauthentication, lifecycle change, release, reliance, rollback,
legacy retirement, or H2. Any source/status/candidate/authority drift returns
to the governing workflow before integration.
