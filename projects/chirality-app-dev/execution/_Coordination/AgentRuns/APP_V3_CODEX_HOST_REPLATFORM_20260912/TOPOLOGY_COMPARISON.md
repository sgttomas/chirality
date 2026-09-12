# Codex host topology comparison (D-GOV-43 ruling items 1 and 7 reopened)

Prepared 2026-09-12 by HELP_HUMAN at the owner's direction after the
independent reviewer's counter-proposal. Basis: branch
`claude/chirality-v3-mvp-trial-ab05cb` at `930df6d1d`; product source is
unchanged since the D-GOV-43 preparation basis. Method: read-only inspection
of `projects/chirality-runtime/packages/*`, `projects/chirality-app-dev/frontend`
and `projects/pec/server`; no builds, tests or experiments. Line counts are
`wc -l`. Every conclusion is marked established from source (E) or judgment
or unverified (U). The objective, in the reviewer's words, is "the smallest
coherent implementation that delivers this experience".

## 1. Facts from source that frame the choice

- **F1 (E). The daemon is the App itself.** The LaunchAgent runs the Chirality
  executable with `--runtime-daemon`; Electron main in that mode hosts the
  Runtime in-process (`frontend/electron/main.ts:958` `initializeDaemon`,
  `runtime-host.ts:208` `startRuntimeHost`). launchd owns it with
  `KeepAlive: always` (`desktop-daemon-posture.ts:42`). In GUI mode the App
  spawns nothing; the daemon spawns the GUI on `activate` (`main.ts:1191`).
- **F2 (E). An in-process host already existed.** `runtime-host-legacy.ts`
  (686 lines, "Historical in-process host retained for compatibility tests")
  constructed `RuntimeService`, the registries and a `RuntimeDaemon` inside
  the GUI process. The packaged-boundary script forbids it from the bundle.
- **F3 (E). The turn path crosses three processes and two sockets.**
  `codex-session.ts` (stdio JSON-RPC) inside the supervisor job, behind the
  second Unix socket (`supervisor-server.ts`, 286) → `SupervisorClient` in the
  daemon → `DelegatedRuntime` / `TurnCoordinator` → `UIEvent` → daemon SSE
  (`runtime-daemon.ts:925`) → `RuntimeClient` (`packages/client`, 886) → the
  harness port (`runtime-daemon-harness-port.ts`, 1,033; a cast, no mapping)
  → Next route in-process in Electron main (`api/harness/turn/route.ts`) →
  browser SSE → the v1 `HarnessEvent` provider. The Next server runs inside
  Electron main and is required for the pages themselves (`main.ts:543-650`).
- **F4 (E). The silence defect has three sites.** `client.ts:139` default
  30 s; `requestSse` (`:177-183`) passes no `timeoutMs`; the daemon writes no
  keepalive (`runtime-daemon.ts:966-991`); the close handler interrupts the
  turn (`:955-959`, `:1002`, `:1028`). No reconnection exists anywhere
  (`sse.ts`, `client.ts`).
- **F5 (E). `codex-session.ts` is two-thirds reusable.** About 700 of 1,064
  lines are Codex-generic (framing, correlation, thread/turn calls, login,
  interrupt, native plan, network approvals, user input, dynamic tools).
  About 360 are Chirality-private (authority initialize `:637-702`, identity
  snapshot, native-child carrier `:489-524`, role TOML pins `:213-234`,
  policy override `:862-875`). The whitelist is at `:545` (8 methods), the
  item-type quarantine at `:624`. Of Codex's ten server-request methods only
  three are handled; any other throws a protocol error (`:291`), which fails
  the session rather than answering Codex. The config veto is `:788-821`.
  `turn/start` already sends model, reasoning effort and `collaborationMode`
  per turn (`:934`); the per-chat freeze is App-side only
  (`chat-panel.tsx:103`, `:751`).
- **F6 (E). Containment is a macOS-only outer sandbox.** `codex-containment.ts`
  (611) wraps Codex in `sandbox-exec` with a private `CODEX_HOME`, a closed
  environment and `-c` overrides including `approval_policy=never` and
  `cli_auth_credentials_store` file or keyring (`:163`). It fails closed off
  macOS.
