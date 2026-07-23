# Return — G3 Provider-Neutral Tool Bridge

- **RunID:** `PI_OMLX_SECOND_ENGINE_2026-07-21`
- **Node:** `G3_TOOL_BRIDGE`
- **Verdict:** `PASS`
- **Actual model:** `gpt-5.6-sol` (no substitution)
- **Authority:** `D-APP-72`, `SCA-APP-002`, and frozen G2 provider-neutral contract

## Result

- Added one Chirality-owned tool representation containing name, label, description, closed object JSON schema, permission metadata, evidence metadata, and one guarded async execution path.
- Added independent Claude and Pi binders. Both binders reuse the same guarded definition and handler; neither duplicates permission, containment, redaction, or evidence policy.
- Added a concrete `read_file` bridge matching the existing canonical descriptor and limited to regular UTF-8 files contained by the active project root and optional managed read scopes.
- The shared execution path validates input, evaluates path and symlink policy, appends the Chirality permission decision, rejects non-allow decisions, and only then invokes the handler. Result evidence uses the existing redacted persistence and governed result-budget pipeline.
- Pi output contains explicit non-secret `chirality` permission metadata for adapter defense in depth. The Pi binder emits only explicitly supplied custom tools and does not add Pi built-ins, native subagents, `delegate_agent`, or ambient tools.

## Changed paths

- `frontend/src/lib/harness/chirality-tool-bridge.ts`
- `frontend/src/lib/harness/claude-tool-binder.ts`
- `frontend/src/lib/harness/pi-tool-binder.ts`
- `frontend/src/__tests__/lib/chirality-tool-bridge.test.ts`
- this return

No runtime, TurnEngine, contract, package, credential, Pi adapter, coordination, or delegation source was edited.

## Public integration surface

- `createBoundedReadToolDefinitions({ context, allowedToolNames: ['read_file'] })`
- `bindChiralityToolsForClaude(definitions)`
- `bindChiralityToolsForPi(definitions)`
- `executeChiralityTool({ definitions, toolName, args, toolUseId, signal })`

The initial bounded factory rejects every tool other than canonical `read_file`. Duplicate requested `read_file` entries collapse to one definition. Both binders also reject duplicate supplied definition names.

## Validation

| Check | Result |
|---|---|
| Focused neutral bridge tests | PASS: 1 file, 4 tests |
| Existing permission overlay tests | PASS: 13 tests |
| Existing Chirality read MCP tests | PASS: 10 tests |
| Combined focused regression run | PASS: 3 files, 27 tests |
| Renderer and Electron TypeScript typecheck | PASS |

The tests prove Claude/Pi allow-result equivalence, permission-before-handler ordering, escaping-path hard denial without handler invocation, malformed/extra/unknown-input fail closure, exact explicit tool binding, canonical permission evidence, and absence of native/ambient/delegation tools.

## Residual risks and integration notes

- The Pi adapter must require `tool.chirality.readOnly === true` and an exact `permissions: ['read']` posture before passing a bound tool to Pi. Metadata is defense in depth; the guarded handler remains authoritative.
- The Claude binder returns SDK MCP tool definitions but is not wired into the existing Claude MCP server in this disjoint tranche. Existing Claude behavior is unchanged.
- The file reader intentionally rejects files above the canonical descriptor's artifact budget and non-regular files. It returns UTF-8 text only; binary/image reading is outside the bounded milestone.
- Result persistence uses the existing Chirality redactor. No new secret-recognition policy was introduced in this tranche.
