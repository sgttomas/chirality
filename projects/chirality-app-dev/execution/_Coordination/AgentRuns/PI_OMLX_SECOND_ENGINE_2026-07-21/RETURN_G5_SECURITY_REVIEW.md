# Return — G5 Independent Security and Conformance Review

- **RunID:** `PI_OMLX_SECOND_ENGINE_2026-07-21`
- **Role:** independent read-only security/conformance reviewer
- **Actual model:** `gpt-5.6-sol` (no substitution)
- **Authority:** `D-APP-72`, `SCA-APP-002`, and the owner-accepted Pi/oMLX execution plan
- **Verdict:** `PASS_AFTER_REMEDIATION_BACKCHECK`
- **Initial verdict:** `BLOCKED_PENDING_REMEDIATION` (superseded by the independent backcheck below)

## Independent remediation backcheck — 2026-07-22

The five initial findings are closed. The scripted G5 security/conformance gate now passes. No remaining code or test blocker was found for the bounded Pi/oMLX child milestone. The owner-gated live oMLX proof remains deferred until an exact tool-capable model is loaded and explicitly selected; it is not represented as completed by this receipt.

### Closed finding evidence

1. **Canonical tool evidence and oMLX-key redaction — CLOSED.**
   - `frontend/src/lib/harness/pi-event-mapper.ts:184-203` suppresses Pi's raw `tool_execution_start`/`tool_execution_update` persistence and emits only the non-sensitive UI result `{name, ok}` at tool end. The neutral bridge remains the sole persisted permission/tool lifecycle writer.
   - `frontend/src/lib/harness/run-logger.ts:64-78` includes provider-keyed Anthropic and oMLX UI credentials plus `ANTHROPIC_API_KEY`, `CHIRALITY_ANTHROPIC_API_KEY`, and `CHIRALITY_OMLX_API_KEY`, including encoded variants.
   - `frontend/src/__tests__/lib/pi-event-mapper.test.ts:65-113` proves raw sensitive paths/results are not mapped to harness evidence; `frontend/src/__tests__/lib/run-logger.test.ts:82-105` proves raw and encoded oMLX keys are redacted.
   - The real wire success at `frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts:265-310` applies strict conformance with forbidden sensitive values and verifies canonical permission-before-result persistence.

2. **Accepted-input replay and provider-neutral preflight failures — CLOSED.**
   - `frontend/src/lib/harness/turn-engine.ts:261-300` persists `message.accepted` before preflight, then persists a typed `turn.failed` with adapter/provider/model/status and `phase: preflight` before rethrowing. The outer lifecycle releases the lock.
   - `frontend/src/__tests__/lib/turn-engine.test.ts:297-360` covers `ENGINE_UNAVAILABLE`, `PROVIDER_AUTH_FAILURE`, `MODEL_UNAVAILABLE`, `PROVIDER_PROTOCOL_FAILURE`, and `CONTEXT_EXHAUSTED`, verifies accepted-message plus terminal replay for every class, and proves a later same-session recovery turn succeeds.
   - `frontend/packages/harness-contract/src/errors.ts:17-39` now uses an exhaustive `Readonly<Record<HarnessErrorType, true>>`; `frontend/src/__tests__/lib/harness-errors.test.ts:1-42` proves structural normalization preserves every new provider-neutral type while unknown values retain the legacy `SDK_FAILURE` fallback.

3. **Conformance and real Pi fake-loopback matrix — CLOSED.**
   - `frontend/packages/harness-contract/src/engine-conformance.ts:95-480` now enforces initialization order and attribution, declared capabilities, one terminal outcome, tool-ID pairing, permission ordering, compaction pairing, persisted-event correspondence, and forbidden-value redaction. Negative and positive coverage is in `frontend/src/__tests__/lib/engine-conformance.test.ts:555-719`.
   - `frontend/src/__tests__/integration/fake-openai-loopback.ts:1-170` is a reusable loopback fake supporting discovery/completion JSON, SSE, redirects, authentication, disconnects, and hangs.
   - `frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts:265-665` covers exact-model discovery, governed read, bad auth, no/unknown model, malformed discovery/schema/SSE/tool calls, discovery and completion redirects, context exhaustion, disconnect, actual hung-stream interruption, timeout cleanup, restart recovery, and concurrent cached parent/real Pi-child targeted interruption without singleton leakage.
   - Independent rerun: `npm test -- --run src/__tests__/integration/pi-omlx-wire.integration.test.ts` passed **11/11** tests in 3.45 seconds. Its malformed-SSE diagnostic printed only `[REDACTED_PROVIDER_PAYLOAD]`. The six focused non-network files passed **42/42** tests in the preceding sandboxed run; the sandbox denied loopback binding with `EPERM`, so the wire file was rerun with loopback permission and passed.

