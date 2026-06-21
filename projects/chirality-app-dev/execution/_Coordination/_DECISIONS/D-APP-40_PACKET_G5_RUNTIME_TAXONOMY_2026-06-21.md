# D-APP-40 Packet - G5 Runtime Naming and Taxonomy Reconciliation

**Status:** PROPOSAL / AWAITING_RULING
**Date:** 2026-06-21
**Decision ID:** D-APP-40
**Prepared by:** WORKING_ITEMS

## Context / Problem

ADQ-05 selected the G5 reconciliation item: `runTurn` / `startTurn`, public event ownership,
interruption terminal taxonomy, and child-run IDs. Current source and current authority are not
uniform:

- `frontend/src/lib/harness/turn-engine.ts` exposes `TurnEngine.runTurn(request)` as the
  route-independent lifecycle method.
- `frontend/src/lib/harness/agent-engine-port.ts` exposes `AgentEnginePort.startTurn(input)` as the
  adapter stream method, while `docs/SPEC.md` Section 10.2 and DEL-03-01 local-kit text still name
  `AgentEnginePort.runTurn(input)`.
- `PUBLIC_UI_EVENT_NAMES` includes `harness:event` as a redacted `HarnessEvent` passthrough, while
  older DEL-03-01/DEL-03-03 specs list only the seven compact turn events.
- Source and tests model user interruption as `interruption.requested`, `interruption.completed`,
  terminal `turn.cancelled`, and `process:exit` with `interrupted: true`; DEL-03-04 keeps
  `DEL-03-04-CONFLICT-001` open because some source text treats interruption as its own terminal
  outcome.
- `docs/TYPES.md` and source now define `ChildRunRecord.childRunId`, while older DEL-08-05 local-kit
  text still names `HarnessSubagentRun.runId` and keeps denied-allocation semantics open.

The interruption terminal taxonomy and denied child-run allocation boundary are material product
semantics. WORKING_ITEMS cannot self-rule them.

## Decision Needed

Choose the canonical G5 runtime taxonomy so ADQ-05 and downstream runtime/session/subagent work can
update authority docs, local kits, tests, and evidence without silently choosing between incompatible
semantics.

## Option A - Ratify Current Source Behavior And Reconcile Docs

Adopt the current implementation as the canonical taxonomy:

- `TurnEngine.runTurn(request)` is the product lifecycle method outside HTTP.
- `AgentEnginePort.startTurn(input)` is the adapter stream method.
- `harness:event` is a public `UIEvent` name for a redacted provider-neutral `HarnessEvent`
  passthrough; provider/SDK event names remain adapter metadata.
- User interruption is represented by `interruption.requested` / `interruption.completed` plus the
  terminal `turn.cancelled` event and `process:exit.interrupted=true`; do not add `turn.interrupted`.
- `ChildRunRecord.childRunId` is the canonical child-run record/key. Subagent lifecycle events include
  `subagent.started`, `subagent.progress`, `subagent.completed`, and `subagent.failed`.
- Denied subagent attempts may produce a `ChildRunRecord` with `status: denied` only when the runtime
  has reached the child-run record layer; earlier denials may remain permission/hook evidence only.

Expected follow-up: update `docs/SPEC.md` and local DEL-03/DEL-08 kits to this vocabulary, run the
D-APP-38 corpus bump/apply flow for authority-doc edits, and add or adjust tests only where docs imply
coverage gaps.

## Option B - Add Dedicated Interruption Terminal Taxonomy

Keep the current method and child-run names, but amend event taxonomy to add a dedicated
`turn.interrupted` terminal event. `turn.cancelled` would remain for client disconnect or non-user
cancellation, while explicit user interrupt would persist `turn.interrupted`.

Expected follow-up: update `docs/SPEC.md`, `docs/TYPES.md`, event schema, mappers/managers,
engine-conformance tests, replay/UI views, DEL-03/DEL-05 local kits, and D-APP-38 corpus snapshots.

## Option C - Revert To Older Local-Kit Names

Normalize implementation toward older local-kit wording:

- rename or alias `AgentEnginePort.startTurn` to `runTurn`;
- remove or demote `harness:event` from the public UIEvent list;
- use `HarnessSubagentRun.runId` as the child-run record/key and restrict subagent event categories to
  the older started/completed shape unless separately amended.

Expected follow-up: broad source/test migration and compatibility review. This option has the highest
code churn and risks weakening already-tested runtime evidence.

## Recommendation

WORKING_ITEMS recommends **Option A** because it matches current source, current tests, D-APP-25 rich
event bridging, and `docs/TYPES.md` child-run vocabulary with the least migration risk. It also keeps
interruption observable without introducing a new terminal event category. This is a recommendation
only; no implementation or authority-doc reconciliation should proceed until the human ruling is
recorded.

## Blocks

- ADQ-05 completion.
- ADQ-12 child-run alignment portions that depend on canonical child-run naming/event categories.
- Any deliverable issue-readiness claim that treats DEL-03-04 interruption taxonomy or DEL-08-05
  denied-allocation semantics as closed.

## Non-Goals / Fences

This decision does not authorize provider/network expansion, remote MCP/plugins/tool search,
release/distribution posture, signing, notarization, publication, release-readiness claims, lifecycle
issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, or
R7 domain-engine implementation.

## Validation Implications

- If Option A is ruled: docs/governance validation plus focused runtime tests should be enough unless
  a doc edit changes an authority corpus member, in which case run the D-APP-38 `status`, `bump`, and
  `apply` sequence.
- If Option B or C is ruled: run `npm run typecheck`, focused runtime tests for event/schema/mapper
  behavior, `npm run harness:validate:section9`, and any additional UI/replay tests touched by the
  migration.

## Affected Files After Ruling

Likely Option A files:

- `docs/SPEC.md` and possibly `docs/TYPES.md` notes, with D-APP-38 corpus update if edited.
- DEL-03-01, DEL-03-03, DEL-03-04, and DEL-08-05 local kits under `execution/`.
- `frontend/docs/harness/runtime_engine_contract.md` and traceability docs if additional wording is
  needed.
- Focused tests only if current coverage does not already prove the ruled vocabulary.
