---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-07-01
package_id: PKG-07
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@2770fda4c63c98ee9f18cffbafd14c9aa59f497f
project_scope_refs: [SOW-002, SOW-027]
package_objective_refs: [OBJ-006, OBJ-008]
---

# Scope of Work — DEL-07-01

## Purpose and Objective Traceability

This candidate defines `DEL-07-01` in service of project scope [SOW-002, SOW-027] and package objectives [OBJ-006, OBJ-008].

- **OUT-001** — Root validation tests, path policy helpers, and instruction-root protection fixtures enforcing working-root validity, root separation, containment, fail-closed hooks, and initial symlink-write rejection.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-07-01 Working Root Validation and Instruction Root Protection

> #### Datasheet: DEL-07-01 Working Root Validation and Instruction Root Protection
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-07-01 |
> | DeliverableName | Working Root Validation and Instruction Root Protection |
> | PackageID | PKG-07 |
> | PackageName | Filesystem Execution, Lifecycle, and Dependencies |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | TBD |
> | Type | SECURITY_CONTROL |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-002, SOW-027 |
> | SupportsObjectives | OBJ-006, OBJ-008 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary control subject | Working-root validity, root separation, path containment, and instruction-root write protection. | `_CONTEXT.md` `Deliverable Scope`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-07` table |
> | Working root meaning | User-selected local filesystem location for project execution state, sessions, artifacts, and git history. | `docs/TYPES.md` Section 1.6 |
> | Instruction root meaning | Release-managed app resource tree containing governance documents, agent instructions, and framework materials. | `docs/TYPES.md` Section 1.5; `docs/SPEC.md` Section 1.1 |
> | Ordinary project truth write location | Working root is the ordinary location where agents and tools write project truth. | `docs/SPEC.md` Section 1.2; `docs/CONTRACT.md` K-ROOT-3 |
> | Validation endpoint | `/api/working-root/validate` validates and normalizes a working root. | `docs/SPEC.md` API endpoints table; `docs/PRD.md` Section 7.1 |
> | Runtime enforcement surfaces | Path helpers, PreToolUse hooks, MCP tools, and Chirality hooks. | `docs/CONTRACT.md` K-PATH-2; `docs/CONTRACT.md` K-ROOT-2 |
> | Anticipated artifacts | Root validation tests; path policy helpers; instruction-root protection fixtures. | `_CONTEXT.md` `Anticipated Artifacts`; decomposition `DEL-07-01` row |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Required Behavior | Source |
> |---|---|---|
> | Working-root path form | Working root must be an absolute existing directory. | `docs/SPEC.md` Section 1.2; `docs/PRD.md` Section 7.1 |
> | Working-root access | Working root must be readable and writable by the app. | `docs/SPEC.md` Section 1.2; `docs/PRD.md` Section 7.1 |
> | Root separation | Working root must not be inside the instruction root. | `docs/SPEC.md` Section 1.2; `docs/CONTRACT.md` K-ROOT-1 |
> | Instruction-root mutation | Ordinary project execution must not mutate the instruction root; writes under instruction root must be denied. | `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2 |
> | Path containment | Runtime tools must enforce working-root containment and reject writes outside the active project root. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |
> | Symlink writes | Symlink writes are rejected in the initial policy. | `docs/CONTRACT.md` K-PATH-3; `docs/SPEC.md` Section 15.2 |
> | Permission override | Deny decisions from policy, hooks, path containment, governance, SDK deny rules, or human gates override allows. | `docs/PRD.md` Section 3; `docs/CONTRACT.md` K-PERM-1 |
> | Source-state warning | `docs/PRD.md` is usable for this draft but has a MATCH in `_REFERENCES.md`; content depending on it should remain review-aware. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Construction Notes | Source |
> |---|---|---|
> | Root validator | Validate absolute path, existence, directory type, readability, writability, and instruction-root containment before use. | `docs/PRD.md` Section 7.1; `docs/PRD.md` FR-003 |
> | Path policy helper | Resolve project-relative and absolute tool paths and reject paths outside the active project root. | `docs/PRD.md` FR-050; `docs/CONTRACT.md` K-PATH-2 |
> | Instruction-root resolver/protection | Identify the active instruction root, including development override behavior, and deny ordinary writes beneath it. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1 |
> | Hook integration | Apply containment, instruction-root protection, symlink rejection, and provenance policy through required hooks before governed writes. | `docs/SPEC.md` Section 15.2; `docs/PRD.md` FR-095 |
> | Test fixtures | Include invalid root cases, instruction-root-contained roots, outside-project paths, instruction-root write attempts, and symlink write attempts. | `docs/PRD.md` FR-003, FR-050, FR-051, FR-095, FR-097 |
> | Code locations | TBD - implementation files are not identified by the authoritative source slices read for this Phase 2.2 draft. | Source-grounding gap |
>

