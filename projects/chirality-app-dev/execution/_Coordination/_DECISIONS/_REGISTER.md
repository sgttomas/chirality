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

## Decision Preparation Rules

- Prepare a packet only when the selected tranche is blocked by the decision.
- Keep packets under `execution/_Coordination/_DECISIONS/`.
- Label packets `PROPOSAL`.
- Include options, recommendation, risks, validation implications, and affected files.
- Treat approval as recorded only when a ruling record is added.
- `RULED` decisions remain subject to their ruling record. Do not infer broader implementation approval than the ruling text grants.
