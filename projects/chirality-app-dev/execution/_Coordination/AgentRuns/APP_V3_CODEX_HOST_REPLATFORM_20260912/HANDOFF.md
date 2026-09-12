# Codex host re-platform (D-GOV-43) — implementation handoff

Prepared 2026-09-12 by HELP_HUMAN for a separate implementing session. Read
Root `AGENTS.md` and your role instruction first. This file is coordination,
not governance: the governing record is D-GOV-43 and its ruling.

## 0. Preconditions — verify before any work

1. **Implementation basis.** The proposal text is revision 3 at commit
   `3ef2ef524956498f8923323dc6cf9d672dbeb50b`; the owner's ruling record and
   this handoff follow it on branch `claude/chirality-v3-mvp-trial-ab05cb`,
   merged to `main` through PR #767 (section 7) under the owner's
   direction of 2026-09-11. Use an integration checkout updated
   from `origin/main` that contains that merge; do not assume an older
   `origin/main` has it (`origin/main` was
   `a75adecf13f055c092ffa92809f66e7817c44242` before the merge). Verify with

   ```bash
   git merge-base --is-ancestor 3ef2ef524956498f8923323dc6cf9d672dbeb50b HEAD && test -f docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md && echo basis-and-ruling-present
   ```

   The originating worktree
   `/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335`
   is preserved local evidence, not a requirement. Do not rewrite history,
   never use bare `git stash`, and do not push or merge beyond the owner's
   direction.
2. **The owner's ruling record exists** at
   `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`
   (ruled 2026-09-11, verbatim, with the post-build clarification and the
   `_REGISTER.md` row). It is the governing record; the packet is the
   proposal history. If your checkout lacks it, you are on the wrong basis.
3. **Read** the packet
   `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/`
   (`D-GOV-43.proposed.md`, `IMPACT.md`, `AGENTS.proposed.patch`,
   `REVIEW_FEEDBACK_R1.md` to `R3.md`, `RULING_CANDIDATE.md`), the trial
   findings
   `../APP_V3_TRIAL_COMPLETION_20260910/R17_FUNCTIONAL_FINDINGS.md`
   (R17-F2 is the transport failure the re-platform removes), and this file.

Owner's prior model direction for this work, subject to the launch prompt:
bounded Type 2 work, separate independent review and packaging on
`fable-5.1` at `medium` reasoning. Role as the owner directs at launch;
WORKING_ITEMS fits (organize implementation, assign bounded work, integrate
results); under HELP_HUMAN the same applies with direct Type 2 dispatch.

## 1. Working priority

1. **Retire the obsolete constraints** (the coordinated application tranche,
   section 2). This removes the daemon's requirements, holds and checks so
   the implementation is not fighting retired governance.
2. **Prove the production-path experience**: plan → execute → save → reuse →
   iterate, as ruling item 12's checks S-1 to S-8 (section 4).

Documentation explains and supports that work. It is not a separate
programme and must not delay the functional demonstration. Remaining
technical discoveries belong in the spike; they need another human decision
only if they materially change the agreed scope or behaviour.

## 2. Application tranche (governance first)

- Its own manifest `docs/governance_harness/tranche_manifests/ROOT-DGOV43-APPLICATION-<YYYYMMDD>.yaml`
  (`instruction-tranche-manifest/v1`): `basis` = the branch head you start
  from; `m2_gate.authorization` quotes the owner's ruling verbatim and cites
  the `_DECISIONS` record; `merge_gate: human-gated-pr`; `self_merge: false`;
  `m6_notice.disposition: routed` to the three loop notices named in
  `IMPACT.md` (they are records of application, not adoption requests).
- Root: apply `AGENTS.proposed.patch` with `git apply`; amend
  `docs/CONTRACT.md` §1.13, `docs/SPEC.md` §14, `docs/DIRECTIVE.md` §5/§7,
  `docs/TYPES.md` §12, `docs/AGENT_WORKFLOW_RUNTIME.md`, and the
  `docs/PLAN.md` / `docs/PRD_ROOT.md` transcriptions exactly as "Surfaces
  touched" lists; make the candidate whitespace guard advisory in
  `.github/workflows/harness-premerge.yml`; add the `_REGISTER.md` row if
  the ruling commit did not.
- Runtime and App: apply the family dispositions in `IMPACT.md` "Purpose
  test by family" (families 1 and 2 retire outright; 3 adapts; 4 retains;
  5 retires as gates; 6 retains) and the per-path tables. Preserve executed
  records unchanged; create the new procedures and supersede applicability.
  One App decision record supersedes D-APP-125 item 3, D-APP-126, D-APP-122,
  D-APP-100, D-APP-88 and D-APP-107; revise SCA-APP-008 before any
  acceptance; close the nine Runtime holds with one `scope-change` amendment
  and a concise rationale.
