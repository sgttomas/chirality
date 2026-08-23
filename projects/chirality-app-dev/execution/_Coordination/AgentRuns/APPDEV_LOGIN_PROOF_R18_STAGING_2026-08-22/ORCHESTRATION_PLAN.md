# DEL-09-04 exact-merge R18 staging — orchestration plan v1

Status: `FROZEN BEFORE DISPATCH`

## Activation

- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ManagerInstanceID: `WI-PKG09-R18-STAGING-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r18-staging`
- Accepted basis / HEAD / origin/main:
  `166efa82748133e90674be62304b81f8a0a8c1b4`
- Selection authority: explicit owner direction in `CHAT_TRANSCRIPTION.md`
- Posture: serialized executor, manager fan-in, fresh evidence-only reviewer
- Lifecycle: `IN_PROGRESS`; login-session proof remains unproved

## Objective

Overwrite the ignored R16 package with one exact-merge, cache-only unsigned
arm64 package; prove package and R17 socket-guard identity; stage a new R18
owner procedure without executing any proof act; and minimally update DEL-09-04
status while retaining every operator and release fence.

## Work graph

1. `A2-PKG09-R18-EXECUTE-01`: sole write owner for ignored package output,
   R18, minimal status, and unique executor evidence.
2. `WI-PKG09-R18-STAGING-01`: validate executor fan-in, freeze all remaining
   non-review run bytes, and create the reviewer brief.
3. `A2-PKG09-R18-REVIEW-01`: fresh evidence-only review; review record only.

Edge: `EXECUTE-01 -> manager fan-in/freeze -> REVIEW-01 -> closeout`.
At most two repair plus fresh-review cycles are permitted. R18/status writes
are serialized to the executor integration owner.

## Concrete staging identities

- App:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- Revision: `166efa82748133e90674be62304b81f8a0a8c1b4`
- Root: `/private/tmp/ch-r18-91499728-51dd`
- Label:
  `com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4`
- Plist:
  `/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4.plist`
- Service:
  `gui/501/com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4`
- Proposed public evidence:
  `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r18-1f16d830-4fd0-4647-a01b-a746e8a22cb4-public-evidence`

Manager pre-dispatch read-only checks found the root/plist/public destination
absent and the exact service unloaded with launchctl exit 113 and the expected
two-line not-found text. Children must re-prove these claims independently.

## Fan-in gates

- Exact `npm run desktop:pack` runs in the frontend under the restricted
  network sandbox, exits zero from the local cache, and preserves a full log.
  Any cache miss or network attempt is a terminal node failure; no escalation.
- Embedded dependency-boundary and current-byte instruction-root checks pass.
- Exact app metadata, thin arm64 executable, ad-hoc/no-team signature posture,
  main and packaged runtime-cli hashes, and packaged R17 guard evidence exist.
- Exact build revision remains HEAD; frontend revision diff and scoped
  porcelain remain empty after the ignored build.
- Root/plist/public destination remain absent, exact service remains unloaded,
  and optionless preflight passes without mutation.
- R18 provides independently copy-pasteable fresh-Terminal blocks with all
  exact identities, 67/103-byte guard, fail-closed gates, three-file-only
  preservation, hashes, and no-proof-acceptance handoff.
- Status remains `IN_PROGRESS` and unproved; no proof or forbidden act occurs.
- Proportional registered checks, containment, candidate whitespace, and fresh
  evidence-only review all pass.

## Hard fences

No Desktop R16 failed-evidence or private R16 proof-root read/traversal; no
network or cache retrieval; no GUI launch, prepare, capture, logout/login,
bootstrap, kickstart, operator/default job/plist/launcher query or mutation,
proof root/plist/job/public-directory creation, signing, notarization,
deployment, distribution, publication, release-readiness or proof-acceptance
claim, provider/dependency expansion, receipt, stage, commit, push, PR, or
merge. Repository writes stay under `projects/chirality-app-dev/`.
