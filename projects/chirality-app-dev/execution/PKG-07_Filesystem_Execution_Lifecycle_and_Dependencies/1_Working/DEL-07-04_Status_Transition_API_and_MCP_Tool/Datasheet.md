# Datasheet: DEL-07-04 Status Transition API and MCP Tool

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-07-04 |
| DeliverableName | Status Transition API and MCP Tool |
| PackageID | PKG-07 |
| PackageName | Filesystem Execution, Lifecycle, and Dependencies |
| DecompositionVariant | SOFTWARE_DECOMP |
| RuntimeDispatchVariant | SOFTWARE |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-028 |
| SupportsObjectives | OBJ-006 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Parse `_STATUS.md` and enforce lifecycle transitions. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-07-04 |
| Canonical state source | `_STATUS.md` is the canonical lifecycle state file for each deliverable. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1; `docs/SPEC.md` Section 4.3 |
| Status file fields | Parser must read `Current State`, `Last Updated`, and history. | `docs/PRD.md` Section 8.9 FR-052; `docs/SPEC.md` Section 4.1 |
| Valid lifecycle chain | `OPEN -> INITIALIZED -> SEMANTIC_READY -> IN_PROGRESS -> CHECKING -> ISSUED`. | `docs/SPEC.md` Section 4.2; `docs/TYPES.md` Section 4.1 |
| Transition rule | Transitions are forward-only and actor-authorized. | `docs/PRD.md` Section 8.9 FR-053; `docs/SPEC.md` Section 4.3 |
| Human gate evidence | Transitions to `CHECKING` or `ISSUED` require approval SHA evidence; PRD acceptance calls for a 7-64 character hex SHA-like token. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-054 |
| API surface | `GET /api/working-root/deliverable/status` reads status; `POST /api/working-root/deliverable/status/transition` applies allowed transition. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
| MCP surface | `mcp__chirality__status_read` reads `_STATUS.md`; `mcp__chirality__status_transition` applies authorized lifecycle transition with approval SHA where required. | `docs/SPEC.md` Section 14.2; `docs/TYPES.md` Section 8.4 |
| MCP boundary | MCP is a transport, not a bypass; in-process Chirality MCP tools pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/DIRECTIVE.md` Design commitments |

## Conditions

| Condition | Status |
|---|---|
| Source hash warning | `docs/PRD.md` is accessible but listed as `HASH_MISMATCH` in `_REFERENCES.md`; PRD-derived claims are used with this warning. |
| Dependency inputs | `_DEPENDENCIES.md` declares no accepted upstream or downstream edges yet. |
| Ownership | Responsible party is `TBD`; `_CONTEXT.md` says to preserve `ResponsibleParty: TBD` until human assignment. |
| Semantic lensing | `_SEMANTIC.md` is `NOT_GENERATED`; this P1/P2 run does not use semantic lensing. |
| Existing implementation path | TBD. Source documents define required behavior but do not name the implementation files for this slice. |
| Variant naming note | `SOFTWARE_DECOMP` names the accepted decomposition family in this deliverable context; `SOFTWARE` is the four-documents runtime dispatch token. |

## Construction

| Component | Expected role | Source grounding |
|---|---|---|
| Status parser | Read `_STATUS.md`, extract current state, last updated date, and history entries. | `docs/SPEC.md` Section 4.1; `docs/PRD.md` Section 8.9 FR-052 |
| Transition validator | Enforce valid states, forward-only ordering, actor authorization, and approval SHA requirements for human gates. | `docs/SPEC.md` Sections 4.2-4.3; `docs/PRD.md` Section 8.9 FR-053/FR-054 |
| Status API | Provide read and transition endpoints for deliverable status contract access. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
| Chirality MCP tools | Expose status read/transition through in-process deterministic `mcp__chirality__*` tooling. | `docs/SPEC.md` Section 14.2; `docs/PRD.md` Section 8.13 FR-119 |
| Tests | Cover parser behavior, actor authorization, forward-only rejection, approval SHA gate, and MCP/API routing. | `docs/PRD.md` Section 8.9 FR-052 through FR-054; decomposition DEL-07-04 anticipated artifacts |

## References

| RefID | SourcePath | SectionRef | Use |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Human authority and design commitments | Approval and MCP boundary posture |
| REF-002 | `docs/CONTRACT.md` | Sections 1.2, 1.6, 1.7 | Binding invariants for approvals, status, MCP wrappers |
| REF-003 | `docs/SPEC.md` | Sections 4, 13, 14.2 | `_STATUS.md` format, lifecycle, API and MCP names |
| REF-004 | `docs/TYPES.md` | Sections 4.1, 8.4 | Lifecycle vocabulary and MCP tool naming |
| REF-005 | `docs/PLAN.md` | R3 implementation targets | Status transition tool target and approval SHA gate |
| REF-006 | `docs/PRD.md` | Sections 8.9, 8.13, API inventory | Product requirements; HASH_MISMATCH warning applies |
| REF-007 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PKG-07 DEL-07-04; SOW-028 | Scope and anticipated artifacts |

## Pass 3 Disposition Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| E-001 | Incorporated as a normalization note distinguishing the accepted decomposition family from the runtime dispatch token. | `_CONTEXT.md` Identification; `_SEMANTIC_LENSING.md` header; `skills/four-documents/SKILL.md` runtime override values. |
