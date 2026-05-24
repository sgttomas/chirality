# Dependencies: DEL-01-04 Scope Boundary and Retired Scope Register

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
- 2026-05-20 dependency-extract run:
  - Runtime overrides: `SCOPE=DEL-01-04`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
  - Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used.
  - Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority.
  - `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`; execution docs were read as `Procedure.md`, `Specification.md`, `Guidance.md`, `_CONTEXT.md`, `_REFERENCES.md`.
  - Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
  - Existing declared dependency lists remain `TBD`; no declared edges were promoted without evidence.
  - `[WARNING] SOURCE_HASH_MISMATCH`: `_REFERENCES.md` reports `docs/PRD.md` REF-006 as `HASH_MISMATCH`; this run preserved the warning and used only the allowed local derivative documents plus decomposition authority.
  - `[WARNING] HUMAN_RULING_TBD`: `Guidance.md` contains conflict-table rulings with `Human ruling (TBD)`; no dependency edge depends on those unresolved rulings.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-01-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-01 Product Governance and Reliance Boundaries | ACTIVE |
| DEP-01-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-065 Remote MCP/plugins out of current scope | ACTIVE |
| DEP-01-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-076 Ambient settings and shipped bypass forbidden | ACTIVE |
| DEP-01-04-004 | ANCHOR | OTHER | UPSTREAM | SOW-077 Retired PKG-08 scope remains retired | ACTIVE |
| DEP-01-04-005 | ANCHOR | OTHER | UPSTREAM | SOW-078 Windows/Linux packaging out of scope | ACTIVE |
| DEP-01-04-006 | ANCHOR | OTHER | UPSTREAM | OBJ-009 Professional boundary and reliance-boundary ownership | ACTIVE |
| DEP-01-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | `_CONTEXT.md` | ACTIVE |
| DEP-01-04-008 | EXECUTION | PREREQUISITE | UPSTREAM | `_REFERENCES.md` | ACTIVE |
| DEP-01-04-009 | EXECUTION | PREREQUISITE | UPSTREAM | Decomposition v3.2 | ACTIVE |
| DEP-01-04-010 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-04-02 SdkOptionsBuilder and Settings Isolation | ACTIVE |
| DEP-01-04-011 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-07-06 Reference Hash and Snapshot Conventions | ACTIVE |
| DEP-01-04-012 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-09-04 macOS DMG Packaging and Instruction Root Integrity | ACTIVE |
| DEP-01-04-013 | EXECUTION | CONSTRAINT | DOWNSTREAM | PKG-10 Domain Engine Future Boundary | ACTIVE |

## Lifecycle Summary

| Metric | Count |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 13 |
| RETIRED rows | 0 |
| ANCHOR rows | 6 |
| EXECUTION rows | 7 |
| OTHER rows | 6 |
| PREREQUISITE rows | 3 |
| CONSTRAINT rows | 4 |
| `SatisfactionStatus=PENDING` | 13 |

Closure state: dependency register schema is present and all extracted rows are ACTIVE; satisfaction remains `PENDING` until downstream closure/audit workflows accept or waive the edges.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:24:28-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH; HUMAN_RULING_TBD | ANCHOR=6; EXECUTION=7; TOTAL=13 |
