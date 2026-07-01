# D-APP-46 — PROPOSAL: Extract the dependency-free harness contract package (DEC-041 keystone)

**Status:** PROPOSAL / `AWAITING_RULING` (execution greenlight). Within-fence (no F-crossing); surfaced for owner sequencing rather than because a fence requires a ruling.
**Date:** 2026-06-24
**Decision ID:** D-APP-46
**Persona:** WORKING_ITEMS
**Companion hygiene:** `plans/artifacts/handoff_tier0_governance_residual_cleanup_2026-06-24.md` (tier-0 residuals, hand-off only)

## Decision to rule

Authorize execution of the **GREEN, within-fence** internal extraction of the dependency-free harness
**contract spine** out of `frontend/src/lib/harness/` into a separate, dependency-free internal package — the
**keystone** of the DEC-041 "harness-as-versioned-packages" posture (`projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611`) —
including the required `event-schema.ts` / `tool-descriptor.ts` pure/impure split, **without** crossing any
hard fence.

This is the app-dev-side **Action 1** from `plans/artifacts/bridge_appdev_contribution_for_tier0_2026-06-21.md:149`
("Extract harness lib into a dependency-free **internal** monorepo package — GREEN, prep today"). Per the
D-APP-39 decision-latitude model, Action 1 is autonomous within the fences; this packet exists because the
extraction is (a) a material structural refactor and (b) the load-bearing capability for eventual cross-repo
consumption, so the precise fence-scoping is surfaced to the owner **before code lands**. It is **not** a
fence amendment and claims no ruling or approval-SHA.

## Why now (motivation, traceable to the readiness assessment)

The readiness assessment found that the decisive gap between today and a live harness is **capability, not
posture**: a real in-process runtime exists, but there is **no headless/versioned consumption surface** —
`frontend/package.json` is `private:true` with no `packages/`, no workspaces, no `bin`. Until a publishable,
dependency-free contract package exists, the DEC-041 "highly-automated package pull, no manual toil"
condition cannot be met, and a "proven L2" (the precondition for opening F3 per D-T0-08) cannot be reached.
This extraction is the lowest-governance, highest-leverage first concrete step and crosses no fence.

## Upstream basis verified from source

