# Source Pack: SRC-DEL-DEL-09-02-SECTION-9-RUNTIME-VALIDATION-ADDITIONS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions/Datasheet.md

### Datasheet: DEL-09-02 Section 9 Runtime Validation Additions

#### Identification

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

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary scope | Add runtime validation IDs for provider-adapter conformance, first-adapter mapper, event log, settings isolation, permissions, MCP, hooks, compaction, and subagents. | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-02 |
| Anticipated artifacts | Section 9 validation IDs; harness runner updates; summary schema. | `_CONTEXT.md`; decomposition DEL-09-02 |
| Covered SOW items | SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063. | `_CONTEXT.md`; decomposition DEL-09-02 |
| Supported objectives | OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008. | `_CONTEXT.md`; decomposition DEL-09-02 |
| Baseline validation context | Section 8 validation already covers server reachability, session CRUD, boot error taxonomy, stream ordering, session persistence/resume, permission markers, interrupts, and SDK-native stream handling. | `docs/PRD.md` Section 12.3; `docs/SPEC.md` Section 19.2 |
| Section 9 validation ID source list | `section9.runtime_engine_contract`, `section9.sdk_turn_engine_event_log`, `section9.sdk_message_mapper`, `section9.session_event_replay`, `section9.reliance_boundary_register`, `section9.settingsources_isolation`, `section9.sdk_session_link_resume`, `section9.permission_overlay_hard_deny_precedence`, `section9.tool_runtime_read_file`, `section9.chirality_mcp_status_dependencies`, `section9.path_containment_hook`, `section9.instruction_root_protection_hook`, `section9.tool_result_budget`, `section9.context_compaction_boundary`, `section9.subagent_governance_hook`, `section9.domain_profile_validation`. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| PRD source status | Source warning only: expected PRD hash `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`; observed `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. Content is used with this warning recorded. | Assignment; `_REFERENCES.md` REF-006 |
| Source grounding | Requirements and validation IDs are limited to accessible local sources. Unsupported implementation details remain `TBD` or `ASSUMPTION`. | `skills/four-documents/SKILL.md`; `_REFERENCES.md` Notes |
| Dependency state | Declared upstream and downstream dependencies remain `TBD`; an extracted dependency register exists, but `_DEPENDENCIES.md` says not to compute blocked/available state until the project-level FULL_GRAPH register has been checked. | `_DEPENDENCIES.md` Dependency Tracking; `_DEPENDENCIES.md` Extracted Dependency Register |
| Domain-profile validation | `section9.domain_profile_validation` appears in the Section 9 list, but PRD says it applies after a governed domain-profile amendment enters scope. | `docs/PRD.md` Section 12.4 |

#### Construction

| Component | Description | Source |
|---|---|---|
| Validation ID registry entries | Section 9 runtime IDs listed in PRD/SPEC should be represented in the harness validation catalog or equivalent registry. Exact file path is TBD. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |
| Harness runner updates | Runner must execute or report Section 9 validation IDs as runtime phases land. Exact runner entrypoint is TBD. | `_CONTEXT.md`; `docs/PRD.md` Section 12.4 |
| Summary schema | Summary output should distinguish Section 9 IDs and preserve stable premerge reporting conventions. Exact schema path is TBD. | `_CONTEXT.md`; `docs/PRD.md` Objective 7 and Section 12.4 |
| Runtime evidence checks | Checks should cover product-owned engine contract, canonical event mirror, SDK mapper, settings isolation, permissions, MCP, hooks, result budgets, compaction, and subagent governance. | `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3; `docs/CONTRACT.md` Sections 1.4-1.6 |
| Registry and summary location slots | Exact validation registry/manifest path, summary schema or fixture path, runner entrypoint, validation command, and validation output artifact remain `TBD` until implementation files are accepted. | `_SEMANTIC_LENSING.md` B-002/A-002/D-002 worklist; `Procedure.md` Steps and Records; `Specification.md` Documentation |

#### References

