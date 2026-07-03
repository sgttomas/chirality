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
Its **Step 0 (Discover)** runs before anything else. The plan carries the
protocol, standing constraints, and pointer indexes ONLY — no status, no
history. Current state is re-derived live (registers, profile, git, harness);
the handoff context (owner directions, gate outcomes, stale-map deltas) lives
in the latest receipts in `_DomainEngines/bridge/LOOP_RECEIPTS.md`, whose
local rules govern what a receipt may contain.

## 3. The stance to carry into Step 0 (the hard-won lesson)

The plan, the receipts, and any dated assessment are **maps with per-claim
citations — not authority**. The recurring failure mode in this archive is a
fluent draft grounded on stale facts. So:

- Before you rely on any derivative statement — a map's claim, a receipt's
  pointer, **or your own tasking and this init text** — open its cited source
  in the live tree and confirm it still holds. On disagreement the **live tree
  wins** — record the delta in your loop receipt, never by editing the map.
  (Twice on 2026-07-02, execution agents caught errors in their own
  instructions this way; the discipline applies to prompts, not just files.)
- New owner rulings since the last receipt are how work unlocks. Check both
  project decision registers and the tier-0 register every iteration.
- Select the **widest lawful tranche(s) now**, re-derived, not pre-assumed.
  Let dependencies resolve organically as you work rather than committing to a
  fixed plan of the whole iteration up front.

## 4. The one gate you cannot cross

**Adoption, ruling, and direction are the owner's acts** (K-AUTH-1; D-GOV-04)
— no command and no agent performs them. For deliverable work, generate
CANDIDATE brief(s); for coordination/control work, present a decision slate
(options + non-binding recommendation + on-ruling mechanism). Surface what you
would do once each is adopted/ruled, and **stop there** for the owner. Only
after the owner acts do you execute inside the fence, run the plan's
work-type checks, and append a minimal receipt to
`_DomainEngines/bridge/LOOP_RECEIPTS.md` (per its local rules: verbatim owner
directions, pointers to artifacts, gate outcomes, check pass/fail) so the
next iteration starts clean.

## 5. Session conventions, constraints, and any per-loop steer

Standing constraints and the loop protocol live in the plan — follow them as
written. The session conventions are:

- Subagent model assignments: `opus` for exploration and reporting; `fable`
  for orchestration, planning, and implementing work.

If the owner appended a steer for this iteration (in their message, or a line
below), honor it on top of the plan; the plan still governs the protocol, the
fences, and the gate above.

