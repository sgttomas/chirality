# D-PEC-16 - PROPOSAL: the built-in agent UI in pec — design gate

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-16
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: the design-gate shape of
`D-PEC-07_embedded_upload_agent_pathway.md` (pathway ruling → adopted design
brief → separate source-tranche row), which this row extends to the full
agent UI.

## Why this row exists now

Owner direction of record (2026-07-05, in-session, Ryan Tufts, verbatim):

> the pec ↔ chirality-app-dev bridge is my top priority for both projects: a
> fully functioning bridge, with a built-in agent UI in pec. This session is
> detailed planning ONLY — prepare the tier-0 decision packet(s) and the
> design brief(s) for the lane and stop at every gate; no source tranche in
> either project this run.

The built-in agent UI is the second half of that direction, and the standing
workflow it serves is already ruled: D-PEC-10 O-A makes the agent "the primary
means of making updates" on a weekly five-document cycle, with the human making
"targeted changes within the current screen" — but pec's web UI has **no agent
surface today** (verified 2026-07-05: no chat/agent/LLM component under
`web/src/`). The adopted upload-agent design brief
(`_DomainEngines/proposals/pec/BRIEF_2026-07-05_embedded_upload_agent_design.md`,
adopted with the RV-12 rider) sketches the in-app upload→proposal seam but is
silent on the agent's runtime host and carries no UI design. The CANDIDATE
brief this row gates is
`_DomainEngines/proposals/pec/BRIEF_2026-07-05_pec_builtin_agent_ui_design.md`.

## Decision to rule

Whether to adopt the CANDIDATE built-in-agent-UI design brief as the governing
design for the pec agent surface, and which agent-runtime option it proceeds
under.

## What adoption changes (and what it does not)

Changes: the brief becomes the adopted design basis; the next lawful step is a
source-tranche row (D-PEC-17-to-be) with an exact file fence under
`projects/pec/{server,web,core}/**`, per the D-PEC-08 precedent.

Does NOT change: adoption authorizes **no implementation** (the D-PEC-07 S-3
adoption-rider precedent — the F-PEC-1 fence stays closed until a ruled
tranche); accept/apply/`force` remain human screen acts (`import.accept`
admin-only; K-DOMAIN-3); the agent actor model stays the D-PEC-10 shape (own
person record, `is_admin=0`, role-bounded); LLM visibility of real instance
content stays governed by tier-0 `D-T0-20` (residual of D-T0-14) — under
CLOSED the UI's LLM features run only on synthetic/demo bases or degrade to
the deterministic mapper; ADR-002's zero-runtime-dependency posture for the
server package is a design constraint the brief must satisfy, not a thing this
row may waive.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Adopt the brief with runtime **RT-B (local sidecar)**: a separate local Node process (free to use the Claude Agent SDK and the app-dev `harness-contract` packages) drives pec exclusively through the RBAC'd HTTP API as the provisioned agent person; the pec web UI gains an agent panel that talks to the sidecar; the pec server package stays zero-dependency. | Richest agent soonest; one engine-side seam shared with the `D-T0-19` bridge; the SDK dependency lives outside the pec server package (ADR-002 intact); the sidecar's packaging/start story is a tranche-level design item. |
| O-B | Adopt the brief with runtime **RT-A (in-server, zero-dep)**: a hand-rolled `node:https` Anthropic API client inside the pec server, streaming to the web UI. | Truly single-process "built-in", ADR-002 intact by construction — but re-implements session/tool-loop/streaming plumbing the SDK already provides; slower to useful, more surface to test. |
| O-C | Defer or redirect (e.g., treat the app-dev harness UI as the only agent surface). | The bridge half proceeds alone; the "built-in agent UI in pec" end goal has no design of record. |
| O-D | Adopt the brief; defer the runtime choice (RT-A vs RT-B) to the source-tranche row, where concrete packaging facts are in front of the owner. | Design of record now, runtime commitment later — the D-APP-50 "transport settles in-tranche" precedent; the tranche packet must then carry the runtime decision explicitly. |

## Recommendation (non-binding)

O-A. The owner's ruled priority is a *useful agent* (D-PEC-12 amendment:
"focus on making a useful agent for now"); RT-B reaches useful fastest while
keeping every governance property structural: the sidecar holds no special
power — it is just another RBAC-bounded API client, so the UI, the harness
bridge, and the loop agents all converge on the same audited seam. O-D is a
sound second choice if the owner prefers ruling the runtime with the tranche
packet's packaging facts in view.

## On ruling (mechanism)

Record the ruling verbatim here and in the register row. O-A/O-B/O-D: the
brief's status moves CANDIDATE → ADOPTED with the runtime choice (or its
O-D deferral-to-tranche) recorded and any owner riders appended; a new row
(D-PEC-17-to-be) opens NOT_PREPARED for the source-tranche authorization; no
source change until that row rules. O-C: the brief stays CANDIDATE (or is
withdrawn) and the row closes with the ruling recorded.

## Human ruling

**Ruling:** —

**Ruling SHA:** TBD at publication commit.
