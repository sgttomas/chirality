# ACTIVATION — A2-PKG09-R20-PR632-UID-BUILD-RESTAGE-01

- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-UID-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-UID-BUILD-RESTAGE-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role and non-delegation are instruction-asserted. No delegation is authorized or performed.
- Sealed brief: `briefs/A2-PKG09-R20-PR632-UID-BUILD-RESTAGE-01.md`.
- Objective: execute the sole offline exact-revision supply verification and package build, verify the package, restage R20 documentation without proof execution, run only exact read-only Step 0, and extend the existing portability TM candidate.
- Accepted source/build basis: branch `codex/app-login-proof-r20-repair`; HEAD `2ee96958daf997b7a156f020739bde43ca78ebf9`; parent `4a48aeaede2d050631006f8ff23fb11736752bef`; frontend tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- Frontend worktree posture at activation: no tracked or untracked frontend change; `git diff --stat HEAD -- projects/chirality-app-dev/frontend` is empty. The Git index is empty. Four manager-authored App-only v13 planning/brief files are untracked outside the frontend and are accepted predecessor state.
- Frozen Electron supply posture: expected non-symlink directory `/Users/ryan/Library/Caches/chirality/electron-dist` with sole expected archive `electron-v43.2.0-darwin-arm64.zip`; size and SHA-256 are frozen separately before the one-shot verifier.
- Network posture: the one-shot supply verifier and package build run under the ordinary sandbox's external-network denial, without escalation, retry, or download authorization.
- Serialized write boundary: the existing R20 record, DEL-09-04 `_STATUS.md`, existing run-root TM-candidate record, and this unique instance directory. No frontend source/test/script, receipt, or other shared write is authorized.
- Retained checks: Phase-F focused normal, `umask 0002`, full suite, typecheck, syntax, APP-HOLD, diagnosis, implementation, and fresh source review are not rerun.
- Hard exclusions: no delegation; no Git mutation; no GUI; no proof prepare/capture/logout/login/bootstrap/kickstart; no default operator job/plist/launcher query or mutation; no private-root or Desktop evidence traversal; no signing, distribution, release, or acceptance claim.
- Stop rule: any failed basis, cache, one-shot, package, identity, Step-0, scope, or fence gate stops the run without retry or repair.
