# Specification: DEL-08-01 Instruction Root Packaging and Agent Conformance

## Scope

This deliverable specifies the test-suite expectations for verifying instruction-root packaging and agent instruction conformance in PKG-08.

In scope:

- Required instruction-root asset presence and packaging integrity checks.
- Agent instruction filename, header, metadata, write-scope, and section-marker conformance.
- Source-completeness checklist coverage for instruction-root assets.
- Fixture coverage for valid and invalid instruction-root and agent-instruction cases.

Out of scope:

- General SDK adapter mechanics. Source: `_CONTEXT.md`.
- Runtime capability expansion. Source: decomposition DEL-08-01 row.
- Implementation of the subagent governance bridge itself, which belongs to DEL-08-04. Source: decomposition DEL-08-04 row.
- Parent-child subagent run records, which belong to DEL-08-05. Source: decomposition DEL-08-05 row.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL0801-REQ001 | The test suite MUST verify that the instruction root is treated as release-managed and read-only during ordinary project execution. | `docs/SPEC.md` section 1.1; `docs/CONTRACT.md` K-ROOT-2 | Negative fixture or runtime-policy test denies instruction-root writes. |
| DEL0801-REQ002 | The test suite MUST verify that the working root is separate from the instruction root and is the ordinary project-truth write location. | `docs/DIRECTIVE.md` section 2.7; `docs/CONTRACT.md` K-ROOT-1/K-ROOT-3 | Path-policy fixture validates separate roots and rejects working-root-inside-instruction-root cases. |
| DEL0801-REQ003 | The test suite MUST check the required instruction-root entries listed by SPEC section 1.1. | `docs/SPEC.md` section 1.1 | Integrity fixture enumerates required entries and reports missing assets as blockers. |
| DEL0801-REQ004 | The test suite SHOULD include PRD FR-058 packaging acceptance entries under the current D-APP-38 authority corpus. | `_REFERENCES.md`; `docs/PRD.md` FR-058; D-APP-38 | Checklist output cites the current REF-006 MATCH source state. |
| DEL0801-REQ005 | The source-completeness checklist MUST surface SOW-073 / OI-004 required instruction-root asset incompleteness as a packaging-readiness issue. | Decomposition SOW-073 and OI-004; `docs/PRD.md` KG-001 under D-APP-38 | Checklist contains SOW-073/OI-004 row and remediation status. |
| DEL0801-REQ006 | Agent instruction files MUST be named with the `AGENT_*.md` convention. | `docs/SPEC.md` section 7 | Validator rejects nonconforming agent instruction filenames when they are in the instruction agent set. |
| DEL0801-REQ007 | Agent instruction files MUST include the required instruction header and `AGENT_TYPE` declaration. | `docs/SPEC.md` section 7.1 | Validator positive/negative fixtures cover missing `[[DOC:AGENT_INSTRUCTIONS]]`, title, and `AGENT_TYPE`. |
| DEL0801-REQ008 | Agent instruction files MUST include an Agent Type table with `AGENT_TYPE`, `AGENT_CLASS`, `INTERACTION_SURFACE`, `WRITE_SCOPE`, `BLOCKING`, and `PRIMARY_OUTPUTS`. | `docs/SPEC.md` section 7.2 | Validator fixture rejects missing table or missing required rows. |
| DEL0801-REQ009 | Agent instruction conformance MUST validate required section markers for `PROTOCOL`, `SPEC`, `STRUCTURE`, and `RATIONALE` where the instruction contract requires those sections. | `docs/SPEC.md` section 7.3 | Validator fixture rejects missing begin/end marker pairs. |
| DEL0801-REQ010 | Agent conformance MUST verify explicit write-scope declaration and preserve the invariant that agents do not write outside declared scope. | `docs/CONTRACT.md` K-WRITE-1; `docs/TYPES.md` AGENT classification properties | Validator checks `WRITE_SCOPE` value; downstream runtime tests cover enforcement. |
| DEL0801-REQ011 | Type 2 candidate checks MUST identify `AGENT_TYPE: 2` and prefer `AGENT_CLASS: TASK`. | `docs/TYPES.md` Type 2 vocabulary | Fixture set includes valid Type 2 task, Type 2 non-task warning/TBD behavior, and non-Type-2 rejection. |
| DEL0801-REQ012 | Subagent-related conformance MUST fail closed when required governance metadata is absent and MUST NOT grant child agents expanded capabilities. | `docs/CONTRACT.md` K-SEAL-1, K-GHOST-1, K-SUBAGENT-1, K-SUBAGENT-2; `docs/PRD.md` FR-060 under D-APP-38 | Governance fixture asserts absent metadata is denied and child cwd/tools remain restricted. |
| DEL0801-REQ013 | The validator MUST treat registry surfaces as source registries rather than relying on mutable count prose. | `docs/PRD.md` KG-013 under D-APP-38 | Checklist records registry source paths and generated discovery output. |
| DEL0801-REQ014 | Unknown runtime metadata option keys MUST be ignored with warnings rather than silently mutating behavior. | `docs/SPEC.md` section 7.4 | Fixture includes unknown key and expects warning-only behavior. |