### CLM-006 — Pass 3 Semantic Lensing Notes

> ##### Pass 3 Semantic Lensing Notes
>
> | ItemID | Datasheet Disposition | Evidence |
> |---|---|---|
> | A-001 | converted to TBD | `Construction` keeps code locations as TBD because accessible sources identify required enforcement surfaces but not final runtime module, hook module, path helper, or test file names. |
> | E-002 | incorporated | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
>

### CLM-007 — References

> ##### References
>
> | RefID | SourcePath | SectionRef | Notes |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Sections 2.6-2.9 | Project truth, root separation, reliance boundaries. |
> | REF-002 | `docs/CONTRACT.md` | Sections 1.3, 1.7; K-PATH/K-HOOK rows | Root separation, path containment, hooks, lifecycle invariants. |
> | REF-003 | `docs/SPEC.md` | Sections 1.1, 1.2, 15.2; API endpoints table | Instruction-root and working-root contracts, hooks, API surfaces. |
> | REF-004 | `docs/TYPES.md` | Sections 1.5, 1.6, 8.2 | Vocabulary and permission-mode terms. |
> | REF-005 | `docs/PLAN.md` | Implementation sequencing references to hooks and path containment | Context only; not used as primary authority for requirements. |
> | REF-006 | `docs/PRD.md` | Sections 7.1, 8.9, 8.15, 10.1, 10.2; FR-003, FR-050, FR-051, FR-095, FR-097 | Product requirements. MATCH status recorded in `_REFERENCES.md`. — reconciled under D-APP-38 |
> | REF-007 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PKG-07 and DEL-07-01 rows; SOW mapping rows | Scope routing and deliverable identity. |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-07-01 Working Root Validation and Instruction Root Protection

> #### Specification: DEL-07-01 Working Root Validation and Instruction Root Protection
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies the security-control behavior for validating the active working root and protecting the release-managed instruction root during ordinary project execution.
>
> In scope:
>
> - Working-root validation for absolute path, existence, directory type, app read/write access, and instruction-root containment.
> - Runtime path containment for tools and governed writes under the active project root.
> - Instruction-root write protection for ordinary project execution.
> - Initial symlink-write rejection where write/edit tools are governed by hooks.
> - Root validation tests, path policy helpers, and instruction-root protection fixtures.
>
> Out of scope:
>
> - UI presentation except scope scan results, per `_CONTEXT.md` package exclusions.
> - General write/edit governance beyond root/path policy. `DEL-06-04` covers the broader write/edit surface and path hooks in the decomposition.
> - Instruction-root packaging completeness and release integrity beyond protection behavior. `DEL-08-01` and release verification deliverables cover packaging conformance.
>

### CLM-010 — Terminology

> ##### Terminology
>
> Use these terms consistently in implementation notes and tests:
>
> | Term | Meaning | Source |
> |---|---|---|
> | Working root | User-selected local filesystem root for mutable project execution state. | `docs/TYPES.md` Section 1.6; `docs/SPEC.md` Section 1.2 |
> | `projectRoot` / active project root | Normalized runtime representation of the accepted working root. | `docs/TYPES.md` Section 1.6; `docs/SPEC.md` API/session sections |
> | Instruction root | Release-managed app resource tree that ordinary execution must not mutate. | `docs/TYPES.md` Section 1.5; `docs/SPEC.md` Section 1.1 |
> | Path containment | Policy that resolves tool/write paths against the active project root and rejects escapes. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |
>

