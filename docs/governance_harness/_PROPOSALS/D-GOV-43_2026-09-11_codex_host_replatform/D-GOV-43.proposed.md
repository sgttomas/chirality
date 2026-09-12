# D-GOV-43 — Codex Host Re-platform: Stock App Server Owned by the App Host

Status: `PROPOSED — AWAITING OWNER RULING`

Decision ID: `D-GOV-43` (verified next free after D-GOV-42 on the preparation basis)

Date: `2026-09-11` (America/Edmonton)

Framed by: HELP_HUMAN, Chirality v3 Codex-only MVP trial session, after the
Stage26/R17 native pass and the plan/execute/workflow demonstration recorded in
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_TRIAL_COMPLETION_20260910/R17_FUNCTIONAL_FINDINGS.md`
(findings R17-F1 and R17-F2).

Accepted preparation basis: `main@a75adecf13f055c092ffa92809f66e7817c44242`
(PR #766 merge). Preparation HEAD on branch `claude/chirality-v3-mvp-trial-ab05cb`:
`03a4b41c3b0e6996c9c8e4b89c95ea25b5e3cb86`.

Supersedes if ruled: D-GOV-20 ruled-architecture items 2, 3 and 4 as they
apply to the App MVP Codex path; D-GOV-36's daemon-owned custody exception and
bootstrap namespace to the extent they presuppose that daemon; the DEL-02-08
byte-for-byte supply pin, the DEL-02-09 root-private Codex home, the DEL-02-10
closed provider-event projection and the DEL-02-11 continuity gate as
requirements on the App MVP path (their register rows are already
`RETIRED — SCA-005`; this ruling confirms the disposition). D-GOV-20 items 1,
5, 6, 7, 8 and 10, D-GOV-35's delegation-class recognition, the Codex
sole-engine rule, K-WRITE-2, K-PROJECT-1, K-STORE-2, K-ROLE-2 and K-EXPORT-1
are preserved with the re-expressions listed in "Surfaces touched".

## Decision requested

Approve or reject re-platforming the Chirality App's Codex integration from a
per-user Runtime daemon that hosts a patched, pinned, event-filtered and
configuration-vetoed Codex App Server behind a Unix socket and an SSE relay,
to a stock OpenAI Codex App Server child owned by the App's own Electron main
process, speaking the published protocol in full, against the user's own
Codex configuration and authentication, with approval and sandbox policy
chosen by the user.

## Owner direction already recorded

Owner Ryan Tufts, 2026-09-11 (America/Edmonton), in the trial session,
verbatim:

> I approve the second re-platform route. You are right to start with the
> governance, and any impacted deliverable's and their scopes of work may
> need to be revised accordingly too.

The "second re-platform route" was defined in the same session as: the
Electron main process owns a stock `codex app-server` child over one channel
to the renderer; the Next turn route and most of the daemon are dropped; the
App leans on Codex's own persistence for restart. The direction authorizes
preparing this governance packet and the revision of impacted deliverables and
scopes. It is not itself the ruling on this record; the ruling is recorded
under "Owner ruling" below when given.

The owner also stated, verbatim, in the same session:

> I need to have the Codex agents in their full glory, so to speak. There
> should not be any limits on tool use or the useful features that come baked
> in to the Codex agents.

and:

> Also, the things built to-date are also, hopefully, useful when we get to
> the local LLM server expansion for Chirality App.

## Findings that motivate the decision

Established from source at the preparation basis and from the upstream
protocol schema at Codex `rust-v0.154.0` (released 2026-09-09):

1. The Runtime daemon accepts eight Codex notification methods and
   quarantines every other item type. Command executions, file changes, MCP
   tool calls, web searches, reasoning, sub-agent items, token usage and rate
   limits never reach the App. Tool work therefore produces no stream bytes,
   the client's default 30 s socket idle timeout destroys the turn stream, and
   the daemon's close handler interrupts the turn (R17-F2). The App's Activity
   Actions view is empty by construction.
2. The daemon refuses to run unless the effective Codex configuration has
   empty `mcp_servers`, `hooks`, `plugins`, `profiles` and `notify`, plugin and
   shell-snapshot features off, approval policy pinned to `never` (or
   `on-request` only for a patched network-ask posture), and a sandbox matching
   an exact table. Codex runs in an App-private home, so the user's own
   configuration, MCP servers, skills, instructions and authentication are
   excluded.
3. The pinned App Server 0.149.0 "supplier" is patched with private protocol
   extensions (`chiralityAdmissionAuthority` on `initialize`,
   `account/identitySnapshot`, a `chiralityRuntime` carrier, a non-schema
   `permissions` thread parameter). None exist in the upstream schema. Upstream
   is five releases ahead; every release requires re-patching and
   re-qualification. The Runtime README records shell canaries still failing
   under the sandbox diagnostics for the accepted payload.
4. The App front end translates Codex into a generic multi-engine harness
   vocabulary retained from the Claude SDK and Pi eras; Codex-native items have
   no rendering target.
5. Turn transport is daemon to Unix socket to SSE to a Next API route to the
   browser, with three independent timeouts and no keepalive, re-deriving state
   that Codex persists in its own thread store. Model and reasoning are frozen
   per chat by the App although Codex accepts them per turn.
6. The upstream protocol already carries what the App needs: 101 client
   methods including `thread/start|resume|fork|list|read|compact/start`,
   `turn/start|interrupt|steer`, `model/list`, `config/read`, `skills/list`,
   `mcpServerStatus/list`, `account/login/start|logout|read|rateLimits/read`,
   `review/start`, `permissionProfile/list`; 82 server notifications including
   `item/started|completed`, `item/agentMessage/delta`,
   `item/reasoning/*`, `item/commandExecution/outputDelta`,
   `item/fileChange/*`, `item/mcpToolCall/progress`, `item/plan/delta`,
   `turn/plan/updated`, `thread/tokenUsage/updated`, `thread/compacted`; and
   ten server requests including `item/commandExecution/requestApproval`,
   `item/fileChange/requestApproval`, `item/permissions/requestApproval`,
   `item/tool/requestUserInput`, `item/tool/call` (dynamic tools) and
   `mcpServer/elicitation/request`. Codex persists threads under the Codex
   home and supports model providers, `--oss`, `oss_provider` and
   `[model_providers.<id>]` for local or OpenAI-compatible servers.
7. An open-source Electron client of the same protocol (T3 Code, MIT) already
   demonstrates a schema-generated TypeScript client, stdio launch with
   pass-through of user config arguments, a shared-config/auth-overlay Codex
   home layout, inline approvals and thread resume. Pi (MIT) is a complete
   harness with its own agent loop and is not a Codex client; it informs UX,
   not the integration.

## Proposed ruling

1. **Hosting.** The Chirality App hosts a stock OpenAI Codex App Server
   (`codex app-server` from the official `@openai/codex` distribution) as a
   child process owned by the App's Electron main process, speaking the
   published JSON-RPC v2 protocol over stdio. The App pins the exact Codex
   version in its package manifest and lockfile, records the distribution hash
   in release evidence, and updates the pin routinely with re-validation.
   Upstream drift is a dependency update, not a stop condition. No patched,
   forked or privately extended supplier is used; the private protocol
   extensions named in finding 3 are retired.
2. **Faithful transport.** The App forwards the complete App Server
   notification and server-request stream to its renderer over one long-lived
   host-to-renderer channel (Electron IPC through the preload bridge), with no
   notification whitelist, quarantine, projection to a closed generic event
   schema, or client-side idle timeout that terminates a turn. Server requests
   are surfaced to the user or answered by the user's recorded policy, never
   dropped or denied silently. Typed protocol bindings are generated from the
   upstream schema for the pinned version.
3. **The user's Codex.** The App runs Codex against the user's own Codex home
   (default `~/.codex`) with the user's configuration, MCP servers, skills,
   plugins, hooks, instructions and authentication, plus project `AGENTS.md`
   discovery. Chirality supplies role, workflow and project context only
   through supported inputs: developer and base instructions per thread,
   configuration layers, and dynamic tools. An isolated home is an opt-in
   setting modeled on a shared-configuration, auth-overlay layout; the App
   never silently substitutes a private home. There is no effective-
   configuration veto.
4. **Chosen policy.** Approval policy and sandbox mode are the user's choice
   per project with per-turn override, taken from Codex's own options
   (approval `untrusted`, `on-request`, `on-failure`, `never`; sandbox
   `read-only`, `workspace-write`, `danger-full-access`; network per the
   user's Codex configuration). The recommended new-project default is
   `on-request` with `workspace-write`. Full access is available by explicit
   user choice. The composer shows the active policy; evidence records it.
   Chirality `permissionMode` maps onto these settings and grants nothing by
   itself.
5. **Continuity from Codex.** Thread persistence, resume, fork, list,
   compaction, token usage and rate limits come from the App Server. The App
   keeps its own chat index and metadata (titles, roles, plan revisions,
   workflow selections, evidence pointers) keyed by Codex thread ID in
   operational user-data state. App relaunch resumes threads through
   `thread/resume`; the daemon's restart-admission mechanism is retired.
6. **Authentication.** Sign-in and sign-out use Codex's own
   `account/login/start`, `account/login/cancel` and `account/logout` against
   the user's Codex home, with credentials custodied by Codex as upstream
   designs. The App never reads, copies or relays credential material. This
   replaces D-GOV-36's daemon-owned custody exception and bootstrap namespace
   on the App path.
7. **Daemon retirement.** The per-user Runtime daemon, its LaunchAgent, Unix
   control socket, client tokens, accepted supervisor-socket design, hosted
   admission and identity binding, packaged-basis hashing and the SSE-over-
   Next turn route are retired from the App MVP path. K-RUNTIME-1's exclusive-
   owner language transfers to the App host process for its own App Server
   child. No network-exposed control listener is introduced; renderer access is
   through the preload bridge only.
8. **Evidence.** Chirality evidence (AgentRuns, plan revisions, workflow
   selections, actual adapter, provider and model attribution under K-ROLE-2,
   approvals given) is recorded by the App from the same event stream into
   checkout-contained project evidence where the governing workflow requires
   it. Codex's own session store is operational, non-authoritative state.
9. **Roles, skills, workflows.** HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS and
   TASK remain. Roles supply instructions and may map to Codex agent roles for
   native delegation; D-GOV-35's recognition of delegated-harness-native
   descendants stands, with its "hard outer envelope" re-expressed as the
   user-chosen policy of item 4. Skill availability follows Codex's native
   discovery (project `.agents/skills`, user `~/.agents/skills`, bundled
   skills, `skills/list`); the App catalog displays Codex's effective skill set
   with origins, and the bundled-only trust restriction on ordinary App skill
   resolution is superseded. Workflows remain Chirality project, user and
   bundled packages selected through conversation and supplied as context;
   catalog refresh remains an App function. Native Plan Mode continues through
   `collaborationMode`.
10. **Local models.** Local inference is configured as Codex model providers
    (`model_provider`, `[model_providers.<id>]`, `--oss`, `oss_provider`),
    which keeps Codex the sole engine. oMLX or other local server management
    (load, unload, residency) may be retained as App-side server management.
    This ruling does not activate a local-model path; K-RESIDENCY-1 and SPEC
    §14.3 remain prospective and are re-homed, not exercised.
11. **Measure of done.** The re-platform is complete for trial when, in one
    chat, a user plans in Plan Mode, revises once, accepts and executes with
    real file reads and tool use, saves the method as a workflow, and every
    action is visible in Activity, with no read-free workaround and no
    interrupted turn attributable to transport.
12. **Exclusions.** This ruling does not authorize release, publishing,
    acceptance of unknown future bytes, any change to the Codex sole-engine
    rule, any change to Root decomposition workflows, or reliance on the
    retired daemon path.

## Surfaces touched by the proposed ruling

Ratified Root surfaces to be amended in the application tranche (M2/G4):

- `AGENTS.md` — Skills paragraph (bundled-only trust) and the Execution and
  governance section; the exact inactive delta is `AGENTS.proposed.patch`.
- `docs/CONTRACT.md` §1.13 — re-express K-RUNTIME-1 (App host owns the App
  Server child), K-CONTROL-1 (no network control listener; the daemon socket
  and supervisor-socket design retired), K-RESIDENCY-1 (prospective, re-homed
  to App-side server management), and the §1.13 closing paragraph and the
  enforcement-map row "Shared runtime daemon and clients".
- `docs/SPEC.md` §14 — replace §14.1 (local control plane) with the App-host
  App Server child description; keep §14.2 project manifests, re-express
  session storage as Codex thread store plus App index; mark §14.3 and §14.4
  prospective/historical.
- `docs/DIRECTIVE.md` §5 constraint row "No external server requirement" and
  §7 Shared Runtime Direction.
- `docs/TYPES.md` §12 — retire `RuntimeClientCredential`,
  `RuntimeDaemonStatus`, `RuntimeBackend`; add `CodexHostStatus`,
  `CodexThreadIndexEntry`, `ApprovalRecord`, `PolicySelection`.
- `docs/AGENT_WORKFLOW_RUNTIME.md` — skills paragraphs (bundled-only) and the
  `permissionMode` sentence, aligned to items 4 and 9.
- `docs/PLAN.md`, `docs/PRD_ROOT.md` — the D-GOV-20 transcriptions read with
  this amendment; PRD annex text per its own amendment rule.

Decision records superseded in the stated parts, never edited: D-GOV-20,
D-GOV-36. Decision records read with this ruling: D-GOV-28, D-GOV-35,
D-GOV-37 through D-GOV-42.

Project-loop surfaces receiving routed M6 notices (owned by their loops):
`projects/chirality-runtime` (CODEX_MVP_INTEGRATION.md, PRD, PRD_AUTHORITY,
AGENTS.md, package READMEs) and `projects/chirality-app-dev` (AGENTS.md, trial
checklist and acceptance criteria, packaging stages, D-APP-126). The impact
file enumerates them.

## Application, compatibility, and closure gates

1. Owner ruling on this record (K-AUTH-1).
2. Application tranche with its own M2/G4 manifest applying the listed Root
   amendments and routing the M6 notices.
3. App and Runtime loops revise their deliverables and scopes under their own
   instruments; the App loop's trial checklist keeps its nine UI acceptance
   criteria and re-expresses restart admission as "relaunch resumes the last
   thread".
4. A spike before any consolidated build: generated bindings against the
   pinned Codex, a thin host client with full item rendering and approvals,
   run against item 11 in a trial project. Existing trial evidence and the R17
   installation are preserved, not deleted.
5. One consolidated signed build after the spike passes, then independent
   review, then the owner's trial.

## Owner ruling

Not yet recorded.
