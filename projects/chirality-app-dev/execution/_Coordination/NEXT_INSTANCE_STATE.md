# NEXT INSTANCE STATE - Chirality App Dev

**Last Updated:** 2026-06-13
**Updated By:** Codex WORKING_ITEMS HarnessEvent expansion tranche
**Active persona:** `WORKING_ITEMS`

## Current Pointers

| Artifact | Path |
|---|---|
| Coordination policy | `execution/_Coordination/_COORDINATION.md` |
| Stable startup prompt | `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` |
| Human decision register | `execution/_Coordination/_DECISIONS/_REGISTER.md` |
| Product requirements | `docs/PRD.md` |
| Strategic roadmap | `docs/PLAN.md` |
| Runtime contract | `frontend/docs/harness/runtime_engine_contract.md` |
| Current completion plan | `plans/chirality-app-future-development-plan.md` |
| Claude SDK follow-ups | `plans/claude-agent-sdk-implementation-followups.md` |
| Pi assessment | `plans/pi-agent-harness-assessment.md` |

## Current Program State

The active direction is app-integration work on the Chirality harness runtime:

- preserve Chirality-owned contracts and governance;
- continue the Claude Agent SDK path where it satisfies the runtime contract;
- borrow Pi patterns selectively for event/session/tool architecture;
- prepare Pi package import or adapter work only after contract hardening and conformance tests exist;
- keep production domain workflows under Chirality-owned profile, proposal, adapter, audit, and human-gate contracts.

Recent assessment artifacts added:

- `plans/pi-agent-harness-assessment.md`
- `plans/pi-assessment/01_core_session_primitives.md`
- `plans/pi-assessment/02_backend_adapter_feasibility.md`
- `plans/pi-assessment/03_security_governance_fit.md`
- `plans/pi-assessment/04_domain_harness_fit.md`
- `plans/pi-assessment/05_license_maintenance.md`

Completed app-integration tranche:

- 2026-06-13: Provider-neutral runtime contract cleanup. Persisted `HarnessEvent` type names were generalized away from SDK-prefixed names, SDK identifiers remain adapter metadata, `engineSessionId` was added as a provider-neutral compatibility alias, and validation defaults were repaired for the nested app-dev workspace layout.
- 2026-06-13: Turn lifecycle extraction. Added product-owned `TurnEngine` for pre-stream turn preflight, same-session locking, attachment/governance shaping, adapter stream execution, session metadata persistence, cancellation delegation, and mid-stream terminal error mapping while preserving `/api/harness/turn` SSE behavior.
- 2026-06-13: HarnessEvent expansion. Added provider-neutral persisted event categories for message, tool, hook, queue, branch, interruption, compaction, and subagent lifecycle coverage; expanded Claude Agent SDK message mapping for deterministic runtime evidence while preserving public browser SSE event names.

## Active Queue

Recommended next unblocked tranches, in order:

1. **Engine conformance fixtures.** Add deterministic adapter conformance tests using fake/scripted provider streams before any new backend adapter.
2. **Tool descriptor design.** Define a Chirality-owned `HarnessToolDescriptor` and permission metadata before enabling additional tool execution.
3. **Pi adapter spike packet.** Prepare a constrained `pi-ai` / `pi-agent-core` sidecar spike brief after the contract and conformance prerequisites are in place.

## Pending Human Rulings

See `execution/_Coordination/_DECISIONS/_REGISTER.md`.

Current known pending questions:

- whether to approve any future Pi-backed adapter spike;
- whether to raise runtime requirements or use a sidecar if Pi packages are ever imported.

## Update Protocol

Update this file only when:

- the active queue changes;
- a human ruling changes scope;
- a tranche completes and changes the recommended next action;
- a new blocker is discovered.

Project truth remains governed docs, source, tests, and git-tracked artifacts.
