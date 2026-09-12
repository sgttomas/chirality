# D — Model and Reasoning Selectors (design)

Owner criterion 6. Role: TASK (read-only design). Engine: Codex app-server only.
Paths: `R` = `projects/chirality-runtime`, `F` = `projects/chirality-app-dev/frontend`
(both under the worktree root). Line numbers are from the current worktree bytes.

## 0. Verified facts the design rests on

- `R/packages/daemon/src/codex-session.ts:654-675` `listModelsPage` validates every
  `supportedReasoningEfforts[].reasoningEffort` (charset `^[\x21-\x7e]{1,64}$`, 1..32,
  unique, contains `defaultReasoningEffort`) then drops it at line 673.
- `R/packages/daemon/src/codex-login.ts:268-300` `resolveDefaultModel` pages `model/list`
  (max 64 pages) on the login-purpose transport, requires exactly one non-hidden
  `isDefault`, closes the transport (line 290), memoises `selectedModel`. In the v2 path
  `status()` deliberately keeps the transport open until this call (lines 335-336).
- `R/packages/daemon/src/hosted-private-composition.ts:516-522` calls it in
  `establishAdmission`, pins `context.model`/`context.defaultReasoningEffort`, folds both into
  `configDigest` (`chirality.hosted-private-config/v2`), passes `model` to the launcher
  bindings (571) and `model`/`reasoningEffort` to `admitHosted` (582); `materializeAdmission`
  returns `selection: {adapterId:"codex-app-server", providerId:"openai", model}` (627) and
  the `DelegatedRuntime` binding `actual: {…, model: context.model}` (617).
- `R/packages/daemon/src/codex-supervisor.ts`: options `model`/`reasoningEffort` (17-18,
  validated 140-141); `codexRuntimeConformanceConfigDigest` keys on `options.model` (63-64);
  worker envelope whitelist (342); `startManager` requires `request.model === options.model`
  (300); every turn resumes/starts a thread and calls `startTurn` with `this.options.model`
  and `this.options.reasoningEffort` (448-450). The model is NOT baked into the native
  config/policy (no `model` in policy/config generators); it is a per-request wire field.
- `codex-session.ts:859` `model()` validator; `860-875` `select()` sends `model`;
  `887-921` `startTurn` sends `model` and `collaborationMode.settings.reasoning_effort`;
  guards `rejectPolicyOverride` (846-848, policy fields only) and `revalidateModelEffectV2`
  (850-858, account/host authority only).
- Login purpose evidence binds methods `["account/login/start","account/login/cancel",
  "account/read","model/list"]` in `runtime-conformance-v2-admission.ts:294`,
  `hosted-release-provisioner.ts:129`, `account-free-login-observation.ts:402`
  (`bounded-protocol-purpose` limb: methods + `modelExecution:false`). The v1 record
  (`codex-login.ts:74`) lacks `model/list` but the v1 path never calls the catalog
  (composition 517 uses `trusted.model!`).
- Status surface: `R/packages/contracts/src/delegated.ts:159-178` `HostedBootstrapStatus`
  is exact-key validated (`hostedRecord`) in four places: contracts validator, daemon
  `safeBootstrapStatus` (`runtime-daemon.ts:841-847`), `host-account-client.ts:131-156`,
  `client.ts:578-596`. Route `/v3/projects/:id/hosted-bootstrap/status` is proof-gated via
  `runHostedAccount(…,"status","runtime:read")` (`runtime-daemon.ts:389`) and signed with
  scope `account:read` (`host-account-protocol.ts:117`).
- `hosted-bootstrap.ts`: `ProjectBootstrap` (99-112) holds `selection`; `projection()`
  (219-222); `selection()` (224-228); `defaultSessionPolicy.resolve` returns
  `bootstrap.selection(projectId)` (458); `retireAdmission` (394-400) and `signOut`
  (313-345) clear `selection`.
