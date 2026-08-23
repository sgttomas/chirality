# WORKING_ITEMS manager return — DEL-09-04 R17 failure repair

- RunID: `APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22`
- InstanceID: `WI-PKG09-R17-FAILURE-REPAIR-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r17-repair`
- Exact basis / HEAD / origin-main:
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Verdict: `VALIDATED_PASS`
- Deliverable: `IN_PROGRESS`, unproved
- Git integration: not performed

## Outcome

R17 preserves the owner-operated R16 attempt as executed-and-failed evidence;
it is not and cannot be proof acceptance. Public artifacts independently bind
the non-claiming PREPARED state, same-source FAIL, observed login-session
transition, RunAtLoad/crash-loop evidence, exact ambiguous-process error, and
cleanup refusal/residual. Owner-reported nonzero capture, `runs = 16`, and
manual residual bootout remain explicitly owner-attributed. The exact proof
plist/service are now absent, and the private root was never traversed or
mutated by this run.

The candidate repairs three bounded failures:

1. macOS prepare rejects the exact future control-socket path above 103 UTF-8
   bytes before any prepare inspection, command, or mutation;
2. proof cleanup may boot out a pid-less job only after exact non-default
   service, plist, launchctl, executable, non-running crash-loop state,
   positive runs, and nonzero last-exit identity all match; PID-present jobs
   retain exact running-state plus lsof validation; and
3. runtime-host fails with a deterministic measured/max error before
   environment mutation or daemon construction, using actual
   `process.platform`, without relocating the socket.

No R18 procedure or proof was staged or executed. The sole proposed future
root `/private/tmp/ch-r18-91499728-51dd` is 33 UTF-8 bytes, absent and not a
symlink; its 67-byte future socket has a 36-byte safety margin.

## Exact reviewed identities

| Path | SHA-256 |
|---|---|
| proof harness | `141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52` |
| harness test | `9338631ef1b295806e17f8be85ffd1a3600c51e68c27d014fc485278a500f595` |
| runtime host | `39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7` |
| runtime-host test | `78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8` |
| R17 | `4e7ebda1e161e93629e5fb7e9f657447a48189882b2d342d6c287dfd914d28f7` |
| DEL status | `d308d4c38c33b087a5aa40b820d22661e15a811558bc388637fc39d0330491c7` |
| executor evidence | `0675197fed51a5508533ac9174ad82d3bbe225d3424f089b87d1008362cf90ef` |
| executor return | `248a49942101fd42b30228c85efb25f152731a6156b3a6b4aff808b333cc21af` |
| fresh review | `8b384aa8363e6a775c9c58cbfe9b2d4e779e1b2c2e4d5bcdbd3cbd26d7f1be88` |
| runtime events | `2c077318c2e091d8765e51d2cf81a6ab7dcfe020ff794d84ca61fdb4df7501ab` |
| runtime summary | `823278a28d123bb6e43a76d997f32f2c26932e4e753c395204be4a38b613b0e6` |

Runtime telemetry is complete: 8 events, 3 matched sessions, one recorded
manager pre-freeze security remediation, zero unmatched sessions, status
PASS, with native context occupancy explicitly unavailable.

## Validation

- Fresh 12-item evidence/security review: PASS, zero findings/blockers.
- Syntax: PASS.
- Focused harness/runtime-host tests: 65/65 PASS.
- Typecheck: PASS.
- Full frontend: 1,258 passed / 4 skipped after exact sandbox-only local bind
  denial was rerun with permission limited to local test sockets.
- Public evidence: exact directory/file modes and six hashes PASS; selected
  JSON fields PASS; count-only logs show 80/80 matching failures in each cited
  log; bounded secret categories all zero without body output.
- APP-HOLD: 53/53 PASS.
- Practitioner self-check: exit 0 at calibrated baseline.
- Practitioner pytest: 350/350 PASS.
- Receipt validator: PASS; receipt ledger unchanged.
- Candidate whitespace including untracked, individual no-index checks,
  worktree/cached diff checks, JSON/JSONL, App-only containment, exact basis,
  and empty index: PASS.

## Exact semantic paths

1. `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
2. `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
3. `projects/chirality-app-dev/frontend/electron/runtime-host.ts`
4. `projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-host-socket-path.test.ts`
5. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R17_LOGIN_PROOF_FAILURE_AND_REPAIR_2026-08-22.md`
6. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`

All remaining candidate files are run controls/evidence beneath the exact run
root `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/`: transcription, plan, graph,
activation, manager preflight/return, telemetry/summary, two sealed briefs,
two amendments, executor evidence/return, and the fresh review plus its eleven
bounded logs. No path outside `projects/chirality-app-dev/` changed; the index
is empty.

## Recommendation conclusions

1. Recommend a separate owner-authorized design for a short per-user socket
   location with exclusive mode-0700 creation, ownership/ancestor/symlink
   checks, collision/stale cleanup controls, canonical client discovery, and
   migration tests. The shorter path reduces `sun_path` risk; a shared
   temporary parent increases collision/ownership/stale-cleanup concerns, and
   system per-user temporary roots may still be long. No relocation is made.
2. Recommend a separate review of `KeepAlive=always` with a bounded guard,
   backoff, or proof-specific restart posture. Unconditional restart amplifies
   deterministic failures into restart/log churn and unstable service;
   weakening it can reduce automatic recovery. No plist or product policy is
   changed.

## Fences and handoff

No network, build, package, rebuild, R18 root mutation/staging, prepare,
capture, logout/login, GUI, bootstrap, kickstart, LaunchAgent/plist/job/default
operator/launcher/private-root mutation, signing, notarization, deployment,
distribution, release-readiness, stage, commit, push, PR, or merge occurred.

Blockers: none for later CHANGE consideration. Any byte change requires
affected validation and fresh review to rerun. R18, an exact rebuilt package,
proof execution, handoff, and acceptance require separate owner authority.
