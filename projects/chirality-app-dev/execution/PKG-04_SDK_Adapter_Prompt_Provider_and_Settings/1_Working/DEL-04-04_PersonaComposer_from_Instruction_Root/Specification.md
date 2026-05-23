# Specification: DEL-04-04 PersonaComposer from Instruction Root

## Scope

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

## Requirements

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
| PC-REQ-010 | Boot fingerprints SHOULD include persona content hash, governance preface hash, mode, SDK tool names/versions, permission-policy version, settings-source posture, MCP server versions, and subagent policy version when those inputs are available. | `docs/SPEC.md` Section 13.2; `docs/PRD.md` FR-029 (HASH_MISMATCH warning) |
| PC-REQ-011 | Unknown runtime option keys relevant to composition MUST be ignored with warnings rather than silently mutating prompt behavior. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-024 (HASH_MISMATCH warning) |
| PC-REQ-012 | The composer MUST treat SDK transcripts, chat drafts, local presets, model context, API keys, and runtime caches as non-authoritative unless imported through a governed project-file process. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Instruction-root contract | Required resources, read-only ordinary execution, integrity expectations. | `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` Section 1.3 |
| Runtime engine boundary | Composer output feeds a product-owned runtime boundary, not SDK-shaped public semantics. | `docs/SPEC.md` Section 10; `docs/CONTRACT.md` Section 1.4 |
| Runtime options and persona composition | Defines fallback chains and prompt composition ingredients. | `docs/SPEC.md` Section 13 |
| Tool-surface and permission policy | Prompt content may describe mode/tool posture, but runtime restrictions require code-level enforcement. | `docs/SPEC.md` Sections 14-15; `docs/CONTRACT.md` Section 1.6 |
| Persona alias vocabulary | Canonical UI alias to agent mapping. | `docs/TYPES.md` Section 3.4 |

## Verification

| Requirement(s) | Verification Approach |
|---|---|
| PC-REQ-001 through PC-REQ-005 | Unit tests for instruction-root validation, canonical persona path resolution, alias mapping or alias-resolver delegation, and missing persona behavior. |
| PC-REQ-006 through PC-REQ-009 | Snapshot or structured-content tests proving the composed prompt includes governance preface, selected agent instruction content, working-root boundaries, mode policy, permitted tool surface, and professional-boundary reminders while avoiding SDK-shaped public contracts. |
| PC-REQ-010 | Fingerprint tests proving changes to persona content, governance preface, mode, visible tool surface, permission-policy version, settings-source posture, MCP server versions, or subagent policy version change the boot fingerprint when those inputs are present. |
| PC-REQ-011 | Runtime option tests proving unknown composition-related option keys warn and do not mutate prompt behavior. |
| PC-REQ-012 | Tests or review checks proving API keys, SDK transcripts, local presets, and draft chat state are not imported into prompt authority or project truth. |

## Documentation

Required implementation artifacts:

- `persona-composer.ts` or accepted equivalent module.
- Persona content hash tests.
- Boot fingerprint update tests.
- Source or module comments only where needed to explain non-obvious boundary decisions.
- A short integration note, if needed, naming where the composed prompt enters the SDK-backed engine boundary.

Required traceability:

- Link tests to SOW-017 and SOW-030 where the test framework supports names or comments.
- Record any unresolved dependency on DEL-04-02, DEL-08-01, or DEL-08-02 as `TBD` or `ASSUMPTION` rather than hiding it in implementation behavior.
