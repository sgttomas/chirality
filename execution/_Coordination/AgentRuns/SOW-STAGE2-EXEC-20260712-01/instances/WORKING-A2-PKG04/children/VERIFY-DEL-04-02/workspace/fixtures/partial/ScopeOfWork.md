---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-02
package_id: PKG-04
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-016, SOW-045, SOW-047, SOW-052]
package_objective_refs: [OBJ-004, OBJ-005]
---

# Scope of Work — DEL-04-02

## Purpose and Objective Traceability

This migration candidate defines `DEL-04-02` in service of project scope [SOW-016, SOW-045, SOW-047, SOW-052] and package objectives [OBJ-004, OBJ-005].

- **OUT-001** — DEL-04-02 SdkOptionsBuilder and Settings Isolation production output: sdk-options-builder.ts, settings isolation tests, and visible tool metadata, bounded by SOW-016, SOW-045, SOW-047, SOW-052, OBJ-004, and OBJ-005.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-02 SdkOptionsBuilder and Settings Isolation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"aba079add6e079d9fec039fd3f957660e3ff40d8aac0fe4ca8ae887e59b1aec5","target_id":"CLM-001"} -->
#### Datasheet: DEL-04-02 SdkOptionsBuilder and Settings Isolation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":21,"line_start":5,"source_sha256":"aba079add6e079d9fec039fd3f957660e3ff40d8aac0fe4ca8ae887e59b1aec5","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-04-02 |
| DeliverableName | SdkOptionsBuilder and Settings Isolation |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-016, SOW-045, SOW-047, SOW-052 |
| SupportsObjectives | OBJ-004, OBJ-005 |
| AnticipatedArtifacts | `sdk-options-builder.ts`; settings isolation tests; visible tool metadata |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":34,"line_start":22,"source_sha256":"aba079add6e079d9fec039fd3f957660e3ff40d8aac0fe4ca8ae887e59b1aec5","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Deterministic SDK option construction and shipped settings isolation for the SDK-backed runtime path. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02 |
| Runtime option inputs | Session state, persona, mode, model/tool/max-turn options, tool policy, hooks, MCP servers, subagents, resume/session linkage, and settings policy. Exact TypeScript input type is TBD until DEL-04-01 probe evidence and adjacent contracts for persona, session linkage, hooks, MCP, subagents, and settings policy are accepted. | `docs/PRD.md` Section 4 and Section 8.4, MATCH; `docs/SPEC.md` Sections 12-15; `execution/_Decomposition/...` DEL-04-01 through DEL-04-05 — reconciled under D-APP-38 |
| Fallback chains | Model: `opts.model` -> `CHIRALITY_GLOBAL_MODEL` or instruction-root frontmatter -> runtime default. Tools: `opts.tools` -> persona frontmatter/defaults -> runtime default. Max turns: `opts.maxTurns` -> persona frontmatter/defaults -> runtime default. Mode and persona use request/session values before runtime defaults. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` Section 8.4, MATCH — reconciled under D-APP-38 |
| Settings posture | Shipped SDK options use `settingSources: []`. Development-only project settings may use `['project']` only behind explicit environment configuration. `user` and `local` setting sources are not permitted in shipped builds. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1; `docs/PRD.md` Sections 8.12 and 10.3.1, MATCH — reconciled under D-APP-38 |
| Tool mapping posture | `opts.tools` maps only to registered SDK built-ins or Chirality MCP tools. Unknown names produce structured validation errors. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, MATCH — reconciled under D-APP-38 |
| Permission boundary posture | `allowedTools` is not a restriction boundary by itself; restrictions depend on deny rules, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | `docs/CONTRACT.md` K-PERM-3; `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, MATCH — reconciled under D-APP-38 |
| Max-turn guard | Resolved `maxTurns` is passed into SDK options so runaway loops stop and terminal max-turn errors can be persisted. Exact error mapping is owned by adjacent runtime/event deliverables. | `docs/PRD.md` Section 8.13, MATCH; `execution/_Decomposition/...` SOW-052 — reconciled under D-APP-38 |
| Visible metadata | Safe adapter metadata should include SDK package version, permission mode, visible tool list, MCP server names, settings-source posture, SDK session ID/resume mode, and transcript/store linkage where available. SDK package version is adapter/runtime evidence, not a public Chirality product-version authority. | `docs/SPEC.md` Section 12.4; `docs/CONTRACT.md` K-ENGINE-4; `docs/TYPES.md` Section 9; `docs/PRD.md` Section 10.3.1, MATCH — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":44,"line_start":35,"source_sha256":"aba079add6e079d9fec039fd3f957660e3ff40d8aac0fe4ca8ae887e59b1aec5","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| SDK role | The Claude Agent SDK is the preferred runtime spine only when verified and kept behind Chirality-owned contracts. | `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-5 |
| Product identity | SDK-specific defaults, transcript shape, tool names, and Claude Code assumptions must not define public Chirality semantics. | `docs/CONTRACT.md` K-ENGINE-3, K-ENGINE-4, K-SDK-4; `docs/PLAN.md` Section 2 |
| Tool expansion sequence | Read tools are enabled before write/edit/bash capability. Write, bash, and subagent execution deepen in PKG-06 and later packages. | `docs/PLAN.md` R2; `docs/PRD.md` Section 8.13, MATCH — reconciled under D-APP-38 |
| Dependency state | Declared upstream and downstream dependencies are TBD; dependency extraction is deferred until after four-document authoring and semantic passes. | `_DEPENDENCIES.md` |
| Source-state warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":54,"line_start":45,"source_sha256":"aba079add6e079d9fec039fd3f957660e3ff40d8aac0fe4ca8ae887e59b1aec5","target_id":"CLM-005"} -->
##### Construction

| Construct | Expected Content |
|---|---|
| `sdk-options-builder.ts` | Deterministic builder for SDK request options, settings-source posture, resolved model/tools/maxTurns/mode/persona, hooks, MCP server registration metadata, subagent descriptors where enabled, resume/session linkage, and safe visible metadata. Candidate R1 path is `frontend/src/lib/harness/sdk-options-builder.ts` per PRD source-state warning; accepted module path and exact exported API remain TBD pending implementation convention. |
| Settings isolation tests | Tests asserting shipped `settingSources: []`, development project-settings opt-in only through explicit environment configuration, and no `user`/`local` setting sources in shipped builds. |
| Tool mapping tests | Tests asserting deterministic tool ordering, registered-name mapping, unknown-tool structured validation errors, and no reliance on `allowedTools` alone as a restriction boundary. |
| Max-turn tests | Tests asserting resolved max-turn value reaches SDK options and terminal max-turn outcome is available to the runtime/event layer. Exact terminal event fixture: TBD in coordination with runtime event deliverables. |
| Visible tool metadata | Safe runtime metadata containing visible tool names, MCP server names, permission posture, settings-source posture, and SDK version fields where known. |

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":66,"line_start":55,"source_sha256":"aba079add6e079d9fec039fd3f957660e3ff40d8aac0fe4ca8ae887e59b1aec5","target_id":"CLM-006"} -->
##### References

| RefID | SourcePath | SectionRef | Use |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 0, 2.8 | Authority order and SDK-governed posture |
| REF-002 | `docs/CONTRACT.md` | Sections 1.4, 1.6 | SDK governance, settings isolation, permission/tool invariants |
| REF-003 | `docs/SPEC.md` | Sections 12-15 | Runtime configuration, fallback chains, tool surface, modes/hooks |
| REF-004 | `docs/TYPES.md` | Sections 7.2, 8.2, 8.3, 9 | Vocabulary for SdkOptionsBuilder, settings, permission, tools, session linkage |
| REF-005 | `docs/PLAN.md` | Sections 2-4, 6-8 | Roadmap sequencing, tests, known SDK risks |
| REF-006 | `docs/PRD.md` | Sections 8.4, 8.12, 8.13, 10.3.1, KG-021 through KG-032 | Product requirements; source hash status: MATCH noted — reconciled under D-APP-38 |
| REF-DEC | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-04-02; SOW-016, SOW-045, SOW-047, SOW-052 | Deliverable scope and traceability |

<!-- sow-source-end -->

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":69,"line_start":67,"source_sha256":"aba079add6e079d9fec039fd3f957660e3ff40d8aac0fe4ca8ae887e59b1aec5","target_id":"CLM-007"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-119/120/121 record the realized split: `TurnEngine.assertKnownAgentSdkTools` owns runtime validation, the options builder owns deterministic mapping, concrete compiling SDK property names are probe-backed, and the module/test paths are landed.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-04-02 SdkOptionsBuilder and Settings Isolation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"c48621523ecf94484922a1d75b730f4ca8506ba2a466dc96f6418a0e70af0093","target_id":"CLM-008"} -->
#### Specification: DEL-04-02 SdkOptionsBuilder and Settings Isolation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":25,"line_start":5,"source_sha256":"c48621523ecf94484922a1d75b730f4ca8506ba2a466dc96f6418a0e70af0093","target_id":"CLM-009"} -->
##### Scope

This deliverable specifies the `SdkOptionsBuilder` backend feature slice for constructing deterministic Claude Agent SDK options from Chirality-owned runtime state and policy. It covers:

- runtime option fallback resolution for model, tools, max turns, mode, and persona;
- shipped SDK settings isolation;
- registered SDK built-in and Chirality MCP tool option mapping;
- safe visible metadata for tool/settings posture;
- max-turn option propagation;
- tests for settings isolation and options/tool mapping.

Exclusions:

- `PersonaComposer` content assembly is owned by DEL-04-04, though this builder consumes its output.
- SDK message to `UIEvent`/`HarnessEvent` mapping is owned by DEL-04-03.
- provider key/base URL handoff is owned by DEL-04-05.
- full permission overlay, hooks, write/bash enablement, and subagent execution gates deepen in PKG-06 and PKG-08; this deliverable must accept policy inputs without weakening those later boundaries.
- Chirality event-store internals beyond safe metadata handoff are outside PKG-04 scope.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02; `docs/SPEC.md` Sections 12-15.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":44,"line_start":26,"source_sha256":"c48621523ecf94484922a1d75b730f4ca8506ba2a466dc96f6418a0e70af0093","target_id":"CLM-010"} -->
##### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-04-02-REQ-001 | The builder MUST resolve runtime option fallback chains deterministically for model, tools, max turns, mode, and persona. | SOW-016; `docs/SPEC.md` Section 13.1; `docs/PRD.md` Section 8.4, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-002 | Unknown option keys MUST be ignored with warnings rather than silently mutating behavior. | SOW-016; `docs/SPEC.md` Section 13.1; `docs/PRD.md` Section 8.4, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-003 | Shipped SDK options MUST use `settingSources: []`. | SOW-045; `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| DEL-04-02-REQ-004 | Development-only project settings MAY use `['project']` only behind explicit environment configuration; `user` and `local` sources MUST NOT be used in shipped builds. | `docs/SPEC.md` Section 12.2; `docs/PRD.md` Section 8.12, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-005 | `opts.tools` MUST map only to registered SDK built-ins or Chirality MCP tools; unknown names MUST produce structured validation errors. | SOW-047; `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-006 | Tool ordering, naming, MCP server IDs, and allow/deny option lists MUST be stable for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | `docs/CONTRACT.md` K-TOOL-1; `docs/PRD.md` Section 8.13, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-007 | The builder MUST NOT treat `allowedTools` alone as a restriction boundary. Restriction posture MUST include deny rules, mode policy, hooks, `canUseTool`, and/or `dontAsk` where applicable. | `docs/CONTRACT.md` K-PERM-3; `docs/SPEC.md` Section 14.3 |
| DEL-04-02-REQ-008 | Resolved `maxTurns` MUST be included in SDK options so max-turn guards can stop runaway loops and terminal max-turn errors can be persisted by runtime/event layers. | SOW-052; `docs/PRD.md` Section 8.13, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-009 | The builder MUST preserve Chirality-owned semantics by keeping SDK-specific names and option details at adapter boundaries and safe metadata surfaces, not public API contracts. | `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-4; `docs/TYPES.md` Section 9 |
| DEL-04-02-REQ-010 | Safe visible metadata SHOULD include SDK package version, SDK permission mode, visible tool list, MCP server names, settings-source posture, SDK session ID/resume mode, and transcript/store linkage where available. | `docs/SPEC.md` Section 12.4 |
| DEL-04-02-REQ-011 | API keys and secrets MUST NOT be written to project files or included in visible metadata produced by this builder. | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` Section 10.3.1, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-012 | Exact SDK option property names beyond cited source text are TBD until the first-adapter probe/version decision confirms current TypeScript APIs. | `docs/PLAN.md` R0; `docs/PRD.md` KG-021, MATCH — reconciled under D-APP-38 |
| DEL-04-02-REQ-013 | The builder input contract MUST either define or explicitly import the owning adjacent contract for session state, persona output, hook policy, MCP server descriptors, subagent descriptors, resume linkage, and settings policy before the exact TypeScript shape is treated as closed. | `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Section 4, MATCH; `execution/_Decomposition/...` DEL-04-01 through DEL-04-05 — reconciled under D-APP-38 |
| DEL-04-02-REQ-014 | Before constructing SDK options, the builder MUST fail closed or return a structured integration error when required governed policy inputs for settings, tools, permission posture, hooks, MCP, or subagents are absent or explicitly unresolved. | `docs/CONTRACT.md` K-RELIANCE-2, K-PERM-1 through K-PERM-3, K-MCP-1, K-HOOK-1; `docs/PLAN.md` R2 |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":54,"line_start":45,"source_sha256":"c48621523ecf94484922a1d75b730f4ca8506ba2a466dc96f6418a0e70af0093","target_id":"CLM-011"} -->
##### Standards

