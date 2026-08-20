# DEL-09-04 D-APP-97 packaged LaunchAgent RunAtLoad PR-CI proof

- Date: 2026-08-20
- Run: `APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20`
- Product node: `5ee3fc12fb73cdf90f6fa47455db70740a2d2f1f`
- G4 proof-loop commit: `dcd10fa83bdff2ba89733bfd96176b6831591173`
- Pull request: `#591`, base `main`; prior PRs #586, #589, and #590 were
  merged before this PR opened, so no stack dependency remains.
- Trigger: the owner-directed `artifact-proof` label was applied at final
  verification and triggered Desktop run `32410644968`, job `96560074456`,
  on exact head `dcd10fa83bdff2ba89733bfd96176b6831591173`.
- Result: job and step `Prove packaged LaunchAgent RunAtLoad` passed on
  `macos-15`; Harness pre-merge run `32410644943` / job `96560003227` and
  governance Harness run `32410644930` / job `96560003072` also passed.
- Retained evidence: artifact
  `chirality-packaged-launchagent-runatload-proof`, artifact id `9422083629`,
  digest `sha256:2863dfc411104c3fb71ce313ff4fd999338b4f64406db10d620420995a1fc9f2`.
  Its `summary.json` reports `status: PASS`, canonical
  `~/Library/LaunchAgents`, `runAtLoad: true`, `bootstrapOnly: true`,
  `automaticLaunchObserved: true`, exact loaded program/arguments, packaged
  executable identity, process/job/plist/runtime-data absence after cleanup,
  and unchanged/excluded default job/plist targets.
- Claim boundary: this closes the narrower evidence defect that earlier proof
  used a test plist outside the actual LaunchAgents directory. It proves
  bootstrap-triggered automatic RunAtLoad from that real directory on a
  disposable CI account. Because the script invokes `launchctl bootstrap`
  directly, it does not prove login-session discovery or recreate a full
  logout/login session.
- State effect: narrow the login-time `RunAtLoad` Remaining item to actual
  login-session discovery/auto-start, parked until a host-capability surface
  can recreate logout/login or an equivalent fresh login session. DEL-09-04
  remains `IN_PROGRESS` on that residual and the later owner-machine
  deployment act. Lifecycle, Checking Approval SHA, signing, notarization,
  distribution, publication, release, reliance, dependency, and lockfile
  posture are unchanged.

This record is derivative proof metadata and does not substitute for the
product commits, GitHub run, or retained artifact.
