# PREGATHER — DEL-02-05 API Key UI and Runtime Feedback

- **Deliverable:** DEL-02-05 (PKG-02), folder `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/`
- **Basis:** frozen tree at `00115c719` (read-only). Run RUN_D128_CONCORDANCE_2026-09-21_1614Z, R2 pre-gather (TASK, Type 2).
- **Nature:** evidence locations only. No dispositions, alignment judgments or CauseTags.
- **Counts:** 32 indexed units (3 SEC, 28 CLM, 1 REM). 13 units are `NO_CANDIDATES` for code; several of them still point to evidence-pack hash facts. HINTS file: 725 data rows. Top hint paths: `frontend/scripts/harness-section9-manifest.json` (147, token noise), `account-consent-settings-states.test.ts` (59), `electron/api-key-ipc.ts` (59), `electron/api-key-storage.ts` (57), `deliverables-route.test.ts` (44, token noise on `_CONTEXT.md` etc.).
- **Method (searches run):**
  - grep of CLAIM_INDEX for the deliverable's rows;
  - python summary of HINTS by ClaimKey, Token and HitPath;
  - evidence pack: REACHABILITY rows for consent, api-key, settings, account, error-display, chat-draft, attachment, preload, hosted-bootstrap, codex-login and credential; TOUCHED_PATHS for the same stems (no frontend path is touched; only runtime `app-owned-composition.ts` and `runtime-daemon.ts` have touched ranges); DECISION_HITS; D-APP-127 application map; REFERENCE_HASHES;
  - frontend greps, all scoped to `src` and `electron`: `ApiKeySettings`, `AccountConsentSettings`, `HostedEngineConsentPort`, `SettingsView`, `useAccountConsentController`, `useHostedBootstrapController`, `ShellFrame`, `AccountRow`, `SafeStorageCredentialStore`, `getProviderApiKey|getUiApiKey|hasUiApiKey`, `HarnessErrorType`, `toHarnessUiError`, `turn:error|process:exit`, `redact`, `Opt-in Preview|role not mechanically enforced|network_access`, `HELP_HUMAN|WORKING_ITEMS`;
  - runtime greps, scoped to `packages/*/src` and `tests/`: `credentials`, `new RuntimeService`, `CodexLogin`, `account/login/start|cancel|logout`, `grantProviderNetworkConsent`, `turn:error`, `redact`;
  - entry tracing from `frontend/src/app/{page,chat/page,pipeline/page,workbench/page,not-found}.tsx`;
  - test case names read by grep of `it(`/`test(` lines.
- **Reach method:** `REACH=` is copied from `REACHABILITY.csv`. `SYMBOL-REACH:` records a static trace from product entries. The notes are facts, not verdicts.

## Candidate registry (referenced by ID in the unit sections)

In the unit sections below, "(C3)" means "see candidate C3 here". All paths are repo-relative.

**Live entry spine (fact).** `frontend/src/app/page.tsx`, `chat/page.tsx`, `pipeline/page.tsx` and `workbench/page.tsx` render `WovenDialogueRoute`. Each passes the legacy shell (`PortalLoopShell`, `LoopShell` or `LoopTertiaryShell`) as the `legacy` prop, which `woven-dialogue-route.tsx:18` voids (`void legacy`). So those legacy shells are imported, which makes them LIVE in the map, but they are not rendered. `WovenDialogueShell` renders `ShellFrame variant="workspace"` with `renderWorkspaceContent` (`woven-dialogue-shell.tsx:812-821`). That leads to `AccountPresentation` (`shell-frame.tsx:373-405`), which constructs:
- `useAccountConsentController()` with **no port** (`shell-frame.tsx:377`);
- `useHostedBootstrapController(folder, …)` (`shell-frame.tsx:379`), which always returns a non-null object (`hosted-bootstrap-controller.tsx:105,335`).

`AccountPresentation` passes `hosted` to both `AccountRow` and `SettingsView` (`shell-frame.tsx:404-405`). The only rendered path to the default (non-workspace) `ShellFrame` is `frontend/src/app/not-found.tsx` > `AppShell` (`app-shell.tsx:316`).

- **C1** — `projects/chirality-app-dev/frontend/src/components/settings/api-key-settings.tsx`:
  - symbols: `:83 ApiKeySettings`, `:237 resolveStorageState` (non-answer becomes `unknown`), `:272 ApiKeySettingsView`, `:316 storageUnavailable warning`, `:325 decryptFailed warning`, `:370 remove control`;
  - REACH=LIVE;
  - SYMBOL-REACH: rendered only via `app/not-found.tsx > AppShell > ShellFrame(default) "Runtime & credentials" disclosure` (`shell-frame.tsx:297-302`). On the woven live path `SettingsView` renders it only when `!hosted` (`settings-view.tsx:35`), and `hosted` is always non-null there, so it is not rendered. The test `settings-view-codex.test.tsx:13` asserts that hosted Codex "omits API-key and local-model panels".
- **C2** — `projects/chirality-app-dev/frontend/src/components/settings/settings-view.tsx`:
  - symbols: `:18 SettingsView`, `:31` (`hosted ? HostedBootstrapView : AccountConsentSettingsView`), `:32` (folder group, `!hosted`), `:33` (`RuntimeStatus`, hosted), `:34` (local-model group, `!hosted`), `:35` (API keys, `!hosted`);
  - REACH=LIVE;
  - SYMBOL-REACH: rendered from `app/page.tsx > WovenDialogueRoute > WovenDialogueShell > ShellFrame(workspace) > AccountPresentation` (`shell-frame.tsx:405`) `> RightPanel settingsView` (`woven-dialogue-shell.tsx:997`).