| Standard or Contract | Application | Source |
|---|---|---|
| Chirality `AgentEnginePort` / `RuntimeEngineContract` | SDK options are constructed behind a product-owned engine boundary. | `docs/CONTRACT.md` K-ENGINE-1; `docs/SPEC.md` Section 11; `docs/PRD.md` Section 8.12, MATCH — reconciled under D-APP-38 |
| SDK settings isolation | Shipped runtime must not load ambient user/global Claude Code settings or local `.claude/settings.local.json`. | `docs/CONTRACT.md` K-SDK-1; `docs/SPEC.md` Section 12.2 |
| Capability-forward policy with explicit hard-deny precedence permission policy | Builder must carry policy posture without confusing auto-approval with restriction. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-6 |
| Chirality MCP naming | Chirality tools use `mcp__chirality__*` names. | `docs/SPEC.md` Section 14.2; `docs/TYPES.md` Section 8.4 |
| Epistemic controls | Unknown implementation details remain `TBD` rather than invented. | `docs/CONTRACT.md` K-INVENT-1; `docs/DIRECTIVE.md` Section 2.5 |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":67,"line_start":55,"source_sha256":"c48621523ecf94484922a1d75b730f4ca8506ba2a466dc96f6418a0e70af0093","target_id":"CLM-012"} -->
##### Verification

