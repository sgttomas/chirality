# SCA-003 PRD application — public-export disposition

Date: `2026-08-03`
Node: `ROOT_FOUR_LANES_2026-08-02 / H3`
Disposition: `DEFERRED — REGENERATION REQUIRED AT NEXT AUTHORIZED EXPORT RELEASE`

## Accepted upstream basis

- owner ruling:
  `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/OWNER_RULING_2026-08-03_S2_APPLY_PI_G1B.md`,
  SHA-256
  `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`;
- applied Root PRD before SHA-256:
  `278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c`;
- applied Root PRD after/candidate SHA-256:
  `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`.

## Derivative observation and disposition

The existing public-export profile includes root `docs/`, so
`docs/PRD_ROOT.md` is export-eligible under the unchanged allowlist. At H3
application time:

- `exports/chirality-app/export-manifest.csv` SHA-256 is
  `079736ce89ab4e3143b91486974eff76336879d8297a04aedd229ceb680b4249`;
- its `docs/PRD_ROOT.md` row still records size `86643` and the pre-application
  SHA-256
  `278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c`;
- `exports/chirality-app/export-report.md` SHA-256 is
  `970753c1a38bbb8036301309e12efea079b44de91d4d7c6e2879e396cff576ef`;
- no `exports/chirality-app/staging/docs/PRD_ROOT.md` file is present.

H3 does not regenerate or publish these derivatives because its owner ruling
authorizes no public-export release act. The next separately authorized
export release must regenerate the staging tree, export manifest, and report
from the accepted integrated state and validate the unchanged boundary before
publication. Until then these derivative bytes are stale and must not be
treated as a substitute for the applied Root PRD.

## Effect limits

This deferral changes no public-export authority, allowlist membership,
boundary, release, lifecycle, reliance, decomposition, register, or Git state.
It is explicit derivative-package handoff evidence, not an export or release
act.
