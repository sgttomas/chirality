# Source Pack: SRC-DEL-DEL-04-04-PERSONACOMPOSER-FROM-INSTRUCTION-ROOT

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Datasheet.md

### Datasheet: DEL-04-04 PersonaComposer from Instruction Root

#### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-04-04 |
| DeliverableName | PersonaComposer from Instruction Root |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-017, SOW-030 |
| SupportsObjectives | OBJ-004, OBJ-007 |

Source: `_CONTEXT.md` Identity, Package Scope, Deliverable Scope, Traceability; decomposition `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 8 / PKG-04 row.

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Persona prompt composition from the instruction root, active persona, working-root policy, mode, and tool surface. | `_CONTEXT.md` Deliverable Scope; `docs/SPEC.md` Section 13.2; decomposition DEL-04-04 row |
| Runtime position | Backend feature slice in the SDK adapter/prompt/provider/settings package. | `_CONTEXT.md` Type and Package Scope |
| Product-owned boundary | Prompt/persona composition is owned by Chirality, not by SDK defaults or vendor-specific product semantics. | `docs/DIRECTIVE.md` Sections 2.8-2.10; `docs/CONTRACT.md` Section 1.4 |
| Instruction-root relationship | Reads release-managed instruction-root governance and selected `agents/AGENT_<persona>.md` content; ordinary execution must not mutate the instruction root. | `docs/SPEC.md` Sections 1.1 and 13.2; `docs/CONTRACT.md` Section 1.3 |
| Working-root relationship | Includes working-root summary/policy in prompt composition while preserving instruction-root/working-root separation. | `docs/SPEC.md` Sections 1.2 and 13.2; `docs/DIRECTIVE.md` Section 2.7 |
| Persona aliases | UI aliases map to canonical agents, including `HELP -> HELP_HUMAN`, `ORCHESTRATE -> ORCHESTRATOR`, `AGGREGATE -> AGGREGATION`, `RECONCILING -> RECONCILIATION`, and `AGENTS -> HELPS_HUMANS`. | `docs/TYPES.md` Section 3.4 |
| Boot fingerprint | Should include hashes for persona content, governance preface, mode, SDK tool names/versions, permission-policy version, settings-source posture, MCP server versions, and subagent policy version. | `docs/SPEC.md` Section 13.2; `docs/PRD.md` Section 8.4 (HASH_MISMATCH warning) |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| Source-state warning | `docs/PRD.md` is accessible but has `HASH_MISMATCH` in `_REFERENCES.md`; PRD-derived details require confirmation against an accepted snapshot before being treated as final project truth. | `_REFERENCES.md` REF-006 |
| Runtime option fallbacks | Persona fallback is request/session persona, then `HELP_HUMAN` or configured default. Other option fallback chains are owned by adjacent SDK-options work. | `docs/SPEC.md` Section 13.1; decomposition DEL-04-02 and DEL-04-04 rows |
| Safety boundary | Prompt text is not sufficient as a reliance boundary; permission, path, hook, and tool enforcement remain runtime code responsibilities. | `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14.3 and 15 |
| Settings isolation | The composer must not depend on ambient SDK settings; shipped SDK options use `settingSources: []` outside this deliverable's implementation responsibility. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| Dependencies | Declared upstream/downstream sections remain TBD, but the extracted dependency register records ACTIVE upstream interfaces/prerequisites for DEL-04-02, DEL-08-01, and DEL-08-02, a PRD snapshot constraint, and a downstream boot/session fingerprint handoff whose consuming interface is `UNKNOWN` / `TBD`. | `_DEPENDENCIES.md` Extracted Dependency Register; `Dependencies.csv` DEP-04-04-004 through DEP-04-04-008 |

#### Construction

