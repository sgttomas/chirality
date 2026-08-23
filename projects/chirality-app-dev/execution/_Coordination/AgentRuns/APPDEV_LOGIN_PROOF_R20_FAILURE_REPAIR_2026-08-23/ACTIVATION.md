# WORKING_ITEMS activation

- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`
- InstanceID: `WI-PKG09-R20-REPAIR-01`
- PackageID / DeliverableID: `PKG-09 / DEL-09-04`
- Pattern: `TERMINAL_FAN_OUT_IN`, serialized implementation then fresh review.
- Selection authority: explicit owner direction transcribed in `CHAT_TRANSCRIPTION.md`.
- Accepted basis: branch `codex/app-login-proof-r20-repair`; HEAD and `origin/main` `a702dd6ec5005b361c8c023b12b599a425e5e2b8`; frontend tree `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`; clean worktree and index at activation.
- Software profile: `projects/chirality-app-dev/software-workflow.json` under `docs/SOFTWARE_WORKFLOW_PROFILE.md`.
- APP-HOLD dispatch preflight: `ALLOW`, target `DEL-09-04`, register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`, scan fingerprint `c63c1e550908573512913d35b8e9e455cbc12c1e31d4d19c0014830eb4af3fe9`.
- Fixture source pre-copy identity: `/private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt`, regular file, 3,049 bytes, SHA-256 `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`.
- Phase-A scope: cleanup parser, cleanup ordering/preservation, non-PASS failure-log preservation, focused tests, verbatim fixture, evidence, and fresh source review.
- Phase-A exclusions: full `npm test`; build/package; final R20/status/Receipt 191; Git integration; network; proof procedure; GUI; LaunchAgent/plist/bootstrap/kickstart/logout/login; operator/default surfaces; signing/notarization/deployment/release claims; prohibited private root/Desktop evidence reads.
- Delegation class: `delegated-harness-native`. Agent-2 role and K-SUBAGENT non-delegation are `instruction-asserted`; role non-delegation is not mechanism-proven.
- Completion gate: fresh source/evidence review `PASS` with no actionable finding before CHANGE may create the final frontend-touching commit.
