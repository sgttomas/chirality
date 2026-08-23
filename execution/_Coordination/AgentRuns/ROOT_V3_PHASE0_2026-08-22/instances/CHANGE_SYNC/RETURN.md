# CHANGE Return — Authorized Main Sync

Run ID: `ROOT_V3_PHASE0_2026-08-22`

Verdict: `COMPLETE — AUTHORIZED APP-ONLY MAIN SYNC MERGED`

## Authorization and identity

The controlling owner authorization is transcribed in `LAUNCH_BRIEF.md`:

> I authorize you to fetch and merge the latest `origin/main` into this branch,
> then complete Receipt 114, validation, push, and PR creation without merging
> the PR.

- Branch: `codex/root-v3-phase0-2026-08-22`
- Pre-merge node `HEAD`:
  `7590c002b1dc9399e95029d51551895bb700b302`
- Fetched `origin/main`:
  `166efa82748133e90674be62304b81f8a0a8c1b4`
- Merge base:
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Merge commit:
  `0bd042e5299c81301cc726bc54eea265285b4159`
- Merge parents, in order:
  1. `7590c002b1dc9399e95029d51551895bb700b302`
  2. `166efa82748133e90674be62304b81f8a0a8c1b4`
- Merge message: `merge main into root v3 phase-0 preparation`
- Strategy: non-rebase merge commit using Git's `ort` strategy.
- Conflict count: `0`.

## Overlap gate

The incoming range was inspected before merge with:

```text
git diff --name-status 6b0c5219b6a2653e2fc491b1d998abcf78fcf776..origin/main
```

The result contained 34 paths. All 34 were confined to
`projects/chirality-app-dev/`; zero paths overlapped a Root-owned tranche path,
live `AGENTS.md`, the Root receipt or handoff, `_LATEST.md`, DEL-02-03, or the
D-GOV-35 / SCA-004 outputs.

Exact incoming path evidence:

```text
M projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md
A projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R17_LOGIN_PROOF_FAILURE_AND_REPAIR_2026-08-22.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/CHAT_TRANSCRIPTION.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/ORCHESTRATION_PLAN.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/WORK_GRAPH.json
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/ACTIVATION_AND_WORK_GRAPH.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/MANAGER_PREFLIGHT.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/MANAGER_RETURN.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/RUNTIME_EVENTS.jsonl
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/RUNTIME_SUMMARY.json
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/briefs/A2-PKG09-R17-EXECUTE-01.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/briefs/A2-PKG09-R17-REVIEW-01.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/briefs/AMENDMENT_01_SHORT_R18_ROOT.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/briefs/AMENDMENT_02_MANAGER_PREFREEZE_SECURITY.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/executor/EVIDENCE_SUMMARY.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/executor/RETURN.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/REVIEW.md
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/app-hold.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/candidate-hashes.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/evidence-checks.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/final-hygiene.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/focused-tests-65.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/focused-tests.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/full-frontend-local-sockets.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/full-frontend-sandbox.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/practitioner-pytest.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/practitioner-self-check.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/receipt-validator.log
A projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/review/typecheck.log
M projects/chirality-app-dev/frontend/electron/runtime-host.ts
M projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs
A projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-host-socket-path.test.ts
M projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
M projects/chirality-app-dev/loop/LOOP_RECEIPTS.md
```

Machine classification reproduced after merge:

```text
incoming_paths 34
app_only_paths 34
root_overlap_paths 0
```

## Node-history preservation

All three node commits remain ancestors of merged `HEAD`:

```text
45eead4edf524b9b31293b4f8b8f59ec58b283d4 ancestor=yes
d329529cf07e255415edef0f2d3f3ceee357d5c1 ancestor=yes
7590c002b1dc9399e95029d51551895bb700b302 ancestor=yes
```

No rebase, amend, reset, or history rewrite occurred.

## Protected identities after merge

| Surface | SHA-256 |
|---|---|
| `AGENTS.md` | `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb` |
| `execution/_ScopeChange/_LATEST.md` | `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` |
| DEL-02-03 `ScopeOfWork.md` | `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f` |
| Root Phase-0 steer source | `c348e9767db4af20787bbcb74c64791ef08d700b08dc19d86289a88a58f067e3` |
| G0 owner-record source | `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b` |

## Confined post-merge state

The index is empty. `git status --short` shows only the two intentionally
uncommitted control folders:

```text
?? execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/CHANGE_NODE_COMMITS/
?? execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/CHANGE_SYNC/
```

No push, PR creation, or PR merge occurred. `HELP_HUMAN` is the next lawful
owner for Receipt 114, integrated validation, and later CHANGE publication.
