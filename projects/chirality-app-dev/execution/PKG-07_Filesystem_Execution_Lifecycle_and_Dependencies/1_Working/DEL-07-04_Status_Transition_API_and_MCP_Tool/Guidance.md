# Guidance: DEL-07-04 Status Transition API and MCP Tool

## Purpose

This deliverable exists to make deliverable lifecycle state a product-owned filesystem contract rather than an inferred UI or runtime condition. The accepted SOFTWARE_DECOMP v3.2 entry defines the slice as parsing `_STATUS.md` and enforcing forward-only, actor-authorized transitions with approval SHA for human gates. The source documents reinforce that `_STATUS.md` is canonical and that status transition behavior is a governed API/MCP surface, not prompt-only convention.

## Principles

1. Treat `_STATUS.md` as the only lifecycle authority.
   Source: `docs/CONTRACT.md` Section 1.7 K-STATUS-1; `docs/SPEC.md` Section 4.3.

2. Keep transition enforcement in code and tests.
   Prompt instructions may reinforce the behavior, but `docs/DIRECTIVE.md` says runtime code enforces safety and prompt instructions are not sufficient enforcement.

3. Preserve forward-only lifecycle movement.
   Source: `docs/SPEC.md` Section 4.3 and `docs/PRD.md` Section 8.9 FR-053.

4. Treat human gates as non-delegable.
   Agents, SDKs, tools, validators, and runtime events must not author binding approval records. Source: `docs/CONTRACT.md` Section 1.2 K-AUTH-1/K-GATE-1 and `docs/DIRECTIVE.md` Human authority.

5. Make MCP a governed transport.
   `mcp__chirality__status_transition` should not bypass permission, hook, path, redaction, or event logging policy. Source: `docs/CONTRACT.md` Section 1.6 K-MCP-1 and `docs/DIRECTIVE.md` Design commitments.

6. Keep dependency behavior separate.
   Dependency register behavior belongs primarily to DEL-07-05; this deliverable may share API patterns but should not absorb `Dependencies.csv` reader/writer scope. Source: decomposition DEL-07-04/DEL-07-05 split and `docs/PRD.md` Section 8.9 FR-055 through FR-057.

## Considerations

- Actor authorization should be explicit enough that unsupported actors fail closed. SPEC Section 4.3 lists authorized actors by transition; implementation-specific actor identity mapping remains `TBD`.
- Approval SHA validation should follow the PRD acceptance detail of a 7-64 character hex SHA-like token for transitions to `CHECKING` or `ISSUED`. PRD hash mismatch warning applies.
- The API and MCP tool should return structured denial information for invalid state, backward transition, unauthorized actor, missing approval SHA, invalid approval SHA, path/policy denial, and malformed `_STATUS.md`. Exact response shape is `TBD`.
- `INITIALIZED -> SEMANTIC_READY` is optional according to `docs/TYPES.md` Section 4.1; if semantic lensing is skipped, deliverables may transition directly from `INITIALIZED -> IN_PROGRESS` under SPEC actor rules.
- Status transition writes should remain subject to project-root containment and instruction-root protection expectations from the filesystem and permission surfaces. Source: `docs/CONTRACT.md` K-PATH-2 and K-MCP-1; `docs/PLAN.md` R3 implementation targets.
- Runtime/event records can support audit, but they are not substitutes for accepted project-state files or human approval records. Source: `docs/DIRECTIVE.md` runtime event discussion and human authority section.

## Trade-offs

| Topic | Guidance | Source |
|---|---|---|
| API versus MCP | Maintain both surfaces because the PRD/SPEC list working-root API endpoints and Chirality MCP tools. Keep validation shared or behaviorally equivalent to avoid drift. | `docs/PRD.md` API inventory; `docs/SPEC.md` Sections 13 and 14.2 |
| SHA gate strictness | Prefer strict SHA-like validation for human gate transitions; if a human chooses alternate immutable evidence, capture it as a deliberate policy extension rather than silently accepting arbitrary text. | `docs/PRD.md` Section 8.9 FR-054; `docs/DIRECTIVE.md` Human authority |
| Parser tolerance | Be tolerant enough to read the SPEC format, but report malformed or ambiguous status files rather than inferring state from other files. | `docs/SPEC.md` Section 4.1; `docs/CONTRACT.md` K-STATUS-1 |
| Semantic-ready shortcut | Support the optional `INITIALIZED -> IN_PROGRESS` route when semantic lensing is skipped, but only under authorized actor rules. | `docs/TYPES.md` Section 4.1; `docs/SPEC.md` Section 4.3 |
| Event logs | Record tool/runtime outcomes for audit, but do not treat runtime events as approval records. | `docs/DIRECTIVE.md` Runtime session logs and human authority |

## Examples

| Scenario | Expected outcome | Source |
|---|---|---|
| Read a valid `_STATUS.md` with `Current State: INITIALIZED` | Status read returns `INITIALIZED`, last updated date, and history. | `docs/SPEC.md` Section 4.1; `docs/PRD.md` FR-052 |
| Transition `OPEN -> INITIALIZED` by authorized document-initialization actor | Transition may be accepted if path/policy checks pass. | `docs/SPEC.md` Section 4.3 |
| Transition `IN_PROGRESS -> CHECKING` without approval SHA | Transition is denied. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` FR-054 |
| Transition `CHECKING -> ISSUED` with a non-hex approval token | Transition is denied under PRD acceptance criterion. | `docs/PRD.md` FR-054 |
| Transition `SEMANTIC_READY -> INITIALIZED` | Transition is denied as backward movement unless a human explicitly amends the record. | `docs/SPEC.md` Section 4.3 |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| TBD | No source conflict identified during P1/P2 drafting. | TBD | TBD | TBD | TBD | TBD |

## Source Warning

`docs/PRD.md` is listed as `HASH_MISMATCH` in `_REFERENCES.md`. Use PRD acceptance details as warned source material until the reference hash is reconciled.
