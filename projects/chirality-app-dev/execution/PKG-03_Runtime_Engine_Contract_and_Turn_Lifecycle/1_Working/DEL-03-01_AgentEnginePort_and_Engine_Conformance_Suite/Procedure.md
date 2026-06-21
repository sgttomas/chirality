# Procedure: DEL-03-01 AgentEnginePort and Engine Conformance Suite

## Purpose

Define and verify the product-owned engine boundary and conformance suite for stub and SDK-backed runtime adapters while preserving Chirality-owned semantics, stable route/SSE behavior, and adapter replaceability.

Sources: `docs/SPEC.md` sections 10-12; `docs/PRD.md` sections 8.16, 9, 12, and 13; `docs/CONTRACT.md` sections 1.4-1.5.

## Prerequisites

| Prerequisite | Status / Note |
|---|---|
| Deliverable state allows drafting | Current `_STATUS.md` state was `OPEN` before this P1/P2 run. |
| Authoritative sources available | REF-001 through REF-007 are locally accessible. |
| PRD source state acknowledged | REF-006 is MATCH under the current D-APP-38 authority corpus. |
| Declared upstream dependencies | `_DEPENDENCIES.md` lists declared upstream as TBD; no accepted dependency edges have been extracted yet. |
| SDK probe details | TBD; exact SDK message categories, session store behavior, and interrupt behavior depend on DEL-04-01. |
| Acceptance authority for staged SDK cases | TBD; human acceptance is required for any `BLOCKED_TBD` SDK-backed conformance case until DEL-04-01 supplies the missing probe detail. |

## Steps

1. Confirm the scope boundary.
   - Use DEL-03-01 only for the engine contract and conformance suite.
   - Keep `TurnEngine` implementation, route adapter fixtures, SDK probe decision, and event store implementation in their owning deliverables unless needed as conformance references.

2. Draft the runtime contract.
   - Define `AgentEnginePort` / `RuntimeEngineContract` as product-owned.
   - Include `startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>`.
   - Include optional `interrupt?(sessionId: string): Promise<void>` when adapter support exists.
   - Define `TurnInput` with active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable.

3. Define adapter boundary rules.
   - Keep SDK/provider message names, tool names, permission modes, transcript paths, hook names, and session IDs outside public APIs and canonical event fields except under explicit adapter metadata.
   - Preserve the stub adapter as deterministic conformance baseline.
   - Mark exact SDK-backed fixture details as `TBD` until DEL-04-01 confirms SDK behavior.

4. Specify the conformance suite.
   - Test accepted-turn persistence before SDK/model execution.
   - Test terminal success, failure, cancellation, and interruption persistence.
   - Test browser SSE compatibility and stable UI event names.
   - Test SDK message mapping into product-owned UI/runtime events.
   - Test permission denial and permitted tool exposure behavior at the contract boundary.
   - Test session resume/linkage metadata without making SDK transcripts canonical.
   - Test redaction and absence of SDK-shaped leakage in public contracts and canonical events.

5. Align with route and event contracts.
   - Confirm `/api/harness/turn` remains a transport adapter.
   - Confirm browser-facing event names remain `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and the additive redacted `harness:event` bridge.
   - Confirm canonical runtime records use `HarnessEvent` shape and product-owned event categories.

6. Record fallback and source-state caveats.
   - Document fallback criteria if SDK behavior cannot satisfy a product-critical boundary.
   - If future authority documents change, run the D-APP-38 corpus bump/apply before acceptance.

7. Prepare deliverable records.
   - Produce or update runtime contract docs.
   - Produce or update `agent-engine-port.ts` or equivalent.
   - Produce or update engine conformance tests.
   - Link the conformance suite to `section9.runtime_engine_contract` once Section 9 validation exists.

## Verification

| Check | Expected Result |
|---|---|
| Contract shape check | `AgentEnginePort` exposes `startTurn` and optional `interrupt` with inputs/outputs matching `docs/SPEC.md` section 10.2. |
| Provider-neutrality check | Public APIs and canonical `HarnessEvent` fields do not contain SDK-shaped names except explicit adapter metadata. |
| Stub conformance | Stub adapter passes the same conformance suite used for SDK-backed adapter where applicable. |
| SDK-backed conformance | SDK-backed adapter passes before default production enablement; cases blocked by SDK probe details remain `TBD` until DEL-04-01 closes. |
| SSE compatibility | Browser event names and `/api/harness/turn` route shape remain stable. |
| Event persistence | Accepted turn and terminal outcomes are persisted in Chirality-owned event form. |
| Redaction | Provider/SDK errors and runtime records do not store API keys or secrets. |
| Authority-corpus check | REF-006 is reconciled under D-APP-38; future authority-doc edits trigger corpus bump/apply. |

## Records

Required records for closure:

- Runtime contract source file: `agent-engine-port.ts` or equivalent.
- Runtime contract documentation.
- Engine conformance test file or suite.
- Test output showing stub adapter pass.
- Test output showing SDK-backed adapter pass, or a `BLOCKED_TBD` record naming the DEL-04-01 blocker, affected conformance case, fallback/risk note, and accepting party status.
- Conformance evidence matrix covering adapter subject, case coverage, result status, test output path or `TBD`, fallback/risk note, D-APP-38 authority-corpus status, and Section 9 linkage status.
- Section 9 validation linkage when `section9.runtime_engine_contract` exists, or a `TBD` linkage record naming DEL-09-02 as the unavailable validation surface.