- Validate: `tools/validation/validate_instruction_tranche_manifest.py`
  (plain, and `--base origin/main --head HEAD --added-manifests-only`),
  `validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
  and the whitespace validator until it is retired.
- Keep the rationale concise. The reviewed Git changes are the record; do
  not build a register to demonstrate simplification.

## 3. Spike — technical starting points (all source-established at the basis)

**Host process.** `projects/chirality-app-dev/frontend/electron/`: keep and
reuse `main.ts`, `preload.ts`, `renderer-window-policy.ts`,
`ipc-sender-policy.ts` (validated IPC), `attachment-*.ts`,
`plan-export-*.ts`, `desktop-log.ts`. The daemon path leaves with
`runtime-host.ts`, `runtime-host-legacy.ts`, `runtime-control-ipc.ts`,
`runtime-autostart.ts`, `runtime-connectivity.ts`, `runtime-socket-watch.ts`,
`daemon-*.ts`, `desktop-daemon-posture.ts`, `host-account-*.ts`,
`protected-runtime-cli.ts`. Add a Codex host module that spawns
`codex app-server` over stdio, owns its lifetime (exit, relaunch, quit) and
relays JSON-RPC both ways.

**Child and pin.** Add `@openai/codex` as a dependency pinned in
`package.json` and the lockfile (upstream was `rust-v0.154.0` / npm 0.154.0
on 2026-09-09; check the current release and pin the one you validate).
Launch `codex app-server` with the pinned binary; pass through user config
arguments (`-c`, `--config`, `--enable`, `--disable`) as T3 Code's
`codexLaunchArgs.ts` does (MIT; reference, not a copy target). No patched or
forked supplier; `tools/codex-supplier` and `tools/native-admission` retire.

**Bindings.** Generate TypeScript types from the upstream JSON schema at the
pinned tag (`codex-rs/app-server-protocol/schema/json`: `ClientRequest.json`,
`ServerRequest.json`, `ServerNotification.json`, `v2/*`; fetch from GitHub at
implementation time, the session scratchpad copies do not persist). Declare
the experimental augmentation in one file, starting with
`TurnStartParams.collaborationMode` (omitted from the exported schema,
accepted at runtime under `experimentalApi`; Plan Mode depends on it). Add an
integration check against the pinned binary: `initialize` with
`experimentalApi`, `thread/start`, `turn/start` in plan collaboration mode,
expect plan items or `turn/plan/updated`.

**Effective Codex home (authentication separation).** `CODEX_HOME` =
`{userData}/codex-home`. Share the user's `~/.codex` entries by reference
(config, skills, plugins, MCP definitions, instruction caches, `sessions`,
`archived_sessions`, MCP OAuth locks); keep `auth.json` and the models cache
private. T3 Code's `CodexHomeLayout.ts` "authOverlay" mode is the reference.
Never copy credentials. Check the pinned version's credential-store setting
(file versus OS keyring): if a keyring backend is active, confirm the
Chirality home yields a separate identity, otherwise report and do not
share silently. S-8 proves it. The direct shared-authentication opt-in is
deferred; do not build it.

**Authentication.** `account/login/start` (open the returned URL with
`shell.openExternal`; the owner completes OAuth and 2FA, never the agent),
`account/login/cancel`, `account/logout`, `account/read`; observe
`account/login/completed`. Credentials are Codex's; the App never reads,
copies or relays them.

**Threads and turns.** `thread/start` with `cwd`, `developerInstructions`
(role plus selected workflow context), sandbox and approval policy from the
project's `PolicySelection`; `thread/resume` on relaunch; App index keyed by
thread id in userData (the sidebar shows the index, not `thread/list`).
`turn/start` with input items and per-turn model and effort (`model/list`
for the picker; the per-chat freeze in `chat-panel.tsx` goes);
`turn/interrupt`; `turn/steer` optional.

**Server requests.** Answer every one: `item/commandExecution/requestApproval`,
`item/fileChange/requestApproval`, `item/permissions/requestApproval`,
`item/tool/requestUserInput`, `item/tool/call`, `mcpServer/elicitation/request`,
`applyPatchApproval`, `execCommandApproval` through cards or the recorded
policy; anything else (including `account/chatgptAuthTokens/refresh` and
`attestation/generate` if they ever arrive under Codex-custodied auth) with
a JSON-RPC error response and a visible "unsupported request" outcome. No
request left pending; no card implies approval. Unfamiliar notifications:
generic inspection card plus the event log.

**Renderer.** One long-lived channel through `preload.ts` (events main to
renderer, requests renderer to main) with validated shapes; `contextIsolation`
on; no credential material crosses. The Next API routes under
`src/app/api/harness/*` (turn, interrupt, permission, session, …) and
`src/lib/runtime-client/*` are replaced by the channel. Reuse
`src/components/shell/chat-panel.tsx` (composer, plan pane, "Execute plan",
"Save as workflow in chat"), `src/components/woven-dialogue/activity-shelf.tsx`
(Activity), the Workflows library and Inspect, the Files panel, the viewer
and the attachment picker. Retire the legacy multi-engine managers and
mappers in `src/lib/harness/` (Claude SDK, Pi) only when nothing references
them; do not let deletion scope delay the demonstration.

**Roles, workflows, delegation.** Role text from the bundled instruction root
(`src/lib/harness/instruction-root.ts`, `agent-instruction.ts`); workflow
context from `.chirality/workflows/<name>/WORKFLOW.md` (project, user,
bundled; catalog refresh stays an App function). Supply through
`developerInstructions` at thread start and resume and as additive turn input
for a mid-conversation selection; Codex discovers project `AGENTS.md`
itself; upstream base instructions are never replaced. Delegation uses the
upstream `[agents]` configuration; S-5 requires evidence that the child
received the intended role instructions (for example a role marker the child
must echo, or its recorded developer instructions).

**Evidence.** Write AgentRuns evidence from the same stream
(`run-logger.ts`, `tool-evidence.ts` are reuse candidates), including the
active policy and approvals given. Codex's session store is operational
state.

**Daemon-era chats.** JSON/JSONL under the trial userData
`runtime/projects/<id>/sessions` plus Codex thread records in the trial's
private home. `src/lib/harness/session-manager.ts` / `session-events.ts` is
the existing reader; if it renders them read-only without new work, keep
that; otherwise leave them as an accessible archive. No import feature, no
continuation.

**Runtime package.** `projects/chirality-runtime/packages/daemon` (`codex-*.ts`,
`hosted-*.ts`, `host-account-*.ts`, `supplier-authority-*.ts`,
`runtime-daemon.ts`, `supervisor-server.ts`), `packages/native-admission`,
`packages/client` and the LaunchAgent tooling are retired from the App path.
`packages/core` and `packages/contracts` (workflow catalog, method identity,
validation) are reuse candidates; decide by reading, do not port daemon code.

## 4. Acceptance and the post-build rule

Run S-1 to S-8 (ruling item 12) on the production path from source first
(`npm run dev` in `frontend/` with a distinct userData directory and its
own effective Codex home, so the running R17 installation is untouched).
Then one consolidated signed build after independent source review; the new
short packaging procedure is build, sign, notarize, verify signature and
Codex pin, then the distinct packaged checks. After the build repeat S-6,
S-8 and the signature and pin verification as the **expected minimum, not a
ceiling**: repeat any affected check when a source, configuration or
packaging change invalidates its earlier evidence (for example, packaged
instruction roots resolving differently from development files; the existing
`instruction-root:integrity` script is the relevant check). Do not repeat
unaffected tests merely because another stage has begun. Native
verification of the packaged App is by the owner's designated direct
tester.

## 5. Review boundary

- Your code gets a **separate independent source reviewer** (a fresh
  session or a dispatched Type 2 reviewer with no authorship of the change)
  before the consolidated signed build. The three proposal reviews do not
  substitute. Record the review in this directory (the
  `INDEPENDENT_REVIEW.md` pattern from `../APP_V3_TRIAL_COMPLETION_20260910/R16_RESTART_ADMISSION/`).
- Return to the owner only for material scope or behaviour changes and
  consequential findings. Routine implementation choices are yours; record
  them here.
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

## 7. Transport record and inherited open items

- Pull request from `claude/chirality-v3-mvp-trial-ab05cb` into `main`:
  [PR #767](https://github.com/sgttomas/chirality/pull/767), opened
  2026-09-12 under the owner's direction; the merge SHA is recorded in
  `../APP_V3_TRIAL_COMPLETION_20260910/RUN_LOG.md` and the PR closeout.
- The owner's perspective note for the implementing session accompanies the
  launch prompt; if committed, it lives beside this file as
  `PERSPECTIVE.md` and explains intent without changing the ruled scope.

- R17-F1 (interrupted turn not rendered live) and R17-F2 (30 s
  stream-silence interruption) are subsumed by the re-platform; S-2 and S-7
  cover them.
- Who relaunched the R16 daemon at 2026-09-12T01:41Z is an unanswered owner
  question; historical, no action.
