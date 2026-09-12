# Spike acceptance evidence (S-1..S-8 and the disconnect check)

Recorded by the implementing session from source (`npm run dev` in
`projects/chirality-app-dev/frontend` with a distinct `userData` and the
App's own effective Codex home; the R17 installation and the owner's
`~/.codex/auth.json` untouched). Times UTC. Logs filtered with `grep -v '@'`.
The owner performs OAuth; no credential is entered by the agent.

| Check | Status | Evidence |
|---|---|---|
| S-1 native Plan Mode with revision | pending | |
| S-2 execution with real file reads and tool use beyond 30 s silence | pending | |
| S-3 save workflow through conversation | pending | |
| S-4 reuse and iterate | pending | |
| S-5 delegated task; child demonstrably receives role instructions | pending | |
| S-6 quit and relaunch continuation | pending | |
| S-7 interruption and approval handling incl. denied approval | pending | |
| S-8 sign-in/out scoped to Chirality; other Codex client unchanged | pending | |
| Renderer disconnect during tool work; recovery; no duplicate execution | pending | |

## Notes

### 2026-09-12T08:56Z launch from source (candidate 5fe619fdd)

- `npm run dev` in `frontend/` with `CHIRALITY_USER_DATA` under the session
  scratchpad, `CHIRALITY_RUNTIME_SOCKET_PATH=/private/tmp/claude-501/spike-a2.sock`
  (socket path length limit), and the client token, runtime directory and
  instruction root exported for the separate `next dev` process. No LaunchAgent,
  no R17 userData, no R17 Codex home.
- Desktop log (filtered), same second: `desktop.gui.starting` 08:56:17.235Z;
  `runtime.service.config_written` .376Z; `runtime.service.spawned` pid 61023
  (`packages/daemon/dist/standalone-bin.js`) .378Z; `runtime.service.ready` .756Z
  with the socket and client token file; `runtime.connectivity.state connected`
  .763Z. One expected `bind_failed` at .247Z before the token file existed.
- Codex child: pid 61025, parent 61023, the pinned binary under
  `node_modules/@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin/bin/codex`
  with `-c cli_auth_credentials_store=file`; `service-config.json` records
  `expectedVersion 0.154.0`. The owner's other Codex client (ChatGPT desktop's
  app-server, started hours earlier) is untouched.
- Effective Codex home `<userData>/runtime/codex-home`: 60 symlinks into
  `~/.codex` (`config.toml`, `sessions`, `archived_sessions`, ...), zero regular
  files, no `auth.json`. The App is signed out until the owner completes OAuth.
- App path through the Next server: `GET /api/harness/hosted-bootstrap/status?projectRoot=<app-dev>`
  returned `{"registration":"required"}` over the per-launch client token (the
  5fe619fdd fix); `/api/harness/roles` returns 400 before a folder is bound.
- Blocked on the owner: bind a project folder in the App window and sign in
  (OAuth in the browser). S-1..S-8 follow from that point.