| Verification ID | Requirement Links | Verification Approach | Expected Evidence |
|---|---|---|---|
| DEL-04-02-VER-001 | REQ-001, REQ-002 | Unit tests for model/tool/maxTurns/mode/persona fallback order and unknown-key warnings. | Options-builder test fixtures assert warning emission and identical resolved SDK behavior when unknown option keys are added to otherwise identical inputs. |
| DEL-04-02-VER-002 | REQ-003, REQ-004 | Settings isolation tests for shipped default, explicit development project opt-in, and forbidden setting-source cases. | Fixtures cover shipped `settingSources: []`, development-only `['project']` behind explicit environment configuration, and rejection/exclusion of `user` and `local` sources in shipped posture. |
| DEL-04-02-VER-003 | REQ-005, REQ-006, REQ-007, REQ-014 | Composite tool/policy mapping tests for registered built-ins, registered Chirality MCP names, deterministic ordering, unknown-name errors, MCP server IDs, allow/deny lists, and permission policy inputs. | One deterministic-order fixture includes requested tools, visible tools, MCP server IDs, `allowedTools`, `disallowedTools`, permission mode, hook/callback posture, and structured validation errors. |
| DEL-04-02-VER-004 | REQ-007, REQ-014 | Tests or static checks proving `allowedTools` is not the sole restriction mechanism for restricted modes. | Fixture showing deny/disallowed/hook/callback posture included or required before option construction proceeds. |
| DEL-04-02-VER-005 | REQ-008 | Max-turn option propagation test and terminal max-turn handoff fixture. | SDK options fixture plus runtime event handoff fixture location TBD; likely adjacent owner is DEL-04-03 or DEL-03-02 pending accepted integration contract. |
| DEL-04-02-VER-006 | REQ-009, REQ-010, REQ-011 | Metadata-shape and redaction review confirming SDK details are adapter metadata and safe runtime metadata only. | Single metadata fixture proves safe fields are present and API keys, raw secrets, hidden user settings content, and public product-version claims are absent. |
| DEL-04-02-VER-007 | REQ-011 | Redaction/secret exclusion test for builder output and visible metadata. | Fixture with API-key-like input verifies no secret output in project files, visible metadata, or runtime records owned by this slice. |
| DEL-04-02-VER-008 | REQ-012, REQ-013 | first-adapter probe/typecheck after package pin and adjacent-contract import review. | Probe notes, TypeScript compile evidence from DEL-04-01 or R1 implementation, and source-backed references for any imported persona/session/hook/MCP/settings policy types. |

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":84,"line_start":68,"source_sha256":"c48621523ecf94484922a1d75b730f4ca8506ba2a466dc96f6418a0e70af0093","target_id":"CLM-013"} -->
##### Documentation

