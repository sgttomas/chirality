# R17 direct functional trial

Completed native pass. Actual signed Stage26/R17 App, source
fb529591d79ac4e7f2015b69f3f9a394df317d88 (restart-admission repair
5045178d4/6e2b631ec plus the reviewed R16 UI batch). Lead used Computer Use
and ordinary synthetic project files; no protected live account/session/event
files were read. R16 evidence remains historical. Times UTC, 2026-09-12.

## Section B and launch (step 0) — PASS

- R16 retired 02:35:51Z: `launchctl bootout gui/501/com.chirality.runtime`
  exit 0, no R16 process remained, plist moved with `mv -n` to
  `/private/tmp/chirality-local-human-trial-20260910-26/retired-r16-com.chirality.runtime.plist`,
  `launchctl print` exit 113 with the exact expected message.
- R17 launcher `--check-only` printed `Launch guard PASS` (exit 0). Guarded
  launch 02:36:06Z; exact R17 GUI pid 27808 and LaunchAgent daemon pid 27838
  observed; window title `Chirality`; daemon started 02:36:19Z; GUI bound and
  account host connected 02:36:24Z.
- Folder `/Users/ryan/dev/chirality-trial-20260911-r6` bound through the
  composer's `Enter a path…` field; Files panel populated; runtime already up.

## Sign-in (step 1) — PASS

Fresh userdata required consent and sign-in. `Allow provider network` then
`Sign in` pressed 02:39:20Z under the standing consent-click warrant; the
owner completed browser OAuth (ceremony started 02:39:29Z, completed
02:40:42Z, 73 s of owner time); `hosted.admission.established … ready` at
02:40:48.792Z. Press→Ready 88 s including the owner's OAuth. Account row:
`OpenAI signed in · Signed in · Ready to work`. Catalog model
`gpt-5.6-luna` / `high` selected by default.

## First turn (step 2) — PASS

Sent 02:43:11Z; reply `I'm ready to work with you as agent0.` and Idle within
~25 s. Chat listed in the sidebar with its time and folder.

## Long chat, scroll, sidebar, interruption (step 3)

- PASS, scroll: a 12-step plan-style reply overflowed the transcript. Keyboard
  paging and End reached step 12 fully visible above the fixed composer; the
  composer remained reachable throughout. Automation note: raw wheel scroll
  from Computer Use did not move the transcript until an element inside it
  was focused; PageDown/End then worked. Not a product failure.
- PASS, sidebar: switching chats (new chat, then reopening the first through
  history) kept the Files panel with the folder tree; no empty Agents/Session
  replay state appeared (the R16 usability finding is resolved).
- PASS after reopen / FINDING live: a long counting turn was interrupted
  02:47:23Z (`Interrupt requested…`, Idle ~8 s later). Live, the transcript
  showed neither the user message, the partial list nor any status; End and
  PageDown did not reveal it and the accessibility element count matched the
  pre-turn state. After switching away and reopening the chat the turn
  rendered correctly: partial output to item 66 followed by a concise
  `Assistant — Interrupted` block, exactly the intended status. Finding
  R17-F1 (medium, UI): interrupted-turn rendering is missing in the live
  view until the chat is reopened. Source inspection warranted; no build
  requested.
- Interaction-mode switch to Plan Mode via the native popup did not take
  through automation (the menu window is separate from the granted app
  window); plan mode itself was verified natively in R15/R16 and is
  unchanged by this source delta, so it was not repeated.

## Second chat file read — PASS

New chat sent 02:48:50Z asked for a real tool read of `README.md`; reply
`# R6 trial project` / 3 lines matches the file on disk; Idle ~40 s.

## Restart admission (step 4, the R16 blocker) — PASS

- Both chats idle. Quit through the app menu 02:51Z; `desktop.shutdown
  before-quit` 02:51:30Z, GUI gone by 02:51:43Z; daemon kept pid 27838 with
  no launchd restart.
- `--check-only` PASS again; guarded relaunch 02:51:57Z; new GUI pid 31613;
  `runtime.connectivity.bound` immediately, three `account_host.client_unavailable`
  status retries over 5 s, then `runtime.account_host.connected` 02:52:03Z.
  Daemon log contains no `hosted.admission.fenced` and no new lines at all
  through 02:58Z; main log has no error lines.
- Owner-observed (Computer Use could not attach, see below): account row
  still Ready, no sign-in prompt. Retained chat follow-up `Step 10 is to
  write the draft to r17-plan-report.md.` (correct from pre-restart history).
  Other chat real file read `# R16 Shell Report` / 3 lines (matches disk).
  Both returned to Idle with no error, sign-in or admission text.
- Result: the post-restart failure of R16 (`Runtime v2 admission is missing,
  invalid, stale or no longer live`) did not recur; renewal of the host
  admission after the App's re-ceremony worked without account edits.

## Stale rejection (step 5)

Not exercised natively (it would require protected admission state). Covered
by the reviewed D36 renewal tests: old admission and preparation rejected
after renewal, disconnect during renewal rejected, expired release rejected
(INDEPENDENT_REVIEW.md PASS, 121/121 and backcheck 56/56). No test accepts a
superseded admission.

## Retained evidence (step 6) and sign-out (step 7)

Shell read/write, inline viewer, image attachment, plan revision/execution,
second role/model chat and PDF opening were not repeated; the source delta
since R16 touches restart admission and the reviewed UI batch only. Sign-out
not exercised.

## Computer Use limitation after restart (explained)

After a GUI restart the daemon (pid 27838) holds the lowest pid for
`com.chirality.app`, and the granted bundle id resolves to it, so
`app_list_windows` returns no windows although the GUI and its renderer are
running. This is the "attachment timed out after restart" seen in R15 and
R16. Pid and display-name addressing are refused by the grant model;
osascript lacks assistive access and no settings were changed. Owner
observation was used, as the checklist prescribes.

