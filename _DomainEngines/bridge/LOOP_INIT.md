# Bridge Work Loop — session init

You are running the next iteration of the app-dev ↔ piping tier-0 bridge work
loop. Get oriented with the steps below, then work the loop.

Treat this text as orientation, **not authority**: the standing plan (step 2)
is newer and governs on any conflict — including anything here it contradicts.
This init deliberately restates no facts, rulings, counts, or SHAs, so it does
not go stale; the load-bearing state is re-derived at Step 0.

## 1. Bootstrap

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; work from there.

## 2. Hand off to the plan

The standing plan is the protocol — read it and do what it says:
`_DomainEngines/bridge/WORKPLAN_*_bridge_loop.md` (newest if more than one).
Its **Step 0 (Discover)** runs before anything else; its Standing constraints,
Backlog, Owner-action queue, and append-only Loop Log carry everything
specific to the current state.

## 3. The stance to carry into Step 0 (the hard-won lesson)

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

## 4. The one gate you cannot cross

Brief **adoption is the owner's act** (K-AUTH-1; D-GOV-04) — no command and no
agent performs it. Generate CANDIDATE brief(s), surface them plus what you
would do once each is adopted, and **stop there** for the owner. Only after
the owner has adopted do you execute inside the fence, run the plan's checks,
and append a Loop Log entry (measurements, deltas, work done, what is newly
unlocked, owner-queue changes) so the next iteration starts clean.

## 5. Session conventions, constraints, and any per-loop steer

Standing constraints and the loop protocol live in the plan — follow them as
written. The session conventions are:

- Subagent model assignments: `opus` for exploration and reporting; `fable`
  for orchestration, planning, and implementing work.

If the owner appended a steer for this iteration (in their message, or a line
below), honor it on top of the plan; the plan still governs the protocol, the
fences, and the gate above.

