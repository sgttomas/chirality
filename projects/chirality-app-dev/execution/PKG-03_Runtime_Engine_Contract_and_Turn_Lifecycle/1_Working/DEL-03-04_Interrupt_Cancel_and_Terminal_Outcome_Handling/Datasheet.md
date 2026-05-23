# Datasheet: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-03-04 |
| DeliverableName | Interrupt, Cancel, and Terminal Outcome Handling |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-012, SOW-015 |
| SupportsObjectives | OBJ-002, OBJ-003 |
| AnticipatedArtifacts | Interrupt tests; cancel cleanup tests; terminal event mapper |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary runtime owner | `TurnEngine` owns the harness turn lifecycle; `/api/harness/turn` remains a transport adapter. | `docs/PRD.md` Section 8.12, FR-070 and FR-071; `docs/SPEC.md` Section 10.4 |
| Engine boundary | `AgentEnginePort` / `RuntimeEngineContract` is the product-owned boundary for turn execution, UI events, canonical `HarnessEvent`s, interrupt behavior, and terminal outcomes. | `docs/PRD.md` Section 6.1; `docs/SPEC.md` Section 10.1 |
| Public interrupt route | `/api/harness/interrupt` interrupts the active turn. | `docs/PRD.md` Section 8.3, FR-019; `docs/SPEC.md` Section 17.1 |
| Turn stream route | `/api/harness/turn` executes a turn and streams browser-facing UI events over SSE. | `docs/PRD.md` Section 8.3, FR-017; `docs/SPEC.md` Section 17.1 |
| Session concurrency constraint | Only one active turn may run per session; concurrent attempts return `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3, FR-018 |
| Accepted-turn durability | Accepted user input must be persisted before model/provider execution so an interrupted or killed turn is recoverable. | `docs/PRD.md` Section 8.3, FR-021; `docs/CONTRACT.md` Section 1.5, K-EVENT-2 |
| Terminal outcome durability | Every accepted turn must end with a durable success, failure, cancellation, or interruption outcome. | `docs/CONTRACT.md` Section 1.5, K-EVENT-3; `docs/PRD.md` Section 8.3, FR-022; `docs/SPEC.md` Section 10.1 |
| Product-owned audit mirror | `.chirality/sessions/<id>/events.jsonl` is the canonical Chirality runtime audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` Section 1.5, K-EVENT-4; `docs/SPEC.md` Section 8.4 |
| Browser event compatibility | Existing SSE event names must remain compatible during SDK adoption. | `docs/SPEC.md` Section 11 |
| PRD source state | `docs/PRD.md` is accessible but hash-mismatched against `_REFERENCES.md`; use as source-state warning, not as rejection. | `_REFERENCES.md` REF-006 |

## Conditions

| Condition | Required Handling | Source |
|---|---|---|
| User interrupt | `POST /api/harness/interrupt` aborts the active provider request and yields interrupted `process:exit`; terminal persistence taxonomy is TBD pending conflict resolution. | `docs/PRD.md` Section 8.3, FR-019; `docs/PRD.md` Section 7.4 |
| Client disconnect | Stream cleanup must occur; once the event log exists, client disconnect cleanup must record cancellation. | `docs/SPEC.md` Section 11 |
| Runtime/provider failure after input acceptance | Accepted input remains recoverable and replay shows terminal failure/cancellation status. | `docs/PRD.md` Section 7.10 |
| Concurrent turn attempt | Must not create a second active turn for the same session; return `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3, FR-018 |
| Malformed trailing event log write | Replay ignores malformed trailing lines and preserves valid prior events. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 7.10 |
| Secret-bearing error or payload | Runtime events, logs, tool artifacts, and provider errors must redact secrets and avoid storing API keys. | `docs/CONTRACT.md` Section 1.5, K-EVENT-6; `docs/SPEC.md` Section 9.2 |

## Construction

| Component / Artifact | Construction Target | Status |
|---|---|---|
| Interrupt tests | Cover active-turn interrupt route, provider abort propagation, SSE `process:exit`, lock release, and durable terminal outcome. | ASSUMPTION: exact test file path TBD |
| Cancel cleanup tests | Cover client disconnect and cancellation-signal cleanup, lock release, and durable cancellation record once event log exists. | ASSUMPTION: exact test file path TBD |
| Terminal event mapper | Map completion, failure, cancellation, and interruption handling into browser `UIEvent`s and persisted `HarnessEvent`s without SDK-shaped public semantics. | ASSUMPTION: exact module path TBD |
| Lock cleanup verification | Confirm interrupt, disconnect, failure, and cancellation all release session active-turn state. | Supported by DEL-03-04 scope and PRD FR-018/FR-019/FR-022 |
| Event log verification | Confirm terminal records append as newline-delimited JSONL with unique event IDs and no secrets. | `docs/SPEC.md` Section 9.2 |

## References

- `docs/CONTRACT.md` Section 1.4 and 1.5, especially K-ENGINE-1 through K-ENGINE-4 and K-EVENT-2 through K-EVENT-6.
- `docs/SPEC.md` Sections 8.4, 9, 10, 11, 17.1, 19.2, and 19.3.
- `docs/TYPES.md` Sections 7.1 through 7.4.
- `docs/PRD.md` Sections 5, 6.1, 7.4, 7.10, 8.3, and 8.12. Source-state warning: REF-006 is HASH_MISMATCH in `_REFERENCES.md`.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-03 / DEL-03-04 and SOW-012 / SOW-015 rows.