| Artifact | Expected Role | Notes |
|---|---|---|
| `persona-composer.ts` | Build system/appended prompt material from governance preface, selected persona instruction, working-root summary, mode policy, permitted tool surface, and professional-boundary reminders. | Anticipated by `_CONTEXT.md`; exact module path TBD. |
| Persona content hash tests | Prove persona instruction content and prompt inputs affect the generated fingerprint. | Anticipated by `_CONTEXT.md`; test file path TBD. |
| Boot fingerprint updates | Extend boot/session metadata to reflect prompt and SDK-policy inputs. | Anticipated by `_CONTEXT.md`; `docs/SPEC.md` Sections 12.4 and 13.2; downstream consuming deliverable/interface remains `UNKNOWN` / `TBD` in `Dependencies.csv` DEP-04-04-008. |

#### References

| RefID | Source | Relevant Slice | Status |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 2.6-2.11, 4.1 | MATCH |
| REF-002 | `docs/CONTRACT.md` | Sections 1.3-1.6 | MATCH |
| REF-003 | `docs/SPEC.md` | Sections 1.1-1.3, 10, 12-15 | MATCH |
| REF-004 | `docs/TYPES.md` | Sections 3.4, 7-9, validation vocabulary | MATCH |
| REF-005 | `docs/PLAN.md` | R1 prompt composer target and validation categories | MATCH |
| REF-006 | `docs/PRD.md` | Section 8.4 and related SDK/runtime requirements | HASH_MISMATCH |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method reference | MATCH; not used for implementation requirements |

## Component: execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Guidance.md

### Guidance: DEL-04-04 PersonaComposer from Instruction Root

#### Purpose

DEL-04-04 exists to replace stub persona prompt behavior with a governed PersonaComposer that reads Chirality instruction-root materials and produces prompt context suitable for the SDK-backed runtime path. The value of the slice is not more prompt text by itself; it is making prompt composition deterministic, traceable, source-grounded, and bounded by Chirality-owned runtime policy.

Sources: `_CONTEXT.md` Deliverable Scope; decomposition DEL-04-04 row; `docs/DIRECTIVE.md` Sections 2.8-2.10; `docs/SPEC.md` Section 13.2.

#### Principles

1. Chirality owns the prompt contract.
   The SDK may host generic model/tool-loop mechanics, but prompt/persona composition is a Chirality-owned product contract. Do not let SDK defaults, SDK transcript shape, vendor product assumptions, or ambient settings decide PersonaComposer behavior. Source: `docs/DIRECTIVE.md` Section 2.8; `docs/PLAN.md` approved vNext direction.

