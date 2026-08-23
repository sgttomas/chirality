# Sealed Child Brief — SCA-004 Gate-2 Fresh Review

InstanceID: `A2_GATE2_FRESH_REVIEW`
Parent: `N2_SCA004_GATE2` (`SCOPE_CHANGE`)
Agent layer: bounded ephemeral Agent 2; non-delegating
Basis: repaired N2 working bytes after `A2_GATE2_TRACE`

## Objective

Freshly review the repaired SCA-004 Gate-2 candidate for exact conformance to
the Phase-0b N2 steer, R1-C, and `AGENT_SCOPE_CHANGE.md` Gate 2. Verify that
all prior trace-review blockers are repaired without opening Gate 3.

## Required reads

- `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`, especially Gate 2
- `plans/steers/chirality_app_v3_phase0b_steer_root_2026-08-22.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`
- all files directly under `execution/_ScopeChange/SCA-004_2026-08-22_1749/`
- sibling child `A2_GATE2_TRACE/RETURN.md`

## Write scope

Only this child folder. Write `RETURN.md` and terminal `STATUS.json`. Do not
edit SCA-004 or any other repository path. Do not delegate, commit, push,
merge, fetch, sync, or rebase.

## Acceptance checks

- Decision log has a G1-ACCEPTED row, R1-C verbatim with all three SHAs, and
  Gate 2 pending-owner state.
- Exactly eight actions each cover the four mandatory impact lenses.
- Separate derivative-package and derivative-surface tables exist.
- Orphan risk, estimate/schedule staleness, snapshot/handoff impact, and
  workflow-owned reruns are explicit.
- Full G0 A3/A4/A7 semantics and exactly ten held bindings are unchanged.
- Handoff uses the four-state form, names D-GOV-35 as ruled/application in N1,
  and stops at `AWAITING_OWNER_GATE_2_ACCEPTANCE` with Gate 3 closed.
- Protected Gate-1 files and `_LATEST.md` retain their required hashes; graph
  bytes did not change, so no AUDIT_DEP_CLOSURE rerun is required.
- No N2 write exists outside the SCA folder and this N2 instance folder.
