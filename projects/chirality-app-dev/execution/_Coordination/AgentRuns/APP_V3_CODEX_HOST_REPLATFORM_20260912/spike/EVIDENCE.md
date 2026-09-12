# Spike acceptance evidence (S-1..S-8 and the disconnect check)

Recorded by the implementing session from source (`npm run dev` in
`projects/chirality-app-dev/frontend` with a distinct `userData` and the
App's own effective Codex home; the R17 installation and the owner's
`~/.codex/auth.json` untouched). Times UTC. Logs filtered with `grep -v '@'`.
The owner performs OAuth; no credential is entered by the agent.

| Check | Status | Evidence |
|---|---|---|
| S-1 native Plan Mode with revision | PASS | Session a86fdf49 created with `interactionMode: native-plan`; capability route reports the Codex adapter under the D-GOV-43 trial disposition. Turn 15:09:48.7Z: `thread/settings/updated` at .865Z (Plan Mode applied), three read-only tool reads, `plan` item 15:10:03.2Z to 15:10:12.4Z; revisions route lists revision 1 (six-step test plan). Revision turn 15:10:50Z: revision 2 present, first step now reads the existing status-view tests and the last two steps are merged, as requested. |
| S-2 execution with real file reads and tool use beyond 30 s silence | PASS | Session 5517a692 (HELP_HUMAN, readOnly). Turn d226da39 15:06:48.8Z to 15:07:05.3Z: two `commandExecution` tools (`head -n 40 AGENTS.md`, `cat chirality.project.json`) started 15:06:58.965Z, completed .982Z; 138 text deltas; correct three-sentence answer naming the four roles; 158 events persisted, 0 malformed; turn state `active:false, lastSeq 161`. Second turn 15:07:56.0Z to 15:08:45.6Z: `sleep 40 && echo done-sleeping` started 15:07:59.756Z, completed 15:08:39.650Z (39.9 s silent), then `cat frontend/package.json`; the same App stream carried `turn.completed`. Note: the App proxy emitted no comment keepalive during the silence (added afterwards, see notes). |
| S-3 save workflow through conversation | PASS | Session 30f2b92c (HELP_HUMAN, workspaceWrite). One conversational request at 15:14:31Z; the agent read the staged instruction root's workflow docs and bundled packages (one `sed` on a docs path failed and it recovered), wrote `.chirality/workflows/summarize-folder/WORKFLOW.md` through a `fileChange` item at 15:15:19.8Z, validated the metadata, and replied with the path and `Workflow: summarize-folder`. The package has the `name`/`description` front matter, required inputs, a five-step method, outputs and a completion check. The App methods route lists it as kind workflow, origin project, among 79 methods. |
| S-4 reuse and iterate | PASS (after a fix) | Reuse: session d4015835 created at 15:17:48Z with `selectedMethods: [{kind: workflow, name: summarize-folder}]` (resolved to the project-qualified reference); turn `Workflow: summarize-folder. Apply it to frontend/electron` 15:17:49.9Z to 15:18:16.1Z followed the saved method (listing, README/AGENTS check, three-sentence summary, risk line). Iterate: the saving session revised the workflow on request at 15:19:14Z (new step 3, counts by extension). Applying the revised workflow in the reuse session at 15:20:56Z failed with `RUNTIME_COMPATIBILITY_MISMATCH` (`successorRequired`), and re-selecting the same method through the transition route failed with "cannot prepare a reversible context successor": the retained v3 successor machinery blocked additive instruction changes on the Codex path. Fixed in the Runtime (additive transitions for engines without successor preparation; changed instruction bytes re-freeze with the accepting turn); after the App restart the same turn at 15:26:24Z to 15:27:05Z applied the revised workflow, including the new extension-count table for `frontend/scripts` (30 `.mjs`, 3 `.ts`, 1 `.json`). The composition test covers the same-process case where the next `turn/start` carries the `Chirality context update:` item. |
| S-5 delegated task; child demonstrably receives role instructions | PASS (with note) | Session 96ce0a33 (WORKING_ITEMS, readOnly), turn 15:15:20.8Z to 15:16:15.4Z. The parent used Codex's `spawn_agent` (child thread 01a09630-2b92, agent path `/root/count_electron_typescript`) and two `wait` calls; the App recorded `subagent.progress` (subAgentActivity started/completed) and `subagent.started`/`subagent.completed` (collabAgentToolCall) events with the child thread id. The child's verbatim report (21 TypeScript files; `main.ts` 979 lines, `renderer-window-policy.ts` 774, `runtime-service-host.ts` 548, all correct) states that its inherited context carried the full WORKING_ITEMS role body plus Root and project AGENTS instructions, and that the parent's assignment named TASK and prohibited delegation. Note: the evidence of what the child received is the parent's `fork_turns: all` spawn arguments and the child's own account; the child thread's `thread/started` payload is not in the parent's event stream, and the TASK role body itself was not supplied to the child. |
| S-6 quit and relaunch continuation | PASS | The App was quit and relaunched three times during the run (desktop log: `desktop.shutdown.started before-quit` 14:50:45.582Z, 15:00:22Z, 15:25:1xZ; each time `runtime.service.stopping`, `codex.app-server.exit signal SIGTERM`, then after relaunch `runtime.service.ready` and `connectivity connected` within a second). Sign-in survived every relaunch (status `signed-in`, no new OAuth). Session 5517a692, whose two turns ran at 15:06Z and 15:07Z before all three relaunches, answered at 15:28:12Z without new reads: it named `chirality.project.json`, the first 40 lines of `AGENTS.md`, and `sleep 40 && echo done-sleeping`, all correct, so the Codex thread continued across the relaunch. Session d4015835 likewise continued after the 15:25Z relaunch (S-4). |
| S-7 interruption and approval handling incl. denied approval | PASS | Session a692d792 in `ask` mode; the thread started with `approvalPolicy: on-request`, `sandboxPolicy.type: workspaceWrite` (Codex notification params). Denied approval, turn 15:13:28.4Z: a write to `projects/pec/` (outside the workspace) raised `item/commandExecution/requestApproval` at 15:13:39.380Z, listed by the session requests route with the command and reason; answered `deny` at 15:13:43Z through the answer route; `codex.request.resolved` (answered, decidedBy user) and `tool.permission deny` at 15:13:44.18Z; `tool.failed` status declined; the assistant reported the decline and stopped; no file exists at the target. A prior attempt at `/private/tmp` needed no approval because Codex's workspace-write sandbox treats the temp directory as writable, and a plain refused write ("operation not permitted") raised no request until escalation was asked for. Interruption, turn 15:14:32.2Z: `sleep 120` started 15:14:36.480Z; interrupt route at 15:14:42Z returned ok; `turn.interrupted` at 15:14:43.320Z (exit 130, interrupted true); turn state inactive; a follow-up turn on the same session answered within 3 s with no thread resume (no retirement). |
| S-8 sign-in/out scoped to Chirality; other Codex client unchanged | pending | |
| Renderer disconnect during tool work; recovery; no duplicate execution | PASS at the App transport level; window-level repeat by the owner pending | Session a692d792, turn 4d2b9f73 started 15:19:45.2Z with `sleep 45 && echo slept-45`. The consuming stream (the same App route the renderer uses) was killed at 15:19:51Z after frame seq 21 while the command ran; turn state then reported `active: true, lastSeq 21`. Reattached at 15:20:12Z through `turn/stream?after=21`: frames resumed at seq 22 with no gap, carried `tool.completed` (15:20:34.113Z, one completion for the one start) and `turn.completed` (15:20:37.051Z), and the answer `slept-45`. The command ran once. |

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

### 2026-09-12T15:31Z renderer boot finding (owner's first chat from the window)

- The owner's first chat from the App window sat at "Booting session..." and failed after
  150 s with `ENGINE_UNAVAILABLE` ("Chat took too long to start"). The renderer boots a
  session before its first message through the legacy boot turn, which sends the reserved
  prompt "bootstrap" as a real engine turn; on the Codex path that turn never reached the
  app-server (session 200147dd: one `turn.accepted boot:true` event, nothing after).
- Fix: the Codex adapter declares `boot: "none"`; boot records readiness and the
  fingerprint without a turn. Verified after relaunch at 15:37Z: boot 258 ms through the
  App route, first turn answered `booted`. No user prompt named "bootstrap" is ever sent.
