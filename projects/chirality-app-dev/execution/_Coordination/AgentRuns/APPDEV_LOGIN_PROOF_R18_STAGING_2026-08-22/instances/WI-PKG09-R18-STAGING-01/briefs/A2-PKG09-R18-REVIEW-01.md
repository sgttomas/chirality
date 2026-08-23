# Sealed brief — A2-PKG09-R18-REVIEW-01

## Identity and objective

- RequestedBy / Parent: `WI-PKG09-R18-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R18-REVIEW-01`
- Fresh ephemeral generalist Agent 2; evidence-only; no delegation
- Basis: branch HEAD
  `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d` with exact two parents recorded
  in v4, plus frozen uncommitted candidate named by
  `MANAGER_CANDIDATE_FREEZE_V4.md`.
- Objective: independently review the complete R18 supply-freeze candidate,
  owner gates, evidence, validation limitation, security, and containment.

## Reads, writes, and prohibitions

Read current agent/App loop/profile instructions; all v1-v4 plans/graphs/
amendments/briefs/returns; attempts 1/2 and network-3 evidence; official
SHASUMS body; accepted sync; candidate source/tests/package/R18/status;
packaging docs; active nested/top-level `@electron/get`; executor-4 evidence;
Git state and owner-staged archive read-only.

Write only
`instances/WI-PKG09-R18-STAGING-01/review-1/REVIEW.md` and bounded review logs
in the same directory. Do not change candidate/manager/executor/deliverable
bytes. No network, package/build command, artifact download, proof act,
operator action, Receipt 189, stage/commit/push/PR/merge, or delegation.

## Required review matrix

1. Verify exact merge HEAD/parents/current origin/main and App-only candidate/
   clean index; verify frozen content hashes and exact path inventory.
2. Verify attempts 1/2 preserved and calibrated; network-3 exact one-invocation
   two-host 302/200 chain, 7,610-byte/full-body hash, official line once,
   sanitized headers/no signed query, no artifact/other host.
3. Independently verify owner-staged archive regular/non-symlink, exact size/
   hash; no mutation.
4. Verify active Electron Builder nested `@electron/get` is exactly 3.1.0 and
   local source hash/lines prove fresh SHASUMS with Bypass; top-level 5.0.0 is
   correctly excluded.
5. Security-review verifier: production pins/official line/URL/version drift,
   literal env/default home resolution, empty/NUL/relative/non-normalized/root,
   lstat/realpath containment, directory/archive symlink and regular-file
   rules, exact size, streaming hash, stdout-only success/stderr failure, no
   CLI or caller bypass of production pins. Treat exported test seams as
   actionable if they can weaken the production CLI/wrapper.
6. Security-review pack wrapper and package scripts: no shell, spaces remain
   one arg, exactly one `-c.electronDist=<verified dir>`, correct builder
   resolution, preserved build/dependency/instruction-root gates and
   `desktop:pack` name, unchanged `desktop:dist`, no lock drift.
7. Independently run syntax, focused tests, typecheck, production verifier,
   package/lock consistency, instruction-root, APP-HOLD, self-check,
   practitioner suite, receipt validator, candidate whitespace/new-file
   no-index checks, `git diff --check`, containment, and empty index.
8. Run full frontend Vitest once only in ordinary network-denied sandbox. Save
   complete output. List exact 21 failing test names/files/errors if reproduced;
   compare each to prior known local TCP/Unix-socket bind restriction and
   determine whether every failure is unrelated environment-only. Do not call
   this suite PASS, do not rerun outside the boundary, and do not conflate an
   actionable candidate regression with EPERM.
9. Verify executor-4 made exactly one post-implementation pack attempt, exit
   zero, full log hash, custom electronDist, no download/GitHub indicator,
   embedded gates and synchronized Git SHA. Do not rerun package. Verify build
   and observed package hashes are evidence-only/non-adopted.
10. Verify R18/status accurately cover cause, attempts, official evidence,
    sync, implementation/tests/build, local-bind limitation, R17 merged,
    `IN_PROGRESS`/unproved, R19 separate, no owner procedure/proof acceptance.
11. Verify no network after attempt 3; no second pack; no R19/GUI/prepare/
    capture/logout/login/bootstrap/kickstart/operator/default job action,
    signing/notarization/deployment/distribution/release claim, receipt or Git
    integration.

## Verdict

Return `VALIDATED_PASS_WITH_ENVIRONMENT_LIMITATION` only if no actionable
finding exists and every full-suite failure is proven environment-only;
preserve the suite as not PASS. Otherwise return actionable findings with
file/line/evidence and hold only this node for repair cycle 1. Include exact
review/log hashes, checks, changed paths, and rerun requirements.