- Session flow: `CreateSessionRequest` (`contracts/src/session.ts:44-57`) already has
  `engineSelection`, but `runtime-service.ts:143-166` requires it together with `role` and
  otherwise uses `defaultSessionPolicy`; `session-store.ts:62-95` persists `engineSelection`.
  `turn-coordinator.ts:153` `opts.model = request.opts?.model ?? session.engineSelection.model`;
  `delegated-engine-adapter.ts:53-54` rejects any `engineSelection.model`/`opts.model` that
  differs from the admitted `selection.model` (503) — today's no-substitution pin.
  `delegated-runtime.ts:391-393` attribution `actual` is per project; `403-405` builds the
  hosted envelope; `478` stamps `attribution: actual` on the terminal event.
  `runtime-service.ts:363` checks `session:init` `model === input.opts.model`; `440`
  rewrites `engineSelection` from `session:init`.
- App: hosted status reaches the renderer only through `useHostedBootstrapController`
  (`F/src/components/settings/hosted-bootstrap-controller.tsx:40`), instantiated once in
  `F/src/components/shell/shell-frame.tsx:401` and passed to `AccountRow`/`SettingsView`
  (414-415). `ChatPanel` is rendered prop-less in five shells (`loop-shell.tsx:47`,
  `loop-tertiary-shell.tsx:45`, `portal-loop-shell.tsx:50`, `app-shell.tsx:357`,
  `woven-dialogue-shell.tsx:571`). Context row: `chat-panel.tsx:1318-1330`. Draft snapshot:
  `F/src/lib/harness/chat-draft.ts:10-14` (`draft`, `attachments`, `methods`) keyed by
  `buildChatDraftStorageKey` (34-40); session creation `chat-panel.tsx:638-646`; turn
  `chat-panel.tsx:798-806` passes `opts: {...optsPayload, mode}`. The operator toolkit has a
  free-text `opts.model` (`operator-toolkit-panel.tsx:65-69`, `toolkit.ts:144-146`) that today
  is rejected by the adapter pin (503) — a stray second source of truth.
- Replay lens reads `engineSelection.model` (`F/src/lib/woven-dialogue/operator-projection.ts:140`)
  and renders it (`selected-session-replay-lens.tsx:272-277`).

## 1. Catalog: capture, retention, exposure

Capture (no new protocol traffic):
1. `codex-session.ts:673` — add `supportedReasoningEfforts: Object.freeze(efforts)` to the
   frozen entry and to the return type. Same request, same params, same page count.
2. `codex-login.ts` — add `resolveModelCatalog(): Promise<HostedModelCatalog>` built from the
   existing loop (272-297): `models` = all non-hidden entries `{model, isDefault,
   defaultReasoningEffort, supportedReasoningEfforts}` in catalog order, `default` = the unique
   non-hidden default. Keep `resolveDefaultModel()` as `(await resolveModelCatalog()).default`
   so `hosted-bootstrap.ts:69` and `tests/codex-login.test.ts:63-67` remain valid. The
   conflict/duplicate checks (280-281) must also compare `supportedReasoningEfforts`.
3. `hosted-bootstrap.ts:66-71` `TrustedHostedLoginCeremony.resolveModelCatalog?()`;
   composition adapter (343-348) exposes it; `establishAdmission` (516) prefers it, stores
   `context.catalog` (add to `CeremonyContext`, 361), keeps `selected = catalog.default`.
   `materializeAdmission` (627) returns `{ …, selection, catalog }`.

Retention: `ProjectBootstrap.catalog?: HostedModelCatalog` set at `hosted-bootstrap.ts:387`
next to `state.selection`, cleared at 395 (`retireAdmission`) and 330 (`signOut`). Add
`catalog(projectId)` beside `selection()` (224). Lifetime = admission lifetime, so a
sign-out/re-sign-in always replaces it and nothing survives across accounts.

