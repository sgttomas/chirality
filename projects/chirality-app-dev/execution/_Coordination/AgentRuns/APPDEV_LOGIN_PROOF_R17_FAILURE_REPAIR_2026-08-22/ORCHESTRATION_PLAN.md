# ORCHESTRATION PLAN — DEL-09-04 R17 failure repair

- RunID: `APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22`
- InstanceID: `WI-PKG09-R17-FAILURE-REPAIR-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r17-repair`
- Exact basis: `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Posture: serialized implementation then evidence-only review
- Selection authority: explicit owner direction transcribed in this run root
- Software profile: `projects/chirality-app-dev/software-workflow.json`
- Maximum repair cycles after review: two

## Graph

`N1_MANAGER_PREFLIGHT -> N2_SINGLE_WRITE_OWNER -> N3_MANAGER_FAN_IN -> N4_FRESH_REVIEW`

N2 is the sole write owner for both frontend source/test surfaces and the R17
record/status surfaces. N4 is read-only over N2's frozen candidate except for
its own review return. No Agent 2 may delegate.

## Gates

- R17 is immutable failed-proof evidence and may never be upgraded to PASS.
- Owner facts and independent observations must remain explicitly separated.
- Private proof-root contents and private log bodies may not be copied into the
  repository. The root is not touched or cleaned.
- No build, package, network, R18 execution/staging, prepare, capture,
  logout/login, bootstrap, kickstart, LaunchAgent/plist/operator/launcher
  mutation, signing, notarization, deployment, distribution, release claim,
  staging, commit, push, PR, or merge.
- The exact proof label and plist may be checked read-only; the default
  operator job/plist/launcher may not be queried or touched.
- Acceptance requires all prescribed checks, App-only containment, empty
  index, complete runtime telemetry, and fresh review PASS.

## Proposed future R18 root — evidence only

`/private/tmp/ch-r18-91499728-51dd`

The 33-byte root is absent and not a symlink. It is proposed only. Its exact
future control-socket path is 67 UTF-8 bytes, leaving a 36-byte safety margin
below the 103-byte maximum. This run does not create the root, stage an R18
procedure, or authorize any proof action.
