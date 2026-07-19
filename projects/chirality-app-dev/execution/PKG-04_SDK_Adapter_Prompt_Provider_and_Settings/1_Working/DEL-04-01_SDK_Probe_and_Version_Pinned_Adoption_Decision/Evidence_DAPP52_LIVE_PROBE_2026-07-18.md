# Evidence: D-APP-52 Live SDK Probe and Packaged Live Proof (2026-07-18)

## Authority

D-APP-52 ruling O-A riders 1–11. The deferred live-LLM demonstration was
executed as the owner's in-session act on 2026-07-18: owner at screen,
short-lived owner-supplied key, never persisted. Code SHA at capture
`a91f72b19aeb6dbca7e565fe336c91ce7e841421`; model `claude-sonnet-5`.
Recorded by WI-PKG04-01 as mechanical conformance under RunID
`DAPP52_LIVE_DEMONSTRATION_2026-07-18` (D-APP-64 overlay; see
`_run_records/TASK_RUN_2026-07-18_DAPP52_live_demonstration_closures.md`).

## Artifacts (traceability)

| Artifact | SHA-256 |
|---|---|
| `Evidence_DAPP52_LIVE_PROBE_2026-07-18_summary.json` (PACK1, byte-verbatim copy of the session capture) | `be155013371f51c1a52a364d19d9f164f9f2509bd921ca4d1af7b00b25a11686` |
| `Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json` (PACK3, byte-verbatim copy of the session capture) | `ac3507b043e5470a7ec16afebdf205e59f6b631b6ada552e44941fd603945e78` |

Every fact below is traceable to these JSON artifacts by the SHA-256 above.
Both artifacts passed the redaction scan (no `sk-ant-` material; re-verified
at copy time).

## PACK1 — dev SDK probe (`frontend/scripts/run-dapp52-live-sdk-probe.mjs`, new; status pass; redaction scan pass)

- Pinned `@anthropic-ai/claude-agent-sdk@0.3.150`; live **claudeCodeVersion
  2.1.150**; node v24.5.0; darwin:arm64.
- Live `query()` message sequence (phase 1): `system/init` → `assistant`
  (thinking block) → `assistant` (tool_use `Read`) → `user` (tool_result) →
  `assistant` (text) → `result/success` with `is_error:false`; every message
  carries `session_id`.
- `result` message top-level keys observed: `api_error_status,
  duration_api_ms, duration_ms, fast_mode_state, is_error, modelUsage,
  num_turns, permission_denials, result, session_id, stop_reason, subtype,
  terminal_reason, total_cost_usd, ttft_ms, type, usage, uuid`.
- Session/transcript placement: transcript JSONL at
  `CLAUDE_CONFIG_DIR/projects/<escaped-cwd>/<session-uuid>.jsonl`; the config
  dir also gains `.claude.json`, `backups/`, `policy-limits.json`; the
  controlled `HOME` stays empty; the project cwd is untouched beyond the read
  target.
- Live error shapes:
  - Invalid key → repeated `system/api_retry` events `{attempt,
    max_retries:10, retry_delay_ms, error_status:401,
    error:"authentication_failed"}` then a synthetic assistant message and
    `result{subtype:"success", is_error:true, api_error_status:401,
    result:"Failed to authenticate. API Error: 401 API key is invalid."}`.
  - Unreachable base URL → `api_retry` with `error_status:null,
    error:"unknown"`.
  - Abort → thrown `Error("Claude Code process aborted by user")`.
- Interrupt behavior (REQ-010): abort after init ends the stream after three
  messages with the same abort error; no partial result message.

## PACK3 — packaged live proof (`frontend/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs`, existing, run against a fresh `desktop:pack` bundle; status pass; redaction pass)

- Packaged SDK 0.3.150 / claudeCodeVersion 2.1.150; platform binary
  `@anthropic-ai/claude-agent-sdk-darwin-arm64` under
  `app.asar.unpacked/node_modules`.
- Live sequence `init → assistant → user → assistant → result/success`; Read
  tool use and proof token observed; no error result.

## Not evidenced

The RATE_LIMITED error shape was NOT live-triggered in this run (bounded and
recorded as such — no fabricated shape); DEL-04-05 RQ-011's four-class
assertion gap remains that deliverable's own gated item. This record makes no
adoption verdict, no release claim, and no professional claim. D-APP-63 rider
check performed: no DEL-04-04 (PersonaComposer / instruction-root)-relevant
output was produced by any pack, so no new dependency row is minted.