| RefID | Source | Notes |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Runtime events, reliance boundaries, SDK boundary posture, capability-forward policy with explicit hard-deny precedence and MCP constraints. |
| REF-002 | `docs/CONTRACT.md` | Invariants for engine, events, permissions, MCP, hooks, paths, and subagents. |
| REF-003 | `docs/SPEC.md` | Runtime event schema, engine contract, MCP names, hook rules, Section 9 IDs. |
| REF-004 | `docs/TYPES.md` | HarnessEvent target, MCP names, hook terms, Section 9 vocabulary. |
| REF-005 | `docs/PLAN.md` | Roadmap sequencing and validation themes. |
| REF-006 | `docs/PRD.md` | Product requirements and Section 9 runtime validation additions; hash mismatch warning applies. |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context; no deliverable-specific requirement extracted. |

## Component: execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions/Guidance.md

### Guidance: DEL-09-02 Section 9 Runtime Validation Additions

#### Purpose

This deliverable turns the vNext runtime-governance requirements into Section 9 validation coverage. Its purpose is to make release readiness visible as SDK-backed runtime phases land, without treating SDK behavior as product truth unless Chirality contracts, event records, and tests verify the boundary.

#### Principles

- Validate product-owned contracts, not SDK implementation details. SDK names, sessions, transcripts, hooks, and messages may appear as adapter metadata, but Chirality `UIEvent`, `HarnessEvent`, permission, session, and governance contracts remain authoritative. Source: `docs/SPEC.md` Sections 9-10; `docs/CONTRACT.md` K-ENGINE-4.
- Adapter metadata is acceptable only when it helps prove or diagnose Chirality-owned behavior. SDK transcripts, sessions, hooks, and message names remain secondary unless imported into `HarnessEvent` form or mapped through product-owned APIs, which preserves release evidence under Chirality contracts rather than SDK-shaped truth. Source: `docs/CONTRACT.md` K-ENGINE-4 and K-SDK-3; `docs/SPEC.md` Sections 9-10.
- Keep Section 8 stable while Section 9 expands. Section 9 additions should not regress server reachability, session CRUD, boot taxonomy, stream ordering, persistence/resume, permissions markers, interrupts, or SDK-native stream handling. Source: `docs/PRD.md` Sections 12.3-12.4.
- Prefer explicit pending states over false pass/fail results for runtime phases that have not landed. Source: PRD Section 12.4 states IDs are added "as runtime phases land"; domain-profile validation is conditional on governed amendment.
- Treat PRD as source with a recorded hash warning. Do not erase the mismatch; use corroborating SPEC/CONTRACT/TYPES slices where possible.
- Keep `ResponsibleParty` as `TBD` until a human assigns ownership. Source: `_CONTEXT.md` Source Authority.

#### Considerations

Section 9 spans several packages and runtime concepts. The runner and summary schema should therefore make each validation ID independently reportable, with clear statuses such as pass, fail, pending, skipped, blocked, or gated. The exact status enum is TBD because no local source defines it. Until the enum is accepted, use these terms descriptively and avoid treating a pending, skipped, blocked, or gated item as a passing validation.

The validation set should distinguish:

- Contract presence checks: engine contract, mapper boundary, event schema, reliance register.
- Runtime behavior checks: event append/replay, settings isolation, permission denial, MCP wrapper behavior, hooks, result budgets, compaction, subagent governance.
- Conditional checks: `section9.domain_profile_validation`, which should remain pending or gated until a governed domain-profile amendment enters scope.

Where implementation files are not yet known, avoid binding tests to guessed paths. Use Section 9 IDs and source-defined contract names as the stable interface until the owning implementation deliverables establish file locations.

The summary schema should balance diagnostic evidence with release readability by carrying per-ID status, source reference, evidence artifact reference, and warning/blocker notes while keeping Section 8 and Section 9 outcomes distinguishable. Exact schema fields remain TBD; the guiding constraint is that release review can see readiness without reading raw fixture output, while auditors can still trace each result to evidence.

#### Trade-offs

| Topic | Guidance |
|---|---|
| ID completeness vs implementation readiness | Register all source-defined Section 9 IDs, but permit pending/gated status for IDs whose runtime phase is not implemented yet. |
| SDK conformance vs product conformance | Product conformance wins. Tests should assert Chirality-owned contracts and use SDK details only as observed inputs or adapter metadata. |
| Summary detail vs release readability | Store enough detail for diagnosis while preserving a stable summary artifact for premerge/release review. Exact schema remains TBD. |
| Broad Section 9 scope vs local deliverable bounds | Keep this deliverable focused on validation additions; defer implementation of runtime features to their owning deliverables. |
| Dependency extraction vs closure readiness | Treat extracted dependency rows as handoff context until accepted graph closure exists; do not block or pass this validation deliverable solely from dependency edges without project-level FULL_GRAPH review. |

