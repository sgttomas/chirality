# Status: DEL-09-04

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-04
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Current R20 disposition

- The owner reports that R19 was executed on 2026-08-23 and failed nonzero at cleanup with `Loaded cleanup job last exit code is invalid`; its proof assertions were true but cleanup refused job mutation and left the job/process present. The three failed JSON paths, hashes, modes, manual bootout/absence facts, and unchanged operator-daemon observations are owner-reported only; raw bootout output was promised but not supplied. Phase A repaired the exact macOS 26 `(never exited)` parser/cleanup/evidence-loss failure at exact revision `cb008dc5d6aa9b249639c91f3453a18609530d0f`. PR #632 then repaired only test fixture portability: explicit runtime-data modes after exact `umask 0002` reproduction, followed by host-real UID derivation after CI exposed the remaining UID-501 assumption; product source remained unchanged. The accepted exact build/proof revision is `2ee96958daf997b7a156f020739bde43ca78ebf9`, with frontend tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`. One frozen-supply verifier and one ordinary network-denied offline package build passed without retry; unsigned arm64 launcher and runtime CLI retain their expected hashes, the exact current-byte instruction root passed at 43 files, and the R17 socket guard is unchanged. The fresh packaged `dist-electron/main.js` identity differs from the prior package and is recorded as an independently observed, causally unexplained output rather than attributed to the test-only delta. The immutable R20 root/label/destinations and procedure structure were unchanged, all `PROOF_REVISION` values were rebound to 2ee, and the exact read-only Step 0 plus optionless preflight passed without mutation. Final Phase-F evidence retained without rerun includes 72/72 ordinary focused, 72/72 under `umask 0002`, 1,282 passed / 4 skipped in the local-socket full suite, typecheck, syntax, APP-HOLD, and fresh review. The owner subsequently executed R20 and returned exact-revision `PASS` public evidence. The packaged-LaunchAgent actual-login-session proof obligation is satisfied by that owner-executed evidence; see `_run_records/R21_R20_OWNER_LOGIN_SESSION_PROOF_PASS_CLOSEOUT_2026-08-23.md`. Any frontend mutation invalidates the staged procedure and requires a newly staged exact revision/package plus fresh owner proof for a future claim. DEL-09-04 remains `IN_PROGRESS` on separately gated signing, notarization, DMG, and release lanes. No acceptance, release-readiness, signing, notarization, distribution, publication, issuance, or reliance claim is made.

## Superseded proof history (preserved, not Remaining)