- **C3** — `projects/chirality-app-dev/frontend/src/components/settings/account-consent-settings.tsx`:
  - symbols: `:46 useAccountConsentController`, `:90 AccountConsentSettings`, `:169 AccountConsentSettingsView`, `:192-196 Opt-in Preview label`, `:200-231 per-root login / CODEX_HOME / ambient ~/.codex explanation`, `:239 not-connected copy`, `:249-258 sign in/out`, `:293 revoke`, `:328,346 network_access = true label`, `:363-365 queued-request caveat`, `:419-440 role not mechanically enforced`;
  - REACH=LIVE;
  - SYMBOL-REACH: the controller is constructed with no port (`shell-frame.tsx:377`), which gives the not-connected state. The View renders only in `!hosted` branches (`settings-view.tsx:31-32`; `account-popover.tsx:29`), and `hosted` is non-null on the live path, so the View is not rendered there (static reading; searched `AccountConsentSettingsView|AccountConsentSettings` in `src`).
- **C4** — `projects/chirality-app-dev/frontend/src/lib/consent/hosted-engine-consent-port.ts`:
  - symbols: `:42 PRODUCT_POSTURE_LABEL`, `:48 COMMAND_NETWORK_POSTURES`, `:53 DEFAULT_COMMAND_NETWORK_POSTURE='off'`, `:56 COMMAND_NETWORK_ON_CONFIG_LABEL`, `:95 NETWORK_PROMPT_DECISIONS` (incl. `acceptForSession`), `:167 ambientCodexRead:false`, `:188 ROLE_NOT_MECHANICALLY_ENFORCED_LABEL`, `:345 type HostedEngineConsentPort`;
  - REACH=LIVE;
  - SYMBOL-REACH: module LIVE via type/constant imports (C3; `account-settings-controls.tsx:6 describeAccountIdentity`). The only port implementation found is the fake (C5); searched `HostedEngineConsentPort` in `src` and `electron`, with no non-fake implementation.
- **C5** — `projects/chirality-app-dev/frontend/src/lib/consent/fake-hosted-engine-consent-port.ts:118 createFakeHostedEngineConsentPort` and `projects/chirality-app-dev/frontend/src/lib/consent/consent-ux-fixtures.ts`. REACH=TEST_ONLY (both).
- **C6** — `projects/chirality-app-dev/frontend/src/components/settings/hosted-bootstrap-view.tsx`:
  - symbols: `:125 HostedBootstrapView`, `:115-116 sign-in explanation` ("Codex keeps the credentials"), `:149 Cancel`, `:152 Sign out`, `:156 Sign in with your ChatGPT account`;
  - REACH=LIVE;
  - SYMBOL-REACH: rendered from `SettingsView` hosted branch (`settings-view.tsx:31`) and `AccountPopover` (`account-popover.tsx:29`) via `AccountRow` (`shell-frame.tsx:404`; woven `footerSlot` at `woven-dialogue-shell.tsx:895`).
- **C7** — `projects/chirality-app-dev/frontend/src/components/settings/hosted-bootstrap-controller.tsx:105 useHostedBootstrapController`, `:335` returned controller (`onStartLogin`/`onCancelLogin`/`onSignOut`). REACH=LIVE. SYMBOL-REACH: constructed at `shell-frame.tsx:379`.
- **C8** — `projects/chirality-app-dev/frontend/src/lib/harness/hosted-bootstrap-client.ts`:
  - symbols: `:142 startHostedBootstrapLogin`, `:150 cancelHostedBootstrapLogin`, `:158 signOutHostedBootstrapProject`;
  - routes `projects/chirality-app-dev/frontend/src/app/api/harness/hosted-bootstrap/{login/start,login/cancel,logout,status,provider-network-consent}/route.ts`, which reach `lib/runtime-client/daemon-harness-port.ts`;
  - REACH=LIVE (the routes are product entries);
  - SYMBOL-REACH: called from C7. Transport fact: the renderer reaches the daemon through Next API routes, not through Electron main IPC.
- **C9** — Runtime login (REACH=LIVE for all files below):
  - `projects/chirality-runtime/packages/daemon/src/codex-login.ts`: `:30 CodexLogin`, `:57 startLogin` (`account/login/start` `:59`), `:67 cancelLogin` (`account/login/cancel` `:70`), `signOut` (`account/logout` `:76`).
  - `projects/chirality-runtime/packages/daemon/src/hosted-bootstrap.ts`: `:21 HostedBootstrapController`, `:56 grantProviderNetworkConsent` (returns status unchanged; comment "not a runtime decision in the App-owned composition"), `:59/:64/:69 startLogin/cancelLogin/signOut`.
  - `projects/chirality-runtime/packages/daemon/src/runtime-daemon.ts:440-465`: hosted-bootstrap routes under `credentials:write`. Not in a touched range; the touched ranges are 15-16, 57, 169-171 and 660-686.
  - `projects/chirality-runtime/packages/daemon/src/codex-effective-home.ts`: `:33 isExcludedCodexHomeEntry` (`auth.json`, `auth*`), `:41 prepareCodexEffectiveHome`.
  - `projects/chirality-runtime/packages/daemon/src/codex-app-server-client.ts`: `:41 CODEX_APP_SERVER_ARGUMENTS` (`cli_auth_credentials_store="file"`), `:44 redactAccountText`.
