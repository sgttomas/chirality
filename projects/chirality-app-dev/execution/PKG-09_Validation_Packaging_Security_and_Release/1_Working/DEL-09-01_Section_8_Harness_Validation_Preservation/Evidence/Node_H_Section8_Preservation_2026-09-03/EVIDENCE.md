# DEL-09-01-V3-01 — Section 8 preservation evidence after the v3 landings (node H, 2026-09-03)

- **Item:** DEL-09-01-V3-01 — Section 8 preservation and Shared Runtime Gate evidence across the v3 program (revision 1: after PRs 683–686).
- **Run:** `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_H_2026-09-03/` · Implementer: Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN.
- **Claim under evidence:** on `main` at `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge — after PRs #683 node E, #684 node D, #685 node B, #686 node A), the Section 8 harness validation surface preserved by DEL-09-01 behaves exactly as it did at the pre-landing basis `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge): the premerge wrapper produces the stable summary artifact with `status: pass`, `testCount: 8`, the eight accepted IDs in `REQUIRED_CHECK_ORDER`, the retired legacy ID absent, and identical behaviour-bearing row details.
- **What this is not:** validation evidence only (RQG §13 posture; `docs/VALIDATION_STRATEGY.md` §1). No release-readiness, signing, notarization, publication, lifecycle, professional, or certification claim (F-APP-2, F-APP-4). No G5 acceptance is claimed; the item is revised, not removed.

## 1. Inputs and cited-byte inventory

