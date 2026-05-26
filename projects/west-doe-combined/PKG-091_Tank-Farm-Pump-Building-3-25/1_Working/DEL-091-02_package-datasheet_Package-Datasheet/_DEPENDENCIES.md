# Dependencies: DEL-091-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted by `dependency-extract` skill on 2026-05-26. Total ACTIVE rows: 10.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-091-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-091 | Tank Farm Pump Building 3-25 | HIGH | ACTIVE |
| DEP-091-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0185 | SOW-0185 Scope Item | HIGH | ACTIVE |
| DEP-091-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0186 | SOW-0186 Scope Item | HIGH | ACTIVE |
| DEP-091-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0187 | SOW-0187 Scope Item | HIGH | ACTIVE |
| DEP-091-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0188 | SOW-0188 Scope Item | HIGH | ACTIVE |
| DEP-091-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | OBJ-002 Objective (range OBJ-002..OBJ-010) | MEDIUM | ACTIVE |
| DEP-091-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-091-01 | EPC Scope of Work (DEL-091-01) | HIGH | ACTIVE |
| DEP-091-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-091-04 | Vendor Engineered Equipment Package (DEL-091-04) | HIGH | ACTIVE |
| DEP-091-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 | GATE-07 Final Published PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-091-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | INTERFACE_REGISTER | INTERFACE_REGISTER.csv (PKG-091 rows) | HIGH | ACTIVE |

**Note on OBJ-002..OBJ-010 objective traces:** The Identification block states "Supports Objectives: OBJ-002 … OBJ-010". A single representative trace row (DEP-091-02-006) is emitted for the range; the full set of objectives OBJ-002 through OBJ-010 is confirmed against the GATE-07 objective register (10 objectives total in project). CONSERVATIVE strictness: one row per explicit range reference rather than expanding to 9 individual rows without per-objective evidence. The row uses MEDIUM confidence to reflect the range notation.

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **ANCHOR_DOC (Pass 1):** `Datasheet.md` (matched heuristic: filename contains `datasheet`)
- **EXECUTION_DOC_ORDER (Pass 2):** `Guidance.md`, `Specification.md`, `Procedure.md` (AUTO ordering: guidance/spec/procedure by content relevance)
- **SOURCE_DOCS scanned:** `Datasheet.md`, `Guidance.md`, `Specification.md`, `Procedure.md`
- **DECOMPOSITION_PATH resolved:** `DECOMPOSITION_PATH` provided as `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — this exact path does not exist on disk. Resolved via `_REFERENCES.md` and existing `_DEPENDENCIES.md` Run Notes to: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Decomposition document confirmed accessible. This resolution is non-blocking.
- **Decomposition validation:** PKG-091 confirmed in GATE-07 snapshot (PROJECT_DECOMP.md + PACKAGE_REGISTER.csv context); OBJ-002 and OBJ-010 confirmed explicitly in PROJECT_DECOMP.md objective table; SOW-0185..SOW-0188 confirmed via SCOPE_LEDGER.csv reference in snapshot companion inventory. DEL-091-01 and DEL-091-04 IDs are consistent with package folder naming conventions (DEL-091-01_scope-of-work, DEL-091-04 visible from Specification.md and Guidance.md cross-references) but were not directly row-verified in DELIVERABLE_REGISTER.csv — TargetDeliverableID values recorded as-stated from source documents (FACT: stated in source; ASSUMPTION: ID format matches project convention).
- **Tree x DAG integrity:** 1 ACTIVE ANCHOR row with AnchorType=IMPLEMENTS_NODE (DEP-091-02-001). Parent anchor check: PASS.
- **No [WARNING] FLOATING_NODE** — parent anchor present.
- **No [WARNING] AMBIGUOUS_ANCHOR** — exactly one IMPLEMENTS_NODE row.
- **No [WARNING] MISSING_DECOMPOSITION** — decomposition resolved (path corrected from brief; see above).

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 6 |
| EXECUTION | 4 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First EXTRACTED run via `dependency-extract` skill (MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). 10 rows extracted (6 ANCHOR, 4 EXECUTION). Decomposition path resolved from brief hint to GateSnapshot location. Schema validation: VALID.
