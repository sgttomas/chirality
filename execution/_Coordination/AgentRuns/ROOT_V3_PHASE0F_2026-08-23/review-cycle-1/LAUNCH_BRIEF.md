# Fresh read-only review brief — Root Phase 0f N1

Reviewer role: bounded Agent 2 evidence reviewer
Parent: HELP_HUMAN
Delegation: forbidden
Review basis: `origin/main@119e08647afdb380704ff660fb32d714d7bd1dad`
Execution node: `N1_GATE5_SECOND_ATTEMPT`

## Objective

Independently review 100% of the Phase-0f N1 result for compliance with the
owner steer, R5-A, the sealed brief, SCOPE_CHANGE invariants, exact-byte
identity gates, write containment, and evidence sufficiency. This is a fresh
read-only review. Do not repair substantive or project artifacts.

## Required reading

- `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`
- Phase-0f steer and R5 ruling record
- R4 ruling record
- the Phase-0f orchestration plan, graph, N1 sealed brief, N1 return/status
- all changed/new SCA-004 records and validator/audit outputs
- `git diff origin/main --` for every changed tracked path and the complete
  untracked Phase-0f/SCA evidence set

## Independent checks

1. Rehash the seven live decomposition files and require R4-A 7/7.
2. Rerun `validate_gate5_applied.py` and require PASS, zero failures, stable
   JSON bytes.
3. Verify Stage A record proves R3-A 7/7, R4-A 7/7, applied validator PASS,
   and governed live revision 1.2 throughout rehearsal.
4. Verify Stage B used exactly seven `/bin/cp` operations, one append check,
   and one append application; no patch-edit re-expression touched live files.
5. Verify the post-Gate5 audit package reports the expected 53/12/11/6/104/7
   topology, 85/59 trace rows, and zero unmapped/unsupported/untraced defects.
6. Verify Decision Log includes the required exact R4-A/R4-B/R4-C/R5-A
   verbatim recorded-form blocks and correct Gate-5 state.
7. Verify Application Record, SCA Handoff, N1 Return, and STATUS agree on
   hashes, check counts, closure state, derivative currentness, blockers, and
   no inferred owner confirmation/pointer/Git effect.
8. Verify all ten DEL-02-06 bindings remain `HELD_UNAVAILABLE` and protected
   inputs/paths remain byte-identical to origin/main, including `_LATEST.md`,
   every `_STATUS.md`, Task Management, approved SCA package inputs, and the
   Gate-1 audit baseline.
9. Verify all changed/untracked paths are within the node/run write envelope;
   run `git diff --check` and relevant JSON parsing.
10. Identify any ambiguity, stale claim, inconsistent count/SHA, insufficient
    command evidence, or out-of-scope write as an actionable finding.

## Output

Write only:

- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0F_2026-08-23/review-cycle-1/REVIEW.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0F_2026-08-23/review-cycle-1/STATUS.json`

Return `PASS — ZERO ACTIONABLE FINDINGS` only if every check passes. Otherwise
return `FAIL` with numbered actionable findings, exact paths/lines, evidence,
and the smallest lawful repair. Do not modify any reviewed file.