## Plan, execute, and save-as-workflow demonstration (owner request, 03:05Z-03:34Z)

Owner asked for a new chat that plans a report about the Chirality App,
iterates once, accepts and executes the plan, then generalizes it into a
report-writing workflow. Performed by full-screen Computer Use (owner
approved `request_full_control` after the per-app grant could not attach).

- New chat, Plan Mode selected from the mode picker: PASS. Revision 1
  "Chirality App Technical Report" rendered in the plan pane.
- One iteration via "Revise in chat" (pre-fills "Revise plan revision 1"):
  PASS. Revision 2 "Chirality App Report - Revision 1" with eight
  implementation steps, a Sources section and a claim-by-claim check.
- "Execute plan" (pre-fills the accepted revision 2 and switches the mode
  to Chat): PASS as a UI flow. The two full execution turns FAILED: each
  streamed a one-paragraph preamble, went silent while the agent read the
  source files, and ended about 90-100 s in with status Idle. Reopening the
  chat showed "Assistant - Interrupted" after each preamble; no report on
  disk; Activity -> Actions "No recorded actions"; no daemon or main log
  lines. See R17-F2.
- Bounded retry: a turn told to skip reads and create the report in one
  write succeeded. `chirality-app-report.md` (85 lines, six sections plus
  Sources) appeared 03:29:42Z, sha256 `ae77b89a...`. The final one-line
  reply did not render live (R17-F1 pattern).
- "Save as workflow in chat" (pre-fills "Save native Plan Mode revision 2
  below as a reusable project workflow at .chirality/workflows/<suitable-
  name>/WORKFLOW.md ...", full plan embedded) plus a generalizing
  instruction: FAILED the same way, this time rendering "Turn interrupted
  by operator" live (so R17-F1 is intermittent, not absolute).
- Bounded retry with the target metadata spelled out and no reads:
  `.chirality/workflows/report-writing/WORKFLOW.md` written 03:33Z, sha256
  `ee428532...`, frontmatter name/description/purpose/applicability, six
  generic steps with `{{subject}}`, `{{audience}}`, `{{sources}}`,
  `{{output_path}}` placeholders, Assumptions section. Reply rendered
  live. Workflows -> Library -> search "report" lists it under "For this
  project" next to `r15-trial-report`; Inspect shows description,
  Technical details and Read instructions.

Outcome: every UI step of the owner's sequence is functional (plan, revise,
accept/execute pre-fill, save-as-workflow pre-fill, catalog refresh and
Library listing). What is not functional is any execution turn whose agent
works silently for more than about 30 s.

### R17-F2 (high, Runtime/client): turns interrupted after ~30 s of stream silence

Source-established chain (frozen source `fb529591d`, unchanged at HEAD):

1. `packages/client/src/client.ts` `request()` applies
   `request.setTimeout(input.timeoutMs ?? this.timeoutMs)` with the default
   `this.timeoutMs = options.timeoutMs ?? 30_000`. The SSE `stream()` path
   (accept `text/event-stream`) passes no `timeoutMs`; the frontend
   constructs `RuntimeClient` without an override
   (`runtime-daemon-harness-port.ts` ~994). `PACKAGED_REQUEST_TIMEOUT_MS`
   and `PACKAGED_TURN_TIMEOUT_MS` govern the daemon side only.
2. Node's socket idle timeout fires after 30 s without bytes; the client
   destroys the request with `RuntimeTransportError("Runtime request timed
   out", ..., "timeout")`.
3. The daemon SSE writer (`runtime-daemon.ts` ~948-1004) emits no keepalive
   frames, and its `response.once("close", close)` handler calls
   `cancelSse` -> `trySseInterrupt` -> `control.interrupt()`, so a client
   disconnect interrupts the Codex turn.
4. `codex-session.ts` only emits `agentMessage` text deltas and `plan`
   items; command execution and file-change items are quarantined
   (`item/started`/`item/completed` for other types). Tool work therefore
   produces no stream bytes, and any reasoning-plus-tool stretch over 30 s
   is fatal. High reasoning effort makes this common.
5. The Next route `api/harness/turn/route.ts` closes the browser stream
   cleanly in `finally`, so the chat panel ends with `setIsRunning(false)`
   (Idle) while the daemon records the turn as interrupted. Whether the
   interruption text renders live depends on ordering (R17-F1).

Not the cause: the daemon `turnTimeoutMs` (packaged 1 800 000 ms), the
packaged request timeout (90 000 ms), authentication or admission. No log
line is written for the client-side timeout. Likely also explains the R15
and R16 "timeout-retry" history and R17-F1's blank live view.

Repair candidates (not started; no rebuild authorized): pass a long or
disabled `timeoutMs` on the client `stream()` path, and/or emit SSE comment
keepalives from the daemon writer, and/or forward tool activity as stream
events. Any fix belongs in the next consolidated batch with R17-F1.

## Findings summary

- R17-F1 (medium, UI): interrupted turn not rendered live (intermittent);
  correct after reopen. Repair candidate for the next batch; no rebuild now.
- R17-F2 (high, Runtime/client): execution turns are interrupted after
  ~30 s without stream bytes (client SSE socket idle timeout -> daemon
  close handler -> interrupt; tool work emits nothing). Plan execution and
  save-as-workflow succeed only as short, read-free turns. Repair candidate
  for the next consolidated batch; no rebuild now.
- No functional, authentication or admission failure observed. Packaging
  PASS plus this native pass do not by themselves constitute trial
  acceptance or publishing approval; those remain the owner's decisions.
