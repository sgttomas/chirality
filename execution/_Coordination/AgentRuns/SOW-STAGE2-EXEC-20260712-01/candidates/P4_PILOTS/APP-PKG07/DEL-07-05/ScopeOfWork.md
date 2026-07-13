---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-07-05
package_id: PKG-07
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@2770fda4c63c98ee9f18cffbafd14c9aa59f497f
project_scope_refs: [SOW-029]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-07-05

## Purpose and Objective Traceability

This candidate defines `DEL-07-05` in service of project scope [SOW-029] and package objectives [OBJ-006].

- **OUT-001** — A Dependencies.csv v3.1 reader, writer, and linter with API/MCP integration, schema and lifecycle preservation, provenance, compatibility warnings, and fixtures.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-001"} -->
#### Datasheet: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":22,"line_start":5,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-07-05 |
| DeliverableName | Dependencies.csv v3.1 Reader, Writer, and Linter |
| PackageID | PKG-07 |
| PackageName | Filesystem Execution, Lifecycle, and Dependencies |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| Scope Item | SOW-029 - Dependencies CSV v3.1 |
| Supported Objective | OBJ-006 |

Sources: `_CONTEXT.md` (Identity, Package Scope, Deliverable Scope, Traceability); `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (PKG-07 deliverable table; Scope Ledger SOW-029).

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":36,"line_start":23,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | `Dependencies.csv` v3.1 contract support | `docs/SPEC.md` Section 6; `docs/PRD.md` Section 8.9 |
| Required register schema version | `v3.1` in every row | `docs/SPEC.md` Section 6 |
| Core schema width | 29 core columns, with extension columns allowed | `docs/SPEC.md` Section 6.1 |
| Reader behavior | Read and validate `Dependencies.csv`; expose required headers, enum values, identity rules, and warnings through contract APIs | `docs/SPEC.md` Section 14.2; `docs/PRD.md` Section 8.9 |
| Writer behavior | Append/update rows while preserving v3.1 schema, host deliverable consistency, row lifecycle, and warnings for legacy/invalid data | `docs/SPEC.md` Sections 6.2 and 14.2; `docs/PRD.md` Section 8.9 |
| Linter behavior | Validate schema, enum values, identity rules, provenance, and resolvable deliverable references; report warnings without fabricating values | `docs/CONTRACT.md` Section 1.7; `docs/PRD.md` Section 8.9 |
| API surface | `/api/working-root/deliverable/dependencies` supports GET/PUT for `Dependencies.csv` snapshot rows | `docs/PRD.md` Section 17.2 |
| MCP surface | `mcp__chirality__deps_read` and `mcp__chirality__deps_write` | `docs/SPEC.md` Section 14.2 |
| Source warning | `docs/PRD.md` is locally accessible but has a recorded hash status: MATCH in `_REFERENCES.md`; use as warned source, not as silent accepted hash truth | `_REFERENCES.md` (Authoritative Source Corpus) — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":47,"line_start":37,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root containment | Dependency tools are subject to project-root containment and write-hook policy | `docs/SPEC.md` Sections 14.3 and 15.2; `docs/CONTRACT.md` Section 1.6 |
| Instruction-root protection | Runtime writes to the instruction root are blocked | `docs/SPEC.md` Section 15.2; `docs/PRD.md` Section 8.8 |
| Dependency authority | Deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` are authoritative for dependencies; aggregation is on demand | `docs/CONTRACT.md` Section 1.7; `docs/DIRECTIVE.md` Section 5 |
| Provenance requirement | Active extracted rows require `EvidenceFile` plus `SourceRef`, or explicit `location TBD` | `docs/CONTRACT.md` Section 1.7; `docs/PRD.md` Section 8.9 |
| Unknown handling | Unknowns remain `TBD`; unresolvable targets use `TargetType=UNKNOWN` | `docs/CONTRACT.md` Section 1.7; `docs/TYPES.md` Section 6.5 |
| Lifecycle behavior | Rows are retired, not deleted; `FirstSeen`, `LastSeen`, `Status`, and `SatisfactionStatus` track extraction and closure state | `docs/SPEC.md` Section 6.2; `docs/PRD.md` Section 10.9 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":49,"line_start":48,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-005"} -->
##### Construction

