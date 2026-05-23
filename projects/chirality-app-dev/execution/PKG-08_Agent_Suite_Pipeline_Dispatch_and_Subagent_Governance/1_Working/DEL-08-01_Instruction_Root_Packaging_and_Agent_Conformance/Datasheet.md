# Datasheet: DEL-08-01 Instruction Root Packaging and Agent Conformance

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-08-01 |
| DeliverableName | Instruction Root Packaging and Agent Conformance |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | TEST_SUITE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-030, SOW-031, SOW-073 |
| SupportsObjectives | OBJ-007, OBJ-008 |

Source: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` lines 340-344, 244-245.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable purpose | Verify required instruction-root assets, agent metadata, write scopes, naming, and section markers. | Decomposition DEL-08-01 row, lines 340-344 |
| Anticipated artifacts | Agent conformance validator; integrity fixtures; source-completeness checklist. | `_CONTEXT.md`; Decomposition DEL-08-01 row, lines 340-344 |
| Instruction root meaning | Release-managed resource set containing governance documents, agent instructions, and framework materials. | `docs/SPEC.md` section 1.1; `docs/TYPES.md` section 1.5 |
| Ordinary mutation policy | Instruction root is read-only during ordinary project execution; writes must be blocked by runtime hooks and path policy. | `docs/SPEC.md` section 1.1; `docs/CONTRACT.md` K-ROOT-2 |
| Required source-tree / packaged-app entries | `AGENTS.md`, `README.md`, `agents/`, `docs/`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `WHAT-IS-AN-AGENT.md` where required, and `PROFESSIONAL_ENGINEERING.md` where required. | `docs/SPEC.md` section 1.1 |
| PRD packaging acceptance entries | `agents/`, `docs/`, `AGENTS.md`, `README.md`, `WHAT-IS-AN-AGENT.md`, and `PROFESSIONAL_ENGINEERING.md` where required by integrity policy. | `docs/PRD.md` FR-058; source hash mismatch warning applies |
| Agent instruction file naming | Agent instruction files use `AGENT_*.md` names. | `docs/SPEC.md` section 7 |
| Required instruction header | `[[DOC:AGENT_INSTRUCTIONS]]`, title, and `AGENT_TYPE: {0|1|2}`. | `docs/SPEC.md` section 7.1 |
| Required agent type table fields | `AGENT_TYPE`, `AGENT_CLASS`, `INTERACTION_SURFACE`, `WRITE_SCOPE`, `BLOCKING`, `PRIMARY_OUTPUTS`. | `docs/SPEC.md` section 7.2 |
| Required section markers | `[[BEGIN:PROTOCOL]]`, `[[BEGIN:SPEC]]`, `[[BEGIN:STRUCTURE]]`, `[[BEGIN:RATIONALE]]` and matching end markers. | `docs/SPEC.md` section 7.3 |
| Type 2 candidate definition | Agent instruction with `AGENT_TYPE: 2`; preferred `AGENT_CLASS: TASK`. | `docs/TYPES.md` Type 2 vocabulary |
| Type 2 execution constraint | Type 2 task-agent execution requires sealed context and gate approval metadata. | `docs/CONTRACT.md` K-SEAL-1 |
| Write-scope invariant | Every agent instruction file declares explicit write scope; agents must not write outside declared scope. | `docs/CONTRACT.md` K-WRITE-1 |

## Conditions

- This deliverable is a test-suite work item for PKG-08 and must not expand runtime capability. Source: `_CONTEXT.md`; decomposition DEL-08-01 row.
- The test suite must respect instruction-root / working-root separation. Ordinary project execution may write project truth only under the working root. Source: `docs/DIRECTIVE.md` section 2.7; `docs/CONTRACT.md` K-ROOT-3.
- `docs/PRD.md` is locally accessible but recorded as `HASH_MISMATCH` in `_REFERENCES.md`. Treat PRD-derived items as source-warning context until the reference hash is reconciled.
- Declared upstream/downstream dependencies are currently `TBD`; dependency extraction has not yet populated accepted edges. Source: `_DEPENDENCIES.md`.
- ASSUMPTION: The validator target path, test framework, and exact fixture directory are implementation choices for a later coding task and are therefore `TBD` here.

## Construction

Minimum expected construction package:

| Component | Required content | Evidence basis |
|---|---|---|
| Agent conformance validator | Checks instruction files for naming, required header, agent type declaration/table fields, required markers, and declared write scope. | `docs/SPEC.md` section 7; `docs/CONTRACT.md` K-WRITE-1 |
| Integrity fixtures | Positive and negative fixtures for complete and incomplete instruction-root asset sets. | `docs/SPEC.md` section 1.1; `docs/PRD.md` FR-058 and KG-001 with hash warning |
| Source-completeness checklist | Checklist for required root assets and source-completeness risks. | `docs/SPEC.md` section 1.1; `docs/PRD.md` KG-001 with hash warning; decomposition SOW-073 |
| Governance fixture cases | Type 2 candidate, non-Type-2 candidate, missing metadata, missing markers, invalid write scope, and attempted instruction-root write. | `docs/TYPES.md` Type 2 vocabulary; `docs/CONTRACT.md` K-WRITE/K-SEAL/K-GHOST/K-SUBAGENT |

Implementation location, command name, and CI wiring: TBD.

## References

- `docs/DIRECTIVE.md` sections 2.7, 5.
- `docs/CONTRACT.md` sections 1.3 and 1.8.
- `docs/SPEC.md` sections 1.1, 1.2, 7.1, 7.2, 7.3, 15.2.
- `docs/TYPES.md` sections 1.5, 3.2, 4.4, Type 2 vocabulary.
- `docs/PLAN.md` R3 subagent implementation targets and section 6.1.
- `docs/PRD.md` sections 8.10 and 15, with `_REFERENCES.md` `HASH_MISMATCH` warning.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-08-01, OBJ-007, OBJ-008, SOW-030, SOW-031, SOW-073, and PKG-08 knowledge groups.
- `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` header and agent type table as a local conformance example.
