# D-PEC-56 — Shared Runtime Agent Migration

**Status:** RULED 2026-07-22
**Decision ID:** D-PEC-56
**Owner:** Ryan Tufts
**Tier-0 companion:** D-T0-23

## Owner direction

The owner supplied the decision-complete Shared Runtime and Local-Agent Pilot and explicitly instructed:

> PLEASE IMPLEMENT THIS PLAN

This packet records the PEC-local effect.

## Ruled behavior

1. Retain PEC’s deterministic acts, RBAC, reporting, domain tools, human-only acts, and data-boundary enforcement as a project adapter service.
2. Remove independent LLM, credential, session, delegation, interruption, and model-residency ownership from the PEC agent path.
3. Connect the PEC backend and embedded panel to the root shared runtime through the registered project-scoped client and canonical event protocol.
4. Retain the old PEC agent endpoint as a compatibility proxy for one migration cycle only. It must not run a second production execution loop.
5. Preserve live event visibility, act-budget evidence, canonical parentage, replay, redaction, and actual engine/provider/model attribution through the daemon path.
6. Validate the migration only with scratch/demo data.
7. Keep all accept/apply/reject-of-others/`force`/conversion-disposition and other human-only acts unavailable to agents.

## Historical decisions preserved

D-PEC-16 through D-PEC-22 and D-PEC-53 remain historical evidence for the built-in agent UI and prototype sidecar. Their independent runtime-ownership assumptions are prospectively replaced only by this migration. Their tool, RBAC, visibility, disclosure, and human-act restrictions remain unless explicitly superseded.

D-PEC-49 remains `AWAITING_RULING`. D-PEC-55’s pending T0 product-and-authority rebaseline remains open. No production PEC data or mutation authority is created.

## Acceptance boundary

The PEC pilot must traverse daemon, project adapter, backend proxy, and embedded UI; prove there is one execution loop and one turn-lock/session owner; and show RBAC still denies forbidden human acts. Failure of the daemon or adapter fails agent execution closed without altering deterministic PEC state.

## Exact exclusions

No source implementation is performed by this governance ruling. No database, fixture, production record, import, report, lifecycle, release, publication, or professional-reliance state changes.
