# Sealed Child Brief — SCA-004 Gate-2 Fresh Review 2

InstanceID: `A2_GATE2_FRESH_REVIEW_2`
Parent: `N2_SCA004_GATE2` (`SCOPE_CHANGE`)
Agent layer: bounded ephemeral Agent 2; non-delegating
Basis: repaired N2 bytes after fresh-review cycle 1

## Objective

Perform a new independent final review of the repaired SCA-004 Gate-2
candidate. Confirm the two prior residual G0 wording blockers are repaired and
re-run the entire Phase-0b N2 acceptance surface, not merely those clauses.

## Required reads

- `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`, especially Gate 2
- Phase-0b steer, R1 record, and G0 record under `plans/steers/`
- all direct files under `execution/_ScopeChange/SCA-004_2026-08-22_1749/`
- the two earlier child review returns in sibling child folders

## Write scope

Only this child folder. Write `RETURN.md` and terminal `STATUS.json`. Do not
edit SCA-004 or any other path. Do not delegate or perform Git/network acts.

## Acceptance checks

- Every Phase-0b N2 product/check requirement passes, including R1-C verbatim,
  eight action rows/four lenses, both derivative tables, explicit risk/state
  sections, four-state handoff, protected hashes, and hard Gate-3 stop.
- G0 A3 includes unchanged hard filesystem/network/process containment.
- G0 A7 includes that a grant may unblock queued requests to the same
  destination and that G-APPR proves prompt delivery/grouping empirically at
  the exact pin.
- A4 and exactly ten `HELD_UNAVAILABLE` bindings remain exact.
- Graph bytes remain unchanged and no AUDIT_DEP_CLOSURE rerun is required.
- N2 writes remain confined to the SCA folder and this N2 instance folder.
