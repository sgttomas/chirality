# D-APP-86 mandatory helper-rerun manifest

Status: `BLOCKED / PARTIAL — OWNER-STATE WRITE STOP`

RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`

Executor: `A2-PKG02-PARITY-EXECUTOR-01`

Parent: `WI-PKG02-DAPP86-RERUN-01`

Authority: D-APP-86 Option A and the sealed executor brief. This is derivative
software evidence only. It does not establish parity, release readiness,
lifecycle issuance, reliance, or owner acceptance.

## Frozen basis

- Commit: `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`
- Tree: `fe8ece104dd281e3219bd95fa8b121437d524520`
- Branch: `codex/app-dapp86-helper-parity-rerun-20260820`
- Tracked source manifest: 509 files; manifest SHA-256
  `941bc28a6bf58ce2ee4d18d778923baec8ad91fca194a4e1ec025eea4b780e2d`
- Runtime: Node `v24.18.0`, npm `11.16.0`, macOS `26.6.2` arm64
- Isolated user-data root: `/private/tmp/chirality-d86pkg02.VWKLGL/userdata`
  (removed after zero-holder checks)

## Frozen package

The retained package log records a sandboxed `desktop:pack` attempt that
stopped before package creation on `getaddrinfo ENOTFOUND github.com`. A
current package subsequently existed and its bytes were frozen and
independently revalidated, but this run contains neither a successful retry
transcript nor durable parent-routed network approval. Retry authorization
provenance and the exact successful package command are therefore `UNKNOWN`.
Package existence and hash facts do not prove either.

- Package: `frontend/dist/mac-arm64/Chirality.app`
- Package manifest: 446 regular files; manifest SHA-256
  `f7c072834fcc48c5a1fe37a6516ff33bcb4592c6dc2978aa0bf70843aa4ae54e`
- Symlink census manifest SHA-256:
  `6308b00235ff20598389689fbe50417fbb184ca45d20bd7fe1c1bdc0ac41f73c`
- Main executable SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- `app.asar` SHA-256:
  `90b3b6a8d5c63a08f5ceec86ff7cf4e86d14f2ad5b843ef3aba1e0723cdd02a9`
- `Info.plist` SHA-256:
  `8bb6ab847fe5734d203316a73e576edb11e41787a0eaadcd3645f42bcd0d916d`
- Signing posture: linker/adhoc only; no Team ID

Compared with the accepted 2026-08-03 package, the generic Electron executable
hash is unchanged, while `app.asar` changed from `18797e99...3c72ce2` and
`Info.plist` changed from `a5bfabe9...1969d414`. The current helper route is
still the packaged executable plus `--runtime-daemon`; its packaged JavaScript
payload now contains the accepted signal-shutdown binder. This is a material
payload difference, not a distinct helper-bundle identity. The accepted
D-APP-88/D-APP-93 closure proves the signal-binder/bounded-teardown remedy; it
does not establish that the deliverable statuses' explicitly distinct-helper
rerun trigger fired. Agent 0 therefore held N2 and authorized no rerun.

## Execution and stop

The isolated daemon started as PID `67623`, registered this worktree, and
completed one deterministic stub session
`2900d411-0e02-4054-9dd4-5fe8c04716ac` with two canonical events and one
derived transcript item.

The packaged GUI then started as PID `67697` and immediately logged:

`desktop.cli_launcher.install {"status":"written","path":"/Users/ryan/.local/bin/chirality"}`

That is an owner-state write outside the sealed brief. Live source exposes
`CHIRALITY_SKIP_CLI_LAUNCHER=1` specifically to suppress launcher installation
during verification, but the instrument invocation omitted it. The write is
therefore recorded as an instrument invocation defect, not a product defect.
The executor stopped
before any UI action or parity observation, did not alter the launcher again,
and did not attempt restoration. Both exact run-owned processes shut down
cleanly; the socket, CDP listener, holders, and disposable root were absent at
cleanup.

No parity surface closed. The distinct-helper trigger is not established and
no rerun is authorized on this basis.