- **F7 (E). The private admission and supplier family is about 4,400 daemon
  lines** (`hosted-*`, `host-account-*`, `supplier-authority-*`,
  `codex-admitted-launcher`, `hosted-packaged-release*`,
  `runtime-conformance-v2-admission`, `account-free-login-observation`),
  plus the `native-admission` addon, `core/exact-supply.ts`,
  `core/runtime-conformance-v2.ts`, the packaging payload and seal phases
  and the App's host-account XPC client. Its purpose is to trust a privately
  built binary and to re-trust each GUI. Ruled items 1 to 4 retire it under
  every topology.
- **F8 (E). The reusable core is real.** `packages/core` (34 files, 8,031
  lines): project registry, session store (`session.json` and `events.jsonl`
  under `runtime/projects/<id>/sessions`), turn coordinator, method catalog
  and runtime method service (workflows, native plan), approvals, consent,
  retirement, process supervisor, instruction basis store. Codex-coupled
  pieces are small (`hosted-consent.ts` home, `delegated-engine-adapter.ts`
  213, `native-role-config.ts` 199, `exact-supply.ts` 235). `engine-claude`
  is dead code; `engine-pi-omlx` is registered only on the local-model path.
- **F9 (E). The v2 event contract is orphaned.** `HarnessEventTypeV2` has 16
  members, only four terminals are produced, and neither the daemon nor the
  App reads it. The live vocabulary is the eight-name `UIEvent` set
  (`sse.ts:62-71`) carrying v1 `HarnessEvent`. Views for tools, sub-agents,
  inline approvals and plan clarifications exist (`tool-stream-view.tsx`,
  `subagent-stream-view.tsx`, `permission-requests.tsx`,
  `NativePlanClarificationCard`) but receive nothing for tool work because
  of F5.
- **F10 (E). Socket consumers.** The Runtime CLI (`cli.ts`, a full client;
  nothing in the repo depends on it) and the PEC server (a real dependency
  on `@chirality/runtime-client`, `pec/server/src/shared-runtime-client.ts`,
  failing closed by default). The App is the only production consumer.
- **F11 (E). The port is the seam.** `DaemonHarnessPort` (21 methods) and
  `HostedBootstrapPort` (7) sit behind a `globalThis` registry designed for
  more than one implementation; the 27 Next routes are thin delegates.
- **F12 (E). The two-job launchd pair exists to keep the authority secret out
  of the daemon.** With F7 retired, the second socket has no purpose under
  any path.

## 2. Work common to every path

| Item | What changes | Modules |
|---|---|---|
| C1 Stock Codex, no private protocol | Remove the ~360 private lines; stock `initialize`; drop role TOML pins, the non-schema `permissions` parameter and the policy override; policy from the user's choice | `codex-session.ts`, `core/native-role-config.ts`, `core/runtime-conformance-v2.ts` |
| C2 Full event delivery and requests | Replace the whitelist and quarantine with pass-through; extend the producer chain (session events → delegated engine adapter → turn coordinator → `UIEvent`/`HarnessEvent`) and the consumer (provider, activity shelf, cards) with tool activity, file changes, reasoning summaries, plan, sub-agents, usage; answer all ten server-request methods, unknown ones with a JSON-RPC error and a visible outcome | `codex-session.ts`, `core/delegated-engine-adapter.ts`, `core/turn-coordinator.ts`, `contracts`, `sse.ts`, App provider and views |
| C3 Lifecycle | `thread/resume` (already at `:893`) on relaunch; index chats by thread id in the session store; interruption only on explicit cancel | `codex-session.ts`, `core/session-store.ts`, App chat index |
| C4 Effective home and separated auth | Replace the private home, Seatbelt and `-c` overrides with the overlay layout (shared config, skills, plugins, MCP, sessions by link; private `auth.json` and models cache; `cli_auth_credentials_store=file`); remove the config veto; keep the existing login flow (`:709-752`, `codex-login.ts`) | `codex-containment.ts`, `codex-login.ts`, `core/hosted-consent.ts` |
| C5 Retire the F7 family | Daemon modules, native addon, core conformance and exact supply, packaging payload and seal phases, App host-account XPC | as F7 |
| C6 UI | Per-turn model and effort; cards for approvals, questions, tool activity and delegation built on the existing views; workflows prominence | `chat-panel.tsx`, `activity-shelf.tsx`, `permission-requests.tsx`, workflows views |

Judgment (U): C1 to C6 are 70 to 80 percent of the total effort and are
identical under A1, A2 and B. Topology decides the rest.

## 3. The small repair, kept separate

