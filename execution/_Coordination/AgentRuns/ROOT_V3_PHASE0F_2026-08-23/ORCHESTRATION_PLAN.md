# Root v3 Phase 0f orchestration plan

Plan version: `1`
Selection authority: `HUMAN — Ryan Tufts, R5-A`
Posture: `TERMINAL_FAN_OUT_IN` (one bounded Agent 2 instance)
Branch basis: `origin/main@119e08647afdb380704ff660fb32d714d7bd1dad`
Branch: `codex/root-v3-phase0f-2026-08-23`

## Objective

Execute the owner-re-authorized second SCA-004 Gate-5 attempt through two
strictly ordered stages: first create and prove the applied-state validator in
a scratch rehearsal; then, only if the rehearsal gate passes, execute the live
byte-copy and approved zero-context append exactly once and record the closure
lane.

## Node and dependency graph

| Node | Role | Depends on | Write ownership | Expected return | Fan-in gate |
| --- | --- | --- | --- | --- | --- |
| `N1_GATE5_SECOND_ATTEMPT` | bounded ephemeral Agent 2, SCOPE_CHANGE execution | all Phase-0f basis gates; Stage B additionally depends on Stage A 7/7 + 7/7 + PASS | exact SCA-004 and seven live decomposition targets in the sealed brief; own runtime return/status | applied live R4-A identities, closure evidence, or exact stopped blocker with recovery state | sealed-brief scope, identity gates, validator and audit results, protected-path parity, fresh review |

There are no concurrent writers and no sibling dependencies. Stage A and
Stage B are serialized inside N1. Stage B may run only once.

## Human gates

- R5-A already authorizes this second attempt and its exact method.
- Gate-5 confirmation remains with the owner after fan-in.
- `_LATEST.md` pointer treatment remains deferred under R4-C.
- Any write-set expansion, identity drift, Stage-A failure, or post-Stage-B
  closure finding stops at the applicable fence and returns to the owner.

## Protected state

No `AGENTS.md`, `agents/**`, `docs/**`, `_LATEST.md`, `_STATUS.md`, live
deliverable folder, SOW, dependency, estimate, schedule, graph, Task
Management, `tools/**`, runtime, project, export, pin, or App surface may
change. Approved and published SCA-004 inputs are read-only.

## Closeout

HELP_HUMAN validates the N1 return, dispatches a fresh read-only review,
performs cross-workflow fan-in, updates the Root handoff and Receipt 119,
runs the steer's validators, and hands the bounded change to CHANGE for
ordered commit, push, and PR creation. No merge.
