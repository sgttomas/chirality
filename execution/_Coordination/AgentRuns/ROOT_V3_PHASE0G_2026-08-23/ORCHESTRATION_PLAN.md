# Root v3 Phase 0g orchestration plan

Plan version: `2`
Selection authority: `HUMAN — Ryan Tufts, R6-A/R6-B/R6-C/R6-D`
Posture: `TERMINAL_FAN_OUT_IN` (one bounded Agent 2 instance)
Branch basis: `origin/main@d279bad6a5903678822ac8b3b85aec76f7a0cfed`
Branch: `codex/root-v3-phase0g-2026-08-23`

## Objective

Close SCA-004 by transcribing R6, applying the owner-approved pointer with
exactly three named fills, backfilling only recorded Git-effect/reference
slots, and setting the SCA handoff to closed-confirmed with propagation still
pending.

## Node and dependency graph

| Node | Role | Depends on | Write ownership | Expected return | Fan-in gate |
| --- | --- | --- | --- | --- | --- |
| `N1_SCA004_CLOSURE` | bounded ephemeral Agent 2, SCOPE_CHANGE record specialist | all Phase-0g basis gates and applied validator PASS 65/65 | exactly four SCA/pointer targets plus own return/status | exact R6 transcription, three-slot pointer, slot-only backfills, closed handoff | write containment, pointer three-slot proof, recorded-act traceability, protected-byte parity |

There are no concurrent writers or sibling dependencies.

Plan amendment V2, authorized by owner ruling R6-D after fresh review cycle 1,
widens N1 by exactly two project targets: the applied validator's sole
`_LATEST.md` expectation and its regenerated validation JSON. The Decision
Log remains inside N1's original write set and receives R6-D verbatim. No
other project path or validator line is selectable. See
`amendments/N1_SCA004_CLOSURE/V2.md`.

## Human gates and parked work

- R6-A confirms Gate 5; R6-B authorizes the exact pointer; R6-C authorizes
  only the named backfills.
- PREPARATION INIT ×7, DEL-02-06 context propagation, dependencies,
  estimates, schedule, graph/DAG, and AUDIT_DEP_CLOSURE remain separately
  gated propagation work.
- TM-ROOT-106/122, C1, pins, all ten holds, implementation, App work,
  release, and reliance remain parked.
- Any write-set expansion or unrecorded fill stops and returns to the owner.

## Protected state

The seven live decomposition files and every other SCA-004 file are read-only.
No instruction, docs, deliverable, status, SOW, dependency, estimate,
schedule, graph, Task Management, tool, runtime, project, export, pin, or App
surface may change.

## Closeout

HELP_HUMAN validates the return, dispatches a fresh read-only review, updates
the Root handoff and Receipt 120, runs all required validators, and performs
the ordered Git closeout: commit, push, and one PR to `main`. No merge.
