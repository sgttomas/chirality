# Root Governance Workplan — Idle Owner-Gate Posture

Status: `IDLE — NO ACTIVE ROOT PRODUCTION PHASE`
Date: 2026-07-27
Supervising role: `HELP_HUMAN`

## Purpose

Keep the deterministic Root loop entry truthful after the original
45-deliverable initialization phase and the later initialization of
`DEL-02-06` both completed.

The prior workplan,
`execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md`, is
complete by its own closure condition. At the accepted basis:

- all 46 Root deliverables are `INITIALIZED`;
- Root decomposition revision 1.1 is accepted;
- `DEL-02-06` has its exact accepted Scope of Work and is initialized but not
  activated; and
- no successor Root production phase has been selected.

## Step 0 — Idle-entry currentness preflight

Run this step before selecting or dispatching any work under this standing
plan.

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; resolve
   `execution/_Coordination/CURRENT_WORKPLAN.md` from that root; and require
   its `Target` to name this exact workplan. If the pointer is missing,
   malformed, escapes the repository, or names another or missing file, stop
   and return the defect to the owner.
2. Inspect and record the current branch or detached-HEAD state, worktree
   cleanliness, and divergence from `origin/main`. Treat unrelated changes as
   external state. Do not claim a synchronized basis unless the inspected refs
   support that claim.
3. Read the live `execution/_Coordination/HANDOFF_STATE.md`, then the newest
   entry in Root `execution/_Coordination/LOOP_RECEIPTS.md` and the newest
   relevant App Dev and Piping loop receipts. Re-open every live decision,
   accepted snapshot, or human direction relied on by those derivative
   surfaces; live authority wins on disagreement.
4. Re-derive the accepted Root PRD and decomposition revisions, the Root
   deliverable lifecycle census, and any separately authorized bounded lane
   from live committed sources. Treat a stale count, pointer, lifecycle claim,
   or authority claim as a currentness defect to report; do not absorb it
   silently.
5. Run and record the standing Root self-development guards:
   `python3 tools/validation/validate_root_materialization_fence.py` (G0),
   `python3 tools/validation/validate_root_harness_adapter.py` (G1),
   `python3 tools/validation/validate_root_surface_ownership.py` (G2),
   `python3 tools/validation/validate_root_work_graph_dispatch.py` (G3), and
   `python3 tools/validation/validate_instruction_tranche_manifest.py` (G4).
   Stop on BLOCK or operational failure.
6. If current human direction and live authority release no separate bounded
   lane, present the current decision slate and stop. This idle plan itself
   authorizes no production, activation, lifecycle transition, scope change,
   implementation, publication, release, or reliance act.

## Operating posture

This workplan authorizes no production, activation, lifecycle transition,
scope change, implementation, repin, release, or professional-reliance act.
On entry, report the live governed state and any exact owner gates supplied by
current human direction. If no separately authorized lane exists, present the
decision slate and stop.

Read-only verification and preparation already authorized by a distinct owner
act may proceed under that act. It does not become an active Root production
phase by appearing in a receipt or candidate package.

## Successor selection

A future substantive Root phase requires its own decision-complete workplan
candidate and the applicable human gate. When accepted, add the successor
workplan and repoint `CURRENT_WORKPLAN.md`; do not infer a phase from pending
candidates, modification times, or narrative status.

## Authority and closeout

This is a coordination surface, not authority. Live standards, decisions,
accepted snapshots, Git state, and current human direction govern. Every
consequential change and lifecycle act remains human-gated. Git closeout does
not constitute semantic acceptance.

## Currency addendum — 2026-07-29

The basis facts above date from 2026-07-27 and are updated here without
changing this plan's posture: Root PRD Revision 8 is now the adopted product
basis (D-GOV-31, Receipt 61; owner-directed simplification, Receipt 64), and
decomposition revision 1.2 is the accepted current basis (SCA-002 accepted
and applied, Receipt 63). All 46 Root deliverables remain `INITIALIZED`;
`DEL-02-06` remains initialized, not activated; no successor phase is
selected. The operating posture and successor-selection rules above are
unchanged.

## Currency addendum — 2026-07-31 (Task Management Stage A closed)

Resumed as the standing posture after Stage A closed (Receipts 66–73).
Posture and successor-selection rules above are unchanged. Two additions
to the idle state of the world since the 2026-07-29 addendum: the root
program register exists at
`execution/_Coordination/_TaskManagement/REGISTER.csv` (101 rows;
46 CLOSED / 51 DEFERRED / 4 OPEN — attention residue only, never gating,
K-TM-4/K-TM-5), and TASK_MANAGEMENT (`agents/AGENT_TASK_MANAGEMENT.md`)
is invocable on demand or by owner-scheduled routine for register
sessions and ruled-item resolution. Three Stage-B adoption packets await
per-loop rulings on their own surfaces (D-APP-83 / D-63 / D-PEC-72).

## Currency addendum — 2026-08-02 (four separately authorized Root lanes)

The idle posture remains the general standing plan; no broad Root production
phase has been selected. A later owner steer separately opened four bounded
lanes prepared by the 2026-08-02 Root Task Management closeout:

1. the `TM-ROOT-107` Root SCOPE_CHANGE intake;
2. the `TM-ROOT-108` DEL-02-06 accepted-turn recovery amendment/activation
   lane;
3. the `TM-ROOT-110` existing G4 diff-mode CI wiring; and
4. the `TM-ROOT-106` Pi `0.82.0` concordance/supply-chain validation.

Their shared HELP_HUMAN work graph and live gate state are under
`execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/`. G4 is locally
ready for checked publication. SCA-003 is stopped at Gate 1, DEL-02-06 is held
at N0, and the Pi evaluation is held for an owner decision. These bounded
lanes do not authorize Task Management row closure, a general production
phase, runtime implementation by implication, lifecycle or release acts, or
merge; the owner retains the Git merge gate.
