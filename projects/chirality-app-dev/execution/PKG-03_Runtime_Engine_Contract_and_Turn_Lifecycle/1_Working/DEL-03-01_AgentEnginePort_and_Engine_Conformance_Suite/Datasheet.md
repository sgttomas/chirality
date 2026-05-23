# Datasheet: DEL-03-01 AgentEnginePort and Engine Conformance Suite

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-03-01 |
| DeliverableName | AgentEnginePort and Engine Conformance Suite |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | API_CONTRACT |
| ContextEnvelope | M |
| CoversScopeItems | SOW-037 |
| SupportsObjectives | OBJ-002 |
| AnticipatedArtifacts | `agent-engine-port.ts`; runtime contract docs; conformance tests |

Source: `_CONTEXT.md` and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` section "PKG-03 Runtime Engine Contract and Turn Lifecycle".

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Contract identity | `AgentEnginePort` / `RuntimeEngineContract` | `docs/SPEC.md` section 10.1; `docs/TYPES.md` section 7.1 |
| Contract ownership | Chirality owns the runtime contract; SDK APIs do not define public harness semantics. | `docs/DIRECTIVE.md` section 2.8; `docs/CONTRACT.md` K-ENGINE-1 |
| Adapter role | `EngineAdapter` is provider/SDK-specific implementation behind `AgentEnginePort`. | `docs/TYPES.md` section 7.1; `docs/SPEC.md` section 10.3 |
| Primary operation | `runTurn(input: TurnInput): AsyncIterable<UIEvent>` | `docs/SPEC.md` section 10.2 |
| Optional operation | `interrupt?(sessionId: string): Promise<void>` | `docs/SPEC.md` section 10.2 |
| Browser stream contract | `UIEvent` stream using stable SSE names. | `docs/SPEC.md` section 11; `docs/TYPES.md` section 7.4 |
| Canonical runtime record | `HarnessEvent` records in product-owned event JSONL. | `docs/SPEC.md` section 9; `docs/TYPES.md` section 7.3 |
| Required conformance subject | Stub adapter and SDK-backed adapter. | `docs/SPEC.md` section 10.3; `docs/PRD.md` section 12.5 |
| Production-default gate | SDK-backed adapter must pass engine conformance before default production use. | `docs/CONTRACT.md` K-ENGINE-2; `docs/PRD.md` FR-123 |

## Conditions

| Condition | Requirement / Constraint | Source |
|---|---|---|
| Provider-neutral core | Public APIs, canonical event schemas, session storage contracts, permission decision records, and governance rules must not become SDK-shaped. | `docs/DIRECTIVE.md` section 2.10; `docs/CONTRACT.md` K-ENGINE-4 |
| Route compatibility | Existing `/api/harness/*` route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/PRD.md` section 9.1; `docs/SPEC.md` section 10.4 |
| SSE compatibility | Browser-facing SSE event names remain compatible during SDK adoption. | `docs/SPEC.md` section 11; `docs/PRD.md` section 9.3 |
| Terminal outcomes | Accepted turns must persist terminal success, failure, cancellation, or interruption outcomes. | `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-123 |
| Accepted-turn persistence | Accepted user input must be persisted before SDK/model execution begins. | `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` section 12.6 |
| SDK metadata boundary | SDK identifiers, message names, permission modes, tool names, transcript paths, and session IDs are adapter metadata. | `docs/DIRECTIVE.md` section 2.10; `docs/SPEC.md` section 10.3 |
| Source-state warning | `docs/PRD.md` is accessible but `_REFERENCES.md` reports HASH_MISMATCH for REF-006. Content derived from PRD slices should be reconfirmed before acceptance. | `_REFERENCES.md` REF-006 |

## Construction

| Construct | Target / Shape | Source / Status |
|---|---|---|
| Runtime contract module | `agent-engine-port.ts` or equivalent product-owned runtime contract. | `execution/_Decomposition/...v3_2.md` DEL-03-01; `docs/PLAN.md` R1; `docs/PRD.md` R1 |
| TypeScript interface | `AgentEnginePort` with `runTurn` and optional `interrupt`. | `docs/SPEC.md` section 10.2 |
| Turn input type | Must include active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable. | `docs/SPEC.md` section 10.2 |
| Conformance suite | `engine-conformance.ts` or equivalent tests for stub and SDK-backed adapters. | `docs/PLAN.md` R1; `docs/PRD.md` section 12.5 |
| Stub adapter | Deterministic adapter retained for tests. | `docs/SPEC.md` section 10.3 |
| SDK-backed adapter | Provider implementation behind the product-owned contract. | `docs/SPEC.md` section 10.3 |
| Exact final source path | CANDIDATE / TBD: `docs/PRD.md` R1 lists `frontend/src/lib/harness/agent-engine-port.ts` or equivalent, while `docs/PLAN.md` R1 and the decomposition name only `agent-engine-port.ts` or equivalent. Treat the frontend path as a candidate until implementation accepts final placement. | `docs/PRD.md` R1 implementation targets; `docs/PLAN.md` R1 implementation targets; `execution/_Decomposition/...v3_2.md` DEL-03-01 |

## References

| RefID | Source | Status / Note |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH; sections 2.8-2.11 used. |
| REF-002 | `docs/CONTRACT.md` | MATCH; sections 1.4-1.5 and enforcement map used. |
| REF-003 | `docs/SPEC.md` | MATCH; sections 9-13 used. |
| REF-004 | `docs/TYPES.md` | MATCH; sections 7 and 12 used. |
| REF-005 | `docs/PLAN.md` | MATCH; sections 2-4, 6.2, and 8 used. |
| REF-006 | `docs/PRD.md` | HASH_MISMATCH in `_REFERENCES.md`; sections 8.16, 9, 12, and 13 used with source-state warning. |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | MATCH; not used for content requirements beyond decomposition provenance. |
