# Dependencies: DEL-10-02 Protected Path and Proposal Path Policy

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract run on 2026-05-20 used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Source documents scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Anchor doc selected: `Datasheet.md`.
- Execution doc order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: available at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Future-boundary warning: PKG-10 is gated; extracted rows do not activate domain-engine work or current-release domain operation execution.
- Source warning: `_REFERENCES.md` reports REF-006 `docs/PRD.md` hash mismatch; retained as a source warning only and not used to invent edges.
- Unknowns preserved: concrete protected/proposal path glob syntax, exact hook API, and adapter manifest behavior remain `TBD`/`UNKNOWN`.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-DEL-10-02-001 | ANCHOR | OTHER | UPSTREAM | SOW-068 | ACTIVE | `Datasheet.md` §Identification |
| DEP-DEL-10-02-002 | ANCHOR | OTHER | UPSTREAM | OBJ-010 | ACTIVE | `Datasheet.md` §Identification |
| DEP-DEL-10-02-003 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-10-01 | ACTIVE | `Datasheet.md` §Conditions |
| DEP-DEL-10-02-004 | EXECUTION | INTERFACE | UPSTREAM | DEL-10-03 | ACTIVE | `Specification.md` §Requirements DEL-10-02-REQ-006 |
| DEP-DEL-10-02-005 | EXECUTION | CONSTRAINT | UPSTREAM | UNKNOWN / TBD | ACTIVE | `Procedure.md` §Steps step 6 |

### Counts

| Dimension | Value | Count |
|---|---|---:|
| DependencyClass | ANCHOR | 2 |
| DependencyClass | EXECUTION | 3 |
| DependencyType | OTHER | 2 |
| DependencyType | PREREQUISITE | 1 |
| DependencyType | INTERFACE | 1 |
| DependencyType | CONSTRAINT | 1 |
| Status | ACTIVE | 5 |
| Status | RETIRED | 0 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 5 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 2 |
| TBD | 3 |

## Run History

| Timestamp | Mode | Strictness | Decomposition | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T21:07:20-0600 | UPDATE | CONSERVATIVE | available | 5 | REF-006 hash mismatch; future-boundary/gated scope; concrete path and hook details TBD |