### CLM-011 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | REQ-07-01-001 | The working-root validator MUST reject non-absolute paths before a root is used for project execution. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2 |
> | REQ-07-01-002 | The working-root validator MUST reject missing paths, non-directory paths, and paths the app cannot read and write. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2 |
> | REQ-07-01-003 | The working-root validator MUST reject any working root inside the active instruction root. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2; `docs/CONTRACT.md` K-ROOT-1 |
> | REQ-07-01-004 | Ordinary project execution MUST NOT mutate the instruction root. | `docs/DIRECTIVE.md` Section 2.7; `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2 |
> | REQ-07-01-005 | Runtime write/edit/tool paths MUST be resolved against the active project root and rejected when outside the allowed root. | `docs/PRD.md` FR-050, FR-097; `docs/CONTRACT.md` K-PATH-2 |
> | REQ-07-01-006 | Writes under the instruction root MUST be blocked even when an SDK or developer-local permission mode would otherwise allow execution. | `docs/PRD.md` FR-051; `docs/TYPES.md` Section 8.2; `docs/PRD.md` permission mapping table |
> | REQ-07-01-007 | Initial write policy MUST reject symlink writes unless a governed amendment and tests approve relaxation. | `docs/CONTRACT.md` K-PATH-3; `docs/SPEC.md` Section 15.2 |
> | REQ-07-01-008 | Hook failures for write, shell, domain, and subagent actions MUST fail closed when they are part of path or instruction-root enforcement. | `docs/CONTRACT.md` K-HOOK-1 |
> | REQ-07-01-009 | Path containment and instruction-root protection MUST be implemented in runtime code, hooks, and policy helpers, not only prompt text. | `docs/DIRECTIVE.md` Section 2.9; `docs/PRD.md` Section 3 |
> | REQ-07-01-010 | Tests MUST cover valid and invalid working roots, instruction-root-contained roots, outside-project tool paths, instruction-root write attempts, and symlink write attempts. | `docs/PRD.md` FR-003, FR-050, FR-051, FR-095, FR-097 |
> | REQ-07-01-011 | ASSUMPTION: The implementation should expose the validation behavior through `/api/working-root/validate` and reuse the same normalized root for tree, scan, chat session, scaffold, and contract APIs. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` API endpoints table |
>

### CLM-012 — Standards

> ##### Standards
>
> | Standard or Contract | Applicability | Source |
> |---|---|---|
> | Chirality root separation contract | Governs instruction-root and working-root separation. | `docs/CONTRACT.md` Section 1.3 |
> | Chirality filesystem/path contract | Governs working-root containment and symlink write policy. | `docs/CONTRACT.md` K-PATH-2, K-PATH-3 |
> | Chirality hook contract | Governs fail-closed hook behavior and required containment/protection hooks. | `docs/CONTRACT.md` K-HOOK-1; `docs/SPEC.md` Section 15.2 |
> | Chirality API contract | Provides working-root validation and deliverable filesystem API surfaces. | `docs/SPEC.md` API endpoints table |
> | Product requirements | Establish P0/P1 acceptance for validation, containment, instruction-root protection, and safe writes. | `docs/PRD.md` Sections 7.1, 8.9, 8.15; REF-006 MATCH status applies — reconciled under D-APP-38 |
>

### CLM-013 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach | Evidence Record |
> |---|---|---|
> | REQ-07-01-001, REQ-07-01-002 | Unit tests for root validation input cases: relative path, missing path, file path, unreadable path, unwritable path, and valid directory. | Root validation test output; fixture list. |
> | REQ-07-01-003, REQ-07-01-004, REQ-07-01-006 | Unit or integration tests with an instruction-root fixture and nested working-root/write-attempt cases. | Instruction-root protection fixture output. |
> | REQ-07-01-005 | Unit tests for path helper resolution of project-relative, absolute-inside, absolute-outside, traversal, and normalized equivalent paths. | Path policy helper test output. |
> | REQ-07-01-007 | Unit tests using symlink fixtures for write target rejection. | Symlink policy fixture output. |
> | REQ-07-01-008, REQ-07-01-009 | Integration tests proving hooks fail closed and policy denials override permissive modes. | Hook failure triage and permission decision records. |
> | REQ-07-01-010 | Test matrix review against required acceptance cases. | Coverage checklist stored with test fixtures. |
> | REQ-07-01-011 | API test for `/api/working-root/validate` response shape and downstream normalized-root reuse. | API test output; ASSUMPTION remains pending until implementation design confirms reuse path. |
> | REQ-07-01-001 through REQ-07-01-011 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Review note or run record naming `_REFERENCES.md` REF-006 disposition. — reconciled under D-APP-38 |
>