<!-- sow-source-end -->

### CLM-006 — Core Schema Columns

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":77,"line_start":50,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-006"} -->
###### Core Schema Columns

The reader, writer, and linter must preserve these core columns from `docs/SPEC.md` Section 6.1:

| # | Column | Requiredness | Notes |
|---:|---|---|---|
| 1 | RegisterSchemaVersion | MUST | Must be `v3.1`; legacy missing values normalize to `v3.1` on write. |
| 2 | DependencyID | MUST | Unique within deliverable register. |
| 3 | FromPackageID | MUST | Host package ID. |
| 4 | FromDeliverableID | MUST | Must match the host deliverable ID. |
| 5 | FromDeliverableName | MUST | Host deliverable name. |
| 6 | DependencyClass | MUST | `ANCHOR` or `EXECUTION`. |
| 7 | AnchorType | MUST | See `docs/TYPES.md` Section 6.2. |
| 8 | Direction | MUST | `UPSTREAM` or `DOWNSTREAM`. |
| 9 | DependencyType | MUST | See `docs/TYPES.md` Section 6.4. |
| 10 | TargetType | MUST | See `docs/TYPES.md` Section 6.5. |
| 11-15 | Target fields | optional/SHOULD as specified | Package, deliverable, reference, name, and location. |
| 16 | Statement | SHOULD | Dependency statement. |
| 17-19 | Evidence fields | MUST*/SHOULD | `EvidenceFile`, `SourceRef`, and short `EvidenceQuote`. |
| 20 | Explicitness | SHOULD | `EXPLICIT` or `IMPLICIT`. |
| 21-22 | Maturity fields | optional | Required/proposed maturity. |
| 23 | SatisfactionStatus | SHOULD | See `docs/TYPES.md` Section 6.6. |
| 24 | Confidence | SHOULD | `HIGH`, `MEDIUM`, or `LOW`. |
| 25 | Origin | MUST | `DECLARED` or `EXTRACTED`. |
| 26-27 | FirstSeen, LastSeen | MUST | ISO dates. |
| 28 | Status | MUST | `ACTIVE` or `RETIRED`. |
| 29 | Notes | optional | Notes and epistemic labels. |

<!-- sow-source-end -->

### CLM-007 — Enum Vocabulary

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":92,"line_start":78,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-007"} -->
###### Enum Vocabulary

| Field | Allowed Values | Source |
|---|---|---|
| DependencyClass | `ANCHOR`, `EXECUTION` | `docs/TYPES.md` Section 6.1 |
| AnchorType | `IMPLEMENTS_NODE`, `TRACES_TO_REQUIREMENT`, `NOT_APPLICABLE` | `docs/TYPES.md` Section 6.2 |
| Direction | `UPSTREAM`, `DOWNSTREAM`; legacy `INBOUND` normalizes to `UPSTREAM`, legacy `OUTBOUND` normalizes to `DOWNSTREAM` | `docs/TYPES.md` Section 6.3 |
| DependencyType | `PREREQUISITE`, `INTERFACE`, `HANDOVER`, `CONSTRAINT`, `ENABLES`, `OTHER` | `docs/TYPES.md` Section 6.4 |
| TargetType | `DELIVERABLE`, `PACKAGE`, `WBS_NODE`, `REQUIREMENT`, `DOCUMENT`, `EQUIPMENT`, `EXTERNAL`, `UNKNOWN` | `docs/TYPES.md` Section 6.5 |
| Explicitness | `EXPLICIT`, `IMPLICIT` | `docs/TYPES.md` Section 6.6 |
| SatisfactionStatus | `TBD`, `PENDING`, `IN_PROGRESS`, `SATISFIED`, `WAIVED`, `NOT_APPLICABLE` | `docs/TYPES.md` Section 6.6 |
| Confidence | `HIGH`, `MEDIUM`, `LOW` | `docs/TYPES.md` Section 6.6 |
| Origin | `DECLARED`, `EXTRACTED` | `docs/TYPES.md` Section 6.6 |
| Status | `ACTIVE`, `RETIRED` | `docs/TYPES.md` Section 6.6 |

