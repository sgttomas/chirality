# LAUNCH BRIEF — Agent 2 "RECORDS" (verbatim copy of dispatch prompt)

Run: TRB-APPDEV-DAEMON-SERVICE-2026-07-25
Instance: RECORDS
Model: opus-5
Worktree: /Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76
Branch: feat/daemon-service (HEAD ~45aeaa465)

---

You are Agent 2 "RECORDS" (opus) under TRB-APPDEV-DAEMON-SERVICE-2026-07-25. Work in /Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76, branch feat/daemon-service (HEAD ~45aeaa465). Copy this prompt to projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/instances/RECORDS/LAUNCH_BRIEF.md first.

CONTEXT: Read (1) ADOPTED_BRIEF.md incl. its Corrections section, (2) instances/*/RETURN.md (A, B, V), (3) instances/AGENT1-VALIDATOR/ROUND1_REVIEW.md + ROUND2_REVIEW.md. The tranche is code-complete: daemon-as-service + self-healing client + packaging/icns/launcher fixes, verified by Stage V drills + Agent 1 round-2 re-drills. PR will be opened by Agent 0 right after your records land.

YOUR TASKS (mirror the records pattern of run APPDEV_WOVEN_REDESIGN_2026-07-24 — read one of its DEL run records as a template):

1. DEL run records + _STATUS updates. Determine affected deliverables by reading projects/chirality-app-dev/execution/**/_STATUS.md Remaining sections that this tranche closes or advances — at minimum: the packaged-desktop smoke-evidence residual (DEL-02-01), the runtime-connectivity dot residual (find its DEL — likely DEL-05-04 or similar from the 2026-07-24 run records), and the .icns residual (DEL-09-04). For each affected DEL: append a run record _run_records/R<n>_DAEMON_SERVICE_2026-07-25.md (numbering follows existing files) summarizing what landed, evidence pointers (AgentRuns instances + evidence dirs), and update _STATUS.md (Remaining/History/Last-Updated) accurately — close only what evidence actually closes; add NEW named residuals: (a) daemon helper-bundle identity (LaunchServices resolution causes a ~2-10s self-healing bounce when Finder-opening while daemon runs; causal fix = own CFBundleIdentifier helper app, future tranche, escalated to owner); (b) SIGKILL leaves stale control.sock (uncatchable, daemon handles on next start — verify how before wording it, else state as observed); (c) premerge evidence row pass_with_skips pending CI Harness pre-merge on the PR; (d) owner-machine deployment steps pending post-merge (LaunchAgent reinstall via rebuilt app/CLI); (e) instruction-root divergence for packaged daemon (pre-existing, deliberately not addressed).

2. plans/PLAN_COMPLETION_LOG.md — append a 2026-07-25 entry consistent with existing entry style.

3. Receipt-91 in projects/chirality-app-dev/loop/LOOP_RECEIPTS.md. Read the receipt grammar in projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md and the existing Receipt-90 as format reference. Constraints: append-only, <=12 records, <=4096 bytes, Parent Receipt-90, Examined-Through = full SHA of the branch HEAD your records commit will sit on top of — compute via git rev-parse HEAD AFTER your content commits are made (see step 5 ordering), outcome EXECUTED, PR pointer "PR: pending (opened by Agent 0 immediately after this receipt)" only if the grammar allows a pending pointer — CHECK Receipt-90's PR field format; if the grammar requires a concrete PR number, instead leave the receipt's PR field per whatever convention the workplan states for pre-PR receipts, and note in your return that Agent 0 must amend/append per grammar. Owner directions this run, VERBATIM (transcribe the load-bearing ones per grammar; these are exact quotes):
- "Now time to debug.  Assume the Agent 0 posture and use `opus-5` model for Agent 1 and 2 instances.  First thing is the logo isn't showing up either as the app logo nor in the app UI itself.   Why is the daemon unavailable?"
- "that's not a fix, that's not acceptable to expect that each time.  Should the daemon be a server that runs separately, requiring whatever build out necessary to host the service for this machine?"
- "should you include it within the larger set of fixes you had thought of?"
- "draft the brief and proceed using the same subagent delegation model established in this session (Agent 0/1/2 as appropriate, `opus-5` models for Agent 1/2)"
- "proceed with the records stage and open the PR when drills pass"
Validate with: python3 tools/validation/validate_app_dev_loop_receipts.py (find exact invocation; it must PASS before you finish).

4. Check whether any governed doc you touch requires corpus reconciliation (tools/.../reconcile_authority_corpus.py status) — if status reports drift caused by your edits, follow the documented bump/apply flow; if drift pre-exists your edits, DO NOT touch it, just report.

5. Commits: (a) first commit = run records + _STATUS + completion log + HANDOFF_STATE.md (write one in the AgentRuns dir per the governance handoff-state rule: accepted upstream = round-2 tree, closure verdict, rerun requirements, remaining blockers/residuals); then (b) compute git rev-parse HEAD, write Receipt-91 with that Examined-Through, validate, commit the receipt separately. Repo-style messages ending with:

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

Do NOT push. Do NOT touch frontend/src, electron, runtime code, package.json, or any README.md (owner is editing a README in another session). Do NOT modify ROUND1/ROUND2 or stage RETURN files. Lockfile discipline applies.

RETURN: instances/RECORDS/RETURN.md + final chat text (compressed): DELs touched with record filenames, residuals added/closed per DEL, receipt validation output, corpus status, commit SHAs, anything Agent 0 must do for grammar compliance (e.g. PR-number amendment). Raw data, no pleasantries.
