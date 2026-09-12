# Native checklist (D-GOV-43, topology A2)

Recorded 2026-09-12. Supersedes the applicability of
`../APP_V3_TRIAL_COMPLETION_20260910/R15_NATIVE_CHECKLIST.md`,
`R16_NATIVE_CHECKLIST.md` and `R17_NATIVE_CHECKLIST.md` (guarded launcher,
LaunchAgent, admission fence, stale rejection), which are preserved
unchanged as executed history. Run this on the consolidated signed build
from `PACKAGING_PROCEDURE.md`, with a fresh `userData` and its own effective
Codex home. Never reuse the R17 userData or Codex home. The tester performs
OAuth and any 2FA; no agent enters credentials. Record each item as PASS or
FAIL with what was observed, in this run directory.

1. **Launch from the consolidated signed build.** Open the stapled App
   directly (no guarded launcher, no LaunchAgent). The App starts its
   Runtime service child and the Codex child; Activity shows the service
   ready. No second socket, no launchd job, no admission prompt.
2. **Signature and Codex pin verification.** `codesign --verify --deep
   --strict` and `spctl --assess` pass on the bundle; the bundled
   `@openai/codex` version equals the lockfile pin.
3. **Sign in through Codex's own flow.** From the account row, start
   sign-in; the tester completes OAuth in the browser. The App shows the
   signed-in account without reading, copying or relaying credential
   material; `auth.json` lives in the Chirality effective home only.
4. **S-6: quit and relaunch with continuation.** In a trial project, run a
   chat with real tool use, quit the App (Quit, not window close), confirm
   the Runtime and Codex children are gone, relaunch, reopen the same chat
   and continue it; the App resumes the thread through `thread/resume` and
   the transcript is intact. Unexpected termination, if it occurs, is shown
   as such, never as completion.
5. **S-8: sign-in and sign-out scoped to Chirality.** With another Codex
   client (for example the Codex CLI) signed in beforehand, sign out of
   Chirality and confirm the other client's state is unchanged; sign back
   in and confirm the same. Record the credential backend observed.
6. **Renderer disconnect during tool work.** Start a turn that reads files
   and runs tools for longer than 30 seconds; while it runs, disconnect the
   renderer (close the window or navigate away, not Quit). Reopen the
   conversation: the turn was not interrupted, the missed activity is shown,
   any outstanding approval or question is presented once, and nothing was
   executed twice or re-sent. Explicit Stop still interrupts.

Repeat an item only when a source, configuration or packaging change has
invalidated its earlier evidence. This checklist records the owner's native
verification; it is not release or publishing approval.
