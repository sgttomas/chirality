# SSE Compatibility Fixture README — DEL-03-03

| Field | Value |
|---|---|
| Purpose | Describe the fixture capture source, replay method, and expected event sequences for the harness SSE compatibility adapter, grounded in the live code and tests |
| Authority | D-APP-65 disposition 4 (owner acceptance unlocking the D-APP-56 R4-P48 documentation-production deferral for DEL-03-03) |
| Source requirements | DEL-03-03-REQ-003, -REQ-004, -REQ-005, -REQ-007 (`ScopeOfWork.md` CLM-009); event names per `docs/SPEC.md` §11, `docs/TYPES.md` §7.4, `docs/PRD.md` §9.3 as restated in `ScopeOfWork.md` CLM-003/CLM-024 |
| Date | 2026-07-18 |
| Status statement | Content is agent findings from reading the live source and test files at working-tree state. No acceptance or issuance is rendered (K-AUTH-1). |

All paths are relative to `projects/chirality-app-dev/`.

## 1. What the "fixtures" currently are — capture source

There are **no recorded capture files** (no stored request/response or SSE
stream dumps) in the repository. The compatibility evidence today comes from
three scripted, deterministic in-test sources that stand in for captured
fixtures:

1. **`StubAgentSdkManager`** — `frontend/src/lib/harness/agent-sdk-manager.ts`.
   The default test-provider engine behind the route tests. It emits scripted
   `UIEvent` sequences keyed by message markers:
   - default path: `session:init` → `chat:delta` (chunked) → `chat:complete`
     → `session:complete` → `process:exit`;
   - `TURN_SDK_FAIL_TEST` → throws `HarnessError('SDK_FAILURE', 500, ...)`,
     which the turn engine converts to `turn:error` + `process:exit`;
   - `INTERRUPT_SIGINT_TEST` → holds the turn open until interrupted, then
     bridged `interruption.completed` / `turn.interrupted` `harness:event`s
     and `process:exit` with `exitCode: 130, interrupted: true`
     (`agent-sdk-manager.ts` :36-51);
   - `__BOOT_SDK_FAIL__` model marker → `process:exit` with `exitCode: 1`;
   - `UNAPPROVED_DENY_TEST` / `UNAPPROVED_ALLOW_TEST` under `dontAsk` mode →
     scripted `tool:result` frames (`agent-sdk-manager.ts` :116, :144). Note:
     these paths are exercised by lib-level tests, not by any route-level test
     (see §6).
2. **`ScriptedSdkProcess`** — `frontend/src/__tests__/api/harness/agent-sdk-dev-turn.test.ts`
   :50-133. An offline `SpawnedProcess` stand-in that writes real
   `stream-json` `SDKMessage` frames (system init, `stream_event` text delta,
   result) into the **real** SDK-manager → `sdk-message-mapper.ts` →
   `harness-ui-bridge.ts` pipeline, so the route-level agentSdk stream is
   produced by the live mapping code, not by a stub of it.
3. **Hand-written SSE frame strings** — `frontend/src/__tests__/lib/harness-client.test.ts`
   `sseResponse()` :22-44. Literal `event: ...\ndata: {...}\n\n` chunks used
   to pin the browser client's frame parser (`src/lib/harness/client.ts`)
   against the wire format.

The wire format itself is produced by `formatSseEvent` in
`frontend/src/lib/harness/http.ts` :43-45
(`event: <type>\ndata: <JSON>\n\n`), invoked by the transport adapter
`frontend/src/app/api/harness/turn/route.ts` :19-21, which encodes whatever
`TurnEngine.runTurn(...).events` yields and owns no event vocabulary of its
own.

**Real-capture status: TBD/OPEN.** The `ScopeOfWork.md` CLM-017 step-3
capture (record baseline commit SHA, capture live route/SSE payloads for
success, error, and disconnect paths) has not been performed; no baseline SHA
is recorded. Exact payload-level compatibility assertions therefore remain
open, per REQ-001 and the CLM-019 template.

## 2. Replay method

How the scripted fixtures are replayed in the current tests:

- **Server-side (route level):** tests invoke the route handlers directly
  (`turnRoute.POST(new Request(...))`) and read the SSE stream either whole
  (`await response.text()`) with ordered-substring assertions
  (`expectOrdered`, `routes.test.ts` :101-108) or incrementally via
  `response.body.getReader()` for interrupt/disconnect timing
  (`routes.test.ts` :1082, :1149, :1203). Client disconnect is replayed with
  `reader.cancel(...)` (:1206), which drives the route's `cancel()` →
  `runningTurn.cancel()` path (`turn/route.ts` :30-32).
- **Browser-side (client level):** `harness-client.test.ts` mocks `fetch` to
  return a `ReadableStream` of SSE chunks and asserts the parsed
  `{ event, data }` sequence delivered by `streamHarnessTurn`.
- **Persisted replay (live == replay):** `harness:event` frames carry the
  same redacted `HarnessEvent` shape that is persisted to `events.jsonl`
  (`frontend/src/lib/harness/harness-ui-bridge.ts` :5-34), so a stream can be
  cross-checked against `GET /api/harness/session/[id]/events`.
  `agent-sdk-dev-turn.test.ts` :323-333 pins this parity (persisted sequence
  `message.accepted` → `turn.accepted` → `turn.started` →
  `adapter.initialized` → `model.delta` → `message.delta` →
  `model.completed` → `turn.completed` for the scripted dev turn).

