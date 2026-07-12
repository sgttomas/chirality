# Specification: DEL-03-01 AgentEnginePort and Engine Conformance Suite

## Scope

This deliverable defines the product-owned runtime boundary for harness turn execution and the conformance suite any engine adapter must satisfy before use as the default production path.

In scope:

- `AgentEnginePort` / `RuntimeEngineContract` API contract.
- Adapter boundary rules for stub and SDK-backed implementations.
- Conformance expectations for accepted-turn persistence, terminal outcomes, SSE compatibility, SDK message mapping, permission/tool boundary behavior, interrupt/cancel behavior, session resume/linkage, and redaction.
- Runtime contract documentation and tests associated with the contract.

Out of scope:

- SDK-specific message translation implementation details, except as conformance inputs and adapter-boundary expectations.
- Full `TurnEngine` extraction and session locking implementation, owned by DEL-03-02.
- Browser API/SSE route adapter fixtures, owned by DEL-03-03 except where conformance verifies compatibility.
- Interrupt/cancel cleanup implementation, owned by DEL-03-04 except where conformance verifies required adapter behavior.
- SDK probe/version decision details, owned by DEL-04-01.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-03-01; `docs/SPEC.md` sections 10-12; `docs/PRD.md` sections 8.16, 9, and 12.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-03-01-REQ-001 | Chirality SHALL define `AgentEnginePort` / `RuntimeEngineContract` separate from SDK APIs. | `docs/SPEC.md` section 10.1; `docs/PRD.md` FR-122 |
| DEL-03-01-REQ-002 | Public harness semantics SHALL remain Chirality-owned; SDK APIs, message names, transcript shape, and tool names SHALL NOT define public semantics. | `docs/DIRECTIVE.md` sections 2.8 and 2.10; `docs/CONTRACT.md` K-ENGINE-1 and K-ENGINE-4 |
| DEL-03-01-REQ-003 | `AgentEnginePort` SHALL expose `startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>`. | `docs/SPEC.md` section 10.2; D-APP-40 |
| DEL-03-01-REQ-004 | `AgentEnginePort` MAY expose `interrupt?(sessionId: string): Promise<void>` when the adapter can support interruption. | `docs/SPEC.md` section 10.2 |
| DEL-03-01-REQ-005 | `AgentEngineRunInput` SHALL carry active session identity, resolved runtime options, and content blocks; normalized project root, persona, mode, and attachment summaries are carried through `SessionRecord`/resolved options, while interrupt and stream cancellation are out of band. | `docs/SPEC.md` section 10.2 |
| DEL-03-01-REQ-006 | The contract SHALL cover accepted turn input, browser `UIEvent` yield, canonical `HarnessEvent` persistence, permission enforcement or invocation, permitted tool exposure, SDK session metadata linkage, interrupt/cancel behavior, and terminal outcomes. | `docs/SPEC.md` section 10.1; `docs/TYPES.md` section 7.1 |
| DEL-03-01-REQ-007 | SDK-specific names, IDs, permission modes, transcript paths, tool names, and hook names SHALL appear only as explicit adapter metadata. | `docs/SPEC.md` section 10.3; `docs/DIRECTIVE.md` section 2.10 |
| DEL-03-01-REQ-008 | The SDK-backed adapter SHALL pass the engine conformance suite before becoming the default production path. | `docs/CONTRACT.md` K-ENGINE-2; `docs/SPEC.md` section 10.3; `docs/PRD.md` FR-123 |
| DEL-03-01-REQ-009 | A deterministic stub adapter SHALL remain available for tests. | `docs/SPEC.md` section 10.3 |
| DEL-03-01-REQ-010 | Engine conformance tests SHALL cover accepted-turn persistence before SDK/model execution, terminal outcome persistence, SSE compatibility, SDK message mapping, permission denial, tool exposure, interrupt/cancel behavior, session resume, and redaction. | `docs/PRD.md` FR-123; `docs/PRD.md` section 12.5 |
| DEL-03-01-REQ-011 | The contract and tests SHALL preserve the stable browser SSE names: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and the additive redacted `harness:event` bridge. | `docs/SPEC.md` section 11; `docs/TYPES.md` section 7.4; D-APP-40 |
| DEL-03-01-REQ-012 | `/api/harness/turn` SHALL remain a transport adapter; runtime policy belongs behind the contract and `TurnEngine`, not in the route. | `docs/SPEC.md` section 10.4; `docs/PRD.md` section 9.1 |
| DEL-03-01-REQ-013 | The conformance suite SHALL reject provider-shaped leakage in public APIs and canonical `HarnessEvent` fields except as explicit adapter metadata. | `docs/PRD.md` section 12.5; `docs/CONTRACT.md` K-ENGINE-4 |
| DEL-03-01-REQ-014 | The contract documentation SHALL record fallback criteria when SDK behavior cannot satisfy or verify a product-critical boundary. | `docs/CONTRACT.md` K-ENGINE-5; `docs/PLAN.md` R0 acceptance; `docs/PRD.md` FR-126 |
| DEL-03-01-REQ-015 | Requirements derived from `docs/PRD.md` SHALL use the current D-APP-38 authority-corpus reference state. | `_REFERENCES.md` REF-006; D-APP-38 |

