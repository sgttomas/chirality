# Guidance: DEL-08-01 Instruction Root Packaging and Agent Conformance

## Purpose

DEL-08-01 exists to make instruction-root packaging and agent conformance explicit and repeatable. It supports OBJ-007 by maintaining agent-suite integrity and governed subagent delegation without expanding authority, and OBJ-008 by keeping validation and instruction-root checks repeatable. Source: decomposition DEL-08-01, OBJ-007, OBJ-008.

## Principles

- Treat the instruction root as release-managed. The working root is mutable project truth; the instruction root is not ordinary task output. Source: `docs/DIRECTIVE.md` section 2.7; `docs/SPEC.md` section 1.1.
- Validate conformance from source files and registries, not from narrative counts. Source: `docs/PRD.md` KG-013 under D-APP-38.
- Keep the validator conservative. Missing source evidence becomes `TBD`, warning, or failure depending on the governing source; it must not be silently accepted. Source: `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1.
- Separate conformance validation from runtime capability implementation. DEL-08-01 verifies packaging and instruction conformance; DEL-08-04 and DEL-08-05 cover subagent bridge execution and child records. Source: decomposition PKG-08 rows.
- Preserve source authority labels. SPEC-backed requirements remain governing structure; PRD-backed requirements are current under the D-APP-38 authority corpus and `_REFERENCES.md` REF-006 MATCH state.

## Considerations

| Topic | Guidance | Evidence |
|---|---|---|
| Required assets | Use `docs/SPEC.md` section 1.1 as the primary required-entry list. Add PRD FR-058/KG-001 candidates under the current authority corpus. | `docs/SPEC.md` section 1.1; `docs/PRD.md` FR-058/KG-001 under D-APP-38 |
| Agent metadata | Validate both the compact header and the Agent Type table; each required row has a separate failure mode. | `docs/SPEC.md` sections 7.1 and 7.2 |
| Section markers | Marker checks should validate paired begin/end markers and section identity, not merely text presence. | `docs/SPEC.md` section 7.3 |
| Type 2 candidates | `AGENT_TYPE: 2` is required; `AGENT_CLASS: TASK` is preferred. Treat non-Type-2 delegation candidates as denial cases. | `docs/TYPES.md` Type 2 vocabulary; `docs/CONTRACT.md` K-SUBAGENT-1 |
| Write scopes | Validate declared `WRITE_SCOPE` values against vocabulary and fixture expected behavior. Runtime enforcement remains a separate hook/path-policy concern. | `docs/TYPES.md` section 3.2; `docs/CONTRACT.md` K-WRITE-1 |
| Unknown option keys | Warnings are preferable to behavior mutation. | `docs/SPEC.md` section 7.4 |

## Trade-offs

| Trade-off | Preferred approach | Rationale |
|---|---|---|
| Strict failure vs warning for PRD-only items | Treat current PRD-backed items as source-current but still separate source truth from implementation proof. | D-APP-38 resolves the former source warning without advancing lifecycle state. |
| Parser complexity vs text checks | Use structured parsing where feasible; allow simple text fixtures only for early validator scaffolding. | Section-marker and metadata checks have stable schemas in SPEC. |
| Broad packaging validation vs DEL-08-01 scope | Check instruction-root assets and conformance only; leave DMG packaging to DEL-09-04. | Decomposition separates DEL-08-01 from release packaging deliverables. |
| Runtime subagent behavior vs conformance fixtures | Include fail-closed fixture expectations, but do not implement the runtime bridge here. | DEL-08-04 owns `evaluateSubagentGovernance` bridge implementation. |

## Human Ruling Path

PRD-backed checks are current under D-APP-38 and `_REFERENCES.md` REF-006 MATCH. This resolves the former source-state warning only; it does not convert source requirements into implementation proof or lifecycle transition evidence. SPEC, CONTRACT, and TYPES remain the governing authority for instruction-root packaging and agent conformance where they define the narrower runtime contract.

## Examples

Example positive agent-instruction expectations:

- Filename matches `AGENT_*.md`.
- Header includes `[[DOC:AGENT_INSTRUCTIONS]]`.
- Header declares `AGENT_TYPE`.
- Agent Type table includes all required rows from SPEC section 7.2.
- Required marker pairs are present for `PROTOCOL`, `SPEC`, `STRUCTURE`, and `RATIONALE` when the contract requires those sections.

Example negative fixture expectations:

- Missing `AGENTS.md` in an instruction-root fixture is a packaging-readiness failure under SPEC section 1.1.
- Missing `WRITE_SCOPE` in an agent instruction is a conformance failure under SPEC section 7.2 and CONTRACT K-WRITE-1.
- A Type 2 subagent request without sealed context or approval metadata is denied under CONTRACT K-SEAL-1 and K-SUBAGENT-1.
- A PRD KG-001-only asset such as `tools/REGISTRY.md` is surfaced as a source-completeness item under the current authority corpus; implementation evidence still determines whether the item is satisfied.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | Former PRD source-state conflict resolved. | `_REFERENCES.md` REF-006 MATCH | D-APP-38 authority corpus v2 | Datasheet Attributes; Specification DEL0801-REQ004, DEL0801-REQ005, DEL0801-REQ012, DEL0801-REQ013; Guidance Considerations | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |
