# DEL-09-04 exact-merge R16 staging — orchestration plan v1

Status: `FROZEN BEFORE DISPATCH`

## Activation

- RunID: `APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22`
- ManagerInstanceID: `WI-PKG09-R16-STAGING-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r16-staging`
- Exact accepted basis / HEAD / origin/main:
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- Selection authority: explicit owner direction transcribed in this run root
- Pattern: serialized executor, manager fan-in, fresh evidence-only reviewer
- Lifecycle: `IN_PROGRESS`; login-session proof remains unproved

## Objective

Rebuild the local unsigned arm64 app from the exact merged repair commit, bind
all package and read-only preflight evidence to that commit, author a new R16
from scratch with a complete concrete owner procedure, and minimally update
DEL-09-04 status. Prior temporary R16/build material is quarantined and must
not be read, copied, cited for identity, or adopted.

## Work graph

1. `A2-PKG09-R16-EXECUTE-01`: exact package build, package/preflight checks,
   new R16/status, and unique executor evidence.
2. `A2-PKG09-R16-REVIEW-01`: fresh full evidence-only review after executor
   return and manager fan-in; review record only.
3. `WI-PKG09-R16-STAGING-01`: after review PASS only, validate that the exact
   authorized recovery target resolves to the explicit narrow path and remove
   it. No child owns deletion.

Edge: `EXECUTE-01 -> manager fan-in -> REVIEW-01 -> manager target validation
and removal -> closeout`.

At most two bounded repair plus fresh-review cycles are permitted. Shared
R16/status writes are serialized.

## Fan-in gates

- Exact tracked `npm run desktop:pack` exits zero and its complete log proves
  embedded dependency-boundary and instruction-root checks pass.
- App, bundle metadata, thin arm64 executable, exact executable hash,
  ad-hoc/linker-only/no-team posture, and packaged CLI presence/readability are
  independently recorded.
- Frontend commit-to-HEAD diff and scoped porcelain are empty after build.
- Proposed root/plist/exact proof job are absent; optionless preflight passes
  read-only and creates no root.
- New R16 discloses the earlier approximately 12:50 prior-authorized local
  rebuild and superseded material as unadopted and superseded, without copying
  or adopting any bytes or claims from it.
- R16's independently copy-pasteable Step 0 through handoff blocks use exact
  current values and fail closed. No GUI/manual-open, bootstrap/kickstart, or
  continue-after-error path is permitted.
- Status remains `IN_PROGRESS` and unproved; all release/operator fences hold.
- Fresh review re-runs package, preflight, procedure, hash, status,
  containment, and whitespace checks and returns PASS with no findings.
- Only after PASS is the exact authorized temp recovery root removed.

## Hard fences

No reading/adopting prior temp R16/build material; no GUI/app launch, proof
prepare/capture, logout/login, root creation, bootstrap/kickstart, default
operator job/plist/launcher query or mutation, signing, notarization,
deployment, release/distribution/publication/reliance claim, provider or
dependency expansion, stage, commit, push, PR, merge, receipt, or lifecycle
acceptance. All repository writes stay under `projects/chirality-app-dev/`.
