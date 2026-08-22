# DEL-09-04 macOS 26 login-proof detector repair — orchestration plan v1

Status: `FROZEN BEFORE DISPATCH`

## Activation

- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- Parent: `HELP_HUMAN`
- Manager: `WORKING_ITEMS`
- Instance: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-macos26-repair`
- Accepted basis: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Selection authority: explicit owner authorization transcribed in this root
- Pattern: serialized implementation then fresh evidence-only review
- Deliverable representation: `SOW_V1`; lifecycle remains `IN_PROGRESS`

## Objective

Record the owner-reported macOS 26.6.2 Terminal failure before preparation,
replace the obsolete JXA/CoreGraphics login identity probe with a fail-closed
read-only detector based on `/dev/console` metadata and the top-level
`launchctl print gui/<uid>` domain, add comprehensive regression tests, and
prove the detector succeeds read-only on this live host.

This tranche stops after repaired source/tests/live preflight and fresh review.
It does not rebuild the app, execute proof preparation/capture, or create an
executable new proof revision.

## Work graph

1. `A2-PKG09-MACOS26-IMPLEMENT-01` — bounded Agent 2 implementation owner.
   Owns the two frontend paths, DEL-09-04 R14/R15 and status amendment, and its
   unique executor evidence. Runs focused/full tests, typecheck, syntax,
   read-only live preflight, APP-HOLD, and self-check as authorized.
2. `A2-PKG09-MACOS26-REVIEW-01` — fresh read-only Agent 2 reviewer over 100%
   of the frozen diff and live-preflight evidence. No repair authority.

Edge: `IMPLEMENT-01 -> manager fan-in -> REVIEW-01`. On review failure, the
manager may run at most two bounded repair plus fresh-review cycles.

## Hard fences

No `desktop:pack`, build, GUI launch, prepare, capture, logout/login,
LaunchAgents access or mutation, bootstrap, kickstart, operator job/launcher
access or mutation, deployment, signing, notarization, distribution,
publication, lifecycle acceptance, release-readiness or issuance claim,
provider expansion, staging, commit, push, PR, receipt, or merge.

All persistent writes remain under `projects/chirality-app-dev/`.

## Fan-in gates

- R14 accurately distinguishes the owner-reported failed command from live
  read-only observation: error `Current GUI login-session identity is not valid
  JSON`, failure before prepare mutation, no plist/job, only the empty old
  proof root, and no proof/acceptance effect.
- The source contains no JXA `CGSessionCopyCurrentDictionary` dependency.
- Detector validates console user, exact UID, Aqua GUI domain, positive unique
  handle/security `asid`, and identifier agreement; malformed, ambiguous,
  mismatched, wrong-user, command-failure, and unchanged-session cases fail.
- A reproducible preflight path performs only `/dev/console` inspection and
  top-level `launchctl print gui/<uid>`; it creates no session root or other
  state and succeeds on macOS 26.6.2.
- Focused/full tests and typecheck pass; no package/build output is produced.
- R15 and `_STATUS.md` retain `IN_PROGRESS`, unproved, unbuilt, and owner-act
  boundaries. A new root/label may be proposed, but exact `PROOF_REVISION` and
  `PROOF_APP` stay gated on the later committed rebuild.
- Fresh review passes with no actionable finding and write containment passes.
