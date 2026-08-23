# R20 direct disposable packaged-daemon precheck

- Exact-root pre-gate: metadata-only `PASS_ABSENT_NON_SYMLINK`; the prior private root was not read or traversed.
- Attempt count: exactly `1`.
- Permission posture: exact local Unix/loopback execution grant; no external network request or network tool.
- Command: `/bin/zsh .../instances/A2-PKG09-R20-PHASEB-EXECUTE-01/disposable-precheck.sh`.
- Started: `2026-08-23T09:34:53Z`.
- Exact executable argv: packaged `Chirality --runtime-daemon`.
- Environment: exact `CHIRALITY_USER_DATA=/private/tmp/ch-r18-91499728-51dd/runtime-data`, `CHIRALITY_SKIP_CLI_LAUNCHER=1`, `CHIRALITY_DAEMON_GUI_SPAWN=0`.
- PID `48351`; `ps` matched the exact executable and argv.
- Exact Unix socket: `/private/tmp/ch-r18-91499728-51dd/runtime-data/runtime/control.sock`, exactly 67 UTF-8 bytes.
- Authenticated packaged CLI health: `project list --json` returned exact `[]`.
- SIGTERM entered bounded graceful shutdown; daemon exit `0`.
- Stopped: `2026-08-23T09:34:56Z`.
- Exact root post-gate: metadata-only `PASS_ABSENT_NON_SYMLINK` after process/socket/runtime-data/root cleanup.
- Complete precheck log: 1,242 bytes, SHA-256 `859126564c1046fcad755774b89a307d9b00ef2fb85ad356c5f7d43f85e4766e`.
- Daemon stdout: 716 bytes, SHA-256 `d311677a7d83ddca96e4442c8f7dbd8407180c2edb9670a3cf01634c3cd86d85`.
- Daemon stderr: 272 bytes, SHA-256 `c01aed12ccf971f55d555fb76a228eb2bb6172e0cc99f3a2b3490a2d7f6a68d0`.

No LaunchAgent, plist, bootstrap, kickstart, GUI, proof procedure, or default operator query/mutation occurred.
