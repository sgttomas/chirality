# Dependencies: DEL-02-01 Desktop Shell and Matrix Navigation

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted declared dependency edges have been provided.

## Declared Downstream

TBD - no accepted declared dependency edges have been provided.

## Extracted Dependency Register

Summary:

| Count Type | Value |
|---|---:|
| Total rows | 8 |
| ACTIVE rows | 8 |
| RETIRED rows | 0 |
| ANCHOR rows | 4 |
| EXECUTION rows | 4 |

Compact register:

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-02-01-001 | ANCHOR | OTHER | UPSTREAM | PKG-02 Desktop Shell, Navigation, and Operator State | ACTIVE |
| DEP-02-01-002 | ANCHOR | OTHER | UPSTREAM | SOW-001 Desktop shell with main navigation. | ACTIVE |
| DEP-02-01-003 | ANCHOR | OTHER | UPSTREAM | SOW-005 Matrix rendering and routing. | ACTIVE |
| DEP-02-01-004 | ANCHOR | OTHER | UPSTREAM | OBJ-001 Governed local desktop harness objective | ACTIVE |
| DEP-02-01-005 | EXECUTION | PREREQUISITE | UPSTREAM | UNKNOWN/TBD existing implementation workspace | ACTIVE |
| DEP-02-01-006 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-08-02 Persona Alias and Agent Matrix Routing Contract | ACTIVE |
| DEP-02-01-007 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-02-02 Workbench and Pipeline Selection UX | ACTIVE |
| DEP-02-01-008 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-08-03 Pipeline Category and Task Scope Dispatch | ACTIVE |

## Run Notes

- Runtime overrides: `SCOPE=DEL-02-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- `_SEMANTIC.md` was not read or consumed. Semantic lensing and P3 enrichment were skipped by human ruling.
- Anchor doc selection: `Datasheet.md`, supplemented by `_CONTEXT.md` and decomposition validation.
- Execution doc order: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.
- No declared edges were found in the existing dependency index; all register rows in this run are `Origin=EXTRACTED`.
- Parent anchor check: PASS. Exactly one ACTIVE `IMPLEMENTS_NODE` row exists.
- Schema validation: PASS. `validate_dependencies_schema.py` reported 29 required columns and 8 data rows.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records `REF-006` with `Status=HASH_MISMATCH`; treated as a source warning, not a blocker, per local source instructions.
- [WARNING] PACKAGE_PATH_MISMATCH: `Guidance.md` records a package path mismatch requiring later human ruling; this run wrote only inside the assigned `ScopePath`.
- [WARNING] ROUTE_SEMANTICS_SOURCE_POINTER: `Guidance.md` records an unresolved PRD/SPEC/TYPES source-pointer issue; dependency extraction used only concrete local evidence and preserved open ruling status.
- [WARNING] UNKNOWN_IMPLEMENTATION_WORKSPACE: `Procedure.md` requires an implementation workspace, but exact implementation paths are `TBD`; row `DEP-02-01-005` preserves `TargetType=UNKNOWN`.

## Run History

| Timestamp | Mode | Strictness | Decomposition Path | Decomposition Status | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|---|
| 2026-05-20T19:24:24-06:00 | UPDATE | CONSERVATIVE | `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | FOUND | PRD_HASH_MISMATCH; PACKAGE_PATH_MISMATCH; ROUTE_SEMANTICS_SOURCE_POINTER; UNKNOWN_IMPLEMENTATION_WORKSPACE | ANCHOR=4; EXECUTION=4; TOTAL=8 |

## Lifecycle Summary

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 8 |
| Status | RETIRED | 0 |
| SatisfactionStatus | NOT_APPLICABLE | 4 |
| SatisfactionStatus | TBD | 4 |
| DependencyType | OTHER | 4 |
| DependencyType | PREREQUISITE | 1 |
| DependencyType | HANDOVER | 1 |
| DependencyType | INTERFACE | 2 |
| DependencyClass | ANCHOR | 4 |
| DependencyClass | EXECUTION | 4 |