Three sites fix R17-F2 as a transport defect: pass a long or disabled
`timeoutMs` on the stream path (`client.ts:177-183`), send SSE comment
keepalives from `sse()` (`runtime-daemon.ts:966-991`), and stop interrupting
on connection close (`:955-959`). Under fifty lines. It makes long silent
turns survive but shows no tool activity, because F5 still discards it. It
is not an argument for or against any topology.

## 4. The three topologies

### A1. Retain the launchd daemon, simplified

- Survives: F8; `runtime-daemon.ts` routes, SSE, tokens and stop generations
  (minus the hosted-bootstrap routes and account proofs); the client, port
  and Next routes; autostart, socket watcher and connectivity supervisor;
  the CLI and PEC socket.
- Changes beyond C1 to C6: fold the supervisor job into the daemon (F12) or
  keep two jobs; keepalive and timeouts; reconnection after a GUI restart
  (none exists, F3) or accept losing the live turn; shutdown ordering across
  three processes.
- Retires: F7, the host-account XPC, restart admission.
- Dependencies: easy because the daemon mode and the port exist. Hard:
  reconnection is new work; DEL-09-07 and `APP-HOLD-1` stay live; the
  daemon's lowest pid keeps defeating Computer Use attachment after a GUI
  restart.
- Acceptance: S-6 is partly native (the daemon keeps running) but the App
  must still re-attach to the chat; the rest as common.
- Effort (U): least new code, most retained code. Migration risk: low to
  medium. Lifecycle: the most complex (three processes, launchd,
  `KeepAlive`). Maintenance: highest (socket protocol, tokens, SSE,
  reconnection, launchd, installer).

### A2. Runtime host as an App-owned child process

- Survives: as A1 minus launchd. The GUI spawns `<exe> --runtime-daemon` (or
  a Node entry) with a private socket directory; `descendant-tracker.ts` and
  `process-supervisor.ts` are reusable for orphan handling.
- Retires in addition: `runtime-autostart.ts` (182), `cli/launch-agent.ts`
  (442), `runtime-jobs.ts` (82), `daemon-activate-policy.ts` (116), the
  `runtime.daemon` IPC operations, DEL-09-07 and `APP-HOLD-1`, the pid
  ambiguity.
- Changes: child lifecycle (spawn, crash and quit ordering); keeps socket,
  tokens, client, daemon SSE with keepalive, port and Next routes.
- Acceptance: S-6 becomes relaunch plus `thread/resume` (C3), the same as B.
- Effort (U): a modest delta from A1 with about 800 lines removed. Risk:
  low to medium. Lifecycle: two App-owned processes. Maintenance: the
  transport layer remains, about 2,600 lines (client 886, port 1,033,
  `sse.ts` 99, daemon routes and SSE roughly 1,000, `supervisor-server.ts`
  286 if kept).

### B. In-process host behind the existing port

- Survives: F8; the generic part of `codex-session.ts`; `CodexSupervisor`
  and `CodexLogin` in-process; `RuntimeService`; the port seam with a new
  in-process implementation of the 21 plus 7 methods replacing the
  1,033-line client-backed one; the Next routes and browser SSE for the
  renderer in the first iteration (they run in-process and are required for
  pages anyway), with preload IPC as a later refinement.
- Retires in addition to A2: `runtime-daemon.ts` HTTP and SSE, `RuntimeClient`
  in the App, App token provisioning, `supervisor-server.ts`,
  `signal-shutdown.ts` and stale-socket recovery, the connectivity
  supervisor, socket watcher, host-account connection and runtime-control
  IPC.
- Precedent: F1 and F2. Daemon mode already hosts these services in
  Electron main; the legacy host did so in the GUI process.
- Changes: a new minimal composition (`RuntimeService`, `DelegatedRuntime`,
  `CodexSupervisor`, `CodexLogin`, effective home) replacing
  `hosted-private-composition.ts` (767); the in-process port; `teardown()`
  already stops `runtimeHost` on quit (`main.ts:1029-1081`).
