# Sealed Child Brief — SCA-004 Gate-2 Trace Review

InstanceID: `A2_GATE2_TRACE`
Parent: `N2_SCA004_GATE2` (`SCOPE_CHANGE`)
Agent layer: bounded ephemeral Agent 2; non-delegating
Basis: `b143444bd497eae1b1b638670a33e6df756d9084`

## Objective

Independently inspect the accepted SCA-004 Gate-1 package and the Phase-0b
R1-C direction. Produce a read-only Gate-2 completeness review that maps all
eight parsed actions across the four mandatory SCOPE_CHANGE lenses:
decomposition structure, variant-local metadata, downstream consumers, and
invariant/telemetry risk. Check that G0 A3/A4/A7 and the ten held bindings are
carried without alteration.

## Required reads

- `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`, especially Gate 2
- `plans/steers/chirality_app_v3_phase0b_steer_root_2026-08-22.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`
- all files directly under `execution/_ScopeChange/SCA-004_2026-08-22_1749/`
- `execution/_ScopeChange/SCA-002_2026-07-29_0800/Impact_Assessment.md`
- `execution/_ScopeChange/SCA-002_2026-07-29_0800/Handoff_State.md`

## Write scope

Only this child folder:
`execution/_Coordination/AgentRuns/ROOT_V3_PHASE0B_2026-08-22/instances/N2_SCA004_GATE2/children/A2_GATE2_TRACE/`.

Write `RETURN.md` and terminal `STATUS.json`. Do not edit SCA-004 or any other
repository path. Do not delegate, commit, push, merge, fetch, sync, or rebase.

## Acceptance checks

- Exactly eight action rows accounted for.
- Each action has all four impact lenses.
- Required derivative-package and derivative-surface tables are assessed.
- Orphan risk, estimate/schedule staleness, snapshot/handoff effect, and
  recommended reruns are covered.
- No Gate 3 implication, no hold lift, no App authority claim.
- Return discrepancies as actionable findings with exact source references.
