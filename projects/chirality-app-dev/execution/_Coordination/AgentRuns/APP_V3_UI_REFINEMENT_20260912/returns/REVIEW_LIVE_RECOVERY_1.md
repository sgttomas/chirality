# Independent review return 1

Candidate: `9eb92d33b58161cbdbc4269fcbf2a333a5c5aefc` against `85f19f019589b798331c804c4b206e34849eeab5`.
Reviewer: fresh `/root/live_recovery_independent_review`, gpt-6-astra, medium.
Return below is verbatim.

FAIL — one actionable finding.

**[P1] An ambiguous first POST can inherit an older turn’s successful result.**  
Location: `projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx:1031–1045`, with recovery at `1070–1072` and replay fallback at `1094–1109`.

Trigger: a conversation contains a completed earlier turn; the next POST fails before any frame arrives, potentially before Runtime receives it. The new transport-error branch reconnects without knowing the submitted turn’s identity. Attaching with `after=0` can return the previous retained turn: `TurnRegistry.subscribe()` selects the session’s retained record without submission correlation. Its old text and terminal then become the new reply and outcome. If that buffer is absent, the replay fallback instead searches all historical turns when `turnId` is undefined, producing the same false completion.

Impact: an unexecuted or uncertain request can display the previous answer and **Completed**; a plan execution attempt can also settle against that unrelated result. No duplicate POST is required to trigger this defect.

Repair: bind observation to a submission identity established before sending—preferably a generated turn ID passed through the App request into the already-supported Runtime `SessionTurnRequest.turnId`. Match retained-stream identity and replay events before using their text or terminal. If correlation cannot be established, retain the sent message and report Outcome unknown. Do not merely fix the unscoped replay fallback: the old retained stream is another entry path. Add regressions with populated previous history for both retained-buffer attachment and `TURN_NOT_ACTIVE` replay, asserting no old reply, false completion, draft restoration, or second POST.

**Coverage and checks**

- Read 100% of the 30-file frozen diff `85f19f019589b798331c804c4b206e34849eeab5..9eb92d33b58161cbdbc4269fcbf2a333a5c5aefc`, including historical packaging records, tests, briefs, and returns. Verified HEAD equals the candidate.
- Traced Runtime stream deadlines, heartbeat/header establishment, subscription cancellation, proxy connection notification, coordinator terminal persistence/publication, replay, plan settlement, and panel sizing.
- `git diff --check` passed.
- Confirmed recorded suite summaries: Runtime 320 passed; App 2175 passed, four skipped. Read the recorded typecheck log; parent reports its successful exit. No tests or live actions rerun.
- No file writes, protected-state reads, App launches, signals, or delegation.

Residual limits: direct service-loss evidence covers graceful SIGTERM, not an unhandled crash; the intermittent `STOPPED_DEGRADED` test remains unresolved; install-over acceptance and replacement packaging remain outstanding. The records accurately distinguish these limits. No other actionable defect found.

Review performed as fresh read-only TASK using software-code-review, Astra/medium; Fable unavailable. This is not owner or release approval.
