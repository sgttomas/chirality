# Integrated tranche review return

- Reviewer task: `/root/app_integrated_final_review`
- Review posture: fresh, read-only, complete-tranche review
- Verdict: **FAIL — 3 actionable record-consistency findings**
- Product source verdict: no new actionable defect found in the reviewed login-
  proof script/test beyond the already preserved REVIEW-01..04 remediation
  chain; live product hashes match frozen diff 04.
- Host action: none. No LaunchAgent, logout/login, capture, Git, network, or
  owner/default launcher action was run.

## Actionable findings

### P1 — the sole final reviewer is persisted as the interrupted duplicate

`WORK_GRAPH_AMENDMENT_09.md:3-11` says the local
`A2-APPDEV-INTEGRATED-REVIEW-01` dispatch was interrupted with no verdict and
names `/root/app_integrated_final_review` as the sole final reviewer. However,
`instances/A2-APPDEV-INTEGRATED-REVIEW-01/STATUS.json:1-6` still marks this
same durable instance `INTERRUPTED`, while its `LAUNCH_BRIEF.md:1-4` identifies
it as a WORKING_ITEMS child rather than the Agent 0 direct reviewer. Placing
this direct review return in that directory therefore makes one instance both
the no-verdict interrupted duplicate and the terminal reviewer. Before
publication, give the direct reviewer an unambiguous durable identity (or
truthfully amend the takeover/brief/status chain) and leave exactly one
terminal reviewer status matching this return.

### P1 — governed dispatches have no actual engine/provider/model attribution

The App project agent index requires every governed dispatched role to record
the engine, provider, and model that actually ran. The complete run root has no
such attribution: `RUNTIME_SUMMARY.json:2-16` records attempt counts and the
measurement limitation but no execution attribution, and none of the child
`instances/*/STATUS.json` or launch briefs supplies it. This AgentRuns package
exists, so the receipt-only fallback does not apply. Record the actual
engine/provider/model for each dispatched role (including substitutions and
the final direct reviewer) in the governed run before the receipt points to
it.

### P2 — the deliverable record overstates the redacted file set

`_run_records/R12_LOGIN_SESSION_PROOF_PREPARATION_2026-08-21.md:32-38` says
capture “writes only” the three redacted evidence JSON files. The product also
writes private `.capture-state.json` during prepare and renames it to
`.capture-state.consumed.json` during capture
(`frontend/scripts/run-packaged-launchagent-login-proof.mjs:562-582` and
`:633-702`). Those files intentionally contain absolute account/app/runtime
paths and are excluded from the evidence package, so they must not be described
as redacted outputs. Calibrate the sentence to distinguish the three public,
redacted evidence files from the private one-shot state retained locally; the
minimal owner procedure should continue to package only the three redacted
files.

## Reviewed integrated inventory

- Owner-ruling transcription, amendment package, closure evidence/check JSON,
  Task Management register maintenance, and DEL-08-04 status amendment.
- DEL-09-04 status, memory, R12 procedure, TASK run record, and the complete
  902-line product script plus 484-line focused test.
- Full run root: activation, work graph and amendments 01-09, takeover,
  frozen diffs 01-04, all implementation/remediation/review briefs, returns,
  statuses, registered checks, runtime summary, manager return, handoff, and
  integrated diff basis.

## Verified evidence

- Live script SHA-256:
  `980e2e710ab66006baeefc14d400584bc8837f3ea3b35390db94b879413e2c20`.
- Live focused-test SHA-256:
  `f168e7d18326a536ff07b4e3a82019904bc43753fa3999acd439b8353171f01a`.
- Owner ruling, amendment, closure, TM checks, DEL-08-04 status, and live App
  register hashes match the values cited by the integrated records.
- `REGISTERED_CHECKS_FINAL.json` reports PASS for typecheck, build, harness
  self-check, and APP-HOLD integrity.
- `REGISTERED_CHECKS_FRONTEND_TEST_HOST.json` reports PASS: 152 files plus one
  skipped, 1,214 tests plus four skipped.
- `REGISTERED_CHECKS_PREMERGE_AGENT0.json` truthfully reports FAIL after a READY
  managed Next service returned HTTP 503 without the shared runtime/project
  registration lifecycle; the surrounding records consistently classify this
  as the required PR-CI rerun, not a local PASS or waiver.
- Owner rulings 1-4 are transcribed verbatim. TM-APP-036 retirement is applied
  without erasing its surviving three-deliverable review; TM-APP-044 is closed
  only as the attention-row rehome while DEL-08-04 retains the Root-owned
  dependency; DEL-09-04 remains IN_PROGRESS and makes no proof/release claim.

## Residual boundary

After the three record findings are corrected, the integrated product and
owner-ruling application are publishable on the reviewed evidence. The actual
logout/login and capture remain an owner act after Git/PR, accepted packaged
identity, and the PR-CI premerge rerun; this review does not constitute that
proof.
