# R19 direct disposable packaged-daemon precheck

- Attempt count: exactly `1`
- Execution-tool posture: local Unix/loopback socket permission only; no
  external network request or network tool
- Exact tool command: `/bin/zsh projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R19_STAGING_2026-08-23/instances/WI-PKG09-R19-STAGING-01/executor/empirical-precheck.sh`
- Script SHA-256 before execution:
  `47893a0a53366a4831795ee870c445c78323b07ec05362767f2143bd308c12be`
- Started: `2026-08-23T06:25:03Z`
- Exact packaged executable argv:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality --runtime-daemon`
- Environment: exact `CHIRALITY_USER_DATA=/private/tmp/ch-r18-91499728-51dd/runtime-data`,
  `CHIRALITY_SKIP_CLI_LAUNCHER=1`, `CHIRALITY_DAEMON_GUI_SPAWN=0`
- PID: `16906`; `ps` matched the exact executable and argv
- Exact socket was a Unix socket at `67` UTF-8 bytes
- Authenticated packaged CLI health:
  `ELECTRON_RUN_AS_NODE=1 <packaged-executable> <packaged-cli> project list --json`
  returned exact `[]`
- Graceful SIGTERM requested: `2026-08-23T06:25:09Z`
- Daemon log recorded `runtime-daemon-signal` shutdown; process exit: `0`
- Stopped: `2026-08-23T06:25:10Z`
- Cleanup: process, socket, exact runtime-data, and exact root absent; proof
  plist and public destination remain absent
- Daemon stdout SHA-256:
  `ee065b0a0739f74358e1e6d168c4cdc14a28481bdb629bcc6bfa0140b9a648d1`
- Daemon stderr SHA-256:
  `845c90a6010b99eebd1c956d4389cc07ba46e6e4759226ce89209c92cd5869cc`

No GUI or LaunchAgent/plist/bootstrap/kickstart/default-operator action
occurred. The instruction-root fallback warning was expected for an
unregistered disposable user-data root and did not affect authenticated local
control health.
