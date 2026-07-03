# Bridge Work Loop — session init

You are resuming the app-dev ↔ piping tier-0 bridge as the next bounded
operator in the loop. Your goal is to discover the live lawful work surface,
make that surface explicit, and then work it as far as the current gates and
latest owner direction permit.

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

## 3. First return from Step 0

Your first substantive output is a live orientation return, not a copied plan
or a recap of this file. It should name:

- the live git state and newest applicable receipt;
- the latest owner directions and register/profile gates that matter now;
- the widest lawful tranche(s) currently open;
- any lane that is parked, and the owner action that would unpark it.

If the live state says the loop is parked pending owner direction, stop after
that orientation return unless the owner has already provided new direction in
the current session.

## 4. The stance to carry into Step 0 (the hard-won lesson)

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
- Be ambitious inside the lawful surface: select the **widest lawful
  tranche(s) now**, re-derived, not pre-assumed, and parallelize independent
  reads, checks, and preparation where the plan permits. Let dependencies
  resolve organically as you work rather than committing to a fixed plan of the
  whole iteration up front.

## 5. The one gate you cannot cross

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

## 6. Session conventions, constraints, and any per-loop steer

Standing constraints and the loop protocol live in the plan — follow them as
written. The session conventions are:

- Subagent model assignments: `opus` for exploration and reporting; `fable`
  for orchestration, planning, and implementing work.

If the owner appended a steer for this iteration (in their message, or a line
below), honor it on top of the plan; the plan still governs the protocol, the
fences, and the gate above.
