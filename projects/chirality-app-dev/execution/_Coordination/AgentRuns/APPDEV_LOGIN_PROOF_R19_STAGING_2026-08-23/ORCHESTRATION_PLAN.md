# R19 staging orchestration plan

Status: `FROZEN`
Plan-Version: `1`
RunID: `APPDEV_LOGIN_PROOF_R19_STAGING_2026-08-23`
ManagerInstanceID: `WI-PKG09-R19-STAGING-01`
PackageID: `PKG-09`
DeliverableID: `DEL-09-04`
Posture: `TERMINAL_FAN_OUT_IN` with serialized overlapping writes
Selection-Authority: explicit owner direction in `CHAT_TRANSCRIPTION.md`

## Accepted basis

- branch: `codex/app-login-proof-r19-staging`
- requested build revision and current HEAD:
  `d6861ae8251e2a81078577d4496e949735ff199d`
- requested frontend tree and current frontend tree:
  `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`
- initial porcelain/index: empty
- live-state note: `origin/main` was observed later than the owner-selected
  basis. This run does not sync, merge, rebase, or rewrite; the exact requested
  build basis remains controlling.
- APP-HOLD dispatch preflight: `ALLOW`, `NOT_HELD`

## Concrete staging values

- `PROOF_ROOT=/private/tmp/ch-r18-91499728-51dd`
- exact control socket:
  `/private/tmp/ch-r18-91499728-51dd/runtime-data/runtime/control.sock`
- `PROOF_LABEL=com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b`
- exact plist:
  `/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b.plist`
- exact public destination:
  `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r19-3951dfe9-ec03-421b-b376-fd5f0d96992b-public-evidence`

Initial read-only checks found the root, plist, and public destination absent
and non-symlinks. The exact service returned launchctl exit 113 with the exact
label-specific two-line not-found response. No default operator surface was
queried.

## Graph

1. `WP-01 MANAGER_ACTIVATION` — complete: instructions, live basis, receipt,
   APP-HOLD, initial uniqueness, and run graph.
2. `WP-02 R19_EXECUTE` — one ephemeral generalist Agent 2, sole writer for
   generated package evidence, R19, status, and executor evidence. It runs the
   supply verifier, exactly one offline pack, package checks, exactly one
   direct disposable daemon precheck, procedure staging, proportional checks,
   one sandbox diagnostic, and one local-socket-permitted cure.
3. `WP-03 R19_FRESH_REVIEW` — dependency on accepted WP-02 byte freeze; fresh
   evidence-only Agent 2, writing only its review directory and never rerunning
   the elevated full suite, pack, empirical daemon check, or network.
4. `WP-04 MANAGER_FAN_IN` — accept, repair/re-review up to two cycles if
   actionable, or return exact blocker. Receipt/Git/PR work remains excluded.

## Hard fences

No external network, GUI launch, login-proof prepare/capture, logout/login,
LaunchAgent/plist/bootstrap/kickstart action, default operator job/plist/
launcher query or mutation, private R16 proof-root or Desktop-failure-evidence
access, signing, notarization, deployment, distribution, publication,
release-readiness claim, Receipt 190, stage, commit, push, PR, or merge.

## Terminal acceptance

WP-02 must return complete build/package/precheck/procedure/test evidence with
all cleanup and containment gates. WP-03 must return `VALIDATED_PASS` with no
actionable finding. DEL-09-04 remains `IN_PROGRESS` and unproved; the staged
procedure is documentation only and the owner proof remains unexecuted.
