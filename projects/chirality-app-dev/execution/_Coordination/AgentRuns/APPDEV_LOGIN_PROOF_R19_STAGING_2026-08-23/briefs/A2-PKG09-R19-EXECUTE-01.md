# A2-PKG09-R19-EXECUTE-01 sealed brief

Status: `FROZEN`

## Identity

- RequestedBy: `WI-PKG09-R19-STAGING-01` / WORKING_ITEMS
- RunID: `APPDEV_LOGIN_PROOF_R19_STAGING_2026-08-23`
- ChildInstanceID: `A2-PKG09-R19-EXECUTE-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- Form: fresh ephemeral generalist Agent 2; no delegation

## One bounded objective

Execute the owner-directed exact-basis R19 tranche serially: verify the pinned
Electron supply, run exactly one no-network unsigned package build, verify the
package, run exactly one direct disposable packaged-daemon health precheck and
clean it, stage but do not execute the R19 owner procedure, update DEL status,
run proportional validation including the retained diagnostic/cure pair, and
freeze a complete executor return for fresh review.

## Accepted basis and concrete values

- HEAD/build revision:
  `d6861ae8251e2a81078577d4496e949735ff199d`
- frontend tree: `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`
- branch: `codex/app-login-proof-r19-staging`
- app path:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- proof root: `/private/tmp/ch-r18-91499728-51dd`
- runtime user data:
  `/private/tmp/ch-r18-91499728-51dd/runtime-data`
- exact 67-byte socket:
  `/private/tmp/ch-r18-91499728-51dd/runtime-data/runtime/control.sock`
- label:
  `com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b`
- plist:
  `/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b.plist`
- service:
  `gui/501/com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b`
- public destination:
  `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r19-3951dfe9-ec03-421b-b376-fd5f0d96992b-public-evidence`

## Declared reads

Read current WORKING_ITEMS/App/loop instructions, DEL status R16-R18,
Receipt 189, R17 source/tests, R18 verifier/wrapper/tests/evidence, packaging
and validation docs, runtime CLI/daemon sources, `CHAT_TRANSCRIPTION.md`, this
brief, and current Git state. Do not read/traverse the Desktop R16 failed
evidence or private R16 proof root. Do not query any default operator job,
plist, or launcher.

## Allowed writes

- generated ignored package/build/instruction-root artifacts under
  `projects/chirality-app-dev/frontend/{dist,dist-electron,.next,artifacts}/`
- new R19 record only under DEL-09-04 `_run_records/`
- minimal DEL-09-04 `_STATUS.md` update
- only this instance's `executor/` evidence and return

No product source, test, package manifest/lock, R16-R18, Receipt 190, shared
run-root plan/graph/transcription, or other deliverable path may be changed.

## Required execution sequence

1. Reverify exact HEAD, branch, frontend tree, clean tracked/index state, no
   in-progress Git operation, initial root/plist/public-destination absence and
   non-symlink posture, and exact service launchctl exit 113 plus exact
   label-specific two-line not-found output. Record that `origin/main` is newer
   but do not sync. Fail closed on any other dirt or collision.
2. From exact frontend cwd run `npm run electron:supply-chain` exactly once.
   Require exit 0 and stdout containing only the exact verified directory;
   freeze stdout/stderr/exit/hashes.
3. Initialize prebuild inventory, full log, and exit evidence, then from exact
   frontend cwd run `npm run desktop:pack` exactly once in the ordinary
   network-denied sandbox without escalation or retry. Require exit 0, exact
   custom-electronDist line, no case-insensitive download/GitHub/
   release-assets indicator, embedded dependency and instruction-root PASS,
   and exact build Git SHA. This overwrites/supersedes R18's ignored evidence
   build and is the R19 staged package.
4. Verify without modifying the package: Info.plist bundle ID, short/bundle
   version, minimum macOS, main executable/name/mode/arm64, codesign ad-hoc/
   linker-only/no team posture and calibrated strict diagnostic, main SHA-256,
   packaged runtime CLI presence/readability/mode/SHA-256, instruction-root
   summary/manifest exact commit/current bytes, empty frontend diff-stat from
   the build revision and clean scoped frontend porcelain. Deterministically
   prove the packaged runtime contains the committed R17 overlong-socket guard
   using bounded asar/module/string evidence; do not alter package bytes.
5. Run the empirical precheck exactly once, only after proving the proof root
   absent. Start the exact packaged main executable with `--runtime-daemon`,
   exact `CHIRALITY_USER_DATA` above, `CHIRALITY_SKIP_CLI_LAUNCHER=1`, and
   daemon GUI spawning disabled. This is direct product execution, never a GUI
   or LaunchAgent action. Local Unix/loopback socket permission may be obtained
   through an exact execution-tool escalation; no external network request or
   network tool is permitted. Freeze executable, argv, env names/values, PID,
   logs, and timestamps. Require the exact path to be a Unix socket, byte count
   67, packaged CLI/authenticated local control health (use a non-LaunchAgent
   CLI action such as `project list --json`, not `daemon status`), and matching
   process/executable identity. Gracefully terminate, boundedly wait, verify
   process/socket absent, remove only the exact runtime-data and then exact
   empty root, and verify root absent. Install a fail-safe cleanup trap scoped
   only to that exact PID/root. No retry; on failure clean only that exact
   disposable state and stop for manager review.
6. Only after empirical cleanup, author new
   `R19_OFFLINE_EXACT_MERGE_BUILD_AND_LOGIN_PROOF_STAGING_2026-08-23.md` and
   minimally update `_STATUS.md`. Preserve exact facts and claim calibration:
   DEL remains `IN_PROGRESS`/unproved; R19 is staged documentation only; no
   procedure/proof/lifecycle/release act. Record exact build/package/precheck
   evidence and that `origin/main` advanced without an unauthorized sync.
7. R19 must provide independently copy-paste-safe blocks. Every block starts
   with the exact repo-root `cd` and `set -euo pipefail` for a fresh Terminal
   tab. Step 0 declares exact app/executable/hash/revision/root/label/plist/
   service/public destination; verifies toplevel, app/executable/hash, empty
   frontend diff from revision (never current HEAD equality), root/plist/public
   absence, launchctl exit 113 and exact two-line label-specific not-found
   text; computes, prints, and enforces socket UTF-8 bytes exactly 67 and max
   103; runs optionless read-only preflight; and verifies unchanged absences.
   Then include prepare, exact PREPARED/proofClaimed false/revision check, one
   owner logout/login instruction only after success, capture, PASS/revision
   check, preservation of exactly prepared/summary/evidence-package as 0600 in
   a new 0700 public directory with private state excluded, and a handoff block
   printing all three hashes and an exact owner message. Explicitly forbid
   manual app open, bootstrap/kickstart, continuing after errors, and execution
   of any block in this tranche. Verify procedure shell syntax/portability,
   including simulated later docs-only HEAD behavior without changing live Git.
8. After content records freeze, run ordinary sandboxed exact `npm test` once
   and preserve the diagnostic. Freeze source/test/package hashes and complete
   candidate diff, then run exact `npm test` once with execution-tool elevation
   restricted in purpose to local loopback/Unix-socket test binding and no
   external network. Preserve complete log/exit/counts and prove pre/post
   hashes/diff identical. Do not run either full suite again.
9. Run syntax and relevant focused tests, typecheck, optionless live read-only
   preflight with exact absence before/after, APP-HOLD scan, repository
   self-check, practitioner pytest, prior-ledger receipt validator, package/
   integrity checks, JSON parsing, new-file/staged-equivalent whitespace,
   `git diff --check`, App-only containment, complete inventory, and empty
   index. Do not run another pack or empirical precheck.
10. Freeze `executor/RETURN.md` with exact paths, hashes, command counts,
    identities, test results, cleanup, skipped/future PR-CI evidence, blockers,
    and derivative status. Do not modify final bytes after return.

## Failure and fences

Fail closed on supply/cache/build/package/precheck/cleanup/uniqueness errors.
Never fetch or retry pack/precheck; never prepare/capture/logout/login; never
open GUI; never install/query/mutate default operator LaunchAgent/plist/
launcher; never touch the private R16 root/Desktop failure evidence; never
sign/notarize/deploy/distribute/publish or claim release readiness; never write
Receipt 190, stage, commit, push, PR, merge, or delegate.
