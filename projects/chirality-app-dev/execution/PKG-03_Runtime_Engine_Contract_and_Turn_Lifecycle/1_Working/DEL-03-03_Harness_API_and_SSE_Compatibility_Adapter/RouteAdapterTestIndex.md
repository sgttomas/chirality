# Route Adapter Test Index — DEL-03-03

| Field | Value |
|---|---|
| Purpose | Working index mapping each in-scope `/api/harness/*` route to the live tests that pin its behavior, with fixture-capture status and honest OPEN entries where coverage is missing |
| Authority | D-APP-65 disposition 4 (owner acceptance unlocking the D-APP-56 R4-P48 documentation-production deferral for DEL-03-03) |
| Source requirements | DEL-03-03-REQ-001, -REQ-002, -REQ-003, -REQ-004, -REQ-008, -REQ-010 (`ScopeOfWork.md` CLM-009); route catalog per `docs/SPEC.md` §17.1 and `docs/PRD.md` §9.1 (`ScopeOfWork.md` CLM-003) |
| Date | 2026-07-18 |
| Status statement | Content is agent findings from reading the live test and source files at working-tree state. No acceptance or issuance is rendered (K-AUTH-1). |

## 1. Method and indexed files

This index was produced by reading the live test files below and the route
sources under `frontend/src/app/api/harness/`. It records what actually
exists; it does not invent coverage. All paths are relative to
`projects/chirality-app-dev/`.

| File | Lines | Scope |
|---|---:|---|
| `frontend/src/__tests__/api/harness/routes.test.ts` | 1546 | Session create/list/get/delete, boot, turn SSE, interrupt, disconnect, persona gate, events replay |
| `frontend/src/__tests__/api/harness/agent-sdk-dev-turn.test.ts` | 344 | Route-level `agentSdk` turn through the real SDK `query` with a scripted offline subprocess |
| `frontend/src/__tests__/api/harness/agents-route.test.ts` | 87 | `GET /api/harness/agents` roster and direct-chat filter |
| `frontend/src/__tests__/api/harness/permission-route.test.ts` | 64 | `POST /api/harness/permission` operator verdict delivery |
| `frontend/src/__tests__/api/harness/scaffold-route.test.ts` | 142 | `POST /api/harness/scaffold` |
| `frontend/src/__tests__/lib/harness-client.test.ts` | 365 | Browser client helpers (`src/lib/harness/client.ts`): request shapes and SSE frame parsing against mocked responses |

Note: the client test lives under `__tests__/lib/`, not `__tests__/api/harness/`;
it is included because it pins the browser-side half of the route contract
(URLs, methods, body shapes, SSE frame parsing).

## 2. Route-to-test index (SPEC §17.1 / PRD §9.1 catalog)

Fixture-path and baseline-SHA columns follow the CLM-019 template. No captured
request/response/SSE fixture files exist in the repository for any route (see
OPEN-1): all current coverage is behavioral, driven by in-test scripted
engines. `routes.test.ts` line numbers refer to the `it(...)` opening line.