Required artifacts:

- `sdk-options-builder.ts` or equivalent module path selected by implementation owner.
- Unit tests for fallback chains, unknown keys, settings isolation, tool mapping, deterministic ordering, max-turn propagation, and visible metadata.
- Safe visible tool/settings metadata fixture.
- Notes in implementation comments or local docs for any SDK option whose exact TypeScript shape depends on the accepted first-adapter probe.

Open documentation items:

- TBD: exact module path and exported TypeScript API.
- TBD: target test command or validation suite for this module after implementation path is selected.
- TBD: exact structured error type for unknown tools.
- TBD: exact integration point with `PersonaComposer`, `TurnEngine`, and PKG-06 permission overlay.
- TBD: exact SDK package version and option names confirmed by DEL-04-01 probe.

<!-- sow-source-end -->

### CLM-014 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":87,"line_start":85,"source_sha256":"c48621523ecf94484922a1d75b730f4ca8506ba2a466dc96f6418a0e70af0093","target_id":"CLM-014"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-119/120/121 record the realized split: `TurnEngine.assertKnownAgentSdkTools` owns runtime validation, the options builder owns deterministic mapping, concrete compiling SDK property names are probe-backed, and the module/test paths are landed.
<!-- sow-source-end -->

- **AC-001** — The DEL-04-02 output satisfies the legacy production-contract requirements and checks for deterministic runtime option fallback, provider/SDK settings isolation, registered tool option mapping, and max-turn guards for SOW-016, SOW-045, SOW-047, and SOW-052.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-04-02 SdkOptionsBuilder and Settings Isolation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"2e329e6f0c59cfb2d48101718eadc6b66a55cb19f3c85f17c01084045c23926e","target_id":"CLM-015"} -->
#### Procedure: DEL-04-02 SdkOptionsBuilder and Settings Isolation

