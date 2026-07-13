# Datasheet: DEL-04-04 PersonaComposer from Instruction Root

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

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

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Persona prompt composition from the instruction root, active persona, working-root policy, mode, and tool surface. | `_CONTEXT.md` Deliverable Scope; `docs/SPEC.md` Section 13.2; decomposition DEL-04-04 row |
| Runtime position | Backend feature slice in the SDK adapter/prompt/provider/settings package. | `_CONTEXT.md` Type and Package Scope |
| Product-owned boundary | Prompt/persona composition is owned by Chirality, not by SDK defaults or vendor-specific product semantics. | `docs/DIRECTIVE.md` Sections 2.8-2.10; `docs/CONTRACT.md` Section 1.4 |
| Instruction-root relationship | Reads release-managed instruction-root governance and selected `agents/AGENT_<persona>.md` content; ordinary execution must not mutate the instruction root. | `docs/SPEC.md` Sections 1.1 and 13.2; `docs/CONTRACT.md` Section 1.3 |
| Working-root relationship | Includes working-root summary/policy in prompt composition while preserving instruction-root/working-root separation. | `docs/SPEC.md` Sections 1.2 and 13.2; `docs/DIRECTIVE.md` Section 2.7 |
| Persona aliases | UI aliases map to canonical agents, including `HELP -> HELP_HUMAN`, `ORCHESTRATE -> ORCHESTRATOR`, `AGGREGATE -> AGGREGATION`, `RECONCILING -> RECONCILIATION`, and `AGENTS -> HELPS_HUMANS`. | `docs/TYPES.md` Section 3.4 |
| Boot fingerprint | Should include hashes for persona content, governance preface, mode, SDK tool names/versions, permission-policy version, settings-source posture, MCP server versions, and subagent policy version. | `docs/SPEC.md` Section 13.2; `docs/PRD.md` Section 8.4 (MATCH status) — reconciled under D-APP-38 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source-state warning | `docs/PRD.md` is accessible but has `MATCH` in `_REFERENCES.md`; PRD-derived details require confirmation against an accepted snapshot before being treated as final project truth. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
| Runtime option fallbacks | Persona fallback is request/session persona, then `HELP_HUMAN` or configured default. Other option fallback chains are owned by adjacent SDK-options work. | `docs/SPEC.md` Section 13.1; decomposition DEL-04-02 and DEL-04-04 rows |
| Safety boundary | Prompt text is not sufficient as a reliance boundary; permission, path, hook, and tool enforcement remain runtime code responsibilities. | `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14.3 and 15 |
| Settings isolation | The composer must not depend on ambient SDK settings; shipped SDK options use `settingSources: []` outside this deliverable's implementation responsibility. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| Dependencies | Declared upstream/downstream sections remain TBD, but the extracted dependency register records ACTIVE upstream interfaces/prerequisites for DEL-04-02, DEL-08-01, and DEL-08-02, a PRD snapshot constraint, and a downstream boot/session fingerprint handoff whose consuming interface is `UNKNOWN` / `TBD`. | `_DEPENDENCIES.md` Extracted Dependency Register; `Dependencies.csv` DEP-04-04-004 through DEP-04-04-008 |

## Construction

| Artifact | Expected Role | Notes |
|---|---|---|
| `persona-composer.ts` | Build system/appended prompt material from governance preface, selected persona instruction, working-root summary, mode policy, permitted tool surface, and professional-boundary reminders. | Anticipated by `_CONTEXT.md`; exact module path TBD. |
| Persona content hash tests | Prove persona instruction content and prompt inputs affect the generated fingerprint. | Anticipated by `_CONTEXT.md`; test file path TBD. |
| Boot fingerprint updates | Extend boot/session metadata to reflect prompt and SDK-policy inputs. | Anticipated by `_CONTEXT.md`; `docs/SPEC.md` Sections 12.4 and 13.2; downstream consuming deliverable/interface remains `UNKNOWN` / `TBD` in `Dependencies.csv` DEP-04-04-008. |

## References

| RefID | Source | Relevant Slice | Status |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 2.6-2.11, 4.1 | MATCH |
| REF-002 | `docs/CONTRACT.md` | Sections 1.3-1.6 | MATCH |
| REF-003 | `docs/SPEC.md` | Sections 1.1-1.3, 10, 12-15 | MATCH |
| REF-004 | `docs/TYPES.md` | Sections 3.4, 7-9, validation vocabulary | MATCH |
| REF-005 | `docs/PLAN.md` | R1 prompt composer target and validation categories | MATCH |
| REF-006 | `docs/PRD.md` | Section 8.4 and related SDK/runtime requirements | MATCH — reconciled under D-APP-38 |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method reference | MATCH; not used for implementation requirements |

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-122 records accepted alias delegation to the shell persona resolver; the composer need not duplicate it. UPD-123 records DEP-04-04-004 retirement and corrected register counts.