<!-- sow-source-end -->

### CLM-008 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":102,"line_start":93,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-008"} -->
##### References

- `docs/SPEC.md` Sections 3, 5, 6, 14.2, 14.3, and 15.2.
- `docs/TYPES.md` Section 6.
- `docs/CONTRACT.md` Section 1.7.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- `docs/DIRECTIVE.md` Sections 2.5 and 5.
- `docs/PLAN.md` R4 target slice and Optional/Retired Scope Status.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-07 deliverable table and Scope Ledger SOW-029.

<!-- sow-source-end -->

### CLM-009 — Pass 3 Semantic Lensing Notes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":112,"line_start":103,"source_sha256":"a7728f8966010a6d528a61886450ee7371822cb75dfc4104dea43fc067fdd145","target_id":"CLM-009"} -->
##### Pass 3 Semantic Lensing Notes

| ItemID | Datasheet disposition |
|---|---|
| C-001 | Converted to a named TBD: the warning output must remain structured and deterministic, but the exact warning code/category taxonomy is not selected by the accessible sources. |
| F-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| D-001 | Converted to implementation slots: module names, API handler names, fixture paths, payload type names, and test paths remain TBD until local code ownership selects them. |
| X-001 | Converted to acceptance-evidence slots: API/MCP dependency payload evidence and governed write-hook evidence remain required, with final artifact paths TBD. |

Source rereads for these notes: `_SEMANTIC_LENSING.md` current warranted rows; `docs/SPEC.md` Sections 6, 14.2, 14.3, 15.1, 15.2, and 17.2; `docs/CONTRACT.md` Sections 1.6 and 1.7; `docs/PRD.md` Sections 8.9, 10.9, and 17.2; `_REFERENCES.md` Authoritative Source Corpus.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-010 — Specification: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-010"} -->
#### Specification: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-011 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":26,"line_start":5,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-011"} -->
##### Scope

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

<!-- sow-source-end -->

### CLM-012 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":49,"line_start":27,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-012"} -->
##### Requirements

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

<!-- sow-source-end -->

### CLM-013 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":59,"line_start":50,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-013"} -->
##### Standards

| Standard or Contract | Applicability | Source |
|---|---|---|
| `Dependencies.csv` v3.1 schema | Governs register headers, requiredness, row rules, and extension column tolerance. | `docs/SPEC.md` Section 6 |
| Dependency vocabulary | Governs dependency classes, anchor types, directions, dependency types, target types, provenance/status terms. | `docs/TYPES.md` Section 6 |
| Filesystem execution and dependency invariants | Governs dependency authority, target resolution, provenance, invention control, and conflict surfacing. | `docs/CONTRACT.md` Section 1.7 |
| Lifecycle and dependency contract requirements | Governs parsing, validation, provenance preservation, and lifecycle behavior acceptance criteria. | `docs/PRD.md` Section 8.9 |
| Working-root tool policy | Governs path containment, instruction-root write blocking, symlink rejection, hooks, and provenance append. | `docs/SPEC.md` Sections 14 and 15 |

<!-- sow-source-end -->

### CLM-014 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":74,"line_start":60,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-014"} -->
##### Verification

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

<!-- sow-source-end -->

### CLM-015 — Pass 3 Acceptance Evidence Mapping

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":84,"line_start":75,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-015"} -->
###### Pass 3 Acceptance Evidence Mapping

