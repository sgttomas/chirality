# DEL-09-04 R17 login-proof failure and bounded repair

- Date: `2026-08-22`
- Run: `APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22`
- Accepted basis: `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Failed proof source revision:
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- Result: `EXECUTED AND FAILED — NO PROOF ACCEPTED`
- Deliverable state: `IN_PROGRESS`

R17 preserves a failed owner-operated login-session attempt and a separate
bounded repair candidate. The attempt is never upgraded to a passing proof.
The repair is uncommitted, unbuilt, unexecuted against an R18 root, and subject
to mandatory fresh evidence-only review.

## Attribution boundary

### Owner-reported acts and observations

The owner reports that the R16 procedure reached `PREPARED`, then crossed one
ordinary logout/login boundary and ran capture. Capture returned nonzero. The
owner reports that the residual loaded job showed `runs = 16`, and that the
owner later manually booted out that residual job. Those act, exit, run-count,
and manual-remediation statements remain owner-attributed; this record does
not portray them as independently witnessed by an agent.

### Independent public-evidence observations

The executor and manager used only bounded read-only metadata, hashes,
selected public JSON fields, and count-only log scans. No private capture state
or log body is reproduced here.

The preserved directory is mode `0700`, contains exactly six regular files,
and every file is mode `0600`:

| Public file | SHA-256 |
|---|---|
| `prepared.json` | `1416d6d162df551163dcc3f90c88d4519b2662d2ba903883e60ece0715fe1476` |
| `summary.json` | `f2f912bc35652e1b877a1eefdf511f9658a88e7ab69051ec637deb260bcfd230` |
| `evidence-package.json` | `d3bf7c4c261916e6de4507f5be1728839ba7676bb9494d31433d00945ff358a4` |
| `daemon.stdout.log` | `cb8f06c1bc2fa8e696fd45c1ca9fe7462373b92177393f0e8560fe15d70ae83c` |
| `daemon.stderr.log` | `6fa805d99101b2f8074600289050b960042892d6312ebda559f2163f199147bb` |
| `desktop-daemon.log` | `1bab152fccad435db691bec70dc159521e1c6d94b5435b0cfdeb2fc1e98196a6` |

Selected public fields independently establish:

- `prepared.json` is `PREPARED`, binds source revision
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`, and explicitly has
  `proofClaimed: false`;
- both summary and evidence package are `FAIL` at that same source revision;
- the summary records an observed login-session identity transition,
  `RunAtLoad: true`, no harness-performed logout/login, no bootstrap, and no
  kickstart;
- capture failed with `Loaded job has ambiguous process identity`; its strict
  proof fields therefore remain false or unavailable and
  `loginDiscoveredJobObserved` is not credited;
- source cleanup reports `plistAbsent: true`, `runtimeDataRemoved: true`,
  `jobAbsent: false`, and `jobMutationRefused: true`; and
- `daemon.stderr.log` and `desktop-daemon.log` each contain 80 occurrences of
  both `runtime.daemon.initialize_failed` and the count-matched
  `listen EINVAL .../runtime-data/runtime/control.sock` signature. This is
  independent evidence of repeated daemon starts failing at the control-socket
  listen boundary, without copying a log body.

The repeated initialization evidence supports a spawned/crash-looping runtime
observation. It does not turn the loaded service into an identified running
process and does not satisfy the proof.

Bounded scans reported zero forbidden private filenames and zero files
matching the capture-state schema, credential/token-name, private-key, or
login-session digest-salt categories. The scans emitted counts only.

### Current host state and private-root boundary

The manager's recorded read-only preflight independently found the exact proof
plist absent and the exact proof service absent with the expected not-found
classification after the owner's reported manual bootout. The private proof
root remains present. Neither manager nor executor traversed, read inside,
wrote, or cleaned that root. No default operator job, plist, or launcher was
queried or touched by this repair.

## Root cause evidence

The exact R16 full socket path
`${R16_PROOF_ROOT}/runtime-data/runtime/control.sock` is 119 UTF-8 bytes. The
corresponding hypothetical R13 path is 111 UTF-8 bytes. Both exceed the macOS
Unix-domain pathname maximum of 103 bytes when the terminating NUL occupies
the final byte of `sun_path[104]`. This matches the independently repeated
`listen EINVAL` evidence.

The only future root proposed by this run is:

```text
/private/tmp/ch-r18-91499728-51dd
```

The exact root is 33 UTF-8 bytes. Its exact future control-socket path is 67
UTF-8 bytes, leaving a 36-byte margin below the macOS maximum. A bounded
read-only check confirmed the exact path is absent and not a symlink. The root
is proposed only: this run did not create, prepare, capture, or otherwise query
inside it and does not stage an R18 owner procedure.

## Bounded repair candidate

### Prepare-time rejection

The proof harness now computes the exact lexical
`${sessionRoot}/runtime-data/runtime/control.sock` path immediately after
argument/source-revision validation. On macOS it rejects any value over 103
UTF-8 bytes with deterministic measured and maximum byte counts and no path or
secret. The check runs before symlink-ancestor inspection, session-root or
LaunchAgents-directory creation, app/plist access, commands, job inspection,
install, or other prepare mutation. The existing containment and symlink rules
still run for an accepted path.

