# F — Runtime model selection tranche (DESIGN.md §7 steps 1-5) — RETURN

Role: TASK. Worktree: `.claude/worktrees/owner-alignment-inspection-db4335`, branch
`claude/chirality-v3-mvp-trial-ab05cb`. `R` = `projects/chirality-runtime`. Nothing committed,
stashed, installed or packaged. No file outside `R/packages/{contracts,core,daemon,client}/src`
and `R/tests` was modified except this RETURN. `R/tests/attachment-content-path.test.ts` untouched.

## 1. Contract additions the App tranche must consume

All exported from `@chirality/runtime-contracts` (`R/packages/contracts/src/delegated.ts`,
`session.ts`, `events.ts`, `v2-events.ts`); `dist` rebuilt (see §5).

```ts
// delegated.ts
export interface HostedModelCatalogEntry { model: string; isDefault: boolean; defaultReasoningEffort: string; supportedReasoningEfforts: readonly string[] }
export interface HostedModelCatalog { models: readonly HostedModelCatalogEntry[]; default: HostedModelCatalogEntry }
export interface HostedModelSelection { model: string; reasoningEffort: string }
export const HOSTED_MODEL_ID_PATTERN = /^[\x21-\x7e]{1,128}$/;
export const HOSTED_REASONING_EFFORT_PATTERN = /^[\x21-\x7e]{1,64}$/;
export function validateHostedModelCatalogEntries(value: unknown): readonly HostedModelCatalogEntry[];
export function hostedModelCatalog(models: readonly HostedModelCatalogEntry[]): HostedModelCatalog;
export function resolveHostedModelSelection(catalog: HostedModelCatalog, requested?: unknown): HostedModelSelection;

export interface HostedBootstrapStatus {
  schema: "chirality-hosted-bootstrap-status/v1"; projectId: string; ceremony: ...; admission: ...; canStartLogin: boolean;
  models?: readonly HostedModelCatalogEntry[];   // NEW — non-hidden catalog, catalog order
  selection?: HostedModelSelection;              // NEW — admitted default model + its default effort
}
// validateHostedBootstrapStatus: `models`/`selection` allowed only together and only when admission === "ready";
// 1..64 entries, exactly one isDefault, each defaultReasoningEffort ∈ its supportedReasoningEfforts (1..32, unique),
// ids/efforts match the patterns above, selection.model ∈ models and its effort ∈ that model's list.

export interface DelegatedTurnRequest { ...; model?: string; reasoningEffort?: string }   // NEW (Runtime-internal delegated path)

// session.ts
export interface CreateSessionRequest { ...; modelSelection?: { model: string; reasoningEffort: string } }  // NEW
export interface RuntimeSessionRecord  { ...; reasoningEffort?: string }                                    // NEW, additive, no schema bump

// events.ts   RuntimeEvent.attribution (+) reasoningEffort?: string
// v2-events.ts EventAttributionV2 { adapterId; providerId; model; reasoningEffort?: string }
//   validateHarnessEventV2 accepts the optional key (non-empty string); projectRuntimeEventV2 copies it.
```

Error codes / `details.reason` strings (HTTP status in parentheses):

| Where | code (status) | `details.reason` | other `details` |
|---|---|---|---|
| `POST /v3/projects/:id/sessions` with `modelSelection` naming an unknown model | `INVALID_REQUEST` (400), message `Model '<id>' is not in the authenticated Codex catalog` | `MODEL_NOT_IN_CATALOG` | `model`, `available: string[]` |
| … with an effort the model does not support | `INVALID_REQUEST` (400), message `Reasoning effort '<x>' is not supported by '<id>'` | `REASONING_EFFORT_UNSUPPORTED` | `model`, `supported: string[]` |
| … partial object, extra keys, bad charset, or combined with explicit `engineSelection` | `INVALID_REQUEST` (400) | `MODEL_SELECTION_INVALID` | — |
| … project whose session policy has no catalog (v1 managed-auth / standalone) and cannot honour it | `INVALID_REQUEST` (400) | `MODEL_SELECTION_UNSUPPORTED` | `model`, `reasoningEffort` |
| … admission not ready | `ENGINE_UNAVAILABLE` (503) (existing `selection()` error) | — | — |
| `POST .../sessions/:sid/boot` or turn for a stored session whose model left the catalog | `ENGINE_UNAVAILABLE` (503), message `Model '<id>' is no longer offered by the authenticated Codex catalog` | `MODEL_NOT_IN_CATALOG` | `model`, `available` |
| … stored effort no longer supported | `ENGINE_UNAVAILABLE` (503) | `REASONING_EFFORT_UNSUPPORTED` | `model`, `supported` |
| turn with `opts.model` differing from the session's fixed model | `ENGINE_UNAVAILABLE` (503) | `MODEL_SELECTION_MISMATCH` | `model`, `sessionModel` |