- **C10** — `projects/chirality-app-dev/frontend/electron/api-key-ipc.ts`:
  - symbols: `:10-16 channels`, `:23 ApiKeyStatusResult` (`source: 'ui'|'env'|'none'`), `:99 unavailableStatusResult`, `:109 parseCredentialStatus` (requires `source`; checks `source==='ui'` ⇔ `storage==='available'`), `:154 invalidStatusResult`, `:185 registerApiKeyHandlers` (sender check `:194`);
  - REACH=LIVE;
  - SYMBOL-REACH: registered from `electron/main.ts:990` with `runtimeClient`.
- **C11** — `projects/chirality-app-dev/frontend/electron/api-key-storage.ts`:
  - symbols: `:30 'api-key.enc'`, `:50 path userData/credentials/…`, `:75 storeProviderApiKey` (`isEncryptionAvailable` `:79`), `:112 readProviderCredential` (typed states), `:226 SafeStorageCredentialStore` (precedence ui → `ANTHROPIC_API_KEY` → `CHIRALITY_ANTHROPIC_API_KEY` at `:236-251`);
  - REACH=LIVE;
  - SYMBOL-REACH: the module is LIVE because `api-key-ipc.ts:2` imports `isProviderCredentialId`. No non-test construction of `SafeStorageCredentialStore` was found (searched the frontend excluding `node_modules` and `__tests__`, and the runtime `packages/*/src`).
- **C12** — `projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts`:
  - symbols: `:225 credentials` stub (`get` → undefined; `status` → `{configured:false}` with no `source`; `set`/`remove` = `offline`), `:180 offline` (throws `ENGINE_UNAVAILABLE`), `:226 new RuntimeService(…, credentials, …)`;
  - `projects/chirality-runtime/packages/daemon/src/runtime-daemon.ts:515-535 /v1/credentials/:id` GET/PUT/DELETE;
  - REACH=LIVE;
  - `app-owned-composition.ts` lines 225-226 are not in a touched range; the adjacent line 228 is TOUCHED(da95ec194);
  - static fact: C10 `parseCredentialStatus` returns null when `source` is absent (`:120-124`), which leads to `invalidStatusResult`. Not executed.
- **C13** — `projects/chirality-app-dev/frontend/electron/preload.ts`: `:33 exposeInMainWorld('chirality')`, `:65 attachments`, `:81 apiKey`, `:86 providerApiKey`. REACH=LIVE.
- **C14** — `projects/chirality-app-dev/frontend/src/lib/harness/error-display.ts`:
  - symbols: `:2` imports `HarnessErrorType` from `@chirality/runtime-contracts/types`, `:4 HarnessUiError {title, …, nextStep}`, `:11 ERROR_COPY`, `:175 modelNotInCatalogUiError`, `:199 toHarnessUiError`;
  - REACH=LIVE;
  - SYMBOL-REACH: called at `chat-panel.tsx:1217,1305,1606`; `ChatPanel` is rendered at `woven-dialogue-shell.tsx:855`.
- **C15** — Error taxonomy:
  - `projects/chirality-runtime/packages/contracts/src/harness/types.ts:3 HarnessErrorType` (REACH=LIVE);
  - `projects/chirality-runtime/packages/contracts/src/harness/errors.ts:17 HARNESS_ERROR_TYPES` (REACH=LIVE);
  - `projects/chirality-app-dev/frontend/packages/harness-contract/src/{types,errors}.ts` (REACH=NOT_IN_MAP; its `package.json` describes it as a "Deprecated compatibility facade" over `@chirality/runtime-contracts`);
  - `projects/chirality-app-dev/frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts:89 harnessErrorType` (REACH=LIVE).
- **C16** — `projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx`:
  - symbols: `:1022 turn:error handling`, `:1037 process:exit handling`, `:1374-1421 preservedDraft/preservedAttachments`, `:1604-1630 restore draft + attachments on failure`, `:1852 pickAttachments`, `:233 AttachmentChips`, `:2048 remove-attachment chip`, `:2095 Attach files (woven)`;
  - `projects/chirality-app-dev/frontend/src/lib/harness/chat-draft.ts`: `:70 buildChatDraftStorageKey`, `:117 readChatDraftSnapshotFromStorage`, `:165 persistChatDraftSnapshotToStorage` (localStorage);
  - `projects/chirality-app-dev/frontend/src/lib/harness/ui-attachments.ts:96 buildUiAttachment`;
  - REACH=LIVE (all);
  - SYMBOL-REACH: `ChatPanel` rendered at `woven-dialogue-shell.tsx:855`.
- **C17** — `projects/chirality-runtime/packages/core/src/turn-coordinator.ts:249-253` (`process:exit` / `turn:error` fatal). REACH=LIVE. SYMBOL-REACH: not checked.
- **C18** — Redaction:
  - `projects/chirality-app-dev/frontend/src/lib/harness/run-logger.ts:81 redactConfiguredApiKeys`, `:95 redactJsonLike` (REACH=LIVE; module reached via `chat-organization.ts`; SYMBOL-REACH: not checked);
  - `projects/chirality-app-dev/frontend/src/lib/harness/api-key-store.ts:33 getProviderApiKey` (precedence ui → `ANTHROPIC_API_KEY` → `CHIRALITY_ANTHROPIC_API_KEY`) (REACH=LIVE). SYMBOL-REACH: its `getUiApiKey`/`hasUiApiKey` callers are `claude-agent-sdk-manager.ts`, `anthropic-agent-sdk-manager.ts` and `runtime.ts`, all REACH=LEGACY_ONLY; `run-logger.ts:1` uses `getProviderUiApiKey`.