### CLM-014 — Documentation

> ##### Documentation
>
> Required artifacts for this deliverable:
>
> - Root validation tests.
> - Path policy helpers.
> - Instruction-root protection fixtures.
> - Test coverage notes mapping fixtures to SOW-002 and SOW-027.
> - Source-state note that `docs/PRD.md` was available but marked `MATCH` in `_REFERENCES.md`. (reconciled under D-APP-38).
>
> Documentation gaps:
>
> - Code module names and final helper/API locations are TBD.
> - Endpoint reuse through `/api/working-root/validate` and downstream normalized-root consumers remains an ASSUMPTION until implementation design confirms the concrete path.
> - Final test command names and evidence record locations for root validation, path policy, instruction-root protection, hook failure, symlink fixtures, and PRD source-state review are TBD.
> - Responsible party is TBD and must not be assigned without human action.
>

### CLM-015 — Pass 3 Semantic Lensing Notes

> ##### Pass 3 Semantic Lensing Notes
>
> | ItemID | Specification Disposition | Evidence |
> |---|---|---|
> | A-001 | converted to TBD | Documentation gaps explicitly retain unknown code module names, helper/API locations, and test file names rather than inventing implementation paths. |
> | C-001 | already covered | `Standards`, `Verification`, and `Documentation` preserve the PRD MATCH status as review-aware source state. — reconciled under D-APP-38 |
> | F-001 | incorporated | `Terminology` normalizes working root, `projectRoot` / active project root, instruction root, and path containment vocabulary for implementation use. |
> | D-001 | converted to TBD | REQ-07-01-011 remains labeled ASSUMPTION and verification requires implementation confirmation of endpoint reuse. |

- **AC-001** — Working roots are validated for path form and access, roots inside the instruction root are rejected, tool and write paths cannot escape the active project root, instruction-root and symlink writes are denied, and enforcement failures fail closed with reviewable evidence.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-07-01 Working Root Validation and Instruction Root Protection

> #### Procedure: DEL-07-01 Working Root Validation and Instruction Root Protection
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-017 — Purpose

> ##### Purpose
>
> Define the operational steps to produce and verify the DEL-07-01 implementation artifacts: root validation tests, path policy helpers, and instruction-root protection fixtures.
>
> This procedure may be used by the implementer or reviewer to check that working-root validity, root separation, path containment, and instruction-root write protection are represented in code and tests.
>

### CLM-018 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status | Source |
> |---|---|---|
> | Accepted deliverable scope for DEL-07-01. | Available in `_CONTEXT.md` and decomposition. | `_CONTEXT.md`; decomposition `DEL-07-01` row |
> | Current lifecycle state permits P3 enrichment. | `INITIALIZED`; Phase 2.5 is `P3_ONLY` and preserves `_STATUS.md` under `NO_STATUS_TOUCH`. | `_STATUS.md`; `_SEMANTIC_LENSING.md` |
> | Authoritative source corpus is accessible. | Accessible; `docs/PRD.md` has MATCH status. | `_REFERENCES.md` — reconciled under D-APP-38 |
> | Declared upstream dependencies. | TBD - no accepted dependency edges extracted yet. | `_DEPENDENCIES.md` |
> | Code module locations for implementation. | TBD. | Source-grounding gap |
>

### CLM-019 — Steps