| Fact | Source |
|---|---|
| DEC-041 keystone = "the ~19 dependency-free harness lib files … as the keystone dependency"; execution condition = "consumable as a highly-automated package pull … must NOT require laborious manual cross-repo/cross-session coordination". | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611` |
| Action 1 (internal extraction) is fence-free / GREEN; Action 2 (external publish) = F2; Action 3/4 (source types / domain MCP) = F3; Action 5 (live binding / egress) = F1; Action 6 (`CHECKING→ISSUED`) = F4. | `plans/artifacts/bridge_appdev_contribution_for_tier0_2026-06-21.md:147-154` |
| The import-graph-derived dependency-free spine: 8 ship-as-is files + 2 requiring a pure/impure split. Global scan: 1 Next import (`http.ts`), zero React/Electron in the lib, Agent SDK in 8 (runtime) files, `node:` in 24. | `plans/artifacts/bridge_appdev_contribution_for_tier0_2026-06-21.md:48-72` |
| `HARNESS_EVENT_TYPES` enumerates **43** members (last = `runtime.mirror.error`), **not 42** as the bridge artifact and piping DEC-041 state. | `frontend/src/lib/harness/event-schema.ts:3-46` (verified cold 2026-06-24) |
| K-ENGINE-6: app-dev is a governance/UI/audit/lifecycle/adapter layer, **not a standalone general agent harness** — the extracted package must stay an adapter/contract, not become a competing harness. | `docs/CONTRACT.md:57` |
| The cross-repo Flow-A contract **version** is tier-0-owned and still `TBD_BY_TIER_0` (D-APP-45 AWAITING_RULING). | `execution/_Coordination/_DECISIONS/D-APP-45_PACKET_FLOW_A_VERSIONING_AND_PKG10_CANON_CONFORMANCE_2026-06-22.md:34` |

## The extraction set (contract = dependency-free)

**Ship as-is (no React/Next/Electron/Node/SDK):**

| File | Provides |
|---|---|
| `frontend/src/lib/harness/types.ts` | Spine: `UIEvent` public union, request/response/session/opts interfaces, `IAgentSdkManager`. |
| `frontend/src/lib/harness/agent-engine-port.ts` | `AgentEnginePort`, `PUBLIC_UI_EVENT_NAMES` — the surface piping drives. |
| `frontend/src/lib/harness/engine-conformance.ts` | `runEngineConformance` / `runEngineInterruptConformance`. |
| `frontend/src/lib/harness/tool-catalog.ts` | `renderHarnessToolCatalog()` (pure markdown). |
| `frontend/src/lib/harness/mcp/tool-names.ts` | MCP naming contract (zero imports). |
| `frontend/src/lib/harness/sdk-version.ts` | `CLAUDE_AGENT_SDK_PACKAGE_VERSION = '0.3.150'`. |
| `frontend/src/lib/harness/errors.ts` | `HarnessError`, `asHarnessError`. |
| `frontend/src/lib/harness/transcript-replay.ts` | Pure persisted-events → `TranscriptView`. |

**Pure/impure SPLIT before shipping as contract:**

| File | Pure part (→ contract package) | Impure part (stays runtime-side) |
|---|---|---|
| `event-schema.ts` | `HARNESS_EVENT_TYPES` (**43**), `HarnessEventType`, `HarnessEvent` | `createHarnessEvent` (uses `node:crypto` `randomUUID`) — move out or inject id |
| `tool-descriptor.ts` | `HarnessToolDescriptor` + type vocab, `HARNESS_TOOL_DESCRIPTORS`, lookups | `resolveHarnessToolPool` (pulls SDK + `node:` deps) |

**Explicitly NOT contract material (runtime/adapter side, unchanged):** `sdk-options-builder.ts` and its
transitive impure deps (`permission-overlay`, `chirality-hooks`, `permission-broker`, `mcp/read-tools`,
`subagent-bridge`, `session-events`). The package **calls** these; it does not re-implement them.

## Options

- **Option A (recommended) — Execute the internal extraction now, as scoped above.** Create a
  dependency-free internal package, perform the pure/impure split, re-export from the in-repo harness for
  back-compat, keep the conformance suite green. Stamp the package's cross-repo version field
  `FLOW_A_CONTRACT_VERSION: TBD_BY_TIER_0` (pending D-APP-45 / D-T0-07) — do **not** invent a version.
- **Option B — Defer until tier-0 rules the Flow-A version (D-APP-45).** Extract only after the version is
  settled so the package is version-stamped at creation. Cost: holds the load-bearing capability behind a
  tier-0 ruling it does not technically require (the version is metadata; the file boundary is not).
- **Option C — Do nothing; keep the harness lib in-tree.** Revisit at live-binding. Cost: DEC-041 automation
  stays impossible; no proven L2 reachable; F3 stays transitively blocked.

**Recommendation: A.** It is reversible (an internal refactor behind re-exports), crosses no fence, and is
the single precondition shared by DEC-041 automation and a proven L2. The version is metadata that can be
filled when D-APP-45/D-T0-07 lands; the package boundary need not wait on it.

## Scope of the ruling (what it does NOT authorize)

- **No F2 crossing.** No external publication or distribution of the package. It is an **internal** package
  only; `private:true` stays until a separate F2 PROPOSAL.
- **No F3 crossing.** No `DomainEngineProfile` / `OperationProposal` **source types**, no protected-path
  hooks, no domain MCP tools (e.g. `piping_propose_operation`). PKG-10 stays doc-only.
- **No F1 crossing.** No live binding, no non-Anthropic provider wiring, no private-data egress. The renderer
  network posture is untouched (Anthropic key-aware loopback default).
- **No F4 crossing.** No `CHECKING→ISSUED` issuance; deliverable states are unchanged.
- **No cross-repo coupling.** No piping-side dependency is declared, no `@chirality` publish, no automated
  pull is built; this packet does not make piping consume anything. Those are downstream, separately gated.
- **K-ENGINE-6 preserved.** The package is an adapter/contract surface, not a standalone agent harness.

## Validation implications

- The new package MUST build with zero React/Next/Electron/Node/SDK imports (CI gate: a dependency-lint over
  the package's `import` graph).
- The impure members (`createHarnessEvent`, `resolveHarnessToolPool`) move to the runtime side; callers are
  rewired; the in-repo `frontend/src/lib/harness/` re-exports the package symbols so existing imports keep
  working (no behavior change).
- The existing conformance suite (`engine-conformance.ts`) MUST still pass against the runtime port.
- The keystone event vocabulary is reconciled to **43** at extraction (see companion hygiene fix), so any
  future Flow-A version pins against the true count.

## Affected files (PROPOSAL — not applied by this packet)

> This packet **does not** perform the extraction. It records the scope for owner greenlight. On A, the
> implementing tranche would touch: a new internal package directory (e.g. `frontend/packages/harness-contract/`
> or a workspace package), `frontend/package.json` (workspaces wiring, `private` unchanged), `tsconfig`
> path/project references, the 8 ship-as-is files (moved + re-exported), the 2 split files, and the runtime
> callers of the two impure members. No `docs/*` authority doc is edited, so no D-APP-38 corpus bump is triggered.

## Agent decisions recorded by WORKING_ITEMS

- Scoped Action 1 to the **internal** package only, holding the F1/F2/F3/F4 lines explicitly (decision
  latitude; recorded, not self-ruled as an owner ruling).
- Chose to stamp `FLOW_A_CONTRACT_VERSION: TBD_BY_TIER_0` rather than invent a version (truthful attribution;
  the version is tier-0-owned).
- Surfaced as a PROPOSAL packet despite being within-fence, so the owner can sequence it against D-APP-45 and
  the piping R4-exit hold.
