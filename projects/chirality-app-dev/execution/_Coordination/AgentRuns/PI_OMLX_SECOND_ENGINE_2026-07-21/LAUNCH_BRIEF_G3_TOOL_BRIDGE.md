# Launch Brief — G3 Provider-Neutral Tool Bridge

- **Role:** TASK neutral tool bridge worker
- **Model:** `gpt-5.6-sol` (record substitutions)
- **Authority:** D-APP-72/SCA-APP-002; G2 contract frozen.

## Write scope

- New provider-neutral tool-definition/binder modules under `frontend/src/lib/harness/`
- New bridge tests under `frontend/src/__tests__/lib/`
- Existing Claude/MCP tool source only if needed to expose an existing handler without semantic change; never edit coordination/delegation, runtime.ts, TurnEngine, contracts, packages, credentials, or Pi adapter files.
- `RETURN_G3_TOOL_BRIDGE.md`

## Required behavior

- Define one Chirality-owned tool representation: name, label/description, JSON schema, permission/evidence metadata, and async handler.
- Provide Claude and Pi binders without duplicating handlers or permission logic.
- Bind at least one existing bounded read-only Chirality tool suitable for the first local child milestone.
- Permission/path containment/hard-deny/redaction/evidence decisions remain in Chirality before handler execution.
- Pi binder produces only explicitly supplied custom tools; no native Pi tool or delegation exposure.
- Tests prove allow result equivalence, denial prevents handler invocation, malformed/unknown input fails closed, and binder output contains no ambient/native tools.

Return exact files/checks/risks and actual model.
