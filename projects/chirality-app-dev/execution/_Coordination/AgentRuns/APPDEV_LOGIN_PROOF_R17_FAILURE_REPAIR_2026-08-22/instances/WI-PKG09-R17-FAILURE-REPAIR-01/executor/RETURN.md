# A2-PKG09-R17-EXECUTE-01 return

## Verdict

`PASS — EXECUTOR CANDIDATE READY FOR MANDATORY FRESH EVIDENCE-ONLY REVIEW`

R17 remains an executed-and-failed record and cannot be read as proof
acceptance. DEL-09-04 remains `IN_PROGRESS` and unproved.

## Applied changes and exact identities

| Path | SHA-256 |
|---|---|
| `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs` | `141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52` |
| `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `9338631ef1b295806e17f8be85ffd1a3600c51e68c27d014fc485278a500f595` |
| `projects/chirality-app-dev/frontend/electron/runtime-host.ts` | `39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7` |
| `projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-host-socket-path.test.ts` | `78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R17_LOGIN_PROOF_FAILURE_AND_REPAIR_2026-08-22.md` | `4e7ebda1e161e93629e5fb7e9f657447a48189882b2d342d6c287dfd914d28f7` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md` | `d308d4c38c33b087a5aa40b820d22661e15a811558bc388637fc39d0330491c7` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/executor/EVIDENCE_SUMMARY.md` | `0675197fed51a5508533ac9174ad82d3bbe225d3424f089b87d1008362cf90ef` |

The harness rejects a macOS prepare path over 103 UTF-8 bytes before any
filesystem/command/identity activity, while preserving the existing
symlink/containment checks after acceptance. Cleanup now validates exact
non-default service identity, regular non-symlink plist bytes, label,
`RunAtLoad`, plist/runtime argv, launchctl service/program/argv, and packaged
executable. It permits an exact pid-less, positive-runs, nonzero-last-exit,
non-running crash-loop/scheduled job bootout without `lsof`; pid-less
`running` refuses. A present PID requires exact `running` state and retains
strict executable inspection; PID-bearing non-running refuses. Runtime-host
rejects an overlong macOS control socket before environment mutation or daemon
construction through its no-argument production entry point and does not
relocate it.

## Failed-proof evidence result

- All six public evidence hashes and `0600` modes match the owner basis; the
  enclosing directory is `0700` with exactly six regular files.
- Public records independently remain non-claiming `PREPARED` then same-source
  `FAIL`, with the exact error and cleanup refusal/residual recorded in R17.
- Count-only scans found 80 matched `runtime.daemon.initialize_failed` and
  `listen EINVAL ...control.sock` events in each of the two relevant logs.
- Bounded secret-category counts are all zero.
- R16/R13 exact full socket paths are 119/111 UTF-8 bytes. The sole proposed
  future root `/private/tmp/ch-r18-91499728-51dd` is 33 bytes, confirmed absent
  and not a symlink read-only; its 67-byte socket path leaves a 36-byte margin.
- Owner-reported nonzero capture, `runs = 16`, and manual residual bootout are
  explicitly owner-attributed. Current proof plist/job absence and private-root
  existence remain manager-attributed read-only observations.
- No log body or private state was copied; the private root was not traversed.

## Checks

| Check | Result |
|---|---|
| syntax | PASS |
| focused login-proof/runtime-host tests | PASS — 65/65 |
| typecheck | PASS |
| full frontend suite | PASS — 1,258 passed / 4 skipped with local test-socket permission |
| APP-HOLD integrity | PASS |
| repository practitioner self-check | PASS at existing calibrated baseline |
| practitioner pytest | PASS — 350/350 |
| receipt validator | PASS; ledger unchanged |
| candidate whitespace including untracked | PASS |
| `git diff --check` / cached check | PASS / PASS |
| containment | PASS — all candidate paths App-contained |
| index | empty |

## Recommendation conclusions

1. Later short socket location: recommend a separately authorized, short,
   permission-contained, symlink-safe per-user socket root with ownership/mode,
   collision, stale cleanup, client-discovery, and migration evidence. No
   relocation is implemented.
2. Later crash-loop posture: recommend a separately authorized guard, backoff,
   or proof-specific KeepAlive policy to balance recovery against restart/log
   churn and unstable service behavior. No plist or product policy is changed.

## Blockers and rerun triggers

- No executor blocker.
- Fresh evidence-only review is mandatory over frozen bytes.
- Any reviewer finding triggers the standing bounded repair/re-review cycle.
- Any source/test/record/status byte change after this return requires affected
  checks, hashes, candidate whitespace, and fresh review to rerun.
- Any later R18 work requires separate owner authorization, Git integration,
  and a newly rebuilt exact package.

## Fences observed

No build/package/network/provider expansion, R18 root mutation or proof action,
prepare/capture/logout/login/GUI, bootstrap/kickstart, LaunchAgent/plist/job,
default operator, launcher, signing/notarization/deployment/distribution/
release, stage/commit/push/PR/merge, private-root traversal, or delegation
occurred.