#### Examples

Example validation record shape, ASSUMPTION based on anticipated "summary schema":

```json
{
  "id": "section9.permission_overlay_hard_deny_precedence",
  "status": "TBD",
  "evidence": [],
  "source": "docs/PRD.md Section 12.4; docs/CONTRACT.md K-PERM-1"
}
```

Example gating note for conditional domain validation:

```json
{
  "id": "section9.domain_profile_validation",
  "status": "pending_governed_amendment",
  "reason": "PRD Section 12.4 scopes this after a governed domain-profile amendment enters scope."
}
```

#### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-001 | PRD hash mismatch recorded in `_REFERENCES.md`, but assignment instructs treating it as source warning only. | `_REFERENCES.md` REF-006 | Assignment runtime override | All PRD-cited sections | Proceed with PRD as accessible source while preserving the warning and corroborating with SPEC/CONTRACT/TYPES where possible. | TBD |
| CONFLICT-002 | Section 9 includes `section9.domain_profile_validation`, but source states it applies only after governed domain-profile amendment enters scope. | `docs/SPEC.md` Section 19.3 | `docs/PRD.md` Section 12.4 | Datasheet Attributes; Specification Requirements; Procedure Steps | Include the ID in the registry but mark it pending/gated until amendment is accepted. | TBD |
| CONFLICT-003 | Declared upstream/downstream dependencies remain `TBD`, while `_DEPENDENCIES.md` now includes an extracted dependency register and warns not to compute blocked/available state until project-level graph checks run. | `_DEPENDENCIES.md` Declared Upstream/Downstream | `_DEPENDENCIES.md` Extracted Dependency Register | Datasheet Conditions; Procedure Prerequisites; Guidance Trade-offs | Use extracted rows as handoff context only; require accepted FULL_GRAPH closure before dependency state becomes implementation closure authority. | TBD |

## Component: execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions/Procedure.md

### Procedure: DEL-09-02 Section 9 Runtime Validation Additions

#### Purpose

Define the operational steps to produce and verify the Section 9 runtime validation additions for DEL-09-02 while preserving source-grounding, existing Section 8 behavior, and deliverable-local boundaries.

#### Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available in the deliverable folder.
- Authoritative source slices are available from `docs/PRD.md`, `docs/SPEC.md`, `docs/CONTRACT.md`, `docs/TYPES.md`, `docs/DIRECTIVE.md`, and the v3.2 software decomposition.
- Declared upstream and downstream dependencies remain `TBD`; an extracted dependency register exists, but do not compute blocked/available state until project-level FULL_GRAPH closure has been checked.
- PRD hash mismatch is recorded as a source warning only for this run.
- Responsible party remains `TBD`.

#### Steps

1. Confirm the Section 8 baseline remains visible in the validation suite: server reachable, session CRUD, boot error taxonomy, smoke stream ordering, session persistence/resume, permission markers, interrupt behavior, and SDK-native stream handling. Source: `docs/PRD.md` Section 12.3; `docs/SPEC.md` Section 19.2.
2. Add or update the Section 9 validation registry with each source-defined ID from PRD Section 12.4 and SPEC Section 19.3.
3. For each Section 9 ID, attach source references and a status. If the runtime phase is not implemented, use a pending, skipped, blocked, or gated status rather than inventing a passing test. Exact status enum is TBD; record the accepted enum or schema reference once available.
4. Implement or wire runner checks for IDs whose runtime surfaces exist:
   - `section9.runtime_engine_contract`: engine conformance and product-owned boundary checks.
   - `section9.sdk_turn_engine_event_log`, `section9.sdk_message_mapper`, `section9.session_event_replay`: event schema, mapper, append/replay, and transcript non-authority checks.
   - `section9.settingsources_isolation`: shipped settings-source posture check.
   - `section9.permission_overlay_hard_deny_precedence`: capability-forward policy with explicit hard-deny precedence and `allowedTools` non-boundary checks.
   - `section9.tool_runtime_read_file` and `section9.chirality_mcp_status_dependencies`: tool exposure and MCP wrapper checks.
   - `section9.path_containment_hook` and `section9.instruction_root_protection_hook`: hook/path checks.
   - `section9.tool_result_budget`: inline/preview/artifact/redaction check.
   - `section9.context_compaction_boundary`: compaction mirror check.
   - `section9.subagent_governance_hook`: fail-closed subagent governance check.
