# NEXT INSTANCE STATE - Chirality App Dev

**Last Updated:** 2026-06-13
**Updated By:** Codex WORKING_ITEMS runtime-contract tranche
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

## Active Queue

Recommended next unblocked tranches, in order:

1. **Turn lifecycle extraction.** Continue moving route-owned lifecycle into a product-owned `TurnEngine` while preserving the existing SSE event contract.
2. **HarnessEvent expansion.** Add Chirality-owned message/tool/queue/compaction/interruption event coverage inspired by Pi's lifecycle.
3. **Engine conformance fixtures.** Add deterministic adapter conformance tests using fake/scripted provider streams before any new backend adapter.
4. **Tool descriptor design.** Define a Chirality-owned `HarnessToolDescriptor` and permission metadata before enabling additional tool execution.
5. **Pi adapter spike packet.** Prepare a constrained `pi-ai` / `pi-agent-core` sidecar spike brief after the contract and conformance prerequisites are in place.

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
