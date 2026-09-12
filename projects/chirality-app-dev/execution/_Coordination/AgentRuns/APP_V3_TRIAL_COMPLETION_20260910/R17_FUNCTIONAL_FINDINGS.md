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

## Findings summary

- R17-F1 (medium, UI): interrupted turn not rendered live; correct after
  reopen. Repair candidate for the next batch; no rebuild now.
- No functional, authentication or admission failure observed. Packaging
  PASS plus this native pass do not by themselves constitute trial
  acceptance or publishing approval; those remain the owner's decisions.
