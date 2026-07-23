# Launch Brief — G3 oMLX Provider Security and Credentials

- **Role:** TASK oMLX security/credential worker
- **Model:** `gpt-5.6-sol` (record substitutions)
- **Authority:** D-APP-72/SCA-APP-002; G1/G2 PASS.

## Write scope

- Provider-keyed evolution of `frontend/electron/api-key-storage.ts`, `api-key-ipc.ts`, `preload.ts`, and `frontend/src/lib/harness/api-key-store.ts`
- Associated Electron/UI contract tests as required to preserve Anthropic behavior
- New `frontend/src/lib/harness/omlx-provider-config.ts` and deterministic provider/fake-server security tests
- `RETURN_G3_PROVIDER_SECURITY.md`

Do not edit runtime.ts, TurnEngine, harness-contract, package files, Pi adapter/mapper, tool/MCP/delegation, or governance.

## Required behavior

- Preserve/migrate the existing Anthropic `api-key.enc` and current IPC compatibility.
- Add provider-keyed encrypted storage and process-global access for `omlx-openai`; never expose decrypted keys to the renderer.
- Support `CHIRALITY_OMLX_API_KEY` fallback without touching Anthropic variables.
- Default base URL `http://127.0.0.1:8000/v1`; permit test ports on literal `127.0.0.1` only.
- Reject non-http, non-127.0.0.1, URL credentials, fragments, unexpected paths, and redirects before prompt transmission.
- Implement authenticated `/models` discovery returning exact IDs and typed/redacted errors for offline, auth, malformed response, empty models, and unknown model.
- Tests cover legacy Anthropic storage, separate provider blobs/globals, loopback validation, model discovery, redirect refusal, and key redaction.

Return exact files/checks/risks and actual model.