- **C19** — `projects/chirality-app-dev/frontend/src/lib/shell/persona-resolution.ts`: `:3 DEFAULT_PERSONA='HELP_HUMAN'`, `:11 DIRECT_ENTRY_ROLES` (HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS). REACH=LIVE. SYMBOL-REACH: imported at `chat-panel.tsx:36`. The `role not mechanically enforced` and `Opt-in Preview` strings occur only in C3/C4 (and a `globals.css:3880` comment); searched `src`, excluding tests.
- **C20** — Account row:
  - `projects/chirality-app-dev/frontend/src/components/shell/account-row.tsx`: `:13 AccountRow`, `:68` identity line (`hosted ? hostedBootstrapSummary : LocalModelStatus`);
  - `projects/chirality-app-dev/frontend/src/components/shell/account-settings-controls.tsx:18 LocalModelStatus`;
  - `projects/chirality-app-dev/frontend/src/components/shell/account-popover.tsx:25 AccountPopover`;
  - REACH=LIVE (all);
  - SYMBOL-REACH: `AccountRow` rendered via `shell-frame.tsx:404`. On the live path `hosted` is non-null, so the row shows `hostedBootstrapSummary` and not `LocalModelStatus`.
- **C21** — Attachment picker (REACH=LIVE for both):
  - `projects/chirality-app-dev/frontend/electron/attachment-picker.ts`: `:51 attachmentDialogOptions`, `:131 createAttachmentSelectionHandler`;
  - `projects/chirality-app-dev/frontend/src/lib/shell/native-attachments.ts:15 getNativeAttachmentBridge`.
- **C22** — `projects/chirality-app-dev/frontend/src/lib/credential-storage-state.ts:21 CREDENTIAL_STORAGE_STATES`, `:30 isCredentialStorageState`. REACH=LIVE.

**Test registry**

All frontend tests are under `projects/chirality-app-dev/frontend/src/__tests__/`; runtime tests are under `projects/chirality-runtime/tests/`.

- **T1** `components/api-key-settings-storage-states.test.ts`:
  - "renders each of the four states with a distinct data-storage marker" (:93);
  - "storageUnavailable: explains what the operator can do and hides entry" (:116);
  - "decryptFailed: asks for re-entry, …" (:145);
  - "keeps entered key material out of the rendered tree …" (:190).
- **T2** `components/api-key-settings.test.ts`:
  - "renders UI-stored status …" (:48);
  - "renders environment status …" (:59);
  - "renders the no-key status as an explicit none source" (:70);
  - "warns when encryption is unavailable …" (:77);
  - "server-renders an unreachable-daemon answer as unknown …" (:108).
- **T3** `electron/api-key-ipc.test.ts`:
  - "consumes the daemon-owned source when UI and environment credentials coexist" (:125);
  - "reports an unreachable daemon as a structured status rather than throwing" (:255).
- **T4** `electron/api-key-storage.test.ts`:
  - "provides the daemon credential port while preserving provider isolation" (:77);
  - "stores encrypted key material outside projectRoot …" (:99).
- **T5** `components/settings-view-codex.test.tsx` :: "shows the App-owned Runtime status and omits API-key and local-model panels for hosted Codex …" (:13).
- **T6** `components/account-consent-settings.test.ts`:
  - "server-renders the not-connected state …" (:45);
  - "pins the verbatim G0 A8 posture label …" (:62);
  - "pins the K-NET-1 posture labels and the network_access = true label" (:70);
  - "pins the ask-per-destination prompt copy …" (:82);
  - "pins the verbatim K-ROLE-2 labels" (:94).
- **T7** `components/account-consent-settings-states.test.ts`: fixture cases (:149-289).
- **T8** `lib/consent/fake-hosted-engine-consent-port.test.ts`:
  - "default to no command network and never pre-accept a destination" (:87);
  - "login creates the root-private app-owned home without touching ambient state; logout keeps it" (:143).
- **T9** `components/account-presentation.test.tsx`:
  - "reports the App-owned Runtime service in hosted Codex settings …" (:96);
  - "keeps the hosted popover to account, Settings, …" (:114);
  - "uses explicit login/logout/consent actions …" (:128).
- **T10** `components/hosted-bootstrap.test.tsx`: "requires an explicit project setup and sign-in …" (:80) and the others at :120-217.
- **T11** `lib/hosted-bootstrap-client.test.ts` and `api/harness/hosted-bootstrap.test.ts` (case names not extracted).
- **T12** `lib/harness-error-display.test.ts`:
  - "maps known typed errors to actionable copy" (:15);
  - "maps MISSING_API_KEY to provisioning guidance" (:36);
  - "falls back to generic copy for unknown codes" (:90).
- **T13** `lib/harness-errors.test.ts` :: "still falls back to SDK_FAILURE for unknown structural error types" (:30).
- **T14** `lib/harness-chat-draft.test.ts` (:12-164).
- **T15** `components/chat-panel-native-attachments.test.tsx`: "keeps the contained selected copy and draft available after a rejected send" (:99).
- **T16** `components/chat-panel-folder-binding.test.tsx`: "retains the actual binding and failed draft when provider synchronization refuses" (:106).
- **T17** `components/chat-panel-model-selectors.test.tsx`: `turn:error` events at :294, :306, :795, the last in "does not erase an earlier fatal turn error when a later exit is marked interrupted" (:793).
- **T18** `lib/run-logger.test.ts` :: "redacts raw and encoded configured API-key variants" (:22).
- **T19** `lib/redaction-path-matrix.test.ts` :: "redacts SDK hook diagnostics before persistence, replay, and browser display" (:23).
- **T20** `electron/attachment-picker.test.ts` and `lib/harness-ui-attachments.test.ts` (case names not extracted).
- **T21** Runtime `app-owned-composition.test.ts`:
  - "prepares the effective home, issues the app-host token, reports sign-in status …" (:59);
  - "relays the sign-in ceremony and refuses new sessions while signed out" (:263).