> ##### Steps
>
> 1. Confirm source state.
>    - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>
> 2. Identify the active instruction root.
>    - Resolve the instruction root from packaged resources or `CHIRALITY_INSTRUCTION_ROOT` during development.
>    - Confirm required instruction-root assets are treated as release-managed resources.
>    - Source: `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1.
>
> 3. Validate candidate working roots before use.
>    - Reject non-absolute paths.
>    - Reject missing paths.
>    - Reject non-directory paths.
>    - Reject paths without app read/write access.
>    - Reject paths inside the active instruction root.
>    - Source: `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2.
>
> 4. Normalize and bind the accepted project root.
>    - Store the accepted root as the active `projectRoot` for file tree, scope scan, chat session, scaffold, and contract APIs.
>    - ASSUMPTION: downstream API reuse should consume the same normalized root object or equivalent canonical string.
>    - Source: `docs/PRD.md` Section 7.1.
>
> 5. Implement path containment checks for tool and write paths.
>    - Resolve project-relative and absolute paths.
>    - Deny paths outside the active project root.
>    - Deny traversal or normalization results that escape the root.
>    - Source: `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050.
>
> 6. Enforce instruction-root write protection.
>    - Deny ordinary writes under the active instruction root.
>    - Apply the denial even when SDK or developer-local modes would otherwise permit execution.
>    - Source: `docs/CONTRACT.md` K-ROOT-2; `docs/PRD.md` FR-051; `docs/TYPES.md` Section 8.2.
>
> 7. Apply required hook behavior.
>    - Ensure PreToolUse or equivalent Chirality hooks enforce path containment, instruction-root protection, symlink write rejection, and provenance policy before governed writes.
>    - Ensure hook failures fail closed.
>    - Source: `docs/SPEC.md` Section 15.2; `docs/CONTRACT.md` K-HOOK-1.
>
> 8. Reject symlink writes in the initial policy.
>    - Add fixtures for symlink write targets.
>    - Deny unless a future governed amendment and tests explicitly authorize a narrower policy.
>    - Source: `docs/CONTRACT.md` K-PATH-3.
>
> 9. Build the test matrix.
>    - Include valid working root.
>    - Include relative, missing, non-directory, unreadable, and unwritable working-root cases.
>    - Include working root inside instruction root.
>    - Include absolute outside-project write path.
>    - Include traversal escape path.
>    - Include instruction-root write attempt.
>    - Include symlink write attempt.
>    - Source: `docs/PRD.md` FR-003, FR-050, FR-051, FR-095, FR-097.
>
> 10. Record verification evidence.
>     - Store test output or summaries where the project test convention requires.
>     - Record final test command names and evidence locations when implementation identifies them; until then they remain TBD.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>     - Preserve source citations and any unresolved `TBD` items for later semantic/dependency passes.
>

### CLM-020 — Verification

> ##### Verification
>
> | Check | Pass Condition | Records |
> |---|---|---|
> | Root validation | Invalid roots are rejected with typed or inspectable errors; valid absolute readable/writable directory is accepted. | Root validation test output. |
> | Root separation | Working roots inside instruction root are rejected. | Instruction-root containment fixture output. |
> | Path containment | Writes/tool paths outside active project root are denied after normalization. | Path helper test output. |
> | Instruction-root protection | Writes beneath instruction root are denied across ordinary execution modes. | Hook or policy fixture output. |
> | Symlink write policy | Symlink writes are denied under the initial policy. | Symlink fixture output. |
> | Fail-closed hooks | Hook failure denies governed action and records triage. | Hook failure test output. |
> | PRD hash warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Review note or run record. — reconciled under D-APP-38 |
> | Fixture evidence completeness | Relative, missing, non-directory, unreadable, unwritable, instruction-root-contained, outside-root, traversal, instruction-root write, and symlink cases have output or summary records. | Test output, fixture list, or coverage checklist. |
>

### CLM-021 — Records

> ##### Records
>
> Expected records and artifacts:
>
> - Root validation tests.
> - Path policy helper implementation and tests.
> - Instruction-root protection fixtures.
> - Symlink write rejection fixtures.
> - Hook failure or policy denial evidence.
> - Documentation of `docs/PRD.md` hash warning.
>
> Records still TBD:
>
> - Final implementation file paths.
> - Final test command names.
> - Final evidence record locations for root validation, path policy, instruction-root protection, hook failure, symlink fixtures, and PRD source-state review.
> - Responsible party.
>

### CLM-022 — Pass 3 Semantic Lensing Notes

> ##### Pass 3 Semantic Lensing Notes
>
> | ItemID | Procedure Disposition | Evidence |
> |---|---|---|
> | B-001 | converted to TBD | Step 10 and Verification require concrete fixture output or summaries; final evidence is not invented before tests exist. |
> | D-001 | converted to TBD | Verification requires API test output for `/api/working-root/validate` and downstream normalized-root reuse; implementation confirmation is still pending. |
> | X-001 | converted to TBD | `Records still TBD` now names final test command names and evidence locations for all fixture families. |
> | E-001 | already covered | Step 8 and Verification preserve initial symlink rejection and require future amendment/test evidence before relaxation. |
> | E-002 | incorporated | Step 10, Verification, and Records require preservation of the PRD hash status: MATCH status in review evidence. — reconciled under D-APP-38 |

- **VER-001** — Run the source-defined root-validation, instruction-root containment, path-policy, symlink, hook-denial, API, and fixture-completeness tests and review their evidence against the source requirements.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-07-01 Working Root Validation and Instruction Root Protection

> #### Guidance: DEL-07-01 Working Root Validation and Instruction Root Protection
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-024 — Purpose

> ##### Purpose
>
> DEL-07-01 exists to make the filesystem boundary trustworthy before agents, tools, MCP wrappers, hooks, or SDK-mediated actions operate on project files. It protects two project-critical distinctions:
>
> - The instruction root is release-managed and read-only during ordinary project execution.
> - The working root is the mutable project filesystem where project truth, deliverables, sessions, and tool artifacts live.
>
> Sources: `_CONTEXT.md` `Deliverable Scope`; `docs/DIRECTIVE.md` Sections 2.7-2.9; `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3.
>