| ItemID | Required evidence | Current disposition |
|---|---|---|
| C-001 | A stable structured warning taxonomy for parse, schema, enum, identity, provenance, target-resolution, legacy-normalization, permission, hook, containment, and source-state findings. | Converted to TBD because the sources require warnings but do not name final warning codes or categories. |
| D-001 | Implementation path register naming parser/writer module, linter module, API handler, MCP wrapper, payload type definitions, fixtures, and tests. | Converted to TBD path slots pending local code ownership. |
| X-001 | API GET/PUT payload tests, MCP dependency read/write tests, write-hook containment tests, instruction-root rejection tests, symlink-write rejection tests, provenance/event-hook evidence, and PRD hash-warning review evidence. | Converted to required acceptance evidence with final artifact paths TBD. |

Source rereads: `docs/SPEC.md` Sections 6, 14.2, 14.3, 15.1, 15.2, and 17.2; `docs/CONTRACT.md` Sections 1.6 and 1.7; `docs/PRD.md` Sections 8.9, 10.9, 17.2, and implementation targets; `docs/TYPES.md` Section 6.

<!-- sow-source-end -->

### CLM-016 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":99,"line_start":85,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-016"} -->
##### Documentation

Required artifacts for this deliverable:

- Dependency parser/writer.
- Linter tests.
- Provenance fixtures.

Recommended supporting documentation:

- Fixture README or inline test comments explaining valid v3.1 rows, legacy normalization cases, invalid enum cases, unresolved target cases, and retired-row preservation.
- API/MCP contract notes that point back to `docs/SPEC.md` Section 6 and `docs/PRD.md` Section 8.9.

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-017 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":104,"line_start":100,"source_sha256":"a52d9a42e9e8921f0bd4af36dce461237c6c8e1cf97f24bd1360fda084833668","target_id":"CLM-017"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-133 adopts the stricter live rule: every ACTIVE dependency row requires both `EvidenceFile` and `SourceRef`.

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
<!-- sow-source-end -->

- **AC-001** — Dependency registers validate v3.1 identity, enums, host, provenance, target, and lifecycle rules; writes preserve retired rows and extension columns, normalize legacy versions with warnings, retain unknowns as TBD, and obey permission, containment, hook, and instruction-root protections.

## Production and Verification Method — Praxeology

### CLM-018 — Procedure: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":4,"line_start":1,"source_sha256":"2bb0df99b6d59c141e99c530c27bd06593607f7ecdece24822f39e65411cc469","target_id":"CLM-018"} -->
#### Procedure: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-019 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":10,"line_start":5,"source_sha256":"2bb0df99b6d59c141e99c530c27bd06593607f7ecdece24822f39e65411cc469","target_id":"CLM-019"} -->
##### Purpose

Define the operating workflow for producing and verifying the DEL-07-05 backend slice: a `Dependencies.csv` v3.1 reader, writer, and linter that preserves schema, provenance, lifecycle behavior, and warnings.

Sources: `_CONTEXT.md` (Deliverable Scope and Anticipated Artifacts); `docs/SPEC.md` Section 6; `docs/PRD.md` Section 8.9.

<!-- sow-source-end -->

### CLM-020 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":21,"line_start":11,"source_sha256":"2bb0df99b6d59c141e99c530c27bd06593607f7ecdece24822f39e65411cc469","target_id":"CLM-020"} -->
##### Prerequisites