- **T22** Runtime `codex-effective-home.test.ts` :: "links every shared entry, excludes credential and cache files, and never writes into the user's home" (:34).

**Decision registry**

Register: `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`. DECISION_HITS for DEL-02-05:
- D-APP-19, 36, 38, 54, 55, 56, 59, 60, 64, 70, 71, 72, 73, 80, 108, 109, 110, 122 and 127 (all `RULED`);
- D-GOV-43 (`ROOT`).

Ruling records naming DEL-02-05:
- `D-APP-108_RULING_…:54`;
- `D-APP-110_RULING_…:48`;
- `D-APP-122_RULING_ACCOUNT_SETTINGS_HOST_GATE_2026-09-06.md:13`, plus register row `:143`;
- `D-APP-127_RULING_APPLICATION_D-GOV-43_…:109` (supersedes the V3-03 Root DEL-02-09 gate and the G3/G-CSP/G4 host gates for live login; replaced by S-8) and `:183` (PKG-02 DEL-02-05 architecture-bound clauses revised);
- `D-APP-70_RULING_2026-07-20.md:50`;
- `D-APP-71_RULING_2026-07-20.md:4`, plus register row `:86`.

D-APP-127 application map (DEL-02-05):
- `_STATUS.md` = YES (`_STATUS.md:11`);
- `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md` and `Dependencies.csv` = NO.

REFERENCE_HASHES (DEL-02-05): CONTRACT, SPEC and PRD are all recorded `MATCH` with recompute `Match=NO` (`HASH-RECOMPUTE@00115c719`).

---

## DEL-02-05#SEC-1 — Current responsibility (SoW:36)
- **Gist:** Provide key entry/status, storage feedback, attachments, typed errors and retry states. Serve as the account/consent UX carrier via `HostedEngineConsentPort`, with the four storage states, three network postures and the role/posture labels.
- **Code:** C1, C2, C3, C4, C5 (TEST_ONLY), C6, C14, C16, C19, C21, C22.
- **Reach facts:** the port-consuming panel (C3) and the key panel (C1) are not rendered on the woven live path. The live account surface is C6/C7 (Codex login, C9).
- **Tests:** T1, T2, T5, T6, T7, T8, T9, T12, T15.
- **Decisions:** D-APP-108 (SCA-APP-010 seating), D-APP-122, D-APP-127, D-GOV-43.

## DEL-02-05#SEC-2 — Current acceptance obligations (SoW:71)
- **Gist:** Five obligations: an app-wide account with per-folder consent; the row shows only local-model status; Settings split into groups; Root-owned login home; role entry with its labels.
- **Code:**
  - (1) C2 `settings-view.tsx:31-32`, C3, C6;
  - (2) C20 `account-row.tsx:68` (hosted summary versus `LocalModelStatus`); searched `OpenAI` in C20: the hosted summary is from C6, and `hosted-bootstrap-view.tsx:115-116` names OpenAI;
  - (3) C2 `:31-37`;
  - (4) C9 `codex-effective-home.ts`;
  - (5) C19, C3 `:419-440`.
- **Tests:** T5, T6, T9, T10, T21, T22.
- **Decisions:** D-APP-108 (Q7, Q8), D-APP-122, D-APP-127.

## DEL-02-05#SEC-3 — Seating and rulings (SoW:79)
- **Gist:** Records D-APP-108 seating of V3-05, the Q7/Q8 rulings, the alignment writes WI-016..020 and the pending DEP-007/008.
- **Code:** NO_CANDIDATES (documentary). Searches: HINTS (1 empty row); DECISION_HITS.
- **Decisions:** D-APP-108 (`_STATUS.md:28`, `ScopeOfWork.md:81`), D-APP-109 (DEP register re-extract, `_STATUS.md:27`).

## DEL-02-05#CLM-001 — Datasheet header (SoW:90)
- **Gist:** Current-state note that REF-006 `docs/PRD.md` is MATCH under D-APP-38 and that older mismatch wording is history.
- **Code:** NO_CANDIDATES (documentary).
- **Other evidence:** REFERENCE_HASHES shows DEL-02-05 PRD recorded MATCH, recompute `Match=NO`.
- **Decisions:** D-APP-56, D-APP-38.

## DEL-02-05#CLM-002 — Identification (SoW:97)
- **Gist:** Identification table: ID, name, PKG-02, type UX_UI_SLICE, SOFTWARE_DECOMP v3.2, envelope S, responsible party TBD.
- **Code:** NO_CANDIDATES (documentary). Searches: HINTS tokens DeliverableID/PackageName (hits only in `deliverables-route.test.ts` and similar fixtures).

## DEL-02-05#CLM-003 — Attributes (SoW:114)
- **Gist:** Lists the UI surfaces, the key status values `ui|env|none`, the precedence ui → `ANTHROPIC_API_KEY` → `CHIRALITY_ANTHROPIC_API_KEY`, and the `turn:error`/`process:exit` event names.
- **Code:**
  - C1 `:303` (`data-source`), C10 `:23`, C11 `:236-251`, C18 `api-key-store.ts:33`;
  - C12 (daemon status stub carries no `source`);
  - C16 `:1022/:1037`, C17.