Exposure — extend `HostedBootstrapStatus` (recommended over a new route):
```
models?: readonly { model: string; isDefault: boolean; defaultReasoningEffort: string;
                    supportedReasoningEfforts: readonly string[] }[];   // non-hidden only
selection?: { model: string; reasoningEffort: string };                // admitted default
```
Validator rules (`delegated.ts:168-178`): both keys present iff `admission === "ready"`;
1..64 entries; ids/efforts match the `codex-session.ts` regexes; exactly one `isDefault`;
each default effort ∈ its supported list; `selection` ∈ `models`. Update the four exact-key
validators together (contracts, `runtime-daemon.ts:842`, `host-account-client.ts:132`,
`client.ts:579`). Justification: the status route is already proof-gated, `account:read`
scoped, polled by the App controller (`hosted-bootstrap-controller.tsx:125-128`) and passed
through Electron IPC unchanged (`host-account-ipc.ts:106-117` forwards `status` verbatim;
`chirality-window.d.ts:18` types it as the contract). A new route would need a new
`HostAccountOperation`, the `ACCOUNT_ROUTE` regex (`host-account-protocol.ts:49`), signing
descriptor (108-123), IPC contract, preload, and client — more attack surface for the same
bytes. The payload carries only model ids and effort labels (no account data).

Evidence impact: the login transport still sends the same `model/list` requests; retaining
fields from responses already received changes no wire bytes, no method list, and no limb
fact (`account-free-login-observation.ts:402` records methods and `modelExecution:false`,
not response shapes). No conformance record or purpose-release record changes. The only
pinned expectation is `tests/codex-session.test.ts:167` (`toEqual` on the page shape).

## 2. Selection scope and flow

Scope: **per session**, fixed at creation (see §5 for why not per turn).

Request → record → worker:
1. `CreateSessionRequest` (+) `modelSelection?: { model: string; reasoningEffort: string }`.
   Do not reuse `engineSelection` from the App: it must be paired with `role`
   (`runtime-service.ts:144`) and bypasses the daemon policy.
2. `hosted-bootstrap.ts:458` `defaultSessionPolicy.resolve(request)` receives
   `modelSelection`, validates it against `state.catalog` (§3) and returns
   `{ role, engineSelection: {adapterId,providerId,model}, reasoningEffort }`.
   `runtime-service.ts:150-166` forwards `reasoningEffort` into `sessions.create`.
3. `RuntimeSessionRecord` (+) `reasoningEffort?: string` (optional, additive; **no schema
   bump** — v3 is already additive, `readCentral` 845-865 passes unknown fields through, and
   `EngineSelection` stays `{adapterId, providerId, model}` so `recordKey`/`toEqual`
   comparisons at `runtime-service.ts:227-229`, `delegated-engine-adapter.ts:53`, and
   `tests/hosted-bootstrap-integration.test.ts:101,228` are untouched). `session-store.ts:75-94`
   persists it; `runtime-service.ts:440` must carry `reasoningEffort` forward when it rewrites
   the record after boot.
4. `delegated-engine-adapter.ts`: options gain `catalog`; `validate()` (52-55) checks
   `session.engineSelection.model ∈ catalog`, `input.opts.model === session.engineSelection.model`,
   and `session.reasoningEffort ∈ supported(model)`; `startTurn` (147-158) adds
   `model: session.engineSelection.model, reasoningEffort: session.reasoningEffort` to the
   delegated turn request; `session:init` (168) yields the session's model, not
   `options.selection.model`.
5. `delegated-runtime.ts`: `DelegatedProjectBinding` (+) `catalog`; turn request (+)
   `model`, `reasoningEffort`; `actual` (391) becomes
   `{ ...binding.actual, model: request.model ?? binding.actual.model }` after checking the
   catalog; the hosted envelope (403-405) carries both fields.
6. `codex-supervisor.ts`: `CodexSupervisorOptions` (+) `modelCatalog` (validated at 140-141
   like `model`/`reasoningEffort`; `options.model`/`reasoningEffort` must be members).
   Envelope whitelist (342) (+) `"model"`, `"reasoningEffort"`; a new
   `assertCatalogChoice(model, effort)` runs before `acquireInternal` proceeds; lines 448-450
   use `request.model ?? this.options.model` and `request.reasoningEffort ??
   this.options.reasoningEffort` for `resumeThread`/`startThread`/`startTurn`.
   Composition passes `modelCatalog: context.catalog` in `admitHosted` (582).

