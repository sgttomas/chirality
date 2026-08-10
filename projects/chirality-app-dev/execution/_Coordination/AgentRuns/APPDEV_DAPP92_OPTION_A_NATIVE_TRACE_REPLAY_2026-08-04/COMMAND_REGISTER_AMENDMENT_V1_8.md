# Command-register amendment v1.8 — terminal cleanup and exact approval gate

Status: `FROZEN BEFORE C199; C196–C198 HELD/DEFERRED`

Attempt 2 passed reconstruction, exact candidate/lock hashes, the accepted R3
six-package projection, focused Vitest (actual 4 files/30 tests), typecheck,
production build, Electron 43.2.0 helper+GUI package construction, and packaged
dependency verification. C178 then failed because the redundant CLI suffix
`-- --publish never` caused npm to pass positional `never` into the final
instruction-root verifier. Per the sealed stop, C179–C184 did not run and no
package identity/topology hash is claimed. C185–C195 restored all source and
removed generated/dependency state; frontend is Git-clean.

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C196 | elevation/privilege/entitlement | HELD — OWNER COMMAND APPROVAL REQUIRED | `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt` | Attach LLDB 2100.0.17.203 to exactly the child PID returned by the future sealed direct helper launch; no PID search/census. macOS task attachment requires Developer Tools/debugger authorization or entitlement. No memory/environment/credential commands. |
| C197 | elevation/privilege/entitlement | HELD WITH C196 | Existing LLDB PTY control only: send interrupt byte `\u0003`, then exact debugger commands `process detach\nquit\n` | Bound trace cleanup after helper settlement or 150-second absolute trace duration. Detach exact target; no kill/security change. |
| C198 | temporary product reconstruction/runtime | DEFERRED TO POST-APPROVAL SEALED RERUN | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack` | Corrected package command, exact frontend cwd; script already contains `--publish never`. Must run only after exact reconstruction/projection and before runtime. |
| C199 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/rm -rf /private/tmp/chirality-dapp92-option-a-20260804` | Remove exact run-owned residual tree after durable preparation returns exist. |
| C200 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` | Prove terminal runtime cleanup. |

## C196 target and capture contract

- Target PID selection: only the direct child PID returned by the future exact
  helper launch command; the PID is written into the command register before
  C196 invocation. No `pgrep`, process-name match, GUI PID, child renderer, or
  foreign process is eligible.
- Executable: packaged Electron `43.2.0` helper at
  `dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service` after source/package hashes reproduce.
- Capture: timestamped breakpoint hits and bounded 16-frame native backtraces
  for `__sigtramp`, `uv__signal_handler`, Node `SignalWrap::OnSignal`, Electron
  `Browser::Quit`, and AppKit `-[NSApplication terminate:]`; existing redacted
  App logs separately bind teardown and Root-stop start/settlement.
- Redaction: no memory reads/dumps, expression evaluation, environment,
  arguments, token files, keychain, credentials, secrets, or owner HOME.
- Duration/scope: one exact helper PID; attach after helper ready and before GUI
  launch; record through first-SIGTERM settlement only; absolute maximum 150 s.
- Cleanup: C197 detaches; helper/GUI and isolated runtime cleanup follow the
  already sealed run-owned PID/path commands. No persistent debugger,
  entitlement, SIP/security, signing, or admin change.
- Alternatives: `sample` is unprivileged but point-in-time only and cannot
  establish the five-stage event sequence. DTrace C052 is sender-side only and
  separately privileged/SIP-limited. `fs_usage` C053 is privileged and lower
  causal value. Neither is required if C196 resolves the bound symbols.
- Evidence available without C196: exact source/build/package readiness,
  process/socket/owner/descriptors, authenticated contact, ordinary first
  signal, bounded polls, cleanup, and existing product shutdown logs. It cannot
  distinguish OS/native delivery, libuv/JS callback, and Electron lifecycle
  entry, so it cannot close the D-APP-92 causal objective.
