# Daemon-as-Service Tranche Handoff State

Status: `APPDEV_DAEMON_SERVICE_IMPLEMENTATION_COMPLETE_PENDING_PR_AND_OWNER_MERGE`

Run: `APPDEV_DAEMON_SERVICE_2026-07-25`
Branch: `feat/daemon-service` (off `main` @ `e9068c87d76c75b133f3686db8bf453565ce8fa2`)
Date: 2026-07-25

Terminal state of this run: all code and evidence commits are landed on the
branch, the round-2 remediation of every Stage V finding is measured on the
packaged app, and the closeout records are written. Opening the pull request is
Agent 0's next act; the owner's merge is the terminal integration act. This file
is a handoff state, not a lifecycle decision, a release-readiness claim, a
certification, or a professional approval.

## Accepted upstream basis

- `ADOPTED_BRIEF.md` — `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`, adopted by owner
  direction in-session 2026-07-25 ("draft the brief and proceed using the same
  subagent delegation model established in this session (Agent 0/1/2 as
  appropriate, `opus-5` models for Agent 1/2)"), **read together with its
  appended `## Corrections` section**. Correction C-1 replaces the brief's root
  cause #2; the original text is preserved as adopted but is not the record of
  the defect.
- **The accepted tree is the round-2 tree**: branch commits `8c20f214d`,
  `22752cf67`, `987541fed`, `071bebf9e`, `ee2154976`, `c3616aa69`, `3e7e57e04`,
  `45aeaa465`. Every gate figure and drill result of record was measured against
  the pack built from `3e7e57e04`'s tree. Round-1 measurements
  (`071bebf9e` tree) are superseded where round 2 re-measured them and are
  retained only as the "before" column.
- Parent run: `APPDEV_WOVEN_REDESIGN_2026-07-24` (PR #330, merged at
  `e9068c87d`), whose DEL-02-01 residuals this tranche was raised against.
- Prior receipt basis: `Receipt-90`.

## Derivative-package status

Everything below is derivative of that accepted basis and cites it; none of it is
decomposition truth or an authoritative snapshot.

- **Stage returns** — `instances/{A-DAEMON-SERVICE,B-PACKAGING,V-PACKAGED-DRILLS}/RETURN.md`
  with their sealed `LAUNCH_BRIEF.md` files.
- **Validation rounds** — `instances/AGENT1-VALIDATOR/ROUND1_REVIEW.md` (with its
  appended correction retracting the §3 quit-veto approval) and
  `ROUND2_REVIEW.md`.
- **Drill evidence** — `instances/V-PACKAGED-DRILLS/evidence/` (drills V0–V9,
  cleanup, owner-state before/after, retained drivers) and
  `instances/AGENT1-VALIDATOR/ROUND2_DRILLS/evidence/` (`d1`–`d6`, including the
  recording `launchctl` trace and the three-arm fork/stop-path experiment).
- **This run's closeout records** — `_run_records/R7_DAEMON_SERVICE_2026-07-25.md`
  (DEL-02-01), `R6_DAEMON_SERVICE_2026-07-25.md` (DEL-02-05),
  `R2_DAEMON_SERVICE_2026-07-25.md` (DEL-05-04),
  `R6_DAEMON_SERVICE_2026-07-25.md` (DEL-09-04), the updated `## Remaining` and
  `## History` sections in those four `_STATUS.md` files, the
  `plans/PLAN_COMPLETION_LOG.md` entry dated 2026-07-25, and `Receipt-91` in
  `loop/LOOP_RECEIPTS.md`.

On any disagreement, the adopted brief (with its corrections) and the instance
returns govern over these derivative summaries.

## Closure verdict

Implementation complete; every Stage V finding remediated and re-measured;
records written; pull request and owner merge pending.

- The owner-reported symptoms are falsified on the packed app: an end-to-end
  stub-adapter turn completed through the packaged GUI's harness surface, and the
  quincunx ships as the in-app mark, the Dock tile and the Finder icon.
- Six Stage V findings (V-D1…V-D6) plus one minor renderer-channel throw are
  fixed, each with an after-measurement on the packaged app.
- A defect introduced during remediation — a fork that silently broke the
  daemon's own stop path — was caught inside the round by re-checking the stop
  path rather than trusting a passing drill, and is recorded in
  `ROUND2_REVIEW.md` §2 rather than smoothed over.
- No lifecycle state changed. All four affected deliverables remain
  `IN_PROGRESS` with `Authorization Basis`, `Directive` and
  `Checking Approval SHA` untouched.
- Fences held: no provider or network expansion (the icns is generated offline
  and electron-builder never fetched its icon toolset), no signing/notarization
  or release claim, no `_DomainEngines`/piping writes, no issuance. Write scope
  stayed inside `projects/chirality-app-dev/**` plus the generic
  `runtime/packages/cli/**` changes required by D-GOV-20 parameterization.
- Owner live-state isolation held in both rounds: the real LaunchAgent, the real
  user data, `~/.local/bin/chirality`, and the owner's main checkout were
  verified byte-unchanged after cleanup.

## Rerun requirements

- **CI harness pre-merge on the pull request.** `validate:release-quality` is
  `pass_with_skips` with the documented evidence-skip reason; the Section 8
  premerge row is unsatisfied locally and is owed from CI on the PR. It is a
  residual, not a satisfied gate.
- **Repository self-check after merging `main`.** The branch is behind `main`,
  and upstream commits touch `tools/practitioner_harness/`, so the recorded
  self-check result is valid only for the pre-merge tree. No file-level overlap
  between the two ranges was found at round 1; re-derive before relying on it.
- **Runtime workspace build output must be rebuilt** after the runtime package
  changes for the frontend typecheck to resolve its workspace aliases. The output
  stays ignored and uncommitted.
- **Post-merge owner-machine deployment** (owner decision gate 3): re-run
  `daemon install` from a rebuilt app or the rebuilt CLI, since an
  earlier-installed plist keeps the crash-only restart contract and carries no
  pinned environment. Not performed by any stage of this run — the owner's live
  machine state was out of write scope for every stage including the drills.
- **No governed authority document was edited by this run**, so no corpus bump
  was required; the authority-corpus status was verified clean before and after
  the record edits.

## Remaining blockers

1. **Pull request not yet opened; owner merge outstanding.** The PR is Agent 0's
   act immediately after `Receipt-91`; the merge is the owner's.
2. **Named residuals, each recorded against its owning deliverable:**
   - daemon helper-bundle identity — activation policy does not stop
     LaunchServices resolving a launch against the running daemon, so a
     Finder/Dock open while the daemon runs bounces the runtime briefly;
     escalated to the owner as its own tranche (DEL-09-04, cross-referenced from
     DEL-02-01);
   - SIGKILL leaves a stale control socket, recovered on the next daemon start by
     the owner-record pid liveness check, refusing rather than replacing a live
     or ambiguous owner (DEL-09-04);
   - release-quality premerge row unsatisfied for this branch, owed from CI on
     the PR (DEL-09-04, cross-referencing DEL-09-01 and DEL-09-05);
   - post-merge owner-machine deployment steps (DEL-09-04);
   - packaged-daemon instruction-root divergence, pre-existing and deliberately
     unaddressed (DEL-09-04);
   - login-time `RunAtLoad` never exercised, because the drill plist deliberately
     lived outside `~/Library/LaunchAgents` (DEL-09-04, folded into the narrowed
     first item);
   - no operator reconnect affordance on the connectivity chip (DEL-02-01);
   - `metadata.icons` file-convention substitution — record-only, no code owed
     (DEL-02-01, retained);
   - packaged Desktop evidence for the Workbench and Pipeline surfaces
     (DEL-02-02) and for the navigator recorded-session selection path
     (DEL-08-02) — unchanged by this tranche and still owed;
   - replay transcript-item rendering against a real daemon session — still
     unevidenced, though daemon unavailability no longer blocks it (DEL-05-04).

## Notes carried for the receiving agent

- **`docs/PRD.md` KG-033 is now partly stale and was deliberately not edited.**
  Its narrowed residual list still names the runtime-connectivity indicator and
  the packaged application icon, both of which this tranche closed. Editing the
  PRD triggers D-APP-38 corpus reconciliation (bump + apply across the
  deliverable reference rows); that was outside this record pass's scope and is
  recommended as a follow-on, whether folded into this PR by Agent 0 or taken as
  its own tranche.
- **Read the corrections, not the original claims.** Two accepted statements were
  falsified during the run: the brief's root cause #2 (corrected by C-1 — a wrong
  restart contract, not a missing plist key) and `ROUND1_REVIEW.md` §3's approval
  of the quit veto (retracted in its appended correction — the JS signal handler
  never runs in a packaged Electron main process). Anyone quoting either source
  must quote the correction.
- The `activate` handler becomes dead code the day the daemon gets its own bundle
  identity, and can be deleted then.
- New environment surfaces are documented in code: keep-alive, run-at-load and
  throttle-interval overrides, LaunchAgent label override, user-data override,
  daemon activation-policy override, CLI-launcher opt-out, and the daemon
  GUI-spawn control arm used as a drill control.
- Retained drill tooling is part of the method record and is reusable: the
  isolated LaunchAgent driver with its label and path refusal guards, the
  isolated runtime-client driver, the window-list helper, and the recording
  `launchctl` shim technique that proves label scoping with zero risk to the
  operator's job.
- Pre-existing and not introduced here: the instruction-root integrity
  `sourceCompleteness` remediation flag for an unrelated examples set, and the
  standing repository self-check review/warning findings outside this tranche's
  paths.
