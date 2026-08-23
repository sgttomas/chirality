# ROOT_CAUSE — A2-PKG09-R20-IMPLEMENT-01

Status: `CONFIRMED_FROM_VERIFIED_FIXTURE_AND_CURRENT_SOURCE`

## Evidence basis

- The only external fixture read was the exact brief-authorized source file.
- Independent pre-copy gate: regular file, not a symlink, exactly 3,049 bytes,
  SHA-256
  `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`.
- The repository fixture is byte-identical at the same size and SHA-256.
- Current source basis before repair was SHA-256
  `141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52`.

## Confirmed cause

The verified launchctl fixture is an exact-owned loaded job with state
`running`, PID `34924`, run count `1`, and exact last-exit sentinel
`(never exited)`. The current cleanup parser accepted only optional signed
integers for `last exit code`; it therefore rejected the real sentinel before
the existing exact service, plist, program, argument, and executable checks
could authorize bootout.

The cleanup routine then unconditionally unlinked the proof plist and removed
runtime data after its bootout loop, including when job mutation was refused,
the job remained loaded, or an observed process was still alive. It also had
no pre-removal preservation step for daemon stdout/stderr on a non-PASS.

## Applied bounded resolution

- Exact `(never exited)` parses only as `lastExitCode: undefined` and
  `neverExited: true`; every other noninteger form remains invalid.
- Exact-owned running PID cleanup remains subject to executable identity and
  now proceeds for the verified runs-1/never-exited shape. Integer and
  pid-less crash-loop behavior is preserved.
- Plist/runtime removal is refused unless the job is absent, mutation was not
  refused, and every observed proof PID is absent.
- Before any permitted plist/runtime removal, both fixed daemon logs are read
  alongside the runtime's actual operator-token file. Both logs are copied to
  `<session-root>/failed-logs/` only after neither contains that token. Token,
  token-file, source-log, or destination ambiguity copies neither log and
  retains runtime data as private-only diagnostic state.
- Pre-removal copies survive proof-observation, cleanup, and later
  default-protection failures. They are deleted only after final status is
  established as PASS, per
  `AMENDMENT_01_FAILURE_LOG_FINAL_STATUS_COVERAGE.md`.

No prompt assertion was used as a substitute for fixture/source confirmation.