When real fixture capture lands (OPEN), the intended replay method per
REQ-001/CLM-011 is: store captured request/response/SSE payloads with their
baseline SHA, then replay the captured requests against the post-extraction
adapter and diff against the stored streams. No such harness exists yet.

## 3. Expected event sequences (test-pinned)

Only source/test-backed order constraints are listed; per REQ-003, event
ordering is otherwise unconstrained in this deliverable.

### 3.1 Successful turn — stub provider

`session:init` → `chat:delta` (1..n) → `chat:complete` → `session:complete`
→ `process:exit` (`exitCode: 0`).
Pinned: `routes.test.ts` :552 `streams ordered SSE events for turn execution`
and :581 (ordered-substring assertions over the full stream).

### 3.2 Successful turn — agentSdk provider (scripted offline subprocess)

Exact 9-frame sequence pinned by `agent-sdk-dev-turn.test.ts` :293-303:

`session:init` → `harness:event` (`turn.accepted`) → `harness:event`
(`turn.started`) → `chat:delta` → `harness:event` (`model.completed`) →
`harness:event` (`turn.completed`) → `chat:complete` → `session:complete` →
`process:exit`.

Per-token `model.delta`/`message.delta` and boot-time `adapter.initialized`
are deliberately **not** bridged as `harness:event` (skip set
`HARNESS_EVENT_STREAM_SKIP`, `harness-ui-bridge.ts` :19-23); they appear only
in the persisted log, covered on-stream by `chat:delta` / `session:init`.

### 3.3 Mid-stream failure

`turn:error` (`phase: "mid-stream"`, typed `errorType`, `status`,
`severity: "error"`, `fatal: true`, `details`) → `process:exit`
(`exitCode: 1` plus mirrored error metadata).
Pinned: `routes.test.ts` :826-851; client-side parse `harness-client.test.ts`
:213 (`turn:error`) and :180 (`process:exit` error payload).

### 3.4 Interrupt

Stream ends with bridged `harness:event` frames whose payloads include
`"type":"turn.interrupted"` and a terminal `process:exit` containing
`"interrupted":true` (stub emits `exitCode: 130`).
Pinned: `routes.test.ts` :1134-1184 and, across module-bundle boundaries,
:1251-1322. The interrupt route itself returns JSON `{ ok: true }`.

### 3.5 Client disconnect

No further SSE is delivered (the reader is cancelled); the route `cancel()`
path records a non-user `turn.cancelled` event (`reason:
"client_disconnect"`, `frontend/src/lib/harness/turn-engine.ts` :340-348)
in `events.jsonl`, verifiable via the events replay route, and releases the
turn lock so a follow-up turn succeeds.
Pinned: `routes.test.ts` :1186-1249 (stub provider only — see §6).

### 3.6 Pre-stream failures are JSON, not SSE

Requests rejected before the stream starts return typed JSON errors, never a
partial stream: `SESSION_NOT_FOUND` 404 (`routes.test.ts` :522),
`MISSING_API_KEY` 503 (:853), `TURN_IN_PROGRESS` 409 on overlapping turns
(:1066). `turn:error` is reserved for mid-stream failures.

## 4. Event-name contract

The REQ-003 named events plus the additive redacted `harness:event` bridge
are defined as the `UIEvent` union in
`frontend/packages/harness-contract/src/types.ts` :231-296 and enumerated as
`PUBLIC_UI_EVENT_NAMES` in
`frontend/packages/harness-contract/src/agent-engine-port.ts` :24. The full
list — `session:init`, `chat:delta`, `chat:complete`, `tool:result`,
`session:complete`, `turn:error`, `process:exit`, `harness:event` — is
name-pinned by `frontend/src/__tests__/lib/agent-engine-port.test.ts` :5, and
provider-shaped public names are rejected by
`frontend/src/__tests__/lib/engine-conformance.test.ts` (engine conformance
suite). Per-event route-level pin status is tabulated in
`RouteAdapterTestIndex.md` §4.

## 5. Redaction guarantee on the bridge

`harness:event` payloads pass through `redactJsonLike`
(`frontend/src/lib/harness/run-logger.ts` :93) before emission
(`harness-ui-bridge.ts` :30-33), the same helper used for persistence, so
configured API keys never reach the browser stream or the event log.
Test-pinned: `agent-sdk-dev-turn.test.ts` :339-342 (neither the UI key nor
the prior env key appears in the raw SSE or the persisted evidence);
`routes.test.ts` :1186-1238 (`[REDACTED_API_KEY]` substitution in persisted
`message.accepted`, secret absent from `events.jsonl`); unit pin
`frontend/src/__tests__/lib/harness-ui-bridge.test.ts` :49.

## 6. Honest limits (what is NOT test-pinned here)

- **No captured fixture files.** Everything in §3 is generated by scripted
  in-test engines; real capture with a recorded baseline SHA remains TBD
  (`RouteAdapterTestIndex.md` OPEN-1/OPEN-4).
- **`tool:result` never appears in a route-level or client-parse test.** The
  stub emits it only on permission-marker paths that route tests do not
  exercise; its shape is contract-defined and name-pinned only
  (`RouteAdapterTestIndex.md` OPEN-2).
- **Disconnect coverage is stub-provider only** and asserts persisted
  cancellation rather than a captured disconnect stream
  (`RouteAdapterTestIndex.md` OPEN-3).
- **`session:complete` has no client-parse pin** (route-level pins only).
- **Event payload examples are not normative.** Exact JSON payloads per event
  remain TBD pending fixture capture (`ScopeOfWork.md` CLM-026); the shapes
  in `types.ts` are the contract source.