| Route | Method | Covering tests (file : line — test name) | What is pinned | Fixture Path | Baseline SHA | Capture Status | Replay Test Status |
|---|---|---|---|---|---|---|---|
| `/api/harness/session/create` | POST | `routes.test.ts` :166 `supports session create/list/get/delete happy path`; :205 `returns typed validation failure for missing projectRoot`; :224 `returns typed failure when projectRoot is inaccessible at create time`; :244 `rejects projectRoot selections that overlap instruction root`; :1359/:1379/:1393/:1404 direct-chat persona gate (D-APP-24); `harness-client.test.ts` :56 `creates sessions through create route` | 200 session envelope; typed `INVALID_REQUEST`-class validation failures; instruction-root overlap rejection; Type-2 persona rejection for CHAT mode; client URL/method/body | NONE | TBD | OPEN | NONE |
| `/api/harness/session/boot` | POST | `routes.test.ts` :265 `boots sessions and persists boot metadata`; :319 `passes subagentGovernance through boot opts...`; :352/:371 `SESSION_NOT_FOUND` cases; :392 `WORKING_ROOT_INACCESSIBLE`; :413 `PERSONA_NOT_FOUND`; :435 `INSTRUCTION_ROOT_INVALID`; :456 `preserves INSTRUCTION_ROOT_INVALID taxonomy across boot route bundle boundaries`; :499 `returns SDK_FAILURE when bootstrap turn exits non-zero`; `harness-client.test.ts` :83 `surfaces typed boot errors for non-2xx responses` | Boot metadata persistence; the typed error taxonomy (404/500 classes); cross-bundle taxonomy stability; client typed-error surfacing | NONE | TBD | OPEN | NONE |
| `/api/harness/session/list` | GET | `routes.test.ts` :166 (list leg); `harness-client.test.ts` :313 `lists sessions for a working root` | 200 `sessions[]` envelope filtered by `projectRoot`; client query-string encoding | NONE | TBD | OPEN | NONE |
| `/api/harness/session/[id]` | GET/DELETE | `routes.test.ts` :166 (get, delete, get-after-delete 404 legs); `agent-sdk-dev-turn.test.ts` :315-321 (GET pins persisted `sdkSessionId`/`sdkPackageVersion` after an agentSdk turn) | GET 200 envelope; DELETE `{ ok: true }`; `SESSION_NOT_FOUND` after delete; SDK session metadata persistence | NONE | TBD | OPEN | NONE |
| `/api/harness/turn` | POST | `routes.test.ts` :522 pre-stream `SESSION_NOT_FOUND` (404 JSON, engine not invoked); :552 `streams ordered SSE events for turn execution`; :581/:647/:704/:767 subagent-governance gating on the turn path; :826 `emits typed process-exit metadata when runtime turn execution fails` (also pins `turn:error`); :853 pre-stream `MISSING_API_KEY` (503 JSON); :884/:919/:969/:993/:1027 attachment resolution and warning paths; :1066 overlapping turn → 409 `TURN_IN_PROGRESS` + lock release; :1134 interrupt of active stream; :1186 disconnect cancellation persistence + key redaction; :1251 cross-bundle turn/interrupt coherence; `agent-sdk-dev-turn.test.ts` :261 full route-level agentSdk turn (exact 9-event SSE sequence incl. `harness:event`, spawn args, key redaction, replay parity); `harness-client.test.ts` :106/:143/:180/:213 client SSE frame parsing and payload shapes | SSE content-type; ordered event names `session:init` → `chat:delta` → `chat:complete` → `session:complete` → `process:exit`; typed mid-stream `turn:error` + `process:exit` metadata; pre-stream JSON error contract; single-active-turn lock; disconnect → `turn.cancelled` persisted; redaction | NONE | TBD | OPEN | NONE |
| `/api/harness/interrupt` | POST | `routes.test.ts` :1066 (interrupt of in-flight turn); :1134 `interrupt endpoint returns ok and marks active turn as interrupted`; :1251 (interrupt from a second module bundle); :1324 `returns typed failure for interrupt on unknown session` | `{ ok: true }` 200; stream then carries `harness:event` `turn.interrupted` and `process:exit` with `"interrupted":true`; 404 `SESSION_NOT_FOUND` | NONE | TBD | OPEN | NONE |
| `/api/harness/scaffold` | POST | `scaffold-route.test.ts` :33 `creates scaffolded execution-root content and returns summary payload`; :86 `returns INVALID_REQUEST when required fields are missing`; :108 `returns fail-fast diagnostics when filesystem conflicts prevent scaffolding`; `harness-client.test.ts` :248 `scaffolds execution roots through scaffold route` | Summary payload incl. `layoutValidation`/`preparationCompatibility`; typed validation failure; conflict diagnostics; client URL/method | NONE | TBD | OPEN | NONE |

## 3. Additional live routes (outside the SPEC §17.1 catalog)

These routes exist and are tested in the same directory. Per the D-APP-56
R4-P30 ownership map (`ScopeOfWork.md` CLM-013) their ownership is assigned
outside DEL-03-03; they are indexed here for completeness only.

| Route | Method | Assigned owner | Covering tests | Fixture Path / Capture Status |
|---|---|---|---|---|
| `/api/harness/session/[id]/events` | GET | DEL-05-02 (replay ownership) | `routes.test.ts` :1418 `replays persisted events with an honest malformed-line count`; :1511 empty replay; :1535 path-traversal rejection; :1186 (replay leg of disconnect test); `harness-client.test.ts` :338 | NONE / OPEN |
| `/api/harness/permission` | POST | PKG-06 permission owner | `permission-route.test.ts` :23 verdict delivery; :37 `decided=false` when nothing pending; :48 invalid verdict 400; :60 missing sessionId 400 | NONE / OPEN |
| `/api/harness/agents` | GET | PKG-08 agent-roster owner | `agents-route.test.ts` :60 full roster; :77 `?directChat=1` Type-0/Type-1 filter; `harness-client.test.ts` :294 | NONE / OPEN |

