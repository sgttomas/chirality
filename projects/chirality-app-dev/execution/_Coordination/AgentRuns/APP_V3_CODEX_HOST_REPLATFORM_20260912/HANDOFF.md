# Codex host re-platform (D-GOV-43, topology A2) — implementation handoff

Prepared 2026-09-12 by HELP_HUMAN for a separate implementing session,
revised the same day to the selected topology. Read Root `AGENTS.md`,
`PERSPECTIVE.md` (the owner's intent) and this file first. This file is
coordination, not governance: the governing records are the D-GOV-43 ruling
and its A2 supplement.

## 0. Preconditions — verify before any work

1. **Basis.** `main` at or after the merge of
   [PR #767](https://github.com/sgttomas/chirality/pull/767),
   `d2878462be59a43b4afc175a8cce85abca9cf696`, which contains everything
   named below. The proposal text is revision 3 at
   `3ef2ef524956498f8923323dc6cf9d672dbeb50b`; the ruling, its supplement,
   the comparison and this handoff follow it. Verify:

   ```bash
   git merge-base --is-ancestor 3ef2ef524956498f8923323dc6cf9d672dbeb50b HEAD && test -f docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md && echo basis-ruling-and-supplement-present
   ```

   Do not assume an older `origin/main` has these. The originating worktree
   `/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335`
   is preserved local evidence, not a requirement. Do not rewrite history,
   never use bare `git stash`, and do not push or merge beyond the owner's
   direction.
2. **Governing records.** `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`
   (ruled 2026-09-11) and `D-GOV-43_supplement_topology_A2.md` (recorded
   2026-09-12). The packet under
   `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/`
   is the proposal history (decision revision 3, `IMPACT.md`,
   `AGENTS.proposed.patch`, three review rounds). `TOPOLOGY_COMPARISON.md`
   here is the reasoning record for A2, with its corrections in section 9.
3. **Trial context.** `../APP_V3_TRIAL_COMPLETION_20260910/R17_FUNCTIONAL_FINDINGS.md`
   (R17-F2 is the transport defect; the demonstration there is the seed of
   the eight checks).

Owner's prior model direction, subject to the launch prompt: bounded Type 2
work, separate independent review and packaging on `fable-5.1` at `medium`
reasoning. Role as the owner directs; WORKING_ITEMS fits (organize
implementation, assign bounded work, integrate results); under HELP_HUMAN
the same applies with direct Type 2 dispatch.

## 1. Working priority and settled points

1. **Retire the obsolete constraints** (section 2) so the implementation is
   not fighting retired governance.
2. **Prove the production-path experience**: plan → execute → save → reuse →
   iterate, as the eight checks in section 4. Get the loop working end to
   end before refining presentation; let the checks justify what the UI must
   show.

Documentation explains and supports; it is not a separate programme and must
not delay the demonstration. **Codex is the only engine** for this release;
the multi-engine abstractions are retired, not generalized (local models
will be Codex model providers later). Two design points are settled and are
not to be reopened by accident: the disconnection rule (section 3, transport)
and the new service composition (section 3, composition). Remaining
technical discoveries belong in the spike; they need another human decision
only if they materially change the agreed scope or behaviour.

**Cross-product constraint (recorded):** keep the Runtime host independent of
Electron and Next and consumable as an application-owned service; package
only what the Chirality App needs; Piping integration and local-model
management remain deferred.

## 2. Application tranche (governance first)

- Its own manifest `docs/governance_harness/tranche_manifests/ROOT-DGOV43-APPLICATION-<YYYYMMDD>.yaml`
  (`instruction-tranche-manifest/v1`): `basis` = the head you start from;
  `m2_gate.authorization` quotes the ruling and the supplement verbatim;
  `merge_gate: human-gated-pr`; `self_merge: false`; `m6_notice.disposition:
  routed` to the three loop notices named in `IMPACT.md` (records of
  application, not adoption requests).
- **Root, A2-adjusted.** Apply `AGENTS.proposed.patch` with `git apply`
  ("owned by the App's own host process" reads as the application-owned
  Runtime service). `docs/CONTRACT.md` §1.13: K-RUNTIME-1 becomes the
  application-owned Runtime child (no per-user LaunchAgent, no exclusive
  daemon) that owns the Codex child; K-CONTROL-1 keeps its spine (Unix
  socket, no TCP listener) with the supervisor socket retired; retire
  K-RESIDENCY-1 from the live contract; revise the closing paragraph and
  the enforcement-map row. `docs/SPEC.md` §14.1: launch and lifetime of the
  child, socket and tokens private to the application, thread index; keep
  §14.2 manifests; §14.3 and §14.4 to history. `docs/DIRECTIVE.md` §5 row
  and §7, adding the cross-product constraint. `docs/TYPES.md` §12: revise
  the runtime types to the child model; add `PolicySelection`,
  `ApprovalRecord`, a thread index entry; retire the residency types.
  `docs/AGENT_WORKFLOW_RUNTIME.md` skills and `permissionMode` sentences.
  `docs/PLAN.md` and `docs/PRD_ROOT.md` transcriptions read with the
  ruling. Whitespace guard advisory in `.github/workflows/harness-premerge.yml`.
  Record the publication SHA `d2878462b` in the two D-GOV-43 rows of
  `docs/governance_harness/_DECISIONS/_REGISTER.md`.
- **Runtime and App.** Apply the family dispositions in `IMPACT.md` "Purpose
  test by family" (families 1 and 2 retire; 3 adapts; 4 retains; 5 retires
  as gates; 6 retains) and the per-path tables, with the A2 difference that
  the socket API, client, port and routes are retained and repaired. Preserve
  executed records unchanged; create the new procedures and supersede
  applicability. One App decision record supersedes D-APP-125 item 3,
  D-APP-126, D-APP-122, D-APP-100, D-APP-88 and D-APP-107; revise SCA-APP-008
  before any acceptance; close the nine Runtime holds with one
  `scope-change` amendment and a concise rationale; DEL-09-07 and
  `APP-HOLD-1` retire with the LaunchAgent.
- Validate: `tools/validation/validate_instruction_tranche_manifest.py`
  (plain, and `--base origin/main --head HEAD --added-manifests-only`),
  `validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
  and the whitespace validator until it is advisory.
- Keep the rationale concise; the reviewed Git changes are the record.

## 3. Spike — technical starting points (source-established at the basis)

**Composition (settled).** Replace `hosted-private-composition.ts` with one
application-owned mode that composes, in one process, `RuntimeService`,
`DelegatedRuntime`, `CodexSupervisor`, `CodexLogin` and the effective Codex
home, with no admission, supplier staging, containment wrapper, native
addon or second socket (the supervisor job folds in; verify that
`DelegatedRuntime` takes `CodexSupervisor` directly through
`DelegatedHarnessProcessSupervisorPort`, `contracts/delegated.ts:45`, rather
than `SupervisorClient`, `standalone.ts:225-255`). The standalone entry
(`standalone-bin.ts`, `chirality-runtime-service daemon --config`, ready
line on stdout) is the shape to reuse; its hosted branch
(`standalone.ts:182`) routes into the retired composition and is not. In
`packages/core`, the conformance, exact-supply and private-home checks
(`runtime-conformance-v2.ts`, `exact-supply.ts`, `hosted-consent.ts`) are
removed deliberately; "keep the core" means keep the services. Reuse is
assessed by behaviour, not line counts.

**App-owned child.** Electron main spawns the service (the daemon-mode path
`main.ts:958` `initializeDaemon` → `runtime-host.ts:208` `startRuntimeHost`
is the starting point, minus launchd; decide the packaged entry by reading
`scripts/build-electron.mjs`), waits for its ready line, connects
`RuntimeClient` with a per-launch token under `userData`, restarts it with
backoff on crash, and stops it in `teardown()` on quit. Reuse
`core/descendant-tracker.ts` and `core/process-supervisor.ts` for orphan
protection. Retire `runtime-autostart.ts`, `cli/launch-agent.ts`,
`runtime-jobs.ts`, `daemon-activate-policy.ts`, `desktop-daemon-posture.ts`,
the `runtime.daemon` IPC operations, `host-account-*.ts` and the XPC
channel, `protected-runtime-cli.ts` if unused. Ordinary private
communication, cleanup and recovery are engineering responsibilities.

**Transport repair and the disconnection rule (settled).** Four sites:
`packages/client/src/client.ts:177-183` (pass a long or disabled
`timeoutMs` on the stream path; default at `:139`), `runtime-daemon.ts:966-991`
(SSE comment keepalives), `runtime-daemon.ts:955-959` with `:1002` and
`:1028` (a closed connection no longer interrupts the turn), and
`frontend/src/app/api/harness/turn/route.ts:17-40` with
`runtime-daemon-harness-port.ts:556-562` (stream cancel unsubscribes; it does
not interrupt). Rule: the Runtime owns the active turn; a browser
subscription observes it; explicit Stop is the existing interrupt endpoint;
reopening after a renderer disconnect recovers current state, missed
activity and any outstanding user decision from the session store and turn
state, without re-sending the prompt or executing twice.

**Interrupt versus retirement (defect found 2026-09-12, settled).** The
supervisor server answers an `interrupt` request by calling `retire()` when
the backend has no native interrupt (`supervisor-server.ts:189-190`); the
client always advertises `interrupt` (`:284`); the coordinator therefore
always takes the interrupt branch (`delegated-runtime.ts:288`, `:490`) and
then retires again after `wait()` resolves (`:518`), and the two attempts do
not share the memoized retirement. The inner protocol collapses the second
failure to `supervisor request rejected`, reported as a 500. Either
interleaving fails (worker finishing before the interrupt fails the
interrupt request, which is what CI recorded; interrupt first fails the
turn request). Full diagnosis by the parallel debugging session in the
[PR #767 comments](https://github.com/sgttomas/chirality/pull/767). Under the
single-process composition the production supervisor has a native
interrupt, so the fallback disappears for the App path; keep the
distinction between interruption and final retirement, make both paths
join one exact-generation retirement result, keep rejection of foreign or
stale generations, and add a deterministic regression that orders
interruption, worker completion and final cleanup explicitly, without
extending sleeps or skipping the assertions.

**Codex session.** In `codex-session.ts` remove the private lines
(authority initialize `:637-702`, identity snapshot, native-child carrier
`:489-524`, role TOML pins `:213-234`, policy override `:862-875`, private
framing `:132-141`, `:275`) and the config veto (`:788-821`); stock
`initialize` with `experimentalApi`; replace the whitelist (`:545`) and
item quarantine (`:624`) with pass-through; answer all ten server-request
methods (today `:288-291` handles three and throws on the rest, which fails
the session): approvals, user input, dynamic tool calls, elicitation and
the legacy approval forms through cards or the recorded policy; any
unfamiliar request with a JSON-RPC error response and a visible
"unsupported request" outcome, never an implied approval. `thread/resume`
exists at `:893`; `turn/start` already carries model, reasoning effort and
`collaborationMode` per turn (`:934`), so the per-chat freeze is App-side
only (`chat-panel.tsx:103`, `:751`).

**Event representation (clarified).** Retaining `packages/contracts` does not
retain its eight-name `UIEvent` set (`client/src/sse.ts:62-71`) or the
orphaned v2 union. Use an extensible representation that preserves upstream
method names, identifiers and payloads for faithful rendering and
inspection, with normalized views for known items (tool activity, file
changes, reasoning summaries, plan, sub-agents, usage, approvals,
questions). Producer chain: session events → `core/delegated-engine-adapter.ts`
→ `core/turn-coordinator.ts` → the App provider
(`components/workspace/harness-events-provider.tsx`) and views
(`tool-stream-view.tsx`, `subagent-stream-view.tsx`,
`permission-requests.tsx`, `NativePlanClarificationCard`). Unfamiliar
notifications stay inspectable in a generic card and the event log.

**Effective home and authentication.** Replace the private `CODEX_HOME`,
Seatbelt wrapper and `-c` overrides in `codex-containment.ts` with the
overlay layout: share the user's config, skills, plugins, MCP definitions,
instruction caches and sessions by reference; keep `auth.json` and the
models cache private; set `cli_auth_credentials_store=file` (the key
already exists, `:163`); never copy credentials. T3 Code's
`CodexHomeLayout.ts` "authOverlay" is the reference (MIT). Keep the login
flow (`codex-login.ts`, `codex-session.ts:709-752`); the owner completes
OAuth in the browser. S-8 proves the separation.

**Threads, roles, delegation.** `thread/start` with `cwd`,
`developerInstructions` (role plus selected workflow context) and the
project's `PolicySelection`; `thread/resume` on relaunch; index chats by
thread id in the session store (sidebar shows the index). Role text from
the bundled instruction root (`src/lib/harness/instruction-root.ts`);
workflow context from `.chirality/workflows/<name>/WORKFLOW.md` (project,
user, bundled; catalog refresh stays); additive turn input for a
mid-conversation selection; Codex discovers project `AGENTS.md` itself;
base instructions are never replaced. Delegation uses the upstream
`[agents]` configuration; S-5 needs evidence that the child received the
intended role instructions.

**Shutdown behaviour (clarified).** Closing or hiding a window is distinct
from quitting. Quit stops the owned Runtime and Codex processes
deliberately and leaves an accurate continuation record. Unexpected
termination is never shown as completion. No unattended execution after
quit is promised.

**UI.** Reuse `chat-panel.tsx` (composer, plan pane, "Execute plan", "Save
as workflow in chat"), `activity-shelf.tsx`, the workflows library and
Inspect, the Files panel, viewer and attachment picker. Lift the model and
effort freeze. Extend the existing cards for approvals, questions, tool
activity and delegation. Keep primary surfaces concise with inspection on
demand. Retire the legacy multi-engine managers in `src/lib/harness/`
(unreachable today; forbidden from the bundle) only when nothing references
them; do not let deletion delay the demonstration.

**Evidence and history.** Write AgentRuns evidence from the same stream
(`run-logger.ts`, `tool-evidence.ts` are reuse candidates), including the
active policy and approvals. Daemon-era chats live under the trial
`userData` `runtime/projects/<id>/sessions` and in the trial's private Codex
home; if the existing session reader renders them read-only without new
work, keep that, otherwise leave them as an accessible archive. No import
feature, no continuation promised. Preserve prior Pi and oMLX work in
history and reference without an obligation to keep it compiling.

**Consumers.** The App is the only production consumer. The Runtime CLI
(`packages/cli`) and the PEC server use the socket API; A2 preserves their
integration opportunity, and their compatibility is unverified and not an
MVP prerequisite. Record affected compatibility honestly.

## 4. Acceptance and the post-build rule

Run S-1 to S-8 (ruling item 12) on the production path from source first
(`npm run dev` in `frontend/` with a distinct `userData` and its own
effective Codex home, so the R17 installation is untouched). Add to the
continuity checks: a renderer disconnect during tool work, after which
reopening the conversation shows the missed activity and any outstanding
decision, with no duplicate execution. Then one consolidated signed build
after independent source review; the new short packaging procedure is
build, sign, notarize, verify signature and Codex pin, then the distinct
packaged checks. After the build repeat S-6, S-8 and the signature and pin
verification as the expected minimum, not a ceiling: repeat any affected
check when a source, configuration or packaging change invalidates its
earlier evidence (for example packaged instruction roots resolving
differently from development files; `instruction-root:integrity` is the
relevant script). Do not repeat unaffected tests merely because another
stage has begun. Native verification of the packaged App is by the owner's
designated direct tester.

## 5. Review boundary

- Your code gets a **separate independent source reviewer** (a fresh
  session or a dispatched Type 2 reviewer with no authorship of the change)
  before the consolidated signed build. The proposal reviews do not
  substitute. Record the review here (the `INDEPENDENT_REVIEW.md` pattern
  from `../APP_V3_TRIAL_COMPLETION_20260910/R16_RESTART_ADMISSION/`).
- Return to the owner only for material scope or behaviour changes,
  substantial product-scope additions, departures from the established
  visual direction (the shell as built through the R16 UI batch and its
  consolidated review), and consequential findings. Routine implementation
  and UI choices are yours; record them here.
- Publishing, the system-prompt discussion and trial acceptance remain the
  owner's separate acts. Nothing here authorizes a release.

## 6. Live state and boundaries carried forward

- R17 installation, preserved: App
  `/Users/ryan/Applications/Chirality Trial 20260910 R17.app`; userData
  `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R17`;
  guarded launcher
  `/Users/ryan/Applications/Launch Chirality Trial 20260910 R17.command`;
  stage root `/private/tmp/chirality-local-human-trial-20260910-26`; trial
  project `/Users/ryan/dev/chirality-trial-20260911-r6` (contains the
  demonstration outputs `chirality-app-report.md` and
  `.chirality/workflows/report-writing/`). At handoff the R17 GUI (pid 31613)
  and LaunchAgent daemon `com.chirality.runtime` (pid 27838) were running and
  signed in. Recheck processes; leave them and all prior evidence intact
  unless the owner directs retirement. The spike from source needs no
  LaunchAgent and must not reuse the R17 userData or Codex home.
- Launch trial Apps only through their guarded launcher; never open a trial
  `.app` directly and never `open_application` on `com.chirality.app`.
- Never enter credentials, passwords or codes; the owner performs OAuth and
  2FA. Never weaken authentication. Never read live identity, auth, token,
  binding, keychain, trial Codex home or session/event files; if a prior
  automated review blocked such a read, do not retry it another way; ask the
  owner for filtered diagnostics. Filter desktop and daemon logs with
  `grep -v '@'` before recording; the owner's account e-mail never appears in
  logs or commits. No `security` commands. No cleanup of preserved trials or
  account resets to make a test pass. No publishing.
- Commit per bounded step with the session's attribution trailer. Keep a
  `RUN_LOG.md` in this directory with UTC timestamps, in the style of
  `../APP_V3_TRIAL_COMPLETION_20260910/RUN_LOG.md`.

## 7. Transport record and inherited items

- [PR #767](https://github.com/sgttomas/chirality/pull/767) carries the
  packet, ruling, supplement, comparison and this handoff from
  `claude/chirality-v3-mvp-trial-ab05cb` into `main`; its merge SHA is
  recorded in the PR closeout comment and
  `../APP_V3_TRIAL_COMPLETION_20260910/RUN_LOG.md`.
- `PERSPECTIVE.md` (the owner's intent) and `LAUNCH_PROMPT.md` (ready to
  paste) sit beside this file.
- PR #767 merged to `main` as `d2878462be59a43b4afc175a8cce85abca9cf696`
  on 2026-09-12 with all checks green at merge; that is the publication SHA
  for the ruling and its supplement (K-AUTH-2). Record it in the
  `_REGISTER.md` rows for D-GOV-43 in the application tranche.
- Known CI condition at handoff: the Harness pre-merge job's Runtime test
  step is intermittent in the two interrupt tests of
  `tests/delegated-runtime.test.ts` (500 on the interrupt or the turn
  request), red at the merged PR #766 head and at one head of PR #767,
  green at the merged head. The cause is the interrupt-versus-retirement
  defect in section 3, not a platform difference; the green run is
  intermittency, not repair. `9d122b08e` added a stderr logger to the
  fixture daemon so a red run prints the bounded cause.
- R17-F1 and R17-F2 are subsumed by the re-platform; S-2, S-6 and S-7 and
  the disconnection check cover them.
- Who relaunched the R16 daemon at 2026-09-12T01:41Z is an unanswered owner
  question; historical, no action.
