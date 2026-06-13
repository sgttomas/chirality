# NEXT INSTANCE STATE - Chirality App Dev

**Last Updated:** 2026-06-13
**Updated By:** Codex WORKING_ITEMS governance planning migration tranche
**Active persona:** `WORKING_ITEMS`
**Status:** Compact coordination state; not substitute authority.

## Current Pointers

| Artifact | Path |
|---|---|
| Coordination policy | `execution/_Coordination/_COORDINATION.md` |
| Stable startup prompt | `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` |
| Human decision register | `execution/_Coordination/_DECISIONS/_REGISTER.md` |
| Product requirements | `docs/PRD.md` |
| Strategic roadmap | `docs/PLAN.md` |
| Validation strategy | `docs/VALIDATION_STRATEGY.md` |
| Release quality gates | `docs/RELEASE_QUALITY_GATES.md` |
| Active runtime completion plan | `plans/PLAN_2026-06-13_runtime_completion.md` |
| Runtime completion log | `plans/PLAN_COMPLETION_LOG.md` |
| Runtime contract | `frontend/docs/harness/runtime_engine_contract.md` |
| Seed runtime roadmap | `plans/chirality-app-future-development-plan.md` |
| Claude SDK follow-ups | `plans/claude-agent-sdk-implementation-followups.md` |
| Pi assessment | `plans/pi-agent-harness-assessment.md` |

## Current Direction

The active direction is app-integration work on the Chirality harness runtime:

- preserve Chirality-owned contracts and governance;
- continue the Claude Agent SDK path where it satisfies the runtime contract;
- borrow Pi patterns selectively for event/session/tool architecture;
- prepare Pi package import or adapter work only after contract hardening, conformance tests, and human rulings exist;
- keep production domain workflows under Chirality-owned profile, proposal, adapter, audit, and human-gate contracts.

## Active Queue

Recommended next unblocked plan items, in order:

1. **Permission overlay skeleton.** Define `HarnessPermissionDecision` and deny-first, mode-aware permission resolution against descriptor metadata before enabling read-tool execution.
2. **SDK read-tool exposure behind deny-first policy.** Enable only read-class SDK built-ins after the overlay exists.
3. **Read MCP / descriptor integration.** Add Chirality-owned read MCP descriptors without write capability.

Human-requested governance-support follow-up, if continuing the migration lane: **Build/release skeleton.** Add app-dev `docs/BUILD_AND_RELEASE.md` without changing application code or package scripts.

## Pending Human Rulings

See `execution/_Coordination/_DECISIONS/_REGISTER.md`.

Current known pending questions:

- whether to approve any future Pi-backed adapter spike;
- whether to raise runtime requirements or use a sidecar if Pi packages are ever imported;
- whether to broaden network/provider policy beyond the current Anthropic-centered runtime scope.

## Update Protocol

Update this file only when:

- active pointers change;
- the active queue changes;
- a human ruling changes scope;
- a new blocker is discovered;
- pending-ruling summary changes.

Do not store landed-tranche narrative history here. Use `plans/PLAN_COMPLETION_LOG.md` for landed-tranche narrative and `plans/PLAN_2026-06-13_runtime_completion.md` for compressed plan rows.