Supervisor keyed by model — answer: **one supervisor, model per turn**. `options.model`
appears in `codexRuntimeConformanceConfigDigest` (63-64) and the composition
`configDigest` (518-522) as admission identity, and in the launcher binding key
(`codex-admitted-launcher.ts:72-78`), but never in the native policy or config. Each turn
launches a fresh admitted candidate (`launchAdmittedCandidate`, 283-293) whose
`thread/start`/`turn/start` carry `model` per request. So no per-model supervisor and no
re-admission is needed; `options.model` stays the admitted default. Do **not** change the
digest recipes in this tranche: the v1 conformance path compares `configDigest` byte-exact
(`runtime-conformance.ts:68`) against accepted records, and the v2 packaged path folds it into
launcher bindings and `conformanceActual` (supervisor 57-58); the catalog is bound instead by
the supervisor constructor check plus the App-facing status. Guards: `rejectPolicyOverride`
— intact (model/effort are not policy fields); `revalidateModelEffectV2` — intact (account
and host authority, called before every `turn/start`); `model()` (859) — intact;
`startManager` check (300) — **explicitly intact**: hosted managers keep the admitted default
model in the MVP (document as a known limitation). `defaultSessionPolicy` and the adapter
`validate()` are the new/updated guards.

## 3. Validation (no silent substitution)

Single validator `resolveHostedModelSelection(catalog, requested?)` in `hosted-bootstrap.ts`,
used by `defaultSessionPolicy.resolve` and reused by the adapter/supervisor checks:
- omitted → `{ model: catalog.default.model, reasoningEffort: catalog.default.defaultReasoningEffort }`;
- `model` not in the non-hidden catalog → `INVALID_REQUEST` 400, message
  `Model '<id>' is not in the authenticated Codex catalog`, `details: { reason:
  "MODEL_NOT_IN_CATALOG", model, available: [ids] }`;
- effort not in that model's list → 400 `Reasoning effort '<x>' is not supported by '<id>'`,
  `details: { reason: "REASONING_EFFORT_UNSUPPORTED", model, supported: [...] }`;
- `modelSelection` present with a partial object or extra keys → 400.
- catalog absent (admission not ready) → existing `ENGINE_UNAVAILABLE` 503 from `selection()`.
Stored session whose model left the catalog after re-sign-in: `runtime-service.bootSession`
(225-236) and the adapter `validate()` throw `ENGINE_UNAVAILABLE` 503 with
`details.reason = "MODEL_NOT_IN_CATALOG"`; the App maps it to "This chat used <model>, which
your Codex account no longer offers. Start a new chat." Nothing is rewritten. The supervisor
check is the last line: an envelope model/effort outside `modelCatalog` fails the acquire
before any provider request (`INVALID_REQUEST`, as at 342).

## 4. History

- v1 harness events: `contracts/src/events.ts:26-33` attribution (+) `reasoningEffort?: string`.
- v2 canonical events: `v2-events.ts` `EventAttributionV2` (+) optional `reasoningEffort`;
  `validateHarnessEventV2` exact-key check on attribution (line with
  `exact(value.attribution, ["adapterId","providerId","model"])`) must accept the optional
  key; `projectRuntimeEventV2` copies it. `delegated-runtime.ts:478` already stamps `actual`,
  so per-turn `actual` (§2.5) puts the chosen model and effort on every terminal event.
- Session record (`reasoningEffort`) + `engineSelection.model` are returned by
  `replaySession` (harness port `runtime-daemon-harness-port.ts:275-290`,
  `asLegacySession` must keep the field). `operator-projection.ts:140` reads
  `readString(source.reasoningEffort)`; `selected-session-replay-lens.tsx:272-277` gains a
  `Reasoning` row under `Model`; `projectionSignature` (92-110) includes it.
- The chat transcript shows the pair once per session in the existing context row (§5) and
  in the side panel via the lens; no per-message badge in the MVP.

## 5. App UI

Placement: `chat-panel.tsx:1323-1326`, after the Interaction mode `<select>`, two labelled
selects `Model` and `Reasoning` (same `chat-mode-selector` class, `aria-label`s "Model",
"Reasoning"). Plan Mode `<select>` and `operatorMode` untouched.