<!-- sow-source-end -->

### CLM-016 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"2e329e6f0c59cfb2d48101718eadc6b66a55cb19f3c85f17c01084045c23926e","target_id":"CLM-016"} -->
##### Purpose

Define the operational steps to produce and verify the `SdkOptionsBuilder` feature slice without exceeding the deliverable boundary. The procedure supports creation of `sdk-options-builder.ts`, settings isolation tests, and visible tool metadata.

<!-- sow-source-end -->

### CLM-017 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":18,"line_start":7,"source_sha256":"2e329e6f0c59cfb2d48101718eadc6b66a55cb19f3c85f17c01084045c23926e","target_id":"CLM-017"} -->
##### Prerequisites

| Prerequisite | Status | Source |
|---|---|---|
| Accepted deliverable scope for DEL-04-02 | Available in decomposition and `_CONTEXT.md` | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02 |
| first-adapter probe/version decision | TBD; required before final exact SDK TypeScript option fields are frozen | `docs/PLAN.md` R0; `docs/PRD.md` KG-021, HASH_MISMATCH |
| Runtime engine contract integration point | TBD; adjacent deliverables define `AgentEnginePort`, `TurnEngine`, and conformance suite | `docs/CONTRACT.md` K-ENGINE-1; `docs/PRD.md` Section 8.12, HASH_MISMATCH |
| Persona composer output contract | TBD; DEL-04-04 owns prompt composition | `_CONTEXT.md`; `execution/_Decomposition/...` DEL-04-04 |
| Permission overlay policy inputs | TBD; PKG-06 owns full overlay and hooks, but this builder must accept policy posture | `_CONTEXT.md` ContextEnvelopeNotes; `docs/PLAN.md` R2 |
| Implementation module path | TBD; candidate R1 path is `frontend/src/lib/harness/sdk-options-builder.ts` but accepted path/export shape must follow implementation convention | `docs/PLAN.md` R1; `docs/PRD.md` Section 13.3, HASH_MISMATCH |
| Dependency edges | TBD; no declared upstream/downstream dependencies have been extracted yet | `_DEPENDENCIES.md` |

<!-- sow-source-end -->

### CLM-018 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":79,"line_start":19,"source_sha256":"2e329e6f0c59cfb2d48101718eadc6b66a55cb19f3c85f17c01084045c23926e","target_id":"CLM-018"} -->
##### Steps

1. Confirm source and package scope.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the DEL-04-02 decomposition row.
   - Confirm SOW coverage: SOW-016, SOW-045, SOW-047, SOW-052.
   - Record the `docs/PRD.md` `HASH_MISMATCH` warning if using PRD-backed details.

2. Define the builder input shape.
   - Include session/runtime state needed for model, tools, max turns, mode, persona, hooks, MCP servers, subagents, resume/session linkage, and settings policy.
   - Reference or import adjacent owner contracts for persona output, session linkage, hooks, MCP server descriptors, subagent descriptors, permission policy, and settings policy when those contracts exist.
   - Mark exact TypeScript API names as TBD until first-adapter probe/version evidence is accepted.

