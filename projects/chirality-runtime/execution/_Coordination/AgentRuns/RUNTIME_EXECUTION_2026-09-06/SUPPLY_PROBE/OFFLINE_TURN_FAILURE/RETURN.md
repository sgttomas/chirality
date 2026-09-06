# Offline invalid-model turn failure-path diagnostic

Parent-authorized actual local protocol test, OpenAI GPT-6 ephemeral Agent 2; exact serving ID unavailable, role instruction-asserted and not mechanically enforced; no delegation. One fresh private HOME, work and temp; no credentials and account/read confirmed account=null. Exact original 0.149.0 payload, existing hard network-deny/home-read-deny/Keychain-deny/write-contained profile.

## Actual observations

Explicit invalid model offline-invalid-model, ephemeral thread, approvalPolicy never and workspace-write were admitted. turn/start returned turn.status=inProgress. thread/status/changed active, turn/started, and userMessage item/started and item/completed followed. The request's input text parsed; response userMessage content includes text_elements:[] automatically.

The invalid model DOES NOT guarantee a local rejection. A warning reports fallback model metadata. Exact binary attempted WebSocket provider endpoint wss://api.openai.com/v1/responses; hard network denial prevented connection. It internally retried, emitting method:error with params.error.codexErrorInfo.responseStreamDisconnected.httpStatusCode=null and params.willRetry=true. Later warning announces HTTPS fallback; final captured retry error says waiting for network. This is denied-egress inventory, not successful provider access. No login, credentials, hosted inference, tools or completed network connection.

No terminal turn/completed arrived within the bounded twelve-second observation. Stdin closed and process exited0; that exit is transport teardown, NOT successful or failed turn terminal evidence. Consumers must not fabricate turn completion from error notifications, especially willRetry=true. Terminal schema remains unavailable from this run.

## Preflight, teardown and limits

Independent preflight first tested socket allocation, which the OS permits without network access. Its assertion stopped before App Server launch. Corrected preflight tests actual loopback connect and records PermissionError errno1. An incidental Python launcher cache write was also denied. Only the corrected preflight proceeded; exact trace retained. No relaxed profile, enabled-network retry, real-model retry, account import or login occurred.

Fresh failure_home/failure_work/failure_tmp removed after process exit; auth.json absent. Exact accepted binary hash unchanged and retained only for parent aggregate diagnostic. The pre-existing supply/home belongs to prior diagnostic stages and remains isolated, not an operational account. Final artifact teardown awaits parent signal.