5. Gate `section9.domain_profile_validation` until a governed domain-profile amendment enters scope.
6. Update the harness runner so Section 9 IDs are executed or reported consistently with the existing premerge validation flow. Exact runner entrypoint, command, and file path are TBD.
7. Update the registry/manifest so every Section 9 ID has source reference, status metadata, and evidence or blocker reference. Exact registry path and field names are TBD.
8. Update the summary schema or fixture so Section 9 results are distinguishable from Section 8 results and usable for release readiness review. Include enough diagnostic evidence for audit without forcing release review to parse raw fixture output. Exact schema path and fields are TBD.
9. Run the relevant local validation command once implementation exists. Current command is TBD; do not claim execution before a command is identified and run.
10. Record any unresolved source mismatch, pending ID, dependency-closure uncertainty, or missing implementation surface in the summary output and release notes/checklist.

#### Verification

| Check | Expected Evidence |
|---|---|
| ID completeness | Every ID listed in PRD Section 12.4 / SPEC Section 19.3 appears in the Section 9 registry or summary. |
| ID status honesty | Every Section 9 ID has explicit status metadata; unimplemented runtime phases are pending, skipped, blocked, or gated rather than pass. |
| Section 8 preservation | Existing Section 8 checks remain present and runnable. |
| Engine contract | Engine conformance test or manifest proves Chirality-owned runtime boundary remains separate from SDK APIs. |
| Event schema and replay | JSONL event test proves append order, unique IDs, redaction, artifact references, malformed-tail tolerance, and terminal outcomes. |
| Settings isolation | Test or runtime metadata proves shipped `settingSources` posture does not load ambient user/local settings. |
| Permission overlay | Denial tests prove deny overrides allow and `allowedTools` alone is not treated as a boundary. |
| MCP and hooks | MCP wrapper and hook tests prove policy, path, redaction, event logging, and fail-closed behavior. |
| Compaction and subagents | Tests prove `context.compacted` and governed child-run lifecycle events are persisted when those SDK callbacks are available. |
| Summary schema | Stable summary artifact includes Section 9 ID status and evidence references. |
| Source warnings and dependency closure | PRD hash warning and dependency-closure uncertainty are visible until human ruling or project-level graph closure resolves them. |

#### Records

- Section 9 validation ID registry or manifest.
- Harness runner update.
- Summary schema/fixture update.
- Validation output or premerge summary artifact.
- Human-ruling log for PRD hash warning and domain-profile validation gating.
- Accepted status enum/schema reference, runner entrypoint, validation command, registry path, and validation output artifact path, all `TBD` until implementation establishes them.

## Component: execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions/Specification.md

### Specification: DEL-09-02 Section 9 Runtime Validation Additions

#### Scope

This deliverable specifies runtime validation additions for Section 9 of the harness validation surface. It covers validation IDs, harness runner updates, and summary schema expectations for runtime boundaries related to the provider-adapter conformance, first-adapter mapper, event log, settings isolation, permissions, MCP tools, hooks, compaction, and subagents.

Excluded from this deliverable:

- Feature implementation outside test fixtures and packaging glue, per package exclusions in `_CONTEXT.md`.
- Creation of dependency register entries or `Dependencies.csv`.
- Domain-profile runtime validation before a governed domain-profile amendment enters scope; the ID may remain listed but should be gated or marked pending.

#### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-09-02-RQ-001 | Section 9 validation additions MUST include the runtime validation IDs enumerated by PRD Section 12.4 and SPEC Section 19.3. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |
| DEL-09-02-RQ-002 | Validation for `section9.runtime_engine_contract` MUST confirm Chirality owns an `AgentEnginePort` / `RuntimeEngineContract` boundary separate from SDK APIs, including accepted turn input, UI events, canonical events, permission decisions, permitted tool exposure, session linkage, interrupt/cancel handling, and terminal outcomes. | `docs/SPEC.md` Sections 10.1-10.4; `docs/CONTRACT.md` K-ENGINE-1, K-ENGINE-2, K-ENGINE-4 |
| DEL-09-02-RQ-003 | Validation for SDK mapping and event-log IDs MUST preserve the distinction between browser `UIEvent`s and persisted `HarnessEvent`s; SDK messages and transcripts are adapter metadata or secondary state unless imported into `HarnessEvent` form. | `docs/SPEC.md` Sections 9 and 10.3; `docs/CONTRACT.md` K-EVENT-1, K-SDK-3 |
| DEL-09-02-RQ-004 | Validation for session replay MUST confirm newline-delimited append order, unique event IDs, no secret storage, artifact references for large payloads, and tolerance for malformed trailing lines. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5, K-EVENT-6, K-EVENT-7 |
| DEL-09-02-RQ-005 | Validation for `section9.settingsources_isolation` MUST confirm shipped runtime does not load ambient user/global Claude Code settings or local `.claude/settings.local.json`; default `settingSources: []` is required where applicable. | `docs/CONTRACT.md` K-SDK-1; `docs/PRD.md` FR-117, NFR-028 |
| DEL-09-02-RQ-006 | Validation for permission overlay MUST confirm explicit hard-deny precedence, that prompt text and `allowedTools` alone are not safety boundaries, and that `disallowedTools`, mode policy, hooks, `canUseTool`, and/or `dontAsk` enforce restrictions. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-4; `docs/SPEC.md` Sections 14.3 and 15.1 |
| DEL-09-02-RQ-007 | Validation for Chirality MCP status/dependency tools MUST use `mcp__chirality__*` naming and confirm MCP tools pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/SPEC.md` Sections 14.1-14.3; `docs/TYPES.md` Section 8.4; `docs/CONTRACT.md` K-MCP-1 |
| DEL-09-02-RQ-008 | Validation for path and instruction-root hooks MUST confirm active project-root containment, instruction-root write denial, initial symlink-write rejection, and fail-closed behavior for write, shell, domain, and subagent actions. | `docs/SPEC.md` Section 15.2; `docs/CONTRACT.md` K-HOOK-1, K-PATH-2, K-PATH-3 |
| DEL-09-02-RQ-009 | Validation for tool result budgets MUST confirm large or sensitive tool results are budgeted, previewed, stored as artifacts, or redacted according to policy. | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` FR-096 |
| DEL-09-02-RQ-010 | Validation for compaction MUST confirm compaction boundaries are persisted when available and replay implications are recorded. | `docs/SPEC.md` Section 15.2; `docs/TYPES.md` Section 8.5; `docs/PRD.md` FR-098, FR-099 |
| DEL-09-02-RQ-011 | Validation for subagent governance MUST confirm subagent delegation fails closed unless governance gates pass, child capabilities do not expand parent permissions, and child run records/artifact references are produced when execution is enabled. | `docs/CONTRACT.md` K-SUBAGENT-1 through K-SUBAGENT-3; `docs/PRD.md` FR-101, FR-102 |
| DEL-09-02-RQ-012 | Harness runner updates MUST preserve existing Section 8 validation coverage while adding Section 9 IDs as runtime phases land. | `docs/PRD.md` Sections 12.3-12.4; `docs/SPEC.md` Sections 19.2-19.3 |
| DEL-09-02-RQ-013 | The summary schema MUST identify Section 9 validation outcomes distinctly enough to support release readiness review. Exact schema fields are TBD. | `_CONTEXT.md`; `docs/PRD.md` Section 12.4; ASSUMPTION based on anticipated artifact "summary schema" |
| DEL-09-02-RQ-014 | Each Section 9 ID MUST carry an explicit status and evidence reference or blocker note; runtime phases that have not landed MUST NOT be reported as passing. Accepted status enum is TBD, but natural-language status terms MUST preserve the distinction between pass, fail, pending, skipped, blocked, and gated. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3; `_SEMANTIC_LENSING.md` A-001/C-001/E-002 worklist |
| DEL-09-02-RQ-015 | The registry or manifest evidence SHOULD include each Section 9 ID, source reference, status metadata, warning/blocker notes, and evidence artifact reference when available. Exact registry/manifest path and field names are TBD. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3; `_CONTEXT.md` Anticipated Artifacts; `_SEMANTIC_LENSING.md` F-001/B-002 worklist |
| DEL-09-02-RQ-016 | Section 9 fixture coverage SHOULD be grouped by runtime surface: engine boundary, SDK mapper/event log/replay, settings isolation, permission overlay, tool/MCP exposure, path/instruction-root hooks, tool-result budget, compaction boundary, and subagent governance. Exact fixture file paths remain TBD. | `docs/CONTRACT.md` Sections 1.4-1.6; `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3; `_SEMANTIC_LENSING.md` X-001 worklist |

#### Standards

| Standard / Contract | Applicability |
|---|---|
| `docs/CONTRACT.md` K-ENGINE, K-SDK, K-EVENT, K-PERM, K-TOOL, K-MCP, K-HOOK, K-PATH, K-SUBAGENT | Governs invariant-level validation targets. |
| `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3 | Governs event schema, runtime engine contract, MCP names, permissions/hooks, and Section 9 validation IDs. |
| `docs/TYPES.md` Sections 7.3, 8.4, 8.5 | Governs type targets and vocabulary for events, MCP names, and hook terms. |
| `docs/PRD.md` Sections 8.12-8.16 and 12.4 | Governs product requirements for runtime boundaries and validation additions. PRD hash mismatch warning applies. |