| Input | Identity |
|---|---|
| Post-landing commit (`main`) | `e59efa4830fb54143c86e511ec35a6d1a476f72e` — PR #686 merge |
| Pre-landing basis | `0c683fb1657706316272951e4c3a0f7781b46009` — PR #681 merge (A12 seating) |
| Landings between them (first-parent) | `01ab9280b` PR #683 (node E), `9c99e4bf7` PR #684 (node D), `e560ded1b` PR #685 (node B), `e59efa483` PR #686 (node A) |
| Frontend paths changed across the landings | `FRONTEND_PATHS_CHANGED_0c683fb16..e59efa483.txt` (36 paths; one under `src/lib/harness/` — `session-manager.ts`, node D's lazy v2 session access; none under `frontend/scripts/validate-harness-*` or the Section 8 fixtures) |
| Evaluator / fixture / workflow bytes | `EVALUATOR_BYTES.tsv` — git blob SHA-1 at both commits and SHA-256 at `e59efa483` for `validate-harness-section8.mjs`, `validate-harness-premerge.mjs`, `validate-harness-section9.mjs`, `harness-section9-manifest.json`, `validate-release-quality-evidence.mjs`, `assert-harness-contract-deps.mjs`, the two `validate-harness-*.test.ts` fixtures, `.github/workflows/harness-premerge.yml`, `chirality.project.json`, `package.json`, `package-lock.json`. **All `SAME` across the landings except `package.json`**, whose only delta is three added script entries (`sbom:generate`, `notices:generate`, `verify:version-identity`, node B) — the `harness:validate:*` and `validate:release-quality` entries are byte-identical. |
| Built evaluator bundles (HEAD) | `run-head-e59efa483/logs/built-bundles.sha256`: `dist-electron/main.js` `4d56cc6f…`, `dist-runtime/chirality-cli.mjs` `0503c40a…` (the same CLI bundle hash node A's packaged proof recorded) |
| Toolchain | Darwin 25.6.0 arm64; node v24.18.0; npm 11.16.0; electron 43.2.0; next 15.5.21; vitest 4.1.10 (`run-head-e59efa483/logs/environment.txt`) |
| Project manifest hash seen by the daemon at registration | `5a79777038acd2b5fda3b0416c0092e2c980ff0eff7e84a019fdac3bac8fdc04` (`registration.redacted.json`; the manifest blob is `SAME` across the landings) |

## 2. Method — the CI lifecycle reproduced locally (bounded rerun method)

`rerun-section8-local.sh` (this folder; executable) mirrors `.github/workflows/harness-premerge.yml` step for step on macOS: build the runtime host and bundled CLI; start `dist-electron/main.js --runtime-daemon` under a disposable `--user-data-dir`; register `chirality.project.json` with `dist-runtime/chirality-cli.mjs project register`; start `next dev` bound to the daemon through `CHIRALITY_RUNTIME_{TOKEN_FILE,PROJECT_ID,PROJECT_ROOT}` and `HARNESS_PROJECT_ROOT`; poll `/api/harness/session/list`; run `npm run harness:validate:premerge` and (with `WITH_RELEASE_QUALITY=1`) `npm run validate:release-quality`; record containment observations; tear down; remove the disposable state. Effective environment for the retained run is in `run-head-e59efa483/logs/environment.txt`; the exact invocation was:

```
cd {REPO_ROOT}/projects/chirality-app-dev/frontend && \
REPO_ROOT={REPO_ROOT} RUN_ROOT=<scratch>/s8-run-head PORT=51840 SKIP_BUILD=1 WITH_RELEASE_QUALITY=1 \
APPROVED_BY=claude-fable-5-1-nodeH APPROVAL_REF=APPDEV_V3_NODE_H_2026-09-03 \
bash <this folder>/rerun-section8-local.sh
```

Two host facts the method had to absorb (both recorded in the script header and verified by the probe logs under `probe/`):

1. **Absent-runtime-daemon-bindings class explained.** Every prior local premerge (Receipts 172/177; nodes A and B on 2026-09-03) failed with `HTTP 503` on all session routes because nothing performed the daemon start / project registration / env binding that CI performs; `src/lib/runtime-client/daemon-harness-port.ts` answers `ENGINE_UNAVAILABLE 503` when the `CHIRALITY_RUNTIME_*` variables are unset. Performing the lifecycle removes the class; no product change is involved.
2. **Keychain block in the development Electron binary** (probe runner and per-log invocations in `probe/RUNNER.md`). With the lifecycle in place, the first `session/create` still hung for the route's 30 s budget and wedged the daemon: `CompatibilitySessionPolicy.resolve` calls `credentials.status("anthropic")` → `safeStorage.isEncryptionAvailable()`, which the unsigned `Electron.app` blocks on inside the macOS Keychain "Safe Storage" item — a prompt a headless daemon cannot show. `probe/safe-storage-probe.js` reproduces it in isolation: it hangs both inside the session sandbox and under sandbox escalation (`probe/safe-storage-probe.escalated.log`: SIGKILL after 20 s), and returns `isEncryptionAvailable=true in 1ms` with Chromium's `--use-mock-keychain` (`probe/safe-storage-probe.mock-keychain.sandbox.log`). The disposable evidence daemon is therefore started with `--use-mock-keychain`. This is a test-harness switch consumed by Chromium, not a product change; it keeps the evidence class identical to CI's Linux runner (no real keychain there either) and guarantees the evidence daemon never touches the operator's Keychain.

## 3. Result at HEAD `e59efa483` (retained run `run-head-e59efa483/`)

| Surface | Result | Bytes |
|---|---|---|
| `npm run harness:validate:premerge` | exit 0; `HARNESS_PREMERGE_STATUS=pass`, `HARNESS_PREMERGE_TEST_COUNT=8`, `HARNESS_PREMERGE_SECTION9_STATUS=pass` (16, report-only) | `logs/premerge.stdout.log`, `logs/premerge.machine-lines.txt` |
| Stable Section 8 artifact `frontend/artifacts/harness/section8/latest/summary.json` | written by the wrapper; `status: pass`, `testCount: 8`, `stagedFromInstructionRoot: false`; all eight rows `pass` | `artifacts/stable/section8-latest-summary.json` (SHA-256 `386a0f189fa720fc48fccbad6ad85f09ca7fce90bd34e1e19fe175a3088dfea8`); the copy rewritten by the release-quality wrapper's second premerge, `…after-release-quality.json` |
| Section 8 run tree (per-check API captures, SSE captures, per-check logs, session cleanup) | 7 sessions created and all 7 deleted (`cleanup/sessions.json`: `cleanupFailures: []`) | `artifacts/section8-run/**` |
| `npm run validate:release-quality` | exit 0; `RELEASE_QUALITY_STATUS=pass`; `full_test` pass (Vitest 162 files / 1489 tests passed, 4 skipped), `typecheck` pass, `section9` pass, `premerge` pass; `summaryConsistency` pass (`summary.section8` and `summary.section9` both pass with no errors) | `artifacts/release-quality/summary.json` (`97c9e7ce…`) and `logs/*` |
| Boot-error taxonomy detail (shared-runtime mode) | `SESSION_NOT_FOUND` (404) · unknown persona `SDK_FAILURE` (400, create phase) · `BOOT_CONFORMANT` (200) · `WORKING_ROOT_INACCESSIBLE` (404, registered-project containment) | `artifacts/section8-run/api/section8.boot_error_taxonomy.json` |

Row-level behaviour projection (as printed by `compare-section8-summaries.py`):

```
setup.server_reachable               pass  {"httpStatus": 200}
regression.session_crud              pass  {"listedCount": 1}
section8.boot_error_taxonomy         pass  {"checkedCodes": ["SESSION_NOT_FOUND","SDK_FAILURE","BOOT_CONFORMANT","WORKING_ROOT_INACCESSIBLE"]}
section8.smoke_stream                pass  {"eventCount": 8}
section8.session_persistence_resume  pass  {"adapterId": "stub", "providerId": "stub"}
section8.permissions_dontask         pass  {"allowEvents": 9, "denyEvents": 7}
section8.interrupt_sigint            pass  {"interruptStatus": 200}
section8.sdk_native_stream           pass  {"eventCount": 8}
```

## 4. Preservation proof — three independent sources agree

`compare-section8-summaries.py` projects a summary onto its behaviour-bearing fields (IDs in order, statuses, `details` minus per-run `sessionId`/`engineSessionId`, overall status, `testCount`, `stagedFromInstructionRoot`) and asserts the required-ID / legacy-ID contract. Over the sources below it prints `BEHAVIOUR_PROJECTIONS_EQUAL=true` with exit 0 (`COMPARE_RESULT.txt`):

| Source | Commit under test | Produced by | Bytes |
|---|---|---|---|
| Local run at HEAD (this method) | `e59efa483` | this run, 2026-09-04T01:35:56Z | `run-head-e59efa483/artifacts/stable/section8-latest-summary.json` |
| Local run at the pre-landing basis (same method, second scratch worktree) | `0c683fb16` | this run — see §5 | `run-base-0c683fb16/artifacts/stable/section8-latest-summary.json` |
| CI `harness-validation-summaries`, PR #681 (pre-landing seating candidate) | run 33800866263, head `974b05374`, 2026-09-03T20:12Z, success | GitHub Actions (`ubuntu-latest`, xvfb daemon) | `ci-artifacts/pr681/section8/latest/summary.json` (`2bd0210d…`) |
| CI `harness-validation-summaries`, PR #686 (post-landing node A) | run 33823453656, head `78a4c526d`, 2026-09-04T00:51Z, success | GitHub Actions | `ci-artifacts/pr686/section8/latest/summary.json` (`a249ab1e…`) |

The CI summaries are corroboration from an independent host class; the local A/B is the recomputable proof (same evaluator bytes, same method, two commits, one machine).

Round 2 (review-1 remediation) added a premerge-only run of the corrected script — `run-head-e59efa483-round2/` (executed in the working tree checked out at the round-1 evidence commit `021e1f186`, whose product bytes are identical to `e59efa483`: the only paths between them are under the two evidence roots, and its `built-bundles.sha256` equals `run-head-e59efa483/`'s; port 51842; stable summary `50391877…`; its script-written per-run manifest verifies) — and `COMPARE_RESULT_round2.txt`, the five-way comparison including it: `BEHAVIOUR_PROJECTIONS_EQUAL=true`, exit 0. `COMPARE_RESULT.txt` remains the four-way result as reviewed (regenerated with the strengthened comparator; byte-identical).

## 5. Pre-landing baseline run at `0c683fb16` (`run-base-0c683fb16/`)

The same script, same host, same toolchain, second scratch worktree checked out detached at `0c683fb1657706316272951e4c3a0f7781b46009` with its own `runtime/` build and `frontend/` install (`SKIP_BUILD=1` after `npm run build:electron`; `PORT=51841`; `WITH_RELEASE_QUALITY=0` — the release-quality wrapper is HEAD's registered gate, the A/B needs only the Section 8 bytes).

| Surface | Result | Bytes |
|---|---|---|
| `npm run harness:validate:premerge` at `0c683fb16` | exit 0; `HARNESS_PREMERGE_STATUS=pass`, `HARNESS_PREMERGE_TEST_COUNT=8`, `HARNESS_PREMERGE_SECTION9_STATUS=pass` | `run-base-0c683fb16/logs/premerge.*` |
| Stable Section 8 artifact | `status: pass`, `testCount: 8`, eight `pass` rows, generated 2026-09-04T01:43:35Z | `run-base-0c683fb16/artifacts/stable/section8-latest-summary.json` (SHA-256 `a59a1549af861c91fd1966e0174fd9cff21d3e4eaebccf282eefa4031461a77b`) |
| Built evaluator bundles at the basis | `dist-electron/main.js` `7dd517da…` (differs from HEAD's `4d56cc6f…` — the Electron host itself changed in PRs 684/686; that is the point of the A/B), `dist-runtime/chirality-cli.mjs` `0503c40a…` (identical to HEAD) | `run-base-0c683fb16/logs/built-bundles.sha256` |
| Sessions / containment / cleanup | 7 created, 7 deleted, no failures; Electron daemon with no TCP socket; 0600 socket; teardown and cleanup all `yes`; checkout clean before and after (`git_status_after=0 dirty paths`) | `run-base-0c683fb16/{artifacts/section8-run/cleanup,logs}` |

Four-way comparator result (`COMPARE_RESULT.txt`, exit 0): `BEHAVIOUR_PROJECTIONS_EQUAL=true` over HEAD-local, basis-local, CI PR #681, CI PR #686. Per-row durations differ run to run (all within ±60 ms here) and are excluded from the projection by design.

## 6. RQG §13 Shared Runtime Gate — rows this deliverable owns

`docs/RELEASE_QUALITY_GATES.md` §13 lists six proofs before SCA-APP-003 closeout and states the gate is validation evidence only. DEL-09-01 owns the Section 8 contribution; the mapping below names, per bullet, exactly what this bundle contributes and what it does not.

| §13 bullet | DEL-09-01 contribution in this bundle | Not covered here (owner) |
|---|---|---|
| runtime-package promotion preserves current Claude/stub/Pi behavior | **stub path preserved**: the eight Section 8 rows pass through the daemon-bound session routes with `adapterId: stub`, `providerId: stub`, and the projection is identical at `0c683fb16`, `e59efa483`, and in both CI runs (§4) | Claude and Pi behaviour (live-provider proofs belong to DEL-04-05 / DEL-05-0x and the D-APP-72 exception carrier); no live credential was used or preserved |
| Desktop and CLI use one daemon, session store, lock system, credential owner, and interruption state | **one daemon, exercised by two public clients**: the bundled CLI registered the project (`registration.redacted.json`), the Desktop-side Next routes served every Section 8 request through the same socket, and `section8.interrupt_sigint` drove the daemon's interruption state (`interruptStatus: 200`, `process:exit` with `interrupted: true`, exit code 130 — `artifacts/section8-run/sse/section8.interrupt_sigint.sse`) | turn-lock contention and restart-recovery (Vitest `runtime-desktop-cli-shared-daemon.integration.test.ts`, passing inside `full_test`; owned by DEL-05-0x) |
| control plane has correct Unix-socket permissions, project-scoped authorization, stale recovery, and no TCP listener | **observed on the live daemon** (`logs/containment-before.txt`, `containment-after.txt`): control socket `srw-------` (0600), runtime dir `drwx------` (0700), the Electron daemon process holds only the Unix control socket and **no TCP socket before or after the run**; the only TCP listener on the host port is the `next dev` server; project-scoped authorization exercised by `WORKING_ROOT_INACCESSIBLE` for an unregistered root (`section8.boot_error_taxonomy`) | stale-socket recovery (not exercised; owned by the daemon package tests) |
| model switching obeys explicit activation, drain, timeout, no-force, `NO_MODEL`, no-helper-unload, no-fallback rules | none — outside Section 8 | DEL-05-0x / residency carriers |
| app-dev and PEC pilot paths pass with canonical evidence and actual-model attribution | **app-dev path, stub attribution**: `section8.session_persistence_resume` records `adapterId`/`providerId`/`model` in `session:init` and in the persisted record (`artifacts/section8-run/api/section8.session_persistence_resume.json`) | PEC pilot path; live-model attribution |
| public export includes only generic runtime/CLI/contracts/safe adapters and excludes credentials, machine state, private adapters | none — outside Section 8 | DEL-09-05 (export boundary) |

## 7. Containment, secrets, and cleanup proof

- **No credential, token, or account material preserved.** The daemon's operator and project tokens lived only under the disposable user-data root; `registration.redacted.json` retains the token-file *path* and the manifest hash only (the raw registration JSON was written to `RUN_ROOT/private/`, which the script deletes — `logs/cleanup.txt: private_dir_removed=yes`). A pattern scan of every retained byte for `sk-ant`, bearer strings, and `"token":` fields found nothing.
- **Operator state untouched.** Disposable `--user-data-dir` under `/private/tmp/chirality-s8.*` (short path: macOS caps Unix socket paths at 104 bytes); `--use-mock-keychain`; the unpackaged daemon installs no LaunchAgent (`electron/main.ts` `initializeDaemon`, `app.isPackaged === false` branch). The operator's real daemon, `userData`, and Keychain were never addressed.
- **Checkout untouched.** `logs/git-status-before.txt` / `git-status-after.txt` are identical (the three paths are this tranche's own edits). Writes inside `frontend/` were confined to the gitignored `artifacts/harness/**` and `.chirality/sessions/` (A1 re-stage declaration in `STEP0_DISCOVERY.md` §3 covers them).
- **Teardown and cleanup** (`logs/teardown.txt`, `logs/cleanup.txt`): daemon process tree remaining 0; dev server stopped; socket absent; no listener on the port; user-data root removed; harness tmp root removed. Not removed, by design and declared: the gitignored `frontend/artifacts/harness/**` (the deliverable surface) and `frontend/.chirality/sessions` (required at registration) — the current script writes a `checkout_leftovers=` line naming them in `cleanup.txt`; the two round-1 retained runs predate that line, `run-head-e59efa483-round2/` carries it. The first (pre-`--use-mock-keychain`) attempt showed that a daemon wedged on the Keychain call ignores SIGTERM, so the script escalates to SIGKILL for processes under the disposable root and for the dev server it started (by pid and children — never a foreign listener; the script now refuses to start on an occupied port), and only removes a user-data root it created itself.
- **Sorted manifests.** `run-head-e59efa483/MANIFEST.sha256` and `run-base-0c683fb16/MANIFEST.sha256` cover `artifacts/**` and `logs/**` (`LC_ALL=C` sorted; recompute with `shasum -a 256 -c` from inside each run folder) and are themselves pinned by the bundle-level `MANIFEST.sha256` in this folder (recompute from this folder). Provenance note (review round 1, H1-F1): the script originally wrote the per-run manifest before its EXIT-trap teardown appended the final lines to `driver.log`/`daemon.log`/`next-dev.log` and created `teardown.txt`/`cleanup.txt`, so the shipped per-run manifests failed verification on three logs and omitted the two teardown files; the script now writes the per-run manifest as the last act of teardown, and both retained per-run manifests were regenerated from the unchanged retained bytes (no rerun). The bundle manifest pinned every byte throughout.
- **Host-identifying strings in retained bytes.** Logs, machine lines, lsof rows, and the summaries' `projectRoot` carry the absolute scratch-worktree path (which embeds `-Users-ryan-`) and the local username in `lsof` output; the launch brief carries `REPO=/Users/ryan/dev/chirality` verbatim. Nothing else host-identifying and no credential, token, or account material is present.
- **Raw bytes retained, not normalised.** Captured SSE streams end in the blank line that terminates their last event and captured stdout/stderr logs end however the producing command ended them; `git diff --check` would flag those as whitespace errors. Rather than rewrite evidence bytes (which would invalidate the per-run manifests), the folder-local `.gitattributes` exempts exactly `*.sse` and `*.log` from the whitespace check. Authored files in this bundle keep the default rules and are clean.

## 8. What was and was not proven

- Proven: the Section 8 stable premerge summary is producible on this host from `main` at `e59efa483` with `status: pass` and the accepted ID set; its behaviour projection equals the pre-landing basis and both CI runs; the evaluator bytes are unchanged across the four landings; the release-quality wrapper passes end-to-end on the same daemon; the daemon exposes no TCP listener and a 0600 control socket.
- Not proven, and not claimed: any live-provider (Anthropic/Pi) behaviour; packaged-app behaviour (the daemon here is the unpackaged development bundle, as in CI); G5 fan-in acceptance; anything under F-APP-2. The `--use-mock-keychain` switch means the *real* Keychain path of `safeStorage` is not exercised by this evidence — that path is DEL-04-05's typed-state evidence and node A's packaged proof, not Section 8.
- Premerge classification for the registered check: **PASS (local, daemon-bound)** — not the `FAIL_DEFERRED_TO_PR_CI` class, which this method resolves rather than defers. PR CI remains additional evidence and will rerun on the PR.

## 9. Next revision trigger

This item is revised after each v3 landing and removed only at G5 fan-in (`_STATUS.md` `Removed when`). The next revision is owed after the next merged v3 product change on `main` that touches `frontend/src/app/api/harness/**`, `frontend/src/lib/harness/**`, `frontend/src/lib/runtime-client/**`, `frontend/electron/**`, `runtime/**`, or the evaluator surfaces listed in `EVALUATOR_BYTES.tsv`; rerun `rerun-section8-local.sh` at the new `main` commit and add the run folder plus a `COMPARE_RESULT` line to this bundle.
