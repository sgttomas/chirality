# R15 frontend second-chat repair return

TASK /root/r14_history_repair, GPT-6 Astra medium as directed; actual delegated-harness-native execution, no descendants. Parent HELP_HUMAN. Brief: frontend-only reconciliation and error projection for created-but-unconfirmed bootstrap, preserve identity/models/roles/drafts, avoid duplicate creation or automatic retries. Upstream source-bounded diagnosis is RETURN.md in this directory. Current source HEAD and exact output hashes in FRONTEND_SCOPE.json. This is derivative implementation evidence, not native qualification or authority acceptance.

## Changes

Created session identity remains owned after boot failure. Subsequent explicit Send reads that same session; it does not create or bootstrap again. Only bootedAt + bootFingerprint + engineSessionId confirms completion. Pending, failed/interrupted and unknown states retain the unsent draft and prevent the real prompt from running. A conflicting response/changed role or folder is rejected. Explicit New Chat clears pending state. Model/effort selectors remain locked to the created session's recorded pair during uncertainty.

Current v3 history readers add optional bootstrapConfirmed. Reopening a known-unbooted history entry reconciles before sending, including the native-observed old timed-out chat case. Legacy projections without this additive flag preserve prior behavior. A full app restart can find the same canonical session through history; no new local session authority is introduced.

Typed RuntimeTransportError timeout/transport and server BOOT_TIMEOUT/BOOT_CANCELLED retain sanitized operation/session identity in structured error details. Primary copy is concise: Chat took too long to start; Your message is saved; Send again to check this chat, or start a new chat. Saved-message copy is used only when ChatPanel confirms its pre-prompt failure path. Failed/cancelled state directs a new chat; context conflicts direct restoring the original role/folder or a new chat. Raw causes/socket details/session IDs are absent from primary copy. Authentication, fencing, model admission and cancellation settlement are unchanged by frontend work.

## Validation and handoff

Focused Vitest: 87/87 passing across chat-panel-folder-binding, runtime-daemon-harness-port, harness-error-display and operator-projection. Coverage includes timeout then still-running reconciliation, later completed reattachment sends exactly one real prompt with no extra create/boot, failed/interrupted/unknown blocking, preserved terra/high visible pair, historical unbooted recovery, deliberate new-chat reset, safe timeout/cancellation copy and v3/legacy projection behavior. Earlier test fixture had reasoningEffort at the wrong nesting; corrected to canonical top-level field, final tests pass. git diff --check passed before final evidence write.

Exact source write scope is listed in FRONTEND_SCOPE.json. No woven-shell, Runtime source, auth/live session state, logs, UI/native execution, network, build, packaging, full suite or commits were performed. Coordinated exact typed timeout contract directly with /root/r13_second_turn_diagnosis under parent authorization. Parent owns combined review, integrated typecheck/full tests and later authorized native verification. Remaining native qualification is open; source fixes are frozen for fan-in.


## Independent review repair

Reviewer identified missing role comparison on pending reconciliation. Added strict matching against authoritative v3 roleId, or legacy persona for older records, before accepting boot status. Missing or mismatched role returns a context conflict and never streams; existing model lock/reconciliation logic is unchanged. Parameterized regression covers v3 mismatch despite matching legacy persona, missing v3 roleId, legacy mismatch and missing legacy persona. Successful reconciliation fixtures now declare their real role. Focused chat-panel-folder-binding suite: 46/46 passed. Source hashes refreshed; bounded repair frozen for reviewer backcheck.