- Acceptance: S-6 as A2. S-7 interruption becomes a direct call.
- Effort (U): the largest deletion (about 4,000 lines of transport and
  lifecycle beyond F7) against roughly 500 to 800 new lines (composition
  and port). Risk: medium, because the composition is new and a GUI crash
  ends the Codex children (mitigated by Codex's thread persistence).
  Lifecycle: one process. Maintenance: lowest.
- Consequence: the CLI and PEC lose the socket unless `RuntimeDaemon` is
  kept as an optional listener over the same in-process service, which its
  constructor allows (`RuntimeDaemon({ service, delegated, socketPath })`).

## 5. Governance by purpose, independent of topology

The family dispositions in the D-GOV-43 `IMPACT.md` hold under every path:
family 1 (F7) and family 2 (fixed-policy control) retire; family 3 adapts to
the overlay home; ordinary integrity, human decisions and independent source
review are retained; whitespace, self-hash and duplicate test runs stop
being gates. What differs is the Root text each path forces:

| Path | K-RUNTIME-1, K-CONTROL-1, SPEC §14.1 | Installer hold |
|---|---|---|
| A1 | Spine intact (one per-user daemon on a Unix socket, no TCP); amend admission, supplier, veto and supervisor-socket clauses | DEL-09-07 and `APP-HOLD-1` stay |
| A2 | "opt-in per-user LaunchAgent daemon" becomes "App-owned child"; socket clauses intact | retired |
| B | Re-expressed as in the ruled packet | retired |

## 6. Established versus uncertain

Established: F1 to F12; the module lists in C1 to C5; the three repair sites;
the precedent for an in-process host; that the overlay needs the file
credential store (`cli_auth_credentials_store` exists; T3's multi-account
note requires `file`).

Uncertain:

- U1. All effort figures are judgment.
- U2. Whether `DelegatedRuntime` accepts `CodexSupervisor` directly without
  the supervisor socket. The port type
  (`contracts/delegated.ts:45 DelegatedHarnessProcessSupervisorPort`) is
  implemented by `CodexSupervisor`; production wiring goes through
  `SupervisorClient` (`standalone.ts:225-255`). Resolvable by reading, not
  by experiment.
- U3. Server-request round trips through loopback SSE plus POST. The network
  approval path proves the shape (`permission-requests.tsx` →
  `/api/harness/permission` → daemon → `replyNetworkApproval`); the other
  request types follow it. Presumed, not exercised.
- U4. Credential backend separation is verified only by S-8.
- U5. Dropping the outer Seatbelt wrapper. Ruled item 4 makes policy the
  user's and Codex's own sandbox applies; the wrapper is Chirality's private
  fence and macOS-only. Recommended drop, owner's call.
- U6. Whether the PEC loop needs a socket inside the MVP window.
- U7. A1's reconnection work is unsized.

## 7. Recommendation

- **Not A1.** Its one unique benefit, a daemon that outlives the GUI, is not
  required by any of S-1 to S-8, and it is the source of the retired defect
  class, the installer hold, the pid ambiguity and reconnection work that
  does not exist.
- **B over A2, narrowly.** The daemon already runs in Electron main (F1); the
  port seam (F11) and the legacy host (F2) show the shape. The socket layer
  buys only a process boundary and a CLI socket, at about 2,600 lines of
  transport to keep correct. Keep the Next loopback routes and browser SSE
  for the renderer in the first iteration; treat preload IPC as a later
  refinement. This narrows the ruled item 2 wording ("one long-lived
  channel through the preload bridge") to its purpose: validated shapes,
  `contextIsolation`, no credential material in the renderer, no idle
  timeout that ends a turn.
- **A2 is the fallback** if U2 resists or the CLI and PEC socket matters in
  the MVP window. The difference from B is confined to the host composition
  and lifecycle; C1 to C6 are identical. No bounded experiment is needed.
- **Reuse, not rewrite.** B as described keeps the core (F8), two-thirds of
  the Codex session code (F5), the supervisor and login modules, the port,
  the routes and the existing views. That is a refactor of the existing
  host, which is what the counter-proposal asked to compare, with the host
  moved into the process that already runs it in daemon mode.

Where this differs from the reviewer's assessment: "reconfigured" is not
sufficient (C1, C2 and C4 are source changes); T3 keeping a server serves
remote clients and several providers that Chirality does not have; and my
own earlier framing of B as a replacement was wrong, since the in-process
host reuses more than it discards.

Decision requested from the owner: B or A2, and whether an optional socket
listener for the CLI and PEC is in the MVP (recommended: no). The ruled
D-GOV-43 record then receives a one-paragraph supplement recording the
reopening and the outcome; items 2 to 6 and 8 to 14 stand as ruled.

## 8. Addendum: embedding in later Chirality applications (owner context, 2026-09-12)

The owner added that the same agents and agent host are intended to be
embedded in later Chirality applications, first Chirality Piping
(`projects/chirality-piping`, also called SWBPIPE and OpenPipeStress), with
local models operating with Codex inside those applications; a vague notion
today, while the Chirality App is close to its release candidate.

Facts checked (E):

- Chirality Piping is a Tauri desktop application: Rust core crates
  (`core/*/Cargo.toml`), a Vite and React front end
  (`apps/desktop/package.json`), WASM builds. It is not Electron and has no
  dependency on, or documented intent about, the Runtime or agents.
- A spawnable service shape already exists: `standalone-bin.ts` (35 lines,
  package bin `chirality-runtime-service daemon|supervisor --config <path>`)
  starts the host as a plain child process and prints its socket path on
  stdout. No launchd involvement.
- PEC is a present out-of-process consumer of the socket API (F10).

Consequences:

1. **A Node in-process library cannot be embedded in a Tauri main process.**
   A later application either runs the host as a sidecar process and speaks
   its socket API, or spawns `codex app-server` itself and re-implements the
   thin Chirality layer. Either way the reusable unit for other
   applications is the service composition plus a protocol-first Chirality
   layer (roles as developer instructions, workflows as files, plans through
   native collaboration mode, evidence as files), which ruled items 8 to 10
   already prescribe.
2. **This moves the recommendation from B to A2.** Under A2 the Chirality App
   spawns the same service composition a sidecar would use, so the flagship
   exercises the embedding path every day, PEC and the CLI keep working, and
   the transport layer that B would delete (client, port, routes, daemon SSE,
   about 2,600 lines) is retained rather than rebuilt later. A2's new code
   is smaller than B's: child lifecycle in Electron main (reusing
   `standalone-bin.ts`, `descendant-tracker.ts`, `process-supervisor.ts`)
   plus the small repair of section 3, against B's new in-process port.
   The composition work (replacing `hosted-private-composition.ts` with a
   minimal one) is common to both. B remains the smaller choice only if the
   embedding intent is set aside.
3. **Unchanged:** not A1; the common work C1 to C6; the F7 retirement; the
   governance families. A2 also keeps K-RUNTIME-1, K-CONTROL-1 and SPEC
   §14.1 closest to their present text (a Chirality host process on a Unix
   socket, no TCP), changing only the launchd, per-user and exclusive-owner
   clauses to "application-owned child".
4. **Local models refine, not reverse, ruled item 13.** Codex reaches local
   models through model providers over a local base URL. What several
   applications would have to share is the local model server itself (GPU
   residency), which is a per-user service separate from the Codex host.
   The daemon-era `ResidencyCoordinator` and `engine-pi-omlx` code is the
   seed of that future service and should be kept compiling as reference,
   as item 13 already says; it does not justify a per-user Codex-host daemon
   (A1).

Revised recommendation: **A2**, the Runtime host as an application-owned
child speaking the existing socket API, with the same composition
packaged as a spawnable service for later applications; B if the owner sets
the embedding intent aside for the MVP. Decision requested: A2 or B, and
whether Piping's future integration is to be recorded now as a design
constraint in DIRECTIVE §7 or left for its own loop.

## 9. Corrections after review (2026-09-12)

- Section 3 named three disconnection sites; there is a fourth. The App's
  turn route passes the browser request's abort signal into the port and
  calls the port's `cancel()` when its stream is cancelled
  (`frontend/src/app/api/harness/turn/route.ts:17-40`), and that cancel
  issues a fresh interrupt (`runtime-daemon-harness-port.ts:556-562`). A
  renderer disconnect is therefore indistinguishable from an explicit Stop
  today. The repair is the four sites plus a rule: Stop is an explicit
  interrupt call; stream teardown is loss of observation only; reopening
  recovers the turn's actual state.
- "A2's new code is smaller than B's" is an estimate. Source establishes the
  reusable interfaces and an existing transport; implementation establishes
  how much survives cleanly.
- The standalone entry's hosted branch routes into the retired admission
  composition (`standalone.ts:182`); reuse is of its shape, not its
  composition, and the core's conformance, exact-supply and private-home
  checks need deliberate removal.
- "PEC keeps working" (section 4, B) overstated: A2 preserves PEC's
  integration opportunity; compatibility is unverified and not an MVP
  prerequisite.
- Section 8's GPU statement was categorical; memory and server capability
  decide. Preserving prior Pi and oMLX work creates no obligation to keep it
  compiling.