On the turn SSE stream these arrive as `turn:error` with `data.details = { runtimeCode: "ENGINE_UNAVAILABLE", reason }`
(the `reason` field on `turn:error.details` is new — `R/packages/core/src/turn-coordinator.ts`). On the boot route the
`RuntimeError` is returned directly with `code`, `status`, `details`.

App mapping per DESIGN §3: `MODEL_NOT_IN_CATALOG` on boot/turn → "This chat used <model>, which your Codex account no
longer offers. Start a new chat." Nothing is rewritten; `GET session` still returns the stored `engineSelection.model`
and `reasoningEffort`.

Session flow for the App: create with `modelSelection` (or omit it for the admitted default), read back
`session.engineSelection.model` + `session.reasoningEffort`; boot and turn must omit `opts.model` (the runtime defaults
to the session's model). Replay (`GET session`, `replaySession`) carries `reasoningEffort` on the record; delegated
terminal events carry `attribution.reasoningEffort`.

## 2. Files changed (all under `R`)

Contracts: `packages/contracts/src/delegated.ts`, `session.ts`, `events.ts`, `v2-events.ts`.
Core: `packages/core/src/runtime-service.ts` (modelSelection validation, policy forwarding, no-silent-fallback guard,
`reasoningEffort` into `sessions.create`), `session-store.ts` (persists `reasoningEffort`), `delegated-engine-adapter.ts`
(`catalog` option; `validate()` catalog/effort checks; turn request carries `model`/`reasoningEffort`; `session:init`
yields the session's model), `delegated-runtime.ts` (`DelegatedProjectBinding.catalog`; `resolveTurnAttribution`;
envelope carries both fields; per-turn `actual` on the terminal event), `turn-coordinator.ts` (`details.reason` on
`turn:error`).
Daemon: `codex-session.ts` (retains `supportedReasoningEfforts`), `codex-login.ts` (`resolveModelCatalog()`;
`resolveDefaultModel()` now derives from it; conflict check includes effort lists), `hosted-bootstrap.ts`
(`resolveModelCatalog?` on the ceremony; `ProjectBootstrap.catalog` set at admission, cleared on retire/sign-out;
`catalog(projectId)`; status projection; adapter gets the catalog; `defaultSessionPolicy.resolve` uses
`resolveHostedModelSelection`), `hosted-private-composition.ts` (production adapter exposes `resolveModelCatalog`;
`CeremonyContext.catalog`; `establishAdmission` prefers the catalog and keeps `selected = catalog.default`;
`admitHosted` gets `modelCatalog`; `materializeAdmission` returns `catalog` and binds it plus the default
`reasoningEffort` into `actual`), `codex-supervisor.ts` (`modelCatalog` option validated in the constructor against
`model`/`reasoningEffort`; envelope whitelist + `assertCatalogChoice` before any launch; `thread/start`, `thread/resume`,
`turn/start` use the envelope choice or the admitted pair; `controlledForTests` accepts `reasoningEffort`/`modelCatalog`).
Client: no change needed (see deviation 1).
Tests: `tests/codex-session.test.ts`, `codex-login.test.ts`, `codex-supervisor.test.ts`, `delegated-runtime.test.ts`,
`hosted-bootstrap-integration.test.ts`, `codex-primary-chat-integration.test.ts`, `hosted-private-composition.test.ts`,
`d36-v2-connected.test.ts`, `v2-contracts.test.ts`, new `hosted-model-selection-contracts.test.ts`.
`git diff --stat`: 23 files, +651 / −60.

Explicit constraints honoured: `configDigest` (`chirality.hosted-private-config/v1|v2`) and launcher-binding recipes
unchanged (byte-exact guards in tests, §4); `codexRuntimeConformanceConfigDigest` unchanged; login method list and
purpose-release/conformance records untouched (`model/list` is sent with the same params and page count; only fields of
already-received responses are retained — proven by the `listCalls` assertion in `codex-login.test.ts`);
`startManager` still requires `request.model === options.model` (tested); `EngineSelection` shape unchanged;
`RuntimeSessionRecord.reasoningEffort` additive with no schema bump.

## 3. Deviations from DESIGN.md (and why)

1. **"Four exact-key validators" are one function.** `runtime-daemon.ts safeBootstrapStatus`,
   `host-account-client.ts:132` and `client.ts:579` all call `validateHostedBootstrapStatus` from contracts; none has
   its own key list. Updating the contracts validator updates all four consistently; no code change was needed in the
   other three. (Design §0/§1 fact was inexact.)
2. **`resolveHostedModelSelection` lives in contracts, not `hosted-bootstrap.ts`.** The adapter (core) and the supervisor
   (daemon) also need it and core cannot import daemon. `hosted-bootstrap.ts` imports and uses it as designed.
3. **Status keys are "present only when ready and a catalog was retained", not "present iff ready".** The v1
   managed-auth composition path (`trusted.model!`, `defaultReasoningEffort: ""`) and controlled test fixtures whose
   `materializeAdmission` returns no catalog have no effort labels to expose, so a strict iff would break those paths
   with no honest value to publish. On the MVP v2 path the catalog is always present. The validator still rejects the
   keys outside `admission === "ready"` and rejects one without the other. `materializeAdmission` result gained an
   optional `catalog`.
4. **Extra guard: `MODEL_SELECTION_UNSUPPORTED`.** A session policy that ignores `modelSelection` (v1/standalone
   compositions) would otherwise silently create the default session; `RuntimeService.createSession` now compares the
   resolved pair with the request and rejects on mismatch. Likewise `modelSelection` with an explicit
   `engineSelection`+`role` is rejected (design left this optional).
5. **`turn:error.details.reason` added** (turn-coordinator) so the App can map `MODEL_NOT_IN_CATALOG` on the turn
   stream without parsing the message; the boot route already returned `details`.
6. **Envelope shortcut:** the raw-prompt shortcut for controlled-worker chat turns is taken only when no model/effort
   is requested; the adapter always sends the session's model, so adapter-driven controlled-worker turns now use the
   JSON envelope. No existing test depended on the raw form through the adapter.
7. **Per-turn attribution** also carries the admitted default `reasoningEffort` (from the v2 admission) when the turn
   did not choose, and a model-only request resolves the effort to that model's `defaultReasoningEffort` in the supervisor
   and in `resolveTurnAttribution` (the session path always sends both, so this only matters for direct delegated use).
8. The e2e case is a second `it` in `codex-primary-chat-integration.test.ts` that runs through
   `startControlledHostedBootstrapRuntimeHostForTests` (the MVP bootstrap composition) rather than the standalone
   `hosted.json` path, because only the bootstrap path has a catalog-bearing session policy. The original standalone case
   is unchanged and still passes (default path unchanged).
9. The v2 `configDigest` regression guard is in `d36-v2-connected.test.ts` (the only test that exercises the v2 recipe);
   `hosted-private-composition.test.ts` guards the v1 recipe and that v1 never reads the catalog.

## 4. Tests (DESIGN §6 Runtime) — commands and results

All from `R` with `export PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin`.

- `npm run typecheck` (`tsc -b --pretty false`): passes (no output), run after every source change.
- `node node_modules/vitest/vitest.mjs run` — full suite, run 1 (after all source changes, before the
  `MODEL_SELECTION_MISMATCH` rename): **Test Files 81 passed | 1 skipped (82); Tests 1073 passed | 14 skipped (1087)**,
  duration 22.32s.
- Full suite, run 2 (final bytes, after `npm run build`): Test Files 1 failed | 80 passed | 1 skipped; Tests 1 failed |
  1072 passed | 14 skipped. The single failure is `tests/hosted-private-composition.test.ts > connects public bootstrap
  through real same-actor admission to retained and fresh controlled candidates` — `Error: Test timed out in 5000ms`
  (ran 5888ms under full-suite load). **Pre-existing and load-sensitive:** the same test failed in the baseline full run
  taken before any edit (`ENOTEMPTY: directory not empty, rmdir '/private/tmp/hcp-…/Resources/instruction-root/workflows'`,
  5691ms), passed in full-suite run 1, and passes 3/3 when the file is run alone
  (`node node_modules/vitest/vitest.mjs run tests/hosted-private-composition.test.ts` → 10 passed, ×3). It spawns real
  child processes with a fixed 5s timeout; my changes do not touch its path beyond the catalog-absent assertions in the
  v1 fixture, which pass.
- Targeted files (final bytes, all green):
  `tests/codex-session.test.ts` 80 passed (page shape now includes `supportedReasoningEfforts`; new case: default effort
  outside the list → `Unusable default model reasoning`);
  `tests/codex-login.test.ts` 12 passed (`resolveModelCatalog` returns non-hidden entries with efforts in catalog order,
  hidden entry absent, `default` equals `resolveDefaultModel`, same two `model/list` requests, conflicting effort lists
  across pages reject);
  `tests/codex-supervisor.test.ts` 35 passed (in-catalog envelope reaches `thread/start.model` and
  `turn/start.model` + `collaborationMode.settings.reasoning_effort`; default pair; model-only → model's default effort;
  out-of-catalog model/effort and bad charset reject before launch (launch count 0); `startManager` with a non-admitted
  in-catalog model rejects; no-catalog supervisor rejects any other model/effort; constructor rejects an admitted
  model/effort outside `modelCatalog`);
  `tests/delegated-runtime.test.ts` 46 passed (envelope carries both fields; terminal `attribution` and
  `roleEvidence.actual` carry the per-turn model/effort and pass `validateHarnessEventV2`; unknown model → 503
  `MODEL_NOT_IN_CATALOG` with `available`, effort → `REASONING_EFFORT_UNSUPPORTED`, with no `acquire` and no retirement
  record; no-catalog binding rejects a different model);
  `tests/hosted-bootstrap-integration.test.ts` 6 passed (status `toEqual` with `models`/`selection` only when ready;
  createSession valid → persisted `engineSelection.model` + `reasoningEffort` (also in the on-disk record); omitted →
  catalog default; unknown model / unsupported effort / partial / extra key / combined with `engineSelection` → 400 with
  the reasons above; turn carries the pair and `session:init.model`; client `opts.model` override → 503
  `MODEL_SELECTION_MISMATCH`; after `signOut` no catalog keys; re-sign-in with a reduced catalog → boot of the stored
  session rejects 503 `MODEL_NOT_IN_CATALOG` `{ model: "gpt-alt", available: ["gpt-default"] }`, turn stream shows the
  same reason, record unchanged, default session still runs);
  `tests/codex-primary-chat-integration.test.ts` 2 passed (end-to-end client → daemon → policy → adapter → DelegatedRuntime
  → supervisor server → controlled `CodexSupervisor` with `modelCatalog`: `thread/start.params.model === "gpt-alt"`,
  `turn/start.params.model === "gpt-alt"`, `collaborationMode.settings.reasoning_effort === "low"`, provider text echoes
  the pair; default session → `gpt-default`/`high`; out-of-catalog createSession → 400 `MODEL_NOT_IN_CATALOG`; record
  and replay carry the choice);
  `tests/hosted-private-composition.test.ts` 10 passed (v1: `materialized.catalog` undefined, ceremony catalog never read,
  `admitHosted` gets no `modelCatalog`, launcher/admit `configDigest` byte-equal to the v1 recipe recomputed in the test);
  `tests/d36-v2-connected.test.ts` 32 passed (v2: `materialized.catalog` equals the Supplier-shaped catalog;
  launcher-binding `configDigest` byte-equal to the `chirality.hosted-private-config/v2` recipe recomputed in the test
  with no catalog term; worker `turn/start` still `model: gpt-default`, `reasoning_effort: high`);
  `tests/v2-contracts.test.ts` 17 passed (optional `reasoningEffort` accepted, empty/undefined/other extension rejected,
  projection copies it);
  new `tests/hosted-model-selection-contracts.test.ts` 4 passed (`validateHostedBootstrapStatus` accept/reject per §1;
  `resolveHostedModelSelection` default/valid/`MODEL_NOT_IN_CATALOG`/`REASONING_EFFORT_UNSUPPORTED`/`MODEL_SELECTION_INVALID`).

## 5. Build

`npm run build` (`tsc -b`) run once in `R` at 2026-09-11 03:53:07 UTC, after all source edits, before the final full
suite; `dist` for contracts/core/daemon/client is current with the source above (`grep reasoningEffort` hits in
`packages/contracts/dist/delegated.js` and `packages/daemon/dist/hosted-bootstrap.js`). Note that `npm run typecheck` is
also `tsc -b` and emits; it was run after each change, so `dist` never lagged the source during testing.

## 6. Risks and what only a native run can prove

- Native-only (per DESIGN §6): packaged Codex `model/list` field names and `hidden` semantics; that `turn/start` honours
  `reasoning_effort` per model; that a non-default model works under the same native policy (the model is a per-request
  wire field, not part of the native policy/config); App end-to-end sign-in → catalog → chat → replay.
- The App's `hosted-bootstrap-client`/IPC validate status through the contracts validator from `dist`; frontend tests
  that `toEqual` a status object will need the App tranche (step 6-7) to account for `models`/`selection` when ready.
- The v1 managed-auth path and the standalone `hosted.json` path expose no catalog; a `modelSelection` there is rejected
  (`MODEL_SELECTION_UNSUPPORTED`), never silently defaulted. Managers (`startManager`) stay on the admitted default
  model (known MVP limitation, unchanged).
- Sessions created through the explicit `engineSelection`+`role` path with a hosted project are now checked against the
  catalog by the adapter (`MODEL_NOT_IN_CATALOG`) rather than only against the admitted default.
- Pre-existing load-sensitive test noted in §4 (5s timeout under full-suite load); unrelated to this change.