3. Implement deterministic fallback resolution.
   - Resolve model, tools, and max turns using `docs/SPEC.md` Section 13.1.
   - Resolve mode and persona from request/session values before runtime defaults.
   - Emit warnings for unknown option keys and ensure unknown keys do not mutate behavior.

4. Implement settings isolation posture.
   - For shipped posture, set SDK settings source behavior to `settingSources: []`.
   - Permit `['project']` only under explicit development configuration.
   - Reject invalid shipped policy inputs before option construction or omit ambient settings by construction; do not pass `user` or `local` settings sources in shipped builds.
   - Add safe visible metadata for selected settings-source posture.

5. Implement tool-surface resolution.
   - Resolve requested tools against registered SDK built-ins and registered Chirality MCP tool names.
   - Preserve deterministic ordering.
   - Return structured validation errors for unknown names before SDK request construction.
   - Include visible tool metadata that is safe for runtime display/logging.

6. Carry permission, hook, MCP, and subagent policy posture.
   - Include `disallowedTools`, permission mode, hooks, `canUseTool`, MCP server descriptors, and subagent descriptors only as supplied by governed policy inputs.
   - Do not treat `allowedTools` alone as sufficient restriction.
   - Fail closed or return TBD/integration errors for subagent descriptors until governance bridge requirements are available.

7. Include max-turn guard option.
   - Pass resolved `maxTurns` into SDK options.
   - Ensure runtime/event layers can observe terminal max-turn errors; exact event mapping is TBD in adjacent deliverables.

8. Produce safe metadata.
   - Include SDK package version where known, permission mode, visible tool list, MCP server names, settings-source posture, SDK session ID/resume mode, and transcript/store linkage where available.
   - Exclude API keys, raw secrets, hidden user settings content, and project-truth claims.

9. Add tests.
   - Add fallback-chain tests.
   - Add unknown-option warning tests that prove resolved SDK behavior is unchanged when unknown keys are present.
   - Add shipped settings isolation tests.
   - Add development-only project-setting opt-in tests.
   - Add forbidden `user` and `local` settings-source tests for shipped posture.
   - Add tool mapping, ordering, and unknown-tool tests.
   - Add one composite deterministic-order fixture covering requested tools, visible tools, MCP server IDs, allow/deny lists, permission mode, hook/callback posture, and permission policy inputs together.
   - Add `allowedTools` misconception guard test.
   - Add max-turn propagation test.
   - Add safe metadata redaction/exclusion test proving safe fields are present and API keys/secrets are absent.

10. Run validation.
    - Run targeted unit tests for `sdk-options-builder.ts` or the selected equivalent module.
    - Run typecheck after SDK version/API is pinned.
    - Run broader harness validation when the feature is wired into `TurnEngine`.
    - Record the exact test command or validation suite once the implementation path exists; until then, keep the command as TBD.
    - Record any remaining TBD fields, terminal max-turn fixture owner, or SDK-probe dependencies.

<!-- sow-source-end -->

### CLM-019 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":94,"line_start":80,"source_sha256":"2e329e6f0c59cfb2d48101718eadc6b66a55cb19f3c85f17c01084045c23926e","target_id":"CLM-019"} -->
##### Verification

| Check | Expected Result |
|---|---|
| Fallback determinism | Same inputs produce same resolved options, warnings, tool ordering, and metadata. |
| Unknown option handling | Unknown option keys warn and do not affect behavior. |
| Shipped settings isolation | Shipped posture produces `settingSources: []` and no `user`/`local` setting sources. |
| Development settings gate | `['project']` requires explicit development configuration. |
| Tool mapping | Registered SDK built-ins and Chirality MCP tools resolve; unknown names produce structured validation errors. |
| Composite deterministic ordering | Tools, MCP server IDs, allow/deny lists, hook/callback posture, permission mode, and policy inputs remain stable for identical inputs. |
| Permission posture | Restricted modes do not rely on `allowedTools` alone. |
| Max-turn guard | Resolved max-turn value reaches SDK options. |
| Metadata safety | Visible metadata contains only safe runtime details and no secrets. |
| Adapter boundary | SDK-specific details do not become public Chirality API or canonical event semantics except as adapter metadata. |

<!-- sow-source-end -->

### CLM-020 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":109,"line_start":95,"source_sha256":"2e329e6f0c59cfb2d48101718eadc6b66a55cb19f3c85f17c01084045c23926e","target_id":"CLM-020"} -->
##### Records

Expected implementation records:

