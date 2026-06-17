# Human Decision Register - Chirality App Dev

**Created:** 2026-06-13
**Status:** Non-governing tracking surface.

This register tracks human-gated decisions for the active app-integration loop. Agents may prepare decision packets labeled `PROPOSAL`; only the human project authority rules. Authority remains with `docs/PRD.md`, `docs/PLAN.md`, source code, tests, and git history.

**Row states:** `NOT_PREPARED` -> `AWAITING_RULING` -> `RULED`.

| ID | Decision | Blocks | State | Packet | Ruling record |
|---|---|---|---|---|---|
| D-APP-01 | Whether Pi should be treated as adapter/fork/import/spike scope or as a pattern corpus only | Any Pi adapter, fork, package import, sidecar, or spike work | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-01_RULING_2026-06-13.md` |
| D-APP-02 | If Pi packages are imported, choose runtime strategy: raise Chirality runtime floor to Node `>=22.19.0` or isolate Pi behind a Node 22 sidecar | Any direct Pi package dependency or Node 22 sidecar/runtime-floor change for Pi | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-02_RULING_2026-06-13.md` |
| D-APP-03 | Whether to broaden runtime strategy beyond the current shipped Anthropic path toward provider-adapter generality | Any concrete non-Anthropic shipped backend adapter or provider routing | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md` |
| D-APP-04 | Which post-write runtime capability lane, if any, is approved next: Bash, governed SDK subagents, or concrete provider expansion preparation | Bash exposure, governed SDK subagent execution, and concrete non-Anthropic provider implementation/routing after `WRITE-HOOKS-001` | RULED | `execution/_Coordination/_DECISIONS/D-APP-04_PACKET_2026-06-15.md` | `execution/_Coordination/_DECISIONS/D-APP-04_RULING_2026-06-15.md` |
| D-APP-05 | Whether to approve bounded R5 governed SDK subagent runtime after landed R4 Bash | SDK `Agent` tool exposure, executable SDK `agents` definitions, and governed subagent runtime execution | RULED | `execution/_Coordination/_DECISIONS/D-APP-05_PACKET_2026-06-15.md` | `execution/_Coordination/_DECISIONS/D-APP-05_RULING_2026-06-15.md` |
| D-APP-06 | Whether to approve bounded executable R5 governed subagent runtime after landed provider-neutral contract prerequisite | Model-visible SDK `Agent` tool execution, executable SDK `agents` definitions, child turn execution, and executable child output artifacts | RULED | `execution/_Coordination/_DECISIONS/D-APP-06_PACKET_2026-06-15.md` | `execution/_Coordination/_DECISIONS/D-APP-06_RULING_2026-06-15.md` |
| D-APP-07 | Whether the residual six-node SCC blocks executable R5, blocks only project-wide dependency closure claims, or requires dependency/decomposition amendment before R5 can proceed | Executable R5 selection after the RECONCILIATION SCC package | RULED | `execution/_Coordination/_DECISIONS/D-APP-07_PACKET_2026-06-15.md` | `execution/_Coordination/_DECISIONS/D-APP-07_RULING_2026-06-16.md` |
| D-APP-08 | Whether to approve bounded executable R5 governed subagent implementation after D-APP-07 Option B | Model-visible SDK `Agent`, executable SDK `agents`, child turn execution, and child output artifacts | RULED | `execution/_Coordination/_DECISIONS/D-APP-08_PACKET_2026-06-16.md` | `execution/_Coordination/_DECISIONS/D-APP-08_RULING_2026-06-16.md` |
| D-APP-09 | Which post-design R5 slice path is approved after R5-DESIGN-001 | R5-SLICE-001 through R5-SLICE-006 source implementation selection, including any SDK `agents`, SDK `Agent`, child turn, or child output artifact work | RULED | `execution/_Coordination/_DECISIONS/D-APP-09_PACKET_2026-06-16.md` | `execution/_Coordination/_DECISIONS/D-APP-09_RULING_2026-06-16.md` |
| D-APP-10 | Which post-bridge R5 continuation path is approved after R5-BRIDGE-001 | R5-SLICE-004 through R5-SLICE-006 continuation selection, including parent-child lifecycle events, child output artifact references, SDK `Agent`, executable SDK `agents`, and child turn work | RULED | `execution/_Coordination/_DECISIONS/D-APP-10_PACKET_2026-06-16.md` | `execution/_Coordination/_DECISIONS/D-APP-10_RULING_2026-06-16.md` |
| D-APP-11 | Whether to accept the Runtime Stabilization program (`plans/PLAN_2026-06-16_runtime_stabilization.md`, STAB-00..06) as the active development queue after the six-node SCC plan closed | Selection of the runtime stabilization plan as the active queue; re-pointing of `_COORDINATION.md` / `NEXT_INSTANCE_PROMPT.md` / `_LATEST.md` | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-11_RULING_2026-06-16.md` |
| D-APP-12 | Whether to cut the default provider over from the current default to the SDK-backed Anthropic path (`agentSdk`) | Any change making `agentSdk` the default provider; any governance text declaring the SDK the active default | RULED | `execution/_Coordination/_DECISIONS/D-APP-12_PACKET_STAB02D_PROOF_2026-06-17.md` | `execution/_Coordination/_DECISIONS/D-APP-12_RULING_STAB02D_PROOF_2026-06-17.md` |
| D-APP-13 | Whether to expose bounded mutating Chirality MCP tools (`status_transition`, `deps_write`) from descriptor metadata-only to `workspaceWrite`-gated, including whether the MCP tool may perform human-gated (`CHECKING`/`ISSUED`) transitions given an `approvalSha` and the required actor identity | STAB-04 mutating Chirality MCP implementation | RULED | `execution/_Coordination/_DECISIONS/D-APP-13_PACKET_2026-06-16.md` | `execution/_Coordination/_DECISIONS/D-APP-13_RULING_2026-06-16.md` |
| D-APP-14 | Whether to accept the R6 Extensibility & MCP Boundary Maturity program (`plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, R6-01..R6-05) as the active development queue after the Runtime Stabilization program closed | Selection of the R6 plan as the active queue; re-pointing of `_COORDINATION.md` / `NEXT_INSTANCE_PROMPT.md` / `_LATEST.md` | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-14_RULING_2026-06-17.md` |

## Decision Preparation Rules

- Prepare a packet only when the selected tranche is blocked by the decision.
- Keep packets under `execution/_Coordination/_DECISIONS/`.
- Label packets `PROPOSAL`.
- Include options, recommendation, risks, validation implications, and affected files.
- Treat approval as recorded only when a ruling record is added.
- `RULED` decisions remain subject to their ruling record. Do not infer broader implementation approval than the ruling text grants.
