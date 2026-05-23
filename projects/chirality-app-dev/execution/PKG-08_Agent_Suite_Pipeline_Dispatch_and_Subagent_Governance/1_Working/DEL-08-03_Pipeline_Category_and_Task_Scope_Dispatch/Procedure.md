# Procedure: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Purpose

Define an operational procedure for producing and verifying the DEL-08-03 implementation artifacts: pipeline selector tests, knowledge-type discovery behavior, and disabled option handling.

## Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Accepted decomposition entry for DEL-08-03 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Deliverable metadata files | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, `_STATUS.md` present |
| Authoritative vocabulary | `docs/TYPES.md` Section 4.4 |
| Product requirements | `docs/PRD.md` Section 8.2; PRD hash mismatch recorded as source warning |
| Workspace scope API contract | `docs/SPEC.md` Section 17.2 |
| Declared upstream dependencies | TBD - no accepted dependency edges have been extracted yet |
| Declared downstream dependencies | TBD - no accepted dependency edges have been extracted yet |

## Steps

1. Confirm the implementation location for the PIPELINE category and TASK scope selector UI.
   - If no existing location is confirmed, record the path as TBD rather than inventing it.

2. Map canonical vocabulary into UI/state constants.
   - Use `PipelineCategory` values for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*` as the operative taxonomy.
   - Use `TaskScopeMode` values `DELIVERABLES` and `KNOWLEDGE_TYPES`.
   - Use `KnowledgeTypeOption` labels for supported bucket discovery where exposed.
   - Use the disabled-option concept for visible unsupported variants.

3. Implement or verify PIPELINE category controls.
   - Confirm `DECOMP`, `PREP`, `TASK`, and `AUDIT` are visible category controls.
   - Confirm each category has documented options.
   - Confirm unsupported options are disabled and cannot start execution.

4. Implement or verify TASK split selector behavior.
   - Confirm task agent selection and scope selection are separate.
   - Confirm scope mode supports deliverables and knowledge types.
   - Confirm knowledge-type mode requires a selected target deliverable.

5. Implement or verify dynamic scope discovery.
   - Use the working-root scope surface to scan deliverables and knowledge types.
   - Detect document-kit buckets: `Datasheet`, `Specification`, `Guidance`, and `Procedure`.
   - If metadata buckets are exposed, align them with the `KnowledgeTypeOption` vocabulary.

6. Implement or verify invalid-selection reset behavior.
   - Clear selected deliverable when the active root changes and the deliverable is absent.
   - Clear selected knowledge target when its deliverable is absent.
   - Clear selected knowledge target when the marker is disabled or stale.

7. Verify governance boundary behavior.
   - Confirm selector state does not bypass Type 2 task-agent governance.
   - Confirm any actual Type 2 execution path still depends on the relevant sealed-context and approval checks.

8. Write or update tests.
   - Cover pipeline category rendering and category option lists.
   - Cover disabled option visibility and non-interactivity.
   - Cover TASK selector split and required target deliverable behavior.
   - Cover knowledge-type discovery for document-kit files.
   - Cover stale-selection reset cases.

## Verification

| Check | Expected Result |
|---|---|
| Category selector test | `DECOMP`, `PREP`, `TASK`, and `AUDIT` are available as PIPELINE category controls. |
| Disabled option test | Unsupported variants are visible but cannot be selected for execution. |
| TASK scope selector test | Task agent and scope controls are independently represented. |
| Knowledge-type target test | Knowledge-type mode requires a selected deliverable. |
| Knowledge bucket discovery test | Document kit files are detected as first-class knowledge buckets. |
| Stale selection reset test | Root changes and stale or disabled targets clear invalid UI state. |
| Governance boundary review | UI dispatch does not grant runtime authority beyond governed execution checks. |

## Records

Maintain or produce these records during implementation:

- Pipeline selector tests.
- Knowledge-type discovery tests or fixtures.
- Disabled option handling tests.
- Any implementation note identifying confirmed UI component and test file paths.
- Any human ruling on the PRD hash mismatch before closure.