- **Tests:** T2, T3, T4, T17.
- **Decisions:** D-APP-73 (context: the daemon owns resolution, per the 2026-08-20 R03 history note in `_STATUS.md`).

## DEL-02-05#CLM-004 — Conditions (SoW:129)
- **Gist:** Key material stays out of project truth; storage at `userData/credentials/api-key.enc` via `safeStorage`; retry context preserved; secrets redacted; PRD MATCH.
- **Code:** C11 `:30,:50,:75-83,:112`; C16 `:1604-1630`; C18; C9 `codex-app-server-client.ts:44`; C12.
- **Tests:** T4 (:99), T14, T15, T18, T19.
- **Other evidence:** REFERENCE_HASHES PRD `Match=NO`.
- **Decisions:** D-APP-38, D-APP-72, D-APP-127 (`_STATUS.md:11`: Codex's own credential handling; `safeStorage` only "where it is still used").

## DEL-02-05#CLM-005 — Construction (SoW:143)
- **Gist:** Five components: key panel via IPC, storage feedback, typed error display, retry-preserving state, SSE compatibility. Paths and copy are TBD.
- **Code:** C1, C10, C13 `:81`, C14, C16, C17.
- **Tests:** T1, T2, T3, T12, T15, T17.

## DEL-02-05#CLM-006 — References (SoW:156)
- **Gist:** Reference list (`_CONTEXT`, `_DEPENDENCIES`, `_REFERENCES`, the decomposition, CONTRACT, DIRECTIVE, PLAN, SPEC, TYPES), with REF-006 MATCH.
- **Code:** NO_CANDIDATES (documentary).
- **Other evidence:** REFERENCE_HASHES shows CONTRACT, SPEC and PRD recorded MATCH, recompute `Match=NO`.

## DEL-02-05#CLM-007 — D-APP-56 R5 P45 reconciliation (SoW:172)
- **Gist:** UPD-112 includes SOW-023 traceability because decomposition v3.2 maps it to DEL-02-05.
- **Code:** NO_CANDIDATES (documentary). Searches: HINTS (1 empty row).
- **Decisions:** D-APP-56.

## DEL-02-05#CLM-028 — Applied decomposition v3 carrier row (SoW:178)
- **Gist:** Verbatim SCA-APP-008 row: account/consent carrier via `HostedEngineConsentPort`, the four storage states, three postures, role labels and outputs; live claims gated.
- **Code:**
  - C3, C4, C5 (TEST_ONLY), C1, C22, C21, C14, C16;
  - live account surface: C6, C7, C8, C9;
  - `grantProviderNetworkConsent` returns status unchanged (C9 `hosted-bootstrap.ts:56`);
  - `network_access` occurs only in C3/C4; searched `src` and runtime `packages/*/src`.
- **Tests:** T1, T5, T6, T7, T8, T9, T10.
- **Decisions:** D-APP-127 (family 1 retires the port; `_STATUS.md:11`), D-GOV-43, D-APP-108.

## DEL-02-05#CLM-008 — Specification header (SoW:192)
- **Gist:** Section header only.
- **Code:** NO_CANDIDATES (documentary). Searches: HINTS (1 empty row).

## DEL-02-05#CLM-009 — Scope (SoW:197)
- **Gist:** In scope: key status UI, storage error feedback, typed errors, retry state, SSE compatibility. Out of scope: engine internals, redaction helper, network allowlist, deps. Remove and reveal controls are optional.
- **Code:** C1 (`:370` remove control), C10, C14, C16, C17.
- **Tests:** T2 (:48 remove control), T12, T15.
- **Decisions:** D-APP-56 (R4-P01, remove/reveal convenience).

## DEL-02-05#CLM-010 — Requirements R01–R10 (SoW:225)
- **Gist:** R01 IPC storage outside the working root; R02 `ui|env|none`; R03 precedence; R04 storage-unavailable error; R05 typed actionable errors; R06 retry preservation; R07 SSE names; R08 not project truth; R09 redaction; R10 consume `HarnessErrorType` from `@chirality/harness-contract`.
- **Code:**
  - R01: C10 `:185`, C11 `:50,:75`, C13 `:81`;
  - R02: C1, C10 `:23`;
  - R03: C11 `:236-251` (SYMBOL-REACH: class not constructed), C18 `api-key-store.ts:33`, C12 (live daemon stub);
  - R04: C1 `:316`, C11 `:79`;
  - R05: C14;
  - R06: C16 `:1604-1630`;
  - R07: C16 `:1022,:1037`, C17;
  - R08: C16 `chat-draft.ts` (localStorage), C11;
  - R09: C18, C9 `:44`;
  - R10: C14 `:2` (imports from `@chirality/runtime-contracts/types`, not `@chirality/harness-contract`), C15.
- **Tests:** T1-T4, T12, T13, T14, T15, T17, T18, T19.
- **Decisions:** D-APP-73, D-APP-72, D-APP-56.

## DEL-02-05#CLM-011 — Standards (SoW:243)
- **Gist:** Project-truth boundary; key storage policy (UI safeStorage plus environment fallback); browser SSE names compatible; runtime redaction policy.
- **Code:** C11, C16 `chat-draft.ts`, C16 `:1022/:1037`, C17, C18, C9 `:44`.
- **Tests:** T4, T14, T17, T18, T19.

## DEL-02-05#CLM-012 — Verification table R01–R10 (SoW:255)
- **Gist:** Verification approach per requirement: IPC save test, status rendering, precedence, unavailable storage, error mapping, retry state, SSE, non-authoritative state, redaction, contract import review.
- **Code:** (the code under test is listed at CLM-010).
- **Tests:**
  - R01: T3 (:105), T4 (:99);
  - R02: T2 (:48, :59, :70);
  - R03: T3 (:125);
  - R04: T1 (:116), T2 (:77);
  - R05: T12;
  - R06: T15, T16;
  - R07: T17;
  - R08: T4 (:99), T14;
  - R09: T18, T19;
  - R10: T13.

## DEL-02-05#CLM-013 — Documentation, REQ-001..005, AC-001, AC-002 (SoW:273)
- **Gist:** Required artifacts are the key panel, error display and storage error UI (paths TBD). REQ-001: account/consent carrier and Electron-main-only transport. REQ-002: four states. REQ-003: postures. REQ-004: roles and labels. REQ-005: fail-closed `binding: unavailable` / `hostedReady:false`. AC-001/002.
- **Code:**
  - REQ-001: C3, C4, C6-C9; transport fact in C8 (Next API routes); C13.
  - REQ-002: C1 `:237`, C22, C10 `:109`.
  - REQ-003: C3 `:328-365`, C4 `:48-56,:95`.
  - REQ-004: C19, C3 `:419-440`, C4 `:188`.
  - REQ-005: searched `canonical-identity-producer-unavailable|hostedReady` in frontend `src` and runtime `packages`; not grepped to line (HINTS token `canonicalRoot` hits only). Candidate starting points: C7 `hosted-bootstrap-controller.tsx:94-102` (project states) and C9 `hosted-bootstrap.ts:50` (`canStartLogin`). SYMBOL-REACH: not checked.
- **Tests:** T1, T5-T10, T21.
- **Decisions:** D-APP-127, D-GOV-43, D-APP-108.

## DEL-02-05#CLM-014 — Procedure header (SoW:301)
- **Gist:** Procedure header with the D-APP-56 PRD MATCH note.
- **Code:** NO_CANDIDATES (documentary).
- **Other evidence:** REFERENCE_HASHES PRD `Match=NO`.

## DEL-02-05#CLM-015 — Purpose (procedure) (SoW:308)
- **Gist:** Working procedure scoped to the UI slice, without engine internals or dependency extraction.
- **Code:** NO_CANDIDATES (documentary). Searches: HINTS (1 empty row).

## DEL-02-05#CLM-016 — Prerequisites (SoW:315)
- **Gist:** Accepted context, references, a status that permits work, contracts available or mocked; dependencies TBD.
- **Code:** NO_CANDIDATES (documentary).
- **Other evidence:** HINTS tokens `_CONTEXT.md` etc. hit only fixtures. The `Dependencies.csv` present in the folder is a fact; see D-APP-109.

## DEL-02-05#CLM-017 — Steps 1–7 (SoW:326)
- **Gist:** Confirm scope; key status contract (`ui|env|none`, precedence); storage feedback via IPC; typed error display with redaction; preserve retry state; SSE compatibility; secret and project-truth checks.
- **Code:** C1, C10, C11, C12, C13, C14, C16, C17, C18.
- **Tests:** T1-T4, T12, T15, T17, T18.

## DEL-02-05#CLM-018 — Verification checks (SoW:368)
- **Gist:** Checks: four-document traceability, key status UI, safeStorage unavailable, runtime error UI, retry state, SSE compatibility, secret hygiene.
- **Code:** see CLM-012.
- **Tests:** T1, T2, T12, T15, T17, T18, T19.

## DEL-02-05#CLM-019 — Records (SoW:383)
- **Gist:** Records expected: panel, error display and storage UI implementations and tests; no-leak evidence; rulings on CT001/CT002.
- **Code:** NO_CANDIDATES (documentary record list).
- **Other evidence:** `Evidence_TYPED_STORAGE_STATES_UI_2026-09-03.md`, `Evidence/V3-02_consent_ux_fixtures_2026-09-03/` and `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md` are in the deliverable folder (not read). The CT002 ruling is D-APP-56 R4-P35.

## DEL-02-05#CLM-020 — Evidence Binding Table, VER-001, VER-002 (SoW:394)
- **Gist:** Seven evidence needs, all bound "TBD". VER-001 covers schema and parity checks. VER-002 runs the consent, retry, storage-state, posture and label tests behind fakes, inspects Electron-main-only transport and no ambient `~/.codex` read, and treats fixtures as UI-only.
- **Code:** C1, C3, C5, C8 (transport fact), C9 `codex-effective-home.ts:33`, C13, C14, C16, C18.
- **Tests:** T1-T8, T12, T15, T17-T19, T22.

## DEL-02-05#CLM-021 — Guidance header (SoW:413)
- **Gist:** Guidance header with the D-APP-56 PRD MATCH note.
- **Code:** NO_CANDIDATES (documentary).
- **Other evidence:** REFERENCE_HASHES PRD `Match=NO`.

## DEL-02-05#CLM-022 — Purpose (guidance) (SoW:420)
- **Gist:** Operators get a clear key-status and failure-recovery UI, while key material and convenience state stay outside project truth.
- **Code:** C1 (rendering fact as in the registry), C14, C16, C11.
- **Tests:** T2, T12, T15.

## DEL-02-05#CLM-023 — Principles (SoW:429)
- **Gist:** Keep key material invisible; separate feedback from runtime authority; preserve retry context; use stable SSE names; PRD MATCH.
- **Code:** C1 (`:190` test target), C14, C16 `:1022/:1037`, C17.
- **Tests:** T1 (:190), T15, T17.
- **Other evidence:** REFERENCE_HASHES PRD `Match=NO`.

## DEL-02-05#CLM-024 — Considerations (SoW:440)
- **Gist:** The key UI is presentation only; the storage-unavailable wording is unspecified; error copy must not leak secrets; no approval language; attachment validation is elsewhere.
- **Code:** C1 `:316`, C14 `:11`, C18, C21.
- **Tests:** T1, T12, T20.

## DEL-02-05#CLM-025 — Trade-offs (SoW:451)
- **Gist:** Detail versus secrecy; convenience versus truth; no invented taxonomy; keep SSE names while internals move behind `TurnEngine`.
- **Code:**
  - C14/C15 (taxonomy imported, not redefined);
  - C16 `:1022/:1037`, C17;
  - `TurnEngine` hits: `projects/chirality-app-dev/frontend/src/lib/harness/turn-engine.ts` (REACH not looked up; HINTS token `TurnEngine`; SYMBOL-REACH: not checked).
- **Tests:** T13, T17.

## DEL-02-05#CLM-026 — Examples (SoW:463)
- **Gist:** TBD; no approved UI copy examples in the source corpus.
- **Code:** NO_CANDIDATES (documentary). Searches: HINTS (1 empty row).

## DEL-02-05#CLM-027 — Conflict Table CT001/CT002 (SoW:470)
- **Gist:** CT001 is the PRD warning (reconciled under D-APP-38). CT002 is the SOW-019 split with DEL-04-05/DEL-09-06 (ruled under D-APP-56 R4-P35).
- **Code:** NO_CANDIDATES (documentary).
- **Other evidence:** REFERENCE_HASHES PRD `Match=NO`.
- **Decisions:** D-APP-38, D-APP-56.

## DEL-02-05#REM-1 — DEL-02-05-V3-03 (_STATUS.md:11)
- **Gate suffix (verbatim):** `NOT_SELECTABLE_UNTIL: the re-platformed login flow lands on the production path (D-GOV-43 items 3 and 6)`
- **Gist:** Live sign-in and sign-out through Codex `account/login/start|cancel` and `account/logout` in the Chirality effective home. The port and postures are retired; the App never relays credentials. Removed when S-8 passes on the production path.
- **Code:**
  - C9: `codex-login.ts:57-80`, `hosted-bootstrap.ts:56-73`, `runtime-daemon.ts:440-465` (not touched), `codex-effective-home.ts:33-41`, `codex-app-server-client.ts:41`;
  - C6, C7, C8 (App side, all REACH=LIVE; rendered per the registry);
  - retired-port residue: C3, C4 (LIVE modules, View not rendered on the live path), C5 (TEST_ONLY).
- **Tests:** T9, T10, T11, T21 (:263), T22.
- **Where the gate status may be checked (App surfaces):**
  - (a) `_STATUS.md` Remaining and History in the deliverable folder;
  - (b) `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:71,95-111` (S-8 definition; supersession of the V3-03 gates);
  - (c) `projects/chirality-app-dev/docs/RELEASE_QUALITY_GATES.md:180-182` (S-1..S-8 of D-GOV-43 item 12 as the acceptance set);
  - (d) the deliverable's `_run_records/` and `Evidence/`: no S-8 evidence file found (searched `S-8` in the folder, where the only hit is `_STATUS.md`).
- **Decisions:** D-APP-127, D-GOV-43, D-APP-122, D-APP-108.

## Cross-cutting

**Recurring modules** (units citing each):

| Module | Candidate | REACH | Units citing |
|---|---|---|---|
| `components/shell/chat-panel.tsx` (+ `chat-draft.ts`) | C16 | LIVE | 14 |
| `components/settings/api-key-settings.tsx` | C1 | LIVE | 12 |
| `lib/harness/error-display.ts` | C14 | LIVE | 11 |
| `electron/api-key-storage.ts` | C11 | LIVE | 9 |
| `electron/api-key-ipc.ts` | C10 | LIVE | 7 |
| `components/settings/account-consent-settings.tsx` | C3 | LIVE | 7 |
| `lib/consent/hosted-engine-consent-port.ts` | C4 | LIVE | 5 |
| `runtime/packages/daemon/src/{codex-login,hosted-bootstrap}.ts` | C9 | LIVE | 5 |

**Rendered versus not rendered** (static reach facts, woven live path from `app/page.tsx`):
- **Rendered:** `ChatPanel` (C16), `HostedBootstrapView` (C6), `AccountRow` with the hosted summary (C20), `SettingsView` hosted branch (C2 `:31,:33,:36-37`).
- **Imported but not rendered** (module tag LIVE): `AccountConsentSettingsView` and the `ApiKeySettings` sections (C2 `:31-35` are `!hosted`, and the live controller is non-null); legacy `LoopShell`/`PortalLoopShell` (voided `legacy` prop).
- `ApiKeySettings` is rendered only from `app/not-found.tsx` via `AppShell` (default `ShellFrame`).

**Live versus legacy, and other facts:**
- The UI-key precedence helper consumers (`getUiApiKey`, `hasUiApiKey`) sit in LEGACY_ONLY modules.
- `SafeStorageCredentialStore` has no non-test construction.
- The live runtime composition passes a credentials stub (C12) whose status lacks `source`.
- The consent port has only a fake implementation (TEST_ONLY).
- `frontend/packages/harness-contract` is NOT_IN_MAP. The live UI imports `HarnessErrorType` from `@chirality/runtime-contracts`.
- No frontend path is in TOUCHED_PATHS. Runtime touched ranges near the candidates: `app-owned-composition.ts:228`, `runtime-daemon.ts:169-171,660-686` (the cited ranges are outside them).
#END
