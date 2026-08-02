# Orchestration Plan — Task Management Federation Survey

RunID: `TM-FEDERATION-SURVEY-20260802`
PlanVersion: `5`
SelectionAuthority: `HUMAN`
Posture: `MIXED`
Status: `COMPLETE`
Basis: `main@3e03b257748822dba2ad7697453f3495fb7578db` (execution basis); final publication base `main@4d55dea0f375034b66949723a7b849a2c962d8a3`
Branch: `codex/task-management-federation-survey`

## Human direction

The owner instructed the active goal to implement
`plans/chirality-task-management/FEDERATION_SURVEY_IMPLEMENTATION_PLAN_2026-08-02.md`.
This supplies Gate H0 implementation authority for the bounded candidate
tranche. The owner later directed, verbatim, "Merge via PR," satisfying H2;
CHANGE completed the checked publication through PR #478.

## Objective

Implement an invocation-local, read-only federation survey at the beginning
of every `TASK_MANAGEMENT` invocation. Do not require any loop to invoke
`TASK_MANAGEMENT` and do not add loop-entry binding, scheduling, CI, daemon,
schema migration, register writes, or foreign-write authority.

## Managed graph

The executable graph is recorded in `WORK_GRAPH.json`. `HELP_HUMAN` supervises
the Agent 1 managers. `HELPS_HUMANS` owns component design, Agent 2 fan-out,
implementation integration, instruction/tool validation, manifest, and
notices. `TASK_MANAGEMENT` performs read-only behavioral acceptance after
integration. `CHANGE` enters only after validated fan-in and the publication
gate.

### Amendment 1 — executable child topology

The first managed HELPS_HUMANS child was stopped before execution because it
produced no child launch, return, or file change. It is not counted as
performed work. Under the current root doctrine permitting Agent 0 to dispatch
bounded Agent 2 instances directly, graph version 2 separates three disjoint
lanes: read-only A2 inventory, A2 tool/test implementation, and Agent 1
HELPS_HUMANS governance/instruction integration. A fresh read-only verifier
follows their fan-in. This changes execution topology only; objective, scope,
gates, outputs, and acceptance criteria are unchanged.

### Amendment 2 — canonical manager topology restored

The owner clarified that the canonical managed workflow is required for this
tranche: `HELP_HUMAN -> HELPS_HUMANS -> Agent 2`. The direct Agent 2 lanes and
the duplicate HELPS_HUMANS lane introduced by Amendment 1 were stopped before
fan-in. Their partial files and observations are unaccepted candidate evidence,
not integrated work. The original HELPS_HUMANS instance is resumed as the sole
Agent 1 integration owner and will dispatch fresh, sealed Agent 2 inventory,
implementation, and independent-verification children. HELPS_HUMANS must
inspect, validate, and explicitly adopt or replace every partial direct-lane
artifact before it can enter the candidate tranche.

### Amendment 3 — recovery and terminal fan-in

`A2-INVENTORY-R2` and its timeboxed replacement `R2B` were interrupted
without returns. HELPS_HUMANS reproduced and accepted the inventory at the
manager layer. `A2-IMPLEMENT-R2` returned successfully; manager inspection
corrected invoking-relative labeling and output/register collision safety.
Fresh `A2-VERIFY-R2` found one missing same-namespace elevation acknowledgement;
the manager repaired it, added a regression, and the verifier closed it with
`READY`. HELPS_HUMANS and the separate TASK_MANAGEMENT behavioral acceptance
both returned `READY`. HELP_HUMAN fan-in is recorded in
`HELP_HUMAN_FANIN.md`, Root Receipt 82, and the four-field handoff state.
At that Amendment-3 checkpoint, CHANGE remained held at H2.

### Amendment 4 — checked publication and terminal closeout

The owner supplied H2 with the exact direction "Merge via PR." CHANGE
published the validated implementation commit
`bb44d71c93cc5431d5fc8a902e716cc88966ea9f` through PR #478. Immediately
before merge, the exact approved source was
`08ed85ae1a1ae2be9eba971e6567fad2bb202b56` and the final base was
`4d55dea0f375034b66949723a7b849a2c962d8a3`; `Harness pre-merge`, `harness`,
and `pec` all reported `SUCCESS`. GitHub merged that source as
`2c25bd2c47c4b2f4190275ad39579a983f8786aa`, by `sgttomas`, at
`2026-08-02T22:13:19Z`. The graph is terminally complete. Earlier manager and
Agent 2 returns retain their as-of-time `READY`/interrupted dispositions.

## Shared-write rule

`HELPS_HUMANS` is the sole integration owner. Its Agent 2 children receive
disjoint sealed scopes; implementation children may write only their declared
component paths and run records. Fresh verification and acceptance are
read-only. No concurrent overlapping writes are permitted.

## Human gates

- H0 implementation: satisfied by the current explicit implementation goal.
- H1 expansion: required for schema, CONTRACT/PRD, central authoritative
  registry, scheduling, CI, daemon, loop-entry, or foreign-write expansion.
- H2 publication/merge: satisfied and completed through checked PR #478.

## Required terminal handoff

The terminal handoff names the accepted and final publication bases, validated
implementation and approved source identities, exact candidate paths,
derivative status, Agent 1/2 validation, federation coverage, effective merge,
closure verdict, and future rerun trigger. There is no remaining blocker or
owner gate for PR #478.