### CLM-025 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Validate before use | Treat working-root validation as a gate before file tree, scan, chat session, scaffold, and contract APIs consume the root. | `docs/PRD.md` Section 7.1 |
> | Deny beats allow | A path-containment or instruction-root denial must override permissive SDK modes, user prompts, persona text, or tool availability. | `docs/PRD.md` Section 3; `docs/CONTRACT.md` K-PERM-1 |
> | Code owns the boundary | Prompts may explain safety posture, but enforcement belongs in runtime code, path helpers, hooks, and policy checks. | `docs/DIRECTIVE.md` Section 2.9; `docs/PRD.md` Section 3 |
> | Separate read policy from write policy | Instruction-root reads may be governed by explicit policy, but ordinary writes under the instruction root are blocked. | `docs/PRD.md` FR-051; `docs/SPEC.md` Section 1.1 |
> | Use project-root containment consistently | Tool and write paths should pass through one normalized containment model rather than ad hoc string checks. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |
> | Fail closed | Hook failures in enforcement paths should deny the action and record triage rather than continue silently. | `docs/CONTRACT.md` K-HOOK-1; `docs/PRD.md` FR-095 |
>

### CLM-026 — Considerations

> ##### Considerations
>
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - The decomposition assigns SOW-002 and SOW-027 to DEL-07-01. SOW-002 covers working-root selection and validation; SOW-027 covers path containment and instruction-root protection.
> - `DEL-06-04` also references path hooks for write/edit execution. ASSUMPTION: DEL-07-01 should define reusable root/path policy expectations and tests, while DEL-06-04 applies them in the broader write/edit surface. This is an inferred coordination note from the decomposition, not an accepted dependency edge.
> - `_DEPENDENCIES.md` currently has no accepted upstream or downstream edges. Do not treat neighboring deliverables as formal dependencies until dependency extraction accepts them.
> - The relationship to `DEL-06-04` remains a coordination note, not an accepted dependency edge, until the dependency register is updated or a human ruling says otherwise.
> - The instruction root may be supplied through `CHIRALITY_INSTRUCTION_ROOT` during development and packaged under app resources in builds. Tests should cover both source-tree and packaged-root resolution if implementation supports both paths.
> - Initial symlink write rejection is explicit. Any future relaxation requires a governed amendment and tests.
>

