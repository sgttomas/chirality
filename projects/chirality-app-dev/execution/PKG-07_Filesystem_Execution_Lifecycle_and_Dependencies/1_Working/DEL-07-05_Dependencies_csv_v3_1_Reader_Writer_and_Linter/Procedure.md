# Procedure: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

Define the operating workflow for producing and verifying the DEL-07-05 backend slice: a `Dependencies.csv` v3.1 reader, writer, and linter that preserves schema, provenance, lifecycle behavior, and warnings.

Sources: `_CONTEXT.md` (Deliverable Scope and Anticipated Artifacts); `docs/SPEC.md` Section 6; `docs/PRD.md` Section 8.9.

## Prerequisites

| Prerequisite | Status / Note | Source |
|---|---|---|
| Accepted source references are available | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` — reconciled under D-APP-38 |
| v3.1 schema and enum vocabulary are known | Defined in SPEC and TYPES. | `docs/SPEC.md` Section 6; `docs/TYPES.md` Section 6 |
| Dependency authority model is known | Deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` are authoritative; aggregation is on demand. | `docs/CONTRACT.md` Section 1.7 |
| Working-root write policy is known | Governed writes require containment, instruction-root protection, symlink rejection, and hook/provenance behavior. | `docs/SPEC.md` Section 15 |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` has no accepted dependency edges yet. | `_DEPENDENCIES.md` |
| Declared downstream dependencies | TBD - `_DEPENDENCIES.md` has no accepted dependency edges yet. | `_DEPENDENCIES.md` |

## Steps

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

## Verification

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

## Records

Expected records from implementation:

- Dependency parser/writer source files. Exact paths TBD.
- Linter test suite and fixtures. Exact paths TBD.
- Provenance fixtures showing valid source citation and `location TBD` behavior.
- API/MCP tests or integration evidence for dependency read/write contract surfaces.
- Review note confirming `docs/PRD.md` hash status: MATCH was considered before accepting PRD-derived requirements. (reconciled under D-APP-38).

## Pass 3 Worklist Disposition

| ItemID | Procedure disposition | Required follow-through |
|---|---|---|
| C-001 | Converted to TBD. | Select and document stable warning categories or codes before locking tests for reader, writer, linter, API, and MCP warning output. |
| F-001 | Already surfaced as conflict. | Preserve `_REFERENCES.md` PRD `MATCH` in review evidence or refresh/accept the PRD hash through the appropriate human-governed path. — reconciled under D-APP-38 |
| D-001 | Converted to implementation-location slots. | Record final module names, API handler names, MCP wrapper names, payload type names, fixture paths, and test paths in implementation evidence once selected. |
| X-001 | Converted to acceptance-evidence slots. | Record API/MCP dependency read-write payload evidence and governed write-hook evidence, including containment, instruction-root rejection, symlink-write rejection, provenance/event hooks, extension-column preservation, retired-row retention, and warning behavior. |

Source rereads: `docs/SPEC.md` Sections 6, 14.2, 14.3, 15.1, 15.2, and 17.2; `docs/CONTRACT.md` Sections 1.6 and 1.7; `docs/PRD.md` Sections 8.9 and 10.9 plus implementation targets; `docs/TYPES.md` Section 6; `docs/PLAN.md` Section 9.