4. **Diagnostic fail-closed guard — CLOSED, with a version-coupled residual.**
   - `frontend/src/lib/harness/pi-agent-engine-adapter.ts:233-264,523-526` replaces raw malformed-provider payload diagnostics for the pinned upstream parser prefixes before Pi session creation. Unit coverage is at `frontend/src/__tests__/lib/pi-agent-engine-adapter.test.ts:431-448`; the real malformed-SSE wire run independently demonstrated redacted stderr.
   - This guard is deliberately narrow and coupled to the pinned Pi/OpenAI parser messages. A Pi upgrade must re-run the malformed-wire diagnostic proof and review upstream logging before the dependency pin changes.

5. **Packaged production route, secrets, and supply-chain evidence — CLOSED.**
   - `frontend/scripts/run-packaged-pi-runtime-proof.mjs:234-499` loads the packaged Next production turn route from `app.asar`, then traverses the production route, registry, Pi adapter, oMLX discovery/completion, neutral tool bridge, and session persistence rather than constructing Pi directly.
   - `frontend/artifacts/harness/packaged-pi/latest/summary.json` records `PASS` for `offline-packaged-production-pi-route-fake-loopback-read-tool`: HTTP 200, Pi/oMLX exact-model attribution, package `0.80.10`, canonical permission/tool/terminal persistence, four authenticated provider requests, and both raw fixture content and the oMLX credential absent from session evidence. `stderr` is empty.
   - `frontend/artifacts/harness/security/latest/secret-scan-summary.json` records `pass`: 2,686 files scanned (2,621 tracked, 73 untracked, 8 generated artifacts), 0 blocked findings, and explicit `CHIRALITY_OMLX_API_KEY` environment input handling. No live environment key was present during that scan; the packaged proof independently injects a synthetic oMLX key and proves it absent from evidence.
   - Independent `node scripts/verify-pi-supply-chain.mjs` rerun passed: exact `@earendil-works/pi-coding-agent@0.80.10`, 140 closure artifacts, SHA-512 integrity, only `@google/genai` and `protobufjs` on the install-script allowlist, explicit native/WASM ASAR unpack policy, and the Pi third-party notice present.

### Remaining blockers and residuals

- **Code/security/conformance blockers:** none found in this backcheck.
- **Human-gated acceptance still outstanding:** the opt-in live oMLX proof requires the owner to load and explicitly select an exact tool-capable model and configure the provider credential. Until then, no claim of real-model compatibility, tool quality, or live timing evidence is warranted.
- The packaged Pi dependency closure remains broad and includes unused remote-provider/platform code. It is inert under Chirality's explicit adapter/resource/provider restrictions but should remain under versioned supply-chain review and may be minimized later.
- The read path retains an ordinary same-user filesystem time-of-check/time-of-use window. Stronger no-follow/open-by-handle semantics remain a future hardening option if concurrent hostile local mutation enters the threat model.
- The diagnostic redaction shim is tied to pinned upstream parser strings as noted above; dependency upgrades require explicit revalidation.

## Initial findings — historical, superseded by the backcheck above

### P1 — Pi tool events bypass the neutral bridge's redacted evidence policy

`frontend/src/lib/harness/pi-event-mapper.ts:203-253` creates a second persisted `tool.started`/`tool.completed` lifecycle containing raw `event.args` and raw `toolOutput(event.result)`. The guarded neutral bridge already persists the authoritative permission, summarized input, budgeted result metadata, and optional redacted artifact at `frontend/src/lib/harness/chirality-tool-bridge.ts:183-265`. Consequently one Pi read currently produces duplicate tool lifecycle records, and the mapper copy can place the entire file body directly in `events.jsonl`, outside the bridge's result budget and metadata-only policy. The wire proof explicitly demonstrates the file body in the Pi tool result but checks only replay event names (`frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts:177-190`), so it does not detect this leak.

The common event redactor does not close the gap for oMLX credentials: `frontend/src/lib/harness/run-logger.ts:64-69` recognizes only the Anthropic UI/environment keys. It omits both the provider-keyed oMLX UI key and `CHIRALITY_OMLX_API_KEY`. A read file, tool error, or other persisted value containing that key can therefore retain it.

**Required remediation:** make the neutral bridge the sole persisted tool-evidence writer for Pi; do not persist raw Pi tool args/results, and use one canonical `toolUseId` pairing. Extend configured-key redaction to every supported provider, including oMLX UI and environment sources. Add replay assertions using both arbitrary sensitive file content and the configured oMLX key, proving neither appears in JSONL or artifacts while permission/result metadata remains attributable.

### P1 — Provider preflight failures do not preserve accepted input for replay

`frontend/src/lib/harness/turn-engine.ts:295` runs adapter preflight before `message.accepted` is appended at lines 298-313. Connection refusal, missing/bad authentication, no loaded model, unknown model, redirect, and malformed `/models` responses therefore reject `runTurn()` before the user input or a typed terminal failure is persisted. The lock is released, but the accepted-input/replay requirement is not met.