### CLM-027 — Trade-offs

> ##### Trade-offs
>
> | Choice | Benefit | Risk or Cost | Preferred Posture |
> |---|---|---|---|
> | Central path policy helper | Consistent containment behavior across APIs, hooks, and tools. | Requires careful normalization and test coverage. | Prefer central helper with fixture coverage. |
> | Enforcement in hooks and wrappers | Catches SDK built-ins and MCP/tool actions at runtime. | Hook failure paths must be tested and observable. | Required for reliance-boundary confidence. |
> | Strict instruction-root write block | Protects release-managed governance assets from ordinary project execution. | Release/governance updates need a separate controlled pathway. | Required by CONTRACT and SPEC. |
> | Reject symlink writes initially | Reduces path escape risk. | Blocks some advanced local workflows. | Required until governed relaxation exists. |
> | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Allows Phase 2.2 drafting to proceed per brief. | Requirement rows may need revalidation when source state is resolved. | Record warning and cite source locations. — reconciled under D-APP-38 |
>

### CLM-028 — Examples

> ##### Examples
>
> | Scenario | Expected Result | Source |
> |---|---|---|
> | User selects `../project` or another relative path as working root. | Reject as invalid because relative paths are not accepted. | `docs/PRD.md` Section 7.1 |
> | User selects a missing path or a file path. | Reject because the working root must exist and be a directory. | `docs/SPEC.md` Section 1.2 |
> | User selects a directory nested inside the instruction root. | Reject because the working root must not be inside instruction root. | `docs/PRD.md` Section 7.1; `docs/CONTRACT.md` K-ROOT-1 |
> | Tool attempts to write outside active project root using an absolute path. | Deny through path containment. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |
> | Tool attempts to write under instruction root while `bypass` is active in developer-local mode. | Deny because Chirality denies still apply. | `docs/TYPES.md` Section 8.2; `docs/PRD.md` permission mapping table |
> | Tool attempts to write through a symlink target. | Deny under initial symlink write policy. | `docs/CONTRACT.md` K-PATH-3; `docs/SPEC.md` Section 15.2 |
>

### CLM-029 — Source-State Warnings

> ##### Source-State Warnings
>
> | Warning ID | Source | Warning | Impacted Sections | Human Ruling |
> |---|---|---|---|---|
> | WARN-07-01-001 | `_REFERENCES.md` REF-006 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Datasheet, Specification, Guidance, Procedure citations to `docs/PRD.md` | TBD — reconciled under D-APP-38 |
>
> No direct source conflict was found among the accessible slices read for this draft.
>

### CLM-030 — Human Rulings Needed

> ##### Human Rulings Needed
>
> | ItemID | Ruling Needed | Current Posture |
> |---|---|---|
> | C-001 | Accept, correct, replace, or explicitly bypass the `docs/PRD.md` REF-006 hash status: MATCH before PRD-dependent rows are treated as stable closure evidence. | Source-state warning preserved; no human ruling invented. — reconciled under D-APP-38 |
> | X-002 | Decide whether `DEL-06-04` remains only a coordination note or becomes an accepted dependency edge for write/edit hook enforcement. | No dependency edge accepted in `_DEPENDENCIES.md`; guidance keeps the relationship non-authoritative. |
> | E-001 | If future symlink-write relaxation is proposed, identify the amendment reference and fixture evidence required for acceptance. | Initial symlink rejection remains required. |
>

### CLM-031 — Pass 3 Semantic Lensing Notes

> ##### Pass 3 Semantic Lensing Notes
>
> | ItemID | Guidance Disposition | Evidence |
> |---|---|---|
> | C-001 | surfaced as human ruling | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | X-002 | surfaced as human ruling | `Considerations` and `Human Rulings Needed` state that `DEL-06-04` is not an accepted dependency edge unless later accepted. |
> | E-001 | already covered | `Considerations`, `Trade-offs`, `Examples`, and `Human Rulings Needed` keep symlink writes rejected until governed amendment and tests exist. |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-002 SOW-027 OBJ-006 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
