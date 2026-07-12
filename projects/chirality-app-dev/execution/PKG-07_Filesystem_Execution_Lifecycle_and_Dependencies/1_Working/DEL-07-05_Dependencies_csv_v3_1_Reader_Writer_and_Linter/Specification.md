# Specification: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Scope

This deliverable covers backend support to read, validate, and write deliverable-local `Dependencies.csv` v3.1 registers while preserving schema, provenance, row lifecycle, and warnings.

In scope:

- Parse `Dependencies.csv` rows that follow the v3.1 core schema.
- Validate required headers, enum values, host identity rules, target resolution rules, provenance requirements, and row lifecycle fields.
- Serialize append/update writes without deleting retired rows.
- Normalize legacy missing `RegisterSchemaVersion` to `v3.1` on write.
- Preserve optional extension columns without treating them as breaking schema changes.
- Expose read/write behavior through the product dependency contract surface, including `/api/working-root/deliverable/dependencies` and Chirality MCP dependency tools.
- Return structured warnings for legacy, invalid, missing, or unresolved data where the source permits warning behavior.

Out of scope:

- Central dependency graph generation, project-level graph visualization, deliverable locks, staleness propagation tooling, or unified pipeline run records unless a governed amendment reopens that scope.
- Human acceptance of dependency truth; tools support parsing, validation, and warning surfaces, while accepted project truth remains in reviewed files.
- Replacing deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` with an external database.

Sources: `_CONTEXT.md` (Deliverable Scope); `docs/SPEC.md` Sections 5, 6, 14.2; `docs/PRD.md` Sections 8.9, 10.9, 17.2; `docs/PLAN.md` Section 9.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-DEL-07-05-001 | The reader MUST recognize `Dependencies.csv` as a deliverable-local structured dependency register using schema version `v3.1`. | `docs/SPEC.md` Sections 3.1 and 6 |
| REQ-DEL-07-05-002 | Every written row MUST include `RegisterSchemaVersion` set to `v3.1`; legacy missing `RegisterSchemaVersion` values MUST be normalized to `v3.1` on write. | `docs/SPEC.md` Sections 6 and 6.2 |
| REQ-DEL-07-05-003 | The linter MUST validate the v3.1 core columns, including requiredness, enum fields, host identity, provenance fields, origin fields, date fields, and lifecycle status fields. | `docs/SPEC.md` Section 6.1; `docs/PRD.md` Section 8.9 |
| REQ-DEL-07-05-004 | `DependencyID` MUST be unique within a deliverable register. | `docs/SPEC.md` Section 6.2 |
| REQ-DEL-07-05-005 | `FromDeliverableID` MUST match the host deliverable ID. | `docs/SPEC.md` Section 6.2 |
| REQ-DEL-07-05-006 | `ANCHOR` rows MUST use `IMPLEMENTS_NODE` or `TRACES_TO_REQUIREMENT` and `DependencyType=OTHER`. | `docs/SPEC.md` Section 6.2 |
| REQ-DEL-07-05-007 | `EXECUTION` rows MUST use `AnchorType=NOT_APPLICABLE`. | `docs/SPEC.md` Section 6.2 |
| REQ-DEL-07-05-008 | Rows MUST be retired, not deleted. | `docs/SPEC.md` Section 6.2; `docs/PRD.md` Section 10.9 |
| REQ-DEL-07-05-009 | Active extracted dependency rows MUST cite `EvidenceFile` plus `SourceRef`, or explicit `location TBD`. | `docs/CONTRACT.md` Section 1.7; `docs/PRD.md` Section 8.9 |
| REQ-DEL-07-05-010 | Dependency references to deliverables MUST resolve to existing stable deliverable IDs; unresolvable targets MUST use `TargetType=UNKNOWN`. | `docs/CONTRACT.md` Section 1.7; `docs/TYPES.md` Section 6.5 |
| REQ-DEL-07-05-011 | Unknown values MUST remain `TBD` rather than being guessed. | `docs/CONTRACT.md` Section 1.7; `docs/DIRECTIVE.md` Section 2.5 |
| REQ-DEL-07-05-012 | The writer MUST preserve host deliverable consistency, schema version, row lifecycle behavior, and warnings for legacy or invalid data. | `docs/PRD.md` Section 8.9 |
| REQ-DEL-07-05-013 | The dependency API surface MUST support GET/PUT for `Dependencies.csv` snapshot rows at `/api/working-root/deliverable/dependencies`. | `docs/PRD.md` Section 17.2 |
| REQ-DEL-07-05-014 | Chirality MCP dependency tools MUST pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Section 14.2 |
| REQ-DEL-07-05-015 | Filesystem write behavior MUST respect project-root containment, instruction-root protection, symlink write rejection, and provenance hook policy. | `docs/SPEC.md` Sections 15.1 and 15.2; `docs/CONTRACT.md` Section 1.6 |
| REQ-DEL-07-05-016 | Extension columns MAY be present and MUST be non-breaking to the schema reader/writer. | `docs/SPEC.md` Section 6.1 |
| REQ-DEL-07-05-017 | Unknown option keys in runtime/tool options MUST be ignored with warnings rather than silently mutating behavior. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-024 |
| REQ-DEL-07-05-018 | Dependency linter behavior remains in scope; retired broader hardening features MUST NOT be reintroduced by this deliverable. | `docs/PLAN.md` Section 9 |

## Standards

| Standard or Contract | Applicability | Source |
|---|---|---|
| `Dependencies.csv` v3.1 schema | Governs register headers, requiredness, row rules, and extension column tolerance. | `docs/SPEC.md` Section 6 |
| Dependency vocabulary | Governs dependency classes, anchor types, directions, dependency types, target types, provenance/status terms. | `docs/TYPES.md` Section 6 |
| Filesystem execution and dependency invariants | Governs dependency authority, target resolution, provenance, invention control, and conflict surfacing. | `docs/CONTRACT.md` Section 1.7 |
| Lifecycle and dependency contract requirements | Governs parsing, validation, provenance preservation, and lifecycle behavior acceptance criteria. | `docs/PRD.md` Section 8.9 |
| Working-root tool policy | Governs path containment, instruction-root write blocking, symlink rejection, hooks, and provenance append. | `docs/SPEC.md` Sections 14 and 15 |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| REQ-DEL-07-05-001 through REQ-DEL-07-05-003 | Unit tests using valid, missing-header, malformed-header, and legacy-missing-version fixtures. |
| REQ-DEL-07-05-004 through REQ-DEL-07-05-007 | Linter fixtures for duplicate IDs, host mismatch, invalid anchor rows, and invalid execution rows. |
| REQ-DEL-07-05-008 and REQ-DEL-07-05-012 | Writer tests showing retired rows are retained and updates preserve lifecycle fields. |
| REQ-DEL-07-05-009 through REQ-DEL-07-05-011 | Provenance and unknown-target tests for active extracted rows, `location TBD`, and `TargetType=UNKNOWN`. |
| REQ-DEL-07-05-013 | API tests for GET/PUT behavior at `/api/working-root/deliverable/dependencies`. |
| REQ-DEL-07-05-014 and REQ-DEL-07-05-015 | MCP/tool integration tests verifying permission, hook, containment, and provenance behavior. |
| REQ-DEL-07-05-016 and REQ-DEL-07-05-017 | Compatibility tests for extension columns and unknown option keys producing warnings. |
| REQ-DEL-07-05-018 | Scope review test or checklist confirming no project-level graph generator, deliverable lock, staleness propagation, or unified pipeline run-record feature is introduced. |

ASSUMPTION: The exact module names, API handler names, and fixture paths are TBD until implementation ownership chooses the local code structure.

### Pass 3 Acceptance Evidence Mapping

| ItemID | Required evidence | Current disposition |
|---|---|---|
| C-001 | A stable structured warning taxonomy for parse, schema, enum, identity, provenance, target-resolution, legacy-normalization, permission, hook, containment, and source-state findings. | Converted to TBD because the sources require warnings but do not name final warning codes or categories. |
| D-001 | Implementation path register naming parser/writer module, linter module, API handler, MCP wrapper, payload type definitions, fixtures, and tests. | Converted to TBD path slots pending local code ownership. |
| X-001 | API GET/PUT payload tests, MCP dependency read/write tests, write-hook containment tests, instruction-root rejection tests, symlink-write rejection tests, provenance/event-hook evidence, and PRD hash-warning review evidence. | Converted to required acceptance evidence with final artifact paths TBD. |

Source rereads: `docs/SPEC.md` Sections 6, 14.2, 14.3, 15.1, 15.2, and 17.2; `docs/CONTRACT.md` Sections 1.6 and 1.7; `docs/PRD.md` Sections 8.9, 10.9, 17.2, and implementation targets; `docs/TYPES.md` Section 6.

## Documentation

Required artifacts for this deliverable:

- Dependency parser/writer.
- Linter tests.
- Provenance fixtures.

Recommended supporting documentation:

- Fixture README or inline test comments explaining valid v3.1 rows, legacy normalization cases, invalid enum cases, unresolved target cases, and retired-row preservation.
- API/MCP contract notes that point back to `docs/SPEC.md` Section 6 and `docs/PRD.md` Section 8.9.

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-133 adopts the stricter live rule: every ACTIVE dependency row requires both `EvidenceFile` and `SourceRef`.

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
