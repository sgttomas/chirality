# Dependencies: DEL-018-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract repair run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated for the previously-missing dependency extract on 2026-05-26.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-018-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0019 | Scope decision SOW-0019 — MV VFD 5000HP 4160V WBS 02 | HIGH | ACTIVE |
| DEP-018-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-018-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package responsibility model | HIGH | ACTIVE |
| DEP-018-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power and equipment basis | HIGH | ACTIVE |
| DEP-018-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation and communications | HIGH | ACTIVE |
| DEP-018-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site and construction support | HIGH | ACTIVE |
| DEP-018-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety regulatory codes and standards | HIGH | ACTIVE |
| DEP-018-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability turnover closure | HIGH | ACTIVE |
| DEP-018-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-018-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Workbook Packages row 20 — 26020-Packages_Interfaces_4_export | HIGH | ACTIVE |
| DEP-018-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 3-25 Compressor and Liquids DBM electrical source slices | HIGH | ACTIVE |
| DEP-018-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 4-25 Deepcut DBM electrical source slices | HIGH | ACTIVE |
| DEP-018-01-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | — | Package Vendor VFD design data | MEDIUM | ACTIVE |
| DEP-018-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-018-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-018-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-018-03_construction-work-package | Construction Work Package | MEDIUM | ACTIVE |

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE (first extracted run; no previous `Dependencies.csv`)
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs scanned:** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`, existing `_DEPENDENCIES.md`
- **Anchor doc:** `Datasheet.md` (identity, scope item, objectives)
- **Execution docs:** `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- **Pass 1 (ANCHOR):** SOW-0019 and objectives OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 are explicit in `Datasheet.md` and `_CONTEXT.md`.
- **Pass 2 (EXECUTION):** Prerequisite rows were extracted only from explicit source-basis requirements: Gate 7 registers, workbook row 20, the two DBM electrical source files, and deferred package-vendor VFD design data. Downstream rows were limited to `DEL-018-02` and `DEL-018-03` where the source documents support a handoff/enabling relationship.
- **Conservative exclusions:** No rows were emitted for pure coordination statements, package adjacency alone, or unconfirmed tag association to KM-2150/KM-2250.
- **Tree integrity:** one `IMPLEMENTS_NODE` anchor found. No `[WARNING] FLOATING_NODE`. No `[WARNING] AMBIGUOUS_ANCHOR`. Decomposition snapshot was found.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 10 |
| SATISFIED | 4 |
| PENDING | 1 |

| DependencyClass | ACTIVE count |
|---|---:|
| ANCHOR | 8 |
| EXECUTION | 7 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — Dependency extract repair run for missing PKG-018 artifacts; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Wrote 15 ACTIVE rows to `Dependencies.csv`; no RETIRED rows; no integrity warnings.
