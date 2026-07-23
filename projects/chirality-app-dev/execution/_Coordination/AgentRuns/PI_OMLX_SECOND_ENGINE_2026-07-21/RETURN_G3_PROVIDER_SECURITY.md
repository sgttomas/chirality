# Return — G3 oMLX Provider Security and Credentials

- **Role:** TASK oMLX security/credential worker
- **Actual model:** `gpt-5.6-sol`
- **Result:** PASS
- **Provider identifier:** `omlx`

## Implemented

- Generalized Electron `safeStorage` persistence to provider-keyed credentials while retaining Anthropic's existing `credentials/api-key.enc`, `__CHIRALITY_UI_API_KEY__`, functions, and IPC channels.
- Added an isolated `credentials/api-key.omlx.enc` blob and provider-keyed process global. Electron startup now loads both supported provider credentials.
- Added provider-keyed IPC/preload operations for `anthropic` and `omlx`; decrypted values never cross the renderer bridge.
- Added server-side `getProviderUiApiKey`, `getProviderApiKey`, `hasProviderApiKey`, and `getOmlxApiKey`. The oMLX fallback reads only `CHIRALITY_OMLX_API_KEY`; existing Anthropic helper semantics remain unchanged.
- Added strict oMLX configuration and authenticated model discovery:
  - default `http://127.0.0.1:8000/v1`;
  - literal `127.0.0.1`, HTTP, exact `/v1`, no URL credentials/query/fragment, and valid explicit test ports;
  - manual redirect refusal;
  - exact model IDs with no aliasing;
  - typed, static, key-redacted errors for configuration, offline, authentication, protocol, malformed/empty models, and unknown models.

## Integration API

- Credential access: `getOmlxApiKey()` or `getProviderApiKey('omlx')` from `api-key-store.ts`.
- Provider setup: `normalizeOmlxBaseUrl()` and `resolveOmlxProviderConfig()`.
- Preflight/discovery: `discoverOmlxModels()` and `requireOmlxModel()`.
- Failure handling: `OmlxProviderError` with `OmlxProviderErrorCode`.
- Renderer bridge: `window.chirality.providerApiKey.store/remove/status('omlx', ...)`.

## Files

- `frontend/electron/api-key-storage.ts`
- `frontend/electron/api-key-ipc.ts`
- `frontend/electron/preload.ts`
- `frontend/src/lib/harness/api-key-store.ts`
- `frontend/src/lib/harness/omlx-provider-config.ts`
- `frontend/src/__tests__/electron/api-key-storage.test.ts`
- `frontend/src/__tests__/electron/api-key-ipc.test.ts`
- `frontend/src/__tests__/lib/api-key-store.test.ts`
- `frontend/src/__tests__/lib/omlx-provider-config.test.ts`
- `execution/_Coordination/AgentRuns/PI_OMLX_SECOND_ENGINE_2026-07-21/RETURN_G3_PROVIDER_SECURITY.md`

## Checks

- `npm run typecheck` — PASS.
- Focused credential/provider suite — PASS, 4 files / 31 tests.
- Existing Anthropic settings and adapter regression suite — PASS, 3 files / 98 tests.
- `git diff --check` on the G3 write scope — PASS.
- The first fake-server run in the restricted sandbox could not bind `127.0.0.1` (`EPERM`); the same deterministic suite passed after approved host-level loopback execution.

## Residual risks / fan-in notes

- The current settings UI remains Anthropic-only by scope; oMLX has secure IPC/preload support but no graphical form in this tranche.
- The existing global `ChiralityBridge` declaration does not describe even the legacy `apiKey` bridge; feature components currently use local narrowed bridge types. A future settings/UI tranche should add the provider bridge to that declaration.
- Callers must preserve `OmlxProviderError` rather than interpolate raw lower-level network errors. This implementation intentionally discards fetch/response bodies from surfaced failures so credentials cannot be reflected.
- No live oMLX process or model was required or contacted; transport behavior is covered by the deterministic loopback fake server.