- `sdk-options-builder.ts` or equivalent module selected by implementation owner.
- Exact module path/export shape record, currently TBD pending implementation convention.
- Settings isolation tests.
- Tool mapping and visible metadata tests.
- Max-turn propagation tests.
- Unknown option warning tests.
- Targeted test command or validation suite, currently TBD until implementation path exists.
- first-adapter probe/version evidence from DEL-04-01 before exact SDK option fields are treated as final.
- Terminal max-turn runtime/event handoff fixture owner, currently TBD and likely adjacent to DEL-04-03 or DEL-03-02 pending accepted contract.
- Any unresolved `TBD`, `ASSUMPTION`, or conflict entries carried forward for human or upstream-agent ruling.

<!-- sow-source-end -->

### CLM-021 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":112,"line_start":110,"source_sha256":"2e329e6f0c59cfb2d48101718eadc6b66a55cb19f3c85f17c01084045c23926e","target_id":"CLM-021"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-119/120/121 record the realized split: `TurnEngine.assertKnownAgentSdkTools` owns runtime validation, the options builder owns deterministic mapping, concrete compiling SDK property names are probe-backed, and the module/test paths are landed.
<!-- sow-source-end -->

- **VER-001** — Verify with the legacy-defined options-builder tests and records covering fallback and unknown-option behavior, shipped and development settings isolation, registered tool mapping and ordering, max-turn propagation, and safe visible metadata.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-04-02 SdkOptionsBuilder and Settings Isolation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-022"} -->
#### Guidance: DEL-04-02 SdkOptionsBuilder and Settings Isolation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-023 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":10,"line_start":5,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-023"} -->
##### Purpose

`SdkOptionsBuilder` exists to keep SDK request construction deterministic, explicit, and governed while Chirality adopts the Claude Agent SDK as a replaceable implementation substrate. It should translate Chirality-owned session state, resolved runtime options, prompt/tool policy, settings posture, and resume metadata into SDK-facing options without allowing SDK defaults or ambient settings to redefine product behavior.

Sources: `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` Section 1.4; `docs/SPEC.md` Sections 12-15; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02.

<!-- sow-source-end -->

### CLM-024 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":30,"line_start":11,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-024"} -->
##### Principles

1. Determinism before convenience.
   For the same session, persona, mode, option set, SDK version, MCP server set, and policy input, the builder should produce stable option values, stable tool ordering, and stable visible metadata. Sources: `docs/CONTRACT.md` K-TOOL-1; `docs/PRD.md` Section 8.13, MATCH. (reconciled under D-APP-38).

2. Settings isolation is a release boundary.
   Shipped builds use `settingSources: []`. Development-only project settings require explicit environment enablement and must not include `user` or `local` sources. Sources: `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1.

3. Policy adequacy is checked before option construction.
   The builder should not normalize missing governed policy into permissive SDK defaults. If required settings, tool, permission, hook, MCP, or subagent policy inputs are absent, explicitly unresolved, or contradictory, the builder should fail closed or return a structured integration error before constructing SDK options. Sources: `docs/CONTRACT.md` K-RELIANCE-2, K-PERM-1 through K-PERM-3, K-MCP-1, K-HOOK-1; `docs/PLAN.md` R2.

4. `allowedTools` is not a safety boundary.
   Treat `allowedTools` as SDK auto-approval posture, not as the complete restriction mechanism. Restricted modes require deny rules, disallowed tools, hooks, `canUseTool`, `dontAsk`, or the PKG-06 overlay as applicable. Sources: `docs/CONTRACT.md` K-PERM-3; `docs/SPEC.md` Section 14.3.

5. Adapter metadata is allowed; public semantic leakage is not.
   SDK-specific names and SDK package version may appear in adapter-local metadata and safe runtime metadata, but they are evidence about the runtime adapter, not public Chirality product-version authority. Public Chirality APIs, canonical events, and governance records remain Chirality-owned. Sources: `docs/CONTRACT.md` K-ENGINE-4; `docs/TYPES.md` Section 9.

6. Prefer explicit unknowns over plausible SDK detail.
REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-025 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":42,"line_start":31,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-025"} -->
##### Considerations

| Topic | Guidance | Source |
|---|---|---|
| Fallback implementation | Keep fallback resolution pure and testable. Emit warnings for unknown option keys; do not let unknown fields affect behavior. | `docs/SPEC.md` Section 13.1 |
| Settings posture | Make shipped/development posture an explicit input or environment-derived policy, then record the selected posture in safe metadata. Shipped option construction should omit ambient settings by using `settingSources: []`; development project settings should be admitted only by the explicit development policy path. | `docs/SPEC.md` Sections 12.2, 12.4 |
| Tool registry | Resolve requested tool names against a deterministic registry of SDK built-ins and Chirality MCP tools. Unknown names should fail before SDK request construction. | `docs/SPEC.md` Section 14.3 |
| Hooks and permissions | Accept hook/callback/deny policy inputs, but do not overclaim that this slice fully implements PKG-06 permission semantics. | `_CONTEXT.md` ContextEnvelopeNotes; `docs/PLAN.md` R2 |
| Resume and session linkage | Include resume/session fields only through the engine/session contract and safe adapter metadata. SDK transcripts remain secondary to Chirality events. | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` Section 12.4 |
| Subagents | Treat subagent option construction as policy-gated and fail-closed until the governance bridge supplies restricted child definitions. | `docs/CONTRACT.md` K-SUBAGENT-1, K-SUBAGENT-2; `docs/PRD.md` KG-027, MATCH — reconciled under D-APP-38 |
| PRD hash state | Use `docs/PRD.md` requirements with caution because `_REFERENCES.md` reports `MATCH`; do not use PRD-only details to override matching higher-authority sources. | `_REFERENCES.md`; `docs/DIRECTIVE.md` Section 0 — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-026 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":51,"line_start":43,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-026"} -->
##### Trade-offs

