# G2 Core Contract Return

Status: PASS

Actual model: `gpt-5.6-sol`

## Result

- Replaced the process-global engine assumption with a provider-neutral `AgentEnginePort`, descriptor, preflight, per-turn selection, and cached adapter registry.
- Added `turnId`, provider-neutral session initialization attribution, versioned runtime fingerprints, typed engine/provider/model failures, and deprecated `IAgentSdkManager` compatibility.
- Added provider-neutral `engineSelection` and opaque `adapterSession` session metadata with lazy legacy-Claude migration and Claude-only dual writes.
- Preserved the existing routes, SSE event names, Claude/stub defaults, environment compatibility, and no-fallback turn behavior.
- Removed Anthropic/package attribution responsibilities from `TurnEngine`; adapters now own preflight and attribution.
- Pinned `@earendil-works/pi-coding-agent` to exact version `0.80.10` after the Electron/Node prerequisite.

## Principal paths

- `frontend/packages/harness-contract/src/agent-engine-port.ts`
- `frontend/packages/harness-contract/src/types.ts`
- `frontend/packages/harness-contract/src/engine-conformance.ts`
- `frontend/src/lib/harness/engine-registry.ts`
- `frontend/src/lib/harness/runtime.ts`
- `frontend/src/lib/harness/turn-engine.ts`
- `frontend/src/lib/harness/session-manager.ts`
- `frontend/src/lib/harness/runtime-fingerprint.ts`
- Claude, direct-Anthropic, stub, boot-route, mapper, and compatibility tests affected by the new attribution contract
- `frontend/package.json`
- `frontend/package-lock.json`

## Validation

- `npm run typecheck`: PASS
- `npm test -- --testTimeout=60000`: PASS — 98 files passed, 1 skipped; 781 tests passed, 4 skipped

## Recorded residual

The exact Pi install changed the npm audit inventory to 26 advisories (1 low, 14 moderate, 8 high, 3 critical). No automatic audit rewrite was applied. G5 must classify the production reachability and package provenance before closeout.
