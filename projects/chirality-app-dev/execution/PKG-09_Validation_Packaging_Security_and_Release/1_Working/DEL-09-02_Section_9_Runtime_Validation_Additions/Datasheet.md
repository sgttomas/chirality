# Datasheet: DEL-09-02 Section 9 Runtime Validation Additions

## Identification

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DeliverableID | DEL-09-02 |
| DeliverableName | Section 9 Runtime Validation Additions |
| ResponsibleParty | TBD |
| Type | TEST_SUITE |
| ContextEnvelope | M |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary scope | Add runtime validation IDs for provider-adapter conformance, first-adapter mapper, event log, settings isolation, permissions, MCP, hooks, compaction, and subagents. | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-02 |
| Anticipated artifacts | Section 9 validation IDs; harness runner updates; summary schema. | `_CONTEXT.md`; decomposition DEL-09-02 |
| Covered SOW items | SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063. | `_CONTEXT.md`; decomposition DEL-09-02 |
| Supported objectives | OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008. | `_CONTEXT.md`; decomposition DEL-09-02 |
| Baseline validation context | Section 8 validation already covers server reachability, session CRUD, boot error taxonomy, stream ordering, session persistence/resume, permission markers, interrupts, and SDK-native stream handling. | `docs/PRD.md` Section 12.3; `docs/SPEC.md` Section 19.2 |
| Section 9 validation ID source list | `section9.runtime_engine_contract`, `section9.sdk_turn_engine_event_log`, `section9.sdk_message_mapper`, `section9.session_event_replay`, `section9.reliance_boundary_register`, `section9.settingsources_isolation`, `section9.sdk_session_link_resume`, `section9.permission_overlay_hard_deny_precedence`, `section9.tool_runtime_read_file`, `section9.chirality_mcp_status_dependencies`, `section9.path_containment_hook`, `section9.instruction_root_protection_hook`, `section9.tool_result_budget`, `section9.context_compaction_boundary`, `section9.subagent_governance_hook`, `section9.domain_profile_validation`. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| PRD source status | Source warning only: expected PRD hash `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`; observed `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. Content is used with this warning recorded. | Assignment; `_REFERENCES.md` REF-006 |
| Source grounding | Requirements and validation IDs are limited to accessible local sources. Unsupported implementation details remain `TBD` or `ASSUMPTION`. | `skills/four-documents/SKILL.md`; `_REFERENCES.md` Notes |
| Dependency state | Declared upstream and downstream dependencies remain `TBD`; an extracted dependency register exists, but `_DEPENDENCIES.md` says not to compute blocked/available state until the project-level FULL_GRAPH register has been checked. | `_DEPENDENCIES.md` Dependency Tracking; `_DEPENDENCIES.md` Extracted Dependency Register |
| Domain-profile validation | `section9.domain_profile_validation` appears in the Section 9 list, but PRD says it applies after a governed domain-profile amendment enters scope. | `docs/PRD.md` Section 12.4 |

## Construction

| Component | Description | Source |
|---|---|---|
| Validation ID registry entries | Section 9 runtime IDs listed in PRD/SPEC should be represented in the harness validation catalog or equivalent registry. Exact file path is TBD. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |
| Harness runner updates | Runner must execute or report Section 9 validation IDs as runtime phases land. Exact runner entrypoint is TBD. | `_CONTEXT.md`; `docs/PRD.md` Section 12.4 |
| Summary schema | Summary output should distinguish Section 9 IDs and preserve stable premerge reporting conventions. Exact schema path is TBD. | `_CONTEXT.md`; `docs/PRD.md` Objective 7 and Section 12.4 |
| Runtime evidence checks | Checks should cover product-owned engine contract, canonical event mirror, SDK mapper, settings isolation, permissions, MCP, hooks, result budgets, compaction, and subagent governance. | `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3; `docs/CONTRACT.md` Sections 1.4-1.6 |
| Registry and summary location slots | Exact validation registry/manifest path, summary schema or fixture path, runner entrypoint, validation command, and validation output artifact remain `TBD` until implementation files are accepted. | `_SEMANTIC_LENSING.md` B-002/A-002/D-002 worklist; `Procedure.md` Steps and Records; `Specification.md` Documentation |

## References

| RefID | Source | Notes |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Runtime events, reliance boundaries, SDK boundary posture, capability-forward policy with explicit hard-deny precedence and MCP constraints. |
| REF-002 | `docs/CONTRACT.md` | Invariants for engine, events, permissions, MCP, hooks, paths, and subagents. |
| REF-003 | `docs/SPEC.md` | Runtime event schema, engine contract, MCP names, hook rules, Section 9 IDs. |
| REF-004 | `docs/TYPES.md` | HarnessEvent target, MCP names, hook terms, Section 9 vocabulary. |
| REF-005 | `docs/PLAN.md` | Roadmap sequencing and validation themes. |
| REF-006 | `docs/PRD.md` | Product requirements and Section 9 runtime validation additions; hash mismatch warning applies. |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context; no deliverable-specific requirement extracted. |
