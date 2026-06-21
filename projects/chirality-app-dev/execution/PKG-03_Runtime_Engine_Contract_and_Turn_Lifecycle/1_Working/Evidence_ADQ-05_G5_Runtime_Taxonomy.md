# Evidence ADQ-05 - G5 Runtime Taxonomy Reconciliation

**Date:** 2026-06-21
**Queue item:** ADQ-05
**Ruling basis:** D-APP-40 Option B

## Scope

ADQ-05 reconciles G5 runtime naming and taxonomy after the D-APP-40 ruling:

- `AgentEnginePort.startTurn(input)` is the canonical adapter stream method.
- `TurnEngine.runTurn(request)` remains the route-independent product lifecycle method.
- `harness:event` remains the additive public `UIEvent` bridge for redacted provider-neutral
  `HarnessEvent` records.
- Explicit user interruption persists terminal `turn.interrupted` and keeps browser-facing
  `process:exit` with `interrupted: true`.
- `turn.cancelled` remains reserved for non-user cancellation such as disconnect or system
  cancellation.
- `ChildRunRecord.childRunId` is the canonical child-run record/key.
- Denied subagent attempts require a denied child-run record only after the runtime reaches the
  child-run record layer; earlier denials may remain permission/hook evidence only.

This evidence does not approve provider/network expansion, remote MCP/plugins/tool search,
release/distribution posture, signing, notarization, publication, release-readiness claims, lifecycle
issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, or
R7 domain-engine implementation.

## Implementation Changes

| Surface | Change |
|---|---|
| Runtime event schema | Added `turn.interrupted` to `HARNESS_EVENT_TYPES`. |
| Claude Agent SDK manager | Explicit interrupt paths now bridge/persist `interruption.completed` then `turn.interrupted`, followed by `process:exit` with `exitCode: 130` and `interrupted: true`. |
| Direct Anthropic manager | Explicit interrupt paths now bridge/persist `interruption.completed` then `turn.interrupted`, followed by `process:exit` with `exitCode: 130` and `interrupted: true`. |
| Stub manager | Explicit interrupt paths now bridge `interruption.completed` then `turn.interrupted` to the live route stream before `process:exit`; the stub still does not claim durable event persistence. |
| Route/engine tests | Interrupt route and engine conformance tests assert `turn.interrupted` evidence while preserving public `process:exit` behavior. |
| Authority docs | `docs/PRD.md`, `docs/SPEC.md`, and `docs/TYPES.md` now include `turn.interrupted`, `harness:event`, and the canonical adapter `startTurn` method where applicable. D-APP-38 authority corpus was bumped to `v2` and applied to deliverable `_REFERENCES.md` rows. |
| Local kits | DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-04, DEL-08-04, and DEL-08-05 local kits and assessments now cite D-APP-40/D-APP-38 and no longer treat the resolved taxonomy/naming/source-state issues as open. |

## Validation Results

Validation performed for this tranche:

- `npm run test -- --testTimeout=15000 src/__tests__/lib/engine-conformance.test.ts src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts src/__tests__/api/harness/routes.test.ts src/__tests__/lib/session-events.test.ts src/__tests__/lib/agent-engine-port.test.ts src/__tests__/lib/agent-runtime-contract.test.ts src/__tests__/lib/sdk-message-mapper.test.ts` - passed 7 files / 144 tests.
- `npm run typecheck` - passed.
- `npm run harness:validate:section9` - passed 13 Section 9 checks.
- `npm run test -- --testTimeout=15000` - passed 76 files / 521 tests.
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` before bump - found expected drift in `docs/SPEC.md`, `docs/TYPES.md`, and `docs/PRD.md`.
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py bump --date 2026-06-21 --reason "ADQ-05 D-APP-40 runtime taxonomy reconciliation updated PRD, SPEC, and TYPES."` - bumped corpus to `v2`.
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py apply` - reconciled 153 reference rows across 51 deliverable `_REFERENCES.md` files to corpus `v2`.
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py audit` - all deliverable reference rows reconciled to corpus `v2`.
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` after bump/apply - no drift.
- Targeted stale-term scan over ADQ-05 active docs - no active-current hits outside historical `_run_records`, parser tests, and intended `TurnEngine.runTurn` lifecycle references.
- `git diff --check` - passed.

## Remaining Residuals

ADQ-05 closes the G5 method/event/child-run taxonomy findings. It does not close these residuals:

- client-disconnect durable cancellation persistence;
- accepted-input recovery semantics for failed/interrupted turns;
- child-output artifact materialization/redaction proof;
- broader packaged/live workflow evidence;
- any lifecycle issuance or release/distribution posture.