| Trade-off | Preferred Direction | Rationale |
|---|---|---|
| SDK defaults vs explicit options | Prefer explicit Chirality options and recorded posture. | Prevents ambient settings and SDK defaults from becoming product semantics. |
| Early tool exposure vs controlled sequence | Prefer read-only and registered tools first; defer write/bash/subagent execution until overlays and hooks are active. | Matches roadmap sequence and avoids permission boundary overclaiming. |
| Rich SDK metadata vs provider-neutral core | Keep SDK metadata local to adapter/runtime metadata, with public APIs and canonical events in Chirality terms. | Preserves engine replaceability and conformance testing. |
| Immediate exact SDK field design vs probe-backed API | Use `TBD` for exact fields until SDK version/probe confirms current TypeScript APIs. | Avoids encoding stale or guessed upstream SDK behavior. |

<!-- sow-source-end -->

### CLM-027 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":53,"line_start":52,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-027"} -->
##### Examples

<!-- sow-source-end -->

### CLM-028 — Example Fallback Trace

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":70,"line_start":54,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-028"} -->
###### Example Fallback Trace

```text
Input:
  opts.model = TBD
  environment CHIRALITY_GLOBAL_MODEL = set
  instruction-root model default = available
  runtime default = available

Expected resolution:
  model = CHIRALITY_GLOBAL_MODEL
  warning list = none unless unknown option keys are present

Source:
  docs/SPEC.md Section 13.1
```

<!-- sow-source-end -->

### CLM-029 — Example Settings Posture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":86,"line_start":71,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-029"} -->
###### Example Settings Posture

```text
Shipped build:
  settingSources = []
  visible metadata includes settings-source posture = "shipped-empty"

Development-only explicit project settings:
  settingSources = ['project']
  visible metadata includes settings-source posture = "development-project"
  user/local setting sources remain forbidden

Source:
  docs/SPEC.md Section 12.2
```

<!-- sow-source-end -->

### CLM-030 — Example Tool Resolution

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":103,"line_start":87,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-030"} -->
###### Example Tool Resolution

```text
Requested tools:
  Read
  mcp__chirality__status_read
  unknown_tool

Expected result:
  Read maps to registered SDK built-in if available.
  mcp__chirality__status_read maps to registered Chirality MCP tool.
  unknown_tool returns structured validation error before SDK request construction.

Source:
  docs/SPEC.md Sections 14.1-14.3
```

<!-- sow-source-end -->

### CLM-031 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":108,"line_start":104,"source_sha256":"3ee08bbc5c405fb2cccb26f8d6ea6898c2f95f190aa52d61e70f518246d54411","target_id":"CLM-031"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONFLICT-DEL-04-02-001 | `docs/PRD.md` is locally accessible and highly relevant, but `_REFERENCES.md` reports `MATCH` against the expected SHA. | `_REFERENCES.md` Authoritative Source Corpus | `docs/PRD.md` Sections 8.4, 8.12, 8.13, 10.3.1 | All PRD-cited requirements and guidance | Treat PRD content as source-state warning: use when consistent with higher-authority matching sources, mark PRD-only exact details as TBD or assumption until source state is accepted. | TBD — reconciled under D-APP-38 |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-016 SOW-045 SOW-047 SOW-052 OBJ-004 OBJ-005 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