Tests use filesystem-facing session-root strings and cover exact 103-byte
acceptance, 104-byte ASCII and Unicode rejection, R16 119-byte rejection, R13
111-byte rejection, and zero command, session-root, or candidate-home creation
on rejection.

### Proof-owned pid-less cleanup

Cleanup now permits bootout of a pid-less loaded proof job only after all of
these independently match:

1. the validated non-default proof label and exact `gui/<uid>/<label>` service;
2. the expected plist path, with regular non-symlink bytes that parse to the
   exact label, `RunAtLoad`, and packaged runtime argument vector;
3. one unambiguous launchctl service wrapper, state, program, and argument
   vector matching the packaged executable; and
4. the packaged executable identity already bound by the prepared state.

A missing PID skips `lsof` only after those checks and only when the job has
one recognized non-running crash-loop/scheduled state, a positive unambiguous
run count, and a nonzero unambiguous last exit code. A pid-less `running` job
refuses bootout. A present valid PID must have exact state `running` before it
retains the prior strict one-executable `lsof` identity check; a PID-bearing
non-running job refuses bootout. Missing, mismatched, or ambiguous service,
plist, program, arguments, executable evidence, and any malformed, ambiguous,
or present-but-invalid PID refuse bootout. Tests include a realistic `runs =
16`, nonzero last-exit, pid-less crash-loop fixture, exact-owned bootout and
cleanup, both state/PID refusal directions, and fail-closed mismatch/ambiguity
cases. Existing default-job protected-state behavior is unchanged.

### Runtime-host diagnostic

Before it mutates runtime environment or constructs `RuntimeDaemon`, the
runtime host now measures its exact control-socket path. On macOS, more than
103 UTF-8 bytes throws a deterministic error containing measured and maximum
counts but not the path. The socket is not relocated. Tests cover 103/104,
Unicode byte counting, non-macOS non-enforcement, and prove the daemon
constructor—and therefore `listen`—is not attempted on rejection.

Candidate identities at executor byte freeze:

| Path | SHA-256 |
|---|---|
| `frontend/scripts/run-packaged-launchagent-login-proof.mjs` | `141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52` |
| `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `9338631ef1b295806e17f8be85ffd1a3600c51e68c27d014fc485278a500f595` |
| `frontend/electron/runtime-host.ts` | `39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7` |
| `frontend/src/__tests__/electron/runtime-host-socket-path.test.ts` | `78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8` |

## Evidence-only recommendations — not implemented

### Later short per-user socket location

Recommendation: in a separate owner-authorized design tranche, prefer a short
per-user runtime socket directory whose parent, ownership, mode, and every
ancestor are verified before use; create it exclusively at mode `0700`, refuse
symlinks and ownership mismatch, and bind clients through one canonical socket
identity. A shallow location avoids macOS `sun_path` failures for otherwise
valid long application-data roots.

Tradeoffs: a predictable shallow path under a shared temporary parent raises
collision, stale-directory, ownership, and cleanup concerns; a system-provided
per-user temporary root is permission-contained but may itself be long.
Relocation also changes client discovery, environment propagation, stale
socket recovery, and diagnostic expectations. Those decisions require their
own threat model and migration tests. No relocation is implemented here.

### Later KeepAlive crash-loop policy

Recommendation: separately review the proof-specific `KeepAlive=always`
posture and add a bounded guard, backoff, or proof-specific restart policy that
prevents a deterministic startup failure from producing an unbounded restart
and log-churn loop while keeping operator-service availability semantics
explicit.

Tradeoffs: weakening restart behavior can reduce automatic recovery; retaining
unconditional restart amplifies stable configuration failures, log volume, and
service instability. The prepare-time path guard prevents this known failure
before future installs, but it is not a general crash-loop policy. No plist,
KeepAlive, backoff, or operator policy is changed here.

## Validation

| Check | Result |
|---|---|
| harness syntax | PASS |
| focused harness/runtime-host tests | PASS — 65/65 |
| frontend typecheck | PASS |
| full frontend Vitest | PASS — 1,258 passed / 4 skipped with local test-socket permission |
| APP-HOLD `scan --require-register-match` | PASS |
| repository practitioner-harness `self-check` | PASS at the existing calibrated baseline |
| practitioner-harness pytest | PASS — 350/350 |
| App loop receipt validator | PASS; ledger unchanged |
| candidate whitespace, `git diff --check`, cached check | PASS |
| containment and index | PASS — all candidate paths under `projects/chirality-app-dev/`; index empty |

## Status and handoff

R17 is immutable failed-proof evidence. DEL-09-04 remains `IN_PROGRESS` and
unproved. Fresh evidence-only review is mandatory after all candidate and
record bytes freeze. Any later R18 preparation, logout/login, capture, proof
handoff, or acceptance remains an owner act after separate authorization,
integration, and an exact rebuilt package. No build, package, network,
LaunchAgent mutation, R18 mutation/proof action, GUI action, signing, notarization,
deployment, distribution, release-readiness, stage, commit, push, PR, or merge
occurred in this repair.