## Standards

| Standard / Source | Applicability |
|---|---|
| `docs/DIRECTIVE.md` sections 2.8-2.11 | Runtime ownership, reliance boundaries, provider-neutral core, product identity. |
| `docs/CONTRACT.md` sections 1.4-1.5 | Binding invariants for engine boundary and runtime events. |
| `docs/SPEC.md` sections 9-13 | Event schema, runtime engine contract, SSE names, SDK settings posture, runtime options/persona composition. |
| `docs/TYPES.md` section 7 | Canonical runtime vocabulary and type targets. |
| `docs/PLAN.md` R0/R1 | Roadmap and sequencing constraints for engine contract and conformance. |
| `docs/PRD.md` sections 8.16, 9, 12, and 13 | Product requirements and validation expectations; REF-006 is reconciled under D-APP-38. |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| REQ-001, REQ-002, REQ-007, REQ-013 | Type/API review and tests proving public contract types do not expose SDK-shaped names except adapter metadata. |
| REQ-003, REQ-004, REQ-005, REQ-006 | Unit tests around `AgentEnginePort`/`RuntimeEngineContract` type fixtures and adapter test harness inputs. |
| REQ-008, REQ-009, REQ-010 | Engine conformance suite runs against stub and SDK-backed adapters before production-default enablement. |
| REQ-011, REQ-012 | Integration or compatibility tests proving `/api/harness/turn` shape and browser SSE event names are unchanged. |
| REQ-014 | Runtime contract documentation includes fallback criteria and cross-reference to reliance-boundary register. |
| REQ-015 | D-APP-38 confirms the current `docs/PRD.md` authority-corpus state before closing the deliverable. |

## Documentation

Required deliverable artifacts:

- `agent-engine-port.ts` or equivalent product-owned runtime contract.
- Runtime contract documentation describing ownership, adapter boundary, input/output shape, and fallback criteria.
- Engine conformance suite covering stub and SDK-backed adapters.
- Test index or validation reference for `section9.runtime_engine_contract` once Section 9 runtime validation is implemented.

Conformance evidence schema:

- Adapter subject: `stub`, `SDK-backed`, or `blocked SDK-backed case`.
- Case coverage: accepted-turn persistence, terminal outcome persistence, SSE compatibility, SDK message mapping, permission denial, tool exposure, interrupt/cancel behavior, session resume/linkage, redaction, and SDK-shaped leakage checks.
- Result status: `PASS`, `FAIL`, or `BLOCKED_TBD`; blocked cases must name the missing DEL-04-01 probe detail or other upstream blocker.
- Closure evidence: test output path or `TBD`, runtime contract documentation link, fallback/risk note when a product-critical boundary cannot be verified, REF-006 human ruling status, and `section9.runtime_engine_contract` linkage status once available.

TBD:

- Final implementation path if not `frontend/src/lib/harness/agent-engine-port.ts`.
- Exact SDK-backed adapter fixture shape until DEL-04-01 confirms SDK probe details.
- Exact session-link metadata fields accepted by the conformance suite until DEL-04-01/DEL-05 work confirms transcript/store placement.
- Accepting party for staged SDK-dependent conformance cases beyond the current scripted adapter coverage.
- Section 9 runtime validation linkage remains through the current `section9.adapter_*` validation IDs until a later governed rename.

## Source-State Warning

D-APP-38 established the authority-corpus reference model. Current `_REFERENCES.md` records REF-006 as `MATCH`; future authority-document edits require a corpus bump/apply before acceptance.