**Required remediation:** establish and persist the turn/message acceptance boundary before provider preflight, then persist a typed terminal failure when preflight fails, without transmitting a prompt or falling back. Add TurnEngine-level replay tests for each preflight failure class and prove the next turn can run.

### P1 — The required conformance and failure matrix is not implemented

The shared conformance runner enumerates only stream/public-event, `session:init`, and terminal `process:exit` checks (`frontend/packages/harness-contract/src/engine-conformance.ts:9-21,64-188`). It does not enforce paired tool IDs, permission-before-handler evidence, persistence/replay, redaction, declared capabilities, compaction pairing, or unique canonical turn outcomes as required by the accepted plan.

The only real Pi wire integration is a success-path read (`frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts:109-191`). There is no wire-level coverage for redirecting completion requests, bad auth, empty/unknown models, malformed SSE/JSON/tool calls, context exhaustion, hung streams, disconnects, restart recovery, or interrupting an actual hung stream. There is also no end-to-end concurrent Claude-parent/Pi-child routing proof; the delegation tests stop at metadata/launcher handoff. Thus the recorded full-suite pass cannot substantiate the milestone's explicit fail-closed and singleton-isolation acceptance claims.

**Required remediation:** extend the reusable conformance suite and fake loopback provider to cover the accepted matrix, including lock release and replay on every failure. Add a real runtime/delegation integration with a Claude or scripted Claude parent and a Pi child running concurrently through the registry.

### P2 — Provider-neutral errors are not fully recognized by the compatibility normalizer

`frontend/packages/harness-contract/src/errors.ts:17-29` omits `ENGINE_UNAVAILABLE`, `MODEL_UNAVAILABLE`, `PROVIDER_AUTH_FAILURE`, `PROVIDER_PROTOCOL_FAILURE`, and `CONTEXT_EXHAUSTED` from `isHarnessErrorType`, despite those values being public in `types.ts`. A structurally equivalent error crossing a bundle/module boundary is downgraded by `asHarnessError()` to legacy `SDK_FAILURE` instead of retaining its provider-neutral type.

**Required remediation:** keep the runtime guard exhaustive with `HarnessErrorType` and add structural-normalization tests for all new failure types.

### P2 — The packaged proof bypasses the production adapter boundary

`frontend/scripts/run-packaged-pi-runtime-proof.mjs:109-185` imports Pi directly, constructs its own runtime/resource loader, and supplies a hand-written `read_file`. It does not import or execute the packaged `PiAgentEngineAdapter`, production oMLX validator/discovery, neutral tool bridge, permission/evidence path, or runtime registry. This proves SDK/assets load from ASAR, but not the audit closeout claim that the packaged production adapter executes the bounded turn.

**Required remediation:** retain the asset smoke proof if useful, but add a packaged proof that invokes the production adapter/runtime against the fake loopback server and verifies canonical persistence, tool permission evidence, attribution, redirect refusal, and terminal cleanup.

## Confirmed controls

- Ambient Pi resources are explicitly disabled with in-memory settings/models/credentials/session state and override-empty resource collections (`pi-agent-engine-adapter.ts:448-545`), with sentinel coverage.
- Both discovery and completion configuration require literal `http://127.0.0.1:<port>/v1`, reject URL credentials/query/fragment, and force manual redirects (`omlx-provider-config.ts:38-74,117-157`; `pi-agent-engine-adapter.ts:189-251`).
- Secure storage uses separate Anthropic/oMLX blobs, provider allowlisting, and status-only renderer responses; decrypted keys are not returned over IPC (`electron/api-key-storage.ts:13-148`; `electron/api-key-ipc.ts:93-134`).
- Managed delegation and adapter defense-in-depth restrict the selection to `pi`/`omlx`, an approved parented Agent 2, exact `read_file`, one tool, no write targets, and no attachments (`managed-delegation.ts:209-256`; `pi-agent-engine-adapter.ts:321-405`).
- The read handler checks project/declared-scope containment, symlink traversal, regular-file status, and the governed byte budget before returning content (`tool-path-policy.ts:240-289`; `chirality-tool-bridge.ts:294-335`).
- The dependency is exactly pinned; the supply verifier passes all 140 closure artifacts with SHA-512 integrity, fixed install-script allowlisting, explicit native/WASM rules, and a shipped notice. The remaining broad optional-provider/platform payload is a recorded packaging surface and does not by itself grant runtime authority.

## Initial residual-risk forecast

- The packaged Pi closure remains large and includes unused remote-provider/platform code. Minimize it in a later packaging tranche or keep it under explicit versioned review.
- The read path has an ordinary local filesystem time-of-check/time-of-use window; stronger no-follow file opening can be considered if same-user concurrent mutation becomes part of the threat model.
- Live oMLX/model proof remains correctly deferred until the owner loads and explicitly selects a tool-capable model and configures its credential.

That remediation condition has now been satisfied by the independent backcheck recorded at the top of this receipt. G5 may be marked PASS for the scripted milestone, subject to the explicitly deferred live-model proof and residuals stated there.