#### Verification

| Requirement | Verification Approach |
|---|---|
| DEL-09-02-RQ-001 | Static test or manifest assertion that every Section 9 ID from PRD/SPEC is present with status metadata. |
| DEL-09-02-RQ-002 | Engine conformance test against `AgentEnginePort` / `RuntimeEngineContract`, including terminal outcome and interrupt/cancel cases. |
| DEL-09-02-RQ-003 | Mapper tests that assert SDK message names do not leak into browser contract or canonical persisted event contract except as explicit adapter metadata. |
| DEL-09-02-RQ-004 | JSONL replay tests covering ordered events, malformed trailing line tolerance, redaction, and artifact references. |
| DEL-09-02-RQ-005 | SDK options builder test asserting shipped default settings-source posture. |
| DEL-09-02-RQ-006 | Permission tests for denied writes, shell, unknown tools, `allowedTools` misuse, and `dontAsk` denial behavior. |
| DEL-09-02-RQ-007 | MCP wrapper tests for status/dependency tool names, permission policy, hook invocation, and redaction/event logging. |
| DEL-09-02-RQ-008 | Hook tests for project-root containment, instruction-root protection, symlink writes, and fail-closed pre-tool failures. |
| DEL-09-02-RQ-009 | Tool-result tests for inline/preview/artifact/redaction behavior. |
| DEL-09-02-RQ-010 | Compaction callback or event-mapping test for `context.compacted` persistence. |
| DEL-09-02-RQ-011 | Subagent governance tests for fail-closed gating, restricted child tools/cwd, and child-run records. |
| DEL-09-02-RQ-012 | Harness premerge run proving Section 8 validations remain present while Section 9 IDs are added. |
| DEL-09-02-RQ-013 | Summary fixture/schema test; exact schema path and fields TBD. |
| DEL-09-02-RQ-014 | Manifest or summary assertion that no ID lacking an implemented runtime phase is marked pass; accepted enum and schema path TBD. |
| DEL-09-02-RQ-015 | Manifest/fixture review that every Section 9 ID has source reference, status metadata, and evidence/blocker reference; exact file path TBD. |
| DEL-09-02-RQ-016 | Fixture-family or evidence-ID review for each runtime surface; exact fixture names and paths TBD. |

#### Documentation

Required deliverable artifacts:

- Section 9 validation ID registry or equivalent manifest.
- Harness runner changes that execute/report the Section 9 IDs.
- Summary schema or fixture update showing Section 9 results.
- Test fixtures for event log, permissions, MCP, hooks, compaction, and subagent governance where implementation exists.
- Human-facing notes for any IDs marked pending because their runtime phase has not landed.
- Section 8 preservation evidence or premerge summary reference alongside new Section 9 outcomes.
- Warning-qualified PRD source-state note while `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`.
