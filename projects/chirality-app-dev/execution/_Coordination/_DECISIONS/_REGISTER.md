# Human Decision Register - Chirality App Dev

**Created:** 2026-06-13
**Status:** Non-governing tracking surface.

This register tracks human-gated decisions for the active app-integration loop. Agents may prepare decision packets labeled `PROPOSAL`; only the human project authority rules. Authority remains with `docs/PRD.md`, `docs/PLAN.md`, source code, tests, and git history.

**Row states:** `NOT_PREPARED` -> `AWAITING_RULING` -> `RULED`.

| ID | Decision | Blocks | State | Packet | Ruling record |
|---|---|---|---|---|---|
| D-APP-01 | Whether to approve a constrained Pi-backed backend-adapter spike after runtime contract hardening and conformance fixtures exist | Any implementation of `pi-ai` / `pi-agent-core` adapter work | NOT_PREPARED | - | - |
| D-APP-02 | If Pi packages are imported, choose runtime strategy: raise Chirality runtime floor to Node `>=22.19.0` or isolate Pi behind a Node 22 sidecar | Any direct Pi package dependency | NOT_PREPARED | - | - |
| D-APP-03 | Whether to broaden network/provider policy beyond the current Anthropic-centered runtime scope | Any non-Anthropic shipped backend adapter or provider routing | NOT_PREPARED | - | - |

## Decision Preparation Rules

- Prepare a packet only when the selected tranche is blocked by the decision.
- Keep packets under `execution/_Coordination/_DECISIONS/`.
- Label packets `PROPOSAL`.
- Include options, recommendation, risks, validation implications, and affected files.
- Treat approval as recorded only when a ruling record is added.
