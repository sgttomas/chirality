# ACTIVATION — A2-PKG09-R20-PR632-BUILD-RESTAGE-01

- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-FIXTURE-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-BUILD-RESTAGE-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role and non-delegation are instruction-asserted. No delegation is authorized or performed.
- Sealed brief: `briefs/A2-PKG09-R20-PR632-BUILD-RESTAGE-01.md`.
- Objective: execute the sole offline exact-revision package build, verify the package, restage R20 documentation without proof execution, execute the exact full-suite diagnostic/cure pair, and harvest the permission-fixture TM candidate.
- Accepted source/build basis: branch `codex/app-login-proof-r20-repair`; HEAD `b33858d33220538ce292f276a442792ecf8050b1`; parent `980f5951dbbfe88302514802384e4ffec33c38b9`; frontend tree `23315613d0d3e4d21580d928909816dc5aad92c7`.
- Frontend worktree posture at activation: no tracked or untracked frontend change; `git diff --stat HEAD -- projects/chirality-app-dev/frontend` is empty.
- Frozen Electron supply posture: expected non-symlink directory `/Users/ryan/Library/Caches/chirality/electron-dist` with sole expected archive `electron-v43.2.0-darwin-arm64.zip`; size and SHA-256 are frozen separately before the one-shot verifier.
- Network posture: the one-shot supply verifier and package build run under the ordinary sandbox's external-network denial, without escalation, retry, or download authorization. Only the later exact cure `npm test` may request local test-socket permission; external network remains forbidden.
- Serialized write boundary: the existing R20 record, DEL-09-04 `_STATUS.md`, one new run-root TM-candidate record, and this unique instance directory. No frontend source/test/package/script write, Receipt 191 write, or path outside `projects/chirality-app-dev/` is authorized.
- Hard exclusions: no delegation; no Git mutation; no GUI; no proof prepare/capture/logout/login/bootstrap/kickstart; no default operator job/plist/launcher query or mutation; no private-root or Desktop failed-evidence traversal; no signing, distribution, release, or acceptance claim.
- Stop rule: any failed one-shot, supply, package, identity, suite, scope, or fence gate stops the run without retry or repair.
