# Datasheet: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-08-02 |
| DeliverableName | Persona Alias and Agent Matrix Routing Contract |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | UX_UI_SLICE |
| ContextEnvelope | S |
| ResponsibleParty | TBD |
| Current Lifecycle State at Draft | OPEN |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Scope summary | Keep UI aliases, canonical agent names, matrix routes, and persona resolution consistent. | `_CONTEXT.md`; decomposition entry DEL-08-02 |
| Anticipated artifacts | Alias resolver tests; route fixtures; matrix mapping tests. | `_CONTEXT.md`; decomposition entry DEL-08-02 |
| Covered scope items | SOW-005, SOW-006, SOW-017. | `_CONTEXT.md`; decomposition scope table |
| Supported objectives | OBJ-001, OBJ-007. | `_CONTEXT.md`; decomposition entry DEL-08-02 |
| UI alias map | `HELP -> HELP_HUMAN`; `ORCHESTRATE -> ORCHESTRATOR`; `AGGREGATE -> AGGREGATION`; `RECONCILING -> RECONCILIATION`; `AGENTS -> HELPS_HUMANS`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 |
| Matrix rows | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE`. | `docs/TYPES.md` Section 4.1; `docs/PRD.md` FR-007 |
| Matrix columns | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING`. | `docs/TYPES.md` Section 4.2; `docs/PRD.md` FR-007 |
| Matrix routing destinations | `NORMATIVE` and `EVALUATIVE` route to WORKBENCH; `OPERATIVE` routes to PIPELINE. | `docs/TYPES.md` Section 4.1; `docs/PRD.md` Section 7.2 and FR-008 |
| Persona filename target | Persona names resolve to `agents/AGENT_*.md`; missing personas return `PERSONA_NOT_FOUND`. | `docs/PRD.md` FR-025 |
| Persona fallback | Request/session persona falls back to `HELP_HUMAN` or configured default. | `docs/SPEC.md` Section 13.1 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source authority warning | `docs/PRD.md` has expected SHA `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` and observed SHA `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`; treated as a warning by dispatch. | `_REFERENCES.md`; ORCHESTRATOR dispatch |
| Governance posture | Unknown values remain `TBD`, and source conflicts must be surfaced rather than silently resolved. | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
| Route shape constraint | Existing harness route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/SPEC.md` Section 17.1 |
| Unsupported variants | Disabled or unsupported matrix/pipeline variants remain visible as coming soon rather than disappearing. | `docs/PRD.md` Section 7.2 and FR-011 |

## Construction

| Construct | Required Datasheet Value |
|---|---|
| Alias resolver | MUST encode only sourced UI alias mappings unless amended by governance. |
| Canonical agent name target | MUST resolve aliases and personas to canonical instruction-root agent names, with `agents/AGENT_<persona>.md` as the file contract. |
| Matrix mapping fixture | MUST cover the canonical 3x4 row/column vocabulary and row-to-surface routing. |
| Workbench route fixture | MUST preserve selected agent, row, and column context from route state or query parameters. |
| Pipeline route fixture | MUST distinguish operative category routing from interactive WORKBENCH persona routing. |
| Unspecified UI details | TBD until implementation evidence or human ruling defines exact component names, route query keys, and fixture file paths. |

## References

| RefID | Source | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Product boundaries and matrix/persona scope. |
| REF-002 | `docs/CONTRACT.md` | Invariants for non-invention, routing governance, and agent boundaries. |
| REF-003 | `docs/SPEC.md` | Runtime option fallback, persona composition, and API route stability. |
| REF-004 | `docs/TYPES.md` | Authoritative alias and matrix vocabulary. |
| REF-005 | `docs/PLAN.md` | Implementation sequencing context. |
| REF-006 | `docs/PRD.md` | Product requirements; hash mismatch warning applies. |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context. |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-08-02 scope, SOW links, objectives, artifacts. |
