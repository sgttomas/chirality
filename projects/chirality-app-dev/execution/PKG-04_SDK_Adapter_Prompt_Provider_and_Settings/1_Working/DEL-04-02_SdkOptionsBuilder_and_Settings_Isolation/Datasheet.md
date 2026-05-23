# Datasheet: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Identification

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

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Deterministic SDK option construction and shipped settings isolation for the SDK-backed runtime path. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02 |
| Runtime option inputs | Session state, persona, mode, model/tool/max-turn options, tool policy, hooks, MCP servers, subagents, resume/session linkage, and settings policy. Exact TypeScript input type is TBD until DEL-04-01 probe evidence and adjacent contracts for persona, session linkage, hooks, MCP, subagents, and settings policy are accepted. | `docs/PRD.md` Section 4 and Section 8.4, HASH_MISMATCH; `docs/SPEC.md` Sections 12-15; `execution/_Decomposition/...` DEL-04-01 through DEL-04-05 |
| Fallback chains | Model: `opts.model` -> `CHIRALITY_GLOBAL_MODEL` or instruction-root frontmatter -> runtime default. Tools: `opts.tools` -> persona frontmatter/defaults -> runtime default. Max turns: `opts.maxTurns` -> persona frontmatter/defaults -> runtime default. Mode and persona use request/session values before runtime defaults. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` Section 8.4, HASH_MISMATCH |
| Settings posture | Shipped SDK options use `settingSources: []`. Development-only project settings may use `['project']` only behind explicit environment configuration. `user` and `local` setting sources are not permitted in shipped builds. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1; `docs/PRD.md` Sections 8.12 and 10.3.1, HASH_MISMATCH |
| Tool mapping posture | `opts.tools` maps only to registered SDK built-ins or Chirality MCP tools. Unknown names produce structured validation errors. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, HASH_MISMATCH |
| Permission boundary posture | `allowedTools` is not a restriction boundary by itself; restrictions depend on deny rules, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | `docs/CONTRACT.md` K-PERM-3; `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, HASH_MISMATCH |
| Max-turn guard | Resolved `maxTurns` is passed into SDK options so runaway loops stop and terminal max-turn errors can be persisted. Exact error mapping is owned by adjacent runtime/event deliverables. | `docs/PRD.md` Section 8.13, HASH_MISMATCH; `execution/_Decomposition/...` SOW-052 |
| Visible metadata | Safe adapter metadata should include SDK package version, permission mode, visible tool list, MCP server names, settings-source posture, SDK session ID/resume mode, and transcript/store linkage where available. SDK package version is adapter/runtime evidence, not a public Chirality product-version authority. | `docs/SPEC.md` Section 12.4; `docs/CONTRACT.md` K-ENGINE-4; `docs/TYPES.md` Section 9; `docs/PRD.md` Section 10.3.1, HASH_MISMATCH |

## Conditions

| Condition | Value | Source |
|---|---|---|
| SDK role | The Claude Agent SDK is the preferred runtime spine only when verified and kept behind Chirality-owned contracts. | `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-5 |
| Product identity | SDK-specific defaults, transcript shape, tool names, and Claude Code assumptions must not define public Chirality semantics. | `docs/CONTRACT.md` K-ENGINE-3, K-ENGINE-4, K-SDK-4; `docs/PLAN.md` Section 2 |
| Tool expansion sequence | Read tools are enabled before write/edit/bash capability. Write, bash, and subagent execution deepen in PKG-06 and later packages. | `docs/PLAN.md` R2; `docs/PRD.md` Section 8.13, HASH_MISMATCH |
| Dependency state | Declared upstream and downstream dependencies are TBD; dependency extraction is deferred until after four-document authoring and semantic passes. | `_DEPENDENCIES.md` |
| Source-state warning | `docs/PRD.md` is accessible but has `HASH_MISMATCH` in `_REFERENCES.md`; PRD-backed statements are used as current local source content with warning, not as unqualified accepted source state. | `_REFERENCES.md` |

## Construction

| Construct | Expected Content |
|---|---|
| `sdk-options-builder.ts` | Deterministic builder for SDK request options, settings-source posture, resolved model/tools/maxTurns/mode/persona, hooks, MCP server registration metadata, subagent descriptors where enabled, resume/session linkage, and safe visible metadata. Candidate R1 path is `frontend/src/lib/harness/sdk-options-builder.ts` per PRD source-state warning; accepted module path and exact exported API remain TBD pending implementation convention. |
| Settings isolation tests | Tests asserting shipped `settingSources: []`, development project-settings opt-in only through explicit environment configuration, and no `user`/`local` setting sources in shipped builds. |
| Tool mapping tests | Tests asserting deterministic tool ordering, registered-name mapping, unknown-tool structured validation errors, and no reliance on `allowedTools` alone as a restriction boundary. |
| Max-turn tests | Tests asserting resolved max-turn value reaches SDK options and terminal max-turn outcome is available to the runtime/event layer. Exact terminal event fixture: TBD in coordination with runtime event deliverables. |
| Visible tool metadata | Safe runtime metadata containing visible tool names, MCP server names, permission posture, settings-source posture, and SDK version fields where known. |

## References

| RefID | SourcePath | SectionRef | Use |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 0, 2.8 | Authority order and SDK-governed posture |
| REF-002 | `docs/CONTRACT.md` | Sections 1.4, 1.6 | SDK governance, settings isolation, permission/tool invariants |
| REF-003 | `docs/SPEC.md` | Sections 12-15 | Runtime configuration, fallback chains, tool surface, modes/hooks |
| REF-004 | `docs/TYPES.md` | Sections 7.2, 8.2, 8.3, 9 | Vocabulary for SdkOptionsBuilder, settings, permission, tools, session linkage |
| REF-005 | `docs/PLAN.md` | Sections 2-4, 6-8 | Roadmap sequencing, tests, known SDK risks |
| REF-006 | `docs/PRD.md` | Sections 8.4, 8.12, 8.13, 10.3.1, KG-021 through KG-032 | Product requirements; source hash mismatch noted |
| REF-DEC | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-04-02; SOW-016, SOW-045, SOW-047, SOW-052 | Deliverable scope and traceability |
