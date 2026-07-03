# Evidence - CODEV-002 Harness Contract Package Consumption Readiness

Date: 2026-07-03

## Scope

This evidence record captures the post-D-APP-46 package-consumption readiness baseline for DEL-03-01. It records the current internal package shape and the remaining shim/import posture that downstream DEC-041 automation must judge against.

This is a documentation and evidence update only. It does not publish a package, settle the Flow-A contract version, authorize piping consumption, open F3, retire shims, mark dependencies satisfied, advance lifecycle state, or create release, professional, certification, sealing, authentication, or code-compliance claims.

## Authority Basis

| Source | Baseline fact used |
|---|---|
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-46_RULING_2026-07-02.md` | D-APP-46 authorizes the internal dependency-free contract-spine extraction, preserves back-compat re-exports, and keeps `FLOW_A_CONTRACT_VERSION` at `TBD_BY_TIER_0`. |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-45_RULING_2026-07-02.md` | D-APP-45 confirms app-dev Flow-A wiring only: the concrete Flow-A version stays tier-0-owned, and the SDK/tool-registry constants are referenced inputs, not version settlement. |
| `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-041 | Piping consumption remains gated behind D-21 and the no-manual-toil automation condition. |
| `projects/chirality-app-dev/frontend/packages/harness-contract/package.json` | The internal package is `@chirality/harness-contract`, version `0.0.0-private`, `private: true`, with the exports map recorded below. |

## Package Baseline

| Field | Measured value |
|---|---|
| Package name | `@chirality/harness-contract` |
| Version | `0.0.0-private` |
| Private flag | `true` |
| Dependency posture | Dependency-free internal Flow-A harness contract spine |
| Package source root | `frontend/packages/harness-contract/src/` |
| Frontend dependency wiring | `@chirality/harness-contract`: `file:packages/harness-contract` in `frontend/package.json` |
| Dependency lint | `frontend/scripts/assert-harness-contract-deps.mjs`, exposed as `npm run harness:validate:contract-deps` |

## Exports Baseline

`frontend/packages/harness-contract/package.json` exposes the root export, 10 module subpaths, and `./package.json`:

| Export | Target |
|---|---|
| `.` | `./src/index.ts` |
| `./agent-engine-port` | `./src/agent-engine-port.ts` |
| `./engine-conformance` | `./src/engine-conformance.ts` |
| `./errors` | `./src/errors.ts` |
| `./event-schema` | `./src/event-schema.ts` |
| `./mcp/tool-names` | `./src/mcp/tool-names.ts` |
| `./sdk-version` | `./src/sdk-version.ts` |
| `./tool-catalog` | `./src/tool-catalog.ts` |
| `./tool-descriptor` | `./src/tool-descriptor.ts` |
| `./transcript-replay` | `./src/transcript-replay.ts` |
| `./types` | `./src/types.ts` |
| `./package.json` | `./package.json` |

## Version And Registry Constants

| Constant | Current value | Source |
|---|---|---|
| `FLOW_A_CONTRACT_VERSION` | `TBD_BY_TIER_0` | `frontend/packages/harness-contract/src/sdk-version.ts` |
| `CLAUDE_AGENT_SDK_PACKAGE_VERSION` | `0.3.150` | `frontend/packages/harness-contract/src/sdk-version.ts` |
| `HARNESS_TOOL_REGISTRY_VERSION` | `harness-tools.v6.mutating-mcp` | `frontend/packages/harness-contract/src/tool-descriptor.ts` |

## Shim And Importer Baseline

The extraction keeps the in-repo harness paths as compatibility shims. As of this record, the direct package imports under `frontend/src` are confined to those shim files; non-shim frontend code still imports the app-dev harness paths.

| Measurement | Result |
|---|---|
| Contract shim files under `frontend/src/lib/harness/` | 10 files re-export package surfaces |
| Non-shim files under `frontend/src` importing through `lib/harness` paths | 64 total |
| Importer distribution | 45 tests, 10 app route files, 9 components |
| Non-shim files under `frontend/src` importing `@chirality/harness-contract` directly | 0 |

The retained shim posture is intentional for this tranche. Shim migration and wrapper retirement are outside this brief and remain owner-gated follow-on work.

## Residual Gates

- Package publication / F2 crossing: not authorized by D-APP-45 or D-APP-46.
- F3 live-binding opening: still gated by the tier-0 D-T0-08 sequence and app-dev F3 disposition.
- Piping-side D-22 consumption: still gated by DEC-041 automation and a lawful piping vehicle.
- Flow-A version settlement: still tier-0-owned; app-dev records `TBD_BY_TIER_0`.
- DEL-03-01 lifecycle: remains CHECKING; any CHECKING->ISSUED transition is human-only.