| Prerequisite | Status / Note | Source |
|---|---|---|
| Accepted source references are available | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` — reconciled under D-APP-38 |
| v3.1 schema and enum vocabulary are known | Defined in SPEC and TYPES. | `docs/SPEC.md` Section 6; `docs/TYPES.md` Section 6 |
| Dependency authority model is known | Deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` are authoritative; aggregation is on demand. | `docs/CONTRACT.md` Section 1.7 |
| Working-root write policy is known | Governed writes require containment, instruction-root protection, symlink rejection, and hook/provenance behavior. | `docs/SPEC.md` Section 15 |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` has no accepted dependency edges yet. | `_DEPENDENCIES.md` |
| Declared downstream dependencies | TBD - `_DEPENDENCIES.md` has no accepted dependency edges yet. | `_DEPENDENCIES.md` |

<!-- sow-source-end -->

### CLM-021 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":89,"line_start":22,"source_sha256":"2bb0df99b6d59c141e99c530c27bd06593607f7ecdece24822f39e65411cc469","target_id":"CLM-021"} -->
##### Steps

1. Confirm the implementation scope is limited to the `Dependencies.csv` v3.1 reader, writer, linter, contract API/MCP behavior, fixtures, and tests for DEL-07-05.
   - Verification hook: scope review confirms no retired graph-generation, deliverable-lock, staleness, or unified pipeline run-record features are introduced.

2. Define the v3.1 column model from `docs/SPEC.md` Section 6.1.
   - Include all 29 core columns.
   - Mark requiredness and optional/SHOULD fields.
   - Allow non-breaking extension columns.

3. Define enum validation from `docs/TYPES.md` Section 6.
   - Validate `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `Explicitness`, `SatisfactionStatus`, `Confidence`, `Origin`, and `Status`.
   - Normalize only source-authorized legacy forms: legacy `INBOUND` to `UPSTREAM`, legacy `OUTBOUND` to `DOWNSTREAM`, and missing `RegisterSchemaVersion` to `v3.1` on write.

4. Implement reader behavior.
   - Read `Dependencies.csv` from the selected deliverable folder.
   - Return parsed rows plus validation findings.
   - Preserve unknown or unsupported data as warnings or `TBD` rather than inventing values.
   - ASSUMPTION: exact return type names are TBD until local code ownership selects module boundaries.

5. Implement linter behavior.
   - Validate required headers and row requiredness.
   - Check unique `DependencyID` values within the deliverable register.
   - Check `FromDeliverableID` against the host deliverable ID.
   - Check anchor and execution row rules.
   - Check active extracted-row provenance: `EvidenceFile` plus `SourceRef`, or explicit `location TBD`.
   - Check target resolution and use `TargetType=UNKNOWN` for unresolvable deliverable targets.
   - Emit structured warnings for legacy or invalid data where warning behavior is required.

6. Implement writer behavior.
   - Append or update dependency rows.
   - Serialize `RegisterSchemaVersion=v3.1`.
   - Retain retired rows instead of deleting them.
   - Preserve host deliverable consistency, extension columns, provenance fields, and lifecycle fields.
   - Pass through working-root containment, instruction-root protection, symlink rejection, and provenance/event hooks.

7. Connect contract surfaces.
   - Expose read/write behavior through `/api/working-root/deliverable/dependencies` GET/PUT.
   - Expose or integrate `mcp__chirality__deps_read` and `mcp__chirality__deps_write` behind the same permission and hook policy as SDK built-ins.
   - Treat unknown option keys as warnings rather than behavior mutations.

8. Build fixtures.
   - Valid v3.1 register.
   - Missing `RegisterSchemaVersion` legacy case.
   - Duplicate `DependencyID`.
   - Host deliverable mismatch.
   - Invalid enum values.
   - Invalid anchor row.
   - Invalid execution row.
   - Missing active extracted-row provenance.
   - Unresolvable deliverable target.
   - Retired row retained during write.
   - Extension column preservation.

9. Run focused tests.
   - Reader unit tests.
   - Writer unit tests.
   - Linter unit tests.
   - API tests for the dependency endpoint.
   - MCP/tool integration tests where the surface exists.
   - Path/hook/provenance tests for write behavior.

10. Record unresolved implementation choices.
    - Module names: TBD.
    - Warning code taxonomy: TBD.
    - Exact fixture paths: TBD.
    - API payload type names: TBD.

<!-- sow-source-end -->

### CLM-022 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":106,"line_start":90,"source_sha256":"2bb0df99b6d59c141e99c530c27bd06593607f7ecdece24822f39e65411cc469","target_id":"CLM-022"} -->
##### Verification

