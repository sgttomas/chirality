# SETTINGS capability inventory — notes (R2 reverse pass, R1b)

Area: the 39 `Area=SETTINGS` rows of `R1_INVENTORY/IMPLEMENTATION_SURFACES.csv`:
`frontend/src/components/settings/**`, `frontend/src/lib/{consent,dependencies,lifecycle,runtime-client}/**`,
`frontend/src/lib/{atomic-write,credential-storage-state}.ts`, `frontend/src/types/chirality-window.d.ts`
and `frontend/packages/harness-contract/**`, read at frozen basis `00115c719`.
Output: `SETTINGS_capabilities.csv`, 42 rows (`CAP-SETTINGS-001`…`042`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders were read. Rows come from code, import greps, the evidence pack and test imports.

## 1. Census

`CENSUS rows=42 LIVE=39 LEGACY_ONLY=0 TEST_ONLY=3 UNREACHED=0 ENABLED=31 DISABLED=11`

- TEST_ONLY: the fake consent port (019), the consent UX fixtures (020), and the `@chirality/harness-contract` facade (042).
- DISABLED (11): local-model residency (008), the two API key rows (009, 010), the six consent-port rows (013–018), the env-configured single-project daemon port (028), and the no-op provider-network consent grant (039).
- Two LIVE rows name a secondary legacy consumer in `Notes` (`REACH=LEGACY_ONLY`): the register writer (022, legacy MCP tools) and the status parser (024, legacy `lib/harness/scaffold.ts`).

## 2. Granularity rationale

- The area is a grab-bag of five layers. Rows are grouped by the behaviour a deliverable could own, not by file:
  - **Settings UI** (001–012): the panel container; the hosted account under Codex credential custody (split into presentation, sign-in ceremony, sign-out, folder registration, and account persistence/refresh); Runtime service status; local models; API keys; the credential storage-state vocabulary; agent instructions.
  - **Consent** (013–020): `hosted-engine-consent-port.ts` is one contract file, but it carries four separable contract clauses: per-root login, consent scope/staleness, command-network posture, and role posture. Each is a row, plus one row for the snapshot status displays. The fake port and the fixtures are separate TEST_ONLY rows.
  - **Deliverable file contracts** (021–026): `Dependencies.csv` read, write and schema; `_STATUS.md` parse and transition; atomic write. `csv-utils.ts` folds into read and write.
  - **Runtime client** (027–040): the production port behind `/api/harness/**`. `runtime-daemon-harness-port.ts` (1141 lines) is split the way the HARNESS model split `client.ts`: session lifecycle, turns, server requests/permission, catalog, native plan, scaffold, authorization/error mapping, hosted binding, hosted account actions, consent no-op, and the two environment factories. The registry and the multi-folder routing in `daemon-harness-port.ts` are separate rows because they have different gates.
  - **Contracts** (041–042): the `window.chirality` ambient types and the deprecated facade.
- The 13 facade files are one row. They are identical one-line `export *` re-exports, and splitting them would only repeat the reach and state.

## 3. Files covered versus total

`COVERAGE covered=39 total=39`

- No file is uncovered.
- `settings-view.module.css` is folded into the Settings panel row (001), because `settings-view.tsx` imports it.
- `chirality-window.d.ts` has its own TYPE-ONLY row (041).
- `packages/harness-contract/package.json` is in the facade row (042).
- `PostReleaseBasis` is `NO` on every row:
  - `TOUCHED_PATHS.csv` has no path under `projects/chirality-app-dev/frontend/**`.
  - The only touched code on the Runtime client dependency path is `packages/client/src/client.ts` lines 50–54 and 363–383 (`da95ec194`), the application-tools methods.
  - `grep ApplicationTool` over the App `src/` and `electron/` finds no caller, so no SETTINGS capability relies on those lines.

## 4. Dead, unreached, disabled or retired code observed

- **Non-hosted Settings branches are retired presentation code.**
  - `AccountPresentation` in `shell-frame.tsx:376-404` always builds a hosted controller and passes it to `SettingsView`.
  - `settings-view.tsx:31-35` therefore never renders the non-hosted groups: the `AccountConsentSettingsView` account and folder groups, the local-model group, and the API-keys group.
  - The other mount of `RuntimeSettings`/`ApiKeySettings` is the default-variant "Runtime & credentials" disclosure (`shell-frame.tsx:299-304`). It is used only by the legacy loop shells, which `woven-dialogue-route.tsx` discards (see SHELL notes).
  - The hooks still run on every render: `useRuntimeSettingsController({localModels:false})` and `useAccountConsentController()`.
  - Side effect: `SettingsView` focus targets `folder` and `local-model` point at groups that are never rendered.
- **Consent port has no production adapter.**
  - `useAccountConsentController()` is called with a null port (`shell-frame.tsx:377`).
  - The only `HostedEngineConsentPort` implementation is `lib/consent/fake-hosted-engine-consent-port.ts`, imported only by tests. It ships under `src/lib`, not `__tests__`. The same holds for `consent-ux-fixtures.ts`.
- **Local-model bridge retired.** `chirality-window.d.ts:72-79` records that `runtime.models` is gone, and `electron/preload.ts` exposes no `models`. `useRuntimeSettingsController` with `localModels:true`, activation and `window.confirm` are unreachable in the product.
- **Provider-network consent is a no-op.** `RuntimeHostedBootstrapPort.grantProviderNetworkConsent` (`runtime-daemon-harness-port.ts:766-778`) only reads status, and no renderer or client module calls the route.
- **Env single-project daemon port is dormant in the desktop app.**
  - `createRuntimeDaemonHarnessPortFromEnvironment` requires `CHIRALITY_RUNTIME_PROJECT_ID=chirality-app-dev` and `_ROOT`.
  - `electron/main.ts:771-773` sets neither, and no `frontend/scripts` file does. `getDaemonHarnessPort()` therefore throws `ENGINE_UNAVAILABLE` until the hosted port installs a binding.
  - The `APP_DEV_PROJECT_ID` default and the "app-dev project" error texts are leftovers.
- **Dead export.** `writeStatusDocument` (`lib/lifecycle/status-writer.ts:89`) has no importer anywhere, tests included.
- **Test-only production helpers.** `installDaemonHarnessPort` and `resetDaemonHarnessPortForTests` have no production caller.
- **Routes with no rendered caller.** The dependency `PUT` and the status-transition `POST` routes are served, but their only renderer caller, `components/pipeline/pipeline-surface.tsx`, is not rendered. I tagged them ENABLED as endpoints.
- **Deprecated facade reach confirmed.** A frozen-tree search for `@chirality/harness-contract` found only:
  - its own `package.json`;
  - a `package-lock.json` workspace link;
  - the rollback test `src/__tests__/lib/harness-contract-rollback.test.ts`;
  - the guard script `scripts/assert-harness-contract-deps.mjs`, which fails if the dependency becomes load-bearing;
  - a comment in `scripts/generate-tool-catalog.mjs`, which imports `@chirality/runtime-contracts` directly;
  - docs.

  There is no production importer, which matches the pack's resolver.

## 5. Method friction with §5.2, with a proposed revision

- **Tests do not reach the real behaviour for disabled UI.** A `STATE=DISABLED` row with a non-empty `CoveringTests` can read as "tested and shipping". The consent and API-key tests mount the components directly or with a fake port.
  - Proposal: allow a `(bypasses-gate)` suffix in `CoveringTests`, like `(indirect)`, for tests that mount a component outside its production gate.
- **Reach of a served route versus a rendered caller.** §9 reach stops at API routes. Behaviour behind a served route with no rendered caller (022, 025) is `LIVE`/`ENABLED` by the rule, but it is dormant from the user's point of view.
  - Proposal: add an optional `CALLER=NONE_RENDERED` token in `Notes` for endpoint-only behaviour.
- **The `.d.ts` and `package.json` coverage rule is implicit.** The brief says the pack has no rows for them, but §5.2 does not say whether such files count toward "covered". I counted them, because the file list is authoritative.
  - Proposal: state that every file in the area list counts, whatever its extension.
- **Mixed-layer area.** The areas were cut by folder, and the area label "SETTINGS" understates the Runtime client (14 rows) and the deliverable file contracts (6 rows).
  - Proposal: a sub-area label, such as `SETTINGS/RUNTIME_CLIENT`, or a separate area for `lib/runtime-client`, so forward workers find the production port.

## 6. Effort

- Files read, partially or by grep: about 45. That is all 39 area files (the facade in full; large files in line ranges), plus `shell-frame.tsx`, `woven-dialogue-shell.tsx`, `electron/preload.ts`, `electron/main.ts` excerpts and route headers.
- The test map was computed with greps. The CSV was generated and checked with a scratchpad script.
- Context was comfortable, not tight.
