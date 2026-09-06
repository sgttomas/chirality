# Diagnostic extension return

AMENDMENT4 changes only unknown non-request notification handling. Unknown methods and non-text item kinds enter a non-authorizing quarantine: counts only, no raw payloads, method names, account material or emitted output. At most1024 diagnostics per session; overflow closes transport. `diagnostics()` returns quarantinedNotifications and retryableErrors, counting only explicit willRetry:true on method:error. Nothing retries or resends a turn.

Known thread/turn/message transitions and terminals remain strict; server messages carrying request IDs plus methods still fail closed, never grant approvals. A retryable error followed by EOF/process exit0 produces a transport error, not a terminal. Only actual validated turn/completed settles terminal state. Existing actor/test preimages are stored losslessly beside this record; original CODEX_SESSION seals remain historical and unchanged. This new OUTPUTS seal names current source bytes.

Validation: workspace typecheck PASS;10 actual controlled-child tests PASS (609ms), including unknown diagnostics followed by valid terminal, unknown-only timeout, retryableerror+actual cleanexit without terminal, quarantine overflow, malformed known terminal and unknown server approval denial. Initial assertions raced asynchronous delivery/reaping; corrected tests wait for bounded completion, with failures not counted as passes.

Author OpenAI GPT-6, serving ID unavailable; bounded Agent2 role instruction-asserted/not mechanically enforced; no delegation. No actual hosted execution/account/network. Exact0.149 offline diagnostics are input evidence, not terminal schema proof.
