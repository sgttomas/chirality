# TM-ROOT-116 decision draft — idle-workplan Step 0

Date: 2026-08-09

Status: `PREPARED FOR ACCOUNTABLE-HUMAN RULING — NOT APPLIED — NOT CLOSURE`

Target if accepted:
`execution/_Coordination/WORKPLAN_2026-07-27_root_idle.md`

Insertion point: immediately after the `## Purpose` section and before
`## Operating posture`.

The amendment form is preferred over a successor workplan because the current
idle posture remains selected, the row identifies only a missing entry step,
and the owner has not selected a different successor objective. The proposed
bytes below do not create a Task Management entry binding and do not activate
production.

## Exact proposed insertion bytes

```markdown
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
```

## Proposed owner ruling

- `ACCEPT`: insert the exact block above into the named idle workplan. Keep
  `CURRENT_WORKPLAN.md` unchanged. This acceptance alone does not close
  `TM-ROOT-116`; application, validation, human-gated PR merge, and a later
  owner disposition remain required.
- `AMEND`: return replacement text or constraints.
- `DECLINE`: leave the workplan and `TM-ROOT-116` unchanged.

No workplan or pointer bytes were changed by preparation of this draft.