## 4. SSE event-name coverage (REQ-003 cross-reference)

Contract definition: `frontend/packages/harness-contract/src/types.ts` :231-296
(`UIEvent` union); stable name list `PUBLIC_UI_EVENT_NAMES` in
`frontend/packages/harness-contract/src/agent-engine-port.ts` :24, pinned by
`frontend/src/__tests__/lib/agent-engine-port.test.ts` :5 `keeps browser UI
event names stable and provider-neutral`.

| Event | Route-level SSE pin | Client-parse pin | Status |
|---|---|---|---|
| `session:init` | `routes.test.ts` :552, :581; `agent-sdk-dev-turn.test.ts` :293 | `harness-client.test.ts` :180 | PINNED |
| `chat:delta` | `routes.test.ts` :552; `agent-sdk-dev-turn.test.ts` :293 | `harness-client.test.ts` :106 | PINNED |
| `chat:complete` | `routes.test.ts` :552; `agent-sdk-dev-turn.test.ts` :293 | `harness-client.test.ts` :106 | PINNED |
| `tool:result` | none found | none found | OPEN (see OPEN-2) |
| `session:complete` | `routes.test.ts` :552, :581; `agent-sdk-dev-turn.test.ts` :293 | none found (client tests do not parse a `session:complete` frame) | PINNED at route level |
| `turn:error` | `routes.test.ts` :826 | `harness-client.test.ts` :213 | PINNED |
| `process:exit` | `routes.test.ts` :552, :826, :1134, :1251; `agent-sdk-dev-turn.test.ts` :293 | `harness-client.test.ts` :106, :180 | PINNED |
| `harness:event` (additive redacted bridge) | `agent-sdk-dev-turn.test.ts` :293-303 (exact position in stream); `routes.test.ts` :1134/:1251 assert bridged `turn.interrupted` payload content on the stream | none found | PINNED at route level; unit pins in `harness-ui-bridge.test.ts` |

## 5. Honest gap inventory (OPEN entries)

- **OPEN-1 — No captured fixtures exist.** There are no recorded
  request/response or SSE fixture files anywhere in the repository for these
  routes. Every "Fixture Path" above is NONE; all coverage is generated
  in-test by scripted engines (`StubAgentSdkManager` in
  `frontend/src/lib/harness/agent-sdk-manager.ts`; `ScriptedSdkProcess` in
  `agent-sdk-dev-turn.test.ts`; hand-written SSE frames in
  `harness-client.test.ts`). The CLM-017 step-3 capture (baseline SHA,
  captured payloads, replay-against-fixture tests) remains TBD, so
  REQ-001/REQ-010 exact-compatibility closure stays open.
- **OPEN-2 — `tool:result` has no route-level or client-parse pin.** It is
  defined in the contract and name-pinned by `agent-engine-port.test.ts`, and
  the stub manager emits it on permission-marker paths
  (`agent-sdk-manager.ts` :116, :144), but no test in
  `__tests__/api/harness/` or `harness-client.test.ts` asserts a
  `tool:result` frame on an actual route stream.
- **OPEN-3 — Disconnect-path evidence is weaker than normal/error/interrupt.**
  `routes.test.ts` :1186 pins persisted `turn.cancelled` and lock release
  after reader cancellation (stub provider only); there is no agentSdk-path
  disconnect test and no captured disconnect stream fixture. Matches
  `Assessment_INSP-03_DEL-03-03.md` gap 2.
- **OPEN-4 — No replay-against-fixture harness.** "Replay Test Status" is
  NONE for every route: the REQ-001 regression method (compare current vs
  post-extraction fixtures) cannot run until OPEN-1 capture happens.
- **OPEN-5 — Negative-path DELETE coverage is thin.** `DELETE
  /api/harness/session/[id]` is pinned only inside the :166 happy path
  (including get-after-delete 404); there is no dedicated invalid-id or
  traversal test for DELETE (the traversal pin at :1535 targets the events
  route).
