# Guidance: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

## Purpose

DEL-07-05 exists to make the dependency register contract executable: `Dependencies.csv` rows must be readable, writable, lintable, and warning-producing without weakening Chirality's plain-file, deliverable-local dependency model.

Sources: `_CONTEXT.md` (Deliverable Scope); `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (PKG-07 deliverable table); `docs/DIRECTIVE.md` Section 5.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Plain-file truth | Treat `_DEPENDENCIES.md` and `Dependencies.csv` as local, inspectable project state. Avoid hidden app state or external database assumptions. | `docs/DIRECTIVE.md` Section 5; `docs/CONTRACT.md` Section 1.7 |
| Schema preservation | Parse and write the complete v3.1 core schema, and carry extension columns forward without making them breaking changes. | `docs/SPEC.md` Section 6.1 |
| Lifecycle-aware rows | Retire rows instead of deleting them so dependency history remains auditable. | `docs/SPEC.md` Section 6.2; `docs/PRD.md` Section 10.9 |
| Evidence over plausibility | Preserve `EvidenceFile` and `SourceRef`; use `location TBD`, `TBD`, and explicit warnings instead of invented provenance. | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` Section 1.7 |
| Stable identifiers | Use stable package, deliverable, dependency, and target identifiers for identity. Paths are projections and may change. | `docs/CONTRACT.md` K-ID-1 and K-PATH-1 |
| Fail visibly | Invalid enum values, unresolved deliverables, missing provenance, and host identity mismatches should become structured errors or warnings rather than silent mutation. | `docs/PRD.md` Section 8.9; `docs/SPEC.md` Section 14.3 |
| Governed writes | Dependency writes should pass through the same path, permission, hook, redaction, and event logging policy as other governed tool writes. | `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14.2 and 15 |

## Considerations

- Reader design should separate syntactic CSV parsing from semantic validation. This keeps parse failures, schema warnings, enum errors, identity errors, and provenance warnings distinguishable.
- Writer design should be conservative: preserve existing column order where possible, preserve extension columns, normalize only source-authorized legacy forms, and retain retired rows.
- Linter output should be deterministic and stable enough for tests. ASSUMPTION: warning codes or categories should be stable once selected, but the exact code vocabulary is TBD.
- Target resolution should use stable deliverable IDs when available. If the target cannot be confidently resolved, the row should use `TargetType=UNKNOWN` rather than inventing a target.
- Provenance validation should distinguish active extracted rows from other row origins/statuses because the explicit provenance invariant applies to active extracted dependency rows.
- The `docs/PRD.md` source is useful but flagged `HASH_MISMATCH` in `_REFERENCES.md`; revalidate PRD-derived acceptance language during human review.
- Do not use this deliverable to reintroduce project-level dependency graph generation, deliverable locks, staleness propagation, or unified pipeline run records. `docs/PLAN.md` Section 9 identifies those as retired without amendment.

## Trade-offs

| Trade-off | Preferred Direction | Rationale |
|---|---|---|
| Strict failure vs warning | Fail hard on structural conditions that make the file unreadable or unsafe to write; warn for legacy/invalid data where the contract calls for warnings. | PRD FR-055 through FR-057 require validation and warnings; SPEC requires schema and row rules. |
| Normalization vs source preservation | Normalize only source-authorized legacy forms, such as missing `RegisterSchemaVersion` on write. Preserve other data and surface warnings. | `docs/SPEC.md` Section 6.2 authorizes version normalization; other normalizations need evidence. |
| Rich graph behavior vs scoped register tooling | Keep this slice focused on reader/writer/linter behavior. | `docs/PLAN.md` Section 9 keeps dependency linter behavior in scope while retiring broader graph/hardening scope. |
| API convenience vs file authority | APIs may expose snapshots and write operations, but file contents remain the authoritative project substrate. | `docs/DIRECTIVE.md` Section 5; `docs/CONTRACT.md` Section 1.7 |

## Examples

### Valid Anchor Row Shape

TBD: A concrete row fixture should be added during implementation. It must use `DependencyClass=ANCHOR`, `AnchorType=IMPLEMENTS_NODE` or `TRACES_TO_REQUIREMENT`, and `DependencyType=OTHER`.

Source: `docs/SPEC.md` Section 6.2.

### Valid Execution Row Shape

TBD: A concrete row fixture should be added during implementation. It must use `DependencyClass=EXECUTION` and `AnchorType=NOT_APPLICABLE`.

Source: `docs/SPEC.md` Section 6.2.

### Unresolved Target

If a dependency points to a deliverable that cannot be resolved to an existing stable deliverable ID, use `TargetType=UNKNOWN` and emit a warning instead of inventing a deliverable identity.

Source: `docs/CONTRACT.md` Section 1.7; `docs/TYPES.md` Section 6.5.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-DEL-07-05-001 | `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`, but PRD Section 8.9 is the local source for FR-055 through FR-057 acceptance language. | `_REFERENCES.md` Authoritative Source Corpus | `docs/PRD.md` Section 8.9 | Datasheet Attributes; Specification Requirements; Procedure Verification | Use PRD content as a source warning for drafting, then require human review before relying on PRD-derived claims as accepted hash truth. | TBD |

## Pass 3 Human Rulings and Design Holds

| ItemID | Guidance disposition |
|---|---|
| C-001 | Keep the warning vocabulary as a design hold. The sources warrant structured warnings, but they do not choose final warning codes; implementation should select stable categories before tests freeze them. |
| F-001 | Preserve the PRD hash conflict as a human ruling item. This P3 pass does not accept, refresh, or bypass the mismatched PRD hash. |
| D-001 | Keep implementation path and payload-type names out of prose until code ownership chooses them. Stable IDs and file contracts are authoritative; module paths are projections. |
| X-001 | Require evidence that API/MCP dependency operations and governed write hooks are tested together, because MCP is a transport and not a bypass of permission, hook, path, redaction, or event policy. |

Source rereads: `_REFERENCES.md` Authoritative Source Corpus; `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-MCP-1, K-HOOK-1, K-PATH-2, K-PATH-3, K-DEP-1, K-DEP-2, K-PROV-1, K-INVENT-1, and K-CONFLICT-1; `docs/SPEC.md` Sections 6, 14.2, 14.3, 15, and 17.2; `docs/PLAN.md` Optional and Retired Scope Status.
