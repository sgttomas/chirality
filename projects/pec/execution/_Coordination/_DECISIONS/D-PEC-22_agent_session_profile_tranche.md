# D-PEC-22 — agent session-profile source tranche (companion to tier-0 D-T0-22)

**Status:** RULED 2026-07-07 (owner launcher steer, verbatim in `D-T0-22`;
implementation directed in the same steer).
**Date prepared:** 2026-07-07
**Decision ID:** D-PEC-22
**Prepared by:** PEC work loop agent. Packet form per the D-PEC-20/D-PEC-21
precedent. Companion rows: tier-0 `D-T0-22` (the basis; owner direction
verbatim there), `D-PEC-21` (the hermetic session this adds a profile
alongside — unchanged as the default), `D-PEC-20`/`D-T0-21` (access basis —
untouched).

## Owner direction of record

2026-07-07 launcher steer, quoted verbatim in `D-T0-22` (tier-0 register):
an opt-in profile permitting the SDK session's built-in tools and setting
sources; **no previous restriction removed** — the hermetic session stays
the default and stays byte-identical.

## The tranche

1. **Config:** `PEC_AGENT_SESSION=hermetic|open` in `config.ts`
   (`SidecarConfig.session`), default `hermetic`, invalid values fail at
   load, never silently.
2. **SDK engine (`projects/pec/agent-sidecar/src/engine/sdk.ts`):**
   `buildQueryOptions` branches on the
   profile —
   - `hermetic` (default): the exact ruled D-PEC-21 shape, unchanged —
     `tools: []`, `settingSources: []`, pec-tool `allowedTools` whitelist,
     `canUseTool` deny-everything-else.
   - `open`: the `tools` restrictor is omitted (the SDK's built-in tool set
     loads), `settingSources: ['user','project','local']`, the pec tools
     stay auto-approved via `allowedTools`, and `canUseTool` allows the
     rest (built-ins) instead of denying — the pec bounded-acts surface,
     act budget, guards, clamp, and refusals are IDENTICAL in both
     profiles (same `buildPecTools`, same `BoundActs` dispatch).
   - System prompt gains an `open`-only paragraph: built-in harness tools
     are additionally available; pec record acts still go ONLY through the
     pec tools; accept/apply/reject-of-others/force remain human acts in
     Admin regardless.
   - Startup validation in `createSdkEngine` (invalid `PEC_AGENT_SESSION`
     fails at startup, like `PEC_AGENT_MAX_ACTS`).
3. **Disclosure:** `/agent/health` gains `session` alongside `access`
   (never widened silently). The panel badge is NOT extended this tranche
   (disclosed; candidate follow-up if the owner wants it visible in-app).
4. **Docs:** README env row + hermetic-session paragraph updated to name
   the profile knob.
5. **Tests (new `projects/pec/agent-sidecar/test/session-profile.test.ts` +
   existing pins untouched):**
   config parse pins (default hermetic / open / invalid); query-options
   shape pins for BOTH profiles — hermetic byte-identical to the ruled
   shape (the existing adversarial pin keeps passing unmodified), `open`
   has no `tools` restrictor, carries the three setting sources, still
   auto-approves exactly the pec tools, and `canUseTool` allows a non-pec
   tool under `open` while the hermetic deny pin stands; health `session`
   disclosure pin.

**Known behavior under `open` (disclosed, in-scope-as-is):** built-in tool
calls are not pec acts — they don't count against the pec act budget (the
SDK `maxTurns` bound still holds; `PEC_AGENT_MAX_ACTS` raises it) and don't
mirror `act:*` events to the panel (the owner sees pec acts + the final
reply). Both are acceptable for the directed limit-testing use.

**Not in scope (unchanged, structural):** the act vocabulary and human-act
boundary (no accept/apply/reject-of-others/`force`/conversion-disposition
in ANY profile), the D-T0-21 access basis and clamp, loopback transport,
credential hygiene, server routes, new dependencies, the stub engine,
real/non-scratch mutation basis, panel UI.

## Fence (exact; STOP outside it)

- `projects/pec/agent-sidecar/src/config.ts`
- `projects/pec/agent-sidecar/src/engine/sdk.ts`
- `projects/pec/agent-sidecar/src/http.ts` (health disclosure line only)
- `projects/pec/agent-sidecar/test/session-profile.test.ts` (new)
- `projects/pec/agent-sidecar/test/{access-basis,sidecar-e2e,pec-client}.test.ts`
  (mechanical only: the existing `SidecarConfig` literals gain
  `session: 'hermetic'` — no assertion changes)
- `projects/pec/agent-sidecar/README.md`
- No `core/**`, no `server/**`, no `web/**`, no root manifests, no profile,
  no DB, no `acts.ts`, no `pec-client.ts`, no `stub.ts`, no `port.ts`.

## Verification plan (workplan step-4 bar)

pec `npm run typecheck && npm test && npm run build && npm run drill`;
scope containment `git diff --name-only ⊆ fence`; hermetic-default
regression (the existing D-PEC-21 adversarial pin passes unmodified);
self-check no baseline shift; `git diff --check`. Live `open` exercise is
the owner's per-launch env act at his screen.

## Rollback

Single revert of the tranche commit; without `PEC_AGENT_SESSION` set the
sidecar is hermetic-default and behaviorally identical to pre-tranche.

## Human ruling

**RULED — 2026-07-07** by the owner direction quoted verbatim in
`D-T0-22` (launcher steer; K-AUTH-1): the profile mechanism directed,
implementation directed in the same steer, previous restrictions retained
as defaults. Branch-first on the live `codex/pec-dpec21-agent-loop` lane;
no self-merge.