Source of truth: a `HostedBootstrapContext` (`F/src/lib/harness/hosted-bootstrap-context.tsx`)
provided by `shell-frame.tsx:401-415` around `children`, exposing the controller snapshot.
`useHostedBootstrap()` in `ChatPanel` derives `signedIn = ceremony==="signed-in" &&
admission==="ready"` and `catalog = status.models`. This avoids threading props through
five shells.

Behaviour:
- Signed out / catalog absent: both selects disabled, `title="Sign in to Codex to choose a
  model"`, showing placeholder options.
- Signed in, no active session: options from `catalog`; default = `status.selection`;
  changing the model resets effort to that model's `defaultReasoningEffort`; effort options =
  that model's `supportedReasoningEfforts`.
- Active session: selects show the session's `engineSelection.model`/`reasoningEffort` and are
  disabled with `title="Model and reasoning are fixed for this chat. Start a new chat to
  change them."` — fixed per session (recommended). Rationale: the session record is the one
  validated, persisted, replayable place for the choice; per-turn change would need
  event-level history, resume-with-different-model semantics (`previousTurnId` →
  `thread/resume`) that no native run has qualified, and a third UI state. Bounded MVP.
- Persistence: `ChatDraftSnapshot` (+) `model?: string`, `reasoningEffort?: string`
  (`chat-draft.ts:10-14`; sanitise with the same regexes; drop values not in the current
  catalog on load). Persisted with the draft under `draftStorageKey` (398-402); the effect at
  443-464 adds the two values to its dependency list.