## Standards

| Standard / authority | Applicability | Location |
|---|---|---|
| Chirality instruction root model | Defines required assets, read-only policy, and root separation. | `docs/SPEC.md` section 1; `docs/DIRECTIVE.md` section 2.7 |
| Chirality agent instruction contract | Defines required filenames, headers, metadata table, and section markers. | `docs/SPEC.md` section 7 |
| Chirality invariant contract | Defines K-ROOT, K-PACKAGE, K-WRITE, K-SEAL, K-GHOST, and K-SUBAGENT checks. | `docs/CONTRACT.md` sections 1.3 and 1.8 |
| Chirality vocabulary | Defines Type 2 candidates, task agents, write-scope vocabulary, and pipeline/task scope terms. | `docs/TYPES.md` sections 3.2, 4.4, Type 2 vocabulary |
| PRD acceptance requirements | Provides FR-058 through FR-063 and known source-completeness gaps, current under D-APP-38 authority corpus v2. | `docs/PRD.md` sections 8.10 and 15 |

## Verification

Verification approach:

- Static source-tree checks for required instruction-root entries.
- Static agent-instruction parsing checks for filename, header, required metadata, and marker pairs.
- Fixture-driven positive and negative cases for missing assets and malformed agent files.
- Path-policy / hook-level tests for instruction-root write denial where runtime enforcement is available.
- Checklist output that separates SPEC-backed requirements from PRD-backed source-corpus items.

Minimum verification matrix:

| Requirement IDs | Verification artifact |
|---|---|
| DEL0801-REQ001, DEL0801-REQ002 | Root policy fixtures and hook/path-policy test |
| DEL0801-REQ003, DEL0801-REQ004, DEL0801-REQ005 | Instruction-root integrity fixture and source-completeness checklist |
| DEL0801-REQ006 through DEL0801-REQ010, DEL0801-REQ014 | Agent conformance validator fixture suite |
| DEL0801-REQ011, DEL0801-REQ012 | Type 2/subagent governance fixture suite |
| DEL0801-REQ013 | Registry discovery / source registry fixture |

## Documentation

Required records:

- Validator output showing checked files, failures, warnings, and skipped checks.
- Integrity fixture inventory for required instruction-root assets.
- Source-completeness checklist, including SOW-073/OI-004 status.
- D-APP-38 source-corpus state in any checklist item that relies on `docs/PRD.md`.
- Validator implementation path, fixture path, test framework, local command, CI location, and output artifact directory: TBD until the coding task opens and records the concrete test owner.
- When the implementation owner selects those paths, this deliverable must record the command, fixture directory, pass/fail artifact directory, and whether CI runs the same command or a named wrapper.
- Human ruling record if the authority-corpus basis changes.