- Before R20 execution, actual login-session discovery and auto-start remained unproved. The exact
  owner-operated R16 attempt reached a non-claiming `PREPARED` state and an
  observed login-session transition, but capture failed nonzero at source
  revision `06f60e42e35ea5c39abf9e33c4d3e877d77c4497` with `Loaded job has
  ambiguous process identity`. Public failure evidence remains `FAIL`; cleanup
  removed the proof plist and runtime data but refused to mutate the residual
  loaded job. The owner reports `runs = 16` and a later manual residual
  bootout; the current exact plist/job absence is independently recorded.
  Repeated `listen EINVAL` evidence and exact 119-byte R16 / 111-byte R13 socket
  paths identify the macOS pathname-boundary failure. R17 records the immutable
  failure; its fail-closed prepare-time 103-byte enforcement, exact-owned
  pid-less crash-loop cleanup, and deterministic runtime-host guard are merged.
  R18 now records a candidate Electron supply freeze and one successful offline
  evidence build only; it does not adopt a package or stage/execute proof. The
  ordinary-sandbox full frontend diagnostic remains not PASS and is classified
  `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`: 21 failed / 1,246 passed / 4 skipped on
  local TCP/Unix-socket `listen EPERM`. The exact owner-authorized `npm test`
  cure with local test-socket permission passed once at 1,267 passed / 4
  skipped, exit 0, with identical before/after source, test, package-script,
  and complete candidate-diff hashes. The PR pre-merge release-quality
  wrapper's `full_test` plus typecheck is future independent confirmation and
  has not yet been observed. R19 has now rebuilt the unsigned arm64 package
  offline from exact merge `d6861ae8251e2a81078577d4496e949735ff199d`,
  confirmed the packaged R17 guard, and passed one direct disposable daemon
  precheck at the 67-byte socket with authenticated packaged-CLI health and
  complete cleanup. The new exact owner procedure is staged as documentation
  only and remains unexecuted. Validation is held after the sole
  local-socket-permitted full-suite cure retained one non-socket Pi/oMLX wire
  timeout failure at 1 failed / 1,266 passed / 4 skipped, with exact pre/post
  source and candidate-diff identity. No full-suite rerun is authorized in
  this executor; manager repair-cycle disposition and fresh review remain.
  The proposed absent/non-symlink 33-byte root
  `/private/tmp/ch-r18-91499728-51dd` and its 67-byte control-socket path leave
  36 bytes below the macOS maximum. See
  `_run_records/R17_LOGIN_PROOF_FAILURE_AND_REPAIR_2026-08-22.md`.
  The prior exact
  owner Terminal attempt failed before preparation completed with `Current GUI
  login-session identity is not valid JSON`; owner-reported failure evidence is
  recorded in `_run_records/R14_MACOS26_LOGIN_IDENTITY_PREPARE_FAILURE_2026-08-22.md`.
  The obsolete JXA/CoreGraphics detector has now been replaced in merged source
  with a fail-closed `/dev/console` plus top-level
  `launchctl print gui/<uid>` detector and an optionless read-only preflight.
  Comprehensive focused/full tests, typecheck, APP-HOLD, practitioner
  self-check, and the live macOS 26.6.2 preflight pass; see
  `_run_records/R15_MACOS26_LOGIN_IDENTITY_REPAIR_2026-08-22.md`. The exact
  merged revision `06f60e42e35ea5c39abf9e33c4d3e877d77c4497` has now been
  rebuilt as the unsigned local arm64 app at
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`;
  the concrete unique absent macOS 26 proof root/label and owner-only procedure
  are staged in
  `_run_records/R16_MACOS26_LOGIN_PROOF_BUILD_AND_STAGING_2026-08-22.md`.
  That R16 procedure has now been executed and failed as recorded in R17.
  Any future preparation, owner logout/login, capture, proof handoff, and proof
  acceptance remain separately authorized owner acts, so the deliverable
  remains unproved.
  The prior reviewed two-phase harness/test candidate was restored at live frontend paths
  under the owner's superseding **“Push through failures”** direction.
  Implementation preparation is complete: Agent 0 repaired only the ignored
  dependency workspace, and mandatory integrated Vitest/typecheck/build plus
  the focused affected trio now pass. Fresh integrated review found only three
  record defects; amendment 10 fixed them and the direct backcheck passed with
  zero actionable findings and unchanged product hashes. The local managed premerge attempt reached
  a READY Next service but returned HTTP 503 because the shared runtime
  daemon/project registration lifecycle was absent; premerge is PR-CI-owned and
  must rerun after PR. Root runtime writes, unrelated App mocks, and tracked
  setup files remain untouched. See
  `_run_records/R12_LOGIN_SESSION_PROOF_PREPARATION_2026-08-21.md`. Any future
  logout/login and capture remain owner acts. The prior unsigned app-directory
  package was rebuilt from exact commit
  `1b375af4f1219ecfc00fc2755854aa7fd4220901`; current-byte instruction-root
  integrity, including the post-#602 HELP_HUMAN bytes, passed and the concrete
  two-phase owner procedure was staged without execution in
  `_run_records/R13_POST_ROOT_LOGIN_PROOF_ENABLEMENT_2026-08-21.md`; that
  package and procedure are now superseded for future execution because they
  do not contain the repaired detector. This history is superseded by the R20
  owner-executed PASS recorded in R21.

## Remaining

- After a rebuilt C1 artifact exists, the owner may deploy the daemon service
  on the owner's machine and report the result (owner act, not agent work;
  owner decision gate 3 of `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`). Merging alone changes
  nothing on a machine whose LaunchAgent was installed earlier: the existing
  plist keeps the crash-only restart contract and carries no pinned environment
  until `daemon install` is re-run from a rebuilt app or the rebuilt CLI.
  Operator-facing behaviour changes are enumerated in the run record.

- **DEL-09-04-V3-01** (`NOT_SELECTABLE_UNTIL: accepted Root supervisor/runtime bytes routed to App (Root DEL-02-07) and the DEL-02-06 implementation act`) — package supervisor/runtime bytes into the unsigned macOS arm64 DMG with preparation posture evidence.
  Trace: OUT-001, AC-001, VER-001; DEL-09-04-REQ-001/002/005/006/008/010; applied decomposition row L367 (produce the macOS arm64 unsigned DMG and prove instruction-root assets plus SDK packaging posture are valid; one release target).
  Plan: WP-09; G5; AT-038 unsigned-artifact configuration, AT-047 nested-byte survival, AT-058 preparation observation; macOS arm64 only (G0 B1). Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Root DEL-02-07 accepted supervisor bytes and DEL-02-06 implementation act (routed notices); DEL-09-05-V3-03 identity check and DEL-09-05-V3-06 identity application (dependency-linked, not gates: the package this item produces is what G5 reviews); DEP-09-04-005 through 009; R18 frozen Electron supply posture (`electron-v43.2.0-darwin-arm64.zip`, SHA-256 `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`). The two-job installer/migration/rollback through runtime-control IPC (AT-054 App side) is unseated (`SCOPE_AMENDMENT_REQUIRED`, see the seating packet MAPPING). Any `frontend/` mutation invalidates the staged R20 procedure (A1 re-stage rule).
  Write locus: `frontend/scripts/**` packaging glue, electron-builder configuration, `Evidence/**`, and deliverable-local state; no signing identity, notary call, or distribution.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched; packaged launches run only under the AGENTS.md host-capability escalation rule.
  Return: Offline network-denied package evidence with nested-byte/signature inventory, integrity summary, and unsigned/ad-hoc posture proof; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the preparation package lands with G5 evidence.

- **DEL-09-04-V3-02** (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-04 selected`) — `build/icon.icns` replacement with packaging-integrity regeneration and the reproducibility record for the raster icon (T7 packaging part).
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L381 (macOS arm64 unsigned DMG; instruction-root assets plus SDK packaging posture proven valid); SOW-030, SOW-072.
  Plan: T7 packaging part; SR-16; Q5 ruled D-APP-108 (icon only; no pop-out window); `05_LOGO_AND_BRAND.md` §4 (SHA-256 `84b466fde1fea8418f41778a51ecadfde496322edeac14f6ec2aa508dc509d2b`). Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: DEL-02-01-V3-04 (source SVG and raster record); F-APP-2 and D-APP-97 (no signing, notarization, or distribution; unsigned DMG only).
  Write locus: `frontend/build/icon.icns`, `frontend/build/icon-macos.svg`, packaging-integrity summary regeneration under `frontend/scripts/**`, `Evidence/**`, deliverable-local state. No signing identity, notary call, or distribution.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched; packaged launches run only under the AGENTS.md host-capability escalation rule.
  Return: a regenerated `.icns` from the recorded source with the reproducibility record (source SVG hash, rasterization command and versions, per-size hashes) and an updated packaging-integrity summary; no signing or release act; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS.

## History
- 2026-09-04 - SCA-APP-010 shell-redesign seating (D-APP-108; owner adopted the seating list as presented): Remaining items seeded DEL-09-04-V3-02 (SELECTABLE: none) with gate, dependency, write-locus, check, and return contracts; ruled questions cited by item. Outside the thirteen SCA-APP-010 carriers: seating only, no Scope of Work, context, or reference change. Run evidence `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; v3 Remaining items seeded (1, of which 0 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-08-23 - The owner executed the exact R20 staged procedure at revision `2ee96958daf997b7a156f020739bde43ca78ebf9` and returned `PASS`. Exactly three public JSON files were independently verified as mode `0600` under a mode-`0700` public directory, copied byte-identically to `Evidence/R20_Owner_Login_Proof_PASS_2026-08-23/`, and verified at hashes `5961b2060b554dc12989947a45335422f48f9e953d5af60c2ece88f7fdcf0a88`, `38a603c470a51209b463a4657448794f8500cb32bfd5f83c2e6c611fb0aa06b1`, and `aa84cdf66753d229dc9b2d27d147bc892107f054266d62f1f4bdf261280a6405`. The packaged-LaunchAgent actual-login-session proof obligation is satisfied by owner-executed evidence. Any frontend mutation invalidates the staged procedure and requires a new staged revision plus fresh owner proof for a future claim. DEL-09-04 remains `IN_PROGRESS` on separately gated signing, notarization, DMG, and release lanes; no G0.25 human ruling, acceptance, release-readiness, signing, notarization, distribution, publication, issuance, or reliance claim is made. See R21.
- 2026-08-23 - PR #632 UID portability is committed at exact revision `2ee96958daf997b7a156f020739bde43ca78ebf9`, frontend tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`, with test-only host-real UID derivation and no product change. Retained final Phase-F checks passed and were not rerun here. Exactly one frozen-supply verification and one ordinary network-denied offline package build passed without retry; the unsigned native launcher and runtime CLI retain their expected hashes, current-byte instruction-root integrity passed at 43 files, and the R17 guard is unchanged. The fresh packaged-main identity is recorded as an independently observed, causally unexplained delta. The unchanged R20 root/label/destinations are rebound to 2ee and the exact read-only Step 0 plus optionless preflight passed without mutation. The fixture-mode/UID/GID/path portability concern is extended in the existing TM candidate with CI as the host-identity arbiter. R20 remains staged, not executed; DEL-09-04 remains `IN_PROGRESS` and unproved; all proof, owner, operator, Receipt 193, Git/publication, signing, notarization, distribution, and release fences remain.
- 2026-08-23 - PR #632 fixture portability is committed at exact revision `b33858d33220538ce292f276a442792ecf8050b1`, frontend tree `23315613d0d3e4d21580d928909816dc5aad92c7`, with test-only explicit `0700`/`0600` fixture creation and no product change. One frozen-supply verification and one ordinary network-denied offline package build passed; unsigned arm64 package, runtime CLI, current-byte instruction root, and packaged R17 guard identities passed. The unchanged R20 root/label/destinations are rebound to the b338 revision and the exact read-only Step 0 plus optionless preflight passed without mutation. One ordinary-sandbox full-suite diagnostic retained 21 socket denials plus one synthetic-PID case at 22 failed / 1,260 passed / 4 skipped; the sole local-socket cure passed 1,282 / 4 skipped with unchanged hashes. The permission-fixture/non-macOS-umask item is harvested as a TM candidate only. R20 remains staged, not executed; DEL-09-04 remains `IN_PROGRESS` and unproved; all proof, owner, operator, Receipt 191, Git/publication, signing, notarization, distribution, and release fences remain.
- 2026-08-23 - Recorded the owner-reported R19 executed-and-failed result without inspecting private/Desktop evidence; raw manual-bootout output remains missing. Phase-A cleanup-parser/failure-evidence repair is committed at exact revision `cb008dc5d6aa9b249639c91f3453a18609530d0f`. One network-denied offline package rebuild and one exact disposable packaged-daemon precheck passed; the main executable remains `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`. The diagnostic retained 21 sandbox socket denials (1,261 passed / 4 skipped); the sole local-socket cure passed 1,282 / 4 skipped with unchanged semantic identities. R20 is documentation-only staging under a fresh UUID label and was not executed. DEL-09-04 remains `IN_PROGRESS` and unproved; all proof, Receipt 191, Git/publication, operator, signing, notarization, distribution, and release fences remain.
- 2026-08-23 - Reverified the frozen Electron 43.2.0 arm64 supply and ran
  exactly one network-denied `npm run desktop:pack` from exact merged revision
  `d6861ae8251e2a81078577d4496e949735ff199d`. Custom `electronDist`, embedded
  dependency/instruction-root gates, package identity, current-byte evidence,
  and the packaged R17 socket guard pass. Exactly one direct disposable
  packaged daemon precheck bound the proposed 67-byte socket, returned
  authenticated packaged-CLI `project list --json` health, exited gracefully,
  and removed its exact process/socket/runtime/root state. R19 stages the
  concrete owner procedure without executing any block. DEL-09-04 remains
  `IN_PROGRESS` and unproved. The sandbox diagnostic retained 21 expected
  socket-denial failures plus one separate synthetic-PID failure; the sole
  local-socket-permitted cure cleared both sets but retained one Pi/oMLX wire
  timeout (1 failed / 1,266 passed / 4 skipped) with unchanged semantic bytes.
  Manager repair-cycle disposition and fresh review remain required. Owner
  prepare/logout/login/capture/handoff and
  acceptance remain future acts. No GUI, LaunchAgent/plist/bootstrap/kickstart,
  default-operator, signing, notarization, deployment, distribution,
  publication, release-readiness, Receipt 190, or Git integration act occurred.
  See `_run_records/R19_OFFLINE_EXACT_MERGE_BUILD_AND_LOGIN_PROOF_STAGING_2026-08-23.md`.
- 2026-08-22 - Added the candidate Electron 43.2.0 arm64 supply freeze after
  preserving the first cache-miss failure, the terminal redirect attempt, and
  the accepted two-host official SHASUMS response. The fail-closed verifier
  pins the exact version, filename, size, hash, official line, and source; the
  argv-safe wrapper passes one verified electronDist directory to Electron
  Builder. One network-denied `npm run desktop:pack` exited zero with custom
  electronDist, no download indicator, and dependency/instruction-root gates
  passing. The ignored build is evidence only and not adopted. Deterministic,
  governance, and focused checks pass. The ordinary-sandbox full frontend
  diagnostic remains not PASS and is classified
  `ENVIRONMENT_SANDBOX_SOCKET_DENIAL` at 21 failed / 1,246 passed / 4 skipped.
  One exact owner-authorized `npm test` cure with local loopback/Unix-socket
  permission passed at 1,267 passed / 4 skipped, exit 0; pre/post semantic
  hashes and the complete candidate diff are identical. Future PR pre-merge
  `full_test` plus typecheck confirmation has not yet been observed. Fresh
  review remains required. DEL-09-04 stays `IN_PROGRESS` and unproved; R19 is a separate
  post-merge owner act. No proof procedure, operator mutation, signing,
  notarization, deployment, distribution, release claim, or Git integration
  occurred. See
  `_run_records/R18_ELECTRON_SUPPLY_FREEZE_AND_OFFLINE_BUILD_2026-08-22.md`.
- 2026-08-22 - Preserved the owner-operated R16 attempt as immutable failed
  evidence: prepared state made no proof claim, the login-session transition
  was observed, and capture/evidence remained `FAIL` at exact source revision
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497` after repeated runtime-daemon
  `listen EINVAL` failures on the 119-byte control-socket path. R17 separates
  owner-reported capture/run/manual-bootout facts from independent public
  evidence and current absence checks. The bounded uncommitted repair rejects
  macOS paths over 103 UTF-8 bytes before prepare mutation, permits only
  exact-owned pid-less proof-job cleanup, and fails runtime-host startup before
  daemon construction. The sole future proposal is the absent/non-symlink
  33-byte root `/private/tmp/ch-r18-91499728-51dd`, whose 67-byte socket leaves
  a 36-byte margin; it was not created or staged as R18. The future
  short-socket and KeepAlive recommendations are evidence only. State remains
  `IN_PROGRESS` and unproved; no R18 execution or mutation, build,
  package, proof acceptance, operator mutation, signing, notarization,
  deployment, distribution, or release act occurred.
- 2026-08-22 - Rebuilt the unsigned thin-arm64 local app from exact merged
  revision `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`. The tracked package
  command's dependency boundary and current-byte instruction-root integrity
  gates passed, independent package and Git identities passed, and the live
  optionless read-only macOS 26 preflight passed without creating the proposed
  proof root or inspecting a service/job. R16 stages concrete owner-only
  prepare, logout/login, capture, PASS, preservation, and handoff documentation
  without executing it. State remains IN_PROGRESS and unproved; all operator,
  lifecycle, signing, notarization, distribution, publication, release, and
  reliance fences remain.
- 2026-08-22 - Recorded the owner-reported macOS 26.6.2 prepare failure and
  replaced the obsolete JXA/CoreGraphics login-session identity probe with a
  fail-closed `/dev/console` plus top-level GUI login-domain detector. The new
  optionless read-only preflight passed live without creating the proposed
  root or issuing service/job-level or mutating launchctl operations. Focused
  tests passed 46/46, full Vitest passed 1,245 with 4 skips after the exact
  sandbox-denied socket fixture run was repeated with local socket permission,
  and typecheck, APP-HOLD, practitioner self-check, syntax, and whitespace
  checks passed. The repair remains uncommitted and unbuilt; DEL-09-04 remains
  IN_PROGRESS and unproved, with prepare/logout/login/capture and operator
  deployment still owner acts. See R14 and R15.
- 2026-08-21 - Post-Root login-proof enablement rebuilt the unsigned arm64 app
  directory with `npm run desktop:pack` from exact commit
  `1b375af4f1219ecfc00fc2755854aa7fd4220901`. The dependency-boundary and
  current-byte instruction-root checks passed; source and bundle
  `AGENT_HELP_HUMAN.md` both match SHA-256
  `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`.
  The frontend-tree commit-to-HEAD diff is empty. R12's owner procedure is now
  staged with concrete unique absent proof values, but prepare, logout/login,
  capture, GUI launch, operator deployment, and proof remain unexecuted owner
  acts. The accepted first-GUI-launch launcher rewrite is recorded as an
  expected operator-facing effect, not a park condition. DEL-09-04 remains
  IN_PROGRESS; no signing, notarization, distribution, publication,
  release-readiness, issuance, or reliance claim is made. See
  `_run_records/R13_POST_ROOT_LOGIN_PROOF_ENABLEMENT_2026-08-21.md`.
- 2026-08-21 - Owner-authorized PREPARE-THEN-OWNER work produced a reviewed
  fail-closed two-phase candidate and minimal future owner procedure. Focused
  tests, syntax, exact scope, practitioner checks, APP-HOLD integrity, and final
  fresh review passed, while mandatory integrated gates exposed the external
  `RUNTIME_INSTRUCTION_ROOT_ENV` alignment. The owner immediately superseded a
  stop disposition with **“Push through failures.”** Exact frozen diff 04 bytes
  were restored to live candidate paths. Agent 0 rebuilt current runtime only
  inside ignored frontend dependencies; registered typecheck/build, host full
  Vitest (1,214 passed / 4 skipped), and focused affected tests (35/35) now pass
  without tracked root/App setup changes. Local premerge reached a READY Next
  service but returned HTTP 503 without shared runtime/project registration, so
  it remains PR-CI-owned. Preparation and local fan-in are complete pending
  Git/PR and PR-CI. Logout/login and capture remain unexecuted,
  DEL-09-04 stays IN_PROGRESS, and no proof, publication, lifecycle, release,
  signing, notarization, distribution, or reliance claim is made. See
  `_run_records/R12_LOGIN_SESSION_PROOF_PREPARATION_2026-08-21.md`.
- 2026-08-20 - PR #591 Desktop run `32410644968` / job `96560074456`
  passed the D-APP-97 packaged-service proof on `macos-15`. The packaged CLI
  installed a unique non-default job in the disposable account's canonical
  `~/Library/LaunchAgents`; one bootstrap relied on `RunAtLoad` without
  `kickstart`; automatic launch, exact loaded argv and executable identity,
  complete process/job/plist/runtime cleanup, and default job/plist protection
  all passed in retained evidence. This materially narrows the login-time
  `RunAtLoad` Remaining item to actual login-session discovery/auto-start; it
  does not recreate a full logout/login session. `IN_PROGRESS`, lifecycle,
  Checking Approval SHA, owner-machine deployment act, and all release fences
  remain unchanged. See
  `_run_records/R11_DAPP97_RUNATLOAD_PR_CI_PROOF_2026-08-20.md`.
- 2026-08-20 - The coordinated DEL-09-06 fresh packaged-security proof passed
  for the exact unsigned arm64 app identity and closed DEL-09-04 REQ-009 /
  R4-P49 packaged-network evidence. Blocked renderer probes, five usable
  descendant TCP snapshots, zero non-allowlisted outbound, provider isolation,
  secret containment, and cleanup all passed. Only the named packaged-network
  Remaining item is removed; login-time `RunAtLoad` and the later owner-machine
  deployment act remain. State stays IN_PROGRESS; lifecycle, Checking Approval
  SHA, signing, notarization, distribution, publication, and release readiness
  remain unchanged.
- 2026-08-19 - PR #585 external proof accepted for the exact selected
  D-APP-97 packaged-SDK/R4-P49 engineering gap. Desktop run `32332985341` /
  job `96317050414` passed separate scripted no-live-provider verifier runs
  against the staged packaged app and the read-only `RUNNER_TEMP`-mounted DMG
  app; both retained summaries report `status: pass`, distinct bundle roots,
  and the same packaged executable identity. Harness run `32332985346` / job
  `96317050162` and governance run `32332985350` / job `96317050220` also
  passed. The packaged-SDK/DMG and release-quality premerge Remaining items
  are removed. Login-time `RunAtLoad`, packaged network-policy proof, and the
  later owner-machine deployment act remain. State stays IN_PROGRESS;
  lifecycle, Checking Approval SHA, signing, notarization, distribution,
  publication, and release-readiness posture are unchanged.
- 2026-08-19 - Pre-CI D-APP-97 packaged-SDK workflow integration added
  separate fail-closed scripted no-live-provider proofs for the staged app and
  read-only mounted DMG app, with both summaries retained in the unsigned CI
  artifact evidence. Local static and deterministic checks passed. Actual
  macOS staged/mounted execution and candidate-range G4 remain PR-CI-owned, so
  the packaged-SDK/R4-P49 Remaining item stays open; state remains IN_PROGRESS
  and lifecycle, Checking Approval SHA, signing, notarization, distribution,
  publication, and release-readiness posture are unchanged.
- 2026-08-19 - D-APP-100 landed as a bounded product-source node. The packaged
  daemon now prefers the registered manifest-resolved instruction root shared
  by app/CLI runtime requests and durably logs packaged-resources fallback only
  when registration/manifest resolution is unavailable. Agreement regression,
  unsigned packaged-under-isolation proof, full deterministic gates, and fresh
  independent review passed. The exact D-APP-100 Remaining item was removed;
  unrelated Remaining items, lifecycle, Checking Approval SHA, signing,
  notarization, distribution, and release-readiness posture are unchanged.
- 2026-08-17 - D-APP-95 accepted guarded recover-on-start as complete handling
  for a SIGKILLed daemon; the stale-socket residual was removed. D-APP-97
  opened the named unsigned release-preparation, `RunAtLoad`, packaged-SDK,
  DMG/dist, and premerge scope while preserving F-APP-2 and APP-HOLD-1. The
  owner-machine deploy remains a later owner act. D-APP-100 authorized the
  packaged-daemon instruction-root engineering node, which remains in
  Remaining until it lands. No engineering or product byte, lifecycle,
  Checking Approval SHA, release, signing, notarization, or distribution act
  occurred in this recording tranche.
- 2026-08-13 - Owner ruling disposed D-APP-93 with the landed PR #551 normalized trace evidence accepted as its complete and sufficient product; no further packet execution or lineage is required or authorized. D-APP-88 is concluded: the accepted engineering explanation is that no SIGTERM handler was bound in the shipped helper at the stop instant combined with the retired `before-quit` veto that swallowed SIGTERM. The held-connection `server.close()` stall hypothesis is neither confirmed nor refuted and is not a cause. PR #552's signal binder, bounded teardown, and held-connection regression are accepted as closing the failure mode under either variant. The helper-stop residual is removed from Remaining. DEL-09-04 stays IN_PROGRESS on its unrelated residuals; lifecycle and Checking Approval SHA are unchanged.
- 2026-08-13 - Runtime helper graceful-stop hardening prepared for review: a shared one-shot process-signal binder now drives the shipped daemon through the complete Electron teardown funnel, native `before-quit` remains vetoed until teardown completes, and the existing two-second grace/forced-transport close remains unchanged. A spawned-process regression arms a daemon-parsed complete-header/incomplete-body Unix-socket request, sends `SIGTERM`, and proves natural exit plus socket/owner cleanup in 2.146 s. Runtime tests passed 76/76; frontend tests passed 1113 with 6 skips; both typechecks and fresh code review passed. This is product implementation evidence only: DEL-09-04 remains IN_PROGRESS and no D-APP-93/D-APP-88 disposition, acceptance, closure, lifecycle, or Checking Approval SHA act is made.
- 2026-08-11 - The owner froze and executed the D-APP-93 owner-operated LLDB trace packet; Step 0 passed and the capture completed with zero stop rules. Landed evidence records SIGTERM delivered to `CrBrowserMain` in the AppKit event loop while two helper control-socket clients were live, with no Node/libuv/V8 signal-handler frames at the stop instant. LLDB intercepted the signal (`PASS=false`), so unintercepted processing was not tested. The helper remained alive after detach and continued serving. Evidence disposition and all D-APP-88 conclusion/remedy/acceptance acts remain reserved to the owner. DEL-09-04 remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-08-04 - D-APP-88 R3 accepted Root TM-ROOT-112 as fit to release the App rerun, reconstructed the exact source-aligned helper, and produced auditable authenticated post-GUI first-signal failure evidence: helper/GUI remained alive through 80 polls, socket/owner persisted, and App teardown/Root stop were not entered. An exact instrumented SINGLE/STANDARD matrix then passed all four credited first-signal arms identically, so `single-process` removal and every other App-native remedy remain unsupported; the instrumentation may perturb absolute timing and does not erase the earlier failure. Fresh verifier PASS accepted the calibrated blocker/handoff only. Product/config/test and local runtime/build residue were rolled back. DEL-09-04 remains IN_PROGRESS, D-APP-88 remains open, TM-APP-036 does not fire, and the next replay is held for owner-authorized interactive GUI-session native tracing plus a sealed uninstrumented command/timing transcript. Lifecycle and Checking Approval SHA are unchanged.
- 2026-08-03 - D-APP-88 R2 evaluated the previously untried separately built full Electron helper. The standalone `com.chirality.app.runtime-helper` package, builder-generated child topology, whole-bundle embedding, relocatability, and fresh graceful-stop evidence passed. Acceptance remains BLOCKED because retained post-GUI evidence proves helper restart, GUI contact, no later daemon shutdown entry, and eventual transport loss but does not independently bind the operator-observed first-signal survival/socket retention. The mandatory post-GUI first-signal graceful-stop proof therefore failed. A Root-side live-connection/server-close interaction is recorded only as an investigation hypothesis. Exact candidate bytes were frozen under the R2 run root and all R2 product/config/test changes were rolled back while preserving D-APP-89. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-08-03 - D-APP-88 Option B bounded implementation produced a distinct LoginItems helper candidate with relocatable relative framework links and helper-routed LaunchAgent/CLI paths. Package, focused tests, typecheck, dependency boundary, instruction-root integrity, fresh helper SIGTERM, CLI status, GUI coexistence, and SIGKILL recovery were evidenced. Acceptance remains BLOCKED because first-signal graceful teardown failed after GUI coexistence and an alternate SIGUSR2 diagnostic failed likewise. Exact candidate bytes were frozen under the run root and all D-APP-88 product/config/test changes were rolled back while preserving D-APP-89. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-25 - Daemon-as-service and packaged-app fix tranche recorded in `_run_records/R6_DAEMON_SERVICE_2026-07-25.md`. The headless-daemon / LaunchAgent / bundled-CLI Remaining item is narrowed to its unexercised login-time path and the still-gated DMG/dist scope on the strength of isolated packaged-app evidence (headless daemon with a `safeStorage` round trip, LaunchAgent install/restart/graceful-stop and label scoping, bundled CLI from a clean environment, asar `public/` and `CFBundleIconFile` checks, an end-to-end stub-adapter turn). Six residuals are added: daemon helper-bundle identity (owner-escalated), the SIGKILL stale-socket recover-on-start case, the unsatisfied premerge row for this branch, post-merge owner-machine deployment (owner decision gate 3), the pre-existing packaged-daemon instruction-root divergence, and the login-time `RunAtLoad` path folded into the narrowed first item. No release, signing, notarization, or distribution authority is created. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-22 - D-APP-72 Electron `43.1.1` regression and packaged offline Pi `0.80.10` production-route proof completed. The unrelated D-APP-56 release-preparation item remains open; no release authority is created. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-21 - SCA-APP-002 added the Electron/Pi package prerequisite proof to Remaining; release fence and state remain unchanged.
- 2026-07-20 - D-APP-71 Option 2 closed the preload physical-lead residual by applying DEL-02-05 as coordination-only lead; DEL-09-06 retains `safeStorage`/security semantics, the packaging/release Remaining item is byte-preserved, and no source, SOW, dependency, lifecycle, or Approval-SHA change occurred.
- 2026-07-20 - D-APP-70 Option A closed the `chirality-window.d.ts`, scripted SDK proof, and contract-lint CQ-F1 residuals and applied only the shared-boundary annotation for `preload.ts`; its unnamed physical lead remains the sole CQ-F1 residual gated by D-APP-71; unrelated packaging/release Remaining is unchanged; no source, lifecycle, Approval SHA, SOW, or dependency change.
- 2026-07-12 - D-APP-56 consolidated R5 decision application recorded; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents P1/P2)
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-075, UPD-078; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
