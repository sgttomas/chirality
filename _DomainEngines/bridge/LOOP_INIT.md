# Bridge Work Loop — session init / orientation

> **Agent-authored process doc — not authority.** This orients an agent
> opening a session to run one iteration of the app-dev ↔ piping tier-0
> bridge work loop. It deliberately restates no facts, rulings, counts, or
> SHAs, so it does not go stale. The loop itself is governed by the standing
> plan (below), which governs on any conflict with this doc.

## Read this first, then hand off to the plan

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; work from there.

2. The standing plan is the protocol — read it and do what it says:
   `_DomainEngines/bridge/WORKPLAN_*_bridge_loop.md` (newest if more than
   one). Its **Step 0 (Discover)** runs before anything else; its Standing
   constraints, Backlog, Owner-action queue, and append-only Loop Log carry
   everything specific to the current state. Do not act on anything in this
   init doc that the plan contradicts — the plan is newer and governs.

## The stance to carry into Step 0 (the hard-won lesson)

The plan, and the readiness assessment it points to, are dated **maps with
per-claim citations — not authority**. The recurring failure mode in this
archive is a fluent draft grounded on stale facts. So:

- Before you rely on any claim from a map, open its cited source in the live
  tree and confirm it still holds. On disagreement the **live tree wins** —
  record the delta in your Loop Log entry, never by editing the map.
- New owner rulings since the last Loop Log entry are how work unlocks. Check
  both project decision registers and the tier-0 register every iteration; do
  not assume the Backlog table is current — re-derive it at Step 0.
- Select the **widest lawful tranche(s) now**, re-derived, not pre-assumed.
  Let dependencies resolve organically as you work rather than committing to a
  fixed plan of the whole iteration up front.

## The one gate you cannot cross

Brief **adoption is the owner's act** (K-AUTH-1; D-GOV-04) — no command and no
agent performs it. Generate CANDIDATE brief(s), surface them plus what you
would do once each is adopted, and **stop there** for the owner. Only after
the owner has adopted do you execute inside the fence, run the plan's checks,
and append a Loop Log entry (measurements, deltas, work done, what is newly
unlocked, owner-queue changes) so the next iteration starts clean.

## Session conventions and constraints

Live in the plan (Standing constraints; Session conventions) — follow them as
written. If the owner's initial message for the session adds a steer for this
iteration, that steer sits on top of the plan; the plan still governs the
protocol, the fences, and the gate above.
