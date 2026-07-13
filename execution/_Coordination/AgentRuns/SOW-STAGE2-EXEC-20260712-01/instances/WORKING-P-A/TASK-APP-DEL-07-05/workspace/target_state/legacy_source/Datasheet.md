# Datasheet: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

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

## Attributes

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

## Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root containment | Dependency tools are subject to project-root containment and write-hook policy | `docs/SPEC.md` Sections 14.3 and 15.2; `docs/CONTRACT.md` Section 1.6 |
| Instruction-root protection | Runtime writes to the instruction root are blocked | `docs/SPEC.md` Section 15.2; `docs/PRD.md` Section 8.8 |
| Dependency authority | Deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` are authoritative for dependencies; aggregation is on demand | `docs/CONTRACT.md` Section 1.7; `docs/DIRECTIVE.md` Section 5 |
| Provenance requirement | Active extracted rows require `EvidenceFile` plus `SourceRef`, or explicit `location TBD` | `docs/CONTRACT.md` Section 1.7; `docs/PRD.md` Section 8.9 |
| Unknown handling | Unknowns remain `TBD`; unresolvable targets use `TargetType=UNKNOWN` | `docs/CONTRACT.md` Section 1.7; `docs/TYPES.md` Section 6.5 |
| Lifecycle behavior | Rows are retired, not deleted; `FirstSeen`, `LastSeen`, `Status`, and `SatisfactionStatus` track extraction and closure state | `docs/SPEC.md` Section 6.2; `docs/PRD.md` Section 10.9 |

## Construction

### Core Schema Columns

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

### Enum Vocabulary

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

## References

- `docs/SPEC.md` Sections 3, 5, 6, 14.2, 14.3, and 15.2.
- `docs/TYPES.md` Section 6.
- `docs/CONTRACT.md` Section 1.7.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- `docs/DIRECTIVE.md` Sections 2.5 and 5.
- `docs/PLAN.md` R4 target slice and Optional/Retired Scope Status.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-07 deliverable table and Scope Ledger SOW-029.

## Pass 3 Semantic Lensing Notes

| ItemID | Datasheet disposition |
|---|---|
| C-001 | Converted to a named TBD: the warning output must remain structured and deterministic, but the exact warning code/category taxonomy is not selected by the accessible sources. |
| F-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| D-001 | Converted to implementation slots: module names, API handler names, fixture paths, payload type names, and test paths remain TBD until local code ownership selects them. |
| X-001 | Converted to acceptance-evidence slots: API/MCP dependency payload evidence and governed write-hook evidence remain required, with final artifact paths TBD. |

Source rereads for these notes: `_SEMANTIC_LENSING.md` current warranted rows; `docs/SPEC.md` Sections 6, 14.2, 14.3, 15.1, 15.2, and 17.2; `docs/CONTRACT.md` Sections 1.6 and 1.7; `docs/PRD.md` Sections 8.9, 10.9, and 17.2; `_REFERENCES.md` Authoritative Source Corpus.