- Submit: `createHarnessSession` (638-646) (+) `modelSelection` → `harness-client.ts` →
  `F/src/app/api/harness/session/create/route.ts:18-53` passthrough →
  `runtime-daemon-harness-port.ts:180-205` → `RuntimeClient.createSession`. Boot and turn
  omit `opts.model` (runtime defaults to the session's model, `turn-coordinator.ts:153`).
- Remove the free-text `opts.model` from the toolkit (`operator-toolkit-panel.tsx:65-69`,
  `toolkit.ts:138,144-146`, `ToolkitValues.model`) so there is one source of truth; keep
  `tools`/`maxTurns`.

## 6. Test plan

Runtime (`R/tests`):
- `codex-session.test.ts:154-168` — expect `supportedReasoningEfforts` in the page; add a
  page whose default effort is outside its list → `protocol("Unusable default model reasoning")`.
- `codex-login.test.ts:50-67` — `resolveModelCatalog` returns non-hidden entries with efforts,
  `default` matches `resolveDefaultModel`; conflicting effort lists across pages reject.
- `codex-supervisor.test.ts` — envelope with in-catalog `model`/`reasoningEffort` reaches
  `turn/start` params (`model`, `collaborationMode.settings.reasoning_effort`); out-of-catalog
  values reject before launch; `startManager` still requires the admitted model.
- `delegated-runtime.test.ts` — hosted envelope carries both fields; terminal event
  attribution has the per-turn model and effort; unknown model → 503 without envelope send.
- `hosted-bootstrap-integration.test.ts` — status carries `models`/`selection` only when
  `admission==="ready"`; `createSession` with valid `modelSelection` persists
  `engineSelection.model` + `reasoningEffort`; omitted → catalog default; invalid → 400 with
  `details.reason`; after `signOut` status has no catalog; a stored session with a removed
  model fails boot with `MODEL_NOT_IN_CATALOG`.
- `codex-primary-chat-integration.test.ts` — end-to-end: chosen model/effort observed in the
  fixture's `thread/start` and `turn/start` requests; default path unchanged.
- `hosted-private-composition.test.ts` — `materializeAdmission` returns the catalog;
  `configDigest` recipe unchanged (regression guard for §2).
- Contracts: `validateHostedBootstrapStatus` accepts/rejects the new keys per §1;
  `validateHarnessEventV2` accepts optional `reasoningEffort`.
App (`F/src/__tests__`):
- `lib/runtime-daemon-harness-port.test.ts` — `createSession` forwards `modelSelection`.
- `lib/harness-chat-draft.test.ts` — snapshot round-trips model/effort; corrupt values dropped.
- `lib/hosted-bootstrap-client.test.ts`, `electron/host-account-ipc.test.ts` — status with
  catalog passes through untouched.
- `lib/operator-projection.test.ts` — `reasoningEffort` projected.
- new `components/chat-panel-model-selectors.test.tsx` (pattern from
  `chat-panel-folder-binding.test.tsx`) — disabled+title when signed out; options from
  status; effort resets on model change; fixed for an active session; Plan Mode select
  unchanged; `createHarnessSession` called with `modelSelection`.
- `components/hosted-bootstrap.test.tsx` — settings rendering unaffected by extra keys.
Native run only (cannot be proven by fixtures): the packaged Codex `model/list` field names
and hidden semantics; that `turn/start` honours `reasoning_effort` per model (observe the
provider's reported effort); that a non-default model works under the same native policy;
App end-to-end sign-in → catalog → chat → replay.

## 7. Ordered steps, write scopes, sizes, risks

| # | Step | Write scope | Size |
|---|------|-------------|------|
| 1 | Contracts: status keys + validator; `CreateSessionRequest.modelSelection`; `RuntimeSessionRecord.reasoningEffort`; attribution `reasoningEffort` (v1 + v2) | `R/packages/contracts/src/{delegated,session,events,v2-events}.ts` | ~70 lines |
| 2 | Catalog capture/retention/exposure | `codex-session.ts:673`, `codex-login.ts:268-300`, `hosted-bootstrap.ts` (66-71, 99-112, 219-228, 387, 395, 330, 458), `hosted-private-composition.ts` (343-348, 361, 516-522, 582, 617-627), `runtime-daemon.ts:841`, `host-account-client.ts:131`, `client.ts:578` | ~130 lines |
| 3 | Session policy + validation + persistence | `hosted-bootstrap.ts:458` + `resolveHostedModelSelection`, `runtime-service.ts:143-200,440`, `session-store.ts:75-94` | ~70 lines |
| 4 | Turn path | `delegated-engine-adapter.ts:20-55,147-168`, `delegated-runtime.ts:28-42,391-405`, `codex-supervisor.ts:14-20,135-145,340-345,446-450` | ~90 lines |
| 5 | Runtime tests (§6) | `R/tests/*` listed | ~250 lines |
| 6 | App plumbing + UI | context provider, `shell-frame.tsx`, `chat-draft.ts`, `chat-panel.tsx` (300-302, 398-464, 638-646, 1323-1330), `harness-client.ts`, `create/route.ts`, `runtime-daemon-harness-port.ts`, `daemon-harness-port.ts`, `toolkit.ts`, `operator-toolkit-panel.tsx`, `operator-projection.ts`, `selected-session-replay-lens.tsx` | ~220 lines |
| 7 | App tests (§6) | `F/src/__tests__/*` listed | ~200 lines |
| 8 | Native run checklist + run evidence | `execution/_Coordination/AgentRuns/...` only | doc |

Steps 1-5 are one Runtime tranche (contracts first; 2-4 can be authored in parallel by
file); 6-7 the App tranche after the Runtime `dist` is rebuilt. Each step keeps CI green on
its own except step 1 + 2, which must land together (four exact-key validators).

Risks:
- Security: catalog exposure is model ids/effort labels only, over the proof-gated status
  route; the App never gains a route to the login transport. The App-supplied
  `engineSelection` path (`runtime-service.ts:143`) remains and is caught by the adapter
  catalog check; optionally reject explicit `engineSelection` for hosted projects (1 line in
  `defaultSessionPolicy`).
- Conformance evidence: unchanged as long as `configDigest`/launcher-binding recipes and the
  login method list are not touched (§1, §2). Any later `catalogDigest` addition re-issues
  accepted conformance records — schedule separately.
- CI: exact `toEqual` at `codex-session.test.ts:167`; four status validators; App
  `folder-preload.test.ts` unaffected (preload shape unchanged); removing the toolkit `model`
  field touches `harness-client.test.ts`/toolkit presets — search for `values.model` first.
- Product: managers (`startManager`) stay on the default model; state this in release notes.
