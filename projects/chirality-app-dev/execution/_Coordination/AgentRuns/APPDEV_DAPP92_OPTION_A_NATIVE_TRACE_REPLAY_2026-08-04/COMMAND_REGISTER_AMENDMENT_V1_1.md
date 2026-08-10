# Command-register amendment v1.1 — discovery repair

Status: `FROZEN BEFORE C072 INVOCATION`

The immutable v1 discovery return records:

- C001–C004 PASS;
- C005 failed because `/usr/bin/test` is absent on this host;
- C006 stopped because the three enumerated candidate test snapshot paths do
  not exist at those locations; and
- C019+ did not run.

This amendment does not substitute or erase those outcomes. It adds only the
read-only commands required to locate and bind the frozen test snapshots and
records the manager-executed v1 C007–C018 results. No reconstruction, build,
GUI, trace, signal, credential, or cleanup command has run.

## Manager-executed v1 discovery results

- C007: Darwin `25.6.0`, arm64.
- C008: macOS `26.6` build `25G72`.
- C009: `/Applications/Xcode.app/Contents/Developer`.
- C010: `/Applications/Xcode.app/Contents/Developer/usr/bin/lldb`.
- C011: `lldb-2100.0.17.203`; Apple Swift `6.3.3`.
- C012: `/Applications/Xcode.app/Contents/Developer/usr/bin/xctrace`.
- C013: `xctrace version 16.0 (17F113)`.
- C014: `/usr/sbin/dtrace`.
- C015: `/usr/bin/sample`.
- C016: `/usr/bin/fs_usage`.
- C017: `/usr/sbin/spindump`.
- C018: `/usr/bin/log`.

`sample` is a point-in-time stack sampler only and cannot by itself establish
the required five-stage signal/lifecycle sequence. C051 remains the first
intended adequate native-trace attachment and remains HELD.

## Added exact commands

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C072 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/find projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source -type f -print` | Enumerate the immutable candidate snapshot; no writes. |
| C073 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test ! -e projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` | Corrected first addition-absence check. |
| C074 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` | Corrected second addition-absence check. |
| C075 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` | Corrected third addition-absence check. |
| C076 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test ! -e projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` | Corrected fourth addition-absence check. |
| C077 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test ! -e projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` | Corrected fifth addition-absence check. |

After C072 identifies the actual immutable snapshot locations, a v1.2
amendment must freeze each corrected hash and copy command before invocation.
No guessed path is permitted.
