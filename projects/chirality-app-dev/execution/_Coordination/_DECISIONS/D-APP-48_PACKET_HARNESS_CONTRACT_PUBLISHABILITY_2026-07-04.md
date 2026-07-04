# D-APP-48 - RULING: Harness-contract publishability mechanism

**Status:** RULED / Option A selected 2026-07-04.
**Date prepared:** 2026-07-04
**Decision ID:** D-APP-48
**Prepared by:** bridge work loop agent, at owner direction to prepare and execute all agent-lawful coordination/control work on D-APP-48.
**Structural precedent:** Follows the D-APP-45/D-APP-46 packet pattern for cross-repo Flow-A package-boundary decisions that cite DEC-041 without copying piping authority.

This packet chooses a mechanism only. It does not publish a package, change the
package version, set the Flow-A contract value, consume anything from piping,
open F2/F3, advance lifecycle state, or create release, professional,
certification, sealing, authentication, or code-compliance claims.

## Decision to rule

Choose how `@chirality/harness-contract` becomes a consumable,
highly-automated, SHA-pinned package pull satisfying the DEC-041 no-manual-toil
condition.

## Verified basis

| Fact | Source |
|---|---|
| The package exists in the app-dev frontend workspace as `@chirality/harness-contract`, version `0.0.0-private`, `private: true`, with file-workspace wiring from the app frontend. | `projects/chirality-app-dev/frontend/package.json`; `projects/chirality-app-dev/frontend/packages/harness-contract/package.json` |
| The package exports the dependency-free contract spine. D-T0-09 now rules `FLOW_A_CONTRACT_VERSION = 'flow-a.contract.v0.1.0'`; the referenced constants remain `CLAUDE_AGENT_SDK_PACKAGE_VERSION = '0.3.150'` and `HARNESS_TOOL_REGISTRY_VERSION = 'harness-tools.v6.mutating-mcp'`. | `_DomainEngines/_DECISIONS/D-T0-09_flow_a_contract_version_value.md`; `projects/chirality-app-dev/frontend/packages/harness-contract/src/sdk-version.ts`; `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts` |
| DEC-041 requires the dependency to be consumable as a highly-automated package pull and not require laborious manual cross-repo/cross-session coordination. | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-041 |
| D-APP-48 blocks piping D-30 consumption execution. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md` |
| Package publication / external distribution is a hard-fence concern under the bridge plan unless separately ruled. | `_DomainEngines/bridge/WORKPLAN_2026-07-02_bridge_loop.md` |

## Options

| ID | Option | Consequence |
|---|---|---|
| **O-A** | **Intra-repo SHA-pinned pull mechanism.** Keep `private: true`; define a governed pull contract that pins repo commit SHA, package path, package name, Flow-A contract version, and validation commands. Piping consumes by deterministic repo/path/SHA metadata, not by registry publication. | Satisfies the no-manual-toil condition without crossing F2. Best fit for the current monorepo and current private package posture. Requires a small manifest/validator implementation in later execution work. |
| **O-B** | **Private registry publication.** Publish the package to a private registry with auth and SHA/provenance metadata. | Strong package semantics, but publication/distribution and credential handling require an F2 proposal/ruling before execution. |
| **O-C** | **Public registry publication.** Publish a public package. | Strong external consumption story, but plainly crosses F2 and creates release/distribution governance obligations. |
| **O-D** | **Defer.** Keep only the current workspace file dependency. | Leaves DEC-041 automation unsatisfied and keeps D-30 blocked. |

## Recommendation

Recommend **O-A**.

O-A is the smallest mechanism that satisfies DEC-041's automation requirement
without claiming publication, distribution, release readiness, or external
package availability. It also keeps the package version truthfully private
until the owner separately opens an F2 publication lane.

## Proposed O-A pull contract

If O-A is ruled, the implementing work should create a machine-checkable record
with at least:

- source repository and commit SHA;
- package path `projects/chirality-app-dev/frontend/packages/harness-contract`;
- package name `@chirality/harness-contract`;
- package version as currently private, unless separately changed;
- `FLOW_A_CONTRACT_VERSION` from D-T0-09 once ruled;
- referenced `CLAUDE_AGENT_SDK_PACKAGE_VERSION` and `HARNESS_TOOL_REGISTRY_VERSION`;
- dependency-free lint command;
- package export list and checksum/provenance evidence.

The consuming piping work should be able to validate that record without asking
the owner to manually copy package files between sessions.

## Scope constraints

- O-A does not publish or distribute anything externally.
- O-A does not open F3, add domain MCP tools, add protected-path hooks, or bind a
  live agent.
- O-A does not decide the concrete Flow-A value; D-T0-09 owns that.
- O-A does not itself consume the package in piping; D-30 owns that after its
  prerequisites are resolved.

## Human ruling

**Ruling recorded:** O-A approved by owner (Ryan Tufts), 2026-07-04.

Ruling record:
`execution/_Coordination/_DECISIONS/D-APP-48_RULING_2026-07-04.md`.