| Check | Expected Result | Source |
|---|---|---|
| Schema version | Every written row has `RegisterSchemaVersion=v3.1`. | `docs/SPEC.md` Section 6 |
| Header validation | Required core columns are recognized and missing required headers are reported. | `docs/SPEC.md` Section 6.1 |
| Enum validation | Values match `docs/TYPES.md` Section 6; legacy direction values normalize only as specified. | `docs/TYPES.md` Section 6 |
| Host identity | `FromDeliverableID` matches the host deliverable ID. | `docs/SPEC.md` Section 6.2 |
| Dependency identity | `DependencyID` is unique within the deliverable register. | `docs/SPEC.md` Section 6.2 |
| Anchor rows | Anchor rows use allowed anchor types and `DependencyType=OTHER`. | `docs/SPEC.md` Section 6.2 |
| Execution rows | Execution rows use `AnchorType=NOT_APPLICABLE`. | `docs/SPEC.md` Section 6.2 |
| Provenance | Active extracted rows have `EvidenceFile` plus `SourceRef`, or `location TBD`. | `docs/CONTRACT.md` Section 1.7; `docs/PRD.md` Section 8.9 |
| Target resolution | Unresolvable deliverable references use `TargetType=UNKNOWN`. | `docs/CONTRACT.md` Section 1.7; `docs/TYPES.md` Section 6.5 |
| Lifecycle preservation | Rows are retired, not deleted; lifecycle fields persist through writes. | `docs/SPEC.md` Section 6.2; `docs/PRD.md` Section 10.9 |
| Extension columns | Additional columns are preserved as non-breaking. | `docs/SPEC.md` Section 6.1 |
| Scope discipline | No retired graph/staleness/lock/unified pipeline record scope is introduced. | `docs/PLAN.md` Section 9 |

<!-- sow-source-end -->

### CLM-023 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":116,"line_start":107,"source_sha256":"2bb0df99b6d59c141e99c530c27bd06593607f7ecdece24822f39e65411cc469","target_id":"CLM-023"} -->
##### Records

Expected records from implementation:

- Dependency parser/writer source files. Exact paths TBD.
- Linter test suite and fixtures. Exact paths TBD.
- Provenance fixtures showing valid source citation and `location TBD` behavior.
- API/MCP tests or integration evidence for dependency read/write contract surfaces.
- Review note confirming `docs/PRD.md` hash status: MATCH was considered before accepting PRD-derived requirements. (reconciled under D-APP-38).

<!-- sow-source-end -->

### CLM-024 — Pass 3 Worklist Disposition

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":126,"line_start":117,"source_sha256":"2bb0df99b6d59c141e99c530c27bd06593607f7ecdece24822f39e65411cc469","target_id":"CLM-024"} -->
##### Pass 3 Worklist Disposition

| ItemID | Procedure disposition | Required follow-through |
|---|---|---|
| C-001 | Converted to TBD. | Select and document stable warning categories or codes before locking tests for reader, writer, linter, API, and MCP warning output. |
| F-001 | Already surfaced as conflict. | Preserve `_REFERENCES.md` PRD `MATCH` in review evidence or refresh/accept the PRD hash through the appropriate human-governed path. — reconciled under D-APP-38 |
| D-001 | Converted to implementation-location slots. | Record final module names, API handler names, MCP wrapper names, payload type names, fixture paths, and test paths in implementation evidence once selected. |
| X-001 | Converted to acceptance-evidence slots. | Record API/MCP dependency read-write payload evidence and governed write-hook evidence, including containment, instruction-root rejection, symlink-write rejection, provenance/event hooks, extension-column preservation, retired-row retention, and warning behavior. |

Source rereads: `docs/SPEC.md` Sections 6, 14.2, 14.3, 15.1, 15.2, and 17.2; `docs/CONTRACT.md` Sections 1.6 and 1.7; `docs/PRD.md` Sections 8.9 and 10.9 plus implementation targets; `docs/TYPES.md` Section 6; `docs/PLAN.md` Section 9.
<!-- sow-source-end -->

- **VER-001** — Run the source-defined valid, malformed, legacy-version, linter, retirement, provenance, unknown-target, API GET/PUT, MCP, containment, hook, extension-column, warning, and retired-scope tests.