2. The instruction root is read authority, not a runtime write target.
   PersonaComposer may read release-managed governance and `agents/AGENT_<persona>.md` files, but ordinary project execution must not mutate those resources. Source: `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2.

3. Prompt text supports policy; it does not enforce policy.
   Include mode and tool-surface descriptions in prompt context, but rely on SDK options, denied tools, hooks, `canUseTool`, path policy, and Chirality overlays for enforcement. Source: `docs/CONTRACT.md` K-PERM-2 and K-PERM-3; `docs/SPEC.md` Sections 14.3 and 15.

4. Fingerprints should reflect real inputs.
   A boot fingerprint that only hashes persona name and mode is insufficient for the target behavior. It should reflect actual persona content, governance preface, mode, tool/policy inputs, settings-source posture, MCP server versions, and subagent policy version when those inputs exist. Source: `docs/SPEC.md` Section 13.2.

5. Keep provider-specific terms behind the adapter boundary.
   The composed prompt can mention the configured permitted tool surface, but public Chirality contracts and runtime events must remain provider-neutral. Source: `docs/DIRECTIVE.md` Section 2.10; `docs/SPEC.md` Section 10.3.

#### Considerations

- Use `docs/TYPES.md` Section 3.4 for alias vocabulary unless a more specific accepted alias resolver exists by implementation time.
- Treat the working-root summary as contextual prompt material, not as instruction-root governance and not as project truth validation.
- Keep prompt assembly deterministic: stable section ordering, stable omitted-field behavior, and explicit handling for missing optional inputs.
- Prefer structured composer inputs over ad hoc strings so tests can isolate persona content, governance preface, mode, tool surface, and fingerprint material.
- If DEL-04-02 owns the final SDK option/tool-surface object, this deliverable should accept that resolved surface rather than reconstruct it.
- Resolve aliases locally only for the canonical vocabulary in `docs/TYPES.md` Section 3.4, or delegate when an accepted DEL-08-02 resolver/interface exists. The decision criterion is ownership: local handling is appropriate for stable source-defined mappings needed to reach `agents/AGENT_<persona>.md`; delegation is appropriate when the routing contract owns broader UI/matrix alias behavior or exposes a tested resolver.
- If DEL-08-01 or DEL-08-02 changes instruction-root packaging or alias contracts, update the composer through an explicit dependency note rather than local convention.

#### Trade-offs

| Decision Area | Preferred Direction | Trade-off |
|---|---|---|
| Prompt detail vs. enforcement | Include concise governance/mode/tool reminders, but enforce with runtime policy. | Long prompts can drift into false reliance if not backed by hooks and permissions. |
| Direct alias handling vs. delegated resolver | Handle only source-defined alias mappings locally unless DEL-08-02 provides an accepted resolver/interface; then delegate to that resolver and keep missing-persona behavior visible. | Duplicating alias logic risks divergence with the routing contract; over-delegation can obscure missing persona failures if the resolver does not return canonical agent names and typed failures. |
| Fingerprint breadth | Hash real prompt and policy inputs that affect runtime behavior. | Broader fingerprints can churn when non-semantic metadata changes; define stable normalized inputs. |
| SDK-specific names in prompt | Keep SDK-specific names as adapter/tool metadata where necessary. | Overexposure can make Chirality appear SDK-shaped; underexposure can make tool context unclear. |

#### Examples

TBD: Final prompt template examples require accepted implementation interfaces for PersonaComposer inputs, resolved tool surface, working-root summary shape, and boot metadata shape.

ASSUMPTION: A useful test fixture can vary one input at a time, such as agent instruction content, mode, and visible tool list, and assert the boot fingerprint changes for each supported input.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-001 | `docs/PRD.md` is listed as `HASH_MISMATCH`, but decomposition SOW rows cite PRD sections for persona and instruction-root scope. | `_REFERENCES.md` REF-006 | Decomposition SOW-017 / SOW-030 and `docs/PRD.md` Section 8.4 | Datasheet References; Specification PC-REQ-004, PC-REQ-006, PC-REQ-010, PC-REQ-011 | Treat PRD-derived details as source-state warnings; prefer matching `docs/SPEC.md`, `docs/CONTRACT.md`, `docs/DIRECTIVE.md`, `docs/TYPES.md`, and accepted decomposition where they overlap. | TBD |

#### Source-State Warning

`docs/PRD.md` was read because it is an authoritative corpus entry, but `_REFERENCES.md` records a hash mismatch. Claims that depend only on PRD content are labeled with a HASH_MISMATCH warning or preserved as `TBD`/`ASSUMPTION`.

## Component: execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Procedure.md

### Procedure: DEL-04-04 PersonaComposer from Instruction Root

#### Purpose

Provide an operational path for implementing and verifying the PersonaComposer slice so it replaces stub prompt behavior with deterministic, source-grounded prompt composition from instruction-root governance, active persona, working-root policy, mode, and permitted tool-surface inputs.

#### Prerequisites

| Item | Requirement / Status | Source |
|---|---|---|
| Instruction root | Must be readable and contain required governance and agent resources. | `docs/SPEC.md` Section 1.1 |
| Working root | Must remain separate from the instruction root and provide contextual project-root information only. | `docs/SPEC.md` Section 1.2; `docs/DIRECTIVE.md` Section 2.7 |
| Persona alias vocabulary | Use or delegate the accepted alias mappings. | `docs/TYPES.md` Section 3.4 |
| Runtime mode/tool policy | Use resolved mode and permitted tool-surface inputs supplied by the runtime/options layer. | `docs/SPEC.md` Sections 13-15 |
| Upstream dependencies | Extracted ACTIVE upstream edges identify DEL-04-02 for resolved mode/tool-surface inputs, DEL-08-01 for instruction-root packaging/conformance, DEL-08-02 for alias routing/resolver interface, and a PRD source-snapshot constraint. Declared dependency sections remain TBD until accepted by the governing dependency workflow. | `_DEPENDENCIES.md` Extracted Dependency Register; `Dependencies.csv` DEP-04-04-004 through DEP-04-04-007 |
| Source-state warning | Treat `docs/PRD.md` hash mismatch as a warning; do not rely on PRD-only details without confirmation. | `_REFERENCES.md` REF-006 |

#### Steps

1. Confirm target boundaries.
   Verify the implementation remains in the prompt/persona composition slice and does not absorb SDK option building, Provider/SDK message mapping, provider key/network handling, or instruction-root packaging conformance.

2. Define PersonaComposer inputs.
   Include at minimum selected persona, normalized project root or working-root summary, mode, permitted tool surface, governance preface source, persona instruction content source, and available fingerprint-policy inputs. The accepted runtime input interface is `TBD`; preserve unresolved fields as explicit optional/TBD inputs rather than inventing an implementation contract.

3. Resolve persona identity.
   Normalize aliases according to accepted vocabulary or delegate to the accepted alias resolver. Resolve the canonical persona to `agents/AGENT_<persona>.md`. Missing persona behavior should produce a typed failure; exact token `PERSONA_NOT_FOUND` is PRD-derived and requires confirmation against an accepted PRD snapshot.

4. Read instruction-root content.
   Read required governance preface material and selected agent instruction content from the instruction root. Do not write to the instruction root. Preserve instruction-root path protection as runtime policy, not prompt convention.

5. Compose prompt material deterministically.
   Build a stable ordered prompt from governance preface, selected persona instruction, working-root boundary/summary, mode policy, permitted tool surface, and professional-boundary reminders. Omit unavailable optional sections in a documented stable way or mark them `TBD` in tests/fixtures.

6. Preserve policy boundaries.
   Ensure prompt text describes mode/tool posture but does not claim to enforce permissions. Runtime enforcement must remain with SDK options, denied tools, `canUseTool`, hooks, path containment, and Chirality overlays.

7. Produce boot fingerprint inputs.
   Normalize and hash supported inputs such as persona content, governance preface, mode, visible SDK tool names/versions, permission-policy version, settings-source posture, MCP server versions, and subagent policy version. Where an input is not yet available from adjacent slices, record it as `TBD` or an explicit optional field.

8. Integrate with the runtime boundary.
   Pass composed prompt material and fingerprint metadata to the product-owned runtime boundary without making public APIs, `UIEvent`, `HarnessEvent`, or session storage SDK-shaped.

9. Add tests.
   Add persona content hash tests, fingerprint sensitivity tests, missing persona tests, alias tests or resolver-delegation tests, prompt section inclusion tests, and checks that API keys/transcripts/local presets do not become prompt authority.

10. Record unresolved dependencies.
   If implementation depends on DEL-04-02 tool-surface shape, DEL-08-01 instruction-root integrity, or DEL-08-02 alias routing, record the dependency explicitly for extraction rather than encoding a silent local assumption.

#### Verification

| Check | Expected Result |
|---|---|
| Four-document consistency | Datasheet, Specification, Guidance, and Procedure use the same deliverable identity and source-state warning. |
| Persona resolution | Canonical personas resolve to instruction-root `AGENT_*.md`; missing personas fail in a typed way. |
| Prompt contents | Prompt includes governance preface, selected persona instruction, working-root boundaries, mode policy, permitted tool surface, and professional-boundary reminders. |
| Policy separation | Tests or review confirm prompt text is not used as the sole permission/path/tool enforcement boundary. |
| Fingerprint sensitivity | Fingerprint changes when supported prompt/policy inputs change. |
| Source-state handling | PRD-only claims remain warned, `TBD`, or `ASSUMPTION` until an accepted PRD snapshot is available. |

#### Records

- Implementation artifact: `persona-composer.ts` or accepted equivalent.
- Tests: persona content hash tests, boot fingerprint tests, alias/missing-persona tests, prompt-content tests.
- Integration evidence: boot/session fingerprint metadata update; downstream consuming deliverable/interface is currently `UNKNOWN` / `TBD` per `Dependencies.csv` DEP-04-04-008.
- Open items: exact runtime input interface, downstream fingerprint handoff consumer, and accepted PRD snapshot confirmation.

## Component: execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Specification.md

### Specification: DEL-04-04 PersonaComposer from Instruction Root

#### Scope

This deliverable specifies the backend PersonaComposer slice for replacing stub prompt behavior with source-grounded prompt composition. It covers composition from instruction-root governance, the active persona, working-root policy, current mode, and the permitted tool surface.

Included:

- Resolve selected personas and alias-normalized persona names to instruction-root `agents/AGENT_<persona>.md` content.
- Compose prompt material from the governance preface, selected agent instruction, working-root summary, mode policy, permitted tool surface, and professional-boundary reminders.
- Preserve instruction-root/working-root separation and product-owned runtime semantics.
- Provide boot fingerprint inputs that reflect actual prompt and SDK-policy material.
- Add tests for persona content hashing and fingerprint sensitivity.

Excluded:

- SDK option construction, `settingSources: []`, and tool list construction beyond accepting/reflecting the configured permitted tool surface; these belong primarily to DEL-04-02.
- SDK stream/message translation; this belongs to DEL-04-03.
- API key, base URL, network policy, and provider error classification; these belong to DEL-04-05.
- Instruction-root packaging conformance beyond consuming readable instruction-root files; this belongs primarily to DEL-08-01 and DEL-09-04.

Sources: `_CONTEXT.md` Deliverable Scope and Anticipated Artifacts; decomposition DEL-04-04 row; `docs/SPEC.md` Sections 10, 12-15.

#### Requirements

| ID | Requirement | Source |
|---|---|---|
| PC-REQ-001 | The composer MUST consume a validated instruction root containing the required governance and agent resources before reading persona content. | `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2 / K-PACKAGE-1 |
| PC-REQ-002 | The composer MUST NOT write to the instruction root during ordinary runtime execution. | `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2 |
| PC-REQ-003 | The composer MUST preserve instruction-root and working-root separation; working-root summary/policy content must not be treated as instruction-root governance. | `docs/DIRECTIVE.md` Section 2.7; `docs/SPEC.md` Sections 1.1-1.2 |
| PC-REQ-004 | Persona names MUST resolve to canonical `agents/AGENT_<persona>.md` instruction files. Missing persona handling is `PERSONA_NOT_FOUND` per PRD, but this exact error token is PRD-derived and subject to the REF-006 hash warning. | `docs/SPEC.md` Section 13.2; `docs/PRD.md` Section 8.4 (HASH_MISMATCH warning) |
| PC-REQ-005 | Persona aliases SHOULD use the canonical mappings in `docs/TYPES.md` Section 3.4 before instruction-file lookup, or delegate to an accepted alias resolver that implements those mappings. | `docs/TYPES.md` Section 3.4; decomposition SOW-017 |
| PC-REQ-006 | The composed prompt MUST include selected agent instruction content, global/governance context, working-root boundaries, mode policy, and the configured permitted tool surface. | `docs/SPEC.md` Section 13.2; `docs/PRD.md` FR-028 (HASH_MISMATCH warning) |
| PC-REQ-007 | The composed prompt MUST include professional-boundary reminders and MUST NOT imply autonomous professional approval, certification, signing, sealing, issuing, or external validation. | `docs/DIRECTIVE.md` Sections 2.8 and 4.2; `docs/CONTRACT.md` K-AUTH-1 |
| PC-REQ-008 | Prompt text MUST NOT be treated as the enforcement boundary for filesystem writes, tool exposure, bash, subagents, or domain operations. | `docs/CONTRACT.md` K-PERM-2; `docs/SPEC.md` Sections 14.3 and 15 |
| PC-REQ-009 | The composer MUST keep Chirality contracts provider-neutral; SDK names, transcript paths, and permission modes may appear only as adapter metadata or prompt support, not as public contract definitions. | `docs/DIRECTIVE.md` Section 2.10; `docs/CONTRACT.md` K-ENGINE-4; `docs/SPEC.md` Section 10.3 |
| PC-REQ-010 | Boot fingerprints SHOULD include persona content hash, governance preface hash, mode, SDK tool names/versions, permission-policy version, settings-source posture, MCP server versions, and subagent policy version when those inputs are available. The composer-owned test surface is persona content, governance preface, mode, and accepted visible tool-surface/fingerprint inputs; adjacent unresolved inputs remain `TBD` until their owning slices expose stable values. | `docs/SPEC.md` Sections 12.4 and 13.2; `docs/PRD.md` FR-029 (HASH_MISMATCH warning); `Dependencies.csv` DEP-04-04-004 and DEP-04-04-008 |
| PC-REQ-011 | Unknown runtime option keys relevant to composition MUST be ignored with warnings rather than silently mutating prompt behavior. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-024 (HASH_MISMATCH warning) |
| PC-REQ-012 | The composer MUST treat SDK transcripts, chat drafts, local presets, model context, API keys, and runtime caches as non-authoritative unless imported through a governed project-file process. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |

#### Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Instruction-root contract | Required resources, read-only ordinary execution, integrity expectations. | `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` Section 1.3 |
| Runtime engine boundary | Composer output feeds a product-owned runtime boundary, not SDK-shaped public semantics. | `docs/SPEC.md` Section 10; `docs/CONTRACT.md` Section 1.4 |
| Runtime options and persona composition | Defines fallback chains and prompt composition ingredients. | `docs/SPEC.md` Section 13 |
| Tool-surface and permission policy | Prompt content may describe mode/tool posture, but runtime restrictions require code-level enforcement. | `docs/SPEC.md` Sections 14-15; `docs/CONTRACT.md` Section 1.6 |
| Persona alias vocabulary | Canonical UI alias to agent mapping. | `docs/TYPES.md` Section 3.4 |

#### Verification

| Requirement(s) | Verification Approach |
|---|---|
| PC-REQ-001 through PC-REQ-005 | Unit tests for instruction-root validation, canonical persona path resolution, alias mapping or alias-resolver delegation, and missing persona behavior. |
| PC-REQ-006 through PC-REQ-009 | Snapshot or structured-content tests proving the composed prompt includes governance preface, selected agent instruction content, working-root boundaries, mode policy, permitted tool surface, and professional-boundary reminders while avoiding SDK-shaped public contracts. |
| PC-REQ-010 | Split fingerprint verification into (a) composer-available inputs: persona content, governance preface, mode, and accepted visible tool-surface/fingerprint fields; and (b) adjacent optional inputs: permission-policy version, settings-source posture, MCP server versions, subagent policy version, and downstream handoff interface, each verified only when supplied by the owning slice. Unavailable inputs remain `TBD` rather than being treated as immediately testable. |
| PC-REQ-011 | Runtime option tests proving unknown composition-related option keys warn and do not mutate prompt behavior. |
| PC-REQ-012 | Tests or review checks proving API keys, SDK transcripts, local presets, and draft chat state are not imported into prompt authority or project truth. |

#### Documentation

Required implementation artifacts:

- `persona-composer.ts` or accepted equivalent module.
- Persona content hash tests.
- Boot fingerprint update tests.
- Source or module comments only where needed to explain non-obvious boundary decisions.
- A short integration note, if needed, naming where the composed prompt enters the SDK-backed engine boundary.

Required traceability:

- Link tests to SOW-017 and SOW-030 where the test framework supports names or comments.
- Record any unresolved dependency on DEL-04-02, DEL-08-01, or DEL-08-02 as `TBD` or `ASSUMPTION` rather than hiding it in implementation behavior.