## Governing Values and Decisions — Axiology

### CLM-025 — Guidance: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-025"} -->
#### Guidance: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-026 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":10,"line_start":5,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-026"} -->
##### Purpose

DEL-07-05 exists to make the dependency register contract executable: `Dependencies.csv` rows must be readable, writable, lintable, and warning-producing without weakening Chirality's plain-file, deliverable-local dependency model.

Sources: `_CONTEXT.md` (Deliverable Scope); `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (PKG-07 deliverable table); `docs/DIRECTIVE.md` Section 5.

<!-- sow-source-end -->

### CLM-027 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":22,"line_start":11,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-027"} -->
##### Principles

| Principle | Guidance | Source |
|---|---|---|
| Plain-file truth | Treat `_DEPENDENCIES.md` and `Dependencies.csv` as local, inspectable project state. Avoid hidden app state or external database assumptions. | `docs/DIRECTIVE.md` Section 5; `docs/CONTRACT.md` Section 1.7 |
| Schema preservation | Parse and write the complete v3.1 core schema, and carry extension columns forward without making them breaking changes. | `docs/SPEC.md` Section 6.1 |
| Lifecycle-aware rows | Retire rows instead of deleting them so dependency history remains auditable. | `docs/SPEC.md` Section 6.2; `docs/PRD.md` Section 10.9 |
| Evidence over plausibility | Preserve `EvidenceFile` and `SourceRef`; use `location TBD`, `TBD`, and explicit warnings instead of invented provenance. | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` Section 1.7 |
| Stable identifiers | Use stable package, deliverable, dependency, and target identifiers for identity. Paths are projections and may change. | `docs/CONTRACT.md` K-ID-1 and K-PATH-1 |
| Fail visibly | Invalid enum values, unresolved deliverables, missing provenance, and host identity mismatches should become structured errors or warnings rather than silent mutation. | `docs/PRD.md` Section 8.9; `docs/SPEC.md` Section 14.3 |
| Governed writes | Dependency writes should pass through the same path, permission, hook, redaction, and event logging policy as other governed tool writes. | `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14.2 and 15 |

<!-- sow-source-end -->

### CLM-028 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":32,"line_start":23,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-028"} -->
##### Considerations

- Reader design should separate syntactic CSV parsing from semantic validation. This keeps parse failures, schema warnings, enum errors, identity errors, and provenance warnings distinguishable.
- Writer design should be conservative: preserve existing column order where possible, preserve extension columns, normalize only source-authorized legacy forms, and retain retired rows.
- Linter output should be deterministic and stable enough for tests. ASSUMPTION: warning codes or categories should be stable once selected, but the exact code vocabulary is TBD.
- Target resolution should use stable deliverable IDs when available. If the target cannot be confidently resolved, the row should use `TargetType=UNKNOWN` rather than inventing a target.
- Provenance validation should distinguish active extracted rows from other row origins/statuses because the explicit provenance invariant applies to active extracted dependency rows.
- The `docs/PRD.md` source is useful but flagged `MATCH` in `_REFERENCES.md`; revalidate PRD-derived acceptance language during human review. (reconciled under D-APP-38).
- Do not use this deliverable to reintroduce project-level dependency graph generation, deliverable locks, staleness propagation, or unified pipeline run records. `docs/PLAN.md` Section 9 identifies those as retired without amendment.

<!-- sow-source-end -->

### CLM-029 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":41,"line_start":33,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-029"} -->
##### Trade-offs

| Trade-off | Preferred Direction | Rationale |
|---|---|---|
| Strict failure vs warning | Fail hard on structural conditions that make the file unreadable or unsafe to write; warn for legacy/invalid data where the contract calls for warnings. | PRD FR-055 through FR-057 require validation and warnings; SPEC requires schema and row rules. |
| Normalization vs source preservation | Normalize only source-authorized legacy forms, such as missing `RegisterSchemaVersion` on write. Preserve other data and surface warnings. | `docs/SPEC.md` Section 6.2 authorizes version normalization; other normalizations need evidence. |
| Rich graph behavior vs scoped register tooling | Keep this slice focused on reader/writer/linter behavior. | `docs/PLAN.md` Section 9 keeps dependency linter behavior in scope while retiring broader graph/hardening scope. |
| API convenience vs file authority | APIs may expose snapshots and write operations, but file contents remain the authoritative project substrate. | `docs/DIRECTIVE.md` Section 5; `docs/CONTRACT.md` Section 1.7 |

<!-- sow-source-end -->

### CLM-030 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":43,"line_start":42,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-030"} -->
##### Examples

<!-- sow-source-end -->

### CLM-031 — Valid Anchor Row Shape

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":49,"line_start":44,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-031"} -->
###### Valid Anchor Row Shape

TBD: A concrete row fixture should be added during implementation. It must use `DependencyClass=ANCHOR`, `AnchorType=IMPLEMENTS_NODE` or `TRACES_TO_REQUIREMENT`, and `DependencyType=OTHER`.

Source: `docs/SPEC.md` Section 6.2.

<!-- sow-source-end -->

### CLM-032 — Valid Execution Row Shape

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":55,"line_start":50,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-032"} -->
###### Valid Execution Row Shape

TBD: A concrete row fixture should be added during implementation. It must use `DependencyClass=EXECUTION` and `AnchorType=NOT_APPLICABLE`.

Source: `docs/SPEC.md` Section 6.2.

<!-- sow-source-end -->

### CLM-033 — Unresolved Target

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":61,"line_start":56,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-033"} -->
###### Unresolved Target

If a dependency points to a deliverable that cannot be resolved to an existing stable deliverable ID, use `TargetType=UNKNOWN` and emit a warning instead of inventing a deliverable identity.

Source: `docs/CONTRACT.md` Section 1.7; `docs/TYPES.md` Section 6.5.

<!-- sow-source-end -->

### CLM-034 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":67,"line_start":62,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-034"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-DEL-07-05-001 | `_REFERENCES.md` records `docs/PRD.md` as `MATCH`, but PRD Section 8.9 is the local source for FR-055 through FR-057 acceptance language. | `_REFERENCES.md` Authoritative Source Corpus | `docs/PRD.md` Section 8.9 | Datasheet Attributes; Specification Requirements; Procedure Verification | Use PRD content as a source warning for drafting, then require human review before relying on PRD-derived claims as accepted hash truth. | TBD — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-035 — Pass 3 Human Rulings and Design Holds

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":77,"line_start":68,"source_sha256":"36a5624d137b9ec5b61c76913bb133e8916edadca427cd0df552914e168ab890","target_id":"CLM-035"} -->
##### Pass 3 Human Rulings and Design Holds

| ItemID | Guidance disposition |
|---|---|
| C-001 | Keep the warning vocabulary as a design hold. The sources warrant structured warnings, but they do not choose final warning codes; implementation should select stable categories before tests freeze them. |
| F-001 | Preserve the PRD hash conflict as a human ruling item. This P3 pass does not accept, refresh, or bypass the mismatched PRD hash. |
| D-001 | Keep implementation path and payload-type names out of prose until code ownership chooses them. Stable IDs and file contracts are authoritative; module paths are projections. |
| X-001 | Require evidence that API/MCP dependency operations and governed write hooks are tested together, because MCP is a transport and not a bypass of permission, hook, path, redaction, or event policy. |

Source rereads: `_REFERENCES.md` Authoritative Source Corpus; `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-MCP-1, K-HOOK-1, K-PATH-2, K-PATH-3, K-DEP-1, K-DEP-2, K-PROV-1, K-INVENT-1, and K-CONFLICT-1; `docs/SPEC.md` Sections 6, 14.2, 14.3, 15, and 17.2; `docs/PLAN.md` Optional and Retired Scope Status.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-029 OBJ-006 | CLM-010 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- pilot-variance: D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674 -->
